import os
import logging
import prometheus_client as prom_client
import tornado.ioloop
import tornado.web
import json
import _thread
import time
import sys
import hashlib
import binascii
import socket
import traceback


isRunning=True
fileAccess='OK'
fileAccessDuration=None

class ConfigManager:
    def __init__(self):
        self.hostname=str(os.getenv('HOST_NAME',socket.gethostname()))
        self.prefix=str(os.getenv('PREFIX','fmarslan_'))
        self.port=int(os.getenv('PORT', 8080))
        self.fileSize=int(os.getenv('FILE_SIZE',8))
        self.fileName=str(os.getenv('FILE_NAME','/tmp/check.tmp'))
        self.logLevel=str(os.getenv('LOG_LEVEL','INFO'))
        self.logFormat=str(os.getenv('LOG_FORMAT','{ \'level\': \'%(levelname)s\', \'message\':\'%(message)s\'}'))
        self.interval=int(os.getenv('CHECK_INTERVAL',1))
    def asJson(self):
        jsonConfig='{{"port":{0},"fileSize":"{1} Bytes","fileName":"{2}","logLevel":"{3}", "logFormat":"{4}","interval":"{5} s", "prefix":"{6}", "hostname":"{7}"}}'.format(self.port, self.fileSize, self.fileName, self.logLevel,self.logFormat, self.interval,self.prefix,self.hostname)
        return jsonConfig

logger = logging.getLogger("diskcheck")
Config = ConfigManager()
logging.basicConfig(format=Config.logFormat, level=Config.logLevel)
wrHist = prom_client.Histogram(Config.prefix + 'write_read_duration_nanoseconds', 'Duration of Write/Read process in nanoseconds',['process','host'])

errCount= prom_client.Counter(Config.prefix + 'write_read_error_count', 'Number of Write/Read Error',['process','host'])
serviceState= prom_client.Enum(Config.prefix + 'write_read_service_state', 'State of Write/Read Service',['host'],states=['RUNNING', 'STOPPED'])
diskState= prom_client.Enum(Config.prefix + 'write_read_disk_state', 'State of Write/Read Service',['host'],states=['OK', 'NOT ACCESS'])


def check():
    global fileAccess
    global fileAccessDuration
    global isRunning
    try:
        if Config.interval==-1:
            isRunning=False
        else:
            time.sleep(Config.interval)
        serviceState.labels(host=Config.hostname).state('RUNNING')
        content = os.urandom(Config.fileSize)
        read_content = []
        _timerStart = time.perf_counter_ns()
        with wrHist.labels(process="write",host=Config.hostname).time():
            with errCount.labels(process="write",host=Config.hostname).count_exceptions():
                with open(Config.fileName,'wb') as fout:
                    fout.write(content)
        with wrHist.labels(process="read",host=Config.hostname).time():
            with errCount.labels(process="read",host=Config.hostname).count_exceptions():
                with open(Config.fileName,'rb') as fin:
                    read_content = fin.read()
        if(hashlib.sha256(read_content).hexdigest()==hashlib.sha256(content).hexdigest()):
            logger.debug(read_content)
            fileAccess='OK'
            fileAccessDuration=time.perf_counter_ns()-_timerStart
        else:
            logger.error(read_content)
            fileAccess='NOT ACCESS'
            fileAccessDuration=-1
            wrHist.labels(process="read",host=Config.hostname).observe(-1)
            errCount.labels(process="equality",host=Config.hostname).inc() 
    except:
        logger.error(traceback.format_exc())
        fileAccess='NOT ACCESS'
        fileAccessDuration=-1
    finally:
        diskState.labels(host=Config.hostname).state(fileAccess)


def start_check():
    def _check():
        while isRunning:
            check()
        serviceState.labels(host=Config.hostname).state('STOPPED')
    _thread.start_new_thread( _check,() )



class MainHandler(tornado.web.RequestHandler):
    async def get(self,slug):
        global isRunning
        if slug=='metrics':
            self.write(prom_client.generate_latest(prom_client.REGISTRY))
            self.set_header("Content-Type", prom_client.CONTENT_TYPE_LATEST)
            self.set_status(200)
        else:
            header = "Content-Type"
            body = "application/json"
            self.set_header(header, body)
            self.set_status(200 if fileAccess=='OK' else 500)
            if slug=='stop':
                isRunning=False
                self.write('{ "service": "PASSIVE" }')
            elif slug=='start':
                if(isRunning!=True):
                    start_check()
                    isRunning=True
                self.write('{ "service": "ACTIVE" }')
            elif slug=='config':
                self.write(Config.asJson())
            elif slug=='check':
                isRunning=True
                check()
                serviceState.labels(host=Config.hostname).state('STOPPED')
                self.set_status(200 if fileAccess=='OK' else 500)
                self.write('{ "service":"' + str('ACTIVE' if isRunning else 'PASSIVE') + '", "status":"'+ fileAccess +'", "duration":' +str(fileAccessDuration)+ ' }')
            else :
                self.write('{ "service":"' + str('ACTIVE' if isRunning else 'PASSIVE') + '", "status":"'+ fileAccess +'", "duration":' +str(fileAccessDuration)+ ' }')
        self.finish()

def run():
    global isRunning
    logging.info(Config.asJson())
    logging.info('RUNNING...')

    app = tornado.web.Application([
        (r"/([^/]*)", MainHandler),
    ])
    app.listen(Config.port)
    start_check()
    tornado.ioloop.IOLoop.current().start()
    isRunning=False

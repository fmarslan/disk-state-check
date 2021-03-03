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

isRunning=True
fileAccess='OK'
fileAccessDuration=None

class ConfigManager:
    def __init__(self):
        self.port=int(os.getenv('PORT', 8080))
        self.fileSize=int(os.getenv('FILE_SIZE',8))
        self.fileName=str(os.getenv('FILE_NAME','/tmp/check.tmp'))
        self.logLevel=str(os.getenv('LOG_LEVEL','INFO'))
        self.logFormat=os.getenv('LOG_FORMAT','{ \'level\': \'%(levelname)s\', \'message\':\'%(message)s\'}')
        self.interval=os.getenv('CHECK_INTERVAL',1)
    def asJson(self):
        jsonConfig='{{"port":{0},"fileSize":"{1} Bytes","fileName":"{2}","logLevel":"{3}","interval":"{4} s"}}'.format(self.port, self.fileSize, self.fileName, self.logLevel, self.interval)
        return jsonConfig

logger = logging.getLogger("diskcheck")
Config = ConfigManager()
logging.basicConfig(format=Config.logFormat, level=Config.logLevel)
wrHist = prom_client.Histogram('write_read_latency_nanoseconds', 'Duration of Write/Read process in nanoseconds',['process'])

def start_check():
    def check():
        global fileAccess
        global fileAccessDuration
        while isRunning:
           # try:
            time.sleep(Config.interval)
            content = os.urandom(Config.fileSize)
            read_content = []
            _timerStart = time.perf_counter_ns()
            with wrHist.labels("write").time():
                with open(Config.fileName,'wb') as fout:
                    fout.write(content)
            with wrHist.labels("read").time():
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
            """ except:
                logger.error(sys.exc_info())
                fileAccess='NOT ACCESS'
                fileAccessDuration=-1 """
    _thread.start_new_thread( check,() )

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
                isRunning=True
                start_check()
                self.write('{ "service": "ACTIVE" }')
            elif slug=='config':
                self.write(Config.asJson())
            else :
                self.write('{ "service":"' + str('ACTIVE' if isRunning else 'PASSIVE') + '", "status":"'+ fileAccess +'", "latency":' +str(fileAccessDuration)+ ' }')
        self.finish()

def run():
    logging.info(Config.asJson())
    logging.info('RUNNING...')

    app = tornado.web.Application([
        (r"/([^/]*)", MainHandler),
    ])
    app.listen(Config.port)
    start_check()
    tornado.ioloop.IOLoop.current().start()
    isRunning=False

run()

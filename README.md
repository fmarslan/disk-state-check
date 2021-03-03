# disk-state-check
Duration of Write/Read process in nanoseconds


Configuration

```sh
 HOST_NAME: xxx # os hostname as default
 PREFIX: fmarslan_
 PORT:8080
 FILE_SIZE:8  # bytes
 FILE_NAME: '/tmp/check.tmp'
 LOG_LEVEL:INFO # INFO,DEBUG,ERROR,WARNING
 LOG_FORMAT: '{ \'level\': \'%(levelname)s\', \'message\':\'%(message)s\'}'
 CHECK_INTERVAL:1 # seconds
```

URLs

### Prometheus

http://localhost:8080/metrics 

### Service Start

http://localhost:8080/start

### Service Stop

http://localhost:8080/stop


### Service State

http://localhost:8080/

### Config Info

http://localhost:8080/config

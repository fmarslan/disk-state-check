# disk-state-check
Duration of Write/Read process in nanoseconds


## Configuration

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

## URLs

### Prometheus

http://localhost:8080/metrics 

```properties
   # HELP python_gc_objects_collected_total Objects collected during gc
   # TYPE python_gc_objects_collected_total counter
   python_gc_objects_collected_total{generation="0"} 130.0
   python_gc_objects_collected_total{generation="1"} 184.0
   python_gc_objects_collected_total{generation="2"} 0.0
   # HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
   # TYPE python_gc_objects_uncollectable_total counter
   python_gc_objects_uncollectable_total{generation="0"} 0.0
   python_gc_objects_uncollectable_total{generation="1"} 0.0
   python_gc_objects_uncollectable_total{generation="2"} 0.0
   # HELP python_gc_collections_total Number of times this generation was collected
   # TYPE python_gc_collections_total counter
   python_gc_collections_total{generation="0"} 59.0
   python_gc_collections_total{generation="1"} 5.0
   python_gc_collections_total{generation="2"} 0.0
   # HELP python_info Python platform information
   # TYPE python_info gauge
   python_info{implementation="CPython",major="3",minor="8",patchlevel="5",version="3.8.5"} 1.0
   # HELP process_virtual_memory_bytes Virtual memory size in bytes.
   # TYPE process_virtual_memory_bytes gauge
   process_virtual_memory_bytes 1.1055104e+08
   # HELP process_resident_memory_bytes Resident memory size in bytes.
   # TYPE process_resident_memory_bytes gauge
   process_resident_memory_bytes 2.6464256e+07
   # HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
   # TYPE process_start_time_seconds gauge
   process_start_time_seconds 1.6147898884e+09
   # HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
   # TYPE process_cpu_seconds_total counter
   process_cpu_seconds_total 3.76
   # HELP process_open_fds Number of open file descriptors.
   # TYPE process_open_fds gauge
   process_open_fds 49.0
   # HELP process_max_fds Maximum number of open file descriptors.
   # TYPE process_max_fds gauge
   process_max_fds 8192.0
   # HELP fmarslan_write_read_latency_nanoseconds Duration of Write/Read process in nanoseconds
   # TYPE fmarslan_write_read_latency_nanoseconds histogram
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.005",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.01",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.025",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.05",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.075",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.1",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.25",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.5",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.75",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="1.0",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="2.5",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="5.0",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="7.5",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="10.0",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="+Inf",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_count{host="fmarslan",process="write"} 5534.0
   fmarslan_write_read_latency_nanoseconds_sum{host="fmarslan",process="write"} 2.003383567556739
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.005",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.01",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.025",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.05",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.075",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.1",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.25",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.5",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="0.75",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="1.0",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="2.5",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="5.0",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="7.5",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="10.0",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_bucket{host="fmarslan",le="+Inf",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_count{host="fmarslan",process="read"} 5534.0
   fmarslan_write_read_latency_nanoseconds_sum{host="fmarslan",process="read"} 0.501490727183409
   # HELP fmarslan_write_read_latency_nanoseconds_created Duration of Write/Read process in nanoseconds
   # TYPE fmarslan_write_read_latency_nanoseconds_created gauge
   fmarslan_write_read_latency_nanoseconds_created{host="fmarslan",process="write"} 1.6147898903187342e+09
   fmarslan_write_read_latency_nanoseconds_created{host="fmarslan",process="read"} 1.6147898903194366e+09
```


### Service Start

http://localhost:8080/start


```json
  {
    "service": "ACTIVE"
  }
```



### Service Stop

http://localhost:8080/stop

```json
  {
    "service": "PASSIVE"
  }
```


### Service State

http://localhost:8080/

```json
  {
    "service": "ACTIVE",
    "status": "OK",
    "latency": 598194
  }
```

### Config Info

http://localhost:8080/config

```json
  {
    "port": 8080,
    "fileSize": "8 Bytes",
    "fileName": "/tmp/check.tmp",
    "logLevel": "INFO",
    "logFormat": "{ 'level': '%(levelname)s', 'message':'%(message)s'}",
    "interval": "1 s",
    "prefix": "fmarslan_",
    "hostname": "fmarslan"
  }
```

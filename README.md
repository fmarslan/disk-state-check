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
 CHECK_INTERVAL:1 # seconds. if the value is -1, auto-check service will be PASSIVE
```

## URLs

### Prometheus

http://localhost:8080/metrics 

```properties
   # HELP python_gc_objects_collected_total Objects collected during gc
   # TYPE python_gc_objects_collected_total counter
   python_gc_objects_collected_total{generation="0"} 134.0
   python_gc_objects_collected_total{generation="1"} 184.0
   python_gc_objects_collected_total{generation="2"} 0.0
   # HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
   # TYPE python_gc_objects_uncollectable_total counter
   python_gc_objects_uncollectable_total{generation="0"} 0.0
   python_gc_objects_uncollectable_total{generation="1"} 0.0
   python_gc_objects_uncollectable_total{generation="2"} 0.0
   # HELP python_gc_collections_total Number of times this generation was collected
   # TYPE python_gc_collections_total counter
   python_gc_collections_total{generation="0"} 57.0
   python_gc_collections_total{generation="1"} 5.0
   python_gc_collections_total{generation="2"} 0.0
   # HELP python_info Python platform information
   # TYPE python_info gauge
   python_info{implementation="CPython",major="3",minor="8",patchlevel="5",version="3.8.5"} 1.0
   # HELP process_virtual_memory_bytes Virtual memory size in bytes.
   # TYPE process_virtual_memory_bytes gauge
   process_virtual_memory_bytes 1.10153728e+08
   # HELP process_resident_memory_bytes Resident memory size in bytes.
   # TYPE process_resident_memory_bytes gauge
   process_resident_memory_bytes 2.5632768e+07
   # HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
   # TYPE process_start_time_seconds gauge
   process_start_time_seconds 1.61486219784e+09
   # HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
   # TYPE process_cpu_seconds_total counter
   process_cpu_seconds_total 0.2
   # HELP process_open_fds Number of open file descriptors.
   # TYPE process_open_fds gauge
   process_open_fds 47.0
   # HELP process_max_fds Maximum number of open file descriptors.
   # TYPE process_max_fds gauge
   process_max_fds 8192.0
   # HELP fmarslan_write_read_duration_nanoseconds Duration of Write/Read process in nanoseconds
   # TYPE fmarslan_write_read_duration_nanoseconds histogram
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.005",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.01",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.025",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.05",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.075",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.1",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.25",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.5",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.75",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="1.0",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="2.5",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="5.0",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="7.5",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="10.0",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="+Inf",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_count{host="fmarslan",process="write"} 30.0
   fmarslan_write_read_duration_nanoseconds_sum{host="fmarslan",process="write"} 0.012958522769622505
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.005",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.01",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.025",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.05",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.075",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.1",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.25",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.5",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="0.75",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="1.0",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="2.5",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="5.0",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="7.5",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="10.0",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_bucket{host="fmarslan",le="+Inf",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_count{host="fmarslan",process="read"} 30.0
   fmarslan_write_read_duration_nanoseconds_sum{host="fmarslan",process="read"} 0.003086010809056461
   # HELP fmarslan_write_read_duration_nanoseconds_created Duration of Write/Read process in nanoseconds
   # TYPE fmarslan_write_read_duration_nanoseconds_created gauge
   fmarslan_write_read_duration_nanoseconds_created{host="fmarslan",process="write"} 1.614862199735808e+09
   fmarslan_write_read_duration_nanoseconds_created{host="fmarslan",process="read"} 1.614862199736488e+09
   # HELP fmarslan_write_read_error_count_total Number of Write/Read Error
   # TYPE fmarslan_write_read_error_count_total counter
   fmarslan_write_read_error_count_total{host="fmarslan",process="write"} 0.0
   fmarslan_write_read_error_count_total{host="fmarslan",process="read"} 0.0
   # HELP fmarslan_write_read_error_count_created Number of Write/Read Error
   # TYPE fmarslan_write_read_error_count_created gauge
   fmarslan_write_read_error_count_created{host="fmarslan",process="write"} 1.6148621997359662e+09
   fmarslan_write_read_error_count_created{host="fmarslan",process="read"} 1.6148621997366009e+09
   # HELP fmarslan_write_read_service_state State of Write/Read Service
   # TYPE fmarslan_write_read_service_state gauge
   fmarslan_write_read_service_state{fmarslan_write_read_service_state="RUNNING",host="fmarslan"} 1.0
   fmarslan_write_read_service_state{fmarslan_write_read_service_state="STOPPED",host="fmarslan"} 0.0
   # HELP fmarslan_write_read_disk_state State of Write/Read Service
   # TYPE fmarslan_write_read_disk_state gauge
   fmarslan_write_read_disk_state{fmarslan_write_read_disk_state="OK",host="fmarslan"} 1.0
   fmarslan_write_read_disk_state{fmarslan_write_read_disk_state="NOT ACCESS",host="fmarslan"} 0.0
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

```js
  {
    "service": "ACTIVE",
    "status": "OK", /*NOT ACCESS or OK*/
    "duration": 598194
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

### Check State As Manuel

http://localhost:8080/check

```js
  {
    "service": "PASSIVE", /* ACTIVE or PASSIVE */
    "status": "OK", /*NOT ACCESS or OK*/
    "duration": 598194
  }
```

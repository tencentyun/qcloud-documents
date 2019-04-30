## Testing Tool
The tool for database benchmark performance test is sysbench 0.5.
Tool modification description:
Modifications to the OTLP script included with sysbench: the read/write ratio is changed to 1:1 and controlled by the testing command parameters "oltp_point_selects" and "oltp_index_updates". All the test cases in this document involve four Select operations and one Update operation, with the read/write ratio remaining at 4:1.

## Testing Environment

| Type | Description |
|:--:|:--:|
| Physical machine | High IO version - a single machine can support database instances with up to 488-GB memory and 6-TB hard disk |
| Instance specification | Current mainstream configuration specifications (see the test cases below) |
| Client configuration | 4-core CPU, 8 GB memory |
| Number of clients | 1-6 (the number of clients increases with the upgrade of configuration) |
| Network environment | Ten-Gigabit IDCs, with the network latency < 0.05 ms |
| Environment load | Load on the machine with MySQL installed > 70% (for non-exclusive instances) |

* Client specification: High-configuration machine is used to ensure the database instance performance can be measured through stress testing on a single client. For low-configuration client, it is recommended to use multiple such clients for parallel stress testing and aggregate the data.
* Network latency: The testing environment ensures that clients and database instances are in the same availability zone to prevent the testing result from being affected by the network environment.

## Testing Method
### 1. Structure of testing database tables

```
CREATE TABLE `sbtest1` ( 
`id` int(10) unsigned NOT NULL AUTO_INCREMENT, 
`k` int(10) unsigned NOT NULL DEFAULT '0', 
`c` char(120) NOT NULL DEFAULT '', 
`pad` char(60) NOT NULL DEFAULT '',
 PRIMARY KEY (`id`), KEY `k_1` (`k`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

### 2. Format of testing data lines

```
id: 1
k: 20106885
c: 08566691963-88624912351-16662227201-46648573979-64646226163-77505759394-75470094713-41097360717-15161106334-50535565977
pad: 63188288836-92351140030-06390587585-66802097351-4928296184
```


### 3. Data preparation

```
/root//sysbench/sysbench --mysql-host=xxxx --mysql-port=xxxx --mysql-user=xxx --mysql-password=xxx --mysql-db=test --mysql-table-engine=innodb --test=tests/db/oltp.lua --oltp_tables_count=20 --oltp-table-size=10000000  --rand-init=on prepare
```

Descriptions of data preparation parameters:
- `--test=tests/db/oltp.lua`: indicates implementing OLTP test by calling the tests/db/oltp.lua script.
- `--oltp_tables_count=20`: indicates that the number of tables for testing is 20.
- `--oltp-table-size=10000000`: indicates that each testing table is populated with 10 million rows of data.
- `--rand-init=on`: indicates that each testing table is populated with random data.
   

### 4. Command for Stress Testing
```
/root//sysbench/sysbench --mysql-host=xxxx --mysql-port=xxx --mysql-user=xxx --mysql-password=xxx --mysql-db=test --test=/root/sysbench_for_z3/sysbench/tests/db/oltp.lua --oltp_tables_count=xx --oltp-table-size=xxxx --num-threads=xxx --oltp-read-only=off --rand-type=special --max-time=600 --max-requests=0 --percentile=99 --oltp-point-selects=4 run
```

 Descriptions of stress testing parameters:
- `--test=/root/sysbench_for_z3/sysbench/tests/db/oltp.lua`: indicates implementing OLTP test by calling /root/sysbench_for_z3/sysbench/tests/db/oltp.lua script.
- `--oltp_tables_count=20`: indicates that the number of tables for testing is 20.
- `--oltp-table-size=10000000`: indicates that each testing table is populated with 10 million rows of data.
- `--num-threads=128`: indicates that the concurrent connections of clients for testing is 128.
- `--oltp-read-only=off`: indicates that the read-only testing model is disabled, and the read/write hybrid model is used.
- `--rand-type=special`: indicates that the stochastic model is specific.
- `--max-time=1800`: indicates the execution time of this testing.
- `--max-requests=0`: indicates that no limit is imposed on the total number of requests and the test is executed according to max-time.
- `--percentile=99`: indicates the sampling rate. 99 means discarding 1% (long requests) of requests, and taking the maximum value among the remaining 99% of requests. Default is 95%.
- `--oltp-point-selects=4`: indicates that the number of Select operations in the SQL testing command in OLTP script is 4. Default is 1.

### 5. Scenario Model

All the cases in this documentation use scenario script our_oltp.lua, which is modified to execute 4 Select operations for query and 1 Update operation (index column), with the read/write ratio remaining at 4:1.
For the maximum configuration, the parameter tuning model is added to the data scenario. For the test results, please see [Test Results](#document_test_result) below.

## Testing Parameters
| Memory | Storage | Number of Tables | Number of Rows | Data Set Size | Concurrency | Execution time (m) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 4 GB | 200 GB | 8 | 40 million | 76 GB | 128 | 30 |
|8 GB|200 GB|15|4000 W|142 GB|128|30|
| 16 GB | 400 GB | 25 | 40 million | 238 GB | 128 | 30 |
|32 GB|700 GB|25|4000 W|238 GB|128|30|
| 64 GB | 1 TB | 40 | 40 million | 378 GB | 256 | 30 |
|96 GB|1.5 T|40|4000 W|378 GB|128|30|
| 128 GB | 2 TB | 40 | 40 million | 378 GB | 128 | 30 |
|244 GB|3 T|60|4000 W|567 GB|128|30|
| 488 GB | 6 TB | 60 | 40 million | 567 GB | 128 | 30 |
| 488 GB (tuning) | 6 TB | 60 | 10 million | 140 GB | 128 | 30 |

<span id="document_test_result"></span>
## Testing Result
| Memory | Storage | Data Set | Number of Clients | Concurrency for a Single Client | QPS | TPS |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 4 GB | 200 GB | 76 GB | 1 | 128 | 4082 | 816 |
|8 GB|200 GB|142 GB|1|128|6551|1310|
| 16 GB | 400 GB | 238 GB | 1 | 128 | 11098 | 2219 |
|32 GB|700 GB|238 GB|2|128|20484|3768|
| 64 GB | 1 TB | 378 GB | 2 | 128 | 36395 | 7279 |
|96 GB|1.5 T|378 GB|3|128|56464|11292|
| 128 GB | 2 TB | 378 GB | 3 | 128 | 81752 | 16350 |
|244 GB|3 T|567 GB|4|128|98528|19705|
| 488 GB | 6 TB | 567 GB | 6 | 128 | 142246 | 28449 |
| 488 GB (tuning) | 6 TB | 140 GB | 6 | 128 | 245509 | 46304 |


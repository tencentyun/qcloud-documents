> This document provides the performance comparison between DCDB sharding and open source MySQL (not optimized) for reference.

### Test Environment Comparison

**Hardware:** 24-core CPU; 128 GB memory; 1.8 TB SSD disk
**Network environment:** LAN, and its average network latency is 0.80 ms
**Operating system:** centos 7.0
**Data volume:** 10 tables, and each has 2,180,000 lines which is about 5.2 GB; innodb buffer: 30 GB
**Open source version:** MySQL 5.7.17 community version (not optimized; **enable semisync**)
**DCDB sharding version:** MySQL5.7 (optimized based on Percona 5.7.17 kernel) (**enable strongsync**). Enable thread pool by default. The parameters are shown as follows:

- thread\_pool\_max\_threads=2000
- thread\_pool\_oversubscribe=10
- thread\_pool\_stall\_limit=50
- thread\_handling=2

### Test Results Comparison

>Based on the results, read and write performance of single DCDB shard is doubled compared with that of open source MySQL.

### Detailed data of comparison test is as follows

#### 1. Data Initialization Parameter

```
create database caccts ;
./sysbench --num-threads=500 --test=./tests/db/oltp.lua.bak --oltp-table-size=2180000 --oltp-tables-count=10 --oltp-point-selects=1 --oltp-simple-ranges=0 --oltp-sum-ranges=0 --oltp-order-ranges=0 --oltp-index-updates=1 --oltp-non-index-updates=0 --report-interval=1 --mysql-user=xxxxxx --mysql-password=xxxxxx --mysql-host=xxxxxx --mysql-db=caccts --max-time=360000 --max-requests=2000000000 prepare

```

#### 2. Non-index Update (Update)

```
./sysbench --num-threads=500 --test=./tests/db/update\_non\_index.lua --oltp-table-size=2180000 --oltp-tables-count=10 --percentile=99 --report-interval=1 --mysql-host=xxxx --mysql-user=xxx --mysql-password=xxx --mysql-db=caccts --max-time=360000 --max-requests=2000000000 --mysql-port=3306 run

```

#### 3. Read-only (Select)

```
./sysbench --num-threads=500 --test=./tests/db/select.lua --oltp-table-size=2180000 --oltp-tables-count=10 --percentile=99 --report-interval=1 --mysql-host=xxxx --mysql-user=xxx --mysql-password=xxx --mysql-db=caccts --max-time=360000 -- max-requests=2000000000 --mysql-port=3306 run

```

#### 4. Hybrid Test

```
./sysbench\_orig --num-threads=500 --test=./tests/db/oltp\_new.lua --oltp-read-only=off --oltp-table-size=2180000 --oltp-tables-count=10 --oltp-point-selects=1 --oltp-simple-ranges=0 --oltp-sum-ranges=0 --oltp-order-ranges=0 --oltp-distinct-ranges=0 --oltp-index-updates=1 --oltp-non-index-updates=0 --percentile=99 --report-interval=1 --mysql-host=xxxx -- mysql-user=xxx --mysql-password=xxx --mysql-db=caccts --max-time=360000 --max-requests=2000000000 --mysql-port=3306 run

```

#### Read Request (Read)

| Concurrence | Version | QPS | Average Response Time (ms) | 99% Response Time (ms) |
| --- | --- | --- | --- | --- |
| 50 | Open source MySQL | 304,585 | 0.16 | 0.26 |
| 50 | DCDB | 330,695 | 0.15 | 0.24 |
| 100 | Open source MySQL | 407,443 | 0.24 | 0.48 |
| 100 | DCDB | 484,640 | 0.2 | 0.72 |
| 200 | Open source MySQL | 433,401 | 0.57 | 1 |
| 200| DCDB | 498,215 | 0.55 | 1.22 |
| 500 | Open source MySQL | 428,542 | 1.16 | 2.42 |
| 500 | DCDB | 494,874 | 1.01 | 2.61 |
| 1000 | Open source MySQL | 412,775 | 2.4 | 6.3 |
| 1000 | DCDB | 478,393 | 2.08 | 4.21 |

#### Write Request (Update)

| Concurrence | Version | QPS | Average Response Time (ms) | 99% Response Time (ms) |
| --- | --- | --- | --- | --- |
| 50 | Open source MySQL | 14,816 | 3.37 | 4.82 |
| 50 | DCDB | 28,925 | 1.73 | 2.55 |
| 100 | Open source MySQL | 25,046 | 3.99 | 6.91 |
| 100 | DCDB | 43,466 | 2.3 | 4 |
| 200 | Open source MySQL | 32,690 | 6.12 | 10.86 |
| 200 | DCDB | 54,045 | 3.7 | 7.27 |
| 500 | Open source MySQL | 37,192 | 13.44 | 21.1 |
| 500 | DCDB | 70,370 | 7.25 | 15.52 |
| 1000 | Open source MySQL | 35,447 | 28.2 | 40.47 |
| 1000 | DCDB | 69,890 | 14.35 | 30.73 |

#### Hybrid Scenario (OLTP test)

| Concurrence | Version | QPS | Average Response Time (ms) | 99% Response Time (ms) |
| --- | --- | --- | --- | --- |
| 50 | Open source MySQL | 63,806 | 4.7 | 7.13 |
| 50 | DCDB | 162,883 | 1.84 | 3.45 |
| 100 | Open source MySQL | 102,516 | 5.85 | 11.4 |
| 100 | DCDB | 173,974 | 3.58 | 6.64 |
| 200 | Open source MySQL | 124,550 | 9.64 | 18.92 |
| 200 | DCDB | 208,128 | 5.76 | 11.9 |
| 500 | Open source MySQL | 125,386 | 23.93 | 39.68 |
| 500 | DCDB | 232,543 | 13.58 | 27.81 |
| 1000 | Open source MySQL | 121,765 | 49.29 | 80.71 |
| 1000 | DCDB | 226,130 | 27.76 | 54.78 |





> Here we provide a comparison on the performance of MariaDB and open source MySQL (unoptimized) for reference.

### Testing Environment Comparison

**Hardware:** 24-core CPU; 128 GB memory; 1.8 TB SSD disk
**Network environment:** LAN, and its average network latency is 0.80 ms
**Operating system:** centos 7.0
**Data volume:** 10 tables, and each has 2,180,000 lines which is about 5.2 GB; innodb buffer: 30 GB
**Open source version:** MySQL 5.6 community version (not optimized; **enable semisync**)
**MariaDB sharding version:** MariaDB 10.1.10 (optimized based on kernel; **enable strongsync**). Thread pool is enabled by default.


### Testing Results Comparison

>Based on the results, the strongsync performance of optimized MariaDB is slightly better than MySQL's async performance.

### Detailed data of comparison test is as follows

#### 1. Data initialization parameters

```
create database caccts ;
./sysbench --num-threads=500 --test=./tests/db/oltp.lua.bak --oltp-table-size=2180000 --oltp-tables-count=10 --oltp-point-selects=1 --oltp-simple-ranges=0 --oltp-sum-ranges=0 --oltp-order-ranges=0 --oltp-index-updates=1 --oltp-non-index-updates=0 --report-interval=1 --mysql-user=xxxxxx --mysql-password=xxxxxx --mysql-host=xxxxxx --mysql-db=caccts --max-time=360000 --max-requests=2000000000 prepare

```

#### 2. Non-index update (update)

```
./sysbench --num-threads=500 --test=./tests/db/update\_non\_index.lua --oltp-table-size=2180000 --oltp-tables-count=10 --percentile=99 --report-interval=1 --mysql-host=xxxx --mysql-user=xxx --mysql-password=xxx --mysql-db=caccts --max-time=360000 --max-requests=2000000000 --mysql-port=3306 run

```

#### 3. Read-only (select)

```
./sysbench --num-threads=500 --test=./tests/db/select.lua --oltp-table-size=2180000 --oltp-tables-count=10 --percentile=99 --report-interval=1 --mysql-host=xxxx --mysql-user=xxx --mysql-password=xxx --mysql-db=caccts --max-time=360000 -- max-requests=2000000000 --mysql-port=3306 run

```

#### 4. Hybrid Test

```
./sysbench\_orig --num-threads=500 --test=./tests/db/oltp\_new.lua --oltp-read-only=off --oltp-table-size=2180000 --oltp-tables-count=10 --oltp-point-selects=1 --oltp-simple-ranges=0 --oltp-sum-ranges=0 --oltp-order-ranges=0 --oltp-distinct-ranges=0 --oltp-index-updates=1 --oltp-non-index-updates=0 --percentile=99 --report-interval=1 --mysql-host=xxxx -- mysql-user=xxx --mysql-password=xxx --mysql-db=caccts --max-time=360000 --max-requests=2000000000 --mysql-port=3306 run

```

#### Read requests (Read)

| Concurrence | Version | QPS | Average Response Time (ms) | 99% Response Time (ms) |
| --- | --- | --- | --- | --- |
| 50 | Open source MySQL | 306512 | 0.16 | 0.26 |
| 50 | MariaDB | 310695 | 0.15 | 0.24 |
| 100 | Open source MySQL | 417443 | 0.24 | 0.48 |
| 100 | MariaDB | 454640 | 0.2 | 0.72 |
| 200 | Open source MySQL | 423419 | 0.57 | 1 |
| 200| MariaDB | 488224 | 0.56 | 1.22 |
| 500 | Open source MySQL | 438512 | 1.16 | 2.42 |
| 500 | MariaDB | 490678 | 1.21 | 2.61 |
| 1000 | Open source MySQL | 412723 | 2.3 | 6.3 |
| 1000 | MariaDB | 481342 | 2.1 | 4.21 |

#### Write requests (update)

| Concurrence | Version | QPS | Average Response Time (ms) | 99% Response Time (ms) |
| --- | --- | --- | --- | --- |
| 50 | Open source MySQL | 24816 | 2.37 | 2.82 |
| 50 | MariaDB | 28925 | 2.33 | 2.55 |
| 100 | Open source MySQL | 43046 | 2.25 | 3.91 |
| 100 | MariaDB | 43466 | 2.3 | 4 |
| 200 | Open source MySQL | 54690 | 3.92 | 7.86 |
| 200 | MariaDB | 54045 | 3.7 | 7.27 |
| 500 | Open source MySQL | 70192 | 7.44 | 14.1 |
| 500 | MariaDB | 70370 | 7.25 | 15.52 |
| 1000 | Open source MySQL | 68447 | 15.2 | 29.47 |
| 1000 | MariaDB | 69890 | 14.35 | 30.73 |

#### Hybrid Scenario (OLTP test)

| Concurrence | Version | QPS | Average Response Time (ms) | 99% Response Time (ms) |
| --- | --- | --- | --- | --- |
| 50 | Open source MySQL | 154806 | 2.7 | 4.13 |
| 50 | MariaDB | 162883 | 1.84 | 3.45 |
| 100 | Open source MySQL | 162696 | 3.85 | 7.4 |
| 100 | MariaDB | 173974 | 3.58 | 6.64 |
| 200 | Open source MySQL | 204550 | 5.64 | 12.92 |
| 200 | MariaDB | 208128 | 5.76 | 11.9 |
| 500 | Open source MySQL | 235386 | 13.93 | 28.58 |
| 500 | MariaDB | 232543 | 13.58 | 27.23 |
| 1000 | Open source MySQL | 201765 | 28.29 | 60.72 |
| 1000 | MariaDB | 226130 | 27.76 | 54.38 |





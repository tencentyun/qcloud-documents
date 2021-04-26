## Performance Monitoring
MariaDB (TDSQL) provides various performance monitoring items to make it easy for users to view and obtain the operation information of instances. You can check it through "Instance Management" -> "System Monitoring" in MariaDB (TDSQL) console.

## Monitoring of Slave
MariaDB (TDSQL) supports slave performance monitoring. You can switch to the slave data according to the instructions on the monitoring page.

## Monitoring Metrics

| Metric | Unit | Notes |
|-------|-------|-------|
| CPU Utilization | % | MariaDB (TDSQL) adopts flexible CPU limits, allowing your instance to use extra CPU resources of the device. In this case, CPU utilization may exceed 100%. |
| Buffer Cache Hit Ratio | % | SELECT or preprocessing query obtains the ratio of data from memory. It is recommended that the value is 90%+. If not, you need to increase the memory size.  |
| Freeable Memory - to be deleted | GB | The actual memory available in Innodb_buffer. Since the database uses LRU scheduling program, normally the value tends to zero. But when you are dealing with large transactions, the value may be negative. In other words, the database memory usage exceeds the assigned value.  |
| Storage Space Utilization | % | The ratio of current space occupied by data, logs, temporary data, and system files to the purchased disk space. It is recommended that the value is 80%-. If not, you need to increase the disk space.  |
| Free Storage Space | GB | The absolute free disk space of current instance. It is recommended that the value is greater than your purchased disk space. If not, you need to increase the disk space.  |
| Binary Log Disk Usage | GB | The storage space temporarily stored in database on data disk. Generally, the value varies with the ratio of the written data. Please note that this value is not the storage space for logs in the backup system.  |
| DB Connections | Count | The total number of connections from the client to the database server.  |
| Active Connections | Count | The total number of active connections from the client to the database server.  |
| IO Utilization | % | MariaDB (TDSQL) adopts flexible IO limits, allowing your instance to use extra IO resources of the device. In this case, IO utilization may exceed 100%. |
| SQL Throughput | Counts per second | The total number of DDL, DML and DCL. |
| SQL Error Throughput | Counts per second | The total number of execution errors in DDL, DML and DCL. If the value is too large, check the business log as soon as possible.  |
| SQL Success Throughput | Counts per second | The total number of success execution in DDL, DML and DCL. |
| Slow Log | Counts per second | The amount of statement data that the execution time of SQL statement exceeds the set value of long_query_time. For more information, please see performance optimization page.  |
| DML Latency 1-5 ms | Counts per second | The statistics of the execution time of SQL statements.  |
| DML Latency 5-20 ms | Counts per second | The statistics of the execution time of SQL statements.  |
| DML Latency 20-30 ms | Counts per second | The statistics of the execution time of SQL statements.  |
| DML Latency more than 30 ms | Counts per second | The statistics of the execution time of SQL statements.  |
| DML Throughput | Counts per second | The total number of DML statements |
| SELECT | Counts per second | The total number of SELECT statements. If the value is large, you can enable read-write separation.  |
| UPDATE | Counts per second | The total number of UPDATE statements.  |
| INSERT | Counts per second | The total number of INSERT statements.  |
| REPLACE | Counts per second | The total number of REPLACE statements.  |
| REPLACE_SELECT | Counts per second | The total number of REPLACE_SELECT statements.  |
| DELETE | Counts per second | The total number of DELETE statements.  |
| Master Switch | Count | The occurrence of switching from the master to the slave |
| Replica Lag | Second | Data latency between the slave and the master. With strongsync, the master returns a transaction response only when data is written to binlog of the slave. But at this time, the data has not been fully written to the disk, so latency still occurs. |
| Innodb Buffer Pool Read | Counts per second | It is used to analyze current performance metrics of the innodb storage engine. |
| Innodb Buffer Pool Read Requests | Counts per second | It is used to analyze current performance metrics of the innodb storage engine. |
| Innodb Innodb Buffer Pool Read Ahead | Counts per second | It is used to analyze current performance metrics of the innodb storage engine. |
| Innodb Rows Deleted | Counts per second | It is used to analyze current performance metrics of the innodb storage engine. |
| Innodb Rows Insert | Counts per second | It is used to analyze current performance metrics of the innodb storage engine. |
| Innodb Rows Read | Counts per second | It is used to analyze current performance metrics of the innodb storage engine. |
| Innodb Rows Updated | Counts per second | It is used to analyze current performance metrics of the innodb storage engine. |

## 1. Feature Description

An SQL statement query that takes longer than specified time is called a "slow log", and such statement is referred to as "slow query log (SQL)". We refer to the process in which database admin (DBA) analyzes the statement and tries to find out the cause for the slow log as "slow log analysis".

Tencent Cloud Database (CDB for PostgreSQL) provides slow log analysis feature which can be found in "Instance Management" -> "Performance Optimization", as shown below:

![](https://mc.qcloudimg.com/static/img/93c466363e23e8a4283ac4b9c5d88927/pgsql-slowlog.png)


## 2. Main Parameters

### 2.1. Default Setting of Slow Log Analysis

Slow log feature: Enabled by default.
Minimum duration (log_min_duration_statement): It is 1s by default, that is, only slow query statements that take longer than 1 second are logged. For adjustments, please submit a ticket, and tell us the instance ID and the time to be modified.
Analyzed data output latency: 1 to 5 minutes.
Logging duration: 7 days (the maximum volume is the latest 10,000 records)

### 2.2. Fields in the Analysis List

Now slow log analysis feature provides the following slow SQL information:

**Basic Information**

a) **Last execution time**: The last time when the abstract statement appeared within statistical range. Because some statements' execution time is expected to be long, we log the begin_time of the statements.

b) **Abstracted SQL statement**: The statement after removing constants in SQL. The abstracted statement can be used for summary statistics of similar statements to facilitate your analysis.

c) **Database**: The database called by the statement.

d) **Account**: The account running the statement.

e) **First execution time**: The last time when the SQL appeared within statistical range. (There may be many records after abstraction and summary).

f) **Total count**: How many times in total the SQL appeared within statistical range.

g) **Occurrence percentage**: The SQL percentage in relation to the total number of all SQL within statistical range.

h) **Number of rows sent**:Total number of data rows sent (returned) to clients by database server within statistical range.

**Query Information Statistics**

a) **Total time**: Total time cost for slow log statements within statistical range;

b) **Total time percentage:** Percentage of total time cost for slow log statements within statistical range.

c) **Average time**: Average time calculated by dividing the total time cost for slow log statements with total number of times;

d) **Minimum time**: Minimum time cost for slow log statements among the abstract statement, which is used to help determine whether the statement is sporadic.

e) **Maximum time**: Maximum time cost for slow log statements among the abstract statement, which is used to help determine whether the statement is sporadic.

**Read and write data statistics**

a) Blocks of shared memory read: How much data in shared memory is read by the SQL within the statistical range.

b) Blocks of shared memory written: How much data is written into shared memory by the SQL within the statistical range.


**IO read and write time statistics**

a) Total IO read time: The total time cost for IO read by the SQL within the statistical range, which is used to help determine whether the statement is performing time-consuming operations including full scan.

b) Total IO write time: The total time cost for IO write by the SQL within the statistical range, which is used to help determine whether the statement writes large amounts of (temporary) data once.






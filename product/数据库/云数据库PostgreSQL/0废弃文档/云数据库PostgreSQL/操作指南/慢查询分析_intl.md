## 1. Feature Description

An SQL statement query that takes longer than the specified time is called a "slow log", and such statement is referred to as a "slow log statement (slow SQL)". We refer to the process in which a database admin (DBA) analyzes the statement and tries to find out the cause for the slow log as "slow log analysis".

TencentDB for PostgreSQL provides the slow log analysis feature in **Instance Management** -> **Performance Optimization**. See the figure below:

![](https://mc.qcloudimg.com/static/img/93c466363e23e8a4283ac4b9c5d88927/pgsql-slowlog.png)


## 2. Main Parameters

### 2.1 Default setting of slow log analysis

Slow log feature: Enabled by default.
Threshold for slow SQL logging (log_min_duration_statement): It is 1s by default, that is, only slow SQLs that take longer than 1 second are recorded. To adjust the threshold, submit a ticket specifying the instance ID and the adjusted time threshold you want.
Analyzed data output latency: 1 to 5 minutes.
Logging duration: 7 days (the maximum volume is the latest 10,000 records)

### 2.2 Fields in the analysis list

Now slow log analysis feature provides the following slow SQL information:

**Basic information**

a) **Last execution time**: The time when the abstract statement appeared for the last time within the statistical range. As some statements may be executed for a long time, we log the begin_time of statement execution.

b) **Abstracted SQL statement**: The statement after constants are removed from the slow SQL. The abstracted statement can be used for summary statistics of similar statements to facilitate your analysis.

c) **Database**: The database called by the statement.

d) **Account**: The account running the statement.

e) **First execution time**: The time when the slow SQL appeared for the first time within the statistical range. (There may be many records after abstraction and summary).

f) **Total occurrences**: How many times in total the slow SQL appeared within the statistical range.

g) **Occurrence percentage**: The percentage of the total occurrences of the slow SQL to the total occurrences of all slow SQLs within the statistical range.

h) **Number of rows sent**: Total number of data rows sent (returned) to the client by the database server within the statistical range.

**Query information statistics**

a) **Total time**: Total time cost by the slow SQL within the statistical range.

b) **Total time percentage:** The percentage of the total time cost by the slow SQL to the total time cost by all slow SQLs within the statistical range.

c) **Average time**: The average time obtained by dividing the total time cost by the slow SQL by the total occurrences of the slow SQL.

d) **Minimum time**: The minimum time cost by the slow SQL among the abstract statement, which is used to determine whether the statement was sporadic.

e) **Maximum time**: The maximum time cost by the slow SQL among the abstract statement, which is used to determine whether the statement was sporadic.

**Read and write data statistics**

a) Blocks of shared memory read: How much data in the shared memory was read by the slow SQL within the statistical range.

b) Blocks of shared memory written: How much data was written into the shared memory by the slow SQL within the statistical range.


**IO read and write time statistics**

a) Total IO read time: The total time cost for IO read by the slow SQL within the statistical range, which is used to determine whether the statement performed time-consuming operations including full scan.

b) Total IO write time: The total time cost for IO write by the slow SQL within the statistical range, which is used to determine whether the statement wrote large amounts of (temporary) data once.






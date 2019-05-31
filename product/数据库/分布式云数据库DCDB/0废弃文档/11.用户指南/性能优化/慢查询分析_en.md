## 1. Feature Description
An SQL statement query that takes longer than specified time is called a "slow log", and such statement is referred to as "slow log statement". We refer to the process in which database admin (DBA) analyzes the statement and tries to find out the cause for the slow log as "slow log analysis".

Tencent Cloud Database (CDB for TDSQL) provides slow log analysis feature which can be found in **Instance Management** -> **Performance Optimization**.

## 2. Main Parameters
### (1) Main Default Settings
-   Slow log feature: Enabled by default.
-   Slow log time (long_query_time): one second, that is, only query statements that take longer than one second are recorded.
-   Analysis delay: 1 to 5 minutes.

### (2) Fields in the Analysis List
-   Checksum (checksum): A sequence of numbers used to identify the slow log statement (64-bit by default);
-   Abstracted slow log statement (fingerprint): Slow log statement with user data hidden;
-   Database: The database in which the slow log statement is located;
-   Account: The account under which the slow log statement is located;
-   Last execution time (last_seen): The last time when slow log statement appeared, within time range;
-   First execution time (first_seen): The first time when slow log statement appeared, within time range;
-   Total number of times (ts_cnt): Number of occurrences for slow log statements, within time range;
-   Occurrence percentage: Slow log statement percentage in relation to the total number of slow log statements, within time range;
-   Total time (query_time_sum): Total time cost for slow log statements within time range;
-   Total time percentage: Percentage of total time cost for slow log statements, within time range;
-   Average time (query_time_avg): Average time calculated by dividing the total time cost for slow log statements with total number of times;
-   Minimum time (query_time_min): Minimum time cost for slow log statements;
-   Maximum time (query_time_max): Maximum time cost for slow log statements;
-   Total lock time (lock_time_sum): Total lock time for slow log statements;
-   Total lock time percentage: Time cost percentage for slow log statements in relation to total slow log statement lock time, within time range;
-   Average lock time (lock_time_avg): Average time calculated by dividing total slow log statement lock time with total number of locks;
-   Minimum lock time (lock_time_min): Minimum slow log statement lock time;
-   Maximum lock time (lock_time_max): Maximum slow log statement lock time;
-   Number of rows sent (Rows_sent_sum): Total number of data rows sent by the slow log statement;
-   Number of rows scanned (Rows_examined_sum): Total number of data rows scanned by the slow log statement.


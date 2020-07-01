## 1. Feature Description
Slow log indicates that a SQL query statement takes more than defined time to execute, and the corresponding statement refers to "slow log statement". Slow log analysis indicates the process during which a database administrator (DBA) analyzes the slow log statement and finds the reasons for the slow log.

CDB for MariaDB (TDSQL) provides the capacity of slow log analysis under the module "Instance Management" - "Performance Optimization".

## 2. Main Parameters
### 2.1 Main default settings
-   Slow log feature: It is enabled by default
-   Slow log time (long_query_time): Default value is 1 second, that is, only slow log statement with query time longer than 1 second can be recorded.
-   Delay time of analysis data output: 1-5 minutes.
-   Log retention period: 30 days, which is determined based on the cycle of backups and logs.

### 2.2 Fields of analysis list
-   Check value (checksum): A sequence of numbers indicating slow log statements. Default is 64-bit;
-   Abstract slow log statement (fingerprint): The slow log statement after the user data is hide;
-   Database: The database where slow log statement occurs;
-   Account: The account under which slow log statement occurs;
-   Time of last execution (last_seen): The last time when the slow log statement occurs within the time span;
-   Time of first execution (last_seen): The first time when the slow log statement occurs within the time span;
-   Total number of occurrences (ts_cnt): The number of times the slow log statement occurs within the time span;
-   Percentage of total number of occurrences: The percentage of the number of occurrences of the slow log statement to that of all the slow log statements within the time span;
-   Total time (query_time_sum): Total time consumed in querying slow log statement within the time span;
-   Percentage of total time: The percentage of the time consumed in querying slow log statement to that in querying all the slow log statements within the time span;
-   Average time (query_time_avg): Divide total time by total number of occurrences;
-   Minimum time (query_time_min): The minimum time during which the slow log statement occurs;
-   Maximum time (query_time_min): The maximum time during which the slow log statement occurs;
-   Total lock time (lock_time_sum): Total time during which the slow log statement lock occurs;
-   Percentage of total lock time: The percentage of the lock time of slow log statement to that of all the slow log statements within the time span;
-   Average lock time (lock_time_avg): Divide total lock time by total number of locks;
-   Minimum lock time (lock_time_min): The minimum time during which the slow log statement lock occurs;
-   Maximum lock time (lock_time_min): The maximum time during which the slow log statement lock occurs;
-   Number of rows sent (Rows_sent_sum): Total number of data rows sent by this slow log statement;
-   Number of rows examined (Rows_examined_sum): Total number of data rows examined by this slow log statement;



## Optimizer Hint ##

Some TiDB-specific Hint syntaxes are added to TiDB based on MySQL's Optimizer Hint syntax. When using these Hints, the TiDB optimizer will try its best to use the specified algorithm, which is better than the default algorithm in some scenarios.

Since hint is contained in a comment like /*+ xxx */, the MySQL client clears the comment by default before version 5.7.7. To use hint on the old client, you need to add the --comments option when launching the client, for example: 

    mysql -h 127.0.0.1 -P 4000 -uroot --comments

***TIDB_SMJ(t1, t2)***


    SELECT /*+ TIDB_SMJ(t1, t2) */ * from t1,t2 where t1.id = t2.id

Hint the optimizer to use the Sort Merge Join algorithm, which usually takes up less memory but takes longer to execute. When the volume of data is too large, or the system memory is not enough, it is recommended to try to use.

***TIDB_INLJ(t1, t2)***


    SELECT /*+ TIDB_INLJ(t1, t2) */ * from t1,t2 where t1.id = t2.id

Hint the optimizer to use the Index Nested Loop Join algorithm, which may be faster in some scenarios and consume less system resources, and may be slower in another scenarios and consume more system resources. For scenarios whose result set is smaller (less than 10,000 lines) after filtered by WHERE conditions, you can try to use. The parameter in TIDB_INLJ() is the candidate table for the drive table (external table) when creating the query plan. It means TIDB_INLJ(t1) will only consider using t1 as driver table to build query plan.

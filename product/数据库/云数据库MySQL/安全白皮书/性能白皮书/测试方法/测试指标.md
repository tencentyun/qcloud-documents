本文为您介绍云数据库 MySQL 性能测试的测试指标。

| 指标 | 定义 | 
|---------|---------|
| TPS（Transactions Per Second） | 数据库每秒执行的事务数，以 COMMIT 成功次数为准 | 
|  QPS（Queries Per Second） | 数据库每秒执行的 SQL 数，包含 INSERT、SELECT、UPDATE、DETELE、COMMIT 等 | 
|  avg_lat（Average Latency） | 数据库所有 event 的平均耗时 | 
|  并发度 | 性能测试时客户端发起的并发数 | 


用户在使用 MongoDB 时发现了 CPU 使用率高，可以从以下几个方面来排查问题。<br>
1. 首先需要确定业务是否有很高的操作数据库频率。
请查看控制台监控指标，具体如下图所示：若业务 QPS 确实高，请评估是否需要升级实例配置。若业务 QPS 并不高，此时需要排查是不是有慢查询。
![](https://main.qcloudimg.com/raw/e013e4387e144b8f98ab1de810503c0d.png)


2. 查看当前 mongod 上有没有慢日志。
登录 [腾讯云 MongoDB 控制台](https://console.cloud.tencent.com/mongodb)，查看实例的慢日志，可选择抽象查询，具体如下图所示。
![](https://main.qcloudimg.com/raw/19a7b1568cf38f6b493cb5088cfdff93.png)
请关注：command、COLLSCAN、IXSCAN、keysExamined、docsExamined 等关键字。
 
 
 - command 指出慢日志中记录的操作。<br>
 - COLLSCAN 代表该查询进行了全表扫描，IXSCAN 代表进行了索引扫描。更多的字段描述请参考 [MongoDB 官网](https://docs.mongodb.com/manual/reference/explain-results/index.html)。<br>
 - keysExamined 代表索引扫描条目，docsExamined 代表文档扫描条目。keysExamined 和 docsExamined 越大代表没有建索引或者索引的区分度不高。请确认索引的创建字段。<br>
更多的日志说明请参考 [MongoDB 官网](https://docs.mongodb.com/manual/reference/log-messages/index.html)

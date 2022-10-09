## 功能描述

SQL 限流功能适用于流量过高引起的 CPU 消耗过大的场景。通过创建 SQL 限流任务，用户可自主设置 SQL 类型、最大并发数、限流时间、SQL 关键词，来控制数据库的请求访问量和 SQL 并发量，从而达到服务的可用性。

> ?
>- SQL 限流仅支持云数据库 MongoDB 4.0 版本，如需升级至此版本，请 [提交工单](https://console.cloud.tencent.com/workorder/category)。
>- SQL 限流中被拒绝语句的错误码显示为：SQL rejected by CDB_SQL_FILTER。

## 创建 SQL 限流

1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain)，在左侧导航选择**诊断优化**，在上方选择对应数据库，然后选择**实时会话**，在该页面下方可查看 **SQL 限流** 模块。
![](https://qcloudimg.tencent-cloud.cn/raw/d0e2b2fe4d926dd5ab7088b6194d46a9.png)
2. 创建限流任务。
  需要先登录数据库，才可以发起 SQL 限流任务。
 - SQL 类型：包含 find、insert、update、delete。
 - 最大并发数：SQL 最大并发数，当包含关键词的 SQL 达到最大并发数时会触发限流策略。如果该值设为0，则表示限制所有匹配的 SQL 执行。
 - 执行方式：支持**定时关闭**和**手动关闭**。
 - 限流时间：选择**定时关闭**时，需选择 SQL 限流的生效时间。
 - SQL 关键词：需要限流的 SQL 关键词，当包含多个关键词时，需要以英文逗号分隔，逗号分隔的条件是逻辑与的关系，且逗号不能作为关键词。
3. 查看 SQL 限流任务状态和详情。
 - 单击**操作**列的**详情**，可以查看 SQL 限流详情。
 - 限流任务开启后，若还在所设置的限流时间以内，列表中的状态为**运行中**，单击**操作**列的**关闭**，可以提前关闭限流任务，状态列将变为**已终止**。
 - 限流任务开启后，若自动达到所设定的限流时间，列表中的状态将变为**已终止**。
 - 单击**操作**列的**删除**，可以对状态为**已终止**和**已完成**的限流任务进行删除。
  
## SQL 限流案例及效果 

数据库流量过高，导致实例 CPU 消耗过大。

1. 通过控制台 mongotop 获取表级流量统计，从 mongotop 可以看出 test11 表流量过高，假设业务主要流量为 test.test10 表的读流量，test.test11 为异常流量。
![](https://qcloudimg.tencent-cloud.cn/raw/9db3e188cfa68a82587b0e9cb60593e4.png)
2. 随后开启 SQL 限流任务，对 test.test11表进行限流。
![](https://qcloudimg.tencent-cloud.cn/raw/436f2f8cdec55a80b1c6e69a6cae813a.png)
3. 限流前后 CPU 性能趋势图如下，可看出限流后 CPU 消耗迅速下降。
![](https://qcloudimg.tencent-cloud.cn/raw/09a71c2bafc01033fa701fd61148d149.png)

 

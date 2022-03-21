用户可以通过 SQL 语句对创建的数据库和数据表中数据进行查询、分析和计算。DLC 支持的 SQL 查询语句及函数可参见[ SQL 语法](https://cloud.tencent.com/document/product/1342/61733) 。
## 执行 SELECT 查询任务
1. 选择默认数据库及计算资源。
	- 用户可以选择一个默认数据库，则在 SQL 语句中会将没有指定数据库的操作在默认数据库下执行。
	- 计算资源可选共享集群或独享集群。
2. 运行 SQL 任务。写入标准SQL语句后，单击**运行**，即可开始运行 SQL 任务。
![](https://qcloudimg.tencent-cloud.cn/raw/4e673ddbe2be463bed02eaef373c8cdc.png)
	- DLC 单个任务运行时间的上限为30分钟。
	- DLC 为 Serverless 架构，算力资源会临时被调度。在一段时间内，首次运行 DML 任务的结果返回时间可能会比正常任务稍慢。
3. 任务执行完成，会在控制台展示查询结果。
	- 若用户退出了控制台页面，则无法在控制台查看历史任务的查询结果，需要到历史运行或用户配置的查询结果 COS 桶中查看任务结果文件。

## 取消正在执行的查询任务
在任务运行过程中，**运行**会切换为**终止**，可单击**终止**，取消本次查询。取消查询后，DLC 不会返回查询结果，但是 DLC 会统计已经执行的数据扫描量。若您使用的计算资源为public_engine，数据扫描量将会产生一定的费用，详细资费可参见 [计费概述](https://cloud.tencent.com/document/product/1342/50371)。
![](https://qcloudimg.tencent-cloud.cn/raw/953bd16bb81cee40ea438f7281c20f20.png)

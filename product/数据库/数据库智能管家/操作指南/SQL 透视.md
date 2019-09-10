SQL 透视是对数据库实例进行深层次的离线诊断分析，通过 Top SQL 分析执行次数最多、消耗时间最长的 SQL，分析事务是否合理，以及安全风险识别。

以数据库一段时间内产生的审计日志为基础，对全量的 SQL 以及执行信息（来源信息、次数、执行时间、返回集合、扫描集合等）进行统计、抽样、聚合。针对聚合后的 SQL 语句根据其执行计划的结果，综合资源消耗、扫描和返回集合大小、索引使用合理性等，对 SQL 的性能进行分析，并针对低质量 SQL 结合索引情况、库表设计，给出优化建议。

## SQL 视图
登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/slow-sql)，在左侧导航选择【SQL 透视】页，透视视图可选择 QPS 或慢查询次数维度。
![](https://main.qcloudimg.com/raw/70bb3e2700f4c239c1738fe6822f064f.png)

## 审计任务
1. 选择所需时间段，单击视图右上角的【创建审计任务】。
![](https://main.qcloudimg.com/raw/c9a4dc3cdd01a63bd53f462cea371e00.png)
2. 在设置页选择审计开始时间和持续时间，单击【确定】。
![](https://main.qcloudimg.com/raw/b0911cf6aef7468545afaf9cb8488758.png)
3. 创建完成后，可在审计任务列表分析审计任务和删除审计任务，单击操作列的【查看SQL分析】，进入 SQL 分析页。
![](https://main.qcloudimg.com/raw/2705cd5537d5bb6b96955dc840b4b2d2.png)
4. 在 SQL 分析页，可选择 SQL Type、Host、User 或 SQL Code 维度的视图，并可选择时间段拉伸视图来查看具体时间点的数据。
在下方的 Schema 列表会显示审计任务时间段段内前XXXX20的 Schema。
![](https://main.qcloudimg.com/raw/48a8b2a7c961c0e701aa48d691baa619.png)
5. 单击某行 Schema，在右侧会弹出 SQL 语句的具体分析和统计数据，您可根据给出的优化建议或说明来调整 SQL 语句。
![](https://main.qcloudimg.com/raw/d27d1b775ffe5774b56703a15618ef2e.png)

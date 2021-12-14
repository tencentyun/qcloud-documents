
## 操作场景
慢 SQL 分析对实例中慢 SQL 的记录和执行信息（来源信息、次数、执行时间、返回集合、扫描集合等）进行统计、抽样、聚合。针对聚合后的 SQL 语句、执行计划、综合资源消耗、扫描和返回集合大小、索引使用合理性等，对慢 SQL 的性能进行分析，并给出优化建议。
>?
>- 慢 SQL 分析目前支持云数据库 MySQL（不含单节点 - 基础型）、云原生数据库 TDSQL-C（TDSQL-C for MySQL）、自建数据库 MySQL、云数据库 MongoDB（请参考 [MongoDB 慢 SQL 分析](https://cloud.tencent.com/document/product/1130/65837))。Redis 的慢日志分析与 MySQL 和 TDSQL-C 不同，请参见 [Redis 慢日志分析](https://cloud.tencent.com/document/product/1130/58851)。
>- agent 接入的自建数据库实例在使用慢日志分析前，需确认慢日志采集是否开启，具体参见 [慢日志分析配置](https://console.cloud.tencent.com/dbbrain/instance?product=dbbrain-mysql)。
>- 直连接入的自建数据库实例不支持慢日志分析。

## 操作步骤
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/slow-sql)，在左侧导航选择【诊断优化】，在上方选择对应数据库，然后选择【慢 SQL 分析】页。
>?“SQL 统计”栏展示实例的慢查询数和 CPU 使用率，可调整时间范围查看任意时间段的慢 SQL 视图。若实例中有慢 SQL，视图中会显示慢 SQL 产生的时间点和个数。
2. 单击（选择单一时间段）或拉选（选择多个时间段）“SQL 统计”图表的慢查询（柱形图），下方会显示聚合 SQL 模板以及执行信息（包括执行次数、总耗时执行时间、扫描行数、返回行数等），各列数据均支持正序或逆序排序。右侧的耗时分布中会展示所选时间段内的 SQL 总体耗时分布情况。
![](https://main.qcloudimg.com/raw/dfce7ffad362522c7002ec33628bf530.png)
3. 单击某条聚合的 SQL 模板行，右侧边会弹出 SQL 的具体分析和统计数据。
 - 在分析页，您可查看完整的 SQL 模板、SQL 样例以及优化建议和说明，您可根据 DBbrain 给出的专家建议优化 SQL，提升 SQL 质量，降低延迟。
![](https://main.qcloudimg.com/raw/aeefc3396bcdfbdd548ea909b1fbabd8.png)
 - 在统计页，您可根据统计报表的总锁等待时间占比、总扫描行数占比、总返回行数占比，横向分析该条慢 SQL 产生的具体原因，以及进行对应优化，同时您还可以查看该类型的 SQL（聚合后汇总的）运行的时间分布区间，以及来源 IP 的访问占比。
![](https://main.qcloudimg.com/raw/14c648980260c952c4af8e370a41860a.png)


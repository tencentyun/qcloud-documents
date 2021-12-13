
## 慢日志介绍
慢日志分析目前支持云数据库 Redis、云数据库 MySQL（不含单节点 - 基础型）、云原生数据库 TDSQL-C（TDSQL-C for MySQL）、自建数据库 MySQL。
>?agent 接入的自建数据库实例在使用慢日志分析前，需确认慢日志采集是否开启，具体参见 [慢日志分析配置](https://console.cloud.tencent.com/dbbrain/instance?product=dbbrain-mysql)。

## 操作场景
Redis 的慢日志分析与 MySQL 和 TDSQL-C 不同，Redis 慢日志分别统计了 “实例” 与 “proxy” 两个维度的慢日志。
- 实例（Redis 数据库实例）维度，可以清晰的看到 CPU 使用率，慢查询数、日志分段耗时统计结果，和整个慢日志列表的列表信息。
- proxy（中间件集群节点）维度，可以看到 proxy 的慢日志统计、分段耗时情况，还有详细的慢日志列表信息。

## 操作步骤
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain)，在左侧导航选择**诊断优化**，在上方选择对应数据库，选择**慢日志分析**页。
![](https://main.qcloudimg.com/raw/540e4d8ce49f62a7cf9c1e03cef6c081.png)
2. 在慢日志分析页，可查看实例级别和 proxy 级别慢日志。
 - 实例级别慢日志：
    - 慢日志统计：单击慢日志统计中（选择单一时间段）或拉选（选择多个时间段），可看到该段范围的慢日志统计信息。
![](https://main.qcloudimg.com/raw/533c6ac4e8e6ee1ac1f35105775bf4cd.png)
    - 慢日志分段耗时统计：分段耗时慢日志分布中会展示所选时间段内的慢日志总体耗时分布情况，其中横轴为慢日志个数占比，纵轴为统计时段，鼠标浮动在某一统计时段上，会显示当前时间段慢日志个数占比。
![](https://main.qcloudimg.com/raw/f60c0a52f9e26b5a4b31d5fa118bb4d3.png)
    - 慢日志信息列表
![](https://main.qcloudimg.com/raw/333ef53b03b74842d9f6d1e8f0fc72ce.png)
 - proxy 级别慢日志：
![](https://main.qcloudimg.com/raw/dff5cb10b23027af7fc8bcc20865fe3f.png)
3. 图表日志联动。
在慢日志统计模块，单击您要定位的时间点，会同步定位当前时间产生的慢日志信息，以及具体耗时情况。
![](https://main.qcloudimg.com/raw/8d0596fc23190dffd3371d15a4c3374b.png)
4. 在慢日志分析页，单击右上角的**监控详情**，可以添加多个时间段，多个监控指标进行对比。
![](https://main.qcloudimg.com/raw/2c8b8f1be41ed82699aa8f1ef31f3124.png)
5. 在下方的慢日志列表，单击某条聚合的命令模板行，可在右侧弹出命令的具体分析和统计数据。
 - 在分析页可查看：
    - 命令模板。
    - 命令样例。
    - 优化建议和说明。
 - 在统计页可查看：
    - 展示该类型的命令（聚合后汇总的）运行的时间分布区间。
    - 来源 IP 的访问分布及占比（proxy 有，Redis 没有）。
![](https://main.qcloudimg.com/raw/c144821910a149ee51b807cc1f861627.png)

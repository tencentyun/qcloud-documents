慢 SQL 分析对实例中慢 SQL 记录和执行信息（来源信息、次数、执行时间、返回集合、扫描集合等）进行统计、抽样、聚合。针对聚合后的 SQL 语句、执行计划、综合资源消耗、扫描和返回集合大小、索引使用合理性等，对慢 SQL 的性能进行分析，并给出优化建议。本文将介绍如何使用慢SQL分析对slow log进行优化。
## SlowLog
登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/slow-sql)，在左侧导航选择【慢 SQL 分析】页，【Slow Log】栏展示实例的慢查询数和 CPU 使用率，可调整时间范围查看任意时间段的慢 SQL 视图。若实例中有慢 SQL，视图中会显示慢 SQL 产生的时间点和个数。
![](https://main.qcloudimg.com/raw/c0c4fd863d8eb1b13acbe6a39e2cac6c.png)

## 慢 SQL 详情
1. 单击 Slow Log 图表的慢查询（柱形图），下方会显示聚合 SQL 模板以及执行信息（包括执行次数、总耗时执行时间、扫描行数、返回行数等），各列数据均支持正序或逆序的排序。
![](https://main.qcloudimg.com/raw/dbd937a104de30de51d9816707e1608d.png)
2. 单击某条聚合的 SQL 模板行，右侧边会弹出 SQL 的具体分析和统计数据。
 - 在分析页，您可查看完整的 SQL 模板、SQL 样例以及优化建议和说明，您可根据 DBbrain 给出的专家建议优化 SQL，提升 SQL 质量，降低延迟。
![](https://main.qcloudimg.com/raw/0017b7d17bdf2562003aab7e83e437b3.png)
 - 在统计页，您可根据统计报表的总锁等待时间占比、总扫描行数占比、总返回行数占比，横向分析该条慢 SQL 产生的具体原因，以及进行对应优化。
 ![](https://main.qcloudimg.com/raw/0753c04e985d5ca2930e023ed04f1813.png)

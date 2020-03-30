## 操作场景
慢 SQL 分析对实例中慢 SQL 的记录和执行信息（来源信息、次数、执行时间、返回集合、扫描集合等）进行统计、抽样、聚合。针对聚合后的 SQL 语句、执行计划、综合资源消耗、扫描和返回集合大小、索引使用合理性等，对慢 SQL 的性能进行分析，并给出优化建议。
>?慢 SQL 分析目前仅支持云数据库 MySQL（不含基础版）。

通过如下视频，您可以了解 DBbrain 慢 SQL 分析功能的详细操作：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/1915-22592?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 操作步骤
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/slow-sql)，在左侧导航选择【诊断优化】，在上方选择【慢 SQL 分析】页，“SQL 统计”栏展示实例的慢查询数和 CPU 使用率，可调整时间范围查看任意时间段的慢 SQL 视图。若实例中有慢 SQL，视图中会显示慢 SQL 产生的时间点和个数。
2. 单击（选择单一时间段）或拉选（选择多个时间段）“SQL 统计”图表的慢查询（柱形图），下方会显示聚合 SQL 模板以及执行信息（包括执行次数、总耗时执行时间、扫描行数、返回行数等），各列数据均支持正序或逆序排序。右侧的耗时分布中会展示所选时间段内的 SQL 总体耗时分布情况。
![](https://main.qcloudimg.com/raw/fa47269970e090de7c6f9f72768c6e56.png)
3. 单击某条聚合的 SQL 模板行，右侧边会弹出 SQL 的具体分析和统计数据。
 - 在分析页，您可查看完整的 SQL 模板、SQL 样例以及优化建议和说明，您可根据 DBbrain 给出的专家建议优化 SQL，提升 SQL 质量，降低延迟。
![](https://main.qcloudimg.com/raw/d3ee9287405e92e1eef993de2385b34c.png)
 - 在统计页，您可根据统计报表的总锁等待时间占比、总扫描行数占比、总返回行数占比，横向分析该条慢 SQL 产生的具体原因，以及进行对应优化。
![](https://main.qcloudimg.com/raw/fc3061c2dc39d8ce788de083dd295c5d.png)
 - 在耗时分布页，您可查看该类型的 SQL（进过聚合后汇总的）运行的时间分布区间，以及来源 IP 的访问占比。
![](https://main.qcloudimg.com/raw/1256b159205af5a7574925708dc9fc95.png)

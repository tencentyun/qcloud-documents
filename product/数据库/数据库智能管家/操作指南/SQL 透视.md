## 操作场景
审计日志分析（原 SQL 透视）对数据库实例进行深层次的 SQL 分析，以数据库一段时间内产生的审计日志为基础，对全量的 SQL 以及执行信息（来源信息、次数、执行时间、返回集合、扫描集合等）进行统计、抽样、聚合。

针对聚合后的 SQL 语句，根据其执行计划的结果，综合资源消耗、扫描和返回集合大小、索引使用合理性等，对 SQL 的性能进行分析，并针对低质量 SQL 结合索引情况、库表设计，给出优化建议。本文将介绍如何进行全量 SQL 分析，及查看分析详情。
>?审计日志分析目前仅支持云数据库 MySQL（不含基础版）。

## 前提条件
实例需要开通 [数据库审计](https://cloud.tencent.com/document/product/672/14403) 功能。如未开通，则在创建 SQL 透视任务时会报如下错误，可单击【一键开通】，完成数据库 SQL 审计的开通和配置。
![](https://main.qcloudimg.com/raw/fc001ac870f1bed1cb301c29baaca47f.png)

通过如下视频，您可以了解 DBbrain 审计日志分析功能的详细操作：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/1915-22594?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 操作步骤
### SQL 视图
登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/slow-sql)，在左侧导航选择【诊断优化】，在上方选择【审计日志分析】页，透视视图可选择 QPS 或慢查询次数维度。
![](https://main.qcloudimg.com/raw/21b1e34c82b6c0ef06e5f4e7bf2673cc.png)

### 创建任务
1. 选择所需时间段，单击视图右上角的【创建审计任务】。
![](https://main.qcloudimg.com/raw/c9a4dc3cdd01a63bd53f462cea371e00.png)
2. 选择任务开始时间和时间间隔，单击【确定】。
![](https://main.qcloudimg.com/raw/b0911cf6aef7468545afaf9cb8488758.png)
3. 创建完成后，可在任务列表查看分析结果和删除任务，单击操作列的【查看SQL分析】，进入 SQL 分析页。
![](https://main.qcloudimg.com/raw/2705cd5537d5bb6b96955dc840b4b2d2.png)

### SQL 分析
1. 在 SQL 分析页，可选择 SQL Type、Host、User 或 SQL Code 维度的视图，并可选择时间段拉伸视图来查看具体时间点的数据。下面表格中会展示该时间段内 SQL 的聚合详情以及执行信息（包括执行次数、总延迟、最大延迟、最小延迟、总影响行数、最大影响行数、最小影响行数等）。
 - 若对图中时间进行部分拉伸选中，表格中的 SQL 数据会随之变化，只显示图中时间范围内的 SQL 分析结果。
 - 图中“SQL Type”和“图例”均可进行单击筛选，表格中的 SQL 数据会随之变化，例如，只想查看 Select 请求，可将其余类型的图例点暗。
![](https://main.qcloudimg.com/raw/c480b9f9c0dfd9569f9110e1aa9fa99d.png)
2. 单击某行 SQL 模板，在右侧会弹出 SQL 语句的详情。
 - 在分析页，可查看和复制具体 SQL 语句，根据给出的优化建议或说明来优化 SQL 语句。
 ![](https://main.qcloudimg.com/raw/d27d1b775ffe5774b56703a15618ef2e.png)
 - 在统计页，可查看该类 SQL 在 Host、User、SQL Code 维度的统计分析和执行时间轨迹。
 ![](https://main.qcloudimg.com/raw/6af044530cc937e920f21a620972d6fc.png)




## 操作场景

TSF 记录了业务丰富的监控数据，控制台提供了多种监控数据展示入口。TSF 提供了部分监控数据接口的 API，客户可基于这些接口对数据进行二次加工、打造更符合业务需求的监控展示平台。

本教程将介绍已开放的监控数据接口。



## 前提条件

在开始本文的实践前，您需要先了解 TSF 的以下功能：

- [Spring Cloud 应用开发 - 服务监控](https://cloud.tencent.com/document/product/649/34294)
- [Mesh 应用开发 - 查询 SiderCar 监控信息](https://cloud.tencent.com/document/product/649/53870)
- 在 TSF 控制台的监控
  - [服务监控](https://cloud.tencent.com/document/product/649/45975)
  - [部署组监控](https://cloud.tencent.com/document/product/649/55601)
  - [实例监控](https://cloud.tencent.com/document/product/649/55599) 
  - [接口监控](https://cloud.tencent.com/document/product/649/55600)
- [JVM 监控相关](https://cloud.tencent.com/document/product/649/42891)



## 操作步骤

### 服务调用监控统计概览

本接口为 [DescribeOverviewInvocation](https://cloud.tencent.com/document/product/649/70428)，API 各项参数请参考文档接口文档。

本接口在 TSF 控制台的入口是：概览页的服务监控部分，包括了请求量、请求错误率、平均响应耗时三个指标。

本接口可获取指定命名空间下所有服务在一段时间内的请求量、请求错误率、平均响应耗时。注意是指定命名空间下的所有服务监控信息的聚合值。



### 服务监控统计

本接口为 [DescribeStatistics](https://cloud.tencent.com/document/product/649/70427)，API 各项参数请参考文档接口文档。

本接口用于多种服务监控数据的统计，具体在 TSF 控制台的入口如下所示：

- 服务监控（`Type` 传参为 `Service`）
  - 首页 > 服务指标统计TOP 10 > 服务
  - 服务监控 > 维度选择 "服务"
  - 服务监控详情 > 服务概览
- 接口监控（`Type` 传参为 `Interface`）(注意仅 23 以上的 SDK 版本支持)
  - 首页 > 服务指标统计TOP 10 > 接口
  - 服务监控 > 维度选择 "接口"
  - 服务监控详情 > 接口监控
  - 服务监控详情 > 接口监控 > 服务上游（需要传 `BucketKey` 为 `UpstreamApi`）
- 实例监控（`Type` 传参为 `Instance`）
  - 服务监控详情 > 实例监控
- 部署组监控（`Type` 传参为 `Group`）
  - 服务监控详情 > 部署组监控
- 组件监控（待上线，`Type` 传参为 `SQL` 或 `NoSQL`）
  - 服务监控详情 > 组件监控（待上线）

使用本接口时请注意传参，尽量避免因传参导致的接口错误。



### 监控指标曲线

本接口为 [DescribeInvocationMetricDataCurve](https://cloud.tencent.com/document/product/649/70433)，API 各项参数请参考文档接口文档。

本接口用于查询监控指标的曲线统计图，在 TSF 控制台的接口包括了：

- 服务治理详情
- 服务监控详情

本接口支持的 Metric 和 Function 如下：

- REQUEST_COUNT（请求数量，支持 SUM）
- FAILURE_COUNT（请求失败数量，支持 SUM）
- FAILURE_RATE（请求失败率，支持 NONE）
- HTTP_STATUS_INFORMATIONAL（支持 SUM）
- HTTP_STATUS_SUCCESSFUL（支持 SUM）
- HTTP_STATUS_REDIRECTION（支持 SUM）
- HTTP_STATUS_CLIENT_ERROR（支持 SUM）
- HTTP_STATUS_SERVER_ERROR（支持 SUM）
- HTTP_STATUS_OTHER（支持 SUM）
- RESPONSE_TIME（支持 AVG, PERCENTAGE_50, PERCENTAGE_75, PERCENTAGE_95, PERCENTAGE_99）
- QPS（qps，支持 NONE）
- TOP_INTERFACE（最大的五个接口占比，支持 BUCKET_5）
- APDEX（apdex，支持 NONE）
- DURATION_MAX(最大调用延时，支持 MAX）

本接口支持的 MetricDimension 如下：ServiceName, OperationName, OperationMethod, PeerServiceName, PeerOperationName, DbName, Script。

本接口较复杂，建议尽量以控制台前端的传参为参考。



### 监控指标值

本接口为 [DescribeInvocationMetricDataPoint](https://cloud.tencent.com/document/product/649/70431)，API 各项参数请参考文档接口文档。

本接口用于查询监控指标的单个值，是一个聚合后的值，在 TSF 控制台的接口是：

- 服务监控详情 > 服务概览

本接口的参数取值可参考 DescribeInvocationMetricDataCurve 接口。



### 监控数据维度

本接口为 [DescribeInvocationMetricDataDimension](https://cloud.tencent.com/document/product/649/70432)，API 各项参数请参考文档接口文档。

本接口在 TSF 控制台的入口是：

- 服务监控详情 > 服务概览 > 请求概览 > 切换客户端与服务端



### 耗时分布散点图

本接口为 [DescribeInvocationMetricScatterPlot](https://cloud.tencent.com/document/product/649/70430)，API 各项参数请参考文档接口文档。

本接口用于查询耗时分布的散点图，在 TSF 控制台的接口是：

- 服务监控详情 > 服务概览 > 请求概览 > 响应耗时分布

本接口支持的 MetricDimension 包括了：NamespaceId, GroupId, InstanceId, OperationName, ServiceName, PeerServiceName, PeerOperationName。

本接口支持的 Metric 和 Function 如下：

- RANGE_COUNT_DURATION （响应耗时分布统计，支持 SUM）



### 服务监控指标

本接口为 [DescribeInovcationIndicators](https://cloud.tencent.com/document/product/649/70434)，API 各项参数请参考文档接口文档。

本接口在 TSF 控制台的入口是服务治理页面，主要配合其他服务相关接口获取服务的监控信息。

本接口的 Dimensions 传参选择 `Service`。



### Java 实例 JVM 监控数据

本接口为 [DescribeJvmMonitor](https://cloud.tencent.com/document/product/649/70429)，API 各项参数请参考文档接口文档。

本接口用于查询 Java 实例的 JVM 的监控信息，由 JVM Monitor 采集，若无 JVM 监控数据，请参阅前提条件中的 JVM 监控相关文档。注意 JVM 监控数据保留时间较短，若使用此接口，请尽量获取最近的数据。

本接口的 `RequiredPictures` 参数是以返回值属性名作为入参，具体请参阅接口文档。



## 说明与注意

- 由于监控接口较为复杂，建议根据 TSF 控制台前端的传参，确定 API 调用的传参。TSF 控制台前端接口可能有变化，以当前页面为准。
- TSF 会对接口调用做限频，请注意调用的频率。
- 本文涉及的各个监控数据接口在查询时间跨度较大时，需要较多的数据聚合操作。若出现接口超时，请减少查询时间跨度以保证数据正常返回。
- 若业务正常但无法查询到监控数据，请优先排查是否有监控数据落盘，路径为 `/data/tsf_apm/monitor/logs/`。若无落盘数据，请根据本文前提条件中的开发指南确认是否正确配置依赖。
- TSF 控制台上未开放的部分接口将在未来陆续开放。



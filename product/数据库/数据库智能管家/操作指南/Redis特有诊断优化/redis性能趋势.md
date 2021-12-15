
>?Redis 性能趋势与其他数据库略有不同，本篇单独介绍 Redis 性能趋势分析。

## 性能趋势简介
Redis 性能趋势支持多种性能指标的选择，实例（Redis 数据库实例）、Redis 节点（节点间，如A节点 - B节点之间）、Proxy（中间件集群节点）节点切换，性能指标选择，实时/历史视图切换，监控粒度切换，单个或对比视图切换，实例、Redis 节点、Proxy 节点的多种视图及对比视图等。

## 操作步骤
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain)，在左侧导航选择**诊断优化**，在上方选择对应数据库，选择**性能趋势**页。
![](https://main.qcloudimg.com/raw/83e776bc61da0ebd1f04229039efe63f.png)
2. 在性能趋势页，可查看各维度的监控、选择不同监控指标、过滤指标、切换视图、图表联动。
 - 监控维度：提供了 Redis 实例监控、Redis 节点监控、Proxy 节点监控。
    - 实例维度：展现实例的监控视图。
    - 节点维度：节点间，各指标的趋势对比查看。
    - Proxy 维度：展现各个 Proxy 里，有相关性的指标对比趋势查看。
![](https://main.qcloudimg.com/raw/f46b8fd4bb3986b12310c1c1e144b676.png)
 - 指标分类：CPU、内存、网络、时延、请求、响应。
![](https://main.qcloudimg.com/raw/2e54ccc455dcc65cadf0e9e273991ed1.png)
 - 性能指标选择方式：提供了全部指标、自定义指标，也支持多种视图的查看。
    - 全局指标过滤
![](https://main.qcloudimg.com/raw/1bc60f16953bb77f135a45233512131a.png)
    - 单个指标过滤
![](https://main.qcloudimg.com/raw/1db5aec77f505bb9ec0ebc1ae0211e46.png)
    - 视图切换
![](https://main.qcloudimg.com/raw/6293b9724851d03500376c1e0756d197.png)
 - 时间视图：提供实时/历史切换，根据时间视图的不同，也提供不同的监控粒度切换，同时也支持单个或对比视图的查看。
![](https://main.qcloudimg.com/raw/5bb111f73d01ecf757330d957073a8a7.png)
自定义多节点对比图。
![](https://main.qcloudimg.com/raw/32418a8351d22d38082ad5a9efd098fc.png)
 - 针对单个实例、单个节点、单个 Proxy：提供相关指标的联动对比趋势查看，也可添加自定义指标，还支持性能指标趋势的时间对比查看。
图表联动（各节点间、各实例的 Proxy 间，各指标的联动对比趋势查看）。
![](https://main.qcloudimg.com/raw/b75a315a12a66be1ddca9486c3611a79.png)


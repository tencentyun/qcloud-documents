
在 Redis 数据库中，我们将访问频率高的 Key 称为热点 Key，当 Redis 数据库请求过大时，多数请求又集中去访问 Redis 上的某个特定 key。这样会造成流量过于集中，触达物理网卡上限，从而导致 Redis 服务出现问题甚至宕机。

通过 DBbrain 的热 Key 分析系统，能够快速发现热点 Key，从而为服务优化提供基础。


## 查看热 Key 分析
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain)，在左侧导航选择**诊断优化**，在上方选择对应数据库，然后选择**延迟分析** > **热Key分析**页。
![](https://main.qcloudimg.com/raw/fb7c74e49a36c05c23a5c58de0ae60c0.png)
2. 在热 Key 分析页，支持实时和历史视图的切换查看。
 - 实时视图：支持实时查看每个时间点的分析。
![](https://main.qcloudimg.com/raw/3533b766179f3fa30984f1d20b207ed3.png)
 - 历史视图：支持查看近1小时、3小时、24小时、7天、自定义时间的分析。
![](https://main.qcloudimg.com/raw/e2ed6394d4d003b234f325ceb1ba6a46.png)

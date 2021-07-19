### 热Key分析
在Redis数据库中，我们将访问频率高的Key称为热点Key，当redis数据库请求过大时，多数请求又集中去访问redis上的某个特定key。这样会造成流量过于集中，触达物理网卡上限，从而导致redis服务问题甚至宕机。
通过DBbrain的热Key分析系统，能够快速发现热点Key，从而为服务优化提供基础。


### 查看热Key分析
登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain)，在左侧导航选择【诊断优化】，在上方选择对应数据库，然后选择【延迟分析】页，点击子页中的【热Key分析】。

![](https://main.qcloudimg.com/raw/fb7c74e49a36c05c23a5c58de0ae60c0.png)

1. 热Key分析支持实时及历史视图的切换查看



2. 实时视图：支持实时查看每个时间点的

![](https://main.qcloudimg.com/raw/3533b766179f3fa30984f1d20b207ed3.png)




3. 历史视图：支持查看近1小时、3小时、24小时、7天、自定义时间的

![](https://main.qcloudimg.com/raw/e2ed6394d4d003b234f325ceb1ba6a46.png)
## 功能描述
在 Redis 数据库中，我们将访问频率高的 Key 称为热点 Key，当 Redis 数据库请求过大时，多数请求又集中去访问 Redis 上的某个特定 key。这样会造成流量过于集中，触达物理网卡上限，从而导致 Redis 服务出现问题甚至宕机。
通过 DBbrain 的热 Key 分析功能，能够快速发现访问频次高的热点 Key，为数据库性能优化提供重要依据。

## 查看热 Key 分析数据

1. 登录 [Redis 控制台](https://console.cloud.tencent.com/redis)。
2. 在左侧导航栏，选择**诊断优化**。
3. 在**数据库智能管家 DBbrain** 的**诊断优化**页面上方，在**实例 ID** 的下拉列表选择需查看的实例。
![](https://qcloudimg.tencent-cloud.cn/raw/7c85143a0a36586321a27cc0845d7fcb.png)
4. 选择**延迟分析** > **热Key分析**页面，并在右上方**自动刷新**后面的下拉列表中设置采集粒度，支持5秒、15秒、30秒。
![img](https://main.qcloudimg.com/raw/3533b766179f3fa30984f1d20b207ed3.png)
5. 查看热 Key 统计数据，支持实时和历史视图的切换查看。
 - **实时视图**
   默认实时统计当前数据库热 key 的访问频次。
   ![img](https://main.qcloudimg.com/raw/3533b766179f3fa30984f1d20b207ed3.png)
 - **历史视图**
   单击**历史**，可直接查看近1小时、近3小时、24小时、近7天的统计数据。在时间选择框，单击<img src="https://qcloudimg.tencent-cloud.cn/raw/a1438740099d1baedaf57020fb2e397b.png" style="zoom: 50%;" />，也可选择近1个月连续7天以内的统计数据，即可查询近1个月内的数据，每次最长统计连续7天的数据。
	 ![img](https://main.qcloudimg.com/raw/e2ed6394d4d003b234f325ceb1ba6a46.png)
   

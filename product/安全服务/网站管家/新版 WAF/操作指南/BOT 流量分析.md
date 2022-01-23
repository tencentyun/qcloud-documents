## 背景信息
BOT 行为管理功能能够对友好及恶意机器人程序进行甄别分类，并采取针对性的流量管理策略。例如：放通搜索引擎类机器人流量；对恶意爬取商品信息流量采取不响应；减缓响应或差异化响应策略；应对恶意机器人程序爬取带来的资源消耗、信息泄露及无效营销问题，同时也保障友好机器人程序（如搜索引擎，广告程序）的正常运行。

BOT 流量分析通过采集 BOT 行为管理中的数据，可以快速了解选中并开启了 BOT 流量分析的域名受 BOT 影响的情况，快速得知当前域名的 BOT 分类趋势、处置趋势、BOT 得分分布、请求量 TOP 统计以及 url 易受侵害的资产 url 列表。


## 操作步骤
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-botconfig)，在左侧导航栏中，选择**报表** > **BOT 流量分析**，进入 BOT 流量分析页面。
2. 在 BOT 流量分析页面，单击左上角“全部域名”下拉框，选择要查看的域名。
3. 在选中非全部域名的情况下，单击左上角**查看配置**，会跳转至对应域名的 BOT 与业务安全页面。
![](https://qcloudimg.tencent-cloud.cn/raw/fa14f99c930a179fbb698b6db09bdde8.png)
4. 在 BOT 流量分析页面，可以通过时间或筛选器，搜索某个域名的防护数据。
    - 相关通过指定的时间范围，搜索某个域名在查询时间范围内的 BOT 防护效果数据。
        ![](https://qcloudimg.tencent-cloud.cn/raw/75c09cb693eb131978907ab496b61012.png)
    - 单击下方的**筛选器**，可出现 BOT 流量分析的过滤器，在此过滤器中将对应条件进行筛选。
    ![](https://qcloudimg.tencent-cloud.cn/raw/74029b7d14110ae26a40f53ea6aa6c86.png)
5.  在流量分类趋势模块，可查看当前选中的域名（可选全局域名）的 BOT 流量分类的趋势和 BOT 会话得分趋势。
   - BOT 流量分类趋势图：按照动作配置中相关动作的标签 BOT 得分进行不同分数段的分类，对每一个访问网站的流量请求进行打分并标记，展示到流量分类趋势图中。
    ![](https://qcloudimg.tencent-cloud.cn/raw/38d2ad52bc930a83eafc390c753997ca.png)
	- BOT 会话得分趋势为展示当前用户对应域名下的 BOT 流量风险分布图，用于展示用户当前的访问流量的趋势分布，用户可以根据此趋势分布进行 BOT 分数的动作设置对应处置。聚集的分数越高，当前受有害 BOT 影响越大。
 ![](https://qcloudimg.tencent-cloud.cn/raw/5fddac4cf8efd029007e1f85a73c1cfe.png)
6.  单击**流量处置趋势**，可查看当前选中的域名（可选全局域名）在不同时间中 BOT 行为管理对流量的相关处置情况，以及整体的 BOT 对所有请求流量的处置动作占比。
![](https://qcloudimg.tencent-cloud.cn/raw/535de2924da469660bf221959827c6d1.png)
7. 在请求量 TOP5 统计模块，展示对应时间段内 BOT 的相关特征，所统计出的 TOP5 键值及其数量。统计图受筛选器影响，受流量趋势对比图框选时间影响。单击对应的“柱状图”，会展示对应提示框，该提示框包含该键值的信息。单击**筛选**或**排除**，可以快速添加相关的过滤器。
![](https://qcloudimg.tencent-cloud.cn/raw/b5f23b550ae8bc67ee54371796f50cfd.png)
8. 在受侵害资产统计列表，展示受到 BOT 影响最多的 URL 资产，以及 BOT 行为管理对其访问进行的处置。
![](https://qcloudimg.tencent-cloud.cn/raw/f2b34a3fb6e02477b004c98e4eda6aec.png)
**字段说明**
 - 访问源：访问者来源。
 - 地理位置：访问者地理位置。
 - 访问目的：访问的域名。
 - 请求路径：访问请求的 uri。
 - BOT 动作：BOT 行为管理处置的动作。
 - 会话数：会话次数。
 - 命中模块：命中了哪些模块。
 - 攻击次数：执行处置动作的次数。
 - 发生时间：发现 BOT 访问的时间。
 - 查看日志：单击**查看日志**，可查看对应 BOT 的访问日志。
>?需已 [购买访问日志](https://cloud.tencent.com/document/product/627/11730#.E5.AE.89.E5.85.A8.E6.97.A5.E5.BF.97.E6.9C.8D.E5.8A.A1.E5.8C.85.E4.BB.B7.E6.A0.BC)。
>
![](https://qcloudimg.tencent-cloud.cn/raw/3681cecca0d9e455a62f4053c22c7753.png)
 - 更多：单击**更多** > **黑名单**，配置相关参数单击**确定**，即可将对应访问源的 IP 加入黑名单。
![](https://qcloudimg.tencent-cloud.cn/raw/642677a513384857a7ef96cf43de1103.png)

 
  

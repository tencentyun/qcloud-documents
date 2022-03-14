BOT 概览展示了网站业务的爬虫请求监控数据，以及防爬规则的防护效果数据。

## 前提条件
已购买[ Web 应用防火墙套餐](https://buy.cloud.tencent.com/buy/waf)，完成防护域名添加，域名处于正常防护状态，并且域名 BOT 检测功能已开通。
>? 
>- 只有 WAF 企业版和旗舰版支持 BOT 行为管理，高级版用户建议升级到企业版或旗舰版。
>- 完成 WAF 域名接入，并开启 WAF 防护开关。
>- 需开启 [BOT 防护设置](https://console.cloud.tencent.com/guanjia/bot2/config) 页面中对应域名的流量分析开关。

## 操作步骤
1. 登录 [Web 应用防火墙（WAF）控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，在左侧导航栏中，选择【BOT 行为管理】>【BOT 详情】>【BOT 概览】，进入 BOT 概览页面。
2. 在 BOT 概览页面，单击左上角“全部域名”下拉框，选择要查看的域名，通过指定的时间范围，搜索某个域名在查询时间范围内的 BOT 防护效果数据。
![](https://main.qcloudimg.com/raw/60658e59e6a8a8b59ad079abdc15dacc.png)
3. BOT 请求概览分布：可通过该页签快速发现域名的 BOT 相关关键指标。
![](https://main.qcloudimg.com/raw/7311541bb2083008d38801950cdc7819.png)
**统计项说明**：
 - 请求总量：统计 WAF 记录的检测请求总量，单击“数字”，可跳转到访问日志页面。
 - BOT 请求量：统计 WAF 分析出的BOT 请求数量，单击“数字”，可跳转到 BOT 报表详情页面。
 - BOT 个数：统计 WAF 检测出该域名的 BOT 数，包括未知类型、自定义类型和公开类型的 BOT 数量。单击“数字”，可跳转至动态行为分析，跟踪全部检测出的 BOT 的行为。
 - 未知类型：展示未知类型 BOT 数量，单击“数字”，可跳转至动态行为分析，跟踪未知类型 BOT 的行为。
 - 自定义类型： 展示自定义类型的 BOT 数量，单击“数字”，可跳转至动态行为分析，跟踪自定义类型 BOT 的行为。
 - 公开类型：展示公开类型的 BOT 数量，单击“数字”，可跳转至动态行为分析，跟踪公开类型的 BOT 的行为。
4. BOT 请求流量类型：展示在对应时间点 BOT 的分布情况。
![](https://main.qcloudimg.com/raw/eaeacd48f5bf3ce0c6b76d35e9b406ef.png)
5. BOT 请求量 TOP5 统计（域名）：展示在总体流量中，BOT 请求量 TOP5 的域名。单击可跳转到 BOT 报表详情页面。
![](https://main.qcloudimg.com/raw/e5340b2348c87323596def5eede4f661.png)
6. BOT 请求量 TOP5 统计（URL）：展示在总体流量中，BOT 请求量 TOP5 的 URL。单击可跳转到 BOT 报表详情页面。
![](https://main.qcloudimg.com/raw/f8cdaf80dc715e644a2870003db406a5.png)
7. BOT 类型占比：展示在总体流量中，各类型的 BOT 的占比。
![](https://main.qcloudimg.com/raw/d79b8e6521ac58c70f6f254d4b023c29.png)
8. BOT 动作占比：展示在总体流量中，对所有 BOT 的动作的占比。
![](https://main.qcloudimg.com/raw/f09de88f84eca5c87b103264f18fe7ed.png)

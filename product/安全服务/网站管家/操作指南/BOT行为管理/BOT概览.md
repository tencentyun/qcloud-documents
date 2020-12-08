
## 背景信息
WAF 的 BOT 行为管理能够对友好及恶意机器人程序进行甄别分类，并采取针对性的流量管理策略，例如，放通搜索引擎类机器人流量，对恶意爬取商品信息流量采取不响应、减缓响应或差异化响应策略，还能够应对恶意机器人程序爬取带来的资源消耗、信息泄露及无效营销问题，同时也保障友好机器人程序（如搜索引擎，广告程序）的正常运行。

通过 BOT 概览页面，可以快速了解 BOT 记录域名 TOP5 - 10 的情况。通过缩略图查看域名 BOT 类型、BOT 动作和 BOT 请求趋势,了解各个域名 BOT 访问占比和趋势概况。
## 使用说明
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/bot2/overview)，在左侧导航栏中，选择【BOT 行为管理】>【BOT 概览】，查看 BOT 行为概况。
2. 概览页默认提供 TOP5 域名的 BOT 记录概览，如用户需要查看更多域名概览，可以在页面右上角单击排名下拉框，查看 TOP10 的 BOT 记录概览。
![](https://main.qcloudimg.com/raw/668fadc23e7d3b23e7ba23fb55c25800.png)
**统计项说明：**
	- **BOT 记录数：**统计 WAF 检测出该域名的 BOT 数，以访问源 IP 作为统计维度，包括未知类型、自定义类型和公开类型的 BOT 数量。
	- **排名：**默认提供 TOP5 BOT 记录数域名排名，最多可以查看 TOP10 排名，如需查看更多域名，可到 [BOT 详情页](https://console.cloud.tencent.com/guanjia/bot2/record/overview) 进行查看。
3. 查看单个域名概览。BOT 概览最多提供 BOT 记录数 TOP10 域名的微缩图统计，可以快速查看域名的 BOT 类型、BOT 动作和 BOT 请求趋势信息。在左上角单击域名可以查看该域名的更多统计信息。
![](https://main.qcloudimg.com/raw/f756062a30ca4ab09be19bc371255536.png)
**统计项说明：**
	- **BOT 类型：**公开类型、未知类型和用户自定义类型，该域名检测出的 BOT 类型统计信息，并提供数量和占比。
	- **BOT 动作：**验证码、重定向、拦截和监控，该域名 BOT 记录触发的动作信息，并提供数量和占比。
	- **BOT 请求趋势：**展示总请求和 BOT 请求趋势图。

## 相关信息
#### BOT 防护设置
若您需根据 BOT 会话行为特征设置 BOT 对抗策略，对 BOT 行为进行动作处理，并结合 BOT 详情进行观察和分析，同时需要进行精细化策略设置，保护网站核心接口和业务的安全，请参见 [BOT 防护设置](http://yehe.isd.com/document/doc-cn/product-article/627/40157)。
#### BOT 详情
若您如需查看域名正常请求和 BOT 请求次数的访问趋势，查看未知类型 BOT、公开类型 BOT和自定义类型 BOT详情，或需要了解 WAF 检测检出的 BOT 会话详情，请参见 [BOT 详情](https://cloud.tencent.com/document/product/627/40158)。

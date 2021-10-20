## 功能简介

安全加速 SCDN 提供实时监控与数据统计功能。进入控制台 [攻击监控](https://console.cloud.tencent.com/cdn/scdn/statistics?tab=cc)，您可以查看域名的 CC 攻击监控数据。



## 页面说明

1. 查询条件筛选
	- 在页面左上角设置查询时间范围。单击域名筛选框，进行域名选择或搜索。
	- 选择防护地域和执行防护动作，单击**查询**可查看所选时间段内攻击数据。
	![](https://qcloudimg.tencent-cloud.cn/raw/2654b964286a57e6be9a91ca56da4c2d.jpg)
2. 查看监控数据
CC 攻击监控数据分为四个模块：请求数视图、QPS 视图、攻击源排名、攻击请求 TOP UA。
	- 请求数视图：从请求数维度展示 CC 攻击情况。
	![](https://qcloudimg.tencent-cloud.cn/raw/92e35603d433116a35bf0b75ca0f022c.jpg)
	- QPS 视图：即请求量视图，展示服务器在单位时间内处理的 CC 攻击流量，计算公式为：QPS = 并发量/平均响应时间。该视图支持不同时间粒度（每分钟/每5分钟/每小时）QPS 历史数据查询，支持数据下载。
	![](https://qcloudimg.tencent-cloud.cn/raw/c21b7e9e88063ca072fc5bc9e44a75f0.jpg)
	- 攻击源排名：根据攻击源 IP 的总攻击次数（从多到少）展示历史数据排名。该模块展示攻击域名、攻击源 IP、目标 URL、总攻击次数信息，支持数据下载。
	![](https://qcloudimg.tencent-cloud.cn/raw/f44e81812eb3fae03d16a1f803ab5513.jpg)
	- 攻击请求 TOP UA：根据攻击源 User-Agent 的总攻击次数（从多到少）展示 TOP UA 排名。该模块展示攻击域名、User-Agent、总攻击次数信息。
	![](https://qcloudimg.tencent-cloud.cn/raw/b7b8e3cfd3ad6db1ca40e1bfae8aedcb.jpg)

>? CC 攻击监控展示内容为新版七层流量攻击防护监控数据。

## 功能简介

安全加速 SCDN 提供实时监控与数据统计功能。进入控制台 [攻击监控](https://console.cloud.tencent.com/cdn/scdn/statistics?tab=cc)，您可以查看域名的 CC 攻击监控数据。



## 页面说明

### 查询条件筛选
- 在页面左上角设置查询时间范围。单击域名筛选框，进行域名选择或搜索。
- 选择防护地域和执行防护动作，单击**查询**可查看所选时间段内攻击数据。
![](https://qcloudimg.tencent-cloud.cn/raw/51190ee29f3effb83330beec55f72317.jpg)
	
### 查看监控数据
CC 攻击监控数据分为四个模块：请求数视图、QPS 视图、攻击源排名、攻击请求 TOP UA。
1. 请求数视图：从请求数维度展示 CC 攻击情况，支持数据下载。
![](https://qcloudimg.tencent-cloud.cn/raw/784d08ef62594fb93b4ee0c67a6239f5.jpg)
2. QPS 视图：即请求量视图，展示服务器在单位时间内处理的 CC 攻击流量，计算公式为：QPS = 并发量/平均响应时间。该视图支持不同时间粒度（每分钟/每5分钟/每小时）QPS 历史数据查询。
![](https://qcloudimg.tencent-cloud.cn/raw/a728c0d3d27ead9312862d120a4ed92f.jpg)
3. 攻击源排名：根据攻击源 IP 的总攻击次数（从多到少）展示历史数据排名。该模块展示攻击域名、攻击源 IP、目标 URL、总攻击次数信息。
![](https://qcloudimg.tencent-cloud.cn/raw/5654b17d09ec4c985703b17e4c11a8a9.jpg)
4. 攻击请求 TOP UA：根据攻击源 User-Agent 的总攻击次数（从多到少）展示 TOP UA 排名。该模块展示攻击域名、User-Agent、总攻击次数信息。
![](https://qcloudimg.tencent-cloud.cn/raw/be6912b043a9d74df1c32aab09e2f2b4.jpg)

>? CC 攻击监控展示内容为新版七层流量攻击防护监控数据。

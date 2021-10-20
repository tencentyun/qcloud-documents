## 功能简介

安全加速 SCDN 提供实时监控与数据统计功能。进入控制台 [攻击监控](https://console.cloud.tencent.com/cdn/scdn/statistics?tab=waf)，您可以查看域名的 Web 攻击监控数据。



## 页面说明

1. 筛选查询条件
	- 在页面左上角设置查询时间范围。单击域名筛选框，进行域名选择或搜索。
	- 选择防护地域和攻击类型，单击**查询**可查看所选时间段内攻击数据。
![](https://qcloudimg.tencent-cloud.cn/raw/664dcd8901c943d2714b9d8d8fbaf123.jpg)
2. 查看监控数据
Web 攻击监控数据分为四个模块：Web 攻击次数、域名排行、类型分布、攻击次数排行。
**Web 攻击次数**：根据上方筛选条件，展示 Web 攻击次数监控数据。支持选择不同的统计时间粒度（每分钟/每5分钟/每小时）查看 Web 攻击次数，支持数据下载。 
![](https://qcloudimg.tencent-cloud.cn/raw/087f08989f5c8cae2c9ecd81795d24a2.jpg)
**域名排行**：根据上方筛选条件，从大到小展示被 Web 攻击的域名、攻击次数以及攻击占比。其中，攻击占比=该域名被 Web 攻的次数/整个账号被 Web 攻击的总次数。 
![](https://qcloudimg.tencent-cloud.cn/raw/e8c8812775721ace7ebaba577a95e57c.jpg)
**类型分布**：监控页面按攻击类型进行 Web 攻击数据展示。
![](https://qcloudimg.tencent-cloud.cn/raw/b758dc94656a2efe1bdb15eb8d2c0277.jpg)
**攻击次数排行**：支持 “URL” 或者“攻击源 IP” 筛选，展示攻击次数排行。
![](https://qcloudimg.tencent-cloud.cn/raw/4a051600657a394f73909582ccc941ca.jpg)
 - 若选中 “URL”，则展示域名、URL、总攻击次数、最后攻击时间。
 - 若选中“攻击源 IP”，则展示攻击 IP、IP 所属地区、总攻击次数、最后攻击时间。

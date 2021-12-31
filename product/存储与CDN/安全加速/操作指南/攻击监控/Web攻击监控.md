## 功能简介

安全加速 SCDN 提供实时监控与数据统计功能。进入控制台 [攻击监控](https://console.cloud.tencent.com/cdn/scdn/statistics?tab=waf)，您可以查看域名的 Web 攻击监控数据。



## 页面说明

###  筛选查询条件
- 在页面左上角设置查询时间范围。单击域名筛选框，进行域名选择或搜索。
- 选择防护地域和攻击类型，单击**查询**可查看所选时间段内攻击数据。
![](https://qcloudimg.tencent-cloud.cn/raw/286b0d74a6f61ecd2676790540a8fd26.jpg)

### 查看监控数据
Web 攻击监控数据分为四个模块：Web 攻击次数、域名排行、类型分布、攻击次数排行。
1. Web 攻击次数：根据上方筛选条件，展示 Web 攻击次数监控数据。支持选择不同的统计时间粒度（每分钟/每5分钟/每小时）查看 Web 攻击次数，支持数据下载。 
![](https://qcloudimg.tencent-cloud.cn/raw/aa4bfab9dab5feec9d30c1c027611e9d.jpg)
2. 域名排行：根据上方筛选条件，从大到小展示被 Web 攻击的域名、攻击次数以及攻击占比。其中，攻击占比=该域名被 Web 攻的次数/整个账号被 Web 攻击的总次数。 
![](https://qcloudimg.tencent-cloud.cn/raw/81d0dc4fc8aa8b666cf03f4e5d82d763.jpg)
3. 类型分布：监控页面按攻击类型进行 Web 攻击数据展示。
![](https://qcloudimg.tencent-cloud.cn/raw/b069c75ed7a5c0539319ba2dee21d365.jpg)
4. 攻击次数排行：支持 “URL” 或者“攻击源 IP” 筛选，展示攻击次数排行。
![](https://qcloudimg.tencent-cloud.cn/raw/2bc0656ebaf06a3c8ebb8cd4aabb55ab.jpg)
 - 若选中 “URL”，则展示域名、URL、总攻击次数、最后攻击时间。
 - 若选中“攻击源 IP”，则展示攻击 IP、IP 所属地区、总攻击次数、最后攻击时间。

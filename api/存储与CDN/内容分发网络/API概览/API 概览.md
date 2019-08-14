## 计费管理

| 接口名       | Action Name                                                  | 功能描述         | 鉴权配置       |
| ------------ | ------------------------------------------------------------ | ---------------- | -------------- |
| 查询计费方式 | [GetPayType](https://cloud.tencent.com/document/product/228/15286) | 查询账号计费方式 | 暂不支持子账号 |
| 修改计费方式 | [UpdatePayType](https://cloud.tencent.com/document/product/228/14973) | 修改账号计费方式 | 暂不支持子账号 |

## 域名管理

| 接口名        | Action Name                                                  | 功能描述         | 鉴权配置   |
| ------------- | ------------------------------------------------------------ | ---------------- | ---------- |
| 新增加速域名  | [AddCdnHost](https://cloud.tencent.com/document/product/228/1406) | 添加域名至 CDN   | 支持子账号 |
| 开启 CDN 域名 | [OnlineHost](https://cloud.tencent.com/document/product/228/1402) | 启动域名加速服务 | 支持子账号 |
| 关闭 CDN 域名 | [OfflineHost](https://cloud.tencent.com/document/product/228/1403) | 关闭域名加速服务 | 支持子账号 |
| 删除加速域名  | [DeleteCdnHost](https://cloud.tencent.com/document/product/228/1396) | 删除加速域名     | 支持子账号 |

## 配置管理

| 接口名           | Action Name                                                  | 功能描述                                                     | 鉴权配置       |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------- |
| 修改域名配置     | [UpdateCdnConfig](https://cloud.tencent.com/document/product/228/3933) | 修改域名加速配置，支持以下配置项修改：<br/>修改源站配置<br/>修改备站信息<br/>修改回源 host<br/>开启/关闭过滤参数<br/>修改 refer 黑白名单配置<br/>修改 IP 黑白名单配置<br/>开启/关闭视频拖拽<br/>修改缓存过期时间配置<br/>开启/关闭高级缓存过期配置<br/>开启/关闭中间源配置<br/>配置带宽封顶<br/>设置 response header<br/>设置 request header<br/>设置 SEO 优化<br/>设置 302 回源跟随<br/>设置 range 回源<br/>设置 IP 访问限频 | 支持子账号     |
| HTTPS 配置        | [SetHttpsInfo](https://cloud.tencent.com/document/product/228/12965) | 支持上传证书配置 https 加速<br/>修改回源方式为协议跟随或 HTTP 回源<br/>HTTPS强制跳转配置修改 | 暂不支持子账号 |
| 切换域名所属项目 | [UpdateCdnProject](https://cloud.tencent.com/document/product/228/3935) | 修改域名所属项目                                             | 暂不支持子账号 |

## 配置查询

| 接口名               | Action Name                                                  | 功能描述           | 鉴权配置       |
| -------------------- | ------------------------------------------------------------ | ------------------ | -------------- |
| 域名列表查询         | [DescribeCdnHosts](https://cloud.tencent.com/document/product/228/3937) | 域名配置查询       | 暂不支持子账号 |
| 域名配置查询（域名） | [GetHostInfoByHost](https://cloud.tencent.com/document/product/228/3938) | 指定域名查询配置   | 支持子账号     |
| 域名配置查询（Id）   | [GetHostInfoById](https://cloud.tencent.com/document/product/228/3939) | 指定域名 ID 查询配置 | 支持子账号     |

## 数据查询

| 接口名              | Action Name                                                  | 功能描述                                                     | 鉴权配置       |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------- |
| 汇总统计查询        | [DescribeCdnHostInfo](https://cloud.tencent.com/document/product/228/13022) | 域名指定时间区间以下总统计项查询：<br/>峰值带宽<br/>总流量<br/>总请求数<br/>平均请求数命中率 | 支持子账号     |
| 消耗明细查询        | [GetCdnHostsDetailStatistics](https://cloud.tencent.com/document/product/228/13026) | 域名指定时间区间以下统计项明细查询：<br/>带宽明细<br/>流量明细<br/>请求数明细<br/>命中流量明细<br/>命中请求数明细<br/>状态码明细 | 支持子账号     |
| 回源统计明细查询    | [GetCdnOriginStat](https://cloud.tencent.com/document/product/228/13211) | 域名指定时间区间以下统计项回源明细查询：<br/>回源带宽明细<br/>回源流量明细<br/>回源请求数明细<br/>回源失败请求数明细 | 暂不支持子账号 |
| TOP URL 查询         | [GetCdnStatTop](https://cloud.tencent.com/doc/api/231/3944)  | 指定流量/请求数排序以下维度统计：<br/>TOP 1000 URL统计<br/>省份排序<br/>运营商排序 | 支持子账号     |
| 运营商/省份明细查询 | [GetCdnProvIspDetailStat](https://cloud.tencent.com/document/product/228/7356) | 指定省份、运营商带宽明细查询                                 | 支持子账号     |

## 刷新预热

| 接口名           | Action Name                                                  | 功能描述                             | 鉴权配置       |
| ---------------- | ------------------------------------------------------------ | ------------------------------------ | -------------- |
| 查询刷新记录     | [GetCdnRefreshLog](https://cloud.tencent.com/doc/api/231/3948) | 查询提交的刷新任务执行状态           | 支持子账号     |
| URL 刷新          | [RefreshCdnUrl](https://cloud.tencent.com/doc/api/231/3946)  | 提交 URL 刷新                          | 支持子账号     |
| 目录刷新         | [RefreshCdnDir](https://cloud.tencent.com/doc/api/231/3947)  | 提交目录刷新                         | 支持子账号     |
| URL 预热          | [CdnPusherV2](https://cloud.tencent.com/document/product/228/15164) | 提交 URL 预热（内测中）                | 支持子账号     |
| URL 预热（新）    | [CdnUrlPusher](https://cloud.tencent.com/document/product/228/12839) | 提交 URL 预热（内测中）                | 暂不支持子账号 |
| 查询预热记录     | [GetPushLogs](https://cloud.tencent.com/document/product/228/12840) | 查询提交的预热任务执行状态（内测中） | 支持子账号     |
| 一键刷新大陆境外 | [FlushOrPushOverall](https://cloud.tencent.com/document/product/228/12841) | 提交 URL 同时刷新大陆&境外 CDN 资源      | 暂不支持子账号 |


## 日志查询

| 接口名               | Action Name                                                  | 功能描述                                                     | 鉴权配置   |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- |
| 查询日志下载链接(V1) | [GenerateLogList](https://cloud.tencent.com/doc/api/231/3950) | 根据用户输入的域名 ID（仅支持一个）<br/>查询该域名一个月内每天的日志下载链接 | 支持子账号 |
| 查询日志下载链接(V2) | [GetCdnLogList](https://cloud.tencent.com/document/product/228/8087) | 根据用户输入的域名<br>查询指定时间区间的日志下载链接         | 支持子账号 |

## 服务查询

| 接口名       | Action Name                                                  | 功能描述                             | 鉴权配置 |
| ------------ | ------------------------------------------------------------ | ------------------------------------ | -------- |
| IP 归属查询  | [QueryCdnIp](https://cloud.tencent.com/document/product/228/12964) | 查询指定 IP 是否归属于腾讯云 CDN     | 公开接口 |
| 服务状态查询 | [GetCdnMonitorData](https://cloud.tencent.com/document/product/228/13218) | 查询 CDN 大盘响应时间/可用性监控数据 | 公开接口 |






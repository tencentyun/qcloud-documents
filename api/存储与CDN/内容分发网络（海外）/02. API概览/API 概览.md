境外 CDN 会逐步开放更多 API 供您使用。

### 1. 境外统计数据查询

| 接口名                 | Action Name                                                  | 功能描述                                                     |
| :--------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 消耗统计查询           | [GetCdnOverseaStat](https://cloud.tencent.com/document/api/228/7341) | 查询指定域名、指定日期的消耗统计信息，包括流量统计明细和带宽统计明细。 |
| 境外访问情况明细查询   | [GetCdnOverseaPv](https://cloud.tencent.com/document/api/228/7342) | 查询指定域名、指定日期的请求数、请求数命中率、IP 访问数统计信息。 |
| 状态码统计查询         | [GetCdnOverseaStatusCode](https://cloud.tencent.com/document/api/228/7343) | 根据域名、日期查询状态码明细，包括2XX、3XX、4XX、5XX。         |
| 运营商地区消耗明细     | [GetCdnOverseaProvIspDetailStat](https://cloud.tencent.com/document/api/228/7344) | 根据域名、日期、地区运营商查看带宽、请求数、流量消耗明细。     |
| 境外流量 TOP 查询        | [GetCdnOverseaStatTop](https://cloud.tencent.com/document/api/228/18003) | 查询多域名/项目指定时间区间按流量排名的 TOP 1000 URL 列表。    |
| 运营商地区回源消耗明细 | [GetCdnOverseaProvIspHyDetailStat](https://cloud.tencent.com/document/api/228/7422) | 查询指定日期、指定运营商、指定地区、指定域名的回源带宽/流量明细，时间粒度为5分钟，一天288个统计点。 |
| 境外请求数 TOP 查询      | [GetCdnStatTop](https://cloud.tencent.com/document/api/228/18004) | 查询多域名/项目指定时间区间请求数 TOP 1000 URL 列表排名。      |

### 2. 境外刷新预热

| 接口名           | Action Name                                                  | 功能描述                                                     |
| :--------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 境外 URL 刷新    | [RefreshCdnOverSeaUrl](https://cloud.tencent.com/document/api/228/7346) | 根据提交的资源 URL（可多个），将对应资源从境外节点中删除，此时再有用户访问，会直接回源站获取最新内容。 |
| 查询境外刷新纪录 | [GetCdnOverseaRefreshLog](https://cloud.tencent.com/document/api/228/7347) | 根据用户输入的信息，如时间、URL，查询对应的境外刷新记录。      |
| 境外 URL 预热    | [CdnOverseaPushser](https://cloud.tencent.com/document/api/228/7359) | 根据提交的资源URL（可多个），将对应资源缓存在境外节点中，此时有用户访问，将直接在境外节点获取资源。 |
| 查询境外预热记录 | [GetCdnOverseaPushLogs](https://cloud.tencent.com/document/api/228/7360) | 根据用户输入的信息，如时间、URL，查询对应的境外预热记录。      |
| 境外刷新目录     | [RefreshCdnOverSeaDir](https://cloud.tencent.com/document/api/228/7389) | 将节点上指定资源目录下的内容设置为过期。                       |

### 3. 域名查询

| 接口名              | Action Name                                                  | 功能描述                            |
| ------------------- | ------------------------------------------------------------ | ----------------------------------- |
| 境外 CDN 开通状态查询 | [GetCdnOverseaOpenStat](https://cloud.tencent.com/document/api/228/20000) | 查询当前帐号境外 CDN 服务的开通状态。 |

### 4. 域名管理

| 接口名           | Action Name                                                  | 功能描述                        |
| ---------------- | ------------------------------------------------------------ | ------------------------------- |
| 新增境外加速域名 | [AddCdnOvHost](https://cloud.tencent.com/document/api/228/9814) | 新增境外加速域名。                |
| 更新境外域名     | [UpdateCdnOverseaConfig](https://cloud.tencent.com/document/api/228/10939) | 更新某个境外域名的 CDN 服务配置。 |
| 上线境外域名     | [OnlineOvHost](https://cloud.tencent.com/document/api/228/10941) | 上线某个境外域名的 CDN 服务。     |
| 下线境外域名     | [OfflineOvHost](https://cloud.tencent.com/document/api/228/10945) | 下线某个境外域名的 CDN 服务。     |
| 删除境外域名     | [DeleteCdnOvHost](https://cloud.tencent.com/document/api/228/10946) | 删除一个境外 CDN 域名。           |

### 5. 证书管理

| 接口名                         | Action Name                                                  | 功能描述                                                   |
| ------------------------------ | ------------------------------------------------------------ | ---------------------------------------------------------- |
| 查询腾讯云 SSL 托管 HTTPS 证书信息 | [GetHostCertList](https://cloud.tencent.com/document/api/228/12543) | 查询用户托管在腾讯云 SSL 上的 HTTPS 证书 ID 等信息，支持分页查询。 |
| 查询 HTTPS 证书信息              | [GetCertificates](https://cloud.tencent.com/document/api/228/10938) | 查询用户的 HTTPS 证书信息，支持分页查询。                      |

### 6. 境外域名查询

| 接口名               | Action Name                                                  | 功能描述                                                     |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 查询境外域名信息     | [DescribeOverseaCdnHosts](https://cloud.tencent.com/document/api/228/8653) | 查询所有域名的详细信息，包括配置信息，支持分页查询。           |
| 查询境外域名详细信息 | [GetCdnOvHostInfo](https://cloud.tencent.com/document/api/228/10947) | 查询某个境外 CDN 域名的详细信息。                              |
| 查询境外域名接入情况 | [CheckOvHost](https://cloud.tencent.com/document/api/228/10948) | 查询某个域名是否已经接入腾讯云 CDN 服务。如果未接入，返回该域名的顶级域名。 |
| 查询域名历史操作清单 | [GetOverseaOpList](https://cloud.tencent.com/document/api/228/10949) | 查询用户对某个域名的历史操作记录清单。                         |

### 7. 境外日志下载

| 接口名           | Action Name                                                  | 功能描述                                                     |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 境外日志下载接口 | [GetOverseaCdnLogList](https://cloud.tencent.com/document/api/228/8703) | 查询指定时间区间内，指定域名境外加速日志的下载链接，一次仅可指定一个域名进行查询。 |

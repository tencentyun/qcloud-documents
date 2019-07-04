境外 CDN 会逐步开放更多 API 供您使用。

### 1. 境外统计数据查询
<table>
<thead>
<tr>
<th align="left" width="20%">接口名</th>
<th align="left" width="30%">Action Name</th>
<th align="left" width="50%">功能描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">消耗统计查询</td>
<td align="left"><a href="https://cloud.tencent.com/document/api/228/7341" target="_blank">GetCdnOverseaStat</a></td>
<td align="left">查询指定域名、指定日期的消耗统计信息，包括流量统计明细和带宽统计明细。</td>
</tr>
<tr>
<td align="center">境外访问情况明细查询</td>
<td align="left"><a href="https://cloud.tencent.com/document/api/228/7342" target="_blank">GetCdnOverseaPv</a></td>
<td align="left">查询指定域名、指定日期的请求数、请求数命中率、IP 访问数统计信息。</td>
</tr>
<tr>
<td align="left">状态码统计查询</td>
<td align="left"><a href="https://cloud.tencent.com/document/api/228/7343" target="_blank">GetCdnOverseaStatusCode</a></td>
<td align="left">根据域名、日期查询状态码明细，包括2XX、3XX、4XX、5XX。</td>
</tr>
<tr>
<td align="left">运营商地区消耗明细</td>
<td align="left"><a href="https://cloud.tencent.com/document/api/228/7344" target="_blank">GetCdnOverseaProvIspDetailStat</a></td>
<td align="left">根据域名、日期、地区运营商查看带宽、请求数、流量消耗明细。</td>
</tr>
<tr>
<td align="left">境外流量 TOP 查询</td>
<td align="left"><a href="https://cloud.tencent.com/document/api/228/18003" target="_blank">GetCdnOverseaStatTop</a></td>
<td align="left">查询多域名/项目指定时间区间按流量排名的 TOP 1000 URL 列表。</td>
</tr>
<tr>
<td align="left">运营商地区回源消耗明细</td>
<td align="left"><a href="https://cloud.tencent.com/document/api/228/7422" target="_blank">GetCdnOverseaProvIspHyDetailStat</a></td>
<td align="left">查询指定日期、指定运营商、指定地区、指定域名的回源带宽/流量明细，时间粒度为5分钟，一天288个统计点。</td>
</tr>
<tr>
<td align="left">境外请求数 TOP 查询</td>
<td align="left"><a href="https://cloud.tencent.com/document/api/228/18004" target="_blank">GetCdnStatTop</a></td>
<td align="left">查询多域名/项目指定时间区间请求数 TOP 1000 URL 列表排名。</td>
</tr>
</tbody></table>

### 2. 境外刷新预热
<table>
<thead>
<tr>
<th align="left" width="20%">接口名</th>
<th align="left" width="30%">Action Name</th>
<th align="left" width="50%">功能描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">境外 URL 刷新</td>
<td align="left"><a href="https://cloud.tencent.com/document/api/228/7346" target="_blank">RefreshCdnOverSeaUrl</a></td>
<td align="left">根据提交的资源 URL（可多个），将对应资源从境外节点中删除，此时再有用户访问，会直接回源站获取最新内容。</td>
</tr>
<tr>
<td align="left">查询境外刷新纪录</td>
<td align="left"><a href="https://cloud.tencent.com/document/api/228/7347" target="_blank">GetCdnOverseaRefreshLog</a></td>
<td align="left">根据用户输入的信息，如时间、URL，查询对应的境外刷新记录。</td>
</tr>
<tr>
<td align="left">境外 URL 预热</td>
<td align="left"><a href="https://cloud.tencent.com/document/api/228/7359" target="_blank">CdnOverseaPushser</a></td>
<td align="left">根据提交的资源URL（可多个），将对应资源缓存在境外节点中，此时有用户访问，将直接在境外节点获取资源。</td>
</tr>
<tr>
<td align="left">查询境外预热记录</td>
<td align="left"><a href="https://cloud.tencent.com/document/api/228/7360" target="_blank">GetCdnOverseaPushLogs</a></td>
<td align="left">根据用户输入的信息，如时间、URL，查询对应的境外预热记录。</td>
</tr>
<tr>
<td align="left">境外刷新目录</td>
<td align="left"><a href="https://cloud.tencent.com/document/api/228/7389" target="_blank">RefreshCdnOverSeaDir</a></td>
<td align="left">将节点上指定资源目录下的内容设置为过期。</td>
</tr>
</tbody></table>

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

<table>
<thead>
<tr>
<th width="20%">接口名</th>
<th width="30%">Action Name</th>
<th width="50%">功能描述</th>
</tr>
</thead>
<tbody><tr>
<td>查询境外域名信息</td>
<td><a href="https://cloud.tencent.com/document/api/228/8653" target="_blank">DescribeOverseaCdnHosts</a></td>
<td>查询所有域名的详细信息，包括配置信息，支持分页查询。</td>
</tr>
<tr>
<td>查询境外域名详细信息</td>
<td><a href="https://cloud.tencent.com/document/api/228/10947" target="_blank">GetCdnOvHostInfo</a></td>
<td>查询某个境外 CDN 域名的详细信息。</td>
</tr>
<tr>
<td>查询境外域名接入情况</td>
<td><a href="https://cloud.tencent.com/document/api/228/10948" target="_blank">CheckOvHost</a></td>
<td>查询某个域名是否已经接入腾讯云 CDN 服务。如果未接入，返回该域名的一级域名。</td>
</tr>
<tr>
<td>查询域名历史操作清单</td>
<td><a href="https://cloud.tencent.com/document/api/228/10949" target="_blank">GetOverseaOpList</a></td>
<td>查询用户对某个域名的历史操作记录清单。</td>
</tr>
</tbody></table>

### 7. 境外日志下载
<table>
<thead>
<tr>
<th width="20%">接口名</th>
<th width="30%">Action Name</th>
<th width="50%">功能描述</th>
</tr>
</thead>
<tbody><tr>
<td>境外日志下载接口</td>
<td><a href="https://cloud.tencent.com/document/api/228/8703" target="_blank">GetOverseaCdnLogList</a></td>
<td>查询指定时间区间内，指定域名境外加速日志的下载链接，一次仅可指定一个域名进行查询。</td>
</tr>
</tbody></table>

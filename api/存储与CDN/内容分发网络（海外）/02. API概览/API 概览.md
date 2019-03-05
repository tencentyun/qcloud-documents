境外 CDN 会逐步开放更多API供您使用。

## 1. 境外统计数据查询

| 接口名       | Action Name                              | 功能描述                             |
| --------- | ---------------------------------------- | -------------------------------- |
| 消耗明细查询    | [GetCdnOverseaStat](https://cloud.tencent.com/doc/api/445/6394) | 根据域名、日期查询消耗明细                    |
| 请求数明细查询   | [GetCdnOverseaPv](https://cloud.tencent.com/doc/api/445/6395) | 根据域名、日期查询请求数明细                   |
| 状态码明细查询   | [GetCdnOverseaStatusCode](https://cloud.tencent.com/doc/api/445/6396) | 根据域名、日期查询状态码明细，包括2XX、3XX、4XX、5XX |
| 运营商地区消耗明细 | [GetCdnOverseaProvIspDetailStat](https://cloud.tencent.com/doc/api/445/7192) | 根据域名、日期、地区运营商查看带宽、请求数、流量消耗明细     |

## 2. 境外刷新预热

| 接口名      | Action Name                              | 功能描述                                     |
| -------- | ---------------------------------------- | ---------------------------------------- |
| 境外 URL 刷新  | [RefreshCdnOverSeaUrl](https://cloud.tencent.com/doc/api/445/6709) | 根据提交的资源URL（可多个），将对应资源从境外节点中删除，此时再有用户访问，会直接回源站获取最新内容 |
| 查询境外刷新纪录 | [GetCdnOverseaRefreshLog](https://cloud.tencent.com/doc/api/445/6710) | 根据用户输入的信息，如时间、URL，查询对应的境外刷新记录            |
| 境外 URL 预热  | [CdnOverseaPushser](https://cloud.tencent.com/doc/api/445/6711) | 根据提交的资源URL（可多个），将对应资源缓存在境外节点中，此时有用户访问，将直接在境外节点获取资源 |
| 查询境外预热记录 | [GetCdnOverseaPushLogs](https://cloud.tencent.com/doc/api/445/6712) | 根据用户输入的信息，如时间、URL，查询对应的境外预热记录            |


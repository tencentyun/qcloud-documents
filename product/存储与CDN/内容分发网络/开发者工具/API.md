腾讯云CDN为广大开发者提供多种API接口，便于满足不同开发者的运维习惯，详细内容，请参考：[腾讯云API文档](http://cloud.tencent.com/doc/api/231/%E7%AE%80%E4%BB%8B) 。

腾讯云CDN为您提供了以下API接口：

##### 域名管理接口

| 接口名       | Action Name                              | 功能描述                                     |
| --------- | ---------------------------------------- | ---------------------------------------- |
| 新增加速域名    | [AddCdnHost](https://cloud.tencent.com/doc/api/231/1406) | 添加域名至 CDN，用户可以将自己的域名添加到 CDN              |
| 开启 CDN 域名 | [OnlineHost](https://cloud.tencent.com/doc/api/231/1402) | 根据域名 ID 启动该域名的加速服务                       |
| 关闭 CDN 域名 | [OfflineHost](https://cloud.tencent.com/doc/api/231/1403) | 根据域名 ID 关闭该域名的加速服务，此时对域名下资源的访问均为 404     |
| 删除加速域名    | [DeleteCdnHost](https://cloud.tencent.com/doc/api/231/1396) | 根据域名 ID 删除该域名，删除域名的状态必须为下线状态             |
| 修改源站配置    | [UpdateCdnHost](https://cloud.tencent.com/doc/api/231/1397) | 根据域名 ID 和域名，设置源站信息，可以设置为一个源站域名（支持域名：PORT），或设置多个源站 IP（支持IP：PORT），端口仅支持大于 0 小于等于 65535 |
| 修改域名配置    | [UpdateCdnConfig](https://cloud.tencent.com/doc/api/231/3933) | 根据域名 ID 和项目 ID，设置域名对应的缓存配置、缓存模式、防盗链配置、回源HOST配置、全路径缓存配置、源站配置等 |
| 设置缓存规则    | [UpdateCache](https://cloud.tencent.com/doc/api/231/3934) | 根据域名 ID，设置域名对应的缓存规则                      |
| 切换域名所属项目  | [UpdateCdnProject](https://cloud.tencent.com/doc/api/231/3935) | 根据域名 ID，并指定需要切换到的项目 ID，进行项目间切换           |

##### 域名查询接口

| 接口名            | Action Name                              | 功能描述                             |
| -------------- | ---------------------------------------- | -------------------------------- |
| 查询域名信息         | [DescribeCdnHosts](https://cloud.tencent.com/doc/api/231/3937) | 查询所有域名详细信息，包括所有配置信息，支持分页查询       |
| 根据域名查询域名信息     | [GetHostInfoByHost](https://cloud.tencent.com/doc/api/231/3938) | 查询指定域名对应的域名详情，支持多个域名一起查询         |
| 根据域名 ID 查询域名信息 | [GetHostInfoById](https://cloud.tencent.com/doc/api/231/3939) | 查询指定域名 ID 对应的域名详情，支持多个域名 ID 一起查询 |

##### 消耗及统计量查询接口

| 接口名          | Action Name                              | 功能描述                                     |
| ------------ | ---------------------------------------- | ---------------------------------------- |
| 查询CDN消耗统计    | [DescribeCdnHostInfo](https://cloud.tencent.com/doc/api/231/3941) | 根据用户输入的信息，如时间区间、消耗类型、项目 ID、域名等，查询对应的统计信息 |
| 查询CDN消耗明细    | [DescribeCdnHostDetailedInfo](https://cloud.tencent.com/doc/api/231/3942) | 根据用户输入的信息，如时间区间、消耗类型、项目 ID、域名等，查询对应的统计明细，目前时间区间为 1 - 3 日的时间粒度为 5 分钟，4 - 7日的明细粒度为 1 小时，8 - 90日的明细粒度为 1 天 |
| 查询状态码统计      | [GetCdnStatusCode](https://cloud.tencent.com/doc/api/231/3943) | 根据用户输入的信息，如时间区间、项目 ID、域名、时间粒度等，查询返回码 200、206、304、404、416、500 统计明细 |
| 查询消耗统计TOP100 | [GetCdnStatTop](https://cloud.tencent.com/doc/api/231/3944) | 根据用户输入的信息，如时间区间、项目 ID、域名、消耗类型、时间粒度等，查询省份、运营商、URL的TOP100排名情况 |

**注意事项**：
+ 消耗及统计量查询目前仅支持 **90天内** 数据查询。

##### 刷新预热接口

| 接口名    | Action Name                              | 功能描述                                     |
| ------ | ---------------------------------------- | ---------------------------------------- |
| 查询刷新记录 | [GetCdnRefreshLog](https://cloud.tencent.com/doc/api/231/3948) | 根据用户输入的信息，如时间区间、URL，查询对应的刷新记录            |
| URL刷新  | [RefreshCdnUrl](https://cloud.tencent.com/doc/api/231/3946) | 根据用户提交的资源URL（可多个），将对应资源从节点中删除，此时再有用户访问，会直接回源站获取最新内容 |
| 目录刷新   | [RefreshCdnDir](https://cloud.tencent.com/doc/api/231/3947) | 根据用户提交的资源目录（可多个），将其中的资源从节点删除，此时再有用户访问，会直接回源站获取最新内容 |

##### 日志查询接口

| 接口名      | Action Name                              | 功能描述                                   |
| -------- | ---------------------------------------- | -------------------------------------- |
| 查询日志下载链接 | [GenerateLogList](https://cloud.tencent.com/doc/api/231/3950) | 根据用户输入的域名 ID（仅支持一个），查询该域名一个月内每天的日志下载链接 |



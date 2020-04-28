内容分发网络（CDN）接入了腾讯云云资源访问管理（Cloud Access Management）系统，您可以在 [访问管理控制台](https://console.cloud.tencent.com/cam/overview) 进行用户组、用户、角色、策略等一系列相关管理操作。

由于 CDN 目前处于权限系统升级过渡阶段，您可以通过以下几种方式为您的子用户和角色分配 CDN 管理权限。

## 资源授权

为方便用户更加细粒度的配置域名查询、管理权限，CDN 系统目前在进行权限策略的升级，将逐步支持策略语法能力，用户可通过自定义策略语句，实现域名级别的权限分配。

已经全面支持策略语法，对应的 Action 如下：

| Action 名称             | 加速区域         | 功能描述               | 控制台对应功能模块                                           |
| ----------------------- | ---------------- | ---------------------- | ------------------------------------------------------------ |
| DescribeCdnData         | 境内、境外均支持 | 查询访问监控数据明细   | 实时监控-访问监控部分数据曲线、汇总数据展示<br/>概览-数据曲线、汇总数据展示 |
| DescribeOriginData      | 境内、境外均支持 | 查询回源监控数据明细   | 实时监控-回源监控部分数据曲线、汇总数据展示                  |
| ListTopData             | 境内、境外均支持 | 多维度数据排序         | 实时监控-域名排序、TOP URL 排序、状态码占比图模块<br/>数据分析-省份 / 运营商 / 区域排名模块<br/>概览页-域名排序 |
| DescribeIpVisit         | 境内、境外均支持 | 独立 IP 访问明细查询   | 数据分析-独立 IP 访问数据曲线、汇总数据                        |
| PurgeUrlsCache          | 境内、境外均支持 | 提交 URL 刷新          | 缓存刷新-URL 刷新提交模块                                    |
| PurgePathCache          | 境内、境外均支持 | 提交目录刷新           | 缓存刷新-目录刷新提交模块                                    |
| DescribePurgeTasks      | 境内、境外均支持 | 刷新记录查询           | 缓存刷新-刷新记录查询模块                                    |
| PushUrlsCache           | 境内、境外均支持 | 提交 URL 预热          | 缓存刷新-URL 预热提交模块（灰度中）                           |
| DescribePushTasks       | 境内、境外均支持 | 预热记录查询           | 缓存刷新-预热记录查询模块（灰度中）                          |
| DescribeCdnIp           | 境内、境外均支持 | IP 归属查询            | IP 归属查询                                                  |
| DescribePayType         | 境内、境外均支持 | 查询境内、境外计费方式 | 概览-计费方式模块                                            |
| DescribeTrafficPackages | 境内             | 查询境内流量包列表     | 概览-流量包数量 / 即将过期数量展示模块<br/>流量包管理          |
| DescribeCdnDomainLogs   | 境内、境外均支持 | 获取日志下载链接       | 日志服务                                                     |

前往  [访问管理控制台](https://console.cloud.tencent.com/cam/overview) ，可按需指引创建资源（域名）维度策略，策略语法示例如下：

```json
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "*"
            ],
            "resource": [
                "qcs::cdn::uin/主账号UIN:domain/www.test.com"
            ],
            "effect": "allow"
        }
    ]
}
```
>!
- 策略语法仅支持上述已列出来的 API 3.0 接口进行授权，因此若 Action 配置为 * ，仅代表上述已列出的所有接口。
- 允许同时按照项目授权、策略语法进行域名级别授权。若授权了项目 A 的数据访问权限，在策略语法中又拒绝了项目 A 中 a 域名的数据查询权限，则没有项目 A 的权限，但是有项目 A 下其他域名权限。

## 功能集策略

若您需要针对项目级别的授权操作进行细化，如数据查询、刷新预热、域名管理操作分别授权给不同的子账号，可通过以下步骤创建策略：

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview) ，单击左侧目录的【策略】。
2. 单击【新建自定义策略】，而后选择【按产品功能或项目权限创建】：
![](https://main.qcloudimg.com/raw/59c8c89263412208344bd071430db23d.png)
3. 按要求填充策略名称，在下方服务类型中勾选【内容分发网络】：
![](https://main.qcloudimg.com/raw/e057955abd823f0b92ff6cc13a016c4c.png)
4. 按需开启需要授权的操作集并关联项目（默认项目不可进行授权），而后关联子用户即可：
![](https://main.qcloudimg.com/raw/961dfce5817ba690b554f12dfa22d7c9.png)

目前操作集归类及对应的 OPEN API 2.0 及 OPEN API 3.0 接口如下所示，拥有操作集权限的子用户，可针对有权限项目内任意一个域名调用列表中的 2.0 接口及 3.0 接口：

| 权限集合              | API2.0                                                       | API3.0                                                       | 是否需要授权 |
| :-------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------- |
| 查询消耗数据及统计量  | DescribeCdnHostInfo<br/> DescribeCdnHostDetailedInfo<br/>GetCdnStatusCode <br/>GetCdnStatTop<br/> GetCdnProvIspDetailStat | DescribeCdnData <br/>DescribeOriginData<br/> ListTopData<br/>DescribeIpVisit | 是           |
| 查询域名信息          | GetHostInfoById<br/>GetHostInfoByHost                        | 暂未上线                                                     | 是           |
| 查询 CDN 日志下载链接 | GenerateLogList<br/>GetCdnLogList                            | DescribeCdnDomainLogs                                        | 是           |
| 添加域名              | AddCdnHost<br/>                                              | 暂未上线                                                     | 是           |
| 上线 / 下线域名         | OnlineHost<br/>OfflineHost                                   | 暂未上线                                                     | 是           |
| 删除域名              | DeleteCdnHost                                                | 暂未上线                                                     | 是           |
| 修改域名配置          | UpdateCdnConfig                                              | 暂未上线                                                     | 是           |
| 刷新预热              | RefreshCdnDir<br/>RefreshCdnUrl<br/>GetCdnRefreshLog<br/>CdnPusherV2<br/>GetPushLogs<br/>CdnOverseaPushser | PurgeUrlsCache<br/>PurgePathCache<br/>DescribePurgeTasks<br/>PushUrlsCache<br/>DescribePushTasks | 是           |
| 服务查询              | QueryCdnIp（无需授权）                                       | DescribeCdnIp                                                | 是           |

**控制台页面权限说明：**
- 查看消耗数据及统计量：若策略开启了【查看消耗数据及统计量】并关联项目，则可查看控制台以下模块信息：
  - 概览页：仅数据展示模块
  - 统计分析：实时监控
  - 统计分析：数据分析
  - 全网数据监控
- 查询域名信息：若策略开启了【查询域名信息】并关联项目，则在控制台【域名管理】页面查看有权限的项目中域名列表及详细配置信息。
- 查询 CDN 日志下载链接：若策略开启了【查询 CDN 日志下载链接】并关联项目，则在控制台【日志服务】页面，可查询访问日志下载链接。
- 添加域名：若策略开启了【添加域名】并关联项目，则可向指定项目中添加域名。
- 上线 / 下线域名：若策略开启了【上线 / 下线域名】并关联项目，则可上线/下线指定项目中的加速域名。
- 删除域名：若策略开启了【删除域名】并关联项目，则可删除指定项目中的加速域名，删除域名需要为下线状态。因此若需要删除一个上线状态的域名，需要具备【上线 / 下线域名】权限。
- 修改域名配置：若策略开启了【修改域名配置】并关联项目，则可以修改指定项目中的加速域名配置。
- 刷新预热：若策略开启了【刷新预热】并关联项目，则可以在【刷新缓存】页面提交对应的刷新、预热（白名单）任务，并查询刷新预热任务的执行状态。

## 项目策略

若需要按照已经分配好的项目授权给某个子用户，使其具备项目下域名的完全读写权限，则可通过创建项目策略实现。

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview) ，单击左侧目录的【策略】。
2. 单击【新建自定义策略】，而后选择【按产品功能或项目权限创建】：
![](https://main.qcloudimg.com/raw/59c8c89263412208344bd071430db23d.png)
3. 按要求填充策略名称，在下方服务类型中勾选【项目管理】：
![](https://main.qcloudimg.com/raw/f0c7a068257c3f4ab8e734791d6ceeb2.png)
4. 开启【管理CDN业务项目内云资源】，而后关联需要授权的项目，即可完成创建一条项目管理员策略：
![](https://main.qcloudimg.com/raw/f9e5762bcae1dfe0cc77044cc3441122.png)

## 预设策略
目前 CDN 可适配的预设策略如下：
- AdministratorAccess：关联了此策略的子用户，可以管理账户内含 CDN 服务在内的所有云服务资产、财务相关信息、用户及权限。
- QCloudResourceFullAccess：关联了此策略的子用户，可以管理账户内含 CDN 服务在内的所有云服务资产。

若子用户关联了以上两类策略，则具备 CDN 所有域名的读写权限。

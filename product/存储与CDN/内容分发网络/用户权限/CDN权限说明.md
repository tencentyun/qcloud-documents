CDN 已经接入了腾讯云云资源访问管理（Cloud Access Management）系统，您可以在 [访问管理控制台](https://console.cloud.tencent.com/cam/overview) 进行用户组、用户、角色、策略等一系列相关管理操作。

由于 CDN 目前处于权限系统升级过渡阶段，您可以通过以下几种方式为您的子用户和角色分配 CDN 管理权限。

## 默认策略
目前 CDN 可适配的默认策略如下：
- AdministratorAccess：关联了此策略的子用户，可以管理账户内含 CDN 服务在内的所有云服务资产、财务相关信息、用户及权限。
- QCloudResourceFullAccess：关联了此策略的子用户，可以管理账户内含 CDN 服务在内的所有云服务资产。

## 项目权限

### 项目管理授权
CDN 支持按项目分配权限，即设置项目管理员。通过创建【项目管理】策略，分配项目，子用户可拥有该项目中所有 CDN 资源的管理权限，创建步骤如下：
1. 单击【按产品功能或项目权限创建】。
2. 为策略命名，并在服务类型中单击【项目管理】。
3. 开启【管理 CDN 业务项目内云资源】。
4. 关联指定项目。

上述策略创建完成并关联子用户后，被关联的子用户可以操作此项目内所有云资源（包括 CDN）。

### 功能 - 项目授权
CDN 支持按照预设的功能集，进行项目级别的授权操作。通过创建【内容分发网络】服务策略，子用户可以拥有该项目指定功能的权限，创建步骤如下：
1. 单击【按产品功能或项目权限授权】。
2. 为策略命名，并在服务类型中单击【内容分发网络】。
3. 开启所需功能集合，如【查看消耗数据及统计量】。
4. 关联指定项目。

上述策略创建完成并关联子用户后，被关联的子用户可以通过以下接口，查询项目内的资源（域名）对应的统计数据。

### API 注意事项
CDN 目前对外提供的接口大部分为 API2.0 接口，进行项目级别的资源授权的子用户，仅可调用以下 API 接口进行相关操作。未在列表中的 API 接口暂不支持子用户调用。

<table><tbody>
    <tr>
        <th>权限集合</th>
        <th>API2.0</th>
        <th>API3.0</th>
        <th>是否需要授权</th>
    </tr>
    <tr>
        <td href="https://cloud.tencent.com/document/product/228/13022">查询消耗数据及统计量</td>
        <td>DescribeCdnHostInfo<br/>DescribeCdnHostDetailedInfo<br/>GetCdnStatusCode<br/>GetCdnStatTop<br/>GetCdnProvIspDetailStat</td>
        <td>DescribeCdnData<br/>DescribeOriginData<br/>ListTopData<Br/>DescribeIpVisit</td>
        <td>是</td>
    </tr>
    <tr>
        <td>查询域名信息</td>
        <td>GetHostInfoById<br/>GetHostInfoByHost</td>
        <td>暂未上线</td>
        <td>是</td>
    </tr>
    <tr>
        <td>查询 CDN 日志下载链接</td>
        <td>GenerateLogList<br/>GetCdnLogList</td>
        <td>暂未上线</td>
        <td>是</td>       
    </tr>
    <tr>
        <td>添加域名</td>
        <td>AddCdnHost</td>
        <td>暂未上线</td>
        <td>是</td>       
    </tr>
    <tr>
        <td>上线/下线域名</td>
        <td>OnlineHost<br/>OfflineHost</td>
        <td>暂未上线</td>
        <td>是</td>       
    </tr>
    <tr>
        <td>删除域名</td>
        <td>DeleteCdnHost</td>
        <td>暂未上线</td>
        <td>是</td>       
    </tr> 
    <tr>
        <td>修改域名配置</td>
        <td>UpdateCdnConfig</td>
        <td>暂未上线</td>
        <td>是</td>       
    </tr>      
    <tr>
        <td>刷新预热</td>
        <td>RefreshCdnDir<br/>RefreshCdnUrl<br/>GetCdnRefreshLog<br/>CdnPusherV2<br/>GetPushLogs<br/>CdnOverseaPushser</td>
        <td>暂未上线</td>
        <td>是</td>
    </tr>     
    <tr>
        <td>服务查询</td>
        <td>QueryCdnIp</td>
        <td>暂未上线</td>
        <td>否</td>
    </tr>
   
</table>


### 控制台注意事项

- 查看消耗数据及统计量：若策略开启了【查看消耗数据及统计量】并关联项目，则可查看控制台以下模块信息：
 - 概览页
 - 统计分析：实时监控
 - 统计分析：数据分析
 - 全网数据监控
- 查询域名信息：若策略开启了【查询域名信息】并关联项目，则在控制台【域名管理】页面查看有权限的项目中域名列表及详细配置信息。
- 查询 CDN 日志下载链接：若策略开启了【查询 CDN 日志下载链接】并关联项目，则在控制台【日志管理】页面，可查询访问日志下载链接。
- 添加域名：若策略开启了【添加域名】并关联项目，则可向指定项目中添加域名。
- 上线/下线域名：若策略开启了【上线/下线域名】并关联项目，则可上线/下线指定项目中的加速域名。
- 删除域名：若策略开启了【删除域名】并关联项目，则可删除指定项目中的加速域名，删除域名需要为下线状态。因此若需要删除一个上线状态的域名，需要具备【上线/下线域名】权限。
- 修改域名配置：若策略开启了【修改域名配置】并关联项目，则可以修改指定项目中的加速域名配置。
 >!在控制台【证书管理】页面，可以修改对应 HTTPS 配置，API 2.0 接口暂不支持。
- 刷新预热：若策略开启了【刷新预热】并关联项目，则可以在【刷新缓存】页面提交对应的刷新、预热（白名单）任务，并查询刷新预热任务的执行状态。
 >!预热目前尚未全量开放，仅部分内测中用户可见。

<span id="ymqx"></span>
## 域名权限

为方便用户更加细粒度的配置域名查询、管理权限，CDN 系统目前在进行权限策略的升级，将逐步支持策略语法能力，用户可通过自定义策略语句，实现域名级别的权限分配。

目前新增的 API3.0 接口及新版的统计分析控制台，已经全面支持策略语法，对应的 Action 如下：

- DescribeCdnData：查询域名访问监控数据，带宽、流量、流量命中率、请求数、状态码、响应时间等实时指标，支持1分钟粒度；对应控制台【统计分析】中实时监控页面，访问监控页面数据。
- DescribeOriginData：查询域名回源监控数据，回源带宽、回源流量、回源请求数、回源失败率、回源状态码等实时指标，支持1分钟粒度；对应控制台【统计分析】中实时监控页面，回源监控页面数据。
- ListTopData：支持多条件组合排序结果查询，如指定时间区间、按域名流量从大到小排序，或指定时间区间、按 URL 流量从大到小排序能；对应控制台【统计分析】中相关列表部分。
- DescribeIpVisit：支持 IP 活跃查询，5分钟粒度活跃 IP 查询及天粒度日活跃数据查询；对应控制台【数据分析】页面中对应模块。

### 策略语法

使用策略语法授权域名权限时，语法如下：

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "*"
            ],
            "resource": [
                "qcs::cdn::uin/987654321:domain/www.test.com"
            ],
            "effect": "allow"
        }
    ]
}
```

**语法说明**

- action：表示需要授权的 Action，仅支持 DescribeCdnData、DescribeOriginData、ListTopData、DescribeIpVisit 这4个 Action 授权，详情请参见 [域名权限](#ymqx)。
- resource：表示需要授权的对象，对 CDN 服务而言，仅支持域名级别的授权，格式需要按示例所示。
- effect：授权允许，即允许对 resource 调用 action，可配置为 deny，即禁止对 resource 调用 action。
- statement 允许配置多条，当域名存在重复配置 deny 与 allow 时，deny 优先。

>!
- 策略语法仅支持上述 DescribeCdnData、DescribeOriginData、ListTopData、DescribeIpVisit 这4个 Action 授权，详情请参见 [域名权限](#ymqx)。因此若配置为 * ，则表示对这几个 Action 均做授权。
- 允许同时按照项目授权、策略语法进行域名级别授权。若授权了项目 A 的数据访问权限，在策略语法中又拒绝了项目 A 中 a 域名的数据查询权限，则没有项目 A 的权限，但是有项目 A 下其他域名权限。





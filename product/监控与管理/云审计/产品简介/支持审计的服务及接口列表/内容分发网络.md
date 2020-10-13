内容分发网络（Content Delivery Network，CDN）是在现有 Internet 中增加的一层新的网络架构，由遍布全球的高性能加速节点构成。这些高性能的服务节点都会按照一定的缓存策略存储您的业务内容，当您的用户向您的某一业务内容发起请求时，请求会被调度至最接近用户的服务节点，直接由服务节点快速响应，有效降低用户访问延迟，提升可用性。

下表为云审计支持的内容分发网络操作列表：

| 操作名称             | 资源类型 | 事件名称                |
|------------------|------|---------------------|
| 新增加速域名           | cdn  | AddCdnDomain        |
| 创建 SCDN 域名         | cdn  | CreateScdnDomain    |
| 创建 SCDN 日志事件任务     | cdn  | CreateScdnLogTask   |
| 删除加速域名           | cdn  | DeleteCdnDomain     |
| 访问数据查询           | cdn  | DescribeCdnData     |
| 校验 SSL 证书并提取其包含的域名 | cdn  | DescribeCertDomains |
| 活跃用户查询           | cdn  | DescribeIpVisit     |
| 回源数据查询           | cdn  | DescribeOriginData  |
| 查询 SCDN 域名配置       | cdn  | DescribeScdnConfig  |
| 查询 SCDN 数据         | cdn  | DescribeScdnData    |
| 禁用 URL           | cdn  | DisableCaches       |
| 查询 SCDN 域名列表       | cdn  | ListScdnDomains     |
| 查询 SCDN 日志下载任务列表   | cdn  | ListScdnLogTasks    |
| Top 数据查询          | cdn  | ListTopData         |
| 获取 SCDN Top 数据      | cdn  | ListTopScdnData     |
| 开通 CDN 业务          | cdn  | OpenCdnService      |
| 刷新目录             | cdn  | PurgePathCache      |
| 刷新 URL           | cdn  | PurgeUrlsCache      |
| 预热 URL           | cdn  | PushUrlsCache       |
| 启用加速服务           | cdn  | StartCdnDomain      |
| 开启域名安全防护         | cdn  | StartScdnDomain     |
| 关闭加速服务           | cdn  | StopCdnDomain       |
| 关闭域名安全防护         | cdn  | StopScdnDomain      |
| 修改域名配置           | cdn  | UpdateDomainConfig  |
| 批量更新域名证书         | cdn  | UpdateDomainsHttps  |
| 修改加速域名图片处理配置     | cdn  | UpdateImageConfig   |
| 修改计费类型           | cdn  | UpdatePayType       |
| 修改 SCDN 域名配置       | cdn  | UpdateScdnDomain    |

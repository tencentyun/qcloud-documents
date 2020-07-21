API 网关（apigw）是 API 托管服务，提供 API 的完整生命周期管理，包括创建、维护、发布、运行、下线等。您可使用 API 网关封装自身业务，将您的数据、业务逻辑或功能安全可靠的开放出来，用以实现自身系统集成、以及与合作伙伴的业务连接。

下表为云审计覆盖的 API 网关相关接口：

| 接口功能                   | 接口名称                     |
|---------------|--------------------------------------------|
| 绑定环境          | BindEnvironment                            |
| 绑定秘钥          | BindSecretIds                              |
| 绑定子域名         | BindSubDomain                              |
| 创建 API         | CreateApi                                  |
| 创建秘钥          | CreateApiKey                               |
| 创建服务          | CreateService                              |
| 创建使用计划        | CreateUsagePlan                            |
| 删除 API         | DeleteApi                                  |
| 删除秘钥          | DeleteApiKey                               |
| 删除 IP 策略        | DeleteIPStrategy                           |
| 删除服务          | DeleteService                              |
| 删除使用计划        | DeleteUsagePlan                            |
| 使用计划降级        | DemoteServiceUsagePlan                     |
| 获取 API 详情       | DescribeApi                                |
| 获取 API 环境策略     | DescribeApiEnvironmentStrategy             |
| 获取 API 秘钥详情     | DescribeApiKey                             |
| 获取秘钥列表        | DescribeApiKeysStatus                      |
| 查询 API 列表       | DescribeApisStatus                         |
| 获取 API 使用计划     | DescribeApiUsagePlan                       |
| 获取服务详情        | DescribeService                            |
| 获取服务环境 key 监控上传 | DescribeServiceEnvironmentKeyMonitorUpload |
| 获取服务环境列表      | DescribeServiceEnvironmentList             |
| 创建服务发布版本      | DescribeServiceReleaseVersion              |
| 查询服务列表        | DescribeServicesStatus                     |
| 获取服务子域名列表     | DescribeServiceSubDomains                  |
| 获取使用计划 API 秘钥   | DescribeUsagePlanSecretIds                 |
| 查询使用计划列表      | DescribeUsagePlansStatus                   |
| 禁用秘钥          | DisableApiKey                              |
| 启用秘钥          | EnableApiKey                               |
| 生成 API 文档       | GenerateApiDocument                        |
| 修改 API         | ModifyApi                                  |
| 修改 IP 策略        | ModifyIPStrategy                           |
| 修改服务          | ModifyService                              |
| 修改服务环境监控上传    | ModifyServiceEnvironmentKeyMonitorUpload   |
| 修改服务环境策略      | ModifyServiceEnvironmentStrategy           |
| 修改子域名         | ModifySubDomain                            |
| 修改使用计划        | ModifyUsagePlan                            |
| 发布服务          | ReleaseService                             |
| 调试 API         | RunApi                                     |
| 解绑环境          | UnBindEnvironment                          |
| 解绑秘钥          | UnBindSecretIds                            |
| 解绑子域名         | UnBindSubDomain                            |
| 环境下线          | UnReleaseService                           |
| 更新 API 秘钥       | UpdateApiKey                               |
| 修改服务          | UpdateService                              |

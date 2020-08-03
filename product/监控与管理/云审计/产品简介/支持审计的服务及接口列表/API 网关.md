API 网关（API Gateway）是 API 托管服务，提供 API 的完整生命周期管理，包括创建、维护、发布、运行、下线等。您可使用 API 网关封装自身业务，将您的数据、业务逻辑或功能安全可靠的开放出来，用以实现自身系统集成、以及与合作伙伴的业务连接。

下表为云审计支持的 API 网关操作列表：



| 操作名称                  | 资源类型 | 事件名称                                   |
| ------------------------- | -------- | ------------------------------------------ |
| 绑定环境                  | apigw    | BindEnvironment                            |
| 绑定密钥                  | apigw    | BindSecretIds                              |
| 绑定子域名                | apigw    | BindSubDomain                              |
| 创建 API                  | apigw    | CreateApi                                  |
| 创建密钥                  | apigw    | CreateApiKey                               |
| 创建服务                  | apigw    | CreateService                              |
| 创建使用计划              | apigw    | CreateUsagePlan                            |
| 删除 API                  | apigw    | DeleteApi                                  |
| 删除密钥                  | apigw    | DeleteApiKey                               |
| 删除 IP 策略              | apigw    | DeleteIPStrategy                           |
| 删除服务                  | apigw    | DeleteService                              |
| 删除使用计划              | apigw    | DeleteUsagePlan                            |
| 使用计划降级              | apigw    | DemoteServiceUsagePlan                     |
| 获取 API 详情             | apigw    | DescribeApi                                |
| 获取 API 环境策略         | apigw    | DescribeApiEnvironmentStrategy             |
| 获取 API 密钥详情         | apigw    | DescribeApiKey                             |
| 获取密钥列表              | apigw    | DescribeApiKeysStatus                      |
| 查询 API 列表             | apigw    | DescribeApisStatus                         |
| 获取 API 使用计划         | apigw    | DescribeApiUsagePlan                       |
| 获取服务详情              | apigw    | DescribeService                            |
| 获取服务环境 key 监控上传 | apigw    | DescribeServiceEnvironmentKeyMonitorUpload |
| 获取服务环境列表          | apigw    | DescribeServiceEnvironmentList             |
| 创建服务发布版本          | apigw    | DescribeServiceReleaseVersion              |
| 查询服务列表              | apigw    | DescribeServicesStatus                     |
| 获取服务子域名列表        | apigw    | DescribeServiceSubDomains                  |
| 获取使用计划 API 密钥     | apigw    | DescribeUsagePlanSecretIds                 |
| 查询使用计划列表          | apigw    | DescribeUsagePlansStatus                   |
| 禁用密钥                  | apigw    | DisableApiKey                              |
| 启用密钥                  | apigw    | EnableApiKey                               |
| 生成 API 文档             | apigw    | GenerateApiDocument                        |
| 修改 API                  | apigw    | ModifyApi                                  |
| 修改 IP 策略              | apigw    | ModifyIPStrategy                           |
| 修改服务                  | apigw    | ModifyService                              |
| 修改服务环境监控上传      | apigw    | ModifyServiceEnvironmentKeyMonitorUpload   |
| 修改服务环境策略          | apigw    | ModifyServiceEnvironmentStrategy           |
| 修改子域名                | apigw    | ModifySubDomain                            |
| 修改使用计划              | apigw    | ModifyUsagePlan                            |
| 发布服务                  | apigw    | ReleaseService                             |
| 调试 API                  | apigw    | RunApi                                     |
| 解绑环境                  | apigw    | UnBindEnvironment                          |
| 解绑密钥                  | apigw    | UnBindSecretIds                            |
| 解绑子域名                | apigw    | UnBindSubDomain                            |
| 环境下线                  | apigw    | UnReleaseService                           |
| 更新 API 密钥             | apigw    | UpdateApiKey                               |
| 修改服务                  | apigw    | UpdateService                              |
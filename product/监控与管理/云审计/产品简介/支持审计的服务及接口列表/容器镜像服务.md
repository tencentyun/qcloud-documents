腾讯云容器镜像服务（Tencent Container Registry，TCR）是腾讯云提供的容器镜像云端托管服务，支持 Docker 镜像、Helm Chart 存储分发及镜像安全扫描，为企业级客户提供了细颗粒度的访问权限管理和网络访问控制。支持镜像全球同步及触发器，可满足企业级客户拓展全球业务及使用容器 CI/CD 工作流的需求。支持具有上千节点的大规模容器集群并发拉取 GB 级大镜像，可保障业务的极速部署。 通过使用容器镜像服务，您不再需要自建并维护镜像托管服务，即可在云上享有安全高效的镜像托管、分发服务，并可与腾讯云容器服务 TKE 结合使用，获得容器上云的顺畅体验。

下表为云审计支持的容器镜像服务操作列表：

| 操作名称              | 资源类型 | 事件名称                               |
|-------------------|------|------------------------------------|
| 批量删除镜像版本          | tcr  | BatchDeleteImagePersonal           |
| 批量删除镜像仓库          | tcr  | BatchDeleteRepositoryPersonal      |
| 创建企业版实例           | tcr  | CreateInstance                     |
| 获取临时登录密码          | tcr  | CreateInstanceToken                |
| 创建命名空间            | tcr  | CreateNamespacePersonal            |
| 创建镜像仓库\-个人版实例     | tcr  | CreateRepositoryPersonal           |
| 创建公网访问策略          | tcr  | CreateSecurityPolicy               |
| 删除个人版全局镜像版本自动清理策略 | tcr  | DeleteImageLifecycleGlobalPersonal |
| 删除镜像版本            | tcr  | DeleteImagePersonal                |
| 删除实例              | tcr  | DeleteInstance                     |
| 删除长期访问凭证          | tcr  | DeleteInstanceToken                |
| 删除命名空间            | tcr  | DeleteNamespacePersonal            |
| 删除镜像仓库            | tcr  | DeleteRepositoryPersonal           |
| 删除实例公网访问白名单策略     | tcr  | DeleteSecurityPolicy               |
| 查询长期访问凭证信息        | tcr  | DescribeInstanceToken              |
| 管理实例公网访问          | tcr  | ManageExternalEndpoint             |
| 设置个人版全局镜像版本自动清理策略 | tcr  | ManageImageLifecycleGlobalPersonal |
| 管理实例内网访问 VPC       | tcr  | ManageInternalEndpoint             |
| 管理实例同步            | tcr  | ManageReplication                  |
| 更新实例长期访问凭证        | tcr  | ModifyInstanceToken                |

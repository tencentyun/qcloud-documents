腾讯云 Elasticsearch Service（ES）是腾讯云基于开源搜索引擎 Elasticsearch 打造的高可用、可伸缩的云端托管 Elasticsearch 服务。腾讯云 ES 服务 100% 兼容 ELK 架构，广泛应用于互联网、游戏、互联网金融等领域客户网站搜索导航、企业级搜索、服务日志异常监控、点击流分析等业务。

下表为云审计支持的 Elasticsearch Service 操作列表：

| 操作名称     | 资源类型 | 事件名称                       |
|----------|------|----------------------------|
| 创建 ES 集群实例 | es   | CreateInstance             |
| 销毁 ES 集群实例 | es   | DeleteInstance             |
| 查询 ES 集群日志 | es   | DescribeInstanceLogs       |
| 查询实例操作记录 | es   | DescribeInstanceOperations |
| 查询 ES 集群实例 | es   | DescribeInstances          |
| 重启 ES 集群实例 | es   | RestartInstance            |
| 更新 ES 集群实例 | es   | UpdateInstance             |
| 升级 ES 集群版本 | es   | UpgradeInstance            |
| 升级 ES 商业特性 | es   | UpgradeLicense             |

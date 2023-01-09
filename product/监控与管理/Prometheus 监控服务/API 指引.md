### Prometheus 实例相关操作接口：

| 接口功能                                                     | 接口名称                               |
| ------------------------------------------------------------ | -------------------------------------- |
| [DescribePrometheusInstances](https://cloud.tencent.com/document/product/248/66097) | 查看 Prometheus 实例列表               |
| [ModifyPrometheusInstanceAttributes](https://cloud.tencent.com/document/api/248/76009) | 修改 Prometheus 实例相关属性           |
| [BindPrometheusManagedGrafana](https://cloud.tencent.com/document/api/248/76020) | 绑定 Grafana 可视化服务实例            |
| [UnbindPrometheusManagedGrafana](https://cloud.tencent.com/document/api/248/76007) | 解除实例绑定的 Grafana 可视化实例      |
| [TerminatePrometheusInstances](https://cloud.tencent.com/document/api/248/76008) | 销毁按量 Prometheus 实例               |
| [DestroyPrometheusInstance](https://cloud.tencent.com/document/api/248/76011) | 强制释放 Prometheus 实例               |
| [CreatePrometheusAgent](https://cloud.tencent.com/document/api/248/76018) | 创建 Prometheus CVM Agent              |
| [UpdatePrometheusAgentStatus](https://cloud.tencent.com/document/api/248/76004) | 更新 Prometheus CVM Agent 状态         |
| [GetPrometheusAgentManagementCommand](https://cloud.tencent.com/document/api/248/76010) | 获取 Prometheus Agent 管理相关的命令行 |
| [DescribePrometheusAgents](https://cloud.tencent.com/document/api/248/76013) | 列出 Prometheus CVM Agent              |
| [CreatePrometheusScrapeJob](https://cloud.tencent.com/document/api/248/76017) | 创建 Prometheus 抓取任务               |
| [UpdatePrometheusScrapeJob](https://cloud.tencent.com/document/api/248/76003) | 更新 Prometheus 抓取任务               |
| [DeletePrometheusScrapeJobs](https://cloud.tencent.com/document/api/248/76015) | 删除 Prometheus 抓取任务               |
| [DescribePrometheusScrapeJobs](https://cloud.tencent.com/document/api/248/76012) | 列出 Prometheus 抓取任务               |
| [UpgradeGrafanaDashboard](https://cloud.tencent.com/document/api/248/76002) | 升级 Grafana Dashboard                 |
| [UninstallGrafanaDashboard](https://cloud.tencent.com/document/api/248/76006) | 删除 Grafana Dashboard                 |
| [CreateExporterIntegration](https://cloud.tencent.com/document/api/248/76019) | 创建 exporter 集成                     |
| [DescribeExporterIntegrations](https://cloud.tencent.com/document/api/248/76014) | 查询 exporter 集成列表                 |
| [DeleteExporterIntegration](https://cloud.tencent.com/document/api/248/76016) | 删除 exporter 集成                     |
| [UpdateExporterIntegration](https://cloud.tencent.com/document/api/248/76005) | 更新 exporter 集成配置                 |
| [CreateAlertRule](https://cloud.tencent.com/document/api/248/55635) | 创建告警规则                           |
| [DeleteAlertRules](https://cloud.tencent.com/document/api/248/55634) | 删除报警规则                           |
| [DescribeAlertRules](https://cloud.tencent.com/document/api/248/55633) | 报警规则查询                           |
| [UpdateAlertRule](https://cloud.tencent.com/document/api/248/55632) | 更新报警规则                           |
| [UpdateAlertRuleState](https://cloud.tencent.com/document/api/248/55631) | 更新报警策略状态                       |
| [CreateRecordingRule](https://cloud.tencent.com/document/api/248/76041) | 创建预聚合规则                         |
| [UpdateRecordingRule](https://cloud.tencent.com/document/api/248/76038) | 更新预聚合规则                         |
| [DeleteRecordingRules](https://cloud.tencent.com/document/api/248/76040) | 删除预聚合规则                         |
| [DescribeRecordingRules](https://cloud.tencent.com/document/api/248/76039) | 查询预聚合规则                         |

### 容器集成相关操作接口：

| 接口功能                                                     | 接口名称                             |
| ------------------------------------------------------------ | ------------------------------------ |
| [获取关联集群列表](https://cloud.tencent.com/document/product/457/73912) | DescribePrometheusClusterAgents      |
| [创建告警策略](https://cloud.tencent.com/document/product/457/73918) | CreatePrometheusAlertPolicy          |
| [删除告警策略](https://cloud.tencent.com/document/product/457/73916) | DeletePrometheusAlertPolicy          |
| [修改告警策略](https://cloud.tencent.com/document/product/457/73907) | ModifyPrometheusAlertPolicy          |
| [查询告警策略](https://cloud.tencent.com/document/product/457/73913) | DescribePrometheusAlertPolicy        |
| [创建全局告警通知渠道](https://cloud.tencent.com/document/product/457/74076) | CreatePrometheusGlobalNotification   |
| [查询全局告警通知渠道](https://cloud.tencent.com/document/product/457/74075) | DescribePrometheusGlobalNotification |
| [修改全局告警通知渠道](https://cloud.tencent.com/document/product/457/74074) | ModifyPrometheusGlobalNotification   |
| [创建模板](https://cloud.tencent.com/document/product/457/73917) | CreatePrometheusTemp                 |
| [修改模板](https://cloud.tencent.com/document/product/457/74013) | ModifyPrometheusTemp                 |
| [删除模板](https://cloud.tencent.com/document/product/457/73915) | DeletePrometheusTemp                 |
| [查询模板](https://cloud.tencent.com/document/product/457/73909) | DescribePrometheusTemp               |
| [同步模板](https://cloud.tencent.com/document/product/457/73906) | SyncPrometheusTemp                   |
| [解除同步模板](https://cloud.tencent.com/document/product/457/73914) | DeletePrometheusTempSync             |
| [查询模板关联实例](https://cloud.tencent.com/document/product/457/73908) | DescribePrometheusTempSync           |


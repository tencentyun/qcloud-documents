腾讯云 Elasticsearch Service 支持分钟级一键安装 Cerebro，并在控制台轻松访问，完全兼容开源，适配0.9.4版本。

## 背景信息

Cerebro 是开源的 Elasticsearch 可视化管理工具，支持您通过 Cerebro 对腾讯云 Elasticsearch 集群进行web可视化管理，如监控实时的索引分片负载、执行 res t请求、修改 Elasticsearch 配置等。

## 操作步骤

1. 登录[腾讯云 Elasticsearch 控制台](https://console.cloud.tencent.com/es)，单击**集群名称**访问目标集群，跳转至**可视化组件**界面。
![](https://qcloudimg.tencent-cloud.cn/raw/f7acb778b34928e3284783fd5d4abf31.png)
2. 在 **Cerebro** 功能模块，一键安装 Cerebro（默认未安装），Cerebro 默认安装在 Kibana 节点上，和 Kibana 公用节点资源，启用前建议前往集群变配界面升级 Kibana 节点规格至2核4G 及以上。
3. 访问 Cerebro 控制台，在登录界面输入用户名和密码登录。用户名默认为 elastic，密码为集群创建时设置的密码。
4. Cerebro 支持内网和公网访问，您可以在**公网访问策略**模块制定 Cerebro 公网访问策略，此公网访问策略将和 Kibana 共用。
5. 登入 Cerebro 后，支持在控制台进行数据查询、仪表板制作等操作。
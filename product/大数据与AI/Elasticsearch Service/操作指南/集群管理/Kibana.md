购买腾讯云 Elasticsearch 集群时，将免费提供1个1核2G 规格的 Kibana 节点，此节点将支持 Kibana、Cerebro 组件的使用，您可以根据业务需要，付费升级该 Kibana 节点至更高规格。

## 背景信息

Kibana 作为 Elastic Stack 的组成部分，天然契合 Elasticsearch 服务，帮助用户实时监测和管理集群状态。腾讯云 Elasticsearch Service 服务提供 Kibana 登陆入口，能够调整 Kibana 基础配置，支持动态调整 Kibana 节点资源，为用户业务提供扩展性。

## 操作步骤

1. 登录腾讯云[ Elasticsearch 控制台](https://console.cloud.tencent.com/es)，单击**集群名称**访问目标集群，在**可视化组件界面**、**集群列表**、**集群详情banner位置**，均支持单击 **Kibana** 访问 Kibana 控制台。
2. 单击前往**可视化组件**界面
![](https://qcloudimg.tencent-cloud.cn/raw/e1fdb9fa2837d186a5c4708deab95b78.png)
3. 访问 Kibana 控制台，在登陆界面输入用户名和密码登录。用户名默认为 elastic，密码为集群创建时设置的密码。
4. 支持通过公网和内网访问 Kibana，并在**公网访问策略**模块配置 [Kibana 公网和内网访问控制](https://tcloud-doc.isd.com/document/product/845/16992)。
5. 登入 Kibana 后，支持在控制台进行数据查询、仪表板制作等操作，详细指引请参见 [ Kibana Guide](https://www.elastic.co/guide/en/kibana/current/index.html?spm=a2c4g.11186623.0.0.2bc8216bPBCELk)。

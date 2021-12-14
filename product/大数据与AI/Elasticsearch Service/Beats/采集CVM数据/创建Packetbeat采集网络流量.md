Packetbeat 是轻量的网络流量包采集器，用于应用程序和性能监测，支持将数据传输至 logstash 实例或 Elaticsearch 集群中进行分析，并在 Kibana 中可视化查看。

## 应用场景
Packetbeat 通过采集应用层的网络流量数据（HTTP、MySQL、Redis 等），使得用户可以密切监测应用程序的延迟和错误、响应时间、SLA 性能、用户访问模式和趋势等。

## 操作须知
- 腾讯云 CVM 实例、腾讯云 ES 集群和 Logstash 实例，必须在同一 VPC 下。且腾讯云 ES 集群和 Logstash 实例的大版本相同。
>! Beats 目前仅支持64位的 Linux 操作系统。
- 腾讯云 CVM 实例必须安装自动化助手，仅支持为已安装自动化助手的 CVM 实例下发采集器配置。具体操作参见 [安装自动化助手客户端](https://cloud.tencent.com/document/product/1340/51945)。

## 操作步骤
### Packetbeat 采集器配置
1. 登录 [Elasticsearch Service 控制台](https://console.cloud.tencent.com/es/beats) Beats 管理界面，并授权服务相关角色，单击创建 **Packetbeat** 采集器。
![](https://qcloudimg.tencent-cloud.cn/raw/a6a97f6ed4813e9f98d11d16072c6914.png)
2. 在创建 Packetbeat 采集器中，设置采集器信息。
 - 配置 Packetbeat 采集器，输入或选择采集器配置信息。完成后单击**下一步**。
    - 采集器名称：自定义采集器的名称，格式为1个 - 50个英文、汉字、数字、连接线（-）或下划线（\_）。  
    - 安装版本：支持6.8.15或7.10.2版本。  
    - 采集器输出：采集的数据支持传送到腾讯云 Elasticsearch 与 Logstash 实例，请选择与需采集数据的 CVM 在同一 VPC 下的 ES 集群和 Logstash 实例。不支持输出至开源版 ES 集群。
    - 用户名密码：若选择输出采集数据到开启用户登录认证的 ES 集群，需要填写用户名和密码，使 Packetbeat 有权限向 ES 集群中写入数据。用户名默认为 elastic，密码为集群创建时设置。
    - Monitoring：勾选后在 Kibana 内生成监控 Packetbeat 的相关指标。当采集器输出为 ES 集群时，Monitoring 默认使用和采集器输出相同的 ES 集群；当采集器输出为 Logstash 实例时，则需要在配置文件中额外添加用于存储监控数据的 ES 集群地址。
    - Kibana Dashboard：勾选后生成默认的 Kibana Dashboard。  
    - 采集器 YML 配置：
Packetbeat 支持采集多种协议的网络流量，具体每个协议的参数可参考官方文档 [Configure Packetbeat](https://www.elastic.co/guide/en/beats/packetbeat/current/configuration-protocols.html)。
![](https://qcloudimg.tencent-cloud.cn/raw/9e0951469559a0d86fd66db0f5ab06e4.png)
 -  将采集器安装到 CVM 实例。选择要安装采集器的 CVM 实例，完成后单击**确定启用**。
     - CVM 必须安装自动化助手，仅支持为已安装自动化助手的 CVM 实例下发采集器配置。
     - 仅支持选择和采集器输出在同一 VPC 下的 CVM 实例进行安装，若无法找到目标 CVM 实例，需要更改采集器输出。
![](https://qcloudimg.tencent-cloud.cn/raw/bda8dba02e55ea3b01f94aa271be0a27.png)
3. 单击**确定启用**后，跳转到 Beats 采集器管理界面，可以查看 Packetbeat 采集器运行状态，显示“正常”则表示采集器安装成功。支持 [修改采集器配置](https://cloud.tencent.com/document/product/845/63301) 和 [管理 CVM 实例](https://cloud.tencent.com/document/product/845/63302)。

![](https://qcloudimg.tencent-cloud.cn/raw/5fa28e39ad540a9b7a289a09d2ee6923.png)

### Kibana 查看结果
1. 登录腾讯云 Kibana 控制台。
2. 在 Kibana 左侧导航栏单击 **Discover**，查询 Packetbeat 采集的数据：
![](https://main.qcloudimg.com/raw/db453667565e7afa7eb928830badf943.png)


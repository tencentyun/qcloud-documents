对于需要采集并分析腾讯云 CVM 服务日志的场景，可以使用 Filebeat 采集数据，再发送到腾讯云 Logstash 中进行过滤与预处理，最终传输到腾讯云 Elasticsearch 集群中进行存储，之后可以在 Kibana 中查询并分析日志。本文介绍如何配置 Filebeat 采集部署在腾讯云 CVM 中的服务日志。

## 应用场景
Filebeat 是一个轻量型的日志采集器，可以轻松地采集云上的 CVM 的日志，从而使得查询或者分析业务服务端的日志变得简单。
- Filebeat 能够逐行读取并发送日志，支持在出现中断的情况下，记录中断时读取到的文件位置信息，后续恢复正常后可以从中断前停止的位置继续开始。
- Filebeat 非常适合采集 nginx、apache 以及容器服务的日志，并且提供可以直接引用的配置模板，极大的简化了这类服务的日志采集过程。

## 操作须知
1. 腾讯云 CVM 实例、腾讯云 ES 集群和 Logstash 实例，必须在同一 VPC 下。且腾讯云 ES 集群和 Logstash 实例的大版本相同。
>!Beats 目前仅支持64位的 Linux 操作系统。
2. 腾讯云 CVM 实例必须安装自动化助手，仅支持为已安装自动化助手的 CVM 实例下发采集器配置。具体操作参见 [安装自动化助手客户端](https://cloud.tencent.com/document/product/1340/51945)。

## 操作步骤
### Filebeat 采集器配置
1. 登录 [Elasticsearch Service 控制台](https://console.cloud.tencent.com/es/beats) Beats 管理界面，授权服务相关角色，单击创建 **Filebeat** 采集器。
![](https://qcloudimg.tencent-cloud.cn/raw/fe79a749432ed3d0212e437d67c31b46.png)
2. 在创建 Filebeat 采集器中，设置采集器信息。
 - 配置 Filebeat 采集器，输入或选择采集器配置信息。完成后单击**下一步**。
    - 采集器名称：自定义采集器的名称，格式为1个 - 50个英文、汉字、数字、连接线（-）或下划线（\_）。 
    - 安装版本：支持6.8.15或7.10.2版本。  
    - 采集器输出：采集的数据支持传送到腾讯云 Elasticsearch 集群与 Logstash 实例，请选择与需采集数据的 CVM 在同一 VPC 下的 ES 集群和 Logstash 实例。不支持输出至开源版 ES 集群。
    - 用户名密码：若选择输出采集数据到开启用户登录认证的 ES 集群，需要填写用户名和密码，使得 Filebeat 有权限向 ES 集群中写入数据。用户名默认为 elastic，密码为集群创建时设置。
    - Monitoring：勾选后生成监控 Filebeat 的相关指标。当采集器输出为 ES 集群时，Monitoring 默认使用和采集器输出相同的 ES 集群；当采集器输出为 Logstash 实例时，则需要在配置文件中额外添加用于存储监控数据的 ES 集群地址。
    - Kibana Dashboard：勾选后生成默认的 Kibana Dashboard。  
    - 采集器 YML 配置：配置内容如下，更多 YML 配置请参考官方文档 [Configure input](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-filebeat-options.html)。
       - type：输入类型，默认为 log，还有 tcp、syslog、stdin 等可选。
       - paths：日志文件路径，需要填写为 CVM 中日志文件的绝对路径。
       - enabled：是否启用该 input 配置，true 为启用，false 则为不启用。
![](https://qcloudimg.tencent-cloud.cn/raw/cafef95daebed075ac1028d7a7f2473f.png)
 - 将采集器安装到 CVM 实例。选择要安装采集器的 CVM 实例，完成后单击**确定启用**。
     - CVM 必须安装自动化助手，仅支持为已安装自动化助手的 CVM 实例下发采集器配置。
     - 仅支持选择和采集器输出在同一 VPC 下的 CVM 实例进行安装，若无法找到目标 CVM 实例，需要更改采集器输出。
![](https://qcloudimg.tencent-cloud.cn/raw/8819bd2d0fa25152b9e066ef31ada9df.png)
3. 单击**确定启用**后，跳转到 Beats 采集器管理界面，可以查看 Heartbeat 采集器运行状态，显示“正常”则表示采集器安装成功。支持 [修改采集器配置](https://cloud.tencent.com/document/product/845/63301) 和 [管理 CVM 实例](https://cloud.tencent.com/document/product/845/63302)。

![](https://qcloudimg.tencent-cloud.cn/raw/5fa28e39ad540a9b7a289a09d2ee6923.png)

### Logstash 管道配置
如需将采集的日志数据传送到腾讯云 Logstash 实例，可参考 [接收 Filebeat 发送的数据并写入到 Elasticsearch](https://cloud.tencent.com/document/product/845/55154) 配置 logstash 管道。

### Kibana 查看结果
1. 登录腾讯云 Kibana 控制台。
2. 左侧导航栏单击 **Dev Tool**，执行下述语句，查看采集成功的数据。
```
GET filebeat-7.10.2/_search
```
![](https://main.qcloudimg.com/raw/fbc0cbf4f89fa6bb9b68cd711db18c26.png)

Heartbeat 是轻量的运行状态监测数据采集器，支持 ICMP 监视（包括 ICMPV4 和 ICMPV6）、TCP 监视和 HTTP 监视，能够主动探测服务的可用性。

## 应用场景
Hearbeat 通过主动探测来检测服务的可用性，可以通过给定 URL 列表对网站运行状况进行监控，支持通过 ICMP、TCP、HTTP 进行 ping 检测，同时也支持 TLS、身份验证和代理。Heartbeat 通过配置 monitors 进行检测指定主机或者网站的运行情况，目前支持三种 monitor：
- ICMP：支持 IPV4 和 IPV6，发送 ICMP 请求检测服务是否可用，该 monitor 需要 root 权限。
- TCP：发送 TCP 请求检测服务是否可用。
- HTTP：发送 HTTP 请求检测服务是否可以正常响应，以及响应状态码、响应头部或者内容是否正确。

## 操作须知
1. 腾讯云 CVM 实例、腾讯云 ES 集群和 Logstash 实例，必须在同一 VPC 下。且腾讯云 ES 集群和 Logstash 实例的大版本相同。
>!Beats 目前仅支持64位的 Linux 操作系统。
2. 腾讯云 CVM 实例必须安装自动化助手，仅支持为已安装自动化助手的 CVM 实例下发采集器配置。具体操作参见 [安装自动化助手客户端](https://cloud.tencent.com/document/product/1340/51945)。

## 操作步骤
### Heartbeat 采集器配置
1. 登录 [Elasticsearch Service 控制台](https://console.cloud.tencent.com/es/beats) Beats 管理界面，授权服务相关角色，单击创建 **Heartbeat** 采集器。
![](https://qcloudimg.tencent-cloud.cn/raw/fc5d5d8f5ecc46b8acdffd977ccb5b7d.png)
2. 在创建 Heartbeat 采集器中，设置采集器信息。
 - 配置 Heartbeat 采集器，输入或选择采集器配置信息。完成后单击**下一步**。
    - 采集器名称：自定义采集器的名称，格式为1个 - 50个英文、汉字、数字、连接线（-）或下划线（\_）。 
    - 安装版本：支持6.8.15或7.10.2版本。  
    - 采集器输出：采集的数据支持传送到腾讯云 Elasticsearch 与 Logstash 实例，请选择与需采集数据的 CVM 在同一 VPC 下的 ES 集群和 Logstash 实例。不支持输出至开源版 ES 集群。
    - 用户名密码：若选择输出采集数据到开启用户登录认证的 ES 集群，需要填写用户名和密码，使 Heartbeat 有权限向 ES 集群中写入数据。用户名默认为 elastic，密码为集群创建时设置。
    - Monitoring：勾选后在 Kibana 内生成监控 Heartbeat 的相关指标。当采集器输出为 ES 集群时，Monitoring 默认使用和采集器输出相同的 ES 集群；当采集器输出为 Logstash 实例时，则需要在配置文件中额外添加用于存储监控数据的 ES 集群地址。
    - Kibana Dashboard：勾选后生成默认的 Kibana Dashboard。  
    - 采集器 YML 配置：配置内容如下，更多 YML 配置请参考官方文档 [Configure Hearbeat](https://www.elastic.co/guide/en/beats/heartbeat/current/configuring-howto-heartbeat.html)。
      - type：monitor 类型，支持 icmp、tcp、http。
      - id：自定义的 monitor 名称。
      - name：自定义的 monitor 名称。
      - hosts：指定要检测的服务地址。
      - schedule：检测频率，`*/5 * * * * * *`表示每隔5s检测一次。
      - check.response.status：当 monitor 为 http 时，http 接口正常响应时的状态码，如200。
![](https://qcloudimg.tencent-cloud.cn/raw/36560e5458b900fd0a8f1b6c31749b8d.png)
 - 将采集器安装到 CVM 实例。选择要安装采集器的 CVM 实例，完成后单击**确定启用**。
     - CVM 必须安装自动化助手，仅支持为已安装自动化助手的 CVM 实例下发采集器配置。
     - 仅支持选择和采集器输出在同一 VPC 下的 CVM 实例进行安装，若无法找到目标 CVM 实例，需要更改采集器输出。
![](https://qcloudimg.tencent-cloud.cn/raw/1130bac6d7016b4bb56786e6ea6ef293.png)
3. 单击**确定启用**后，跳转到 Beats 采集器管理界面，可以查看 Heartbeat 采集器运行状态，显示“正常”则表示采集器安装成功。支持 [修改采集器配置](https://cloud.tencent.com/document/product/845/63301) 和 [管理 CVM 实例](https://cloud.tencent.com/document/product/845/63302)。

![](https://qcloudimg.tencent-cloud.cn/raw/5fa28e39ad540a9b7a289a09d2ee6923.png)

### Kibana 查看结果
1. 登录腾讯云 Kibana 控制台。
2. 在 Kibana 左侧导航栏单击 **Discover**，查询 Heartbeat 采集的数据。
![](https://main.qcloudimg.com/raw/35140dc9a421b5b12952b5dc86686af5.png)


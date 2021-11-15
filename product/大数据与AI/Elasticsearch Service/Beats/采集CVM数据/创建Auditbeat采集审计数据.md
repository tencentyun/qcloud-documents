Auditbeat 是轻量的审计数据采集器，能够收集和监控腾讯云 CVM Linux 审计框架数据，并基于 Kibana 实现可视化分析。

## 应用场景
Auditbeat 可用于审核 Linux 系统上用户和进程的活动，例如，可以使用 AuditBeat 从 Linux Audit Framework 采集并集中审核事件，也可以使用 Auditbeat 来检测对二进制文件或者配置文件的修改，并发现潜在的安全策略冲突。

Auditbeat 目前有两种模块：
- auditd：auditd 模块用于接收来自 Linux 审计框架的审计事件。审计框架是 Linux 内核的一部分，该模块建立对内核事件的订阅，使得在事件发生时可以接收到通知。如果使用 auditd 模块，部分系统中其他的监控工具可能会干扰 Auditbeat，例如，在服务器中启用 audit 进程来从 Linux 审计框架中接收数据，此时 Auditbeat 的运行会收到影响，需要先通过执行`service auditd stop`命令来关闭 auditd 进程。关于该模块更详细的介绍请参考官方文档 [Auditd Module](https://www.elastic.co/guide/en/beats/auditbeat/7.15/auditbeat-module-auditd.html)。
- file\_integrity：file\_integrity 模块用于实时监控指定目录下的文件的改动。**在 Linux 系统中，需要使用 inofity 才可以启用该模块，2.6.13版本以上的 Linux 内核均已默认安装了 inofity。**关于该模块更详细的介绍请参考官方文档 [File Integrity Module](https://www.elastic.co/guide/en/beats/auditbeat/7.15/auditbeat-module-file_integrity.html)。

## 操作须知
1. 腾讯云 CVM 实例、腾讯云 ES 集群和 Logstash 实例，必须在同一 VPC 下。且腾讯云 ES 集群和 Logstash 实例的大版本相同。
>!Beats 目前仅支持64位的 Linux 操作系统。
2. 腾讯云 CVM 实例必须安装自动化助手，仅支持为已安装自动化助手的 CVM 实例下发采集器配置。具体操作参见 [安装自动化助手客户端](https://cloud.tencent.com/document/product/1340/51945)。

## 操作步骤
### Auditbeat 采集器配置
1. 登录 [Elasticsearch Service 控制台](https://console.cloud.tencent.com/es/beats) Beats 管理界面，授权服务相关角色，单击创建 **Auditbeat** 采集器。
![](https://qcloudimg.tencent-cloud.cn/raw/363699bcac5ef6ede32ef066a9ecc79f.png)
2. 在创建 Auditbeat 采集器中，设置采集器信息。
 - 配置 Auditbeat 采集器，输入或选择采集器配置信息。完成后单击**下一步**。
     - 采集器名称：自定义采集器的名称，格式为1个 - 50个英文、汉字、数字、连接线（-）或下划线（\_）。 
     - 安装版本：支持6.8.15或7.10.2版本。  
     - 采集器输出：采集的数据支持传送到腾讯云 Elasticsearch 与 Logstash 实例，请选择与需采集数据的 CVM 在同一 VPC 下的 ES 集群和 Logstash 实例。不支持输出至开源版 ES 集群。
     - 用户名密码：若选择输出采集数据到开启用户登录认证的 ES 集群，需要填写用户名和密码，使 Auditbeat 有权限向 ES 集群中写入数据。用户名默认为 elastic，密码为集群创建时设置。
     - Monitoring：勾选后在 Kibana 内生成监控 Auditbeat 的相关指标。当采集器输出为 ES 集群时，Monitoring 默认使用和采集器输出相同的 ES 集群；当采集器输出为 Logstash 实例时，则需要在配置文件中额外添加用于存储监控数据的 ES 集群地址。
     - Kibana Dashboard：勾选后生成默认的 Kibana Dashboard。  
     - 采集器 YML 配置：auditd 模块和 file\_integrity 模块配置如下，更多 YML 配置请参考官方文档 [Configure modules](https://www.elastic.co/guide/en/beats/auditbeat/7.15/configuration-auditbeat.html)。
      - auditd 模块：
          - audit\_rule\_files：指定的审计规则文件路径，支持通配符。
          - audit\_rules：自定义的审计规则（一般情况下默认的审计规则就可以满足审计需求）。
      - file\_integrity 模块：
         - paths：用于指定被监控的文件的路径，默认的文件路径包含 /bin、/usr/bin、/sbin、/usr/sbin、/etc。
![](https://qcloudimg.tencent-cloud.cn/raw/f9e6e33cdbb407b16a2af762ccbeee29.png)
 - 将采集器安装到 CVM 实例。选择要安装采集器的 CVM 实例，完成后单击**确定启用**。
     - CVM 必须安装自动化助手，仅支持为已安装自动化助手的 CVM 实例下发采集器配置。
     - 仅支持选择和采集器输出在同一 VPC 下的 CVM 实例进行安装，若无法找到目标 CVM 实例，需要更改采集器输出。
![](https://qcloudimg.tencent-cloud.cn/raw/664edd917bb188e4a0686cae525ac7a5.png)
3. 单击**确定启用**后，跳转到 Beats 采集器管理界面，可以查看 Auditbeat 采集器运行状态，显示“正常”则表示采集器安装成功。支持 [修改采集器配置](https://cloud.tencent.com/document/product/845/63301) 和 [管理 CVM 实例](https://cloud.tencent.com/document/product/845/63302)。

![](https://qcloudimg.tencent-cloud.cn/raw/5fa28e39ad540a9b7a289a09d2ee6923.png)

### Kibana 查看结果
1. 在 Kibana 左侧导航栏单击 **Discover**，查询 Auditbeat 采集的数据：
   ![](https://main.qcloudimg.com/raw/7e05fff2cf738d49901f6ecbe25a9a91.png)
2. 在 Kibana 左侧导航栏，单击 **Dashboard**，在 Dashboard 列表中，单击 **[Auditbeat File Integrity] Overview**，查看监控文件的变动情况：
   ![](https://main.qcloudimg.com/raw/d6faf740ca520cb2968432bf2f83cd94.png)


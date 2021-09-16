应用性能观测（APM）覆盖了 TSW 对于 Skywalking 协议的兼容和支持，您只需要简单修改上报信息，即可完成从 TSW 到 APM 的迁移。
整个过程预计耗时10分钟。

## 准备工作
我们已经把您默认添加到了应用性能观测服务的白名单，您无需再次提交开白申请，直接登录 [应用性能观测控制台](https://console.cloud.tencent.com/apm) 即可开始体验。

### 创建业务系统
应用性能观测服务继承 TSW 原有业务系统的概念，以便更好地组织和管理被监控的服务，并实现业务监控。您可以参考 TSW 业务系统部署关系在 APM 创建业务系统，两个业务系统的作用都是应用分组。
>?为了更好的帮助您管理成本，不同的业务系统在应用性能观测平台中是不同的资源实例，所以不同业务系统间会进行数据隔离。后续您也可以在计费结算中，得到业务系统维度的成本统计。

进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **资源管理**页面，单击**新建**即可创建业务系统。
>!业务系统创建成功之后，我们会为您自动分配上报 Token。

### 获取接入点和 Token
进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **应用监控** > **应用列表**页面，单击**添加应用**，在添加应用列 Java 语言与 SkyWalking 的数据采集方式。
在应用接入步骤获取您的接入点和 Token，如下图所示：
![](https://main.qcloudimg.com/raw/d7d94913947d31edf70e85c6462c6bac.png)

## 上报迁移
### Java 应用迁移
1. 打开 config/agent.config 文件，配置接入点、 Token 和自定义服务名称。
```
collector.backend_service=<接入点>
agent.authentication=<Token>
agent.service_name=<上报的服务名称>
```
2. 根据应用的运行环境，选择相应的方法来指定 SkyWalking Agent 的路径
 - Linux Tomcat 7/Tomcat 8
   在 `tomcat/bin/catalina.sh`  第一行添加以下内容：
```
CATALINA_OPTS="$CATALINA_OPTS -javaagent:<skywalking-agent-path>"; export CATALINA_OPTS
```
 - JAR File 或 Spring Boot
    在应用程序的启动命令行中添加 -javaagent 参数，参数内容如下：
```
java -javaagent:<skywalking-agent-path> -jar yourApp.jar
```
3. 重新启动应用

完成上述部署步骤后，根据 [Skywalking 官网指导](https://github.com/apache/skywalking/blob/v8.2.0/docs/en/setup/service-agent/java-agent/README.md#install-javaagent-faqs) 重新启动应用即可。
### Go应用迁移
1. 修改上报配置，将 reporter 的 serverAddr 修改为 APM 的接入点，将 reporter 的 auth 修改为 APM 的 Token。
2. 重启服务，开始上报数据。



<dx-alert infotype="explain" title="迁移常见疑问">
1. 是否会迁移 TSW 里的监控数据？
考虑到 Trace 数据的时效性较强，同时目前TSW仅处于内测阶段。我们将不会迁移您的历史数据。
2. 云监控 APM 和 TSW 相比有哪些变化？
  - 增加 JVM 监控指标分析。
  - 更可靠易用的应用性能指标告警。
  - 架构优化，更稳定的性能。
</dx-alert>


<dx-alert infotype="explain" title="">
如迁移过程中有任何疑问，您可通过以下方式加入微信交流群：

添加小助手微信（微信号：hitherecm ），回复 “APM” ，小助手将会拉您进入微信交流群。
直接扫描以下二维码，添加小助手微信，小助手将会拉您进入微信交流群。
<img src="https://main.qcloudimg.com/raw/c20740abb44f5cdf8de337879b658366.jpg" style="width: 20%"></img>
</dx-alert>


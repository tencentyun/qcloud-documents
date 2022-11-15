Java Agent 基于字节码增强技术研发，支持自动埋点完成数据上报，Java Agent 包含(并二次分发) opentelemetry-java-instrumentation CNCF 的开源代码，遵循 Apache License 2.0 协议，在 Java Agent 包中对 opentelemetry License 进行了引用。

>?OpenTelemetry 是工具、API 和 SDK 的集合。使用它来检测、生成、收集和导出遥测数据（指标、日志和跟踪），以帮助您分析软件的性能和行为。OpenTelemetry 社区活跃，技术更迭迅速，广泛兼容主流编程语言、组件与框架，为云原生微服务以及容器架构的链路追踪能力广受欢迎。通过对 Java 字节码的增强技术 OpenTelemetry-java-instrumentation 可以实现自动埋点上报数据,且腾讯云 APM 基于 OpenTelemetry-java-instrumentation 进行二次开发,可以让您拿到更完善的调用琏数据及其对应的行号信息。

本文将通过相关操作介绍如何在腾讯云 APM 使用 OpenTelemetry-java-instrumentation 上报 Java 应用数据。


### 步骤一：获取接入点和 Token
进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **应用监控** > **应用列表**页面，单击**接入应用**，在接入应用时选择 Java 语言与 OpenTelemetry 的数据采集方式。
在选择接入方式步骤获取您的接入点和 Token，如下图所示：
![](https://main.qcloudimg.com/raw/d7d94913947d31edf70e85c6462c6bac.png)
<dx-alert infotype="explain" title="上报方式说明">
- 内网上报：使用此上报方式，您的服务需运行在腾讯云 VPC 。通过 VPC 直接联通，在避免外网通信的安全风险同时，可以节省上报流量开销。
- 外网上报：当您的服务部署在本地或非腾讯云 VPC 内，可以通过此方式上报数据。请注意外网通信存在安全风险，同时也会造成一定上报流量费用。
  </dx-alert>


### 步骤二：下载 opentelemetry-javaagent.jar 
>?  OpenTelemetry-java-instrumentation 支持数十种框架自动埋点能力。更多信息，请参见 [OpenTelemetry 官方文档](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md?spm=a2c4g.11186623.0.0.1e455765eR4tEn&file=supported-libraries.md)。

下载  Java agent： [opentelemetry-javaagent.jar]( https://github.com/TencentCloud/tencentcloud-opentelemetry-java.git)。
![](https://qcloudimg.tencent-cloud.cn/raw/6176ee3745ffe0ad7c60c33ded2a4bf3.png)

### 步骤三：修改上报参数
通过修改 Java 启动的 VM 参数上报链路数据。
```
-javaagent:/path/to/opentelemetry-javaagent.jar    //请将路径修改为您文件下载的实际地址。
-Dotel.resource.attributes=service.name=<appName>,token=<token> //service.name：服务名,如果是spring cloud/dubbo服务，最好与其服务名保持一致
-Dotel.exporter.otlp.endpoint=<接入点>
```
>?
>- 如果您选择直接上报数据，请将< token >替换成从前提条件中获取的 Token ，将<接入点>替换成对应地域的接入点。替换对应参数值时，“< >”符号需删去，仅保留文本。
>- 如果您选择使用 OpenTelemetry Collector 转发，则需删除-Dotel.exporter.otlp.headers=Authentication=< token >并修改<接入点>为您本地部署的服务地址。

### 步骤四：启动您的应用
### 查看应用数据
登录 [应用性能观测控制台](https://console.cloud.tencent.com/apm) ，在应用列表中即可查看性能数据。


## 操作场景
当您已经使用 Skywalking 追踪应用服务的调用数据时，您可通过客户端将 Tracing 数据上报至 TSW。通过将客户端采集的 Tracing 数据上报给 TSW，您可在 TSW 控制台使用全量功能，同时免除运维 Skywalking 服务端的人力成本与机器成本。此外，您无需对客户端进行代码修改，仅需修改上报配置即可完成接入。

## 前提条件
- 下载 SkyWalking 8.X.X版本（[下载地址](http://skywalking.apache.org/downloads/)），解压后将 Agent 文件放至 Java 应用宝所在目录下。
- 插件放置路径与日志输出路径与原生保持一致，不要改变文件夹的结构。

## 操作流程
#### 1. 获取接入点信息与 Token
在 [TSW 控制台](https://console.cloud.tencent.com/tsw)的【服务监控】>【服务列表】页，单击【接入服务】，选择 Java 语言与 Skywalking 的数据采集方式。
您可在下方的获取接入点和 Token 中找到私网接入点与您的个人 Token。
![](https://main.qcloudimg.com/raw/3af9f458e45a0d45274476e91f39207f.png)

#### 2. 下载 Skywaling
- 若您已经使用了 Skywalking，可跳过本步骤。
- 若您还未使用 Skywalking，建议 [下载最新版本](http://skywalking.apache.org/downloads/?spm=a2c4g.11186623.2.12.65355968AbUoDc)，将解压后的 Agent 文件夹放至 Java 进程有访问权限的目录，插件均放置在 /plugins 目录中。

#### 3. 打开 config/agent.config，配置接入点和 Token。并配置好服务名称。
collector.backend_service=&lt;endpoint&gt;
agent.authentication=&lt;auth-token&gt; 
agent.service_name=&lt;ServiceName&gt;

#### 4. 重启
根据 [官网指导](https://github.com/apache/skywalking/blob/v8.2.0/docs/en/setup/service-agent/java-agent/README.md#install-javaagent-faqs)，指定 Agent 路径。完成后重启。

## 接入验证
向应用发送请求，在收到响应后，在 TSW 控制台查看调用数据。
您可以在1分钟内通过【链路追踪】>【调用链查询】>【[Span查询](https://console.cloud.tencent.com/tsw/trace?rid=1&tab=span)】查找调用详情。监控曲线与统计数据将在1分钟后开始正常显示。


## Prometheus 介绍
[Prometheus](https://prometheus.io/) 是一个非常灵活的时序数据库，通常用于监控数据的存储、计算和告警。

用户可以将 Flink 内置的 [各项指标](https://ci.apache.org/projects/flink/flink-docs-release-1.11/zh/monitoring/metrics.html)，连同自己定义的业务指标，统一通过 Prometheus Pushgateway 的方式，推送到自建或者腾讯云 Prometheus 服务端，随后即可对 Grafana 面板进行分组、聚合和数据展示。

流计算 Oceanus 建议用户使用腾讯云监控提供的 [Prometheus 服务](https://console.cloud.tencent.com/monitor/prometheus)，以免去部署、运维开销；同时它还支持腾讯云的 [通知模板](https://console.cloud.tencent.com/monitor/alarm2/notice)，可以通过短信、电话、邮件、企业微信机器人等方式，将告警信息轻松触达不同的接收方。

## Oceanus Grafana 面板导入方法
1. 下载 Oceanus Grafana Dashboard 模板并解压到本地。[点此下载 Dashboard](https://oceanus-public-1257058918.cos.ap-guangzhou.myqcloud.com/Oceanus-Prometheus-Dashboard.zip)
2. 在 Prometheus 的 Grafana 面板上，鼠标移动到左边栏，选择![](https://main.qcloudimg.com/raw/1747bb326e66317fc234c04530896607.png) **> Manage**。
![](https://main.qcloudimg.com/raw/4899b13ef9523d5f5dbb3491018dc6aa.png)
3. 创建一个名为 Oceanus 新文件夹。
![](https://main.qcloudimg.com/raw/e6886e7dd7b99a6d1ebca724bd923d50.png)![](https://main.qcloudimg.com/raw/ce24ede1a62e492fbf2fa9e896d2883b.png)
4. 再次进入 Dashboard 管理页面，单击右上角的 **Import**，**逐个**将解压后的 json 文件内容粘贴进来。
> !
>- 请按照下文指引，逐一导入每个 JSON 文件。
>- 不要修改面板的 UID（即不要单击 **Change uid**），以免面板之间的跳转链接失效。
>
![](https://main.qcloudimg.com/raw/262bcf13814f254c8eac922e62a81852.png)
![](https://main.qcloudimg.com/raw/dc0a7cd37ebdb2154ee0f03d2a0df7b0.png)![](https://main.qcloudimg.com/raw/61ad2099bbc35aa07c5256fce2e48784.png)![](https://main.qcloudimg.com/raw/54481cc9355d7bc21a6c25faeb89f48d.png)
5. 导入完毕后，检查 Oceanus 目录是否包含了如下面板：
![](https://main.qcloudimg.com/raw/cc4eda9ac87d43c1ff9f6840f0ccec1c.png)

## 作业启用 Prometheus 监控指标上报
> !
>- 每个作业需要单独配置 Prometheus 上报。
>- 修改每个作业的配置后，必须单击**发布运行**，待作业重启后才会正式上报监控数据。

1. 在 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus/job)，单击需要添加监控的作业，进入**开发调试**面板。
![](https://main.qcloudimg.com/raw/469266f4c077fa0584113f8bc231f037.png)
2. 单击**作业参数**，在高级参数中新增以下内容：
> ! ${ } 的变量需替换为实际值。
> 
```yaml
metrics.reporters: promgateway
metrics.reporter.promgateway.host: ${Prometheus PushGateway 的 IP 地址}
metrics.reporter.promgateway.port: ${Prometheus PushGateway 的端口}
```
 如果使用腾讯云监控的 Prometheus 服务，还需要额外配置鉴权信息（Password 即控制台看到的 Token）：
```yaml
metrics.reporter.promgateway.needBasicAuth: true
metrics.reporter.promgateway.password: ${Prometheus 访问密码}
```
 **示例图：**
![](https://main.qcloudimg.com/raw/3f305d970ab40af7b6b99aa1808086f0.png)![](https://main.qcloudimg.com/raw/b36788e0d29379f88f408bf3be892d64.png)
2. 以新的配置发布并启动作业，稍等1分钟（上报周期），随后即可查看面板上的数据。
![](https://main.qcloudimg.com/raw/740638bdbdefa2d860d0afbfb623a278.png)
3. 还可以编辑 Prometheus 面板，以满足个性化的监控需求。
![](https://main.qcloudimg.com/raw/173aba463177171d6ecfd26f4a1b4d79.png)

## 告警配置
如果希望对某项指标进行告警，我们以 `Checkpoint 失败数`为例，在腾讯云 [Prometheus 监控](https://console.cloud.tencent.com/monitor/prometheus) 上展示配置告警策略的方法。
1. 在 Dashboard 选择需要配置告警的指标项，例如 `Checkpoint 失败数`。
![](https://main.qcloudimg.com/raw/aa79e8cca779680dac9317d0e8535154.png)
2. 进入编辑界面，查看告警指标的查询条件。
![](https://main.qcloudimg.com/raw/846fe998f9c201d66cf25247df455fef.png)
![](https://main.qcloudimg.com/raw/617f95916d5f5eb2aa13e4781e411a57.png)
3. 进入 Prometheus 的告警配置界面，新增一条规则。
> ! 
>- 在规则 PromQL 中，{ } 中不要包含上图中的 Grafana 变量，例如 `instance_id="$InstanceId"` 等。如果需要按条件筛选，请在 { } 中填入具体值，例如 `instance_id="cql-abcd0012"`。
>- 数据源中的标签（例如 job_id），可以在告警对象和告警消息中引用，例如 `{{ $labels.job_id }}`，而查询语句的值可以用 `{{ $value }}` 表示。
> 
![](https://main.qcloudimg.com/raw/ec1b90b289b6a92e816e03c579a51e1f.png)
4. 当告警触发、恢复时，配置的告警渠道就会收到通知。此外，[通知模板](https://console.cloud.tencent.com/monitor/alarm2/notice) 中还支持短信、电话、邮件等其他告警渠道。
> !这里演示企业微信回调推送到群机器人（Bot）。
> 
![](https://main.qcloudimg.com/raw/a30e7fcb7a181fed581c9e7901905e32.png)

当前腾讯云服务网格（Tencent Cloud Mesh，TCM）集成了 [云监控 CM](https://cloud.tencent.com/document/product/248)、 [云原生监控 TPS](https://cloud.tencent.com/document/product/457/49888)，为您提供服务流量 metric 数据的收集、存储与展示。

服务网格控制台集成云监控，提供 metric 数据的基础图表与分析，如您有自定义监控的诉求，您可以开启高级监控，网格 metric 数据将集成至云原生监控托管 Prometheus 监控实例，通过预置 Grafana Dashboard 或自定义 Dashboard 即可实现灵活自定义监控的诉求。

## 服务网格控制台基础监控

TCM 集成云监控的能力，控制台基于 metric 数据提供网格拓扑、服务拓扑、服务监控（请求数、请求状态码分布、请求耗时、请求大小）图表的展示分析。

### 网格拓扑

网格拓扑记录服务网格所有服务的调用结构，查看网络拓扑须确保相关服务已注入 sidecar，且存在请求流量。

查看指定网格的网络拓扑流程：

1. 登录 [服务网格控制台](https://console.cloud.tencent.com/tke2/mesh)，在列表页面单击指定网格 ID，进入网格详情页面。
2. 单击左侧**网格拓扑**页签，即可查看当前服务网格拓扑图。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1eaf3b71d5d36af87c91bc07f78a167e.png)
3. 点击节点可展示该节点相关的监控详情。如下图所示：
![](https://main.qcloudimg.com/raw/7672985c2203a42074b37f35dfc7fd2a.png)
4. 界面上方可以选择数据过滤条件，包括 namespace 与时间跨度；支持切换节点的粒度，当前支持 service 粒度和 workload 粒度。如下图所示：
![](https://main.qcloudimg.com/raw/3f091e8c0ca0c98f23b59d5ba6fc81d3.png)

### 服务拓扑

服务拓扑记录某个服务的前后调用依赖关系，查看指定服务的服务拓扑流程是：

1. 在指定网格的详情页面，点击左侧**服务**进入服务列表页，点击想要查看的服务，进入服务详情页。
![](https://main.qcloudimg.com/raw/8b01e1ca0aed5c1d78a9803effb272a0.png)
2. 在服务详情页面的基本信息 Tab，第二个卡片即可查看该服务的服务拓扑。
![](https://main.qcloudimg.com/raw/031055264e7fba1cfffc0b4942c25bf4.png)

### 服务监控

您可以在服务列表页面对比多个服务的监控数据（请求数、请求耗时、请求大小等），或在服务详情页面查看指定服务的监控详情。

- 在服务列表页查看多个服务的监控数据：
![](https://main.qcloudimg.com/raw/ee2db2675ae941d28eec98c850ba8d20.png)
- 在服务详情页面查看指定服务的监控数据详情图表：在服务详情页面的监控 Tab 即可查看。
![](https://main.qcloudimg.com/raw/e77e2471a8e82231327c6ac37b1b9778.png)

## 高级监控

如您有更灵活的自定义 metric 监控数据分析的诉求，服务网格控制台基础监控图表无法满足，您可以为网格开启高级监控，当前 TCM 高级监控功能支持将 metric 数据对接至 [云原生监控](https://cloud.tencent.com/document/product/457/49888) 托管 Prometheus 监控实例，请确认前往 TPS 控制台完成 [TPS 服务相关角色授权](https://console.cloud.tencent.com/tke2/prometheus)。您可以在创建服务网格时或网格创建完成后在网格详情页为网格开启高级监控功能，开启后提供预置的 Service Mesh Grafana Dashboard。

- 创建服务网格时开启高级监控：
![](https://qcloudimg.tencent-cloud.cn/raw/dbaf2ad761b6d75f080ad1cc26971994.png)
- 网格创建完成后，网格详情页面开启高级监控：
![](https://main.qcloudimg.com/raw/affb975b4e200a77e1483ef402981b61.png)
![](https://qcloudimg.tencent-cloud.cn/raw/8d426682a6aac18829b0a51b88a13daf.png)

您可以选择自动创建云原生监控实例，或关联已有云原生监控实例。选择自动创建云原生监控实例将在网格所在地域自动创建云原生监控实例，如当前网格的服务发现集群为空，您还需要选择自动创建的云原生监控实例所在的网络，并保证后续添加的服务发现集群与所选网络的连通性，否则 TCM metric 数据无法正常采集。选择关联已有的云原生监控实例，您需要保证所选实例与服务所在网络的连通性，否则 TCM metric 数据无法正常采集。

**高级监控** > **云原生监控**开启后，您可以登录 Grafana 查看已预置的 Grafana Dashboard，查看监控数据。
![](https://main.qcloudimg.com/raw/155a87eabe1c59662c7ab617426f9d9e.png)
![](https://main.qcloudimg.com/raw/32599053a427f168359122fb2722203f.png)

更多关于云原生监控产品的信息，请参见 [云原生监控](https://cloud.tencent.com/document/product/457/49888) 。

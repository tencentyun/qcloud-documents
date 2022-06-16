当前腾讯云服务网格使用 Prometheus 作为监控指标存储方案，您可选择使用 [Prometheus 监控 TMP](https://cloud.tencent.com/document/product/457/71896) 为您提供服务流量 metric 数据的收集、存储与展示，也可以使用第三方 Prometheus 服务，作为监控指标存储服务。

服务网格数据面 Sidecar 将 Metric 数据上报到 TMP 或第三方 Prometheus 服务，控制台从对应的服务查询指标数据，并提供网格拓扑、服务拓扑、服务监控（请求数、请求状态码分布、请求耗时、请求大小）图表的展示分析。此外，如果您有自定义监控的诉求，可以通过 TMP 中的 Grafana 面板设置自定义的监控面板。

## 操作步骤


### 开启 TMP 监控
在 [**创建网格**](https://cloud.tencent.com/document/product/1261/62958) 或**网格基本信息页**中的可观测性配置 >  监控指标中，勾选**腾讯云 Prometheus 监控 TMP**，按需选择自动创建或者关联已有 TMP 实例即可。开启后，Sidecar 将会将 metric 数据上报到对应的实例，您也可以在 TMP 控制台查看该实例。
![](https://qcloudimg.tencent-cloud.cn/raw/064b68e13ee610b9f1b491e41dbdfbc2.png)

### 开启第三方 Promehtues 服务
在 [**创建网格**](https://cloud.tencent.com/document/product/1261/62958) 或**网格基本信息页**中的可观测性配置 >  监控指标中，勾选第三方 Prometheus 服务，填写该服务对于的 VPC 信息、地址、认证信息。
>? 由于 TCM 控制台会从 Prometheus 服务中查询和展示监控指标数据，对数据源服务的网络可达性、稳定性要求较高，因此当前仅支持通过内网的形式访问。
> 
![](https://qcloudimg.tencent-cloud.cn/raw/20b6d37040aa83341199c26db5b26c3c.png)

### 查看监控相关图表
#### 网格拓扑
记录服务网格所有服务的调用结构，查看网络拓扑须确保相关服务已注入 sidecar，且存在请求流量。查看指定网格的网络拓扑流程如下：
1. 登录 [服务网格控制台](https://console.cloud.tencent.com/tke2/mesh)，在列表页面单击指定网格 ID，进入网格详情页面。
2. 单击左侧**网格拓扑**页签，即可查看当前服务网格拓扑图。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1eaf3b71d5d36af87c91bc07f78a167e.png)
3. 单击节点可展示该节点相关的监控详情。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/3afd6e9a651775192e59a68166dd88ff.png)
4. 界面上方可以选择数据过滤条件，包括 namespace 与时间跨度；支持切换节点的粒度，当前支持 service 粒度和 workload 粒度。如下图所示：
![](https://main.qcloudimg.com/raw/3f091e8c0ca0c98f23b59d5ba6fc81d3.png)

#### 服务拓扑
记录某个服务的前后调用依赖关系，查看指定服务的服务拓扑流程如下：

1. 在指定网格的详情页面，单击左侧**服务**进入服务列表页。
2. 单击想要查看的服务，进入服务详情页。
![](https://qcloudimg.tencent-cloud.cn/raw/786e24f78b11fc23a9d3dc8849260662.png)
3. 在服务详情页面的“基本信息”中，即可查看该服务的服务拓扑。如下图所示：
![](https://main.qcloudimg.com/raw/031055264e7fba1cfffc0b4942c25bf4.png)

#### 服务监控
您可以在服务列表页面对比多个服务的监控数据（请求数、请求耗时、请求大小等），或在服务详情页面查看指定服务的监控详情。

- 在服务列表页查看多个服务的监控数据：
	1. 登录 [服务网格控制台](https://console.cloud.tencent.com/tke2/mesh)，在列表页面单击指定网格 ID，进入网格详情页面。
	2. 选择**服务 > 监控**，单击需查看监控数据的服务并在右侧查看服务监控数据。如下图所示：
  ![](https://qcloudimg.tencent-cloud.cn/raw/cfbfd88bb869170077255591245b6afe.png)


  
- 在服务详情页面查看指定服务的监控数据详情图表：
 1. 在指定网格的详情页面，单击左侧**服务**进入服务列表页。
 2. 单击想要查看的服务，进入服务详情页。
 3. 在服务详情页面的“监控”中即可查看。
![](https://main.qcloudimg.com/raw/e77e2471a8e82231327c6ac37b1b9778.png)

### 关闭监控

您可以在**网格基本信息页**选择编辑可观测性配置，取消勾选**腾讯云 Prometheus 监控 TMP**，取消勾选后，服务网格侧并不会删除 TMP 实例，如有需要，请在 [TMP 控制台](https://console.cloud.tencent.com/tke2/prometheus2/list?rid=4) 进一步删除该 TMP 实例。

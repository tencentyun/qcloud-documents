服务网格默认集成应用性能观测 APM 作为调用追踪消费端，开启后网格将会为您创建一个 APM 实例并将 tracing 数据上报到对应的 APM 实例，您可以在服务网格控制台查看到请求在网格内的完整调用瀑布图和每层调用的 trace 日志信息，帮助您理解服务的调用依赖，以及做网格内的延迟分析。您也可以直接在 APM 控制台查看调用相关数据。

除了 APM 之外，网格支持将调用数据上报到第三方 Jaeger/Zpkin 服务，如果开启使用第三方 tracing 服务，则服务网格控制台将无法展示调用追踪相关信息，需要在第三方服务中查看。


## 配置调用追踪采样率

调用追踪采样率是 trace 数据的采样比例，sidecar 采集与上报数据消耗资源与带宽和采样率成正相关。通常生产环境下，不需要为所有调用都生成 trace 数据并采集上报，避免过多消耗计算资源与带宽资源，只需要配置一定比例即可。建议开发测试环境可以配置100%采样率，生产环境配置1%采样率。

您可以通过以下两种方式配置调用追踪采样率：

#### 方式1：在网格创建时配置采样率

1. 登录 [服务网格控制台](https://console.cloud.tencent.com/tke2/mesh)。
2. 选择地域，单击页面左上角的**新建**。
3. 在创建服务网格页面，按需填写网格创建相关配置，在“可观测性配置”中配置采样率。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/26433b10e90d87609af2ca6a759ffd08.png)


#### 方式2：在网格基本信息页面修改采样率配置
1. 登录 [服务网格控制台](https://console.cloud.tencent.com/tke2/mesh)。
2. 选择地域，单击需要变更配置的网格 ID，进入网格的管理页面。
![](https://qcloudimg.tencent-cloud.cn/raw/c6dc859ba3eef984187211bc38bca516.png)
2. 在网格基本信息页面，单击**调用追踪 > 采样率** 的![](https://qcloudimg.tencent-cloud.cn/raw/ccc8b44f4283be7f9e6d11993fab08a5.png)，调整采样率。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1f447ca5462b3d653f1412cd410122bd.png)


## 查看调用追踪

>? 由于服务网格中的 service 并非任何情况下都与 k8s service 完全一一对应， tracing span 中上报服务名时实际使用 pod 中 app label值作为服务名（k8s service 亦是通过此 label 关联 pod，但service name 可以和 label 不同）。控制台查询服务调用链信息时，服务名默认使用 k8s service 名查询，因此如果 k8s service 名 和 pod 的 app label 不匹配时，控制台无法查询到相应数据。

查看调用追踪的流程如下：

1. 需要关注网格某个服务的调用情况，在网格的服务列表页面单击该服务，进入服务详情页面。
![](https://main.qcloudimg.com/raw/74dc1322db1c4632a63f61d20dafac78.png)
2. 在服务详情页面单击**调用追踪**，您可以查看到该服务作为被调方，被调用的记录列表，以及这些调用记录的耗时分布统计直方图。
![](https://main.qcloudimg.com/raw/6f91e54969ce1bedd9b61667fc2a3b10.png)
3. 被调记录列表第一列记录了调用的 URL，单击即可查看该调用相关的完整调用链路瀑布图，上方瀑布图概览可以拖拽实现缩放。
![](https://main.qcloudimg.com/raw/fbdd2c75aa908ba1251acffcca968fed.png)
![](https://main.qcloudimg.com/raw/27ffe0f1ccdeeeef1d8ca2e479c415ba.png)
4. 单击想要查看详情的调用，可以查看对应调用环节的详细 trace 日志。
![](https://main.qcloudimg.com/raw/463834f7af476e8677c5047c7a682453.png)
5. 单击关闭按钮可关闭 span 详情，以及返回服务被调记录列表页。
![](https://main.qcloudimg.com/raw/57c0e5e319df3ecbb08313644977d7f2.png)
6. 查询服务被调记录 Tips：您可以按照耗时、时间跨度、源端IP、Trace ID、返回码过滤被调记录，过滤完成后您可以按照**延时**和**开始时间**对调用记录排序，方便您选择查看需要关注的调用。
![](https://main.qcloudimg.com/raw/e8136d1be43345d1c1d8ff91c43e3305.png)


## 查看完整调用链


完整调用链形成的基本条件是需要请求经过每个环节的调用链路信息都能往下传递直到请求结束，虽然 Sidecar 在转发请求时会增加链路追踪相关的信息。但由于 Sidecar 处理 in、out 流量是在两个独立的步骤中进行的，且这两个步骤之间是 Sidecar 无法干预的业务逻辑环节（由于传递链路被业务逻辑步骤打断，Sidecar 也失去了 in、out 流量映射关系），所以如果业务代码处理业务请求时不转发这些额外的调用链路信息，则链路形成将会中断。因此服务网格无法实现完全无侵入的全链路追踪，需要在业务代码中添加链路追踪相关信息的转发逻辑：


服务网格通过在7层流量中增加符合 B3 trace 规范的 header 来记录调用链信息，因此您需要对业务代码做少量改造，传递这些 header，以便网格可以正确关联入站和出站的 span，形成完整调用链路。这些 header 包括：

- x-request-id 
- x-b3-traceid 
- x-b3-spanid 
- x-b3-parentspanid 
- x-b3-sampled 
- x-b3-flags 
- x-ot-span-context 

更多关于 Envoy-based tracing 的信息，请参见 [Istio Distributed Tracing FAQ](https://istio.io/latest/faq/distributed-tracing/)。

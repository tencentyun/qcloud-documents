腾讯云服务网格（Tencent Cloud Mesh，TCM）集成云监控的能力，在服务网格控制台提供调用追踪查询与分析的能力。您可以查看到请求在网格内的完整调用瀑布图和每层调用的 trace 日志信息，帮助您理解服务的调用依赖，以及做网格内的延迟分析。

调用追踪数据通过 sidecar 收集上报，sidecar 会自动生成 trace span。您需要在业务代码中做少量改造，传递请求上下文，以便 TCM 可以正确关联入站和出站的 span，形成完整调用链路。需要业务传递的 headers 包括：

- ` x-request-id `
- ` x-b3-traceid `
- ` x-b3-spanid `
- ` x-b3-parentspanid `
- ` x-b3-sampled `
- ` x-b3-flags `
- ` x-ot-span-context `

更多关于 Envoy-based tracing 的信息，请参见 [Istio Distributed Tracing FAQ](https://istio.io/latest/faq/distributed-tracing/)。

## 查看调用追踪

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

## 配置调用追踪采样率

调用追踪采样率是 trace 数据的采样比例，sidecar 采集与上报数据消耗资源与带宽和采样率成正相关。通常生产环境下，不需要为所有调用都生成 trace 数据并采集上报，避免过多消耗计算资源与带宽资源，只需要配置一定比例即可。建议开发测试环境可以配置100%采样率，生产环境配置1%采样率。

您可以在网格创建时配置采样率，网格创建后，也可以在网格基本信息页面修改采样率配置。如下图所示：
![](https://main.qcloudimg.com/raw/cd22709601ef09d58b4f696bbe57a4cd.png)
![](https://main.qcloudimg.com/raw/bf192503ca214c01923a3287257d3c3d.png)

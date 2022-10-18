## 操作场景

TSF SDK 对一些常用的消息队列组件、数据库组件等有埋点操作以支持全链路跟踪，但在客户实际场景下可能存在 TSF SDK 无法埋点的场景，例如流量经过 API 网关或客户未接入 TSF 组件时无法持续跟踪请求。

本文将介绍如何通过传递 HTTP header 使外部组件可在 TSF 依赖拓扑图和调用链查询中显示。



- 当前仅以下 SDK 版本及其之后的 SDK 版本支持：1.29.5-Hoxton、1.29.12-Finchley、1.29.2-Greenwich。
- 当前支持在依赖拓扑图中展示特定图标的外部组件包括：API 网关。



## 前提条件

在开始本文的实践前，您需要先了解 TSF 的以下功能

- [调用链快速入门](https://cloud.tencent.com/document/product/649/16622)
- [服务依赖拓扑](https://cloud.tencent.com/document/product/649/15544)
- [调用链查询](https://cloud.tencent.com/document/product/649/13688)



## 操作步骤

#### API 网关（apigw）接入

调用链路为如下几种：

- consumer > apigw > provider，其中 consumer 与 provider 均部署在 TSF 上。TSF 依赖拓扑图将显示三个节点串联的链路，以及展示完整的两跳请求的调用详情。
- 外部请求 > apigw > provider，其中 provider 部署在 TSF 上。TSF 依赖拓扑将显示 apigw 和 provider 两个节点的链路，以及 apigw > provider 一跳请求的调用详情。
- consumer > apigw > msgw，其中 consumer 与 msgw 均部署在 TSF 上，msgw 为微服务网关。TSF 依赖拓扑图将显示三个节点串联的链路，以及展示完整的两跳请求的调用详情。
- 外部请求 > apigw > msgw，其中 msgw 部署在 TSF 上。TSF 依赖拓扑将显示 apigw 和 msgw 两个节点的链路，以及 apigw > msgw 一跳请求的调用详情。



**consumer 侧注入**

consumer 侧需要注入 apigw 的组件类型。因为通过 RestTemplate 或 Feign 调用 apigw，TSF sdk 无法得知下游服务的组件类型。若不注入，在 TSF 依赖拓扑图中，链路将会在 apigw 处中断。

consumer 侧还需要注入 apigw 的服务 ID 作为唯一标志。

```java
TsfTracingContext tsfTracingContext = TsfTracingContextHolder.get();
tsfTracingContext.setClientTag("remoteComponent", "api");
tsfTracingContext.setServerServiceName("service-mygpdlyb");  // 设置为 apigw 的 service id
```



**apigw 注入**（注：该步骤由 apigw 实现）

apigw 需要透传 consumer 传递来的 trace 上下文信息。如果为第一跳可忽略。TSF 调用链功能使用基于 zipkin，因此需要透传如下信息。

|    HTTP Header    | 必选 |                             含义                             |                         示例                         |                             说明                             |
| :---------------: | :--: | :----------------------------------------------------------: | :--------------------------------------------------: | :----------------------------------------------------------: |
|   X-B3-TraceId    |  是  |                调用链 trace id。64 bit 长度。                |                   471a1b50aa4e9852                   |      透传 consumer 的值，请勿修改。若为第一跳，可为空。      |
| X-B3-ParentSpanId |  是  |             调用链 parent span id。64 bit 长度。             |                   471a1b50aa4e9852                   | 64 bit 长度。透传 consumer 的值，请勿修改。若为第一跳，可为空。 |
|    X-B3-SpanId    |  是  |                调用链 span id。64 bit 长度。                 |                   d3cc868d837f1985                   | 64 bit 长度。透传 consumer 的值，请勿修改。若为第一跳，可为空。 |
|   X-B3-Sampled    |  是  |           调用链是否被采样。设置为 1，表示被采样。           |                          1                           |      透传 consumer 的值，请勿修改。若为第一跳，可为空。      |
|        b3         |  否  | 调用链单个 header。格式为b3={TraceId}-{SpanId}-{SamplingState}-{ParentSpanId}。id 均为 64 bit 长度 | 471a1b50aa4e9852-d3cc868d837f1985-1-471a1b50aa4e9852 |  brave 5.3+ 版本支持单个 b3 header。若有该 header，需要透传  |



apigw 接受 consumer 的请求，这一跳的 span 数据需要如下信息。如果为第一跳可忽略。

|          HTTP Header           | 必选 |                             含义                             |               示例                |                             说明                             |
| :----------------------------: | :--: | :----------------------------------------------------------: | :-------------------------------: | :----------------------------------------------------------: |
|     X-Tsf-Server-Timestamp     |  是  | apigw 接受请求以及返回响应的时间戳。格式为 sr-ss，时间精度均为微妙 | 1652358271377000-1652358281000000 | 注意精度为微妙，用单横线连接 server receive 和 server send的时间戳 |
|   X-Tsf-Server-Service-Name    |  是  |    apigw 的服务名。将显示在 TSF 依赖拓扑图和调用链详情中     |         service-mygpdlyb          |                        apigw 服务 ID                         |
| X-Tsf-Server-Service-Interface |  否  |          apigw 的接口名，将显示在 TSF 调用链详情中           |   /apigw-echo-provider/{param}    |                      默认值为 external                       |
|      X-Tsf-Server-Ip-Port      |  否  |               apigw 接受请求机器的 ip 和 port                |          127.0.0.1:8009           |         默认值为部署在 TSF 上的下游服务的 ip 和 port         |
|  X-Tsf-Server-Remote-Ip-Port   |  否  |            apigw 上游节点 consumer 的 ip 和 port             |         172.16.0.9:18083          | 默认值为部署在 TSF 上的下游服务的 HTTP 请求的 remoteAddress  |
|  X-Tsf-Server-Local-Component  |  是  |                       apigw 的节点类型                       |               apigw               |                        必填且唯一取值                        |



apigw 向 provider  msgw 发送请求，这一跳的 span 数据需要如下信息

|          HTTP Header           | 必选 |                         含义                          |             示例             |                     说明                     |
| :----------------------------: | :--: | :---------------------------------------------------: | :--------------------------: | :------------------------------------------: |
|     X-Tsf-Client-Timestamp     |  是  |    apigw 发送请求时间戳。格式为 cs，时间精度为微妙    |       1652358271377000       | 注意精度为微妙，cs 表示 client send 的时间戳 |
|   X-Tsf-Client-Service-Name    |  是  | apigw 的服务名。将显示在 TSF 依赖拓扑图和调用链详情中 |       service-mygpdlyb       |                apigw 服务 ID                 |
| X-Tsf-Client-Service-Interface |  否  |       apigw 的接口名，将显示在 TSF 调用链详情中       | /apigw-echo-provider/{param} |              默认值为 external               |
|      X-Tsf-Client-Ip-Port      |  否  |            apigw 发出请求机器的 ip 和 port            |        127.0.0.1:8009        |                  默认值为空                  |
|  X-Tsf-Client-Local-Component  |  是  |                   apigw 的节点类型                    |            apigw             |                必填且唯一取值                |



#### 外部组件接入

调用链路为如下几种：

- consumer > 任意多跳的外部组件 > provider，其中 consumer 与 provider 均部署在 TSF 上。TSF 依赖拓扑图将显示三个节点串联的链路，以及展示完整的两跳请求的调用详情。
- 外部请求 >任意多跳的外部组件 > provider，其中 provider 部署在 TSF 上。TSF 依赖拓扑将显示外部组件和 provider 两个节点的链路，以及 外部组件 > provider 一跳请求的调用详情。
- consumer > 任意多跳的外部组件 > msgw，其中 consumer 与 msgw 均部署在 TSF 上，msgw 为微服务网关。TSF 依赖拓扑图将显示三个节点串联的链路，以及展示完整的两跳请求的调用详情。
- 外部请求 > 任意多跳的外部组件 -> msgw，其中 msgw 部署在 TSF 上。TSF 依赖拓扑将显示外部组件和 msgw 两个节点的链路，以及外部组件 > msgw 一跳请求的调用详情。



**consumer 侧注入**

consumer 侧需要注入外部组件的组件类型，默认为 ms，表示微服务组件，无须注入。

```java
TsfTracingContext tsfTracingContext = TsfTracingContextHolder.get();
tsfTracingContext.setClientTag("remoteComponent", "ms");
```

consumer 侧需要注入外部组件的微服务名。注入的微服务名需要与后续传递的 HTTP header 中微服务名保持一致。

```java
tsfTracingContext.setServerServiceName("my-service");
```



**外部组件注入**

apigw 需要透传 consumer 传递来的 trace 上下文信息。如果为第一跳，可忽略。TSF 调用链功能使用基于 zipkin，因此需要透传如下信息。

|    HTTP Header    | 必选 |                             含义                             |                         示例                         |                             说明                             |
| :---------------: | :--: | :----------------------------------------------------------: | :--------------------------------------------------: | :----------------------------------------------------------: |
|   X-B3-TraceId    |  是  |                调用链 trace id。64 bit 长度。                |                   471a1b50aa4e9852                   |      透传 consumer 的值，请勿修改。若为第一跳，可为空。      |
| X-B3-ParentSpanId |  是  |             调用链 parent span id。64 bit 长度。             |                   471a1b50aa4e9852                   | 64 bit 长度。透传 consumer 的值，请勿修改。若为第一跳，可为空。 |
|    X-B3-SpanId    |  是  |                调用链 span id。64 bit 长度。                 |                   d3cc868d837f1985                   | 64 bit 长度。透传 consumer 的值，请勿修改。若为第一跳，可为空。 |
|   X-B3-Sampled    |  是  |           调用链是否被采样。设置为 1，表示被采样。           |                          1                           |      透传 consumer 的值，请勿修改。若为第一跳，可为空。      |
|        b3         |  否  | 调用链单个 header。格式为b3={TraceId}-{SpanId}-{SamplingState}-{ParentSpanId}。id 均为 64 bit 长度 | 471a1b50aa4e9852-d3cc868d837f1985-1-471a1b50aa4e9852 |  brave 5.3+ 版本支持单个 b3 header。若有该 header，需要透传  |



外部组件接受 consumer 的请求，这一跳的 span 数据需要如下信息。如果为第一跳可忽略。

|          HTTP Header           | 必选 |                             含义                             |               示例                |                             说明                             |
| :----------------------------: | :--: | :----------------------------------------------------------: | :-------------------------------: | :----------------------------------------------------------: |
|     X-Tsf-Server-Timestamp     |  是  | 外部组件接受请求以及返回响应的时间戳。格式为 sr-ss，时间精度均为微妙 | 1652358271377000-1652358281000000 | 注意精度为微妙，用单横线连接 server receive 和 server send的时间戳 |
|   X-Tsf-Server-Service-Name    |  否  |   外部组件的服务名。将显示在 TSF 依赖拓扑图和调用链详情中    |             external              | 需要与 X-Tsf-Client-Service-Name 保持一致，否则无法在依赖拓扑图中串联。默认值为 external |
| X-Tsf-Server-Service-Interface |  否  |                       外部组件的接口名                       |             external              |                      默认值为 external                       |
|      X-Tsf-Server-Ip-Port      |  否  |                    外部组件的 ip 和 port                     |          127.0.0.1:8009           |         默认值为部署在 TSF 上的下游服务的 ip 和 port         |
|  X-Tsf-Server-Remote-Ip-Port   |  否  |           外部组件上游节点 consumer 的 ip 和 port            |         172.16.0.9:18083          | 默认值为部署在 TSF 上的下游服务的 HTTP 请求的 remoteAddress  |
|  X-Tsf-Server-Local-Component  |  否  |                      外部组件的节点类型                      |                ms                 | 需要与在 consumer 侧注入的节点类型、X-Tsf-Client-Local-Component 保持一致。默认值为 ms |



外部组件向 provider 或 msgw 发送请求，这一跳的 span 数据需要如下信息

|          HTTP Header           | 必选 |                          含义                           |       示例       |                     说明                     |
| :----------------------------: | :--: | :-----------------------------------------------------: | :--------------: | :------------------------------------------: |
|     X-Tsf-Client-Timestamp     |  是  |    外部组件发送请求时间戳。格式为 cs，时间精度为微妙    | 1652358271377000 | 注意精度为微妙，cs 表示 client send 的时间戳 |
|   X-Tsf-Client-Service-Name    |  否  | 外部组件的服务名。将显示在 TSF 依赖拓扑图和调用链详情中 |     external     |              默认值为 external               |
| X-Tsf-Client-Service-Interface |  否  |       外部组件的接口名，将显示在 TSF 调用链详情中       |     external     |              默认值为 external               |
|      X-Tsf-Client-Ip-Port      |  否  |            外部组件发出请求机器的 ip 和 port            |  127.0.0.1:8009  |                  默认值为空                  |
|  X-Tsf-Client-Local-Component  |  否  |                   外部组件的组件类型                    |        ms        |                 默认值为 ms                  |



## 说明与注意

- 注入失败不会影响业务的正常运行

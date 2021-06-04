TSF 原生应用基于开源的 Spring Cloud 应用，无需改造可直接接入TSF，使用 TSF 服务治理和调用链等功能。

## 优势说明

* 无需修改应用代码
* 无需引入额外 SDK（除调用链外）
* 无需额外配置

## 实现原理

应用到注册中心的所有请求如注册、发现，会被代理到我们自己的注册中心从而完成服务的注册和发现。当前的服务治理功能是基于 [TSF Mesh](https://cloud.tencent.com/document/product/649/17928) 来实现的，服务调用会经过 TSF Mesh 的 sidecar，在 sidecar 中实现负载均衡、服务路由等治理功能。

>!服务中的熔断、限流功能可能会 TSF 自身的功能冲突，请确保只开启了一种，否则可能会产生非预期的结果。如果确定要启用 TSF 的治理功能来代替服务自身的，可以参考 [关闭服务熔断和限流规则](https://cloud.tencent.com/document/product/649/54152) 。

## 功能说明

目前仅支持 Spring Cloud，且支持 Eureka/Consul 两种注册中心。后续可能支持更多语言和框架，以及更多注册中心。具体如下：

| spring cloud功能 | 开源实现                                 | 原生应用 | 说明                                                   |
| ---------------- | ---------------------------------------- | -------- | ------------------------------------------------------ |
| 注册发现         | Netflix Eureka Consul Discovery          | 兼容     | -                                                      |
| 负载均衡         | Netflix Ribbon Spring Cloud loadbalancer | 兼容     | -                                                      |
| 服务调用         | Feign RestTemplate                       | 兼容     | 自定义标签，需在 HTTP 请求头添加 tsf-mesh-tag: KEY=VALUE |
| 服务限流         | -                                        | 支持     | 自定义标签，需在 HTTP 请求头添加 tsf-mesh-tag: KEY=VALUE |
| 服务熔断         | hystrix                                  | 支持     |             -                                          |
| 服务鉴权         | -                                        | 支持     | 自定义标签，需在 HTTP 请求头添加 tsf-mesh-tag: KEY=VALUE |
| 配置管理         | Config Server Consul Config              | 支持     | 引入 tsf-sdk                                            |
| 链路追踪         | Spring Cloud Sleuth zipkin               | 兼容     | -                                                      |
| 微服务网关       | Spring Cloud Gateway Netflix Zuul        | 兼容     | -                                                      |

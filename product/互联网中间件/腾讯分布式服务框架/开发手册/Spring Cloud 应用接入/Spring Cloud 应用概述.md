TSF 支持原生 Spring Cloud 微服务框架，开发者只需要添加依赖和修改配置即可使用服务注册、调用链、分布式配置等能力。
以下视频将为您介绍 Spring Cloud 框架及相关原理：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2037-24357?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>


## 兼容性说明
TSF 兼容主流 SDK 版本（Edgware、Finchley、Greenwich），具体可参考 [SDK 版本概述](https://cloud.tencent.com/document/product/649/49320)。Spring Cloud 功能、开源实现及 TSF 兼容性如下表所示：

| <nobr>Spring Cloud 功能</nobr> | 开源实现                            | TSF 兼容性 | 说明                                            |
| ----------------- | ---------------------------------------- |:--------------:| ------------------------------------------ |
| 服务注册与发现  | <li>Netflix Eureka</li><li>Consul</li>  | 基于开源增强| 提供金融级高可用注册中心，无须用户自行搭建|        |
| 负载均衡        | Netflix Ribbon                         | 兼容       | -                                                            |
| 服务调用         |<li>RestTemplate/AsyncRestTemplate</li><li>Feign</li>         | 兼容       | -                                              |
| 调用链            | Spring Cloud Sleuth           | 基于开源增强        | 提供服务依赖拓扑、调用链查询基础功能，同时支持调用链与业务日志联动、调用链支持下游组件等高级特性 |
| 分布式配置     | <li>Spring Cloud Config</li><li>Consul Config</li> | 基于开源增强       | 支持通过控制台管理配置，发布配置和查看配置发布历史           |
| 消息驱动        | Kafka                  | 兼容       | 提供调用链传递到腾讯云消息队列 CMQ、Ckafka、开源 Kafka       |
| 安全              | Spring Cloud Security         | 兼容       | -                                                           |
| 微服务网关    | <li>Spring Cloud Gateway</li><li>NetflixZuul</li> | 兼容 Zuul、Spring Cloud Gateway | -                           |
| 熔断降级       |Spring Cloud Hystrix                   | 自研  |TSF 采用官方推荐的 Resilience4J 作为底层实现，扩展支持实例、API 和服务级别的熔断|



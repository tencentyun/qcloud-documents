TSF 支持原生 Spring Cloud 微服务框架，开发者只需要添加依赖和修改配置即可使用服务注册、调用链、分布式配置等能力。
以下视频将为您介绍 Spring Cloud 框架及相关原理：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2037-24357?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 版本配套关系说明
TSF 目前支持 Spring Cloud Edgware、Spring Cloud Finchley、Spring Cloud Greenwich 三个版本。Spring Cloud 、Spring Boot 及 TSF SDK 版本之间的关系如下表所示。

| Spring Cloud | Spring Boot | 最新 TSF SDK 版本|
| ------------ | ----------- | -----------------------------|
| Edgware      | 1.5.x       | 1.20.0-Edgware-RELEASE |
| Finchley     | 2.0.x       | 1.20.0-Finchley-RELEASE |
| Greenwich     | 2.1.x       | 1.20.0-Greenwich-RELEASE |
 
[SDK 版本更新日志 >>](https://cloud.tencent.com/document/product/649/38983) 

## 兼容性说明
Spring Cloud 功能 、开源实现及 TSF 兼容性如下表所示：
<style>
table th:first-of-type {
	width: 150px;
}
table th:nth-of-type(2) {
	width: 200px;
}
table th:nth-of-type(3) {
	width: 120px;
}
</style>
| Spring Cloud 功能 | 开源实现                            | TSF 兼容性 | 说明                                            |
| ----------------- | ---------------------------------------- |:--------------:| ------------------------------------------ |
| 服务注册与发现  | <li>Netflix Eureka</li><li>Consul</li>  | 兼容 Consul  | 提供高可用注册中心，支持本地缓存          |
| 负载均衡         | Netflix Ribbon                         | 兼容       | -                                                            |
| 服务调用         |<li>RestTemplate</li><li>Feign</li>         | 兼容       | -                                              |
| 调用链            | Spring Cloud Sleuth           | 兼容       | 提供服务依赖拓扑、调用链查询基础功能，同时支持调用链与业务日志联动、调用链支持下游组件等高级特性 |
| 分布式配置     | <li>Spring Cloud Config</li><li>Consul Config</li> | 兼容       | 支持通过控制台管理配置，发布配置和查看配置发布历史           |
| 消息驱动        | Kafka                  | 兼容       | 提供调用链传递到腾讯云消息队列 CMQ、Ckafka、开源 Kafka       |
| 安全              | Spring Cloud Security         | 兼容       | -                                                           |
| 微服务网关    | <li>Spring Cloud Gateway</li><li>NetflixZuul</li> | 兼容 Zuul、Spring Cloud Gateway（近期发布） | -                           |
| 熔断降级       |Spring Cloud Hystrix                   | 兼容       | -                                           |



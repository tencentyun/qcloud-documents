## 简介

TSF 支持原生 Spring Cloud 微服务框架，开发者只需要添加依赖和修改配置即可将应用托管到 TSF 平台上，使用服务注册发现、调用链、服务治理、分布式配置和可观测行等能力，帮助您全面提升应用的稳定性和安全性。

以下视频将为您介绍 Spring Cloud 框架及相关原理：

<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2037-24357?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>


## 兼容性说明

TSF 兼容主流 SDK 版本，包含 Edgware、Finchley 和 Greenwich，各版本对应关系请参见 [版本配套关系说明](#explain)。关于 Spring Cloud 功能、开源实现及 TSF 兼容性如下表所示：

| <nobr>Spring Cloud 功能</nobr> | 开源实现                            | TSF 兼容性 | 说明                                            |
| ----------------- | ---------------------------------------- |:--------------:| ------------------------------------------ |
| 服务注册与发现  | <li>Netflix Eureka</li><li>Consul</li>  | 基于开源增强| 提供金融级高可用注册中心，无须用户自行搭建|
| 负载均衡        | Netflix Ribbon                         | 兼容       | -                                                            |
| 服务调用         |<li>RestTemplate/AsyncRestTemplate</li><li>Feign</li>         | 兼容       | -                                              |
| 调用链            | Spring Cloud Sleuth           | 基于开源增强        | 提供服务依赖拓扑、调用链查询基础功能，同时支持调用链与业务日志联动、调用链支持下游组件等高级特性 |
| 分布式配置     | <li>Spring Cloud Config</li><li>Consul Config</li> | 基于开源增强       | 支持通过控制台管理配置，发布配置和查看配置发布历史           |
| 消息驱动        | Kafka                  | 兼容       | 提供调用链传递到腾讯云消息队列 CMQ、CKafka、开源 Kafka      |
| 安全              | Spring Cloud Security         | 兼容       | -                                                           |
| 微服务网关    | <li>Spring Cloud Gateway</li><li>NetflixZuul</li> | 兼容 Zuul、Spring Cloud Gateway | -                           |
| 熔断降级       |Spring Cloud Hystrix                   | 自研  |TSF 采用官方推荐的 Resilience4J 作为底层实现，扩展支持实例、API 和服务级别的熔断|





[](id:explain)
## 版本配套关系说明

TSF 目前支持 Spring Cloud Edgware、Spring Cloud Finchley、Spring Cloud Greenwich、Spring Cloud Hoxton 四个版本。Spring Cloud 、Spring Boot 及 TSF SDK 版本之间的关系如下表所示。

| Spring Cloud | Spring Boot |
| :----------- | :---------- |
| Hoxton       | 2.3.x       |
| Greenwich    | 2.1.x       |
| Finchley     | 2.0.x       |
| Edgware      | 1.5.x       |

> !
>
> 2020年5月19日起，TSF 主要支持 Greenwich 和 Finchley 版本的功能更新，Edgware 版本主要进行缺陷修复（[社区 Edgware 版本](https://spring.io/blog/2019/05/29/spring-cloud-edgware-sr6-released) 于2019年8月停止更新）。


[](id:SDKexplain)
## SDK 版本使用说明

>?**所有 SDK 版本可支持在 JDK 8、JDK 11（包括 KNOA JDK8，KNOA JDK11 ）环境下运行。**

### 长期维护 SDK 版本

TSF 长期维护 LTS (Long Term Support) 版本，SDK 的第三位版本号会根据缺陷修复递增。详情参见 [SDK 版本更新日志](https://cloud.tencent.com/document/product/649/73926) 。

| SDK 版本号 | 新增特性                                                     |
| ---------- | ------------------------------------------------------------ |
| 1.29.x     | <li>微服务网关增加单元化功能</li><li>微服务网关增加 Dubbo 协议转换功能</li><li>补齐 Spring Cloud Gateway 网关的服务治理能力</li><li>微服务网关支持托管外部 API</li><li>支持云上 Spring Cloud 应用平滑迁移 TSF</li> <li>调用链支持 CMQ、PostgreSQL</li> |
| 1.23.x     | <li>新增 spring cloud gateway 微服务网关，链路追踪和调用监控</li><li>微服务网关路径重写配置和微信小程序登录插件</li> <li>调用链支持 RocketMQ</li> |
| 1.21.x     | <li>支持服务熔断</li><li>支持服务容错</li><li>支持全链路灰度发布</li> |
| 1.18.x     | <li> 支持微服务网关（zuul1 版）SDK，基于此 SDK 二次研发，无缝集成 TSF 平台服务治理能力</li> <li>增加 swagger-ui 依赖包</li> <li>调用链支持 MySQL JDBC、Redis、MongoDB、CMQ、Kafka</li><li>支持全局命名空间</li><li>新增自定义日志配置需要的 Converter 和 Layout 类，支持用户使用自定义 logback\log4j\log4j2 日志配置</li> |
| 1.12.x     | <li>支持服务限流</li><li>支持服务路由</li><li>支持服务鉴权</li><li>支持分布式配置</li><li>支持调用链</li> |



### 公有云 TSF

对于 TSF 公有云的用户，建议使用 TSF LTS 版本。如果您希望使用最新的产品能力，可以使用最新的版本。

### 私有化 TSF

对于 TSF 私有云的用户，SDK 版本号需要和 TSF 平台版本**保持一致**，SDK 的缺陷会在第三位版本号上体现，例如用户使用 TSF 1.12.4 版本，推荐使用的 SDK 版本为 1.12.x。

| TSF 私有化平台版本 | Edgware                | Finchley                 | Greenwich                 | Hoxton                       |
| :----------------- | :--------------------- | :----------------------- | :------------------------ | :--------------------------- |
| 1.29.x             | -                      | 1.29.11-Finchley-RELEASE | 1.29.0-Greenwich-RELEASE  | 1.29.3-Hoxton-Higher-RELEASE |
| 1.23.x             | -                      | 1.23.12-Finchley-RELEASE | 1.23.16-Greenwich-RELEASE | -                            |
| 1.21.x             | -                      | 1.21.12-Finchley-RELEASE | 1.21.4-Greenwich-RELEASE  | -                            |
| 1.18.x             | -                      | 1.18.8-Finchley-RELEASE  | 1.18.1-Greenwich-RELEASE  | -                            |
| 1.12.x             | 1.12.5-Edgware-RELEASE | 1.12.5-Finchley-RELEASE  | -                         | -                            |

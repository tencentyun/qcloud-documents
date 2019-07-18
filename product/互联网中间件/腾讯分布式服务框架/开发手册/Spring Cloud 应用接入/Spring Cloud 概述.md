TSF 支持原生 Spring Cloud 微服务框架，开发者只需要添加依赖和修改配置即可使用服务注册、调用链、分布式配置等能力。



### 版本配套关系说明

TSF 目前支持 Spring Cloud Finchley、Spring Cloud Edgware 两个版本，Spring Cloud Greenwich 版本将于近期推出。Spring Cloud 、Spring Boot 及 TSF SDK 版本之间的关系如下表所示。

| Spring Cloud | Spring Boot | 最新 TSF SDK 版本       |
| ------------ | ----------- | ----------------------- |
| Edgware      | 1.5.x       | 1.14.0-Edgware-RELEASE  |
| Finchley     | 2.0.x       | 1.14.0-Finchley-RELEASE |
| Greenwich    | 2.1.x       | 近期发布                |



### 兼容性说明

Spring Cloud 功能 、开源实现及 TSF 兼容性如下表所示：

| Spring Cloud 功能 | 开源实现                                 | TSF 兼容性 | 说明                                                         |
| ----------------- | ---------------------------------------- | ---------- | ------------------------------------------------------------ |
| 服务注册与发现    | - Netflix Eureka<br>- Consul             | 兼容       | 提供高可用注册中心，支持本地缓存                             |
| 负载均衡          | Netflix Ribbon                           | 兼容       | -                                                            |
| 服务调用          | - RestTempalte <br>- Feign               | 兼容       | -                                                            |
| 调用链            | Spring Cloud Sleuth                      | 兼容       | 提供服务依赖拓扑、调用链查询基础功能，同时支持调用链与业务日志联动、调用链支持下游组件等高级特性 |
| 分布式配置        | - Spring Cloud Config<br>- Consul Config | 兼容       | 支持通过控制台管理配置，发布配置和查看配置发布历史           |
| 消息驱动          | Kafka                                    | 兼容       | 提供调用链传递到腾讯云消息队列 CMQ、Ckafka、开源 Kafka       |
| 安全              | Spring Cloud Security                    | 兼容       | -                                                            |
| 微服务网关        | - Spring Cloud Gateway<br> - NetflixZuul | 兼容       | -                                                            |
| 熔断降级          | - Spring Cloud Hystrix                   | 兼容       | -                                                            |


## 版本配套关系说明
TSF 目前支持 Spring Cloud Edgware、Spring Cloud Finchley、Spring Cloud Greenwich、Spring Cloud Hoxton、Spring Cloud 2020 以及 Spring Cloud 2021。Spring Cloud 、Spring Boot 及 TSF SDK 版本之间的关系如下表所示。

| Spring Cloud | Spring Boot |
| ------------ | ----------- |
| 2021       | 2.7.x       |
| 2020       | 2.5.x      |
| Hoxton     | 2.3.x       |
| Greenwich     | 2.1.x       |
| Finchley     | 2.0.x       |
| Edgware      | 1.5.x       |

>!2020年5月19日起，TSF 主要支持 Greenwich 和 Finchley 以及更新版本的功能迭代更新，Edgware 版本主要进行缺陷修复（[社区 Edgware 版本](https://spring.io/blog/2019/05/29/spring-cloud-edgware-sr6-released) 于2019年8月停止更新）。

### 长期维护 SDK 版本

TSF 长期维护 LTS (Long Term Support) 版本，SDK 的第三位版本号会根据缺陷修复递增。详情参见 [SDK 版本更新日志](https://cloud.tencent.com/document/product/649/73926) 。

|SDK 版本号|新增特性|
|----|----|
|1.40.x|<li>支持微服务网关可扩展性。支持使用 TSF 网关 SDK 的同时，自定义网关路由策略、支持 websocket、支持跨域等原生网关能力</li><li>Oauth 插件支持第三方鉴权地址为微服务 API 的能力</li><li>支持原生网关使用熔断治理的能力</li><li>支持服务监听触发回调</li><li>支持查看下发配置</li> |
|1.29.x|<li>微服务网关增加单元化功能</li><li>微服务网关增加 Alibaba Dubbo 协议转换功能</li><li>补齐 Spring Cloud Gateway 网关的服务治理能力</li><li>微服务网关支持托管外部 API</li><li>支持云上 Spring Cloud 应用平滑迁移 TSF</li> <li>调用链支持 CMQ、PostgreSQL</li> |
|1.23.x|<li>新增 spring cloud gateway 微服务网关，链路追踪和调用监控</li><li>微服务网关路径重写配置和微信小程序登录插件</li> <li>调用链支持 RocketMQ</li> |
|1.21.x|<li>支持服务熔断</li><li>支持服务容错</li><li>支持全链路灰度发布</li>|
|1.18.x|<li> 支持微服务网关（zuul1 版）SDK，基于此 SDK 二次研发，无缝集成 TSF 平台服务治理能力</li> <li>增加 swagger-ui 依赖包</li> <li>调用链支持 MySQL JDBC、Redis、MongoDB、CMQ、Kafka</li><li>支持全局命名空间</li><li>新增自定义日志配置需要的 Converter 和 Layout 类，支持用户使用自定义 logback\log4j\log4j2 日志配置</li>|
|1.12.x|<li>支持服务限流</li><li>支持服务路由</li><li>支持服务鉴权</li><li>支持分布式配置</li><li>支持调用链</li>|

##  SDK 版本使用说明
>?**所有 SDK 版本可支持在 JDK 8、JDK 11、JDK 17（包括 KONA JDK8，KONA JDK11，KONA JDK17）环境下运行。**

### 公有云 TSF

对于 TSF 公有云的用户，建议使用 TSF LTS 版本。如果您希望使用最新的产品能力，可以使用最新的版本。

### 私有化 TSF

对于 TSF 私有云的用户，SDK 版本号需要和 TSF 平台版本**保持一致**，SDK 的缺陷会在第三位版本号上体现，例如用户使用 TSF 1.12.4 版本，推荐使用的 SDK 版本为 1.12.x。

|TSF 私有化平台版本| Edgware|Finchley|Greenwich| Hoxton | 2020 | 2021 |
|----|------|----|------|------|------|------|
|1.40.x|-|1.40.x-Finchley-RELEASE|1.40.x-Greenwich-RELEASE|1.40.x-Hoxton-Higher-RELEASE|1.40.x-SpringCloud2020-RELEASE|1.40.x-SpringCloud2021-RELEASE|
|1.29.x|-|1.29.x-Finchley-RELEASE|1.29.x-Greenwich-RELEASE|1.29.x-Hoxton-Higher-RELEASE|-|-|
|1.23.x|-|1.23.x-Finchley-RELEASE|1.23.x-Greenwich-RELEASE|-|-|-|
|1.21.x|-|1.21.x-Finchley-RELEASE|1.21.x-Greenwich-RELEASE|-|-|-|
|1.18.x|-|1.18.x-Finchley-RELEASE|1.18.x-Greenwich-RELEASE|-|-|-|
|1.12.x|1.12.x-Edgware-RELEASE|1.12.x-Finchley-RELEASE|-|-|-|-|

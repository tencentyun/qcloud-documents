## 公有云 TSF 使用SDK版本

对于 TSF 公有云的用户，建议使用 TSF LTS (Long Term Support) 版本，SDK 的缺陷在第三位版本号上进行修复。

|SDK 版本号|新增特性|
|----|----|
|1.23.x|<li>新增 spring cloud gateway 微服务网关，链路追踪和调用监控</li><li>微服务网关路径重写配置和微信小程序登录插件</li> <li>调用链支持 RocketMQ</li> |
|1.21.x|<li>支持服务熔断</li><li>支持服务容错</li><li>支持全链路灰度发布</li>|
|1.18.x|<li> 支持微服务网关（zuul1 版）SDK，基于此 SDK 二次研发，无缝集成 TSF 平台服务治理能力</li> <li>增加 swagger-ui 依赖包</li> <li>调用链支持MySQL JDBC、Redis、MongoDB、CMQ、Kafka</li><li>支持全局命名空间</li><li>新增自定义日志配置需要的 Converter 和 Layout 类，支持用户使用自定义 logback\log4j\log4j2 日志配置</li>|
|1.12.x|<li>支持服务限流</li><li>支持服务路由</li><li>支持服务鉴权</li><li>支持分布式配置</li><li>支持调用链</li>|


## 私有化 TSF 使用SDK版本

对于 TSF 私有云的用户，SDK 版本号需要和TSF 平台版本保持一致，SDK的缺陷会在第三位版本号上体现，例如用户使用 TSF 1.12.4 版本，推荐的 SDK 版本使用 1.12.x。

|TSF 私有化平台版本| 支持 SDK 版本|
|----|------|
|1.23.x|[1.23.4-Finchley-RELEASE](https://cloud.tencent.com/document/product/649/38984#1.23.4-finchley-release.EF.BC.882020-09-16.EF.BC.89)、[1.23.5-Greenwich-RELEASE](https://cloud.tencent.com/document/product/649/38985#1.23.5-greenwich-release-.EF.BC.882020-09-21.EF.BC.89)|
|1.21.x|[1.21.4-Edgware-RELEASE](https://cloud.tencent.com/document/product/649/38983#1.21.4-edgware-release.EF.BC.882020-08-20.EF.BC.89)、[1.21.4-Finchley-RELEASE](https://cloud.tencent.com/document/product/649/38984#1.21.4-finchley-release.EF.BC.882020-08-20.EF.BC.89)、[1.21.4-Greenwich-RELEASE](https://cloud.tencent.com/document/product/649/38985#1.21.4-greenwich-release-(2020-08-20))|
|1.18.x|[1.18.1-Edgware-RELEASE](https://cloud.tencent.com/document/product/649/38983#1.18.1-edgware-release.EF.BC.882020-01-14.EF.BC.89)、[1.18.1-Finchley-RELEASE](https://cloud.tencent.com/document/product/649/38984#1.18.1-finchley-release.EF.BC.882020-01-14.EF.BC.892)、[1.18.1-Greenwich-RELEASE](https://cloud.tencent.com/document/product/649/38985#1.18.1-greenwich-release.EF.BC.882020-01-14.EF.BC.89)|
|1.12.x|[1.12.5-Edgware-RELEASE](https://cloud.tencent.com/document/product/649/38983#1.12.5-edgware-release.EF.BC.882020-07-17.EF.BC.89)、[1.12.5-Finchley-RELEASE](https://cloud.tencent.com/document/product/649/38984#1.12.5-finchley-release.EF.BC.882020-07-17.EF.BC.892)|


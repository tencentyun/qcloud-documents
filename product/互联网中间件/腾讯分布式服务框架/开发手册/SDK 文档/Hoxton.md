基于 Spring Cloud Hoxton SR9 版本 SDK，支持 spring boot 2.3.1。

## 1.29.2-Hoxton-Higher-RELEASE（2021-10-18）

### 新特性

#### 服务限流（spring-cloud-tsf-rate-limit）

- 支持针对所有请求、单个服务的请求进行流量控制。
- 支持服务下单个 API 请求级别的限流。

#### 服务路由（spring-cloud-tsf-route）

- 支持基于部署组、系统标签、自定义标签的路由设置。
- 支持服务下单个 API 请求级别的路由。
- 支持自动重注册，服务鉴权/路由/限流策略本地缓存。
- 服务路由支持基于可用区和地域就近访问策略。

#### 服务鉴权

支持基于服务名和标签的鉴权设置。

#### 链路跟踪（spring-cloud-tsf-sleuth）

- 支持微服务调用全链路跟踪。
- 支持 MySQL JDBC、Redis、MongoDB、CMQ 组件调用链。
- 支持在调用链上设置标签和自定义 Metada。

#### 分布式配置（spring-cloud-tsf-config）

- 支持分布式配置功能。
- 配置回调。
- 配置加密 spring-cloud-tsf-encrypt。

#### API注册（spring-cloud-tsf-swagger）

- API 注册：支持服务下 API 信息自动注册，查看 API 出入参请求结构。
- 集成 spring-cloud-tsf-swagger 包，支持本地使用 swagger-ui 进行调试。

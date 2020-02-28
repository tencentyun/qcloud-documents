基于 Spring Cloud Greenwich 版本 SDK，支持 spring boot 2.1.6。

### 1.19.0-Greenwich-RELEASE（2020-01-16）

#### 新特性

新增服务熔断、容错功能。

#### 版本建议

支持向后兼容，建议全量升级。

### 1.18.1-Greenwich-RELEASE（2020-01-14）

#### Bug 修复

- spring-cloud-tsf-route 修复路由权重不准的问题。
- spring-cloud-tsf-consul-discovery 修复服务发现线程池上限的问题。

#### 版本建议

支持向后兼容，建议全量升级。


### 1.18.0-Greenwich-RELEASE（2019-12-25）

#### 新特性
- 服务治理支持全局命名空间。
- 新增自定义日志配置需要的 Converter 和 Layout 类，支持用户使用自定义 logback\log4j\log4j2 日志配置。

#### 优化
spring-cloud-tsf-sleuth 优化 TraceStatementProxyHandler JDBC 代理过程内部异常处理逻辑：非代理异常、非 SDK 产生的异常，直接抛出；代理异常或 SDK 产生的异常，直接调用服务不经过调用链逻辑。

#### Bug 修复
- spring-cloud-tsf-sleuth 修复 JdbcDataSourceBeanPostProcessor NPE Bug 问题。
- spring-cloud-tsf-consul-discovery 修复 ConsulProperties 中同时使用 @Value 和  @ConfigurationProperties 方式进行属性注入，先后顺序导致的 Bug 问题。
- spring-cloud-tsf-sleuth 修复监控日志可能出现的 NPE Bug 问题。

#### 版本建议
支持向后兼容，建议全量升级。

### 1.16.1-Greenwich-RELEASE（2019-12-03）

#### Bug 修复
API 注册兼容从环境变量和启动参数中读取 TSF 参数信息。

### 1.16.0-Greenwich-RELEASE（2019-11-05）

#### 新特性

- **服务限流**（spring-cloud-tsf-rate-limit）
	- 支持针对所有请求、单个服务的请求进行流量控制。
	- 支持服务下单个 API 请求级别的限流。

- **服务路由**（spring-cloud-tsf-route）
	- 支持基于部署组、系统标签、自定义标签的路由设置。
	- 支持服务下单个 API 请求级别的路由。
	- 支持自动重注册，服务鉴权/路由/限流策略本地缓存。
	- 服务路由支持基于可用区和地域就近访问策略。

- **服务鉴权**
支持基于服务名和标签的鉴权设置。

- **链路跟踪**（spring-cloud-tsf-sleuth）
	- 支持微服务调用全链路跟踪。
	- 支持 MySQL JDBC、Redis、MongoDB、CMQ 组件调用链。
	- 支持在调用链上设置标签和自定义 Metada。

- **分布式配置**（spring-cloud-tsf-config）
	- 支持分布式配置功能。
	- 配置回调。
	- 配置加密 spring-cloud-tsf-encrypt。

- **API 注册**（spring-cloud-tsf-swagger）
	- API 注册：支持服务下 API 信息自动注册，查看 API 出入参请求结构。
	- 集成 spring-cloud-tsf-swagger 包，支持本地使用 swagger-ui 进行调试。

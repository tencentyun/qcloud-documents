基于 Spring Cloud Edgware 版本 SDK，支持 springboot 1.5.x。


### 1.19.0-Edgware-RELEASE（2020-01-16）

#### 新特性

新增服务熔断、容错功能。

#### 版本建议

支持向后兼容，建议全量升级。

### 1.18.1-Edgware-RELEASE（2020-01-14）

#### Bug 修复
- spring-cloud-tsf-route 修复路由权重不准的问题。
- spring-cloud-tsf-consul-discovery 修复服务发现线程池上限的问题。

#### 版本建议
支持向后兼容，建议全量升级。

### 1.18.0-Edgware-RELEASE（2019-12-25）

#### 新特性
- 服务治理支持全局命名空间。
- 新增 spring-cloud-tsf-gateway 微服务网关（zuul1 版）SDK，基于此 SDK 二次研发，无缝集成 TSF 平台服务治理能力。
- 新增自定义日志配置需要的 Converter 和 Layout 类，支持用户使用自定义 logback\log4j\log4j2 日志配置。

#### 优化
spring-cloud-tsf-sleuth 优化 TraceStatementProxyHandler JDBC 代理过程 SDK 内部异常处理逻辑：非代理异常、非 SDK 产生的异常，直接抛出；代理异常或 SDK 产生的异常，直接调用服务不经过调用链逻辑。

#### Bug 修复
- spring-cloud-tsf-sleuth 修复 JDBC 代理过程 NPE Bug 问题。
- spring-cloud-tsf-route 修复路由系统标签匹配的问题。

#### 版本建议
支持向后兼容，建议全量升级。

### 1.16.1-Edgware-RELEASE（2019-12-03）

#### Bug 修复
API 注册兼容从环境变量和启动参数中读取 TSF 参数信息。


### 1.16.0-Edgware-RELEASE（2019-10-11）

#### 新特性
- Kafka 的链路追踪能力。
- 增加 swagger-ui 依赖包。

#### 优化

- 集成 spring-cloud-tsf-swagger 包后，本地启动无需设置 tsf.swagger.enabled=false。
- 集成 spring-cloud-tsf-swagger 包后，支持本地使用 swagger-ui 进行调试。

#### Bug 修复

- 修复在自定义 RedisTemplate 中指定序列化方式时的错误。
- 修复对 StringRedisTemplate 的支持。
- 修复引入 swagger 包后，低版本 guava 包引起冲突。
- 配置回调功能空指针异常。

#### 版本建议

支持向后兼容，建议全量升级。


### 1.14.2-Edgware-RELEASE（2019-09-10）

#### Bug 修复

- 限流 Bug fix。
- TsfContext.putTag覆盖 Bug fix。

#### 版本建议

支持向后兼容，建议全量升级。



### 1.14.1-Edgware-RELEASE（2019-07-24）

#### Bug 修复

- 修复 TSF SDK 依赖的 scheduler 和业务自身的 scheduler 相互影响的问题。
- 修复 spring-cloud-tsf-ratelimit 包限流不准确问题。
- 修复 spring-cloud-tsf-sleuth 包数据源和 Mybatis 兼容性问题。

#### 版本建议

支持向后兼容，建议全量升级。


### 1.14.0-Edgware-RELEASE（2019-06-21）

#### 新特性

支持 MySQL JDBC、Redis、MongoDB、CMQ 组件调用链。	

#### 版本建议

支持向后兼容，建议全量升级。



### 1.12.4-Edgware-RELEASE（2019-08-15）

#### Bug 修复

- 修复 TSF SDK 依赖的 scheduler 和业务自身的 scheduler 相互影响的问题。
- 修复 spring-cloud-tsf-ratelimit 包限流不准确问题。

#### 版本建议

支持向后兼容，建议全量升级。



### 1.12.2-Edgware-RELEASE（2019-04-22）

#### Bug 修复

修复 Edgware 版本自定义 tag 问题。

#### 版本建议

支持向后兼容，建议全量升级。



### 1.12.1-Edgware-RELEASE（2019-03-25）

#### Bug 修复

修复配置回调功能未生效问题。

#### 版本建议

支持向后兼容，建议全量升级。



### 1.12.0-Edgware-RELEASE（2019-03-13）

#### 新特性

- 支持自动重注册，服务鉴权/路由/限流策略本地缓存。
- 服务路由支持基于可用区和地域就近访问策略。

#### 优化

- 升级分布式配置监听，精确并减小监听范围，处理更新为空的场景，避免大范围 key 刷新事件。
- 优化分部署配置回调触发逻辑。

#### Bug 修复

- spring-cloud-commons 升级到1.3.1解决 RetryTemplate 会导致 LoadBalanceInterceptor thread unsafe 问题。
- 修复启用 hystrix 时配置会导致 tsf-route 与 feignbuilder 冲突的问题。

#### 版本建议

支持向后兼容，建议全量升级。



### 1.10.0-RELEASE（2018-11-12）

#### 新特性

- 服务路由（srping-cloud-tsf-route）：支持服务下单个 API 请求级别的路由。
- 服务限流（spring-cloud-tsf-ratelimite）：支持服务下单个 API 请求级别的限流。
- 日志输出（spring-cloud-tsf-logger）：支持默认日志输出。
- API 注册（spring-cloud-tsf-swagger）：支持服务下 API 信息自动注册，查看 API 出入参请求结构。

#### Bug 修复

解决 RestTemplate Bean 冲突问题。

#### 升级建议

- 支持向后兼容。
- 新功能建议全量升级。



### 1.1.1-RELEASE（2018-08-26）

#### 新特性

- 服务限流 （spring-cloud-tsf-rate-limit） ：支持针对所有请求、单个服务的请求进行流量控制。
- 服务路由（spring-cloud-tsf-route）：支持基于部署组、系统标签、自定义标签的路由设置。
- 服务鉴权 （spring-cloud-tsf-auth）：支持基于服务名和标签的鉴权设置。
- 配置加密 （spring-cloud-tsf-encrypt）：支持配置加密功能。
- 应用状况监控（spring-cloud-tsf-metrics）：支持查看 Spring Boot 应用的 JVM 内存分布、线程、HTTP Traces、环境变量。
- 调用链 （spring-cloud-tsf-sleuth）：支持在调用链上设置标签和自定义 Metada。

#### Bug 修复

 调用链 SDK 问题修复。

#### 升级建议

全部建议升级。

# Spring Cloud TSF Edgware

基于 Spring Cloud Edgware 版本 SDK，支持 springboot 1.5.x。

## 1.22.0-Edgware-RELEASE（2020-04-29）

### 优化

- 优化默认日志配置支持容器部署场景
- 优化TSF MSGW zuul依赖

### 版本建议

- 支持向后兼容，建议全量升级。

## 1.21.1-Edgware-RELEASE (2020-04-29)

### bug fix

- 修复泳道ID在非泳道起始应用中传递丢失的问题

### 优化

- 优化调用链生成文件名称的生成规则
- 任务调度组件优化任务生成器逻辑, 兼容BeanName和BeanType方式获取工厂

### 版本建议

- 支持向后兼容，建议全量升级。

## 1.21.0-Edgware-RELEASE（2020-04-17）

### 新特性

- 全链路灰度发布
- 增加熔断状态变更事件上报

### bug fix

- spring-cloud-tsf-swagger 修复@ApiParam注解Example属性解析异常问题。
- 修复Tag在AsyncRestTemplate下不传递的问题
- 修复Feign无法使用绝对URL请求的问题
- spring-cloud-tsf-gateway: 
  - 修复Tag标签插件未在调用中透传的问题
  - 修复当绑定网关插件后造成Query参数未透传的问题

### 优化

- 支持swagger自动扫描包多路径特性。

## 1.20.0-Edgware-RELEASE（2020-03-02）

### 新特性

- 新增`分布式任务调度`功能

### bug fix

- spring-cloud-tsf-gateway 修复tag plugin中header类型取值大小写敏感的问题。
- 处理tomcat组件开源漏洞风险。
  - 升级org.apache.tomcat.embed.tomcat-embed-core到8.5.51版本。
  - 升级org.apache.tomcat.embed.tomcat-embed-el到8.5.51版本。
  - 升级org.apache.tomcat.embed.tomcat-embed-websocket到8.5.51版本。
  - 升级org.apache.tomcat.tomcat-annotations-api到8.5.51版本。
- 修复application/x-www-form-urlencoded类型请求，通过zuul网关代理访问provider时，服务端不到请求参数的问题。  

### 优化

- spring-cloud-tsf-gateway  新增tag plugin中path类型取值。

### 版本建议

- 支持向后兼容，建议全量升级。

## 1.19.0-Edgware-RELEASE（2020-01-16）

### 新特性

- 新增`服务熔断`功能

### 版本建议

- 支持向后兼容，建议全量升级。

## 1.18.1-Edgware-RELEASE（2020-01-14）

### bug fix

- spring-cloud-tsf-route 修复路由权重不准的问题
- spring-cloud-tsf-consul-discovery 修复服务发现线程池上限的问题。
- spring-cloud-tsf-sleuth 修复druid连接池事务兼容问题
- spring-cloud-tsf-sleuth 修复同时依赖多个数据库连接池问题
- spring-cloud-tsf-core 修复Custom Metadata设置接口不兼容

### 优化

- 支持通过 `tsf.discovery.watch.enabled` 关闭服务发现时的 watch 监听

### 版本建议

- 支持向后兼容，建议全量升级。

## 1.18.0-Edgware-RELEASE（2019-12-25）

### bug fix

- spring-cloud-tsf-sleuth 修复JDBC代理过程NPE bug问题。
- spring-cloud-tsf-route 修复路由系统标签匹配的问题。

### 新特性

- 服务治理支持全局命名空间。
- 新增spring-cloud-tsf-gateway微服务网关(zuul1版)SDK, 基于此SDK二次研发，无缝集成TSF平台服务治理能力。
- 新增自定义日志配置需要的Converter和Layout类，支持用户使用自定义logback\log4j\log4j2日志配置。

### 优化

- spring-cloud-tsf-sleuth 优化TraceStatementProxyHandler JDBC代理过程SDK内部异常处理逻辑: 非代理异常、非SDK产生的异常，直接抛出; 代理异常或SDK产生的异常，直接调用服务不经过调用链逻辑。

### 版本建议

- 支持向后兼容，建议全量升级。

## 1.16.3-Edgware-RELEASE (2020-04-29) 

### 优化

- 优化调用链生成文件名称的生成规则

## 1.16.2-Edgware-RELEASE (2020-03-02) 

### bug fix

- spring-cloud-tsf-sleuth bug fixed:
  - 修复application/x-www-form-urlencoded类型请求，通过zuul网关代理访问provider时，服务端不到请求参数的问题。
  - 处理Custom Metadata设置接口不兼容。
  - 调用链输出用户自定义Tag和Metadata。
  - 修复druid连接池事务兼容问题。
  - 修复同时依赖多个数据库连接池问题。

## 1.16.1-Edgware-RELEASE（2019-12-3）

### bug fix

- API注册兼容从环境变量和启动参数中读取TSF参数信息.

## 1.16.0-Edgware-RELEASE（2019-10-11）

### 新特性

- kafka的链路追踪能力。
- 增加 swagger-ui依赖包

### 优化

- 集成spring-cloud-tsf-swagger包后, 本地启动无需设置tsf.swagger.enabled=false。
- 集成spring-cloud-tsf-swagger包后, 支持本地使用swagger-ui进行调试。

### Bug 修复

- 修复在自定义RedisTemplate中指定序列化方式时的错误。
- 修复对StringRedisTemplate的支持。
- 修复引入swagger包后, 低版本guava包引起冲突。
- 配置回调功能空指针异常。

### 版本建议

- 支持向后兼容，建议全量升级。

## 1.14.2-Edgware-RELEASE（2019-09-10）

### Bug 修复

- 限流Bug fix。
- TsfContext.putTag覆盖bug fix。

### 版本建议

- 支持向后兼容，建议全量升级。

### 1.14.1-Edgware-RELEASE（2019-07-24）

### Bug 修复

- 修复tsf sdk依赖的scheduler和业务自身的scheduler相互影响的问题
- 修复spring-cloud-tsf-ratelimit包限流不准确问题
- 修复 spring-cloud-tsf-sleuth 包数据源和Mybatis兼容性问题

### 版本建议

- 支持向后兼容，建议全量升级。

## 1.14.0-Edgware-RELEASE（2019-06-21）

### 新特性

- 支持 MySQL JDBC、Redis、MongoDB、CMQ 组件调用链。	

### 版本建议

- 支持向后兼容，建议全量升级。
  
## 1.12.4-Edgware-RELEASE（2019-08-15）

### Bug 修复

- 修复tsf sdk依赖的scheduler和业务自身的scheduler相互影响的问题
- 修复spring-cloud-tsf-ratelimit包限流不准确问题

### 版本建议

- 支持向后兼容，建议全量升级。

## 1.12.2-Edgware-RELEASE（2019-04-22）

### Bug 修复

- 修复 Edgware 版本自定义 tag 问题。

### 版本建议

- 支持向后兼容，建议全量升级。

## 1.12.1-Edgware-RELEASE（2019-03-25）

### Bug 修复

- 修复配置回调功能未生效问题。

### 版本建议

- 支持向后兼容，建议全量升级。

## 1.12.0-Edgware-RELEASE（2019-03-13）

### 新特性

- 支持自动重注册，服务鉴权/路由/限流策略本地缓存。
- 服务路由支持基于可用区和地域就近访问策略。

### 优化

- 升级分布式配置监听，精确并减小监听范围，处理更新为空的场景，避免大范围 key 刷新事件。
- 优化分部署配置回调触发逻辑。

### Bug 修复

- spring-cloud-commons 升级到1.3.1解决 RetryTemplate 会导致 LoadBalanceInterceptor thread unsafe 问题。
- 修复启用 hystrix 时配置会导致 tsf-route 与 feignbuilder 冲突的问题。

### 版本建议

- 支持向后兼容，建议全量升级。

## 1.10.0-RELEASE（2018-11-12）

### 新特性

- 服务路由（srping-cloud-tsf-route）：支持服务下单个 API 请求级别的路由。
- 服务限流（spring-cloud-tsf-ratelimite）：支持服务下单个 API 请求级别的限流。
- 日志输出（spring-cloud-tsf-logger）：支持默认日志输出。
- API 注册（spring-cloud-tsf-swagger）：支持服务下 API 信息自动注册，查看 API 出入参请求结构。

### Bug 修复

- 解决 RestTemplate Bean 冲突问题。

### 升级建议

- 支持向后兼容。
- 新功能建议全量升级。

## 1.1.1-RELEASE（2018-08-26）

### 新特性

- 服务限流 （spring-cloud-tsf-rate-limit） ：支持针对所有请求、单个服务的请求进行流量控制。
- 服务路由（spring-cloud-tsf-route）：支持基于部署组、系统标签、自定义标签的路由设置。
- 服务鉴权 （spring-cloud-tsf-auth）：支持基于服务名和标签的鉴权设置。
- 配置加密 （spring-cloud-tsf-encrypt）：支持配置加密功能。
- 应用状况监控（spring-cloud-tsf-metrics）：支持查看 Spring Boot 应用的 JVM 内存分布、线程、HTTP Traces、环境变量。
- 调用链 （spring-cloud-tsf-sleuth）：支持在调用链上设置标签和自定义 Metada。

### Bug 修复

- 调用链 SDK 问题修复。

### 升级建议

- 全部建议升级
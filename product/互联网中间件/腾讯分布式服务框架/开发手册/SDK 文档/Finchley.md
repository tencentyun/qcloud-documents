基于 Spring Cloud Finchley 版本 SDK，支持 spring boot 2.0.x。

## 1.22.1-Finchley-RELEASE（2020-05-06）

### 优化

优化 TSF MSGW scg 使用，用户无需显示配置全局路由。

### 版本建议

支持向后兼容，建议全量升级。

## 1.22.0-Finchley-RELEASE（2020-04-29）

### 新特性

- 支持 SpringCloud Gateway 链路追踪和调用监控。
- TSF MSGW scg 版本发布。

### Bug 修复

- 修复在使用 redis，自定义多个 LettuceConnectionFactory 时，不能链路追踪所有请求的问题。
- 修复调用监控禁用场景内存泄露问题。

### 优化

- 优化默认日志配置支持容器部署场景。
- 优化 TSF MSGW zuul 依赖。

## 1.21.1-Finchley-RELEASE（2020-04-29）

### Bug 修复

- 修复泳道 ID 在非泳道起始应用中传递丢失的问题。
- 修复调用链生成文件名称问题。

### 优化

任务调度组件优化任务生成器逻辑，兼容 BeanName和BeanType 方式获取工厂。

## 1.21.0-Finchley-RELEASE (2020-04-17)

### 新特性
- 全链路灰度发布。
- 增加熔断状态变更事件上报。

### Bug 修复

- 修复 Feign 无法使用绝对 URL 请求的问题。
- spring-cloud-tsf-swagger 修复 @ApiParam 注解 Example 属性解析异常问题。
- spring-cloud-tsf-gateway：
   - 修复 Tag 标签插件未在调用中透传问题。
   - 修复当绑定网关插件后造成 Query 参数未透传问题。

### 优化

支持 swagger 自动扫描包多路径特性。

## 1.20.0-Finchley-RELEASE（2020-03-02）

### 新特性

新增`分布式任务调度`功能。

### Bug 修复

- spring-cloud-tsf-gateway 修复 tag plugin中header 类型取值大小写敏感的问题。
- 处理 tomcat 组件开源漏洞风险。
  - 升级 org.apache.tomcat.embed.tomcat-embed-core 到8.5.51版本。
  - 升级 org.apache.tomcat.embed.tomcat-embed-el 到8.5.51版本。
  - 升级 org.apache.tomcat.embed.tomcat-embed-websocket 到8.5.51版本。

### 优化

spring-cloud-tsf-gateway  新增 tag plugin 中 path 类型取值。

### 版本建议

支持向后兼容，建议全量升级。

## 1.19.0-Finchley-RELEASE（2020-01-16）

### 新特性

新增`服务熔断`功能。

### 版本建议

支持向后兼容，建议全量升级。

## 1.18.1-Finchley-RELEASE（2020-01-14）

### Bug 修复

- spring-cloud-tsf-route 修复路由权重不准的问题。
- spring-cloud-tsf-consul-discovery 修复服务发现线程池上限的问题。
- spring-cloud-tsf-sleuth 修复 druid 连接池事务兼容问题。
- spring-cloud-tsf-sleuth 修复同时依赖多个数据库连接池问题。
- spring-cloud-tsf-core 修复 Custom Metadata 设置接口不兼容。

### 优化

支持通过 `tsf.discovery.watch.enabled` 关闭服务发现时的 watch 监听。

### 版本建议

支持向后兼容，建议全量升级。

## 1.18.0-Finchley-RELEASE（2019-12-25）

### Bug 修复

- spring-cloud-tsf-sleuth 修复 JDBC 代理过程 NPE bug 问题。
- spring-cloud-tsf-consul-discovery 修复 ConsulProperties 中同时使用 @Value 和  @ConfigurationProperties 方式进行属性注入，先后顺序导致的 bug 问题。
- spring-cloud-tsf-sleuth 修复监控日志可能出现的 NPE bug 问题。
- spring-cloud-tsf-core 修复 ContextConfiguration Bean 初始化依赖顺序问题。


### 新特性

- 服务治理支持全局命名空间。
- 新增 spring-cloud-tsf-gateway 微服务网关（zuul1 版）SDK，基于此 SDK 二次研发，无缝集成 TSF 平台服务治理能力。
- 新增自定义日志配置需要的 Converter 和 Layout 类，支持用户使用自定义 logback\log4j\log4j2 日志配置。

### 优化

spring-cloud-tsf-sleuth 优化 TraceStatementProxyHandler  JDBC 代理过程 SDK 内部异常处理逻辑：非代理异常、非 SDK 产生的异常，直接抛出；代理异常或 SDK 产生的异常，直接调用服务不经过调用链逻辑。

### 版本建议

支持向后兼容，建议全量升级。

## 1.16.2-Finchley-RELEASE (2020-03-02)

### Bug 修复

spring-cloud-tsf-sleuth bug fixed：
  - 处理 Custom Metadata 设置接口不兼容。
  - 调用链输出用户自定义 Tag和Metadata。
  - 修复 druid 连接池事务兼容问题。
  - 修复同时依赖多个数据库连接池问题。
 
## 1.16.1-Finchley-RELEASE（2019-12-3）

### Bug 修复

- 增加使用 jedis 作为 redis 客户端的调用链追踪功能。
- 修复因为 kafka 生产者、消费者使用 sdk 版本不匹配导致的错误。
- API 注册兼容从环境变量和启动参数中读取 TSF 参数信息。

## 1.16.0-Finchley-RELEASE（2019-10-11）

### 新特性

- kafka 的链路追踪能力。
- 增加 swagger-ui 依赖包。

### 优化

- 集成 spring-cloud-tsf-swagger包后，本地启动无需设置 tsf.swagger.enabled=false。
- 集成 spring-cloud-tsf-swagger包后，支持本地使用 swagger-ui 进行调试。

### Bug 修复

- 修复 DEBUG 日志级别启动时，spring-cloud-tsf-sleuth 包空指针异常。
- 修复引入 swagger 包后，低版本 guava 包引起冲突。
- 配置回调功能空指针异常。

### 版本建议

支持向后兼容，建议全量升级。

## 1.14.3-Finchley-RELEASE（2019-09-10）

### Bug 修复

- 限流 Bug fix。
- TsfContext.putTag 覆盖 bug fix。

### 版本建议

支持向后兼容，建议全量升级。

### 1.14.2-Finchley-RELEASE（2019-08-14）

### Bug 修复

- 修复使用 RedisConnectionFactory 获取 Redis 连接，这种方式使用时的一个类型转化错误。
- 修复在给 span.tag(key,value) 传入 value 时没判空抛出异常的问题。

### 版本建议

支持向后兼容，建议全量升级。

## 1.14.1-Finchley-RELEASE（2019-07-24）

### Bug 修复

- 修复 tsf sdk 依赖的 scheduler 和业务自身的 scheduler 相互影响的问题
- 修复 spring-cloud-tsf-route 包路由不生效的问题
- 修复 spring-cloud-tsf-ratelimit 包限流不准确问题
- 修复 spring-cloud-tsf-sleuth 包数据源和 Mybatis 兼容性问题

### 版本建议

支持向后兼容，建议全量升级。

## 1.14.0-Finchley-RELEASE（2019-06-21）

### 新特性

支持 MySQL JDBC、Redis、MongoDB、CMQ 组件调用链。	

### 版本建议

支持向后兼容，建议全量升级。

## 1.12.4-Finchley-RELEASE（2019-08-15）

### Bug 修复

- 修复 tsf sdk 依赖的 scheduler 和业务自身的 scheduler 相互影响的问题。
- 修复 spring-cloud-tsf-route 包路由不生效的问题。
- 修复 spring-cloud-tsf-ratelimit 包限流不准确问题。

### 版本建议

支持向后兼容，建议全量升级。

### 1.12.3-Finchley-RELEASE（2019-05-17）

### Bug 修复

修复 Finchley 版本服务调用监控问题。

### 版本建议

支持向后兼容，建议全量升级。

## 1.12.2-Finchley-RELEASE（2019-04-22）

### Bug 修复

- 修复 Finchley 版本 TSF Route 启动问题。
- 修复 Finchley 版本 Feign HttpClient 调用链问题。

### 版本建议

支持向后兼容，建议全量升级。

## 1.12.1-Finchley-RELEASE（2019-03-25）

### Bug 修复

修复配置回调功能未生效问题。

### 版本建议

支持向后兼容，建议全量升级。

## 1.12.0-Finchley-RELEASE（2019-03-13）

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

支持向后兼容，建议全量升级。

基于 Spring Cloud Greenwich 版本 SDK，支持 spring boot 2.1.6。


## 1.29.0-Greenwich-RELEASE（2021-06-23）
### 新特性
- 微服务网关增加单元化功能。
- spring-cloud-tsf-sleuth: 新增 cmq-tcp-client 和 cmq-http-client 调用支持。

### 优化
- 优化和开源 spring cloud consul 依赖的冲突。
- actuator 依赖改为 optional。
- spring-cloud-tsf-sleuth：优化 getProperties 性能。
- spring-cloud-tsf-sleuth：监控数据添加 http method 和 path template。
- spring-cloud-tsf-ratelimit：优化限流的 httpclient。
  
### Bug 修复
- spring-cloud-tsf-logger：修复自定义日志格式没有服务名的问题。
- spring-cloud-tsf-sleuth：修复调用链获取 IP 偶现获取不到问题。
- spring-cloud-tsf-sleuth：修改 scg metrics duration 异常问题。
- spring-cloud-tsf-sleuth：修复未发布分组时，网关没法作为组件显示成蓝色 logo 的 Bug。
- spring-cloud-tsf-swagger：修复 IgnoreGatewayApi 注解导致的潜在空指针异常。
- spring-cloud-tsf-consul-discovery：修复被调方实例不存在时不断打印异常日志的问题。
- 修复 Feign 在指定 URL 的模式下无法请求的问题。

### 版本建议
支持向后兼容，建议全量升级。

## 1.26.2-Greenwich-RELEASE（2021-04-25）
### 优化
支持通过配置 `-Dspring.cloud.consul.enabled=false` 关闭连接 consul ，适配单元测试场景时的启动。

### 版本建议
支持向后兼容，建议全量升级。

## 1.26.1-Greenwich-RELEASE（2020-12-31）
### 优化
spring-cloud-tsf-sleuth 新增 CMQ 调用支持。

### 版本建议
支持向后兼容，建议全量升级。


## 1.26.0-Greenwich-RELEASE（2020-12-07）

### 新特性
- spring-cloud-tsf-msgw-scg：
  - 补齐 Spring Cloud Gateway 网关的服务治理能力，支持用户按照需求灵活选择 Zuul 或 Spring Cloud Gateway。
  - 支持托管外部 API。
- spring-cloud-tsf-msgw-zuul：支持托管外部 API。
- spring-cloud-tsf-swagger：支持添加注解 @IgnoreGatewayApi 来忽略某个网关 API 不被发现（忽略该网关的 API，但服务治理 API 不受影响）。

### 版本建议

支持向后兼容，建议全量升级。

## 1.25.0-Greenwich-RELEASE（2020-12-04）

### 新特性
spring-cloud-tsf-msgw-zuul 支持服务熔断能力。

### Bug 修复

- spring-cloud-tsf-ratelimit：修复多个限流规则时，全局限流无法关闭的问题。
- spring-cloud-tsf-route：修复当只有一个路由规则时，路由规则关闭不生效的问题。
- spring-cloud-tsf-lane：修复泳道规则内存可见性 Bug。

### 版本建议

支持向后兼容，建议全量升级。

## 1.24.0-Greenwich-RELEASE（2020-09-25）

### 新特性
- 支持云上 Spring Cloud 应用平滑迁移 TSF。
- 支持 PostgreSQL 组件调用链。

### Bug 修复

- spring-cloud-tsf-consul-config：
  - 修复本地加密配置不能正确解密的问题。
  - 修复 MySQL 调用链对多数据源支持。
- spring-cloud-tsf-core：
  增加线程上下文接口，在父亲线程中塞入线程局部变量后，子线程不论是线程池反复使用还是一次性使用都能正确继承父线程局部变量。
  
### 版本建议

支持向后兼容，建议全量升级。

## 1.23.14-Greenwich-RELEASE（2021-09-05）

### Bug 修复
- 修复 for 循环调用导致泳道 HTTP Header 过大的问题。

### 优化
- 优化 TSF 加密判断逻辑，只有配置了 TSF 密钥才对 ENC 配置进行解析。
- 优化服务发现相关日志的日志级别。
- 优化和开源 spring cloud consul 依赖的冲突。

### 版本建议

支持向后兼容，建议全量升级。

## 1.23.12-Greenwich-RELEASE（2021-08-16）

### Bug 修复
修复泳道规则排序问题。

### 优化
- 优化服务监听触发回调。
- 优化限流的 httpclient。
- 支持关闭 consul 的启动，以支持单元测试场景。
- 优化熔断模块不必要的日志输出
- 优化零实例保护优化引起的，服务发现实例为空时的 warn 提示。
- 优化 TSF 加密判断逻辑，只有配置了 TSF 密钥才对 ENC 配置进行解析。

### 版本建议

支持向后兼容，建议全量升级。

## 1.23.9-Greenwich-RELEASE（2021-06-11）
### 新特性
- 支持服务监听触发回调。

### 优化
- 服务发现增加零实例保护。
- consul 异常时，避免一直刷日志。

### 版本建议
支持向后兼容，建议全量升级。

## 1.23.8-Greenwich-RELEASE（2021-02-07）

### Bug 修复
修复 msgw-scg 依赖 actuator 缺失导致启动失败的问题。

### 优化
- spring-cloud-tsf-fault-tolerance 和 spring-cloud-tsf-circuitbreaker 对 zuul 的依赖改为 optional。
- spring-cloud-tsf-route 对 actuator 依赖改为 optional。

### 版本建议

支持向后兼容，建议全量升级。

## 1.23.7-Greenwich-RELEASE（2021-01-25）

### Bug 修复
- 修复服务治理时 API PATH 标签匹配 PATH 参数失败问题。
- 修复当存在多个限流规则的时候，全局限流规则开启后，无法删除的问题。
- 修复泳道规则内存可见性 Bug。
- 修复路由关闭问题。
- 修复分布式配置下发 spring.application.name 时，无法上报 swagger 问题。
- 修复本地加密配置不能被正确解密的问题。 
- 修复网关多个命名空间时 consul index 混用导致第一次跨命名空间调用加载慢的问题。
- 修复 Spring Framework 反射型文件下载漏洞。
- 解决和 spring-boot-devtools 的冲突。

### 优化
- actuator 依赖改为 optional。
- TTL 单独超时时间，并增加重试。
- 优化 spring-cloud-tsf-sleuth 的 getProperties 性能。

### 版本建议

支持向后兼容，建议全量升级。

## 1.23.6-Greenwich-RELEASE（2020-11-11）
### 优化
- spring-cloud-tsf-msgw-zuul 支持服务熔断能力。
- spring-cloud-tsf-sleuth 修改调用 SQL 存储的最长长度到64000字符。

### 版本建议

支持向后兼容，建议全量升级。

## 1.23.5-Greenwich-RELEASE（2020-09-21）

### 优化
调整泳道入口行为。

### 版本建议

支持向后兼容，建议全量升级。

## 1.23.4-Greenwich-RELEASE（2020-09-16）

### Bug 修复

- 修复 MySQL 调用链中对多数据源支持。
- 修复 feign 请求调用链中只展示 HTTP 方法。
- 修复定时任务的线程数问题。
- 修复网关使用就近命名空间的问题。
    

### 版本建议

支持向后兼容，建议全量升级。

## 1.23.3-Greenwich-RELEASE（2020-09-14）

### Bug 修复

- spring-cloud-tsf-msgw：
修复网关 MSGW SDK 和服务发现 SDK 不兼容，造成拉取服务列表过快的问题，从而导致注册中心负载压力过大的问题。
- spring-cloud-tsf-consul-discovery：
修复服务发现线程数不准确（少于需要请求的服务数），导致服务发现线程调度不及时，节点状态更新可能会延迟30s的问题。
  
## 1.23.2-Greenwich-RELEASE（2020-08-19）

### Bug 修复

spring-cloud-tsf-msgw-zuul：
  - 修复无法在 filter 中使用 Feign 发起微服务调用的问题。
  - 修复 application/x-www-form-urlencoded 类型请求，当绑定插件通过 zuul 网关代理访问时错误问题。

### 版本建议

支持向后兼容，建议全量升级。

## 1.23.1-Greenwich-RELEASE（2020-08-12）

### Bug 修复

spring-cloud-tsf-msgw：
修复 scg 版本网关不支持 HTTP 请求中文编码的问题。

### 版本建议

支持向后兼容，建议全量升级。

## 1.23.0-Greenwich-RELEASE（2020-07-06）

### 新特性

- spring-cloud-tsf-msgw：
  - 新增网关路径重写配置功能。
  - 新增网关微信小程序登录插件功能。 
- spring-cloud-tsf-sleuth：新增调用链支持 RocketMQ。
- spring-cloud-tsf-core：
  - 监控数据结构中增加 HTTP 请求方法、以及请求模版路径。
  - 调用链数据结构中增加 HTTP 请求方法。

### Bug 修复

- spring-cloud-tsf-msgw：
  - 修复数据同步时，可能会短暂获取到错误数据的问题。
  - 修复 SCG Tag 中数据未正确清除的问题。
- 处理 tomcat 组件开源漏洞风险：
  - 升级 org.apache.tomcat.embed.tomcat-embed-core 到9.0.36版本。
  - 升级 org.apache.tomcat.embed.tomcat-embed-el 到9.0.36版本。
  - 升级 org.apache.tomcat.embed.tomcat-embed-websocket 到9.0.36版本。
- spring-cloud-tsf-sleuth：修复 Kafka 中的类型转发错误。
  
  

## 1.22.1-Greenwich-RELEASE（2020-05-06）

### 优化

优化 TSF MSGW scg 使用，用户无需显示配置全局路由。

### 版本建议

支持向后兼容，建议全量升级。

## 1.22.0-Greenwich-RELEASE（2020-04-29）

### 新特性

- 支持 SpringCloud Gateway 链路追踪和调用监控。
- TSF MSGW scg 版本发布。
- TSF MSGW zuul1 版本发布。

### Bug 修复

- 修复在使用 redis，自定义多个 LettuceConnectionFactory 时，不能链路追踪所有请求的问题。
- 修复调用监控禁用场景内存泄露问题。
- 修复 Spring Cloud Gateway 无法使用 TSF 服务注册和发现的问题。

### 优化

优化默认日志配置支持容器部署场景。

## 1.21.4-Greenwich-RELEASE (2020-08-20)
### bug 修复
- 处理 MySQL 中 SQL 获取截断的问题。
- 修复 MySQL 调用链中对多数据源支持。

## 1.21.3-Greenwich-RELEASE（2020-07-16）
### Bug 修复
修复 MySQL 中 SQL 获取截断的问题。

## 1.21.2-Greenwich-RELEASE（2020-07-06）

### Bug 修复
处理 tomcat 组件开源漏洞风险：
  - 升级 org.apache.tomcat.embed.tomcat-embed-core 到9.0.36版本。
  - 升级 org.apache.tomcat.embed.tomcat-embed-el 到9.0.36版本。
  - 升级 org.apache.tomcat.embed.tomcat-embed-websocket 到9.0.36版本。

### 优化
- 调整泳道标签的传递属性
- 调整泳道入口行为

## 1.21.1-Greenwich-RELEASE（2020-04-29）

### Bug 修复

修复泳道 ID 在非泳道起始应用中传递丢失的问题。

### 优化

- 修复调用链生成文件名称问题。
- 任务调度组件优化任务生成器逻辑，兼容 BeanName 和 BeanType 方式获取工厂。

## 1.21.0-Greenwich-RELEASE（2020-04-17）

### 新特性

- 全链路灰度发布。
- 增加熔断状态变更事件上报。

### Bug 修复

- 修复 Feign 无法使用绝对 URL 请求的问题
- 修复 spring-cloud-tsf-swagger 包中 @ApiParam 注解 Example 属性解析异常问题。

### 优化

支持 swagger 自动扫描包多路径特性。

## 1.20.0-Greenwich-RELEASE（2020-03-02）

### 新特性

- 新增`分布式任务调度`功能。
- spring-cloud-tsf-sleuth 支持`kafka`和`rocketmq`链路追踪功能。

### Bug 修复

处理 tomcat 组件开源漏洞风险。
  - 升级 org.apache.tomcat.embed.tomcat-embed-core 到9.0.31版本。
  - 升级 org.apache.tomcat.embed.tomcat-embed-el 到9.0.31版本。
  - 升级 org.apache.tomcat.embed.tomcat-embed-websocket 到9.0.31版本。

## 1.19.0-Greenwich-RELEASE（2020-01-16）

### 新特性

新增`服务熔断`功能。

### 版本建议

支持向后兼容，建议全量升级。

## 1.18.1-Greenwich-RELEASE（2020-01-14）

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

## 1.18.0-Greenwich-RELEASE（2019-12-25）

### Bug 修复

- spring-cloud-tsf-sleuth 修复 JdbcDataSourceBeanPostProcessor NPE bug 问题。
- spring-cloud-tsf-consul-discovery 修复 ConsulProperties 中同时使用 @Value 和  @ConfigurationProperties 方式进行属性注入，先后顺序导致的 bug 问题。
- spring-cloud-tsf-sleuth 修复监控日志可能出现的 NPE bug 问题。

### 新特性

- 服务治理支持全局命名空间。
- 新增自定义日志配置需要的 Converter 和 Layout 类，支持用户使用自定义 logback\log4j\log4j2 日志配置。

### 优化

spring-cloud-tsf-sleuth 优化 TraceStatementProxyHandler  JDBC 代理过程内部异常处理逻辑：非代理异常、非 SDK 产生的异常，直接抛出；代理异常或 SDK 产生的异常，直接调用服务不经过调用链逻辑。

### 版本建议

支持向后兼容，建议全量升级。

## 1.16.2-Greenwich-RELEASE（2020-03-02）

### Bug 修复

- spring-cloud-tsf-sleuth bug fixed：
  - 处理 Custom Metadata 设置接口不兼容。
  - 调用链输出用户自定义 Tag 和 Metadata。
  - 修复druid连接池事务兼容问题。
  - 修复同时依赖多个数据库连接池问题。

## 1.16.1-Greenwich-RELEASE（2019-12-3）

### Bug 修复

API 注册兼容从环境变量和启动参数中读取 TSF 参数信息。

## 1.16.0-Greenwich-RELEASE（2019-11-5）

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

基于 Spring Cloud Finchley 版本 SDK，支持 spring boot 2.0.x。

## 1.32.0-Finchley-RELEASE（2020-06-21）
### 新特性
- 支持微服务网关可扩展性。支持使用 TSF 网关 SDK 的同时，自定义网关路由策略、支持 websocket、支持跨域等原生网关能力。
- Oauth 插件支持第三方鉴权地址为微服务 API 的能力。
- 支持原生网关使用熔断治理的能力。
- 支持服务监听触发回调。

### 优化
- consul 异常时，避免一直刷日志。
- 增加 tsf launcher。 
  
### Bug 修复
- 修复 Feign 在指定 URL 的模式下无法请求的问题。
- 修改scg metrics duration异常问题

### 版本建议
支持向后兼容，建议全量升级。

## 1.29.4-Finchley-RELEASE（2021-10-18）
### 优化
- 支持通过 -Dtsf.discovery.zeroInstanceProtect=false 关闭零实例保护。
- 优化 TSF 加密判断逻辑，只有配置了 TSF 密钥才对 ENC 配置进行解析。
  
### Bug 修复
- 修复 for 循环调用导致泳道 HTTP Header过大的问题。
- 修复服务发现时无本地缓存文件导致延迟。

### 版本建议
支持向后兼容，建议全量升级。

## 1.29.2-Finchley-RELEASE（2021-08-16）
### 优化
- 增加 catalog 内存 cache 的优化。
- 优化熔断模块不必要的日志输出。
- 优化去除 TSF日志配置后，使用 log4j2 时出现 `${sys:LOG_FILE}` 的情况。
- 统一第三方组件的版本号。
  
### Bug 修复
- 修复 Feign 在指定 URL 的模式下无法请求的问题。
- 修复日志组件 log4j 和 log4j2 输出调用链数据问题。
- 修复 sleuth 模块 debug 日志打印异常。
- 修复 scg metrics duration 异常问题。

### 版本建议
支持向后兼容，建议全量升级。

## 1.29.0-Finchley-RELEASE（2020-05-07）
### 新特性
- 微服务网关增加单元化功能。
- 微服务网关增加 Dubbo 协议转换功能。
- spring-cloud-tsf-sleuth: 新增 cmq-tcp-client 和 cmq-http-client 调用支持。

### 优化
- 优化和开源 spring cloud consul 依赖的冲突。
- 支持通过配置 -Dspring.cloud.consul.enabled=false 关闭连接 consul，适配单元测试场景时的启动。
- actuator 依赖改为 optional。
- spring-cloud-tsf-sleuth：优化 getProperties 性能。
- spring-cloud-tsf-ratelimit：优化限流的 httpclient。
  
### Bug 修复
- spring-cloud-tsf-logger：修复自定义日志格式没有服务名的问题。
- spring-cloud-tsf-sleuth：修复调用链获取 IP 偶现获取不到问题。
- spring-cloud-tsf-swagger：修复 IgnoreGatewayApi 注解导致的潜在空指针异常。
- spring-cloud-tsf-consul-discovery：修复被调方实例不存在时不断打印异常日志的问题。

### 版本建议
支持向后兼容，建议全量升级。


## 1.23.11-Finchley-RELEASE（2021-09-28）
### Bug 修复
- 修复sdk 调用链数据 输出 log4j组件重复初始化导致写入多个文件的问题

### 优化
- 优化零实例保护优化引起的，服务发现实例为空时的 warn 提示
- 优化 TSF 加密判断逻辑，只有配置了 TSF 密钥才对 ENC 配置进行解析
- 增加 catalog 内存 cache 的优化
- consul 异常时，避免一直刷日志。

### 版本建议
支持向后兼容，建议全量升级。

## 1.23.10-Finchley-RELEASE（2021-08-16）
### Bug 修复
修复 for 循环调用导致泳道 HTTP Header过大的问题。

### 优化
优化限流的 httpclient。

### 版本建议
支持向后兼容，建议全量升级。

## 1.23.9-Finchley-RELEASE（2021-06-23）
### Bug 修复
修改 scg metrics duration 异常问题。

### 优化
- 服务发现增加零实例保护。
- consul 异常时，避免一直刷日志。

### 版本建议
支持向后兼容，建议全量升级。

## 1.23.8-Finchley-RELEASE（2021-04-13）
### 优化
网关支持适配特殊 url。例如：用户请求 url 是 `/echo`、`/echo/`、`/echo\` 时，网关统一会当 `/echo` 处理。

### 版本建议
支持向后兼容，建议全量升级。

## 1.23.7-Finchley-RELEASE（2021-02-02）
### Bug 修复
- 修复服务治理时 API PATH 标签匹配 PATH 参数失败问题。
- 修复本地启动时监听原生 consul 路径的问题。

### 优化
统一第三方组件的版本号。

### 版本建议
支持向后兼容，建议全量升级。

## 1.23.6-Finchley-RELEASE（2020-12-21）
### Bug 修复
- 处理 Spring 组件开源漏洞风险，升级 Spring Framework 到5.0.19版本。
- spring-cloud-tsf-core 修复与 spring-boot-devtools 的冲突。
- spring-cloud-tsf-ratelimit：修复当只有一个限流规则时，限流规则关闭不生效的问题。
- spring-cloud-tsf-route：修复当只有一个路由规则时，路由规则关闭不生效的问题。
- spring-cloud-tsf-swagger 修复通过分布式配置下发 spring.application.name 时，API 上报失败的问题。
- 修复网关多个命名空间时 consul index 混用问题。

### 优化
- spring-cloud-tsf-consul-discovery 心跳请求增加重试。
- spring-cloud-tsf-consul-config 支持本地加密配置解析。
- spring-cloud-tsf-lane：优化泳道规则生效逻辑。

### 版本建议
支持向后兼容，建议全量升级。

## 1.23.5-Finchley-RELEASE（2020-11-11）
### 优化
- spring-cloud-tsf-msgw-zuul 支持服务熔断能力。
- spring-cloud-tsf-sleuth 修改调用 SQL 存储的最长长度到64000字符。
- 调整泳道入口行为。

### 版本建议

支持向后兼容，建议全量升级。

## 1.23.4-Finchley-RELEASE（2020-09-16）

### Bug 修复

- 修复 MySQL 调用链中对多数据源支持。
- 修复 feign 请求调用链中只展示 HTTP 方法。
- 修复定时任务的线程数问题。
- 修复网关使用就近命名空间的问题。
    
### 版本建议

支持向后兼容，建议全量升级。

## 1.23.3-Finchley-RELEASE（2020-09-14）

### Bug 修复

- spring-cloud-tsf-msgw：
修复网关 MSGW SDK 和服务发现 SDK 不兼容，造成拉取服务列表过快的问题，从而导致注册中心负载压力过大的问题。
- spring-cloud-tsf-consul-discovery：
修复服务发现线程数不准确（少于需要请求的服务数），导致服务发现线程调度不及时，节点状态更新可能会延迟30s的问题。
    

### 版本建议

支持向后兼容，建议全量升级。

## 1.23.2-Finchley-RELEASE（2020-08-19）

### Bug 修复

spring-cloud-tsf-msgw：
修复 application/x-www-form-urlencoded 类型请求，当绑定插件通过 zuul 网关代理访问时出错的问题。

### 版本建议

支持向后兼容，建议全量升级。

## 1.23.1-Finchley-RELEASE（2020-08-12）

### Bug 修复

spring-cloud-tsf-msgw：
 修复 scg 版本网关不支持 HTTP 请求中文编码的问题。

### 版本建议

支持向后兼容，建议全量升级。

## 1.23.0-Finchley-RELEASE（2020-07-06）

### 新特性
- spring-cloud-tsf-msgw：
  - 新增网关路径重写配置功能。
  - 新增网关微信小程序登录插件功能。
- spring-cloud-tsf-sleuth：
  - 新增调用链支持 RocketMQ。
  - 修复 Kafka 中的类型转发错误。
- spring-cloud-tsf-core：
  - 监控数据结构中增加 HTTP 请求方法、以及请求模版路径。
  - 调用链数据结构中增加 HTTP 请求方法。

### Bug 修复

- spring-cloud-tsf-msgw：
  - 修复数据同步时，可能会短暂获取到错误数据的问题。
  - 修复 SCG Tag 中数据未正确清除的问题。
- 处理 tomcat 组件开源漏洞风险：
  - 升级 org.apache.tomcat.embed.tomcat-embed-core 到8.5.56版本。
  - 升级 org.apache.tomcat.embed.tomcat-embed-el 到8.5.56版本。
  - 升级 org.apache.tomcat.embed.tomcat-embed-websocket 到8.5.56版本。

## 1.21.12-Finchley-RELEASE（2021-07-15）
### 新特性
- 新增对 CMQ TCP SDK 的支持。
- 新增对 CMQ 异步接收方法的调用链支持。

### Bug 修复
- 修复 SDK 调用链数据输出 log4j 组件重复初始化导致写入多个文件的问题。
- spring-cloud-tsf-logger：修复自定义日志格式没有服务名的问题。

## 1.21.9-Finchley-RELEASE（2021-02-02）
### Bug 修复
- 修复服务治理时 API PATH 标签匹配 PATH 参数失败问题。
- 修复本地启动时监听原生 consul 路径的问题。

### 优化
统一第三方组件的版本号。

### 版本建议
支持向后兼容，建议全量升级。

## 1.21.8-Finchley-RELEASE（2020-12-31）
### Bug 修复
spring-cloud-tsf-sleuth：修复特殊场景调用链 IP 获取失败问题。

### 版本建议
支持向后兼容，建议全量升级。

## 1.21.7-Finchley-RELEASE（2020-12-21）
### Bug 修复
- spring-cloud-tsf-ratelimit：修复当只有一个限流规则时，限流规则关闭不生效的问题。
- spring-cloud-tsf-route：修复当只有一个路由规则时，路由规则关闭不生效的问题。
- spring-cloud-tsf-swagger 修复通过分布式配置下发 spring.application.name 时，API 上报失败的问题。
- 修复网关多个命名空间时 consul index 混用问题。

### 优化
- spring-cloud-tsf-sleuth 新增 CMQ 调用支持。
- spring-cloud-tsf-consul-discovery 心跳请求增加重试。
- spring-cloud-tsf-consul-config 支持本地加密配置解析。
- spring-cloud-tsf-lane：优化泳道规则生效逻辑。

### 版本建议
支持向后兼容，建议全量升级。

## 1.21.6-Finchley-RELEASE（2020-10-19）
### Bug 修复
- 处理 Spring 组件开源漏洞风险，升级 Spring Framework 到 5.0.19 版本。
- spring-cloud-tsf-core 修复与 spring-boot-devtools 的冲突。

### 优化
- spring-cloud-tsf-gateway 支持服务熔断能力。
- spring-cloud-tsf-sleuth 修改调用 SQL 存储的最长长度到64000字符。

### 版本建议
支持向后兼容，建议全量升级。

## 1.21.5-Finchley-RELEASE（2020-09-09）
### 优化
spring-cloud-tsf-gateway 优化因配置被误删除可能导致的问题。

### 版本建议
支持向后兼容，建议全量升级。

## 1.21.4-Finchley-RELEASE（2020-08-20）
### Bug 修复
- 修复 MySQL 调用链支持多数据源问题。
- 修复 feign 请求调用链只展示 HTTP 方法。
- spring-cloud-tsf-msgw：
 修复 application/x-www-form-urlencoded 类型请求，当绑定插件通过 zuul 网关代理访问时出错的问题。

### 版本建议
支持向后兼容，建议全量升级。

## 1.21.3-Finchley-RELEASE（2020-07-16）
### Bug 修复
- 修复网关 MSGW SDK 和服务发现 SDK 不兼容，造成拉取服务列表过快的问题。
- 修复 MySQL 调用链中 SQL 截断问题。

### 优化
spring-cloud-tsf-gateway 网关兼容新插件类型。

## 1.21.2-Finchley-RELEASE（2020-07-06）

### Bug 修复

处理 tomcat 组件开源漏洞风险：
  - 升级 org.apache.tomcat.embed.tomcat-embed-core到 8.5.56版本。
  - 升级 org.apache.tomcat.embed.tomcat-embed-el 到8.5.56版本。
  - 升级 org.apache.tomcat.embed.tomcat-embed-websocket 到8.5.56版本。

### 优化

- 调整泳道标签的传递属性
- 调整泳道入口行为

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



## 1.18.5-Finchley-RELEASE（2020-10-27）
### Bug 修复
- 修复 druid 连接池事务兼容问题。
- 修复同时依赖多个数据库连接池问题。
- 修复调用链生成文件名称问题。
- 修复服务发现线程数不准确问题。
- 修复 Feign 无法使用绝对 URL 请求的问题。

### 版本建议
支持向后兼容，建议全量升级。

## 1.18.4-Finchley-RELEASE（2020-10-20）
### 优化
spring-cloud-tsf-sleuth 修改调用 SQL 存储的最长长度到64000字符。

### 版本建议
支持向后兼容，建议全量升级。

## 1.18.3-Finchley-RELEASE（2020-10-13）

### Bug 修复

- 处理 Spring 组件开源漏洞风险，升级 Spring Framework 到5.0.19版本。
- spring-cloud-tsf-core 修复与 spring-boot-devtools 的冲突。

### 版本建议

支持向后兼容，建议全量升级。

## 1.18.2-Finchley-RELEASE（2020-08-21）

### Bug 修复

- spring-cloud-tsf-route 修复网关使用就近命名空间的问题。
- spring-cloud-tsf-consul-discovery 修复服务发现线程池上限的问题。
- spring-cloud-tsf-sleuth 修复 MySQL 调用链支持多数据源问题。
- spring-cloud-tsf-gateway 修复网关 MSGW SDK 和服务发现 SDK 不兼容，造成拉取服务列表过快的问题。
- spring-cloud-tsf-gateway 兼容低版本 MSGW SDK。

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

## 1.12.6-Finchley-RELEASE（2021-03-25）

### Bug 修复
- 处理 Spring 组件开源漏洞风险，升级 Spring Framework 到5.0.19版本。
- spring-cloud-tsf-core 修复与 spring-boot-devtools 的冲突。
- spring-cloud-tsf-ratelimit：修复多个限流规则时，全局限流无法关闭的问题。

### 优化
- spring-cloud-tsf-consul-discovery 心跳请求增加重试。
- spring-cloud-tsf-consul-config 支持本地加密配置解析。
- spring-cloud-tsf-swagger 支持多路径扫码。

### 版本建议

支持向后兼容，建议全量升级。

## 1.12.5-Finchley-RELEASE（2020-07-17）

### Bug 修复

修复 spring-cloud-tsf-route 包路由不准确问题。

### 优化

调整心跳请求的超时时间，当出现丢包时能够快速重试。

### 版本建议

支持向后兼容，建议全量升级。
## 1.12.4-Finchley-RELEASE（2019-08-15）

### Bug 修复

- 修复 tsf sdk 依赖的 scheduler 和业务自身的 scheduler 相互影响的问题。
- 修复 spring-cloud-tsf-route 包路由不生效的问题。
- 修复 spring-cloud-tsf-ratelimit 包限流不准确问题。

### 版本建议

支持向后兼容，建议全量升级。

## 1.12.3-Finchley-RELEASE（2019-05-17）

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

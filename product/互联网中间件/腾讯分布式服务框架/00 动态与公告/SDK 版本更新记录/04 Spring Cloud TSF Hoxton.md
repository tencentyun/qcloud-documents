基于 Spring Cloud Hoxton SR9 版本 SDK，支持 spring boot 2.3.1。


## 1.40.1-Hoxton-Higher-RELEASE（2022-10-21）
### 新特性
- 支持微服务网关可扩展性。支持使用 TSF 网关 SDK 的同时，自定义网关路由策略、支持 websocket、支持跨域等原生网关能力。
- Oauth 插件支持第三方鉴权地址为微服务 API 的能力。
- 支持原生网关使用熔断治理的能力。
- 支持服务监听触发回调。
- 支持查看下发配置。

### Bug 修复
- postgresql jdbc driver 版本升级至 42.3.7
- 修复出现组件自身的调用问题
- 修复指标avg合并计算错误

## 1.29.13-Hoxton-Higher-RELEASE（2022-11-02）

### Bug 修复
- 修复 scg 调用在 filter 中增加 restTemplate 或 feign 以后，scg 最终调用目标下游服务的熔断功能失效的问题。
- 修复 TSF Consul 与开源 Consul 双注册双发现的问题。
- 修复 swagger 上报因为报文不完整出现空指针的问题。

### 优化
- 支持调用链中展示 oceanbase 监控。

## 1.29.11-Hoxton-Higher-RELEASE（2022-09-08）

### Bug 修复
- 修复 controller 的 scope 是其他类型的，上报 API 报错的问题。
- 修复调用链 scg resultStatus 获取的问题。
- 修复实例级熔断 half open 再次进入 open 时的隔离问题。

### 优化
- 支持 HTTP 请求的 IP 鉴权。
- 优化零实例保护节点的判断。


## 1.29.9-Hoxton-Higher-RELEASE（2022-07-21）

### Bug 修复
修复 RocketMQ 调用链 npe 问题。

## 1.29.8-Hoxton-Higher-RELEASE（2022-07-15）

### 优化
scg 兼容 ribbon 的 WeightedResponseTimeRule 策略。

## 1.29.7-Hoxton-Higher-RELEASE（2022-07-06）

### 优化
TracingFeignClient 支持 resttemplate 的传递。

### Bug 修复
- 调用链修复 jdbc postgresql Multi-Hosts 解析失败的问题。
- 修复 invocation AggregatedStat 数据合并的问题。
- 修复潜在的重复 bean 问题。
- 修复潜在的监控数据 http method 异常的问题。
- MySQL 调用链兼容 ShardingConnection。

## 1.29.5-Hoxton-Higher-RELEASE（2022-06-07）

### 优化
- 自定义负载均衡策略支持。
- 升级 logback、tomcat、guava、jackson 等第三方依赖的版本。
- 优化 swagger 的依赖冲突，并升级到 springfox 2.10.5。

### Bug 修复
- 修复不配置 logging.file 且无日志配置文件(log*.xml)时，导致 logging.level 无效。
- 修复异常时，网关tag未设置的问题。
- 修复路由、鉴权、限流的 api path 标签的匹配。
- 修复实例熔断超过阈值时，对应实例的熔断事件依旧上报的问题。
- 修复熔断规则变化时，后续熔断事件没有上报的问题。
- 修复网关使用 log4j2 时提示 Log4J2TraceConverter 重复的问题。


## 1.29.4-Hoxton-Higher-RELEASE（2022-05-06）

### 优化
- 兼容 mysql-connector-java 5.x。
- 优化 log4j2 默认日志文件位置。
- 优化服务发现对于零实例的判断。
- zuul 默认关闭 hystrix。
- 调用链支持 Kafka 批量消费消息场景。
- 支持网关自动预热加载服务。
- 支持普通应用预热加载。

### bug 修复
- 修复泳道规则排序问题。
- 修复调用链 MongoDB 异常时 resultStatus 为空的问题。
- 修复 zuul 重试参数配置不生效。
- 修复 consul actuator 因为不兼容而导致 down。
- 修复处理 feign 和 resttemplate 调用链丢失 remote 信息 包括 ip port interface。


## 1.29.3-Hoxton-Higher-RELEASE（2021-11-26）
### 优化
- 优化 swagger 依赖。

### Bug 修复
- 修复 kafka 调用链 span 异常。
- 修复 kafka 调用链丢失 parentId 的问题。
- 修复 rocketmq 调用链显示内部异常的问题。

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

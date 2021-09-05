基于 Spring Cloud Edgware 版本 SDK，支持 Spring Boot 1.5.x。

>!2020年5月19日起，TSF 主要支持 Greenwich 和 Finchley 版本的功能更新，Edgware 版本主要进行缺陷修复，建议您优先使用 Finchley和 Greenwich 版本（[社区 Edgware 版本](https://spring.io/blog/2019/05/29/spring-cloud-edgware-sr6-released) 于2019年8月停止更新）。


## 1.12.5-Edgware-RELEASE（2020-07-17）

### Bug 修复

修复 spring-cloud-tsf-route 包路由不准确问题。

### 优化

调整心跳请求的超时时间，当出现丢包时能够快速重试。

### 版本建议

支持向后兼容，建议全量升级。

## 1.12.4-Edgware-RELEASE（2019-08-15）

### Bug 修复

- 修复 tsf sdk 依赖的 scheduler 和业务自身的 scheduler 相互影响的问题。
- 修复 spring-cloud-tsf-ratelimit 包限流不准确问题。

### 版本建议

支持向后兼容，建议全量升级。

## 1.12.2-Edgware-RELEASE（2019-04-22）

### Bug 修复

修复 Edgware 版本自定义 tag 问题。

### 版本建议

支持向后兼容，建议全量升级。

## 1.12.1-Edgware-RELEASE（2019-03-25）

### Bug 修复

修复配置回调功能未生效问题。

### 版本建议

支持向后兼容，建议全量升级。

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

支持向后兼容，建议全量升级。

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

调用链 SDK 问题修复。

### 升级建议

全部建议升级。

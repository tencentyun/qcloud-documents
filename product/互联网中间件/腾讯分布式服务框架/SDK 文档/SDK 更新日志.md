## 1.10.0 - RELEASE（2018-11-12）

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

## 1.1.1 - RELEASE（2018-08-26）

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

- 全部建议升级。

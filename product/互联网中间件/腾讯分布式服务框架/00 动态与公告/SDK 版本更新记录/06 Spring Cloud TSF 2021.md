基于 Spring Cloud 2021 版本 SDK，支持 spring boot 2.7.5。

<dx-alert infotype="notice" title="">
Spring Cloud 2021 SDK 的调用链、监控功能需使用 OpenTelemetry Agent，具体使用方式参考  [Spring Cloud 2020 & 2021 SDK 使用说明](https://cloud.tencent.com/document/product/649/81429) 文档。
</dx-alert>

## 1.40.0-SpringCloud2021-RELEASE（2023-01-06）
### 新特性
- 支持 TSF 网关使用 kona fiber 协程来提升性能。
- 支持同时使用 TSF 网关和开源原生网关的能力。支持自定义网关路由策略、支持 websocket 以及支持跨域等原生网关能力。
- 支持 Oauth 插件使用第三方鉴权地址为微服务 API 的能力。
- 支持开源原生网关使用 TSF 服务治理的能力。
- 支持服务监听触发回调。
- 支持查看下发配置。
- 支持使用 OpenTelemetry Agent 来使用 TSF 监控调用链的能力。

### 优化
- 补齐 1.40.x 之前的版本支持的能力。
- 在限流时把限流id设置到调用链。
- 熔断，限流事件适配支持多服务名。
- 优化 Swagger 上报的依赖 Springfox 兼容适配 Spring Cloud TSF 2021。

### Bug 修复
- 修复非单元化场景下，网关监控信息异常的问题。

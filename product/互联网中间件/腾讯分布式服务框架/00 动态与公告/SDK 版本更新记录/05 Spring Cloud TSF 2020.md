基于 Spring Cloud 2020 版本 SDK，支持 spring boot 2.5.14（TSF SDK 1.40.7-SpringCloud2020-RELEASE 及其之后的版本）和 spring boot 2.4.3（TSF SDK 1.40.7-SpringCloud2020-RELEASE 之前的版本），推荐使用 2.5.14 版本。

<dx-alert infotype="notice" title="">
Spring Cloud 2020 SDK 的调用链、监控功能需使用 OpenTelemetry Agent，具体使用方式参考  [Spring Cloud 2020 & 2021 SDK 使用说明](https://cloud.tencent.com/document/product/649/81429) 文档。
</dx-alert>


## 1.40.7-SpringCloud2020-RELEASE（2023-01-10）
### 优化
- 升级 protobuf-java 版本为 3.19.6。
- 升级 spring boot 版本为 2.5.14。

## 1.40.6-SpringCloud2020-RELEASE（2022-12-22）
### 优化
- 网关 kona fiber 协程改用反射方式来获取。
- 熔断，限流事件适配支持多服务名。

### Bug 修复
- 继续修复 metadata decode 的问题。
- 修复非单元化场景下，网关监控信息异常的问题。
- 修复网关请求出现空指针异常的问题。

## 1.40.5-SpringCloud2020-RELEASE（2022-11-11）
### 优化
- 修改泳道日志信息。

### Bug 修复
- 修复swagger上报因为报文不完整出现空指针的问题。
- 修改泳道日志信息。
- 修复网关 header 头重复写入的问题。
- 修复网关的 realPath 被覆盖的问题。

## 1.40.4-SpringCloud2020-RELEASE（2022-11-03）
### 优化
- 优化 Metadata 序列化时 url decode 的问题。

## 1.40.3-SpringCloud2020-RELEASE（2022-10-27）
### 优化
- 优化缓存文件名。

## 1.40.2-SpringCloud2020-RELEASE（2022-10-27）
### Bug 修复
- 修复网关开源原生模式下获取 API 超时时间的空指针异常。

## 1.40.1-SpringCloud2020-RELEASE（2022-10-25）
### 优化
- 去除无用的泳道日志信息。

## 1.40.0-SpringCloud2020-RELEASE（2022-08-30）
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

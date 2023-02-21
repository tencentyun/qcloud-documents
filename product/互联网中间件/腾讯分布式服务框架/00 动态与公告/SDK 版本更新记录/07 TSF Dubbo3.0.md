支持 dubbo3.0.x。

>! dubbo3 应用接入方法参考 [Dubbo3 接入 TSF](https://cloud.tencent.com/document/product/649/84542) 文档。


## 1.0.7-RELEASE（2023-01-10）
>! 适配的 spring-cloud-tsf-dependencies 为 1.40.7-SpringCloud2020-RELEASE、1.40.0-SpringCloud2021-RELEASE

### Bug 修复
- 修复结合 spring-cloud-tsf-starter 一起使用时，dubbo 服务也上报 rest api 的问题


## 1.0.6-RELEASE（2022-12-22）
>! 适配的 spring-cloud-tsf-dependencies 为 1.40.6-SpringCloud2020-RELEASE
### 新特性

#### 服务限流

- 支持针对所有请求、单个服务的请求进行流量控制。
- 支持服务下单个 API 请求级别的限流。

#### 服务路由

- 支持基于部署组、系统标签、自定义标签的路由设置。
- 支持服务下单个 API 请求级别的路由。
- 支持自动重注册，服务鉴权/路由/限流策略本地缓存。
- 服务路由支持基于可用区和地域就近访问策略。

#### 服务鉴权

支持基于服务名和标签的鉴权设置。

#### 链路跟踪

- 支持微服务调用全链路跟踪。
- 支持 MySQL JDBC、Redis、MongoDB、CMQ 组件调用链。
- 支持在调用链上设置标签和自定义 Metada。

#### 全链路灰度发布

支持基于标签的全链路灰度发布

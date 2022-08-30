## Ingress 是什么？
Ingress 是从 Kubernetes 集群外部访问集群内部服务的入口，同时为集群内的Service提供七层负载均衡能力。您可以在Ingress配置可供外部访问URL、负载均衡等。通过Ingress资源配置不同的转发规则，实现根据不同规则访问集群内不同的Service所对应的后端Pod。Ingress controller 负责实现 Ingress，集群中必须有一个正在运行的 Ingress Controller。Nginx Ingress Controller 是最常见的一种Ingress Controller类型。
<img src="https://qcloudimg.tencent-cloud.cn/raw/63b95b38cf3edf01ee633abd648c4b88.png">

## TSE Nginx Ingress Controller
- Nginx 可以用作反向代理、负载平衡器和 HTTP 缓存。
- Nginx Ingress 是使用 Nginx 作为反向代理和负载平衡器的 Kubernetes 的 Ingress Controller。
TSE 云原生网关是腾讯云基于开源网关推出的一款高性能高可用的云上网关产品，减少用户自建网关的开发及运维成本。作为云上微服务架构的流量入口，集成请求分发、API 管理、流量监控、访问限制等功能，是微服务架构中的重要组件。
TSE 云原生网关提供了产品化的 Nginx Ingress 能力，帮助您一键安装和使用Nginx Ingress。提供全方面、多视角的日志、监控体系。

## 工作原理
TSE 云原生网关提供的 Nginx Ingress Controller组件与 Nginx 部署在 TSE 独立的 K8s 集群中，由 TSE 维护组件生命周期管理，支持原生对接到您的后端K8s集群，并且支持跨集群流量路由，如下图所示：
TSE 云原生网关的控制面通过关联的 K8s 集群（支持TKE/EKS）的 API Server 获取 Ingress 资源的变化，然后动态更新 TSE 云原生网关的路由规则。当 TSE 云原生网关收到请求时，匹配 Ingress 转发规则转发请求到后端Service所对应的Pod。
>? 版本
> 目前支持TKE/EKS的版本：v1.19.0版本以上。
<img src="https://qcloudimg.tencent-cloud.cn/raw/17c8b869e7a9d6270ec3290991f16c1b.png">

## 核心特性与优势
- 兼容原生 Ingress 架构和使用方式，无缝对接容器服务TKE。
- 享有 TSE 云原生网关全部能力，如安全、流控、监控、日志等。
- 支持多 K8s 集群的流量路由，TSE nginx ingress支持跨集群管理Ingress，在跨集群、容灾场景下非常友好。

### 网格
服务网格是一层与业务逻辑无耦合的基础设施，核心职责是通过无侵入的方式为网格内服务提供流量管理、可观测性增强、安全加固等附加能力。云原生场景下，服务网格内的业务应用通常以容器化形式部署。

### Istio

一个开源的服务网格实现项目，TCM是基于Istio项目的服务网格产品，关于Istio的详细介绍，请见[Istio](https://istio.io/latest/zh/docs/concepts/what-is-istio/)。

### Envoy

一个开源的7层代理项目，Istio的数据面实现依托于envoy，关于envoy的详细介绍，请见[Envoy](https://www.envoyproxy.io/docs/envoy/latest/intro/what_is_envoy)。

### Sidecar

Sidecar通过无侵入的形式实现为应用程序添加控制功能，在Istio中，envoy 以sidecar 容器的形式存在于业务Pod中。

### Virtual Service
Virtual Service定义流量通过何种路由策略转发，每个虚拟服务包含一组路由规则，例如基于不同header，进入不同的版本的服务中。

### Destination Rule

和Virtual Service一样，Destination Rule也是Istio流量管理的重要组成部分，定义流量收到流量后的处理策略。

### Gateway

在Istio中，Gateway是流量进入或者流出网格的入口，分为Ingress gateway和egress gateway，可通过配置gateway策略，控制网格的入站和出站流量。

### 边缘代理网关

边缘代理网关是流量进出网关的实体设备，Gateway规则最终在边缘代理网关上承载，在TCM中边缘代理网关为腾讯云CLB。


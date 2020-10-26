## 概述

Nginx Ingress 功能强大且性能极高，有多种部署方式。本文将介绍 Nginx Ingress 在腾讯云容器服务（Tencent Kubernetes Engine，TKE）上 [Deployment + LB](#step1)、[Daemonset + HostNetwork + LB](#step2) 和 [Deployment + LB 直通 Pod](#step3) 三种部署方案及其部署方法。

## Nginx Ingress 简介

Nginx Ingress 是 Kubernetes Ingress 的一种实现。它通过 watch Kubernetes 集群的 Ingress 资源，将 Ingress 规则转换成 Nginx 的配置，让 Nginx 进行7层的流量转发。如下图所示：
<img style="width:450px" src="https://main.qcloudimg.com/raw/cc1260950a0cc812508cf25819e3c129.png" data-nonescope="true">
Nginx Ingress 有以下两种实现方式，本文重点对 Kubernetes 开源社区的实现进行介绍：
- [Kubernetes 开源社区的实现](https://github.com/kubernetes/ingress-nginx)
- [Nginx 官方的实现](https://github.com/nginxinc/kubernetes-ingress)

### 部署方案选型建议
对 Nginx Ingress 在 TKE 上部署的三种方案进行比较，本文向您提出以下选型建议：
1. [Deployment + LB](#step1)：较为简单通用，但在大规模和高并发场景存在性能问题。如果对性能要求低，可以考虑使用此方案。
2. [Daemonset + HostNetwork + LB](#step2)：使用 hostNetwork 性能好，但需要手动维护 CLB 和 Nginx Ingress 节点，也无法实现自动扩缩容，不太建议用此方案。
3. [Deployment + LB 直通 Pod](#step3)：性能好，而且不需要手动维护 CLB，是理想解决方案。但在此方案中需要集群支持 VPC-CNI，如果已有集群本身用的 VPC-CNI 网络插件，或者用的 Global Router 网络插件并开启了 VPC-CNI 的支持（两种模式混用），建议使用此方案。

## 方案1： Deployment + LB<span id="step1"></span>

在 TKE 上部署 Nginx Ingress 最简单的方式是将 Nginx Ingress Controller 以 Deployment 的方式部署，并且为其创建 LoadBalancer 类型的 Service（自动创建负载均衡 CLB 或绑定已有 CLB），使 CLB 接收外部流量，再转发到 Nginx Ingress 内部。如下图所示：
<img style="width:450px" src="https://main.qcloudimg.com/raw/337cf2fa30cb27f89eed438b0458d557.png" data-nonescope="true">
当前 TKE 上 LoadBalancer 类型的 Service 默认实现是基于 NodePort：CLB 会绑定各节点的 NodePort 作为后端 RS（Real Server），将流量转发到节点的 NodePort，节点再通过 Iptables 或 IPVS 将请求路由到 Service 对应的后端 Pod（即 Nginx Ingress Controller 的 Pod）。后续如有节点的增删，CLB 也会自动更新节点 NodePort 的绑定。
执行以下命令安装 Nginx Ingress：
```
kubectl create ns nginx-ingress
```
```
kubectl apply -f https://raw.githubusercontent.com/TencentCloudContainerTeam/manifest/master/nginx-ingress/nginx-ingress-deployment.yaml -n nginx-ingress
```

## 方案2： Daemonset + HostNetwork + LB<span id="step2"></span>

在方案1中，流量会经过一层 NodePort，会多一层转发。因此存在以下问题：
- 转发路径较长，流量到 NodePort 后会再经过 Kubernetes 内部 LB，通过 Iptables 或 IPVS 转发到 Nginx，会增加网络耗时。
- 经过 NodePort 必然发生 SNAT，如果流量过于集中则容易导致源端口耗尽或 conntrack 插入冲突导致丢包，引发部分流量异常。
- 每个节点的 NodePort 也充当一个负载均衡器，CLB 如果绑定大量节点的 NodePort，LB 的状态就分散在每个节点上，容易导致全局负载不均。
- CLB 会对 NodePort 进行健康探测，探测包最终会被转发到 Nginx Ingress 的 Pod，如果 CLB 绑定的节点多，而 Nginx Ingress 的 Pod 少，会导致探测包对 Nginx Ingress 造成较大的压力。

在方案2中，提出以下解决方法：
让 Nginx Ingress 使用 hostNetwork，CLB 直接绑节点 IP + 端口（80,443），不用经过 NodePort。由于使用 hostNetwork，Nginx Ingress 的 pod 就不能被调度到同一节点，为避免端口监听冲突，可提前选取部分节点作为边缘节点，专门用于部署 Nginx Ingress，并为这些节点打上 label，然后 Nginx Ingress 以 DaemonSet 方式部署在这些节点上。架构如下图所示：
<img style="width:450px" src="https://main.qcloudimg.com/raw/09e4a46655dcaa2a32d6b8e02fb8d96c.png" data-nonescope="true">
如需安装 Nginx Ingress，请执行以下步骤：
1. 执行以下命令，将规划好的用于部署 Nginx Ingress 的节点打上 label（注意替换节点名称）：
```
kubectl label node 10.0.0.3 nginx-ingress=true
```
2. 执行以下命令，将 Nginx Ingress 部署在这些节点上:
```
kubectl create ns nginx-ingress
```
```
kubectl apply -f https://raw.githubusercontent.com/TencentCloudContainerTeam/manifest/master/nginx-ingress/nginx-ingress-daemonset-hostnetwork.yaml -n nginx-ingress
```
3. 手动创建 CLB，及创建80和443端口的 TCP 监听器，分别绑定已部署 Nginx Ingress 节点的80和443端口。

## 方案3：Deployment + LB 直通 Pod<span id="step3"></span>

方案2相比方案1更有优势，但仍存在以下问题：
- 提高了手动维护 CLB 和 Nginx Ingress 节点的运维成本。
- 需要提前规划好 Nginx Ingress 的节点，增删 Nginx Ingress 节点时需要手动在 CLB 控制台绑定和解绑节点。
- 无法支持自动扩、缩容。

在方案3中，提出以下解决方法：
- 若网络模式是 VPC-CNI，且所有的 Pod 都使用弹性网卡，您可以使用 CLB 直接绑定弹性网卡的 Pod，即绕过 NodePort，不用手动管理 CLB且支持自动扩、缩容。如下图所示：
<img style="width:450px" src="https://main.qcloudimg.com/raw/83630c50a259482ede83742945fc591e.png" data-nonescope="true">
- 若网络模式是 Global Router，您可以在集群信息页 [为集群开启 VPC-CNI 支持](https://cloud.tencent.com/document/product/457/34993)，即两种网络模式混用。如下图所示：
![](https://main.qcloudimg.com/raw/c61d57e3614c87cbca143fe4d746a15d.png)
确保集群支持 VPC-CNI 之后，依次执行以下命令，即可安装 Nginx Ingress：
```
kubectl create ns nginx-ingress
```
```
kubectl apply -f https://raw.githubusercontent.com/TencentCloudContainerTeam/manifest/master/nginx-ingress/nginx-ingress-deployment-eni.yaml -n nginx-ingress
```



## 常见问题
### 如何支持内网 Ingress ?   
[方案2：Daemonset + HostNetwork + LB](#step2) 是手动管理 CLB，在自行创建 CLB 时可以选择用公网或内网。[方案1：Deployment + LB](#step1) 和 [方案3：Deployment + LB 直通 Pod](#step3) 默认创建公网 CLB。  
如果要用内网，可以重新部署 YAML，给 nginx-ingress-controller 中的 Service 添加 key，例如 `service.kubernetes.io/qcloud-loadbalancer-internal-subnetid`，value 为内网 CLB 创建的子网 id 的 annotation。请参考以下代码：
```
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: subnet-xxxxxx # value 替换为集群所在 vpc 的其中一个子网 id
  labels:
    app: nginx-ingress
    component: controller
  name: nginx-ingress-controller
```

### 如何复用已有 LB ?

[方案1：Deployment + LB](#step1) 和 [方案3：Deployment + LB 直通 Pod](#step3) 默认自动创建新的 CLB，Ingress 的流量入口地址取决于新创建 CLB 的 IP 地址。如果业务对入口地址有依赖，可以让 Nginx Ingress 绑定已有的 CLB。
操作方法为重新部署 YAML，给 nginx-ingress-controller 中的 Service 添加 key，例如 `service.kubernetes.io/tke-existed-lbid`，value 为 CLB ID 的 annotation。请参考以下代码：
```
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.kubernetes.io/tke-existed-lbid: lb-6swtxxxx # value 替换为 CLB 的 ID
  labels:
    app: nginx-ingress
    component: controller
  name: nginx-ingress-controller
```

### Nginx Ingress 公网带宽有多大？

腾讯云账号有标准账户和传统账户两种类型：
>! 您可参考文档 [区分腾讯云账户类型](https://cloud.tencent.com/document/product/684/39903) 来区分自己账号的类型。
>
- **标准账户类型：**指带宽上移到 CLB 或 IP 上管理。
  当您的账号是标准账户类型时，Nginx Ingress 的带宽等于已购 CLB 的带宽，默认是 10Mbps（按量计费），可按需调整。
- **传统账户类型：**指带宽在云服务器（CVM）上管理。
    当您的账号是传统账户类型时，Nginx Ingress 使用公网 CLB，Nginx Ingress 的公网带宽是 CLB 所绑定的 TKE 节点的带宽之和。如果使用 [方案3：Deployment + LB 直通 Pod](#step3)，CLB 直通 Pod，即 CLB 直接绑定弹性网卡，那么此时 Nginx Ingress 的公网带宽是所有 Nginx Ingress Controller Pod 被调度到的节点上的带宽之和。



### 如何创建 Ingress?<span id="ingress"></span>
当您在 TKE 上自行部署 Nginx Ingress，需使用 Nginx Ingress 管理 Ingress 时，在容器服务控制台上无法创建 Ingress 时，可通过 YAML 的方式来创建 Ingress 并且需要给每个 Ingress 都指定 Ingress Class 的 annotation。请参考以下代码：
```
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: test-ingress
  annotations:
    kubernetes.io/ingress.class: nginx # 这里是重点
spec:
  rules:
  - host: *
    http:
      paths:
      - path: /
        backend:
          serviceName: nginx-v1
          servicePort: 80
```

### 如何监控？

通过 [如何创建 Ingress](#ingress) 安装的 Nginx Ingress，已经暴露了 metrics 端口，可以被 Prometheus 采集。如果集群内安装了 prometheus-operator，可以使用 ServiceMonitor 来采集 Nginx Ingress 的监控数据。请参考以下代码：
```
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: nginx-ingress-controller
  namespace: nginx-ingress
  labels:
    app: nginx-ingress
    component: controller
spec:
  endpoints:
  - port: metrics
    interval: 10s
  namespaceSelector:
    matchNames:
    - nginx-ingress
  selector:
    matchLabels:
      app: nginx-ingress
      component: controller
```

原生 Prometheus 配置请参考以下代码：
```
    - job_name: nginx-ingress
      scrape_interval: 5s
      kubernetes_sd_configs:
      - role: endpoints
        namespaces:
          names:
          - nginx-ingress
      relabel_configs:
      - action: keep
        source_labels:
        - __meta_kubernetes_service_label_app
        - __meta_kubernetes_service_label_component
        regex: nginx-ingress;controller
      - action: keep
        source_labels:
        - __meta_kubernetes_endpoint_port_name
        regex: metrics
```

采集监控数据后，可为 grafana 配置 [Nginx Ingress 社区提供的面板](https://github.com/kubernetes/ingress-nginx/tree/master/deploy/grafana/dashboards)，并展示数据。   
实际操作中，直接复制 json 导入 grafana，即可导入面板。其中，`nginx.json` 是展示 Nginx Ingress 各种常规监控的面板。如下图所示：
<img style="width:450px" src="https://main.qcloudimg.com/raw/f6c14b7cd6ff9f2959a818b0c4c4f644.png" data-nonescope="true">
`request-handling-performance.json` 是展示 Nginx Ingress 性能方面的监控面板。如下图所示：
<img style="width:450px" src="https://main.qcloudimg.com/raw/d21748c1903103a5b6988051848292f5.png" data-nonescope="true">


## 参考资料

- [TKE Service YAML 示例](https://cloud.tencent.com/document/product/457/45489#yaml-.E7.A4.BA.E4.BE.8B)
- [TKE Service 使用已有 CLB](https://cloud.tencent.com/document/product/457/45491)
- [区分腾讯云账户类型](https://cloud.tencent.com/document/product/684/39903)

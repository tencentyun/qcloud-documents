>?本文适用于腾讯云容器服务（Tencent Kubernetes Engine ，TKE），以下简称 TKE。
>

## 应用场景
当需明确服务请求来源以满足业务需求时，则需后端服务能够准确获取请求客户端的真实源 IP。例如以下场景：
- 具有对服务请求的来源进行审计的需求，例如异地登录告警。
- 具有针对安全攻击或安全事件溯源的需求，例如 APT 攻击及 DDoS 攻击等。
- 业务场景具有数据分析的需求，例如业务请求区域统计。
- 其他需获取客户端地址的需求。

## 实现方法
在 TKE 中默认的外部负载均衡器为 [腾讯云负载均衡](https://cloud.tencent.com/product/clb) 作为服务流量的访问首入口，腾讯云负载均衡器会将请求流量负载转发到 Kubernetes 工作节点的 Kubernetes Service（默认）。此负载均衡过程会保留客户端真实源 IP（透传转发），但在 Kubernetes Service 转发场景下，无论使用 iptbales 或 ipvs 的负载均衡转发模式，转发时都会对数据包做 SNAT，即不会保留客户端真实源 IP。在 TKE 使用场景下，本文提供以下4种方式获取客户端真实源 IP，请参考本文按需选择适用方式。


### 通过 Service 资源的配置选项保留客户端源 IP
该方式优缺点分析如下：
- **优点**：只需修改 Kubernetes Service 资源配置即可。
- **缺点**：会存在潜在的 Pods（Endpoints）流量负载不均衡风险。

如需启用保留客户端 IP 功能，可在 Service 资源中配置字段 `Service.spec.externalTrafficPolicy`。该字段表示服务是否希望将外部流量路由到节点本地或集群范围的端点。有两个选项值：`Cluster`（默认）和  `Local` 方式。如下图所示：
![externalTrafficPolicy](https://main.qcloudimg.com/raw/a6ff4729ef98bedf5fd677030daf7d50.jpg)
 - `Cluster`：表示隐藏客户端源 IP，`LoadBalancer` 和 `NodePort` 类型服务流量可能会被转发到其他节点的 Pods。
 -  `Local`：表示保留客户端源 IP 并避免 `LoadBalancer` 和 `NodePort` 类型的服务流量转发到其他节点的 Pods，详情请参考 [Kubernetes 设置外部负载均衡器说明](https://kubernetes.io/zh/docs/tasks/access-application-cluster/create-external-load-balancer/)。相关 YAML 配置示例如下：
```yaml
apiVersion: v1
kind: Service
metadata:
  name: example-Service
spec:
  selector:
    app: example-Service
  ports:
    - port: 8765
      targetPort: 9376
  externalTrafficPolicy: Local
  type: LoadBalancer
```


### 通过 TKE 原生 CLB 直通 Pod 转发模式获取
该方式优缺点分析如下：
 - **优点**：为 TKE 原生支持的功能特性，只需在控制台参考对应文档配置即可。
 - **缺点**：集群需开启 VPC-CNI 网络模式，详情请参见 [VPC-CNI 模式说明](https://cloud.tencent.com/document/product/457/34993)。

使用 TKE 原生支持的 CLB 直通 Pod 的转发功能（CLB 透传转发，并绕过 Kubernetes Service 流量转发），后端 Pods 收到的请求的源 IP 即为客户端真实源 IP，此方式适用于四层及七层服务的转发场景。转发原理如下图：
![LB_TO_POD](https://main.qcloudimg.com/raw/bb9884e4b7bfaa776e8741a468694f65.jpg)
详细介绍和配置请参见 [在 TKE 上使用负载均衡直通 Pod](https://cloud.tencent.com/document/product/457/48793)。


### 通过 HTTP Header 获取
该方式优缺点分析如下：
 - **优点**：在七层（HTTP/HTTPS）流量转发场景下推荐选择该方式，可通过 Web 服务代理的配置或后端应用代码直接获取 HTTP Header 中的字段，即可拿到客户端真实源 IP，非常简单高效。
 - **缺点**：仅适用于七层（HTTP/HTTPS）流量转发场景，不适用于四层转发场景。



在七层（HTTP/HTTPS）服务转发场景下，可以通过获取 HTTP Header 中 `X-Forwarded-For` 和 `X-Real-IP`  字段的值来获取客户端真实源 IP。TKE 中有两种场景使用方式，原理介绍图如下所示：
![HttpHeader](https://main.qcloudimg.com/raw/f512625e5fff323a924ddb62a58e8a4b.jpg)

#### 场景一：使用 TKE Ingress 获取真实源 IP
[腾讯云负载均衡器](https://cloud.tencent.com/product/clb)（CLB 七层） 默认会将客户端真实源 IP 放至 HTTP Header 的 `X-Forwarded-For` 和 `X-Real-IP`  字段。当服务流量在经过 Service 四层转发后会保留上述字段，后端通过 Web 服务器代理配置或应用代码方式获取到客户端真实源 IP，详情请参见 [负载均衡如何获取客户端真实 IP](https://cloud.tencent.com/document/product/214/3728)。通过容器服务控制台获取源 IP 步骤如下：
1. 为工作负载创建一个主机端口访问方式的 Service 资源，本文以 nginx 为例。如下图所示：
![](https://main.qcloudimg.com/raw/09c32efc5905dcc76fd97a84eb6a0511.png)
2. 为该 Service 创建一个对应的 Ingress 访问入口，本文以 test 为例。如下图所示：
![](https://main.qcloudimg.com/raw/a9c9e507d8487112c4f5730e20c36153.png)
3. 待配置生效后，在后端通过获取 HTTP Header 中的 `X-Forwarded-For` 或 `X-Real-IP` 字段值得到客户端真实源 IP。后端抓包测试结果示例如下图所示：
![](https://main.qcloudimg.com/raw/a5f36c927c12c616c37039fb0d7a5e76.png)


#### 场景二：使用 Nginx Ingress 获取真实源 IP
Nginx Ingress 服务部署需要 Nginx Ingress 能直接感知客户端真实源 IP，可以采用保留客户端源 IP 的配置方式，详情请参见 [Kubernetes 设置外部负载均衡器说明](https://kubernetes.io/zh/docs/tasks/access-application-cluster/create-external-load-balancer/)。或通过 CLB 直通 Pod 的方式，详情请参见 [在 TKE 上使用负载均衡直通 Pod](https://cloud.tencent.com/document/product/457/48793)。当 Nginx Ingress 在转发请求时会通过 `X-Forwarded-For` 和 `X-Real-IP` 字段来记录客户端源 IP，后端可以通过此字段获得客户端真实源 IP。配置步骤如下：

1. Nginx Ingress 可以通过 TKE 应用商店、自定义 YAML 配置或使用官方（helm 安装）方式安装，原理和部署方法请参见 [在 TKE 上部署 Nginx Ingress](https://cloud.tencent.com/document/product/457/47293)  中的部署方案1或方案3。若选择方案1部署，则需要修改 Nginx Ingress Controller Service 的 `externalTrafficPolicy` 字段值为 `Local` 。
安装完成后，会在容器服务控制台自动为 Nginx Ingress Controller 服务创建一个 CLB（四层）访问入口，如下图所示：
![image-20200928153915958](https://main.qcloudimg.com/raw/09c32efc5905dcc76fd97a84eb6a0511.png)
2. 为需转发的后端服务创建一个 Ingress 资源并配置转发规则。YAML 示例如下：
```yaml
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: nginx  # ingressClass类为"nginx"
  name: example
  namespace: default
spec:
  rules:  # 配置服务转发规则
     - http:
        paths:
          - backend:
              serviceName: nginx  
              servicePort: 80
            path: /
```
3. 待配置生效后，在后端获取 HTTP Header 中的 `X-Forwarded-For` 或 `X-Real-IP` 字段值得到客户端真实源 IP。后端抓包测试结果示例如下图所示：
![image-20200928195217294](https://main.qcloudimg.com/raw/5285ddcb8f56cb3efbc184293b7076b3.png)


### 通过 TOA 内核模块加载获取真实源 IP
该方式优缺点分析如下：
 - **优点**：对于 TCP 传输方式，在内核层面且仅对 TCP 连接的首包进行改造，几乎没有性能损耗。
 - **缺点**：
  - 需要在集群工作节点上加载 TOA 内核模块，且需在服务端通过函数调用获取携带的源 IP 及端口信息，配置使用较复杂。
  - 对于 UDP 传输方式，会对每个数据包改造添加 option 数据（源 IP 和源端口），带来网络传输通道性能损耗。


TOA 内核模块原理和加载方式请参见 [获取访问用户真实 IP](https://cloud.tencent.com/document/product/608/14426) 文档。





## 参考资料
- 腾讯云负载均衡器获取客户端真实 IP 介绍：[如何获取客户端真实 IP](https://cloud.tencent.com/document/product/214/3728)
- 腾讯云负载均衡介绍：[负载均衡 CLB](https://cloud.tencent.com/product/clb)
-  [在 TKE 上部署 Nginx Ingress](https://cloud.tencent.com/document/product/457/47293) 
- TKE 网络模式介绍：[GlobalRouter 附加 VPC-CNI 模式说明](https://cloud.tencent.com/document/product/457/34993)
- [在 TKE 上使用负载均衡直通 Pod](https://cloud.tencent.com/document/product/457/48793)
- TOA 模块使用介绍：[获取访问用户真实 IP](https://cloud.tencent.com/document/product/608/14426)
- Kubernetes 设置外部负载均衡器说明：[创建外部负载均衡器 Kubernetes](https://kubernetes.io/zh/docs/tasks/access-application-cluster/create-external-load-balancer/)

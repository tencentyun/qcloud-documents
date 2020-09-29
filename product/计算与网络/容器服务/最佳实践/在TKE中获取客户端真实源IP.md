# 在 TKE 中获取客户端真实源 IP

> 适用范围：腾讯云容器服务（Tencent Kubernetes Engine ，TKE）, 以下简称 TKE。



## 为什么需要获取客户端真实源 IP？

当需要能感知到服务请求来源去满足一些业务需求时，就需要后端服务能准确获取到请求客户端的真实源 IP， 比如以下场景：

1. 对服务请求的来源有做审计的需求，如异地登陆告警。

2. 针对安全攻击或安全事件溯源需求，如 APT 攻击、DDoS 攻击等。

3. 业务场景数据分析需求，如业务请求区域统计。

4. 其他需要获取客户端地址的需求。

   

## 在 TKE 使用场景下如何获取客户端真实源 IP？

在TKE中默认的外部负载均衡器是 [腾讯云负载均衡器](https://cloud.tencent.com/product/clb)，作为服务流量的访问首入口，腾讯云负载均衡器会将请求流量负载转发到 Kubernetes 工作节点的 Kubernets Service（默认），此负载均衡过程会保留客户端真实源 IP（透传转发），但在 Kubernetes Service 转发场景下，无论是使用 iptbales 还是 ipvs 的负载均衡转发模式，转发时都会对数据包做 SNAT，即不会保留客户端真实源 IP，为了能够准确的获取到客户端的真实源 IP，在 TKE 使用场景下，主要有四种方法获取客户端真实源 IP，下面将逐个展开介绍下：



### 一、通过 Service 资源的配置选项保留客户端源 IP

要启用保留客户端 IP 功能，可在 Service 资源中配置字段 `Service.spec.externalTrafficPolicy`，此字段表示服务是否希望将外部流量路由到节点本地或集群范围的端点。有两个选项值：`Cluster`（默认）和  `Local` 方式，如下图所示：

![externalTrafficPolicy](https://main.qcloudimg.com/raw/a6ff4729ef98bedf5fd677030daf7d50.jpg)

`Cluster`  表示隐藏了客户端源 IP， `LoadBalancer`  和  `NodePort`  类型服务流量可能会被转发到其他节点的 Pods； `Local` 表示保留客户端源 IP 并避免  `LoadBalancer`  和  `NodePort`  类型的服务流量转发到其他节点的 Pods，详情请参考 [kubernets设置外部负载均衡器说明](https://kubernetes.io/zh/docs/tasks/access-application-cluster/create-external-load-balancer/)。相关 YAML 配置示例如下：

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

优点：只需要修改 Kubernets Service 资源配置即可。

缺点：会存在潜在的 Pods（Endpoints）流量负载不均衡风险。



### 二、通过TKE原生的 CLB 直通 Pod 转发模式获取

使用TKE原生支持的 CLB 直通 Pod 的转发功能（CLB 透传转发，并绕过 Kubernetes Service 流量转发），后端 Pods 收到的请求的源IP即是客户端真实源IP，此方式无论是在四层还是七层服务的转发场景下都适用，转发原理如下图：

![LB_TO_POD](https://main.qcloudimg.com/raw/bb9884e4b7bfaa776e8741a468694f65.jpg)

详细介绍和配置请参考文档 [TKE场景下腾讯云CLB直通Pod使用场景介绍]()。

优点：TKE原生支持的功能特性，只需在控制台按照文档配置即可。

缺点：集群需要开启 VPC-CNI 模式网络，详情参考文档 [VPC-CNI 模式说明](https://cloud.tencent.com/document/product/457/34993)



### 三、通过 HTTP Header 获取

在七层（HTTP/HTTPS）服务转发场景下，可以通过获取 Http Header 中 `X-Forwarded-For` 和 `X-Real-IP`  字段的值来获取客户端真实源 IP， TKE 中有两种场景使用方式，原理介绍如下：

![HttpHeader](https://main.qcloudimg.com/raw/f512625e5fff323a924ddb62a58e8a4b.jpg)

在场景一中，[腾讯云负载均衡器](https://cloud.tencent.com/product/clb)（CLB 七层） 默认会将客户端真实源IP放到 HTTP Header 的 `X-Forwarded-For` 和 `X-Real-IP`  字段，当服务流量在经过 Service 四层转发后会保留上述字段，后端通过WEB服务器代理配置或应用代码方式获取到客户端真实源IP，详情参考请文档 [负载均衡如何获取客户端真实 IP - 最佳实践 - 文档中心 - 腾讯云](https://cloud.tencent.com/document/product/214/3728)；

在场景二中， Nginx Ingress 服务部署需要 Nginx Ingress 能直接感知客户端真实源 IP，可以采用保留客户端源IP的配置方式（详情参考 [kubernets设置外部负载均衡器说明](https://kubernetes.io/zh/docs/tasks/access-application-cluster/create-external-load-balancer/) ），或通过 CLB 直通 Pod 的方式（详情参考 [TKE场景下腾讯云CLB直通Pod使用场景介绍]()），当 Nginx Ingress 在转发请求时会通过 `X-Forwarded-For` 和 `X-Real-IP`  字段来记录客户端源 IP，后端可以通过此字段获得客户端真实源 IP。



下面详细介绍在 TKE 中两种场景的配置使用方法：

- #### 场景一：使用 TKE Ingress 获取真实源 IP

 在TKE控制台先为工作负载创建一个主机端口访问方式的 Service 资源，如下图：

![image-20200928151418383](https://main.qcloudimg.com/raw/94ddb4723c57fee53554bf0f0a74d305.png)

然后在控制台为 Service 新建一个对应的 Ingress 访问入口，如下图：

![image-20200928151556491](https://main.qcloudimg.com/raw/116eadeaad1b2d200477e47c24d6beef.png)

待配置生效后，在后端通过获取 HTTP Header 中的 `X-Forwarded-For` 或 `X-Real-IP` 字段值得到客户端真实源 IP。抓包测试结果示例如下：

![image-20200928193102234](https://main.qcloudimg.com/raw/a5f36c927c12c616c37039fb0d7a5e76.png)

- #### 场景二： 使用 Nginx Ingress 获取真实源 IP

Nginx Ingress 可以通过 TKE 应用商店、自定义 YAML 配置或使用官方（helm 安装）方式安装，原理和部署方法可参考文档 [在 TKE 上部署 Nginx Ingress](https://cloud.tencent.com/document/product/457/47293)  中的部署方案一或方案三，若选择方案一部署，则需要修改 Nginx Ingress Controller Service 的 `externalTrafficPolicy` 字段值为 `Local` 。安装完成后，会在TKE控制台自动为 Nginx Ingress Controller 服务创建一个 CLB（四层）访问入口，如下图所示：

![image-20200928153915958](https://main.qcloudimg.com/raw/0d9482fa72a610dbbd6b8253c5a5d4b8.png)



为要转发的后端服务创建一个 Ingress 资源并配置转发规则， 可以使用以下 YAML 创建：

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



待配置生效后，在后端获取 Http Header 中的 `X-Forwarded-For` 或 `X-Real-IP` 字段值得到客户端真实源 IP，测试结果示例如下：

![image-20200928195217294](https://main.qcloudimg.com/raw/5285ddcb8f56cb3efbc184293b7076b3.png)

以上介绍的两种场景都可以满足获取客户端真实源 IP 的需求，且具有以下优点和缺点：

优点：在七层（HTTP/HTTPS）流量转发场景下比较推荐，可通过WEB服务代理的配置或后端应用代码直接获取 Http Header 中的字段即可拿到客户端真实IP，非常简单高效。

缺点：仅适用于七层（HTTP/HTTPS）流量转发场景，不适用于四层转发场景，如果是四层转发场景，请使用后面介绍的其他方式。



### 四、通过 TOA 内核模块加载获取真实源 IP

TOA 内核模块原理和加载方式参考 [全球应用加速 获取访问用户真实 IP - 操作指南 - 文档中心 - 腾讯云](https://cloud.tencent.com/document/product/608/14426) 文档。

优点：对于 TCP 传输方式，在内核层面且仅对 TCP 连接的首包进行改造，几乎没有性能损耗。

缺点：

1. 需要在集群工作节点上加载 TOA 内核模块，且需在服务端通过函数调用获取携带的源 IP、端口信息，配置使用比较麻烦。
2. 对于 UDP 传输方式，会对每个数据包改造添加 option 数据（源 IP 和源端口），带来网络传输通道性能损耗。



## 总结

本文主要介绍了在TKE使用场景下服务端如何获取客户端真实源 IP，以满足用户相关使用场景的需求，用户可通过对比上述四几种方式的优点和缺点，选择适合实际需求场景的最佳方案。



## 参考资料

- 腾讯云负载均衡器获取客户端真实 IP 介绍：[负载均衡 如何获取客户端真实 IP - 最佳实践 - 文档中心 - 腾讯云](https://cloud.tencent.com/document/product/214/3728)


- 腾讯云负载均衡器介绍：[负载均衡CLB负载均衡器弹性流量分发   - 腾讯云](https://cloud.tencent.com/product/clb)
- 在 TKE 上部署 Nginx Ingress： [在 TKE 上部署 Nginx Ingress - 最佳实践](https://cloud.tencent.com/document/product/457/47293) 


- TKE 容器服务网络模式介绍：[容器服务 GlobalRouter 附加 VPC-CNI 模式说明 - 用户指南 - 文档中心 - 腾讯云](https://cloud.tencent.com/document/product/457/34993)


- TKE 场景下 CLB 直通 Pod 使用介绍：[待补充...]


- TOA 模块使用介绍：[全球应用加速 获取访问用户真实 IP - 操作指南 - 文档中心 - 腾讯云](https://cloud.tencent.com/document/product/608/14426)


- Kubernets 设置外部负载均衡器说明：[创建外部负载均衡器 | Kubernetes](https://kubernetes.io/zh/docs/tasks/access-application-cluster/create-external-load-balancer/)




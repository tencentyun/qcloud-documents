### GlobalRouter 附加 VPC-CNI 模式说明
VPC-CNI 模式是腾讯云容器服务支持的扩展网络模式，利用腾讯云的多弹性网卡能力，为集群内的 Pod 分配 VPC 内的 IP 地址。 由腾讯云 VPC 功能负责路由，可实现 Pod 和 Node 的控制面和数据面完全在同一网络层面，该模式下的 Pod 能够复用腾讯云 VPC 所有产品特性。
VPC-CNI 模式存在使用限制，建议您提前考虑是否适配您的业务场景。

### VPC-CNI 模式应用场景
集群开启 VPC-CNI 模式后，创建工作负载时可以选择工作负载使用 VPC-CNI 模式，在 VPC-CNI 模式下能够支持：
StatefulSet 支持固定 IP 类型的 Pod。该类型的 Pod 重启和迁移保持 IP 不变，适用于需要对 IP 来源做访问限制、通过 IP 查询日志等场景。

### VPC-CNI 模式使用限制
- 仅支持 TKE kubernetes 版本在1.10及以上版本。
- 集群需要开启 cni 支持。
- 当前 VPC-CNI 模式的子网不能与其他云上资源共用（如云服务器、负载均衡等）。
- 和子网处于相同可用区的节点才支持创建 VPC-CNI 模式的 Pod，请提前规划 VPC-CNI 模式子网。
- 您需要指定单节点下 VPC-CNI 模式的 Pod 数量上限，创建后不可修改。建议集群中节点配置相同。

### VPC-CNI 模式使用方法
#### 开启 VPC-CNI
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)。
2. 在左侧导航栏中，单击**集群**，进入集群管理页面。单击**基本信息**。
3. 在 VPC-CNI 字段中单击开启，选择子网，并确认使用限制。如下图所示：
![](https://main.qcloudimg.com/raw/e5e3212e0a1fac8eebe5ef6e12f5ed42.png)

#### 在集群内创建使用 VPC-CNI 模式的工作负载
**yaml 示例**
``` yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  labels:
    k8s-app: busybox
  name: busybox
  namespace: default
spec:
  replicas: 3
  selector:
    matchLabels:
      k8s-app: busybox
      qcloud-app: busybox
  serviceName: ""
  template:
    metadata:
      annotations:
        tke.cloud.tencent.com/networks: "tke-route-eni"  
        tke.cloud.tencent.com/vpc-ip-claim-delete-policy: Never
      creationTimestamp: null
      labels:
        k8s-app: busybox
        qcloud-app: busybox
    spec:
      containers:
      - args:
        - "10000000000"
        command:
        - sleep
        image: busybox
        imagePullPolicy: Always
        name: busybox
        resources:
          limits:
            tke.cloud.tencent.com/eni-ip: "1"
          requests:
            tke.cloud.tencent.com/eni-ip: "1"
```
其中：
- spec.template.annotations：tke.cloud.tencent.com/networks: "tke-route-eni"  表明 Pod 使用 VPC-CNI 模式。 
- spec.template.annotations：创建 VPC-CNI 模式的 Pod，您需要设置 annotations，即 `tke.cloud.tencent.com/vpc-ip-claim-delete-policy`，默认是 “Immediate”，Pod 销毁后，关联的 IP 同时被销毁，如需固定 IP，则需设置成 “Never”，Pod 销毁后 IP 将会保留，那么下一次同名的 Pod 拉起后，会使用之前的 IP。
- spec.template.spec.containers.0.resources：创建 VPC-CNI 模式的 Pod，您需要添加 requests 和 limits 限制，即 `tke.cloud.tencent.com/eni-ip`。

>? 如需使用固定 IP 的 StatefulSet，请参见 [固定 Pod IP 类型 StatefulSet 管理](https://cloud.tencent.com/document/product/457/34994)。


#### 关闭 VPC-CNI
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)。
2. 在左侧导航栏中，单击**集群**，进入集群管理页面。单击**基本信息**。
3. 在 VPC-CNI 字段中单击关闭。（仅支持在集群内不存在任何 VPC-CNI 模式的 Pod 时关闭）如下图所示：
![](https://main.qcloudimg.com/raw/6a5d9b920fcec57e1db7bc324f13fbf0.png)

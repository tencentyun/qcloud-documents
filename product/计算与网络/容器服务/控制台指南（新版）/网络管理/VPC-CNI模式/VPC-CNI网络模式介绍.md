
## 使用说明
VPC-CNI 模式是容器服务 TKE 基于 CNI 和 VPC 弹性网卡实现的容器网络能力，适用于对时延有较高要求的场景。该网络模式下，容器与节点分布在同一网络平面，容器 IP 为 IPAMD 组件所分配的弹性网卡 IP。VPC-CNI 模式使用原理图如下所示：
![](https://main.qcloudimg.com/raw/76fce8d2541f9a91a1a2ecdc89403390.jpg)


其中 VPC-CNI 模式分为共享网卡模式和独占网卡模式。两种网络模式适用于不同的场景。您可以根据业务需要选择不同的网络模式。
- [共享网卡模式](https://cloud.tencent.com/document/product/457/50356)：Pod 共享一张弹性网卡，IPAMD 组件为弹性网卡申请多个 IP 给到不同的 Pod。
- [独占网卡模式](https://cloud.tencent.com/document/product/457/50357)：每个 Pod 有独立的弹性网卡，性能更高。受机型影响，不同节点可使用的弹性网卡数量有限，单节点 Pod 密度更低。


## 使用限制
- 仅支持 TKE kubernetes 版本在1.10及以上版本。
- 集群需要开启 cni 支持。
- 当前 VPC-CNI 模式的子网不能与其他云上资源共用（如云服务器、负载均衡等）。
- 和子网处于相同可用区的节点才支持创建 VPC-CNI 模式的 Pod，请提前规划 VPC-CNI 模式子网。
- 您需要指定单节点下 VPC-CNI 模式的 Pod 数量上限，创建后不可修改。建议集群中节点配置相同。



## 使用方法
### 开启 VPC-CNI
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。单击【基本信息】。
3. 在 VPC-CNI 字段中单击开启，选择子网，并确认使用限制。如下图所示：
![](https://main.qcloudimg.com/raw/e5e3212e0a1fac8eebe5ef6e12f5ed42.png)

### yaml 示例

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

### 关闭 VPC-CNI
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。单击【基本信息】。
3. 在 VPC-CNI 字段中单击关闭。（仅支持在集群内不存在任何 VPC-CNI 模式的 Pod 时关闭）如下图所示：
![](https://main.qcloudimg.com/raw/6a5d9b920fcec57e1db7bc324f13fbf0.png)





## 相关操作
### 开启支持固定 Pod IP
- 默认情况下，VPC-CNI 模式**不支持固定 Pod IP 能力**，且该能力仅支持在 [创建集群](https://cloud.tencent.com/document/product/457/32189) 时设置，集群创建完成后无法更改。创建集群时，在配置“集群信息”步骤中，选择“容器网络插件”为【VPC-CNI】，并勾选“开启支持”即可。如下图所示：
![](https://main.qcloudimg.com/raw/f36911bf904ebd35867e24e3b6bb6bb1.png)
 如需为集群开启支持固定 Pod IP，请参见 [固定 IP 模式使用说明](https://cloud.tencent.com/document/product/457/50358)。
- 开启固定 Pod IP 能力后，仅支持选择空子网作为集群网络。
- 固定 IP 的 Pod 不支持跨子网迁移。






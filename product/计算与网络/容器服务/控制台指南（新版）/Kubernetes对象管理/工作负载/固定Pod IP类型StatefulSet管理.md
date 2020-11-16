## 操作场景

如果您存在业务需要在 TKE 中部署，并存在固定 Pod IP 的需求， 您可以使用固定 IP 类型的 StatefulSet。 腾讯云容器服务提供扩展 StatefulSet 固定 IP 的能力，该类型的 StatefulSet 创建的 Pod 将通过弹性网卡分配真实的 VPC 内的 IP 地址。腾讯云容器服务 VPC-CNI 的插件负责 IP 分配，当 Pod 重启或迁移，可实现 IP 地址不变。
您可以通过创建固定 IP 类型 StatefulSet 来满足以下场景：
- 通过来源 IP 授权。
- 基于 IP 做流程审核。
- 基于 Pod IP 做日志查询等。

>!固定 IP 类型 StatefulSet 存在使用限制，仅支持 StatefulSet 生命周期内固定 IP。

## 前提条件

需要在集群内开启 VPC-CNI 模式网络， 详情请参考 [集群开启 VPC-CNI 模式网络](https://cloud.tencent.com/document/product/457/34993)。

## 操作步骤

### 控制台使用
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，并进入【[集群](https://console.qcloud.com/tke2/cluster?rid=1)】的管理页面。。
2. 选择需要查看的集群ID/名称，进入该集群的管理页面。
3. 选择 【工作负载】>【StatefulSet】，进入【StatefulSet】的集群管理页面。
4. 单击【新建】，查看【实例数量】。如下图所示：
![](https://main.qcloudimg.com/raw/2dbd219d6bd76b8fe90971390daacc3c.png)
5. 单击【显示高级设置】，根据您实际需求，设置【StatefulSet】参数。关键参数信息如下：
   ![创建StatefulSet](https://main.qcloudimg.com/raw/2a5bf4e7b3e5c85c62fef2b7b09e02f3.png)
 - 网络模式：勾选【使用 VPC-CNI 模式】。
 - IP 地址范围：目前仅支持随机。
 - 固定 Pod IP：选择【开启】。

#### Yaml 示例
```yaml
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
- spec.template.annotations：tke.cloud.tencent.com/networks: "tke-route-eni"  表明 Pod 使用 VPC-CNI 模式。
- spec.template.annotations：创建 VPC-CNI 模式的 Pod，您需要设置 annotations，即 `tke.cloud.tencent.com/vpc-ip-claim-delete-policy`，默认是 “Immediate”，Pod 销毁后，关联的 IP 同时被销毁，如需固定 IP，则需设置成 “Never”，Pod 销毁后 IP 也将会保留，那么下一次同名的 Pod 拉起后，会使用之前的 IP。
- spec.template.spec.containers.0.resources：创建 VPC-CNI 模式的 Pod，您需要添加 requests 和 limits 限制，即 `tke.cloud.tencent.com/eni-ip`。


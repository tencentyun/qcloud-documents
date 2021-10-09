
## 使用场景

适用于依赖容器固定 IP 的场景。例如，传统架构迁移到容器平台及针对 IP 做安全策略限制。 对 IP 无限制的业务不推荐您使用固定 IP 模式。

## 能力和限制

- 支持 Pod 销毁 IP 保留，Pod 迁移 IP 不变，从而实现固定 IP。
- 支持多子网，但不支持跨子网调度固定 IP 的 Pod， 因此固定 IP 模式的 Pod 不支持跨可用区调度。
- 支持 Pod IP 自动关联弹性公网 IP，从而可支持 Pod 外访。
- 共享网卡的固定 IP 模式，固定 IP 的 Pod 销毁后，其 IP 只在集群范围内保留。若有其他集群或者业务（如 CVM、CDB、CLB 等）使用了同一子网，可能会导致保留的固定 IP 被占用，Pod 再启动时将无法获取 IP。**因此请保证该模式的容器子网是独占使用。**

## 使用方法

您可以通过以下两种方式启用固定 IP：
- 创建集群选择固定 IP 模式的 VPC-CNI。
- 为 GlobalRouter 模式附加固定 IP VPC-CNI 模式。


### 创建集群选择固定 IP 模式的 VPC-CNI
>? 使用此方式启用 VPC-CNI，通过控制台或通过 yaml 创建工作负载，Pod 均默认使用弹性网卡。
>
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，单击左侧导航栏中**集群**。
2. 在“集群管理”页面，单击集群列表上方的**新建**。
3. 在“创建集群”页面，在容器网络插件中选择 “VPC-CNI”。
4. 选择“容器网络插件”为**VPC-CNI**，并勾选“开启支持”固定 Pod IP 即可。如下图所示：
![](https://main.qcloudimg.com/raw/f36911bf904ebd35867e24e3b6bb6bb1.png)


### 为 GlobalRouter 模式附加固定 IP VPC-CNI 模式
#### 为已有集群开启 VPC-CNI
>?
- 为 GlobalRouter 模式附加固定 IP VPC-CNI 模式即创建集群时选择 Global Router 网络插件，后续在集群基本信息页面开启 VPC-CNI 模式（两种模式默认混用）。
- 使用此方式启用 VPC-CNI，Pod 默认不使用弹性网卡。
>
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，单击左侧导航栏中**集群**。
2. 在“集群管理”页面，选择需开启 VPC-CNI 的集群 ID，进入集群详情页。
3. 在集群详情页面，选择左侧**基本信息**。
4. 在集群“基本信息”页面的集群信息模块，在 VPC-CNI 字段中单击开启。
5. 在弹出窗口中选择子网，并确认 IP 回收策略。如下图所示：
![](https://main.qcloudimg.com/raw/cda22252025915b5bb264570c924958a.png)
>! 
>- 针对固定 IP 场景，启用 VPC-CNI 后需要设置 IP 回收策略，即设置 Pod 销毁后需要退还 IP 的时长。
>- 非固定 IP 的 Pod 销毁后可立即释放 IP（非释放回 VPC，释放回容器管理的 IP 池），不受此设置的影响。
6. 单击**提交**，即可完成为已有集群开启 VPC-CNI。


#### 创建固定 Pod IP 类型 StatefulSet
在 GlobalRouter 模式附加 VPC-CNI 模式下，如果您存在业务需要在容器服务 TKE 中部署，并存在固定 Pod IP 的需求，您可以使用固定 IP 类型的 StatefulSet。TKE 提供扩展 StatefulSet 固定 IP 的能力，该类型的 StatefulSet 创建的 Pod 将通过弹性网卡分配真实的 VPC 内的 IP 地址。容器服务 TKE VPC-CNI 的插件负责 IP 分配，当 Pod 重启或迁移，可实现 IP 地址不变。

您可以通过创建固定 IP 类型 StatefulSet 来满足以下场景：
- 通过来源 IP 授权。
- 基于 IP 做流程审核。
- 基于 Pod IP 做日志查询等。

>!固定 IP 类型 StatefulSet 存在使用限制，仅支持 StatefulSet 生命周期内固定 IP。
>
您可通过以下两种方法创建固定 IP：
- 通过控制台创建固定 IP 类型 StatefulSet
 1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，单击左侧导航栏中**集群**。
 2. 选择需要使用固定 IP 模式的集群 ID 名称，进入该集群的管理页面。
 3. 选择**工作负载** > **StatefulSet**，进入**StatefulSet**的集群管理页面。
 4. 单击**新建**，查看**实例数量**。如下图所示：
   ![](https://main.qcloudimg.com/raw/2dbd219d6bd76b8fe90971390daacc3c.png)
 5. 单击**显示高级设置**，根据您实际需求，设置**StatefulSet**参数。关键参数信息如下：
   ![创建StatefulSet](https://main.qcloudimg.com/raw/2a5bf4e7b3e5c85c62fef2b7b09e02f3.png)
   - 网络模式：勾选**使用 VPC-CNI 模式**。
      - IP 地址范围：目前仅支持随机。
      - 固定 Pod IP：选择**开启**。

- 通过 Yaml 创建
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
 - spec.template.annotations：`tke.cloud.tencent.com/networks: "tke-route-eni"` 表明 Pod 使用共享网卡的 VPC-CNI 模式，如果使用的是独立网卡的 VPC-CNI 模式，请将值修改成 `"tke-direct-eni"`。
 - spec.template.annotations：创建 VPC-CNI 模式的 Pod，您需要设置 annotations，即 `tke.cloud.tencent.com/vpc-ip-claim-delete-policy`，默认是 “Immediate”，Pod 销毁后，关联的 IP 同时被销毁。如需固定 IP，则需设置成 “Never”，Pod 销毁后 IP 也将会保留，那么下一次同名的 Pod 拉起后，会使用之前的 IP。
 - spec.template.spec.containers.0.resources：创建共享网卡的 VPC-CNI 模式的 Pod，您需要添加 requests 和 limits 限制，即 `tke.cloud.tencent.com/eni-ip`。如果是独立网卡的 VPC-CNI 模式，则添加 `tke.cloud.tencent.com/direct-eni`。

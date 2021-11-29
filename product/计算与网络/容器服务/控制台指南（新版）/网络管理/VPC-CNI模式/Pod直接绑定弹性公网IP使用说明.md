您可以通过下述方式为 VPC-CNI 模式的 Pod 直接绑定弹性公网 IP（EIP）。

## 前提条件和限制

- IPAMD 使用的角色策略被授权了 EIP 相关的接口权限。
- 目前仅支持自动新建 EIP，不支持指定使用已有 EIP。
- 目前 VPC-CNI 独占网卡非固定 IP 模式暂不支持 EIP 功能（v3.3.9及之后版本可支持）。
- 当前集群删除时暂不支持回收该集群自动创建的 EIP。

## IPAMD 组件角色添加 EIP 接口访问权限

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/policy)，选择左侧的**角色**。
2. 在**访问管理控制台** > **[角色](https://console.cloud.tencent.com/cam/role)**中搜索 IPAMD 组件的相关角色 `IPAMDofTKE_QCSRole`，单击角色名称进入角色详情页面。
3. 在权限设置中，单击**关联策略**。
4. 在弹出的关联策略窗口中，在搜索框中搜索 `QcloudAccessForIPAMDRoleInQcloudAllocateEIP`, 然后勾选已创建的预设策略 `QcloudAccessForIPAMDRoleInQcloudAllocateEIP`。单击**确定**，完成为 IPAMD 组件角色添加 EIP 接口访问权限操作。该策略包含了 IPAMD 组件操作弹性公网 IP 所需的所有权限。

## 自动新建 EIP

如需自动关联 EIP，可参考以下 Yaml 示例：
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  labels:
    k8s-app: busybox
  name: busybox
  namespace: default
spec:
  replicas: 1
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
        tke.cloud.tencent.com/eip-attributes: '{"Bandwidth":"100","ISP":"BGP"}'
        tke.cloud.tencent.com/eip-claim-delete-policy: "Never"
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
            tke.cloud.tencent.com/eip: "1"
          requests:
            tke.cloud.tencent.com/eni-ip: "1"
            tke.cloud.tencent.com/eip: "1"
```

- **spec.template.annotations：tke.cloud.tencent.com/eip-attributes: '{"Bandwidth":"100","ISP":"BGP"}'** 表明该 Workload 的 Pod 需要自动关联 EIP，且 EIP 的带宽是 100 Mbps，线路类型是 BGP。
- **spec.template.annotations：tke.cloud.tencent.com/eip-claim-delete-policy: "Never"** 表明 Workload 的 Pod 的 EIP 也需要固定，Pod 销毁后不能变更。若不需要固定，则不添加该注解。
- **spec.template.spec.containers.0.resources**：关联 EIP 的 Pod，您需要添加 requests 和 limits 限制，即 `tke.cloud.tencent.com/eip`，从而让调度器保证 Pod 调度到的节点仍有 EIP 资源可使用。


#### 关键配置说明
- 各节点可绑定的 EIP 资源受到相关配额限制和云服务器的绑定数量限制，详情可参考 [EIP使用限制](https://cloud.tencent.com/document/product/1199/41648#eip-.E9.85.8D.E9.A2.9D.E9.99.90.E5.88.B6)。
各节点可绑定的最大 EIP 数量为**云服务器绑定数量 - 1**。
- **tke.cloud.tencent.com/eip-attributes: '{"Bandwidth":"100","ISP":"BGP"}'**：当前只支持配置带宽和线路类型两个参数。`ISP`参数可配置为 `BGP`、`CMCC`、`CTCC`、`CUCC`，分别对应普通线路 BGP IP、静态单线 IP（网络运营商中国移动、中国电信、中国联通）。若不填写，则默认值为 100 Mbps 和 BGP。
- 当前自动申请的 EIP 绑定后不收取 IP 资源费用，访问公网网络默认计费方式为`流量按小时后付费`，详情见 [EIP 计费概述](https://cloud.tencent.com/document/product/1199/41692)。

## EIP 的保留和回收

Pod 启用自动关联 EIP 特性后，网络组件会为该 Pod 在同 namespace 下创建同名的 CRD 对象 `EIPClaim`。该对象描述 Pod 对 EIP 的需求。

对于非固定 EIP 的 Pod，其 Pod 销毁后 `EIPClaim` 也会被销毁，Pod 关联的 EIP 随之销毁回收。而对于固定 EIP 的 Pod，其 Pod 销毁后 `EIPClaim` 仍然保留，EIP 也因此保留。**同名**的 Pod 启动后会使用同名的 `EIPClaim` 关联的 EIP，从而实现 EIP 保留。

下面介绍三种回收 EIP 的方法：过期回收、手动回收及级联回收。

### 过期回收（默认支持）
在 [创建集群](https://cloud.tencent.com/document/product/457/32189) 页面，容器网络插件选择 **VPC-CNI** 模式并且勾选**开启支持**固定 Pod IP 支持，如下图所示：
![](https://main.qcloudimg.com/raw/ad1290436fa0ff66d8bb17abd2bab161.png)
在高级设置中设置 IP 回收策略，可以设置 Pod 销毁后多少秒回收保留的固定 IP。如下图所示：
![](https://main.qcloudimg.com/raw/a9adcfc9618452c4afd45dfdd27c050f.png)
对于**存量集群**，也可支持变更：
- 修改现存的 tke-eni-ipamd deployment：`kubectl edit deploy tke-eni-ipamd -n kube-system`。
- 执行以下命令，在 `spec.template.spec.containers[0].args` 中加入/修改启动参数。
```yaml
- --claim-expired-duration=1h # 可填写不小于 5m 的任意值 
```

### 手动回收
对于急需回收的 EIP，找到对应的 Pod 的名称空间和名称，执行以下命令通过手动回收：
>! 需保证回收的 EIP 对应的 Pod 已经销毁，否则会再次触发关联绑定 EIP。
>
```
kubectl delete eipc <podname> -n <namespace>
```

### 级联回收
目前的固定 EIP 与 Pod 强绑定，而与具体的 Workload 无关（例如 deployment、statefulset 等）。Pod 销毁后，固定 EIP 不确定何时回收。TKE 现已实现删除 Pod 所属的 Workload 后即刻删除固定 EIP。**要求 IPAMD 组件版本在 v3.3.9+（可通过镜像 tag 查看）**。

以下步骤介绍如何开启级联回收：
1. 修改现存的 **tke-eni-ipamd deployment：`kubectl edit deploy tke-eni-ipamd -n kube-system`**。
2. 执行以下命令，在 `spec.template.spec.containers[0].args` 中加入启动参数：
```yaml
- --enable-ownerref
```

修改后，ipamd 会自动重启并生效。生效后，增量 Workload 可实现级联删除固定 EIP，存量 Workload 暂不能支持。

## 固定IP模式使用说明

### 固定IP模式的使用场景
适用于依赖容器固定 IP 的场景。例如，传统架构迁移到容器平台及针对 IP 做安全策略限制。 对IP无限制的业务不推荐您使用固定IP模式。

### 固定IP模式的能力和限制
1. 支持多子网，但不支持跨子网调度固定IP的Pod， 因此固定IP模式的Pod不支持跨可用区调度
2. 固定 IP 的动态预留，固定 IP 模式下，网卡的主 IP 不能漂移，也即不能作为固定 IP。因此节点在绑定弹性网卡后，会占用一个不能分配给 Pod 的 IP。因此，如果不做预留，那么若用户不加限制的扩展节点，会导致子网内的 IP 都作为节点主 IP 使用了，无法再分配给 Pod，也就导致节点绑定的弹性网卡不可再绑定辅助 IP（主 IP 和辅助 IP 需在同子网）。从而产生了 IP 严重浪费的问题。TKE提供了动态预留IP资源的能力， 动态预留组件 tke-dynamic-reservation 会定时计算各节点的资源使用率，当节点的 CPU requests 或 Memory requests 超过阈值后，组件会设置节点的 eni-ip 配额 tke.cloud.tencent.com/eni-ip 为当前已使用的值+1。
3. 固定 IP Workload 级联删除：目前的固定 IP 与 Pod 强绑定，而与具体的 Workload 无关（如 deployment, statefulset 等）。Pod 销毁后，固定 IP 不好确定何时回收。 TKE实现了删除 Pod 所属的 Workload 后就删除固定 IP。


### 使用方法
您可以通过以下两种方式使用固定IP
- 创建集群选择固定IP模式的VPC-CNI
- 为GlobalRouter模式附加固定IPVPC-CNI模式

#### 创建固定Pod IP类型StatefulSet

如果您存在业务需要在 TKE 中部署，并存在固定 Pod IP 的需求， 您可以使用固定 IP 类型的 StatefulSet。 腾讯云容器服务提供扩展 StatefulSet 固定 IP 的能力，该类型的 StatefulSet 创建的 Pod 将通过弹性网卡分配真实的 VPC 内的 IP 地址。腾讯云容器服务 VPC-CNI 的插件负责 IP 分配，当 Pod 重启或迁移，可实现 IP 地址不变。
您可以通过创建固定 IP 类型 StatefulSet 来满足以下场景：
- 通过来源 IP 授权。
- 基于 IP 做流程审核。
- 基于 Pod IP 做日志查询等。

>!固定 IP 类型 StatefulSet 存在使用限制，仅支持 StatefulSet 生命周期内固定 IP。


##### 操作步骤

##### 控制台使用
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

##### Yaml 示例
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



### 固定IP模式常见问题
#### 1. 节点不能分配到弹性网卡，从而无法正常调度Pod
当节点加入到集群后，ipamd会尝试从和节点相同可用区的子网（配置给ipamd的子网）中为节点绑定一个弹性网卡，如果ipamd异常或者没有给ipamd配置和节点相同可用区的子网，ipamd都没法给节点分配辅助网卡，另外如果当前vpc使用的辅助网卡数目超过上限，也无法给节点分配辅助网卡，遇到这种问题可以通过以下命令确认问题
```hell
kubectl get event
```
如果event中显示 ENILimit，可以明确是配额问题，可以让vpc调大弹性网卡数目配额，当配额调大后，问题会自动消失
![](https://main.qcloudimg.com/raw/6e3b74969497f286ff8adebad370ebf3.png)
另外如果event中显示上图信息则说明子网中的IP可能不够用了，可以通过该命令获取当前子网IP使用数目
```shell
kubectl get vip | wc -l
```

如果明确子网中使用的IP还远远没有达到子网的理论上限，可能和底层做的软限制有关，这个解释起来有些复杂：
以高配机型（每个节点关联的弹性网卡可以额外分配29个IP）和配置的子网是 /23 的为例，当集群有17个节点时，这些节点上理论能使用的IP资源 17*(29+1) 已经超过500了，已经能把 /23的子网填满了，ipamd就会限制新的节点不再分配弹性网卡了，这里推荐的解决方案是再添加一些子网，这样弹性网卡可以从新子网中创建并绑定到新添加的节点上，新的节点虽然能够加入集群，但是pod不会调度到没有绑定弹性网卡的节点
如果不加限制，后面节点加的越来越多时会导致能分给pod的IP越来越少，因为弹性网卡本身会占用一个主IP，这个主IP不能用于Pod，所以添加一个节点，实际上子网可以分给pod的IP会少一个，并且在极端情况下，可能分配给节点的辅助网卡都集中在一个子网中，这会限制整个集群中pod的规模，并且只能通驱逐旧的节点，添加子网后，再将节点加入集群才能恢复.


#### 2.节点不能分配到弹性网卡，提示弹性网卡数量超出限制
现象：节点配置的弹性网卡无法绑定，nec 关联的 vip attach 失败。查看 nec 可以看到节点关联的 nec status 为空。
```shell
kubectl get nec -o yaml
```
![](https://main.qcloudimg.com/raw/97960b500a2239f5a4e0003f1fe1b5af.png)

查看 nec 关联的 vip 可以看到报错 VIP 状态为 Attaching，报错信息为
```shell
kubectl get vip -oyaml
```
![](https://main.qcloudimg.com/raw/141db7416dcfa546e6083e6f099ecf98.png)

解决方案：目前腾讯云弹性网卡限制一个 Vpc 下面最多绑定 50 个弹性网卡。提交工单申请提高配额，配额按地域生效。


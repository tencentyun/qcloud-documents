## 使用场景

适用于不依赖容器固定 IP 的场景。例如，可部署多副本的无状态服务，无状态离线业务等。

## 能力和限制

- 支持节点维护可用的网卡/ IP 池，从而支持 Pod 大规模快速重建。
- 支持预绑定策略，从而一定范围内支持 Pod 快速扩容。
- 支持弹性伸缩网卡/ IP，从而可避免 IP 浪费，提高 IP 利用率。
- 预绑定值不可为0，即暂不能支持完全按需分配，节点数过多可能会造成 IP 浪费。




## IP 地址管理原理
TKE 组件在每个节点维护一个可弹性伸缩的独占网卡/IP 池。已绑定的独占网卡/IP 数量将被维持在 **Pod 数量 + 最小预绑定数量**及 **Pod 数量 + 最大预绑定数量**之间。
- 当**已绑定数量 < Pod 数量 + 最小预绑定数量**时，会绑定独占网卡/IP 使得**已绑定数量 = Pod 数量 + 最小预绑定数量**。
- 当**已绑定数量 > Pod 数量 + 最大预绑定数量**时，会定时释放独占网卡/IP（约2分钟一次），直到**已绑定数量 = Pod 数量 + 最大预绑定数量**。
- 当**最大可绑定数量 < 当前已绑定数量**时，会直接释放多余的空闲独占网卡/IP，使得**已绑定数量 = 最大可绑定数量**。

## 使用方法


您可以通过以下方式启用非固定 IP：
- 创建集群选择非固定 IP 模式的 VPC-CNI：集群创建时不勾选**固定Pod IP** 选项。
![](https://qcloudimg.tencent-cloud.cn/raw/851c0378d547b63f3c1d1ab960046db8.png)


### 支持快释放

默认情况，非固定 IP 模式管理的网卡/IP 池采用慢释放策略，默认是2分钟只释放1个多余的网卡/IP，若用户需要更高效的利用 IP，则需要开启快释放，快释放模式下，每2分钟会检查一次网卡/IP 池，释放多余的网卡/IP，直到空闲网卡/IP 数等于最大预绑定值。

#### 开启方法
- 修改现存的 tke-eni-agent daemonset：`kubectl edit ds tke-eni-agent -n kube-system`。
- 在 `spec.template.spec.containers[0].args` 中加入以下启动参数开启快释放。修改后，agent 会滚动更新生效特性。
```
- --enable-quick-release
```

### 指定某节点预绑定数量
可通过修改节点对应的 CRD `NEC` 的注解来指定该节点 eni-ip 预绑定的数量，相关的注解为：
```
# 共享网卡模式指定最小预绑定值
"tke.cloud.tencent.com/route-eni-ip-min-warm-target"
# 共享网卡模式指定最大预绑定值
"tke.cloud.tencent.com/route-eni-ip-max-warm-target"
# 独占网卡模式指定最小预绑定值
"tke.cloud.tencent.com/direct-eni-min-warm-target"
# 独占网卡模式指定最大预绑定值
"tke.cloud.tencent.com/direct-eni-max-warm-target"
```
修改方法如下：
```
# 示例, 修改节点 <nodeName> 的最小预绑定 ip 值为1
kubectl annotate nec <nodeName> "tke.cloud.tencent.com/route-eni-ip-min-warm-target"="1" --overwrite
# 示例, 修改节点 <nodeName> 的最大预绑定 ip 值为3
kubectl annotate nec <nodeName> "tke.cloud.tencent.com/route-eni-ip-max-warm-target"="3" --overwrite
```
- 修改后即触发动态预绑定的检查，如果预绑定数量不满足期望，会绑定足够网卡/IP。反之则会解绑网卡/IP。
- 修改时这两个注解必须同时存在，且满足：`0 <= 最小预绑定 <= 最大预绑定`，否则修改失败。

### 指定某节点最大绑定数量
可通过修改节点对应的 CRD `nec` 的注解来指定该节点网卡/IP 最大绑定的数量，可指定最大的网卡数和单网卡绑定的 IP 数，相关的注解为：
```
# 共享网卡模式指定最大网卡数
kubectl annotate nec <nodeName> "tke.cloud.tencent.com/route-eni-max-attach"="1" --overwrite
# 共享网卡模式指定单网卡绑定的 IP 数
kubectl annotate nec <nodeName> "tke.cloud.tencent.com/max-ip-per-route-eni"="9" --overwrite
# 独占网卡模式指定最大独占网卡数
kubectl annotate nec <nodeName> "tke.cloud.tencent.com/direct-eni-max-attach"="5" --overwrite
```
修改时需保证修改值大于等于节点当前正在使用的网卡/IP 数量，否则修改失败。
修改后即触发动态预绑定的检查，如果`已绑定数量 > 最大可绑定值`，则会解绑网卡/IP，使`已绑定数量 = 最大可绑定值`。

### 指定默认预绑定数量
- 修改现存的 tke-eni-ipamd deployment：`kubectl edit deploy tke-eni-ipamd -n kube-system`。
- 在 `spec.template.spec.containers[0].args` 中加入以下启动参数修改默认预绑定值。修改后，ipamd 会自动重启并生效。默认值只影响新增的节点：
```
# 共享网卡模式最小预绑定默认值，默认值为 5
- --ip-min-warm-target=3
# 共享网卡模式最大预绑定默认值，默认值为 5
- --ip-max-warm-target=3
# 独占网卡模式最小预绑定默认值，默认值为 1
- --eni-min-warm-target=3
# 独占网卡模式最大预绑定默认值，默认值为 1
- --eni-max-warm-target=3
```

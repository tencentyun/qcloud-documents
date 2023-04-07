
VPC-CNI 组件包含3个 kubernetes 集群组件，分别是 `tke-eni-agent`、`tke-eni-ipamd` 和 `tke-eni-ip-scheduler`。一般情况下，三个组件版本相同，但 `tke-eni-ip-scheduler` 组件变更较少，版本可能会稍微落后。

## 查看当前组件的版本信息

组件的版本即为镜像的 Tag，通过 kubernetes API 可查看：
```
# 查看 tke-eni-agent 的版本
kubectl -nkube-system get ds tke-eni-agent -o jsonpath={.spec.template.spec.containers[0].image}
# 查看 tke-eni-ipamd 的版本
kubectl -nkube-system get deploy tke-eni-ipamd -o jsonpath={.spec.template.spec.containers[0].image}
# 查看 tke-eni-ip-scheduler 的版本
kubectl -nkube-system get deploy tke-eni-ip-scheduler -o jsonpath={.spec.template.spec.containers[0].image}
```

## 变更记录



<table>
<tr>
	<th style="width:13%">版本号</th><th>发布时间</th><th>变更内容</th><th>变更影响</th>
</tr>
<tr>
	<td>v3.4.7</td><td>2022-09-07 </td>
    <td>
<li>支持 ip-scheduler 优先调度策略，已固定 IP 的 Pod 优先调度到子网匹配的网卡上。</li><li> eni-ipamd 支持干跑（dryrun）同步存量自定义资源（CR），及时发现变更异常。</li><li>优化网卡和IP绑定的轮询逻辑，减少因 网卡/IP 正在绑定导致的报错。</li><li>修复非固定 IP 模式共享网卡释放时小概率造成内部 IP 分配泄漏的问题。</li>
    </td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.4.6</td><td>2022-07-26 </td>
    <td>
<li>支持原生节点池。</li>
    </td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.4.5</td><td>2022-06-28 </td>
    <td>
<li>共享网卡非固定 IP 模式支持 IPv6 双栈，双栈模式下，每个 Pod 会同时分配 v6 IP 和 v4 IP。</li><li>修复由于超级节点上的 nodeLost 导致 EIP 失效的问题，修复后会重新绑定 EIP。</li>
    </td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.4.4</td><td>2022-06-06 </td>
    <td>
<li>EIP 默认打上标签 `tke-clusterId` 和 `tke-created-eip`, 同时默认继承自 TKE 集群的标签。</li><li>支持解绑已关机实例上的网卡。</li><li>优化调度器 ip-scheduler，解决因子网太多导致启动太慢的问题。</li>
    </td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.4.3</td><td>2022-04-13 </td>
    <td>
<li>eni-ipamd 和 ip-scheduler 支持禁用子网，禁用的子网只能指定分配，通过启动参数`--only-nominated-eni-subnets`设置。</li><li> 固定 IP 模式支持 pod 指定子网，通过注解 `tke.cloud.tencent.com/nominated-eni-subnets` 指定，多个子网用 `,` 分隔。</li><li> eni-agent 支持保护系统关键内核参数，利用 TLinux 的新特性防止关键内核参数（`rp_filter`，`ip_forward`）修改。</li><li> 修复共享网卡模式下节点初始化时小概率由于 kubelet 重启，节点的 eni-ip 资源注册失败的问题。</li><li>修复由于容器运行时进程 dockershim 或 containerd 重启导致 IP 垃圾回收机制失效的问题。</li>
    </td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.4.2</td><td>2022-03-04 </td>
    <td>
<li>非固定 IP 模式支持节点指定弹性网卡子网。</li><li>eni-agent 支持自动定时设置 ip_forward 和 rp_filter 等关键内核参数，以避免关键内核参数变更导致的网络故障。</li><li> 优化调度性能，共享网卡模式若遇到网卡正在绑定会轮询等待，减少调度失败。</li><li> 修复节点高负载情况下小概率丢失 eni-ip 扩展资源的问题。</li><li>尝试删除并重建长时间 Pending 的网卡和 IP，修复由于底层故障导致的网卡和 IP 长时间不可用的问题</li>
    </td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.4.1</td><td>2022-01-21 </td>
    <td>
<li>支持固定 IP Pod 弹 TKE Serverless 节点且 IP 不变。</li><li> 支持指定 EIP，相关注解`tke.cloud.tencent.com/eip-id-list`。</li><li> 支持独立网卡非固定 IP 模式绑定安全组。</li><li> 升级 CRD APIVersion 至 v1，支持 kubernetes 1.22。</li><li>修复固定 IP 模式下，IP 状态小概率不同步的问题。</li>
    </td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.4.0</td><td>2021-12-08 </td>
    <td>
<li> 支持固定 IP 多网卡。</li><li> 支持混合云 Underlay 云下云上互通，pod 弹性部署。</li><li> 修复同 pod 小概率并发 CNI 导致的 CNI 数据面设置不正确的问题。</li>
</td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.3.9</td><td>2021-11-09 </td>
    <td>
<li> 修复网络原因导致的 EIP 重复创建问题。</li><li> 支持独立网卡非固定 IP 模式的 Pod 绑定 EIP。</li><li> 优化 eni-agent 的扩展资源机制，使扩展资源的管理更加稳定健壮。</li><li> 修复节点设置配额和实际配额不一致导致的问题。</li><li> 优化 eni-agent IP 垃圾回收机制，针对正在创建的 Pod，如果有脏容器，则将回收 IP 分给该 Pod 的新容器。</li><li> 优化非固定 IP 模式下已使用 IP 和网卡的资源计数算法，修复 Error、Evicted、Completed 等状态的 Pod 导致的资源计数不准的问题</li>
</td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.3.8</td><td>2021-08-17 </td>
    <td>
<li> 支持 `--master` 参数直接配置后端 kube-apiserver 地址，解除 kube-proxy 依赖。</li><li> eni-agent 支持参数 `--kube-client-qps` 和 `--kube-client-burst` 配置 kube client 的 QPS 和 Burst，默认值提升至 10 和 20。</li><li> eni-agent 若发现更新后的扩展资源比原来更少，提前将最新的扩展资源信息更新到节点状态中，避免因为 kubelet 异步更新带来的问题。</li></td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.3.7</td><td>2021-08-13 </td>
    <td>

<li> eni-ipamd 支持 `--enable-node-condition` 和 `--enable-node-taint` 参数，打开后，若节点缺少 `eni-ip` 或 `direct-eni` 等本该需要的扩展资源，节点的 condition 或 taints 将被设置。</li><li> EIP 支持 json 格式解析新的 API 参数。</li><li> 修复 containerd 运行时下，eni-agent 的垃圾回收小概率会把刚分配好的 IP 错误回收的问题。</li><li> 修复 EIP 接口可能导致的 ipamd panic 问题。</li><li> 修复非固定 IP 模式升级时，可能误设置了 `disable-node-eni` annotation 导致网卡被解绑的问题</li>
</td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.3.6</td><td>2021-07-26 </td>
    <td>
<li> 修复 eni-agent 垃圾回收机制可能导致刚分配好的 IP 和路由被错误回收的问题。</li><li> 修复 eni-ipamd 在打开级联回收 `--enable-ownerref` 之后，在删除deployment等上层资源时，IP 可能先于 Pod 释放的问题。</li>
    </td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.3.5</td><td>2021-07-20 </td>
    <td>
<li> 修复非固定 IP 模式下，共享网卡/独占网卡的 Pod 由于 IP 或 ENI 资源被误删除导致本地存储数据不能删除的问题。</li><li> 修复非固定 IP 模式下，共享网卡/独占网卡的 CNI 信息没有存储校验 Pod 网卡信息的问题。</li>
    </td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.3.4</td><td>2021-07-07 </td>
    <td>
<li> 修复 CVM 已关机下不断重试解绑网卡的问题。</li><li> 修复异步日志同步写导致的 panic 问题。</li><li> 优化非固定 IP 模式的网卡同步逻辑，保证内部数据一致性，避免解绑正在使用的网卡。</li><li> 修复从 v3.2 升级的非固定 IP 集群由于子网 IP 不足导致存量节点不能分配 IP 的问题。</li><li> 修复存量网卡主 IP 被 Pod 使用的网卡可能会被错误释放的问题。</li>
    </td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.3.3</td><td>2021-06-07 </td>
    <td>
<li> 支持混合云 ipam，与 cilium overlay/underlay 模式协同工作。</li>
    </td><td>对业务无影响</td>
</tr>
</tr>
<tr>
	<td>v3.3.2</td><td>2021-06-01 </td>
    <td>
<li> ip-scheduler 支持抢占，但只支持默认资源不足导致的抢占，暂不支持 ip 资源不足导致的抢占。</li><li> 重构共享网卡的安全组功能逻辑，支持与节点设置安全组强同步，保证安全组绑定顺序与优先级与用户设置一致。</li><li> 支持 cilium cni-chain 模式。</li><li> eni-agent 支持`--port-mapping` 参数实现 Pod `hostPort` 字段支持。</li><li> 支持 Pod 打上注解 `tke.cloud.tencent.com/claim-expired-duration` 实现特定的固定 IP 回收时间，Pod 注解只影响增量。</li>
    </td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.3.1</td><td>2021-05-11 </td>
    <td>
<li> 支持共享网卡非固定 IP 模式使用多网卡。</li><li> 支持腾讯云 API 调用接口 QPS 限制，默认单集群限制为 50 QPS（按 CVM、VPC、TKE 类型限制）。</li><li> 支持非固定 IP 模式升配后的 IP 配额变化感知。</li><li> 支持 `node` 注解 `tke.cloud.tencent.com/desired-route-eni-pod-num`，写入需要的 route-eni ip 数量，写入后组件自动调整节点配额。</li><li> 修复由于 VPC 任务不存在导致的 VPC 任务轮询超时问题。</li><li> 修复由于网卡创建任务失败导致的 eni-ipamd panic 问题。</li><li> 优化路由对账逻辑，只清除属于 eni-agent 管理的 IP 路由。</li><li> 修复独立网卡非固定 IP 模式在释放网卡的时候可能由于网卡已经释放导致的异常 panic 问题。</li>
    </td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.3.0</td><td>2021-04-13 </td>
    <td>
<li> 支持自定义 GR 模式，该模式支持节点集群多 CIDR。</li>
    </td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.2.6</td><td>2021-03-31 </td>
    <td>
<li> 减少独占网卡模式下绑定网卡的重试时间，提高绑定效率。</li><li> 通过并发控制，减少并发绑定和解绑网卡的失败，提高绑定和解绑的效率。</li><li> 非固定 IP 模式优化网卡子网分配逻辑，修复并发加节点时，部分节点在 IP 充足的情况下拿不到 IP 的问题。</li><li> eni-agent 垃圾回收机制支持自感知底层运行时，并支持 containerd。</li>
    </td><td>对业务无影响</td>
</tr>
<tr>
	<td>v3.2.5</td><td>2021-02-22 </td>
    <td>
<li> eni-ipamd 和 ip-scheduler 部署时增加 dnsConfig，避免用户自建 DNS 带来的问题。</li><li> 共享网卡固定 IP 模式下，每个节点绑定的网卡的 subnetID 信息会同步到节点的 label 上，key 为 `tke.cloud.tencent.com/route-eni-subnet-ids`。</li><li> eni-agent 会尝试获取 IP 申请分配失败的原因，并返回给 CNI 插件，最终体现在 Pod event 中。</li><li> 支持裸 Pod 指定 IP，通过注解 `tke.cloud.tencent.com/nominated-vpc-ip` 可指定。</li><li> eni-agent 支持定时测试和 APIServer 的连接情况，若超时则自动重启。</li><li> 修复由于内部数据不一致导致的 ip 浪费的问题。</li>
    </td><td>对业务无影响</td>
</tr>
</table>


## TKE kubernetes 1.16.3 revisions
| 时间         | 版本                  | 更新内容                                               |
| ---------- | ------------------- | ----------------------------------------------------- |
| 2020.03.11 | v1.16.3-tke.3 | <ul class="params"><li> [cbs intree 解决磁盘不存在时继续卸载磁盘，导致大量无效请求的问题](https://git.code.oa.com/k8s/kubernetes/merge_requests/128)</li> <li> [metadata 增加本地缓存](https://git.code.oa.com/k8s/kubernetes/merge_requests/135)</li></ul>|
| 2020.02.14 | v1.16.3-tke.2 | <ul class="params"><li>合并[ pr2359 ](https://github.com/google/cadvisor/pull/2359)解决获取不到 docker root 造成的监控缺失问题</li><li>合并[ pr86583 ](https://github.com/kubernetes/kubernetes/pull/86583)提高 iptables 不支持 random-fully 时的日志输出级别，避免产生过多日志</li><li>kube-scheduler 支持[ 动态设置日志级别 ](https://git.code.oa.com/k8s/kubernetes/merge_requests/103)</li><li>绕过 cbs 出现的 device path（/dev/disk/by-id/virtio-xxx/...）缺失的问题，让用户能正常使用 cbs </li><li>合并[ pr86230 ](https://github.com/kubernetes/kubernetes/pull/86230)，在 pod 调度过程中，跳过更新 assumed pod 的调度</li></ul> |
| 2020.01.06 | v1.16.3-tke.1 | <ul class="params"><li>合并[ pr79036 ](https://github.com/kubernetes/kubernetes/pull/79036)解决当开启 cpumanager 时，如果 pod 的 QoS 为 Guaranteed，则关闭 cpu quota</li><li>合并[ pr84167 ](https://github.com/kubernetes/kubernetes/pull/84167)解决因为 ETCD key 前缀不正确导致 apiserver 健康检查失败的问题</li><li>https://github.com/kubernetes/kubernetes/pull/84167</li><li>revert [ pr63066 ](https://github.com/kubernetes/kubernetes/pull/63066)修复 LB 健康检查与 IPVS 的问题</li><li>合并[ pr72914 ](https://github.com/kubernetes/kubernetes/pull/72914)修复删除Pod后立即创建并调度到同一个节点可能导致无法挂载成功的问题</li><li>解决在CentOS下创建容器会导致[ cgroup泄露的问题 ](https://git.code.oa.com/k8s/kubernetes/merge_requests/31) </li><li> [ubuntu16 下 lxcfs 升级造成 pod 退出问题修复](https://git.code.oa.com/k8s/kubernetes/merge_requests/70)</li><li> [metadata 增加缓存和超时;cloud-provider 增加将节点名称作为hostname的支持](https://git.code.oa.com/k8s/kubernetes/merge_requests/74)</li><li> [revert: pr79036 解决当开启 cpumanager 时，如果 pod 的 QoS 为 Guaranteed，则关闭 cpu quota](https://git.code.oa.com/k8s/kubernetes/merge_requests/78)</li><li>绕过 cb s出现的 device path（/dev/disk/by-id/virtio-xxx/...）缺失的问题，让用户能正常使用 cbs</li></ul> |

## TKE kubernetes 1.14.3 revisions
| 时间         | 版本                  | 更新内容                                               |
| ---------- | ------------------- | ----------------------------------------------------- |
| 2020.01.13 |v1.14.3-tke.9  | <ul class="params"><li> 合并[ pr2359 ](https://github.com/google/cadvisor/pull/2359)解决获取不到docker root造成的监控缺失问题</li> <li>合并[ pr86583 ](https://github.com/kubernetes/kubernetes/pull/86583)提高 iptables 不支持 random-fully 时的日志输出级别，避免产生过多日志</li><li>kube-scheduler支持[ 动态设置日志级别 ](https://git.code.oa.com/k8s/kubernetes/merge_requests/103)</li><li>绕过 cbs 出现的 device path（/dev/disk/by-id/virtio-xxx/...）缺失的问题，让用户能正常使用 cbs </li><li>合并[ pr86230 ](https://github.com/kubernetes/kubernetes/pull/86230)，在 pod 调度过程中，跳过更新 assumed pod 的调度</li></ul> |
| 2019.12.23 | v1.14.3-tke.8 | revert：[pr79036](https://github.com/kubernetes/kubernetes/pull/79036) 解决当开启 cpumanager 时，如果 Pod 的 QoS 为 Guaranteed ，则关闭 cpu quota |
| 2019.12.17 | v1.14.3-tke.7 |<ul class="params"><li>metadata 增加缓存和超时</li> <li> Ubuntu16 下 lxcfs 升级造成 Pod 退出问题修复 </li><li> kubelet 重启避免 readiness 的 pod not ready </li></ul> |
| 2019.11.28 | v1.14.3-tke.6 | cloud-provider 增加将节点名称作为 hostname 的支持 |
| 2019.11.18 | v1.14.3-tke.5 | <ul class="params"><li>合并 [pr83435](https://github.com/kubernetes/kubernetes/pull/83435) 解决攻击者可发送特殊构造的恶意 YAML 或 JSON 攻击载荷导致 kube-apiserver CPU 或内存耗尽无法提供服务的问题</li><li>合并 [pr84167](https://github.com/kubernetes/kubernetes/pull/84167) 解决因为 Etcd key 前缀不正确导致 apiserver 健康检查失败的问题</li><li>合并 [pr75622](https://github.com/kubernetes/kubernetes/pull/75622) 解决当集群存在大量 sts（>2000）工作负载的情况下对 sts 的改变同步到 pod 延迟大（大概20s）的问题</li></ul>|
| 2019.10.23 | v1.14.3-tke.4 |合并 [pr79036](https://github.com/kubernetes/kubernetes/pull/79036) 解决当开启 CPU Manager 时，如果 Pod 的 QoS 为 Guaranteed，则关闭 cpu quota |
| 2019.09.10 | v1.14.3-tke.3       | 合并 [pr63066](https://github.com/kubernetes/kubernetes/pull/63066) 修复 IPVS 模式下负载均衡健康检查失败的问题 |
| 2019.09.06 | v1.14.3-tke.2	   | <ul class="params"><li>解决 [cve-2019-9512&cve-2019-9514](https://discuss.kubernetes.io/t/security-release-of-kubernetes-v1-15-3-v1-14-6-v1-13-10-cve-2019-9512-and-cve-2019-9514/7596) HTTP/2 DDoS 安全漏洞</li><li>合并 [pr72914](https://github.com/kubernetes/kubernetes/pull/72914) 修复删除 Pod 后立即创建并调度到同一个节点上可能导致挂载 volume 失败的问题</li><li>解决在 CentOS 下创建容器会导致 cgroup 泄露的问题</li></ul> |


## TKE kubernetes 1.12.4 revisions

| 时间         | 版本                  | 更新内容                                               |
| ---------- | ------------------- | ----------------------------------------------------- |
| 2020.01.13 | v1.12.4-tke.16 |  <li>合并[ pr2359 ](https://github.com/kubernetes/kubernetes/pull/2359)解决获取不到 docker root 造成的监控缺失问题</li><li> 合并[ pr86583 ](https://github.com/kubernetes/kubernetes/pull/86583)提高 iptables 不支持 random-fully 时的日志输出级别，避免产生过多日志</li><li> kube-scheduler 支持动态设置日志级别</li><li> 绕过 cbs 出现的 device path（/dev/disk/by-id/virtio-xxx/...）缺失的问题，让用户能正常使用 cbs </li><li>合并[ pr86230 ](https://github.com/kubernetes/kubernetes/pull/86230)，在 pod 调度过程中，跳过更新assumed pod 的调度</li> |
| 2019.12.23 | v1.12.4-tke.15 | revert：[pr79036](https://github.com/kubernetes/kubernetes/pull/79036) 解决当开启 cpumanager 时，如果 Pod 的 QoS 为 Guaranteed ，则关闭 cpu quota |
| 2019.12.17 | v1.12.4-tke.14 |<ul class="params"> <li>metadata 增加缓存和超时</li> <li> Ubuntu16 下 lxcfs 升级造成 Pod 退出问题修复 </li><li> kubelet 重启避免 readiness 的 pod not ready </li></ul> |
| 2019.11.28 | v1.12.4-tke.13	 | cloud-provider 增加将节点名称作为 hostname 的支持 |
| 2019.11.18 | v1.12.4-tke.12 |	合并 [pr75622](https://github.com/kubernetes/kubernetes/pull/75622) 解决当集群存在大量 sts（>2000） 工作负载的情况下对 sts 的改变同步到 pod 延迟大（大概20s）的问题 |
| 2019.10.23 | v1.12.4-tke.11 |	<ul class="params"><li>合并 [pr79036](https://github.com/kubernetes/kubernetes/pull/79036) 解决当开启 CPU Manager 时，如果 Pod 的 QoS 为 Guaranteed，则关闭 cpu quota</li><li>合并 [pr72866](https://github.com/kubernetes/kubernetes/pull/72868) 为 kube-proxy 增加`--metrics-port`命令行参数，同时解决`--metrics-bind-address`不能包含 port 的 bug </li></ul> |
| 2019.09.06 | v1.12.4-tke.10      | <ul class="params"><li>解决 [cve-2019-9512&cve-2019-9514](https://discuss.kubernetes.io/t/security-release-of-kubernetes-v1-15-3-v1-14-6-v1-13-10-cve-2019-9512-and-cve-2019-9514/7596) HTTP/2 DDoS 安全漏洞</li><li>合并 [pr72914](https://github.com/kubernetes/kubernetes/pull/72914) 修复删除 Pod 后立即创建并调度到同一个节点上可能导致挂载 volume 失败的问题</li><li>合并  [pr71834](https://github.com/kubernetes/kubernetes/pull/71834) 修复 IPVS 模式下 sessionAffinity为ClientIP 会访问失效 RS 的问题</li></ul> |
| 2019.08.09 | v1.12.4-tke.9       | 解决在 CentOS 下创建容器会导致 cgroup 泄露的问题 |
| 2019.08.08 | v1.12.4-tke.8       | 合并 [pr72118](https://github.com/kubernetes/kubernetes/pull/72118) 解决基于 cbs 的 StatefulSet 重新调度到同一个 node 上时无法挂载的问题 |
| 2019.07.17 | v1.12.4-tke.7       | 合并 [pr75037](https://github.com/kubernetes/kubernetes/pull/75037) 解决 kubectl cp 命令安全隐患 |
| 2019.07.16 | v1.12.4-tke.6	   | 解决 tlinux 内核版本与 IPVS 兼容问题，修复 IPVS 模式下 CLB 健康检查失败的问题 |
| 2019.07.09 | v1.12.4-tke.5	   | 合并 [pr72361](https://github.com/kubernetes/kubernetes/pull/72361) 解决kube-proxy可能发生死锁的问题 |
| 2019.06.25 | v1.12.4-tke.4	   | 解决 tlinux 内核版本与 IPVS 兼容问题 |
| 2019.06.17 | v1.12.4-tke.3	   | 合并 [pr71114](https://github.com/kubernetes/kubernetes/pull/71114) 解决 IPVS 吞吐量问题 |
| 2019.06.04 | v1.12.4-tke.2       | <ul class="params"><li>合并 [pr74755](https://github.com/kubernetes/kubernetes/pull/74755) 解决kubelet hang住的问题</li> <li>合并 [pr69047](https://github.com/kubernetes/kubernetes/pull/69047) 解决向后兼容'node.Spec.Unschedulable'的问题</li><ul class="params"> |


## TKE kubernetes 1.10.5 revisions

| 时间         | 版本                  | 更新内容                                               |
| ---------- | ------------------- | ----------------------------------------------------- |
| 2020.01.13 | v1.10.5-tke.14 |  <li>合并[ pr2359 ](https://github.com/kubernetes/kubernetes/pull/2359)解决获取不到 docker root 造成的监控缺失问题</li><li> 合并[ pr86583 ](https://github.com/kubernetes/kubernetes/pull/86583)提高 iptables 不支持 random-fully 时的日志输出级别，避免产生过多日志</li><li> kube-scheduler 支持动态设置日志级别</li><li> 绕过 cbs 出现的 device path（/dev/disk/by-id/virtio-xxx/...）缺失的问题，让用户能正常使用 cbs </li><li>合并[ pr86230 ](https://github.com/kubernetes/kubernetes/pull/86230)，在 pod 调度过程中，跳过更新assumed pod 的调度</li> |
| 2019.12.23 | v1.12.4-tke.15 | revert：[pr79036](https://github.com/kubernetes/kubernetes/pull/79036) 解决当开启 cpumanager 时，如果 Pod 的 QoS 为 Guaranteed ，则关闭 cpu quota |
| 2019.12.17 | v1.12.4-tke.14 |<ul class="params"> <li>metadata 增加缓存和超时</li> <li> Ubuntu16 下 lxcfs 升级造成 Pod 退出问题修复 </li><li> kubelet 重启避免 readiness 的 pod not ready </li></ul> |
| 2019.12.23 | v1.10.5-tke.13 | revert：[pr79036](https://github.com/kubernetes/kubernetes/pull/79036) 解决当开启 cpumanager 时，如果 Pod 的 QoS 为 Guaranteed ，则关闭 cpu quota |
| 2019.12.13 | v1.10.5-tke.12 |	<ul class="params"> <li> kubelet 检查 externalID 时不 delete node</li> <li> metadata 增加缓存和超时</li><li> Ubuntu16 下 lxcfs 升级造成 Pod 退出问题修复</li><li> kubelet 重启避免 readiness 的 pod not ready</li></ul>|
| 2019.11.18 | v1.10.5-tke.11 | 去掉 kube-controller-manager 的反向探测 |
| 2019.10.23 | v1.10.5-tke.10 |  <ul class="params"><li>合并 [pr79036](https://github.com/kubernetes/kubernetes/pull/79036) 解决当开启 CPU Manager 时，如果 Pod 的 QoS 为 Guaranteed，则关闭 cpu quota</li><li>合并 [pr72866](https://github.com/kubernetes/kubernetes/pull/72868) 为 kube-proxy 增加 `--metrics-port` 命令行参数，同时解决 `--metrics-bind-address` 不能包含 port 的 bug </li></ul> |
| 2019.09.06 | v1.10.5-tke.9       | <ul class="params"><li>解决 [cve-2019-9512&cve-2019-9514](https://discuss.kubernetes.io/t/security-release-of-kubernetes-v1-15-3-v1-14-6-v1-13-10-cve-2019-9512-and-cve-2019-9514/7596) HTTP/2 DDoS 安全漏洞</li><li>合并 [pr72914](https://github.com/kubernetes/kubernetes/pull/72914) 修复删除 Pod 后立即创建并调度到同一个节点上可能导致挂载 volume 失败的问题</li><li>合并 [67430](https://github.com/kubernetes/kubernetes/pull/67430) 解决 updateContainerCPUSet 失败情况下的数据结构回滚</li></ul> |
| 2019.08.08 | v1.10.5-tke.8       | 合并 [pr72118](https://github.com/kubernetes/kubernetes/pull/72118) 解决 kubelet 在 Unmount 后对同一设备立即进行 Mount 报 "resource name may not be empty" 的问题
| 2019.07.17 | v1.10.5-tke.7       | 合并 [pr75037](https://github.com/kubernetes/kubernetes/pull/75037) 解决 kubectl cp 命令安全隐患 |
| 2019.06.25 | v1.10.5-tke.6       | 解决 tlinux 内核版本与 IPVS 兼容问题 |
| 2019.06.17 | v1.10.5-tke.5       | 合并 [pr71114](https://github.com/kubernetes/kubernetes/pull/71114) 解决 IPVS 吞吐量问题 |
| 2019.03.19 | v1.10.5-tke.4       | 合并 [pr65092](https://github.com/kubernetes/kubernetes/pull/65092) 解决 apiserver 处理特定请求时 panic 问题 |
| 2019.02.19 | v1.10.5-tke.3       | 合并 [pr67288](https://github.com/kubernetes/kubernetes/pull/67288) 解决 apiserver 做 proxy 时连接泄漏问题 |
| 2018.09.28 | v1.10.5-tke.2       | 将创建 clb 的逻辑从 controller-manager 移出（通过独立的 service controller 来实现）                                            |
| 2018.09.27 | v1.10.5-tke.1       | backport [pr63321](https://github.com/kubernetes/kubernetes/pull/63321)，解决 pod 中有多个业务容器时 Terminating 时间太长的问题 |
| 2018.09.21 | v1.10.5-qcloud-rev1 | 当 kubelet 更新状态超时，controller-manager 对 kubelet 端口做下探测                                                         |

## TKE kubernetes 1.8.13 revisions

| 时间         | 版本                  | 更新内容                             |
| ---------- | ------------------- | ----------------------------------------|
| 2020.01.13 | v1.8.13-tke.7 |<ul class="params"><li>合并[ pr2359 ](https://github.com/google/cadvisor/pull/2359)解决获取不到 docker root 造成的监控缺失问题<li>绕过 cbs 出现的 device path（/dev/disk/by-id/virtio-xxx/...）缺失的问题，让用户能正常使用cbs</li></ul> |
| 2019.12.13 | v1.8.13-tke.6 |	<ul class="params"> <li> kubelet 检查 externalID 时不 delete node</li> <li> metadata 增加缓存和超时</li><li> Ubuntu16 下 lxcfs 升级造成 Pod 退出问题修复</li><li> kubelet 重启避免 readiness 的 pod not ready</li></ul> |
| 2019.11.18 | v1.8.13-tke.5 | <ul class="params"><li>去掉 kube-controller-manager 的反向探测</li><li>给 cbs pvc 添加了 metric</li></ul> |
| 2018.09.28 | v1.8.13-tke.2       | 将创建 clb 的逻辑从 controller-manager 移出（通过独立的 service controller 来实现）         |
| 2018.09.27 | v1.8.13-tke.1       | <ul class="params"><li>关闭 kmem 统计避免 cgroup 数量泄漏</li><li>减少创建 pod 时触发 resourcequota 冲突</li></ul> |
| 2018.09.21 | v1.8.13-qcloud-rev1 | 当 kubelet 更新状态超时，controller-manager 对 kubelet 端口做下探测                             |

## TKE kubernetes 1.7.8 revisions

| 时间         | 版本                 | 更新内容                           |
| ---------- | ------------------ | ------------------------------------ |
| 2019.12.17 | v1.7.8-tke.4 |<ul class="params"><li>[kubelet 检查 externalID 时不 delete node](https://git.code.oa.com/qc_container_cluster/kubernetes/merge_requests/101)</li> <li>metadata 增加缓存和超时</li> <li> Ubuntu16 下 lxcfs 升级造成 Pod 退出问题修复 </li><li> kubelet 重启避免 readiness 的 pod not ready </li></ul> |
| 2018.09.28 | v1.7.8-tke.2       | 解决 controller-manager 和外部 service controller 冲突问题                |
| 2018.09.27 | v1.7.8-tke.1       | 将创建 clb 的逻辑从 controller-manager 移出（通过独立的 service controller 来实现） |
| 2018.09.21 | v1.7.8-qcloud-rev1 | 当 kubelet 更新状态超时，controller-manager 对 kubelet 端口做下探测             |

<style>
.params{
	margin-bottom:0px!important;
}
</style>

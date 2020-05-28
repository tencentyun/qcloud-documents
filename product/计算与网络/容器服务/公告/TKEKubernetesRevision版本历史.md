
## TKE kubernetes 1.16.3 revisions
<table><thead>
<tr><th width="13%">时间</th><th width="13%">版本</th><th width="74%">更新内容</th></tr>
</thead>
<tbody>
<tr>
    <td>2020.04.20</td>	
    <td>v1.16.3-tke.5</td>	
    <td>合入<a href="https://github.com/kubernetes/kubernetes/pull/69047"> pr69047</a>，解决向后兼容 <code>node.Spec.Unschedulable</code> 的问题（此修复在合入 in-tree cbs 代码时被覆盖了）。</td>
</tr>
<tr>
    <td>2020.04.14</td>
    <td>v1.16.3-tke.4</td>
    <td><ul class="params"><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/87913"> pr87913</a>，修复 CVE-2020-8551：Kubelet DoS 攻击问题。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/87669"> pr87669</a>，修复 CVE-2020-8552：apiserver DoS 攻击问题。</li><li>容器服务支持感知单个 node 可挂载 qcloudcbs 的最大数量（1.12 版本及以上为 maxAttachCount-2，1.10 版本目前默认为18）。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/87467"> pr87467</a>，修复授权用户发送恶意 YAML 导致 kubectl 在解析 YAML 时消耗过多 CPU 问题。</li></ul></td>
</tr>
<tr>
	<td>2020-03-11</td>
	<td>v1.16.3-tke.3</td>
	<td><ul class="params"><li>cbs intree 解决磁盘不存在时继续卸载磁盘，导致大量无效请求的问题。</li> <li>metadata 增加本地缓存。</li></ul></td>
</tr>
<tr>
	<td>2020-02-14</td>
	<td>v1.16.3-tke.2</td>
	<td><ul class="params"><li>合并<a href="https://github.com/google/cadvisor/pull/2359" target="_blank"> pr2359 </a>解决获取不到 docker root 造成的监控缺失问题。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/86583" target="_blank"> pr86583 </a>提高 iptables 不支持 random-fully 时的日志输出级别，避免产生过多日志。</li><li>kube-scheduler 支持动态设置日志级别。</li><li>绕过 cbs 出现的 device path（/dev/disk/by-id/virtio-xxx/...）缺失的问题，让用户能正常使用 cbs。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/86230" target="_blank"> pr86230</a>，在 pod 调度过程中，跳过更新 assumed pod 的调度。</li></ul></td>
</tr>
<tr>
	<td>2020-01-06</td>
	<td>v1.16.3-tke.1</td>
	<td><ul class="params"><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/79036" target="_blank"> pr79036 </a>解决当开启 cpumanager 时，如果 pod 的 QoS 为 Guaranteed，则关闭 cpu quota。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/84167" target="_blank"> pr84167 </a>解决因 ETCD key 前缀不正确导致 apiserver 健康检查失败的问题。</li><li>revert <a href="https://github.com/kubernetes/kubernetes/pull/63066" target="_blank"> pr63066 </a>修复负载均衡健康检查与 IPVS 的问题。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/72914" target="_blank"> pr72914 </a>修复删除 Pod 后立即创建并调度到同一个节点可能导致无法挂载成功的问题。</li><li>解决在 CentOS 下创建容器会导致 cgroup 泄露的问题。</li><li>Ubuntu16 下 lxcfs 升级造成 pod 退出问题修复。</li><li>metadata 增加缓存和超时，cloud-provider 增加将节点名称作为 hostname 的支持。</li><li>revert pr79036 解决当开启 cpumanager 时，如果 pod 的 QoS 为 Guaranteed，则关闭 cpu quota。</li><li>绕过 cbs 出现的 device path（/dev/disk/by-id/virtio-xxx/...）缺失的问题，让用户能正常使用 cbs。</li></ul></td>
</tr>
</tbody></table>

## TKE kubernetes 1.14.3 revisions
<table>
<thead>
<tr><th width="13%">时间</th><th width="13%">版本</th><th width="74%">更新内容</th></tr>
</thead>
<tbody>
<tr>
    <td>2020.04.14</td>
    <td>v1.14.3-tke.11</td>
    <td><ul class="params"><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/75442"> pr75442</a>，将 bandwidth 单位从 Kb 修正为 b。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/86583"> pr87669</a>，修复 CVE-2020-8552：apiserver DoS 攻击问题。</li> <li>容器服务支持感知单个 node 可挂载 qcloudcbs 的最大数量（1.12 版本及以上为 maxAttachCount-2，1.10 版本目前默认为18）。</li></ul></td>
</tr>
<tr>
    <td>2020.04.14</td>
    <td>v1.14.3-tke.10</td>
    <td>cbs intree 解决磁盘不存在时继续卸载磁盘导致大量无效请求的问题。</td>
</tr>
<tr>
	<td>2020-01-13</td>
	<td>v1.14.3-tke.9</td>
	<td><ul class="params"><li> 合并<a href="https://github.com/google/cadvisor/pull/2359" target="_blank"> pr2359 </a>解决获取不到 docker root 造成的监控缺失问题。</li> <li>合并<a href="https://github.com/kubernetes/kubernetes/pull/86583" target="_blank"> pr86583 </a>提高 iptables 不支持 random-fully 时的日志输出级别，避免产生过多日志。</li><li>kube-scheduler 支持动态设置日志级别。</li><li>绕过 cbs 出现的 device path（/dev/disk/by-id/virtio-xxx/...）缺失的问题，让用户能正常使用 cbs。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/86230" target="_blank"> pr86230</a>，在 pod 调度过程中，跳过更新 assumed pod 的调度。</li></ul></td>
</tr>
<tr>
	<td>2019-12-23</td>
	<td>v1.14.3-tke.8</td>
	<td>revert <a href="https://github.com/kubernetes/kubernetes/pull/79036" target="_blank">pr79036</a> 解决当开启 cpumanager 时，如果 Pod 的 QoS 为 Guaranteed ，则关闭 cpu quota。</td>
</tr>
<tr>
	<td>2019-12-17</td>
	<td>v1.14.3-tke.7</td>
	<td><ul class="params"><li>metadata 增加缓存和超时。</li> <li> Ubuntu16 下 lxcfs 升级造成 Pod 退出问题修复。</li><li> kubelet 重启避免 readiness 的 pod not ready。</li></ul></td>
</tr>
<tr>
	<td>2019-11-28</td>
	<td>v1.14.3-tke.6</td>
	<td>cloud-provider 增加将节点名称作为 hostname 的支持。</td>
</tr>
<tr>
	<td>2019-11-18</td>
	<td>v1.14.3-tke.5</td>
	<td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/83435" target="_blank">pr83435</a> 解决攻击者可发送特殊构造的恶意 YAML 或 JSON 攻击载荷导致 kube-apiserver CPU 或内存耗尽无法提供服务的问题。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/84167" target="_blank">pr84167</a> 解决因Etcd key 前缀不正确导致 apiserver 健康检查失败的问题。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/75622" target="_blank">pr75622</a> 解决当集群存在大量 sts（&gt;2000）工作负载的情况下对 sts 的改变同步到 pod 延迟大（大概20s）的问题。</li></ul></td>
</tr>
<tr>
	<td>2019-10-23</td>
	<td>v1.14.3-tke.4</td>
	<td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/79036" target="_blank">pr79036</a> 解决当开启 CPU Manager 时，如果 Pod 的 QoS 为 Guaranteed，则关闭 cpu quota。</td>
</tr>
<tr>
	<td>2019-09-10</td>
	<td>v1.14.3-tke.3</td>
	<td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/63066" target="_blank">pr63066</a> 修复 IPVS 模式下负载均衡健康检查失败的问题。</td>
</tr>
<tr>
	<td>2019-09-06</td>
	<td>v1.14.3-tke.2</td>
	<td><ul class="params"><li>解决 <a href="https://discuss.kubernetes.io/t/security-release-of-kubernetes-v1-15-3-v1-14-6-v1-13-10-cve-2019-9512-and-cve-2019-9514/7596" target="_blank">cve-2019-9512&amp;cve-2019-9514</a> HTTP/2 DDoS 安全漏洞。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/72914" target="_blank">pr72914</a> 修复删除 Pod 后立即创建并调度到同一个节点上可能导致挂载 volume 失败的问题。</li><li>解决在 CentOS 下创建容器会导致 cgroup 泄露的问题。</li></ul></td>
</tr>
</tbody></table>

## TKE kubernetes 1.12.4 revisions

<table>
<thead>
<tr><th width="13%">时间</th><th width="13%">版本</th><th width="74%">更新内容</th></tr>
</thead>
<tbody>
<tr>
    <td>2020.04.14</td>	
    <td>v1.12.4-tke.18</td>
    <td><ul class="params"><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/73401"> pr73401</a>、<a href="https://github.com/kubernetes/kubernetes/pull/73606">pr73606</a>、<a href="https://github.com/kubernetes/kubernetes/pull/76060">pr76060</a>，删除分配到不存在的节点上的 DaemonSet Pod。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/68619"> pr68619</a>，解决 cpumanager 脏数据问题。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/87669"> pr87669</a>，修复 CVE-2020-8552：apiserver DoS 攻击问题。</li><li> 容器服务支持感知单个 node 可挂载 qcloudcbs 的最大数量（1.12 版本及以上为 maxAttachCount-2，1.10 版本目前默认为18）。</li></ul></td>
    </tr>
<tr>
    <td>2020.02.14</td>	
    <td>v1.12.4-tke.17</td>	
    <td><ul class="params"><li> cbs V2 接口升级到 V3。</li><li>cbs intree 解决磁盘不存在时继续卸载磁盘导致大量无效请求的问题。</li></ul></td>
    </tr>
<tr>
	<td>2020-01-13</td>
	<td>v1.12.4-tke.16</td>
	<td><ul class="params"><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/2359" target="_blank"> pr2359 </a>解决获取不到 docker root 造成的监控缺失问题。</li><li> 合并<a href="https://github.com/kubernetes/kubernetes/pull/86583" target="_blank"> pr86583 </a>提高 iptables 不支持 random-fully 时的日志输出级别，避免产生过多日志。</li><li> kube-scheduler 支持动态设置日志级别。</li><li> 绕过 cbs 出现的 device path（/dev/disk/by-id/virtio-xxx/...）缺失的问题，让用户能正常使用 cbs。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/86230" target="_blank"> pr86230</a>，在 pod 调度过程中，跳过更新 assumed pod 的调度。</li></ul></td>
</tr>
<tr>
	<td>2019-12-23</td>
	<td>v1.12.4-tke.15</td>
	<td>revert <a href="https://github.com/kubernetes/kubernetes/pull/79036" target="_blank">pr79036</a> 解决当开启 cpumanager 时，如果 Pod 的 QoS 为 Guaranteed ，则关闭 cpu quota。</td>
</tr>
<tr>
	<td>2019-12-17</td>
	<td>v1.12.4-tke.14</td>
	<td><ul class="params"> <li>metadata 增加缓存和超时。</li> <li> Ubuntu16 下 lxcfs 升级造成 Pod 退出问题修复。 </li><li> kubelet 重启避免 readiness 的 pod not ready。 </li></ul></td>
</tr>
	<tr>
	<td>2019-11-28</td>
	<td>v1.12.4-tke.13</td>
	<td>cloud-provider 增加将节点名称作为 hostname 的支持。</td>
	</tr>
<tr>
	<td>2019-11-18</td>
	<td>v1.12.4-tke.12</td>
	<td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/75622" target="_blank">pr75622</a> 解决当集群存在大量 sts（&gt;2000）工作负载的情况下对 sts 的改变同步到 pod 延迟大（大概20s）的问题。</td>
</tr>
<tr>
	<td>2019-10-23</td>
	<td>v1.12.4-tke.11</td>
	<td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/79036" target="_blank">pr79036</a> 解决当开启 CPU Manager 时，如果 Pod 的 QoS 为 Guaranteed，则关闭 cpu quota。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/72868" target="_blank">pr72866</a> 为 kube-proxy 增加<code>--metrics-port</code>命令行参数，同时解决<code>--metrics-bind-address</code>不能包含 port 的 bug。</li></ul></td>
</tr>
<tr>
	<td>2019-09-06</td>
	<td>v1.12.4-tke.10</td>
	<td><ul class="params"><li>解决 <a href="https://discuss.kubernetes.io/t/security-release-of-kubernetes-v1-15-3-v1-14-6-v1-13-10-cve-2019-9512-and-cve-2019-9514/7596" target="_blank">cve-2019-9512&amp;cve-2019-9514</a> HTTP/2 DDoS 安全漏洞。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/72914" target="_blank">pr72914</a> 修复删除 Pod 后立即创建并调度到同一个节点上可能导致挂载 volume 失败的问题。</li><li>合并  <a href="https://github.com/kubernetes/kubernetes/pull/71834" target="_blank">pr71834</a> 修复 IPVS 模式下 sessionAffinity 为 ClientIP 会访问失效 RS 的问题。</li></ul></td>
</tr>
<tr>
	<td>2019-08-09</td>
	<td>v1.12.4-tke.9</td>
	<td>解决在 CentOS 下创建容器会导致 cgroup 泄露的问题。</td>
</tr>
<tr>
	<td>2019-08-08</td>
	<td>v1.12.4-tke.8</td>
	<td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/72118" target="_blank">pr72118</a> 解决基于 cbs 的 StatefulSet 重新调度到同一个 node 上时无法挂载的问题。</td>
</tr>
<tr>
	<td>2019-07-17</td>
	<td>v1.12.4-tke.7</td>
	<td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/75037" target="_blank">pr75037</a> 解决 kubectl cp 命令安全隐患。</td>
</tr>
<tr>
	<td>2019-07-16</td>
	<td>v1.12.4-tke.6</td>
	<td>解决 tlinux 内核版本与 IPVS 兼容问题，修复 IPVS 模式下负载均衡健康检查失败的问题。</td>
</tr>
<tr>
	<td>2019-07-09</td>
	<td>v1.12.4-tke.5</td>
	<td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/72361" target="_blank">pr72361</a> 解决 kube-proxy 可能发生死锁的问题。</td>
</tr>
<tr>
	<td>2019-06-25</td>
	<td>v1.12.4-tke.4</td>
	<td>解决 tlinux 内核版本与 IPVS 兼容问题。</td>
</tr>
<tr>
	<td>2019-06-17</td>
	<td>v1.12.4-tke.3</td>
	<td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/71114" target="_blank">pr71114</a> 解决 IPVS 吞吐量问题。</td>
</tr>
<tr>
	<td>2019-06-04</td>
	<td>v1.12.4-tke.2</td>
	<td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/74755" target="_blank">pr74755</a> 解决 kubelet hang 住的问题。</li> <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/69047" target="_blank">pr69047</a> 解决向后兼容 <code>node.Spec.Unschedulable</code> 的问题。</li></ul></td>
</tr>
</tbody></table>

## TKE kubernetes 1.10.5 revisions

<table>
<thead>
<tr><th width="13%">时间</th><th width="13%">版本</th><th width="74%">更新内容</th></tr>
</thead>
<tbody>
<tr>
    <td>2020.04.29</td>
	<td>v1.10.5-tke.17</td>
    <td>合并<a href="https://github.com/kubernetes/kubernetes/pull/75622"> pr75622</a>，解决在集群存在大量 sts（>2000）工作负载的情况下，sts 同步到 Pod 延迟大（~20s）的问题。 </td>
    </tr>
<tr>
    <td>2020.04.14</td>
    <td>v1.10.5-tke.16</td>
    <td><ul class="params"><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/68619"> pr68619</a>，解决 cpumanager 脏数据问题。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/87669"> pr87669</a>，修复 CVE-2020-8552：apiserver DoS 攻击问题。</li><li>容器服务支持感知单个 node 可挂载 qcloudcbs 的最大数量（1.12 版本及以上为 maxAttachCount-2，1.10 版本目前默认为18）。</li></ul></td>
    </tr>
<tr>
    <td>2020.02.14</td>	
    <td>v1.10.5-tke.15</td>
    <td><ul class="params"><li> cbs V2 接口升级到 V3。</li><li>cbs intree 解决磁盘不存在时继续卸载磁盘，导致大量无效请求的问题。</li></ul></td>
    </tr>
<tr>
<tr>
	<td>2020-01-13</td>
	<td>v1.10.5-tke.14</td>
	<td><ul class="params"><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/2359" target="_blank"> pr2359 </a>解决获取不到 docker root 造成的监控缺失问题。</li><li> 合并<a href="https://github.com/kubernetes/kubernetes/pull/86583" target="_blank"> pr86583 </a>提高 iptables 不支持 random-fully 时的日志输出级别，避免产生过多日志。</li><li> kube-scheduler 支持动态设置日志级别。</li><li> 绕过 cbs 出现的 device path（/dev/disk/by-id/virtio-xxx/...）缺失的问题，让用户能正常使用 cbs。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/86230" target="_blank"> pr86230</a>，在 pod 调度过程中，跳过更新assumed pod 的调度。</li></ul></td>
</tr>
<tr>
	<td>2019-12-23</td>
	<td>v1.10.5-tke.13</td>
	<td>revert <a href="https://github.com/kubernetes/kubernetes/pull/79036" target="_blank">pr79036</a> 解决当开启 cpumanager 时，如果 Pod 的 QoS 为 Guaranteed ，则关闭 cpu quota。</td>
</tr>
<tr>
	<td>2019-12-13</td>
	<td>v1.10.5-tke.12</td>
	<td><ul class="params"> <li> kubelet 检查 externalID 时不 delete node。</li> <li> metadata 增加缓存和超时。</li><li> Ubuntu16 下 lxcfs 升级造成 Pod 退出问题修复。</li><li> kubelet 重启避免 readiness 的 pod not ready。</li></ul></td>
</tr>
<tr>
	<td>2019-11-18</td>
	<td>v1.10.5-tke.11</td>
	<td>去除 kube-controller-manager 的反向探测。</td>
</tr>
<tr>
	<td>2019-10-23</td>
	<td>v1.10.5-tke.10</td>
	<td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/79036" target="_blank">pr79036</a> 解决当开启 CPU Manager 时，如果 Pod 的 QoS 为 Guaranteed，则关闭 cpu quota。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/72868" target="_blank">pr72866</a> 为 kube-proxy 增加 <code>--metrics-port</code> 命令行参数，同时解决 <code>--metrics-bind-address</code> 不能包含 port 的 bug。 </li></ul></td>
</tr>
<tr>
	<td>2019-09-06</td>
	<td>v1.10.5-tke.9</td>
	<td><ul class="params"><li>解决 <a href="https://discuss.kubernetes.io/t/security-release-of-kubernetes-v1-15-3-v1-14-6-v1-13-10-cve-2019-9512-and-cve-2019-9514/7596" target="_blank">cve-2019-9512&amp;cve-2019-9514</a> HTTP/2 DDoS 安全漏洞。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/72914" target="_blank">pr72914</a> 修复删除 Pod 后立即创建并调度到同一个节点上可能导致挂载 volume 失败的问题。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/67430" target="_blank">67430</a> 解决 updateContainerCPUSet 失败情况下的数据结构回滚。</li></ul></td>
</tr>
<tr>
	<td>2019-08-08</td>
	<td>v1.10.5-tke.8</td>
	<td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/72118" target="_blank">pr72118</a> 解决 kubelet 在 Unmount 后对同一设备立即进行 Mount 报 "resource name may not be empty" 的问题。</td>
</tr>
<tr>
	<td>2019-07-17</td>
	<td>v1.10.5-tke.7</td>
	<td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/75037" target="_blank">pr75037</a> 解决 kubectl cp 命令安全隐患。</td>
</tr>
<tr>
	<td>2019-06-25</td>
	<td>v1.10.5-tke.6</td>
	<td>解决 tlinux 内核版本与 IPVS 兼容问题。</td>
</tr>
<tr>
	<td>2019-06-17</td>
	<td>v1.10.5-tke.5</td>
	<td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/71114" target="_blank">pr71114</a> 解决 IPVS 吞吐量问题。</td>
</tr>
<tr>
	<td>2019-03-19</td>
	<td>v1.10.5-tke.4</td>
	<td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/65092" target="_blank">pr65092</a> 解决 apiserver 处理特定请求时 panic 问题。</td>
</tr>
<tr>
	<td>2019-02-19</td>
	<td>v1.10.5-tke.3</td>
	<td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/67288" target="_blank">pr67288</a> 解决 apiserver 做 proxy 时连接泄漏问题。</td>
</tr>
<tr>
	<td>2018-09-28</td>
	<td>v1.10.5-tke.2</td>
	<td>将创建负载均衡的逻辑从 controller-manager 移出（通过独立的 service controller 来实现）。</td>
</tr>
<tr>
	<td>2018-09-27</td>
	<td>v1.10.5-tke.1</td>
	<td>backport <a href="https://github.com/kubernetes/kubernetes/pull/63321" target="_blank">pr63321</a>，解决 pod 中有多个业务容器时 Terminating 时间太长的问题。</td>
</tr>
<tr>
<td>2018-09-21</td>
<td>v1.10.5-qcloud-rev1</td>
<td>当 kubelet 更新状态超时，controller-manager 对 kubelet 端口做下探测。</td>
</tr>
</tbody></table>                                                

## TKE kubernetes 1.8.13 revisions

<table>
<thead>
<tr><th width="13%">时间</th><th width="13%">版本</th><th width="74%">更新内容</th></tr>
</thead>
<tbody>
<tr>
	<td>2020-01-13</td>
	<td>v1.8.13-tke.7</td>
	<td><ul class="params"><li>合并<a href="https://github.com/google/cadvisor/pull/2359" target="_blank"> pr2359 </a>解决获取不到 docker root 造成的监控缺失问题。</li><li>绕过 cbs 出现的 device path（/dev/disk/by-id/virtio-xxx/...）缺失的问题，让用户能正常使用 cbs。</li></ul></td>
</tr>
<tr>
	<td>2019-12-13</td>
	<td>v1.8.13-tke.6</td>
	<td><ul class="params"> <li> kubelet 检查 externalID 时不 delete node。</li> <li> metadata 增加缓存和超时。</li><li> Ubuntu16 下 lxcfs 升级造成 Pod 退出问题修复。</li><li> kubelet 重启避免 readiness 的 pod not ready。</li></ul></td>
</tr>
<tr>
	<td>2019-11-18</td>
	<td>v1.8.13-tke.5</td>
	<td><ul class="params"><li>去掉 kube-controller-manager 的反向探测。</li><li>cbs pvc 添加 metric。</li></ul></td>
</tr>
<tr>
	<td>2018-09-28</td>
	<td>v1.8.13-tke.2</td>
	<td>将创建负载均衡的逻辑从 controller-manager 移出（通过独立的 service controller 来实现）。</td>
</tr>
<tr>
	<td>2018-09-27</td>
	<td>v1.8.13-tke.1</td>
	<td><ul class="params"><li>关闭 kmem 统计避免 cgroup 数量泄漏。</li><li>减少创建 pod 时触发 resourcequota 冲突。</li></ul></td>
</tr>
<tr>
	<td>2018-09-21</td>
	<td>v1.8.13-qcloud-rev1</td>
	<td>当 kubelet 更新状态超时，controller-manager 对 kubelet 端口做下探测。</td>
</tr>
</tbody></table>

## TKE kubernetes 1.7.8 revisions

<table>
<thead>
<tr><th width="13%">时间</th><th width="13%">版本</th><th width="74%">更新内容</th></tr>
</thead>
<tbody>
<tr>
	<td>2019-12-17</td>
	<td>v1.7.8-tke.4</td>
	<td><ul class="params"><li>kubelet 检查 externalID 时不 delete node。</li> <li>metadata 增加缓存和超时。</li> <li> Ubuntu16 下 lxcfs 升级造成 Pod 退出问题修复。 </li><li> kubelet 重启避免 readiness 的 pod not ready。 </li></ul></td>
</tr>
<tr>
	<td>2018-09-28</td>
	<td>v1.7.8-tke.2</td>
	<td>解决 controller-manager 和外部 service controller 冲突问题。</td>
</tr>
<tr>
	<td>2018-09-27</td>
	<td>v1.7.8-tke.1</td>
	<td>将创建负载均衡的逻辑从 controller-manager 移出（通过独立的 service controller 来实现）。</td>
</tr>
	<tr>
	<td>2018-09-21</td>
	<td>v1.7.8-qcloud-rev1</td>
	<td>当 kubelet 更新状态超时，controller-manager 对 kubelet 端口做下探测。</td>
	</tr>
</tbody></table>

<style>
.params{
	margin-bottom:0px!important;
}
</style>

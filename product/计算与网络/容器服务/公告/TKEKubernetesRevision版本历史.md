## TKE kubernetes 1.20.6 revisions
<table>
  <thead>
    <tr><th> 时间         </th><th> 版本                 </th><th> 更新内容                           </th></tr>
  </thead>
  <tbody>
	<tr><td>2021-12-09</td><td>v1.20.6-tke.9</td><td><li> 优化 EKS 虚拟节点调度及 HPA。(kube-controller-manager,kube-scheduler)</li><li> 修复 EKS 计算 cpu 资源时与前端不一致的问题 。(kube-scheduler)</li></td></tr>
	<tr><td>2021-12-02</td><td>v1.20.6-tke.8</td><td><li>  优化 grpc 日志，避免 kubelet 采集 volume 状态时打印过多日志。（kubelet）</li><li>  避免使用了 cbs 的 Pod 调度到外部 CHC 节点。（kube-scheduler）</li></td></tr>
	<tr><td>2021-11-26</td><td>v1.20.6-tke.7</td><td><li> 添加混合云外部节点支持定制化安装其他 cni。(kube-controller-manager)</li> 
<li> 避免对 Pod Assumed 之后的更新进行不必要的处理。(kube-scheduler)</li> 
<li> 合并 <a href="https://github.com/kubernetes/kubernetes/pull/99336">pr99336</a>，改进 kubelet 启动时节点信息的同步机制。(kubelet)</li> </td></tr>
<tr><td>2021-10-13</td><td>v1.20.6-tke.6</td><td>合并 89465，修复滚动更新时基于 pod 指标的 HPA 错误计算实例个数的问题。(kube-controller-manager)</td></tr>
<tr><td>2021-09-27</td><td>v1.20.6-tke.5</td><td>支持收集 containerd 运行时的磁盘用量指标。(kubelet)</td></tr>
<tr><td>2021-09-23</td><td>v1.20.6-tke.4</td><td><li>修复使用 cgroup v2 时存储指标没有数据的问题。(kubelet)</li>
<li> 修复 <a href="https://github.com/kubernetes/kubernetes/pull/104348">CVE-2021-25741</a>，避免通过软链不合法访问主机文件。(kubelet)</td></tr>
<tr><td>2021-07-19 </td><td> v1.20.6-tke.3</td><td><ul class="params">
<li>从 TKE 集群扩容到 EKS，在批量调度 Pod 时，能正确感知子网剩余 ip，调度正确数量的 Pod 到虚拟节点上。  (kube-scheduler)</li>
<li>移植 upstream 对 kubelet 及 cadvisor 的修改，修复使用 cgroupv2 时指标收集统计的问题。  (kubelet)</li></td></ul></tr>
    <tr><td>2021-06-21 </td><td> v1.20.6-tke.2</td><td>默认开启 CSIMigration 及 CSIMigrationQcloudCbs，以 CSI 方式挂载 CBS 盘。</td></tr>
    <tr><td> 2021-05-25   </td><td> v1.20.6-tke.1</td><td><ul class="params"><li>revert pr63066，修复 LB 健康检查与 IPVS 的问题。（kube-proxy）</li>
<li>合并 pr90260，修复 containerd 集群网络监控缺失问题。（kubelet）</li>
<li>ubuntu16下 lxcfs 升级造成  Pod  退出问题修复。（kubelet）</li>
<li>合并 pr72914，修复删除 Pod 后立即创建并调度到同一个节点可能导致无法挂载成功的问题。（kube-controller-manager）</li>
<li>解决在 CentOS 下创建容器会导致 cgroup 泄露的问题。（kubelet）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/98262" rel="nofollow">pr98262</a>，支持 kube-controller-manager 动态调整日志级别。（kube-controller-manager）</li>
<li>合并 pr97752，修复 describe deployment 时 NewReplicaSet 显示为的问题。（kubectl）</li>
<li>合并 pr94833，修复当 Pod 镜像有多个 tag 时，status 中镜像 tag 不匹配的问题。（kubelet）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/100060" rel="nofollow">pr100060</a>，自动删除孤儿 Pod 遗留的 volume 目录。（kubelet）</li>
<li>kube-controller-manager 支持虚拟节点。（kube-controller-manager）</li>
<li>kube-scheduler 支持混合云扩容到 EKS 时，保留固定数目的本地副本。（kube-scheduler）</li>
<li>支持 cbs csi migration。（kube-controller-manager，kubelet）</li>
<li>合并 pr93260，解决 AWS Credential Provider 导致节点启动变慢的问题。（kubelet）</li>
<li>为调度器增加命令行参数 eks-config-namespace：指定扩容 eks 相关配置所在的 namespace。（kube-scheduler）</li>
<li> TKE支持混合云节点。（kube-controller-manager）</li></ul></td></tr>
  </tbody>
</table>


## TKE kubernetes 1.18.4 revisions

<table><thead>
<tr><th width="13%">时间</th><th width="13%">版本</th><th width="74%">更新内容</th></tr>
</thead>
<tbody>
<tr><td>2021-12-09</td><td>v1.18.4-tke.17</td><td><li> 解决当集群中有大量 volumeattachmant 对象时，kube-controller-manage 访问 api-server 被限频的问题 。(kube-controller-manager)</li><li> 合并 <a href="https://github.com/kubernetes/kubernetes/pull/95650"> PR95650</a>，HPA 计算副本数时忽略已删除 Pod。(kube-controller-manager)</li><li>修复 EKS 计算 cpu 资源时与前端不一致的问题。(kube-scheduler)</li></td></tr>
<tr><td>2021-12-02</td><td>v1.18.4-tke.16</td><td><li>修复调度到虚拟节点时的 bug。(kkube-scheduler)</li><li>优化虚拟节点调度算法。(kube-scheduler)</li></td></tr>
	<tr><td>2021-11-26</td><td>v1.18.4-tke.15</td>
<td><ul class="params"><li> 合并 <a href="https://github.com/kubernetes/kubernetes/pull/96444" target="_blank">pr96444</a>，在同步 RBAC 策略时，如果有错误则返回重试。(kube-apiserver)</li>
	<li> 添加混合云外部节点支持定制化安装其他 cni。(kube-controller-manager)</li>
	<li> 支持云游安卓容器分组绑核需求。(kubelet)</li>
	<li> 支持扩展调度器 Prebind 及 Unreserve 操作。(kube-scheduler)</li>
	<li> 合并 <a href="https://github.com/kubernetes/kubernetes/pull/99336" target="_blank">pr99336</a>，改进 kubelet 启动时节点信息的同步机制。(kubelet)</li>
	<li> 修复 <a href="https://github.com/kubernetes/kubernetes/pull/104340" target="_blank">CVE-2021-25741</a>，避免通过软链不合法访问主机文件。(kubelet)</li>
	<li> 优化 cbs 磁盘创建失败导致调度超时的错误信息。(kube-scheduler)</li>
	<li> 优化 grpc 日志，避免 kubelet 采集 volume 状态时打印过多日志。(kubelet)</li>
	<li> 避免使用了 cbs 的 Pod 调度到外部 CHC 节点。(kube-scheduler)</li></ul></td></tr>
	<tr>
	<tr><td>2021-08-23</td><td>v1.18.4-tke.14</td>
<td><ul class="params"><li>从 TKE 集群扩容到 EKS：支持固定 IP   (kube-scheduler)</li>
	<li>从 TKE 集群扩容到 EKS：当匹配 EKS 固定 IP 时，跳过其他预选策略   (kube-scheduler)</li><li>从 TKE 集群扩容到 EKS：针对 EKS 节点的调度优化 EKS 节点资源感知重调度；EKS 节点优先机型调度；优化了针对 EKS 节点的优选/预选策略   (kube-scheduler)</li>
	<li>记录已加载的 ipvs 内核模块，避免 ipvs 模式时 kube-proxy 崩溃   (kube-proxy)</li>
	<li>写入 cpu manager 状态文件发生错误时，避免 panic   (kubelet)</li></ul></td></tr>
	<tr><td>2021-07-22</td><td>v1.18.4-tke.13</td><td>合并 <a rel="nofollow" href="https://github.com/kubernetes/kubernetes/pull/91859" target="_blank">PR91859</a>，修复 CRD 类型只有一个字母时导致 kube-apiserver panic 的问题   (kube-apiserver)</td></tr>
<tr><td>2021-07-13</td><td>v1.18.4-tke.12</td><td><ul class="params"><li>从 TKE 集群扩容到 EKS：在批量调度 Pod 时，能正确感知子网剩余 IP ，调度正确数量的 Pod 到虚拟节点上   (kube-scheduler)</li>
<li>支持收集 Containerd 运行时的磁盘用量指标   (kubelet)</li><li>缩容时支持指定 Pod   (kube-controller-manager)</li></td></ul></tr>
    <td>2021-06-05</td>	
    <td>v1.18.4-tke.11</td>	
    <td>
TKE 支持混合云节点。（kube-controller-manager）</td>
</tr>
<tr>
    <td>2021-05-14</td>	
    <td>v1.18.4-tke.9</td>	
    <td><ul class="params">
<li>移植 <a href="https://github.com/kubernetes/kubernetes/pull/93370" rel="nofollow">pr93370</a>，支持 CronJobControllerV2。（kube-controller-manager）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/100376" rel="nofollow">pr100376</a>，开启 HTTP/2 健康检查，避免连接丢失后无法恢复的问题。（kube-apiserver，kube-controller-manager，kube-scheduler，kubelet，kube-proxy，kubectl）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/100317" rel="nofollow">pr100317</a>，修复 CVE-2021-25735 节点更新可能绕过 Validating Admission Webhook 的问题。（kube-apiserver）</li>
<li>从 TKE 集群扩容到 EKS 支持 ComputeResource 和 EKS ClusterIP 及 HPA。（kube-controller-manager，kube-scheduler）</li>
</ul></td>
</tr>
<tr>
    <td>2021-04-02</td>	
    <td>v1.18.4-tke.8</td>	
    <td><ul class="params">
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/97752" rel="nofollow">pr97752</a>，修复 describe deployment 时 NewReplicaSet 显示为 <code>&lt;none&gt;</code> 的问题。（kubectl）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/93808" rel="nofollow">pr93808</a>，修复执行 <code>kube-scheduler --version</code> 返回多余信息的问题。（kube-scheduler）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91590" rel="nofollow">pr91590</a>，修复使用 NodePort 类型多协议 Service 时警告端口已分配的问题。（kube-apiserver）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/98262" rel="nofollow">pr98262</a>，支持 kube-controller-manager 动态调整日志级别。（kube-controller-manager）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/95154" rel="nofollow">pr95154</a>，修复 kube-scheduler snapshot 包含删除中的节点的问题。（kube-scheduler）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/95711" rel="nofollow">pr95711</a>，修复 kubectl drain 命令占用 CPU 高的问题。（kubectl）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/96602" rel="nofollow">pr96602</a>，修复时间前后跳变时，apiserver 内存泄漏的问题。（kube-apiserver）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/97023" rel="nofollow">pr97023</a>，在卸载 emptyDir 类型的卷时，删除相关元数据目录。（kubelet）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/97527" rel="nofollow">pr97527</a>，修复  cpumanager 中未同步 map 访问操作的问题。（kubelet）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/100190" rel="nofollow">pr100190</a>，自动删除孤儿 Pod 遗留的 volume 目录。（kubelet）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/92614" rel="nofollow">pr92614</a>，当重启策略为 RestartPolicyOnFailure 的 Pod 所有容器都成功退出时，不再创建新的 Sandbox。（kubelet）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/94833" rel="nofollow">pr94833</a>，修复当 Pod 镜像有多个 tag 时，status 中镜像 tag 不匹配的问题。（kubelet）</li>
	        </ul></td>
</tr>
<tr>
    <td>2020-12-28</td>	
    <td>v1.18.4-tke.6（从本版本起，开始支持 ARM 集群）</li></td>	
    <td><ul class="params">
		<li>为 QcloudCbs 添加 metrics。（kube-controller-manager）</li>
	        <li>修复 mount cbs 盘时查看 serial 值的多余空格问题。（kubelet）</li>
	        </ul></td>
</tr>
<tr>
    <td>2020-12-21</td>	
    <td>v1.18.4-tke.5</td>	
    <td><ul class="params">
		<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/94712">pr94712</a>，修复 CVE-2020-8564 - 当文件格式不正确，logLevel >= 4 时，Docker 配置泄露。（kubelet）</li>
		<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/95316">pr95316</a>，修复 CVE-2020-8565 - 对 CVE-2019-11250 的不完整修复导致的日志 token 泄露。（logLevel >= 9）（kube-apiserver，kubectl）</li>
		<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/95245">pr95245</a>，修复 CVE-2020-8566 - 当 loglevel >= 4 时，Ceph RBD adminSecrets 暴露在日志中。（kube-controller-manager）</li>
		<li>修复重启 kubelet 导致 Pod 就绪检查失败的问题。（kubelet）</li>
		<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/90825">pr90825</a>，解决由于 race condition 可能导致 client-go 中 fifo 队列 Pop 操作卡住，进而导致 pod 一直处于 pending 状态的问题。（kubelet）</li>
		<li>调度器支持虚拟节点。（kube-scheduler）</li>
		<li>kube-controller-manager 支持虚拟节点。（kube-controller-manager）</li>
		<li>根据节点真实机型设置 instance-type 标签，不再固定为 QCLOUD。（kubelet）</li>
		<li>在 OpenAPI 中增加 CBS 部分。（kube-apiserver）</li>
		<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91126">pr91126</a>，修复 Pod 同名但 UID 不同时调度器缓存不一致的问题。（kube-scheduler）</li>
		<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/93387">pr93387</a>，修复调度器中节点缓存信息错乱导致 daemonset pod 无法调度到某些节点的问题。（kube-scheduler）</li>
                <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/89465">pr89465</a>，修复滚动更新时基于 pod 指标的 HPA 错误计算实例个数的问题。（kube-controller-manager）</li>
	        </ul></td>
</tr>
<tr>
    <td>2020-10-13</td>	
    <td>v1.18.4-tke.3</td>	
    <td><ul class="params">
		<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/89629">pr89629</a>，解决 configmap 变更后挂载 subpath 的容器重启永远失败的问题（kubelet）。</li>
	        <li>QcloudCbs 支持 BulkVolumeVerification（kube-controller-manager）。</li>
	        <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/94430">pr94430</a>，修复 client-go reflector 无法检测到 "Too large resource version" 错误的问题（kubelet）。</li></ul></td>
</tr>
<tr>
    <td>2020-08-12</td>	
    <td>v1.18.4-tke.2</td>	
    <td><ul class="params">
		<li> 合并 <a href="https://github.com/kubernetes/kubernetes/pull/93403">pr93403</a>，移去 kubelet 的更新不属于 kubelet 的 Pod Condition 的错误打印信息（kubelet）。</li></ul></td>
</tr>
<tr>
    <td>2020-08-04</td>	
    <td>v1.18.4-tke.1</td>	
    <td><ul class="params"><li>revert <a href="https://github.com/kubernetes/kubernetes/pull/63066">pr63066 </a>修复 LB 健康检查与 IPVS 的问题（kube-proxy）。</li>
    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/93403">pr72914</a>，修复删除 Pod 后立即创建并调度到同一个节点可能导致无法挂载成功的问题（kube-controller-manager）。</li>
    <li>解决在 CentOS 下创建容器会导致 cgroup 泄露的问题（kubelet）。</li>
    <li>Ubuntu16 下 lxcfs 升级造成 Pod 退出问题修复（kubelet）。</li>
    <li>metadata 增加缓存和超时。cloud-provider 增加将节点名称作为 hostname 的支持（kubelet）。</li>
    <li>metadata 增加本地缓存（kubelet）。</li>
    <li>合入 CBS 及相关修复代码（kubelet）。</li>
    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/90260">pr90260</a>，修复 containerd 集群网络监控缺失问题（kubelet）。</li>
    <li>TKE 支持感知单个 node 可挂载 qcloudcbs 的最大数量。1.12版本及以上为 maxAttachCount-2，1.10版本现在默认为18（kube-scheduler）。</li>
    <li>CBS intree 解决磁盘不存在时继续卸载磁盘，导致大量无效请求的问题（kubelet）。</li>
    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/2359">pr2359</a>，解决获取不到 docker root 造成的监控缺失问题（kubelet）。</li>
    <li>kube-scheduler 支持动态设置日志级别（kube-scheduler）。</li>
    <li>绕过 CBS 出现的 device path（/dev/disk/by-id/virtio-xxx/...）缺失的问题，让用户能正常使用 CBS（kubelet）。</li>
    <li>TKE 感知单个 node 可挂载 qcloudcbs 的最大数量，kubelet 侧不去 patch node（kubelet）。</li>
    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/89296">pr89296</a>，不在日志中记录是否启用了 iptables random-fully参数（kube-proxy）。</li>
    <li>修复 aws 问题， <a href="https://github.com/kubernetes/kubernetes/pull/92162">pr92162</a>（kubelet）。</li>
    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91277">pr91277</a>，避免 CLB 健康检查导致 kube-apiserver 产生大量 TLS 握手错误日志的问题（kube-apiserver）。</li>
    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91500">pr91500</a>，修复 KUBERNETES_SERVICE_HOST 环境变量缺失的问题（kubelet）。</li>
    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/92537">92537</a>，修复 client-go reflector 无法从 "Too large resource version" 错误恢复的问题（kube-apiserver、kube-controller-manager、kube-scheduler、kubelet 及 kube-proxy）。</li>
    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/92969">pr92969</a>，修复 CVE-2020-8559从被侵入节点提升权限从而侵入其他节点的问题（kube-apiserver）。</li>
    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/92921">pr92921</a>，修复 CVE-2020-8557通过写入 “/etc/hosts” 耗尽磁盘空间的 DOS 攻击问题（kubelet）。</li></ul></td>
</tr>
</tbody></table>




## TKE kubernetes 1.16.3 revisions
<table><thead>
<tr><th width="13%">时间</th><th width="13%">版本</th><th width="74%">更新内容</th></tr>
</thead>
<tbody>
<tr><td>2021-12-09</td><td>v1.16.3-tke.24</td><td>修复 EKS 本地副本数策略在 statefulset 类型的 Pod 上失效的问题。(kube-scheduler)</td></tr>
<tr><td>2021-12-02</td><td>v1.16.3-tke.23</td><td><li>支持扩展调度器 Prebind 及 Unreserve 操作。(kube-scheduler)</li><li> 避免使用了 cbs 的 Pod 调度到外部 CHC 节点。(kube-scheduler)</li><li> 修复调度到虚拟节点时的 bug。(kube-scheduler)</li></td></tr>
<tr><td>2021-09-03</td><td>v1.16.3-tke.22</td><td>写入 cpu manager 状态文件发生错误时，避免 panic (kubelet)</td></tr><tr><td>2021-08-17</td><td>v1.16.3-tke.21</td><td><ul class="params"><li>针对 EKS 节点的调度优化：针对 EKS 节点的调度优化 EKS 节点资源感知重调度；EKS 节点优先机型调度；优化了针对 EKS 节点的优选 / 预选策略 (kube-scheduler)</li><li>移植 <a rel="nofollow" href="https://github.com/kubernetes/kubernetes/pull/87692" target="_blank">87692</a>，修复调度器 pending_pods 和 schedule_attempts_total 指标没有数据的问题 (kube-scheduler)</li></ul></td></tr><tr><td>2021-07-19</td><td>v1.16.3-tke.20</td><td><ul class="params"><li>移植 <a rel="nofollow" href="https://github.com/kubernetes/kubernetes/pull/87688" target="_blank">87688 </a>及 <a rel="nofollow" href="https://github.com/kubernetes/kubernetes/pull/87693" target="_blank">87693</a>，优化 Node Authorizer 性能 (kube-apiserver)</li><li> 从 TKE 集群扩容到 EKS： 在批量调度 Pod 时，能正确感知子网剩余 IP，调度正确数量的 Pod 到虚拟节点上 (kube-scheduler)</li><li>合并 <a rel="nofollow" href="https://github.com/kubernetes/kubernetes/pull/88507" target="_blank">pr88507</a>，解决更新 Pod 状态时 podIP 和 podIPs 不一致的问题 (kube-apiserver)</li></ul></td></tr>
<tr>
    <td>2021-05-24</td>	
    <td>v1.16.3-tke.17</td>	
    <td><ul class="params">
<li>移植 <a href="https://github.com/kubernetes/kubernetes/pull/93370" rel="nofollow">pr93370</a>，支持 CronJobControllerV2。（kube-controller-manager）</li>
<li>从 TKE 集群扩容到 EKS 支持保留本地副本数。（kube-scheduler） </li>
	        </ul></td>
</tr>	
<tr>
    <td>2021-05-06</td>	
    <td>v1.16.3-tke.16</td>	
    <td><ul class="params">
<li>更新以镜像方式运行 kube-proxy 时的启动方式，自动适配所在节点的 iptables 运行模式，以支持默认使用 nf_tables 模式运行 iptables 的操作系统。</li>
	        </ul></td>
</tr>	
<tr>
    <td>2021-04-14</td>	
    <td>v1.16.3-tke.15</td>	
    <td><ul class="params">
<li> 合并 <a href="https://github.com/kubernetes/kubernetes/pull/97752" rel="nofollow">pr97752</a>，修复 describe deployment 时 NewReplicaSet 显示为 <code>&lt;none&gt;</code> 的问题。（kubectl）</li>
<li> 合并 <a href="https://github.com/kubernetes/kubernetes/pull/92614" rel="nofollow">pr92614</a>，当重启策略为 RestartPolicyOnFailure 的 Pod 所有容器都成功退出时，不再创建新的 Sandbox。（kubelet）</li>
<li> 合并 <a href="https://github.com/kubernetes/kubernetes/pull/91590" rel="nofollow">pr91590</a>，修复使用 NodePort 类型多协议 Service 时警告端口已分配的问题。（kube-apiserver）</li>
<li> 合并 <a href="https://github.com/kubernetes/kubernetes/pull/98262" rel="nofollow">pr98262</a>，支持 kube-controller-manager 动态调整日志级别。（kube-controller-manager）</li>
<li> 合并 <a href="https://github.com/kubernetes/kubernetes/pull/95301" rel="nofollow">pr95301</a>，自动删除孤儿 Pod 遗留的 volume 目录。（kubelet）</li>
	        </ul></td>
</tr>	
<tr>
    <td>2020-12-28</td>	
    <td>v1.16.3-tke.14</td>	
    <td><ul class="params">
		<li>为 QcloudCbs 添加 metrics（kube-controller-manager）。</li>
	        <li>修复 mount cbs 盘时查看 serial 值的多余空格问题（kubelet）。</li>
	        </ul></td>
</tr>		
<tr>
    <td>2020-12-21</td>	
    <td>v1.16.3-tke.13</td>	
    <td><ul class="params">
		<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/94712">pr94712</a>，修复 CVE-2020-8564 - 当文件格式不正确，logLevel >= 4 时，Docker 配置泄露（kubelet）。</li>
		<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/95316">pr95316</a>，修复 CVE-2020-8565 - 对 CVE-2019-11250 的不完整修复导致的日志 token 泄露（logLevel >= 9）（kube-apiserver，kubectl）。</li>
		<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/95245">pr95245</a>，修复 CVE-2020-8566 - 当 loglevel >= 4 时，Ceph RBD adminSecrets 暴露在日志中（kube-controller-manager）。</li>
	        <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/86191">pr86191</a>，修复节点重启时，Pod 可能处于错误状态的问题（kubelet）。</li>
                <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/86140">pr86140</a>，修复 controller manager 没有正确处理超时错误导致扩容的pod无法创建的问题（kube-controller-manager）。</li>
	        <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/90825">pr90825</a>，解决由于 race condition 可能导致 client-go中fifo 队列 Pop 操作卡住，进而导致 pod 一直处于 pending 状态的问题（kubelet）。</li>
	        <li>调度器支持虚拟节点（kube-scheduler）。</li>
		<li>kube-controller-manager 支持虚拟节点（kube-controller-manager）。</li>
		<li>根据节点真实机型设置 instance-type 标签，不再固定为 QCLOUD（kubelet）。</li>
		<li>在 OpenAPI 中增加 CBS 部分（kube-apiserver）。</li>
	        <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/81344">pr81344</a>，修复 CPU Manager 不支持 SourcesReady 的问题（kubelet）。</li>
		<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91126">pr91126</a>，修复 Pod 同名但 UID 不同时调度器缓存不一致的问题（kube-scheduler）。</li>
	        <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/89224">pr89224</a>, 修复 NodeInfo 没有检查导致 kube-scheduler 异常重启的问题（kube-scheduler）。</li>
                <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/89465">pr89465</a>，修复滚动更新时基于 pod 指标的 HPA 错误计算实例个数的问题（kube-controller-manager）。</li>
                </ul></td>
</tr>	    
<tr>
    <td>2020-10-13</td>	
    <td>v1.16.3-tke.11</td>	
    <td><ul class="params">
	    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/92971">pr92971</a>，修复 CVE-2020-8559从被侵入节点提升权限从而侵入其他节点的问题（kube-apiserver）。</li>
	    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/92924">pr92924</a>，修复 CVE-2020-8557通过写入 /etc/hosts 耗尽磁盘空间的 DOS 攻击问题（kubelet）。</li>
	    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/93403">pr93403</a>，移去 kubelet 的更新不属于kubelet 的 Pod Condition 的错误打印信息（kubelet）。</li>
	    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/89629">pr89629</a>，解决 configmap 变更后挂载 subpath 的容器重启永远失败的问题（kubelet）。</li>
	    <li>QcloudCbs支持BulkVolumeVerification（kube-controller-manager）。</li>
	    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/84998">pr84998</a>，解决 node 删除后对应的 node lease 对象可能会被重建造成垃圾数据的问题（kubelet）。</li></ul></td>
</tr>
<tr>
    <td>2020-07-28</td>	
    <td>v1.16.3-tke.10</td>	
    <td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91277">pr91277</a>，避免 CLB 健康检查导致 kube-apiserver 产生大量 TLS 握手错误日志的问题（kube-apiserver）。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91500">pr91500</a>，修复 KUBERNETES_SERVICE_HOST 环境变量缺失的问题（kubelet）。</li></ul></td>
</tr>
<tr>
    <td>2020-06-17</td>	
    <td>v1.16.3-tke.9</td>	
    <td>临时修复 AWS 问题 <a href="https://github.com/kubernetes/kubernetes/issues/92162">pr92162</a>。不再注册 AWS Credential Provider，避免由它引起的节点启动变慢问题。</td>
</tr>
<tr>
    <td>2020-06-11</td>	
    <td>v1.16.3-tke.8</td>	
    <td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/85993">pr85993</a>，支持使用 CNI 结果设置 kubenet 的网关地址。</td>
</tr>
<tr>
    <td>2020-06-10</td>	
    <td>v1.16.3-tke.7</td>	
    <td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/90260">pr90260</a>，修复 containerd 集群网络监控缺失问题。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/89515">pr89515</a>，修复滚动更新时 HPA 错误计算实例个数的问题。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91252">pr91252</a>，忽略其他组件产生的 Pod Condition 更新，以免进行不必要的调度。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/89794">pr89794</a>，清理 kube-controller-manager 的错误日志，避免 CVE-2020-8555 的 Half-Blind SSRF 攻击。</li></ul></td>
</tr>
<tr>
    <td>2020-05-18</td>	
    <td>v1.16.3-tke.6</td>	
    <td>tke 可感知单个 node 可挂载 qcloudcbs 的最大数量，不支持动态获取最大值。</td>
</tr>
<tr>
    <td>2020-04-20</td>	
    <td>v1.16.3-tke.5</td>	
    <td>合入<a href="https://github.com/kubernetes/kubernetes/pull/69047"> pr69047</a>，解决向后兼容 <code>node.Spec.Unschedulable</code> 的问题（此修复在合入 in-tree cbs 代码时被覆盖了）。</td>
</tr>
<tr>
    <td>2020-04-14</td>
    <td>v1.16.3-tke.4</td>
    <td><ul class="params"><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/87913"> pr87913</a>，修复 CVE-2020-8551：Kubelet DoS 攻击问题。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/87669"> pr87669</a>，修复 CVE-2020-8552：apiserver DoS 攻击问题。</li><li>tke 支持感知单个 node 可挂载 qcloudcbs 的最大数量（1.12 版本及以上为 maxAttachCount-2，1.10 版本目前默认为18）。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/87467"> pr87467</a>，修复授权用户发送恶意 YAML 导致 kubectl 在解析 YAML 时消耗过多 CPU 问题。</li></ul></td>
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
<tr><td>2021-12-02</td><td>v1.14.3-tke.23</td><td><li>从 TKE 集群扩容到 EKS，在批量调度 Pod 时，能正确感知子网剩余 ip，调度正确数量的 Pod 到虚拟节点上。(kube-scheduler)</li><li> 针对 EKS 节点的调度优化：EKS 节点资源感知重调度；EKS 节点优先机型调度；优化了针对 EKS 节点的优选/预选策略。(kube-scheduler)</li><li> 支持扩展调度器 Prebind 及 Unreserve 操作。(kube-scheduler)</li><li> 避免使用了 cbs 的 Pod 调度到外部 CHC 节点。(kube-scheduler)</li><li> 修复调度到虚拟节点时的 bug。(kkube-scheduler)</li></td></tr>
<tr>
    <td>2021-05-06</td>	
    <td>v1.14.3-tke.22</td>	
    <td>更新以镜像方式运行 kube-proxy 时的启动方式，自动适配所在节点的 iptables 运行模式，以支持默认使用 nf_tables 模式运行 iptables 的操作系统。</td>
</tr>	
<tr>
    <td>2021-04-14</td>	
    <td>v1.14.3-tke.21</td>	
    <td><ul class="params">
	<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/97752" rel="nofollow">pr97752</a>，修复 describe deployment 时 NewReplicaSet 显示为 <code>&lt;none&gt;</code> 的问题。（kubectl）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/78999" rel="nofollow">pr78999</a>，修复优雅关闭时判断协议的大小写问题。（kube-proxy）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91590" rel="nofollow">pr91590</a>，修复使用 NodePort 类型多协议 Service 时警告端口已分配的问题。（kube-apiserver）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/98262" rel="nofollow">pr98262</a>，支持 kube-controller-manager 动态调整日志级别。（kube-controller-manager）</li>
<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/95301" rel="nofollow">pr95301</a>，自动删除孤儿 Pod 遗留的 volume 目录。（kubelet）</li>
	        </ul></td>
</tr>	
<tr>
    <td>2020-12-28</td>	
    <td>v1.14.3-tke.19</td>	
    <td><ul class="params">
		<li>为 QcloudCbs 添加 metrics（kube-controller-manager）。</li>
	        <li>修复 mount cbs 盘时查看 serial 值的多余空格问题（kubelet）。</li>
	        </ul></td>
</tr>	
<tr>
    <td>2020-12-21</td>	
    <td>v1.14.3-tke.18</td>	
    <td><ul class="params">
		<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/94712">pr94712</a>，修复 CVE-2020-8564 - 当文件格式不正确，logLevel >= 4 时，Docker 配置泄露（kubelet）。</li>
		<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/95316">pr95316</a>，修复 CVE-2020-8565 - 对 CVE-2019-11250 的不完整修复导致的日志 token 泄露（logLevel >= 9）（kube-apiserver，kubectl）。</li>
		<li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/95245">pr95245</a>，修复 CVE-2020-8566 - 当 loglevel >= 4 时，Ceph RBD adminSecrets 暴露在日志中（kube-controller-manager）。</li>
	        <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/86140">pr86140</a>，修复 controller manager 没有正确处理超时错误导致扩容的pod无法创建的问题（kube-controller-manager）。</li>
	        <li>调度器支持虚拟节点（kube-scheduler）。</li>
	        <li>kube-controller-manager 支持虚拟节点（kube-controller-manager）。</li>
		<li>根据节点真实机型设置 instance-type 标签，不再固定为 QCLOUD（kubelet）。</li>
	        <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/79338">pr79338</a>，在 SupportPodPidsLimit 及 SupportNodePidsLimit 都未开启时，不启用 pids cgroup 子系统（kubelet）。</li>
	        <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/89224">pr89224</a>, 修复 NodeInfo 没有检查导致 kube-scheduler 异常重启的问题（kube-scheduler）。</li>
                <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/89465">pr89465</a>，修复滚动更新时基于 pod 指标的 HPA 错误计算实例个数的问题（kube-controller-manager）。</li></ul></td>
</tr>	    
<tr>
    <td>2020-10-13</td>
    <td>v1.14.3-tke.17</td>
    <td><ul class="params">
	    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/74781">pr74781</a>，将 ConfigMap 及 Secret 默认更新策略由 Cache 改为 Watch（kubelet）。</li>
	    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/93403">pr93403</a>，移去 kubelet 的更新中不属于 kubelet 的 Pod Condition 的错误打印信息（kubelet）。</li>
	    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/89629">pr89629</a>，解决 configmap 变更后挂载 subpath 的容器重启永远失败的问题（kubelet）。</li>
	    <li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/8094">pr80942</a>，修复 ipvs 模式下，删除 service 后，规则未删除的问题（kube-proxy）。</li>
            <li>QcloudCbs 支持 BulkVolumeVerification（kube-controller-manager）。</li></ul></td>
</tr>
<tr>
    <td>2020-08-04</td>
    <td>v1.14.3-tke.16</td>
    <td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/78883">pr78883</a>，修复默认会给 pod.spec.container.SecurityContext.ProcMount 增加默认值的 bug。</td>
</tr>
<tr>
    <td>2020-07-28</td>	
    <td>v1.14.3-tke.15</td>	
    <td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/76518">pr76518</a> 及 <a href="https://github.com/kubernetes/kubernetes/pull/82514">pr82514</a>，限制 http 及 exec probe 的返回大小，避免占用大量节点内存（kubelet）。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91277">pr91277</a>，避免 CLB 健康检查导致 kube-apiserver 产生大量 TLS 握手错误日志的问题（kube-apiserver）。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91500">pr91500</a>，修复 KUBERNETES_SERVICE_HOST 环境变量缺失的问题（kubelet）。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/77475">pr77475</a>，修复 Job 数量超过500时，Cronjob 无法调度的问题（kube-controller-manager）。</li></ul></td>
</tr>
<tr>
    <td>2020-06-10</td>	
    <td>v1.14.3-tke.14</td>	
    <td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/85027">pr85027</a>，修复滚动更新时 HPA 错误计算实例个数的问题。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/79708">pr79708</a>，使用 spec.replicas 来计算 HPA 当前副本数量。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91252">pr91252</a>，忽略其他组件产生的 Pod Condition 更新，以免进行不必要的调度。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/89794">pr89794</a>，清理 kube-controller-manager 的错误日志，避免 CVE-2020-8555 的 Half-Blind SSRF 攻击。</li></ul></td>
</tr>
<tr>
    <td>2020-06-04</td>	
    <td>v1.14.3-tke.13</td>	
    <td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/90260">pr90260</a>，修复 containerd 集群网络监控缺失问题。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/79451">pr79451</a>，修复 restartPolicy 为 Never 时 kubelet 创建 SandBox 失败后不重新创建的问题。</li></ul></td>
</tr>
<tr>
    <td>2020-05-18</td>	
    <td>v1.14.3-tke.12</td>	
    <td>tke 可感知单个 node 可挂载 qcloudcbs 的最大数量，不支持动态获取最大值。</td>
</tr>
<tr>
    <td>2020-04-14</td>
    <td>v1.14.3-tke.11</td>
    <td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/75442"> pr75442</a>，将 bandwidth 单位从 Kb 修正为 b。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/86583"> pr87669</a>，修复 CVE-2020-8552：apiserver DoS 攻击问题。</li> <li>tke 支持感知单个 node 可挂载 qcloudcbs 的最大数量（1.12 版本及以上为 maxAttachCount-2，1.10 版本目前默认为18）。</li></ul></td>
</tr>
<tr>
    <td>2020-04-14</td>
    <td>v1.14.3-tke.10</td>
    <td>cbs intree 解决磁盘不存在时继续卸载磁盘导致大量无效请求的问题。</td>
</tr>
<tr>
	<td>2020-01-13</td>
	<td>v1.14.3-tke.9</td>
	<td><ul class="params"><li>合并 <a href="https://github.com/google/cadvisor/pull/2359" target="_blank"> pr2359 </a>解决获取不到 docker root 造成的监控缺失问题。</li> <li>合并<a href="https://github.com/kubernetes/kubernetes/pull/86583" target="_blank"> pr86583 </a>提高 iptables 不支持 random-fully 时的日志输出级别，避免产生过多日志。</li><li>kube-scheduler 支持动态设置日志级别。</li><li>绕过 cbs 出现的 device path（/dev/disk/by-id/virtio-xxx/...）缺失的问题，让用户能正常使用 cbs。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/86230" target="_blank"> pr86230</a>，在 pod 调度过程中，跳过更新 assumed pod 的调度。</li></ul></td>
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
    <td>2021-05-06</td>	
    <td>v1.12.4-tke.28</td>	
    <td>更新以镜像方式运行 kube-proxy 时的启动方式，自动适配所在节点的 iptables 运行模式，以支持默认使用 nf_tables 模式运行 iptables 的操作系统。</td>
</tr>	
<tr>
    <td>2020-12-28</td>	
    <td>v1.12.4-tke.27</td>	
    <td><ul class="params">
		<li>为 QcloudCbs 添加 metrics（kube-controller-manager）。</li>
	        <li>修复 mount cbs 盘时查看 serial 值的多余空格问题（kubelet）。</li>
	        </ul></td>
</tr>	
<tr>
    <td>2020-12-15</td>	
    <td>v1.12.4-tke.26</td>	
    <td>QcloudCbs 支持 BulkVolumeVerification（kube-controller-manager）。</td>
</tr>
<tr>
    <td>2020-11-17</td>	
    <td>v1.12.4-tke.25</td>	
    <td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/79495">pr79495</a>，修复 CRD 有多个版本时导致 webhook 调用失败的问题（kube-apiserver）。</td>
</tr>
<tr>
    <td>2020-10-13</td>
    <td>v1.12.4-tke.24</td>
    <td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/93403">pr93403</a>，移去 kubelet 的更新不属于 kubelet 的 Pod Condition 的错误打印信息（kubelet）。</td>
<tr>
    <td>2020-08-04</td>
    <td>v1.12.4-tke.23</td>
    <td>合并 <a href="https://github.com/kubernetes/kubernetes/pull/78881">pr78881</a>，修复默认会给 pod.spec.container.SecurityContext.ProcMount 增加默认值的 bug。</td>
</tr>
<tr>
    <td>2020-07-28</td>	
    <td>v1.12.4-tke.22</td>	
    <td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91277">pr91277</a>，避免 CLB 健康检查导致 kube-apiserver 产生大量 TLS 握手错误日志的问题（kube-apiserver）。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91500">pr91500</a>，修复 KUBERNETES_SERVICE_HOST 环境变量缺失的问题（kubelet）。</li></ul></td>
</tr>
<tr>
    <td>2020-06-10</td>	
    <td>v1.12.4-tke.21</td>	
    <td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/73915"> pr73915</a>，避免 watcher 收到开始 watch 之前的事件。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91252">pr91252</a>，忽略其他组件产生的 Pod Condition 更新，以免进行不必要的调度。</li><li> 合并 <a href="https://github.com/kubernetes/kubernetes/pull/89794">pr73915</a>，清理 kube-controller-manager 的错误日志，避免 CVE-2020-8555 的 Half-Blind SSRF 攻击。</li></ul></td>
</tr>
<tr>
    <td>2020-06-04</td>
    <td>v1.12.4-tke.20</td>
    <td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/90260"> pr90260</a>，修复 containerd 集群网络监控缺失问题。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/79451">pr79451</a>，修复 restartPolicy 为 Never 时 kubelet 创建 SandBox 失败后不重新创建的问题。</li></td>
<tr>
    <td>2020-05-18</td>	
    <td>v1.12.4-tke.19</td>	
    <td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/77802"> pr77802</a>，Disable graceful termination for UDP traffic。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/68741"> pr68741</a>，解决软链 /var/lib/kubelet 及使用 subpath 时，删除 pod 后主机无法解挂导致挂载点泄露以及 pod 一直 terminating 的问题。</li><li>tke 可感知单个 node 可挂载 qcloudcbs 的最大数量，不支持动态获取最大值。</li></ul></td>
</tr>
<tr>
    <td>2020-04-14</td>	
    <td>v1.12.4-tke.18</td>
    <td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/73401"> pr73401</a>、<a href="https://github.com/kubernetes/kubernetes/pull/73606">pr73606</a>、<a href="https://github.com/kubernetes/kubernetes/pull/76060">pr76060</a>，删除分配到不存在的节点上的 DaemonSet Pod。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/68619"> pr68619</a>，解决 cpumanager 脏数据问题。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/87669"> pr87669</a>，修复 CVE-2020-8552：apiserver DoS 攻击问题。</li><li> tke 支持感知单个 node 可挂载 qcloudcbs 的最大数量（1.12 版本及以上为 maxAttachCount-2，1.10 版本目前默认为18）。</li></ul></td>
    </tr>
<tr>
    <td>2020-02-14</td>	
    <td>v1.12.4-tke.17</td>	
    <td><ul class="params"><li> cbs V2 接口升级到 V3。</li><li>cbs intree 解决磁盘不存在时继续卸载磁盘导致大量无效请求的问题。</li></ul></td>
    </tr>
<tr>
	<td>2020-01-13</td>
	<td>v1.12.4-tke.16</td>
	<td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/2359" target="_blank"> pr2359 </a>解决获取不到 docker root 造成的监控缺失问题。</li><li> 合并 <a href="https://github.com/kubernetes/kubernetes/pull/86583" target="_blank"> pr86583 </a>提高 iptables 不支持 random-fully 时的日志输出级别，避免产生过多日志。</li><li> kube-scheduler 支持动态设置日志级别。</li><li> 绕过 cbs 出现的 device path（/dev/disk/by-id/virtio-xxx/...）缺失的问题，让用户能正常使用 cbs。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/86230" target="_blank"> pr86230</a>，在 pod 调度过程中，跳过更新 assumed pod 的调度。</li></ul></td>
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
    <td>2021-05-06</td>	
    <td>v1.10.5-tke.20</td>	 
    <td>更新以镜像方式运行 kube-proxy 时的启动方式，自动适配所在节点的 iptables 运行模式，以支持默认使用 nf_tables 模式运行 iptables 的操作系统。</td>
<tr>
<tr>
    <td>2020-06-10</td>	
    <td>v1.10.5-tke.19</td>	 
    <td><ul class="params"><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/90260">pr90260</a>，修复 containerd 集群网络监控缺失问题。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/91252">pr91252</a>，忽略其他组件产生的 Pod Condition 更新，以免进行不必要的调度。</li><li>合并 <a href="https://github.com/kubernetes/kubernetes/pull/89794">pr89794</a>，清理 kube-controller-manager 的错误日志，避免 CVE-2020-8555 的 Half-Blind SSRF 攻击。</li></td>
<tr>
    <td>2020-05-18</td>	
    <td>v1.12.4-tke.19</td>	 
    <td>合并<a href="https://github.com/kubernetes/kubernetes/pull/61549"> pr61549</a>，为 mountedPods 缓存增加 volumeSpec 数据，解决多个 pod 使用同一 volume 时无法正常删除的问题。</td>
<tr>
    <td>2020-04-29</td>
	<td>v1.10.5-tke.17</td>
    <td>合并<a href="https://github.com/kubernetes/kubernetes/pull/75622"> pr75622</a>，解决在集群存在大量 sts（>2000）工作负载的情况下，sts 同步到 Pod 延迟大（~20s）的问题。 </td>
    </tr>
<tr>
    <td>2020-04-14</td>
    <td>v1.10.5-tke.16</td>
    <td><ul class="params"><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/68619"> pr68619</a>，解决 cpumanager 脏数据问题。</li><li>合并<a href="https://github.com/kubernetes/kubernetes/pull/87669"> pr87669</a>，修复 CVE-2020-8552：apiserver DoS 攻击问题。</li><li>tke 支持感知单个 node 可挂载 qcloudcbs 的最大数量（1.12 版本及以上为 maxAttachCount-2，1.10 版本目前默认为18）。</li></ul></td>
    </tr>
<tr>
    <td>2020-02-14</td>	
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
<tbody><tr>
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


## 1.18 changes since 1.16
### 重大更新
#### cloud provider 标签功能达到 GA
下列标签被废弃，需要使用新标签。

| 废弃标签 | 新标签 | 
|:---------|:---------|
| `beta.kubernetes.io/instance-type` | `node.kubernetes.io/instance-type` |
| `failure-domain.beta.kubernetes.io/region` |`topology.kubernetes.io/region` |
| `failure-domain.beta.kubernetes.io/zone` | `topology.kubernetes.io/zone` |



#### 卷快照（Volume Snapshot）功能进入 Beta 阶段
VolumeSnapshotDataSource 默认开启。详情请参阅 [releasing CSI volume snapshots to beta](https://kubernetes.io/blog/2019/12/09/kubernetes-1-17-feature-cis-volume-snapshot-beta/)。

#### CSI Migration 进入 Beta 阶段
CSIMigration 默认开启。详情请参阅 [CSI migration going to beta](https://kubernetes.io/blog/2019/12/09/kubernetes-1-17-feature-csi-migration-beta/)。

#### Kubernetes 拓扑管理器迎来 beta 版
拓扑管理器功能（TopologyManager）在1.18中进步 beta，可以让 CPU 与其他设备（例如 SR-IOV-VF）实现 NUMA 对齐，让工作负载支持低延迟的工作场景。在引入拓扑管理器之前，CPU 与设备管理器只能彼此独立地做出资源分配决策，这可能导致在多插座 CPU 系统中得到不理想的资源分配结果，影响延迟敏感应用的性能。

#### Serverside Apply 进入 beta 2阶段
Server-side Apply 在 Kubernetes 在1.16版本被提升到 beta 版，1.18引入第二个 beta 版本（ServerSideApply），此版本会记录和管理所有新K8s 对象字段的变化，确保用户了解资源于何时何处发生变化。

#### IngressClass资源
`IngressClass` 资源描述在 Kubernetes 集群内的一种 Ingress 控制器类型。`Ingress` 资源新增 `ingressClassName` 字段，用于设置使用的 `IngressClass` 控制器名称，替代废弃的 `kubernetes.io/ingress.class` 标注。

### 其他更新
- Node Local DNSCache 达到 GA
- IPv6进入 Beta 阶段
- kubectl debug，Alpha 特性
- Windows CSI support，Alpha 特性
- ImmutableEphemeralVolumes，Alpha 特性，支持不可变 ConfigMap 和 Secret，不刷新对应的 volume
- 以下特性达到 GA
  - ScheduleDaemonSetPods
  - TaintNodesByCondition
  - WatchBookmark
  - NodeLease
  - CSINodeInfo
  - VolumeSubpathEnvExpansion
  - AttachVolumeLimit
  - ResourceQuotaScopeSelectors 
  - VolumePVCDataSource
  - TaintBasedEvictions
  - BlockVolume，CSIBlockVolume
  - Windows RunAsUserName
- 进入 Beta 的特性
  - EndpointSlices：默认关闭
  - CSIMigrationAWS：默认关闭
  - StartupProbe
  - EvenPodsSpread

### 废弃和移除
#### 移除的特性
以下特性被移除，默认开启且不可配置：
- GCERegionalPersistentDisk
- EnableAggregatedDiscoveryTimeout
- PersistentLocalVolumes
- CustomResourceValidation
- CustomResourceSubresources
- CustomResourceWebhookConversion
- CustomResourcePublishOpenAPI
- CustomResourceDefaulting

#### 其他移除
- 移除内置的 cluster role：`system:csi-external-provisioner` 和 `system:csi-external-attacher`

####  废弃的特性和参数
- 废弃默认的 service IP CIDR（`10.0.0.0/24`），必须通过 kube-apiserver 的 `--service-cluster-ip-range` 参数进行设置。
- 废弃 `rbac.authorization.k8s.io/v1alpha1` 和 `rbac.authorization.k8s.io/v1beta1` API 组，计划在1.20版本中移除。请迁移到`rbac.authorization.k8s.io/v1`。
- 废弃 `CSINodeInfo` 特性。该特性已经 GA 并默认开启。

### 参数及其他变更
#### kube-apiserver
- `--encryption-provider-config`：如果配置文件中指定 `cacheSize: 0`，1.18之前的版本会自动设置为缓存1000个 key，1.18会报告配置验证错误；可以设置 cacheSize 为负值来关闭缓存。
-  `--feature-gates`：这些特性默认开启，并不再支持通过命令行设置：`PodPriority`, `TaintNodesByCondition`, `ResourceQuotaScopeSelectors` 及`ScheduleDaemonSetPods` 。
- 不再支持以下资源版本（group version）。
    - `apps/v1beta1` 及 `apps/v1beta2` ，请使用`apps/v1` 。
    - `extensions/v1beta1`下的`daemonsets` ,  `deployments` ,  `replicasets` ，请使用`apps/v1`。
    - ` extensions/v1beta1`下的`networkpolicies`，请使用`networking.k8s.io/v1`。
    - `extensions/v1beta1`下的`podsecuritypolicies `，请使用`policy/v1beta1`。

#### kubelet
  - `--enable-cadvisor-endpoints`：这个参数默认关闭。如果需要访问 cAdvisor v1 Json API，需要明确开启。
  - 废弃参数`--redirect-container-streaming`，并将在后续版本中移除。1.18只支持默认行为（通过kubelet代理streaming请求）。如果设置了`--redirect-container-streaming=true`必须移除。
  - 废弃 metrics endpoint `/metrics/resource/v1alpha1`，请使用`/metrics/resource`。

#### kube-proxy
- 废弃以下两个参数，请使用新的参数：
    - `--healthz-port` -->`--healthz-bind-address`
    - `--metrics-port` --> `--metrics-bind-address`
- 增加特性开关 `EndpointSliceProxying`（默认关闭）来控制是否在 kube-proxy 中启用 EndpointSlices。特性开关 `EndpointSlice` 不再影响 kube-proxy 的行为。
- 增加以下三个参数配置 ipvs 连接的超时：
  - `--ipvs-tcp-timeout`
  - `--ipvs-tcpfin-timeout`
  - `--ipvs-udp-timeout`
- iptables 模式增加 IPv4/IPv6双协议栈支持。

#### kube-scheduler
- 废弃`scheduling_duration_seconds`指标
- `scheduling_algorithm_predicate_evaluation_seconds` --> `framework_extension_point_duration_seconds[extension_point="Filter"]`
    `scheduling_algorithm_priority_evaluation_seconds` --> `framework_extension_point_duration_seconds[extension_point="Score"]`
- 在调度器Policy API中废弃`AlwaysCheckAllPredicates`

#### -enable-profiling参数
为了对齐`kube-apiserver`，`kube-controller-manager`和`kube-scheduler`也[默认开启profiling](https://github.com/kubernetes/kubernetes/pull/88663)。要关闭profiling，需要指定参数`--enable-profiling=false`

#### kubectl
- 移除已废弃的`--include-uninitialized`参数
- `kubectl` 和 `k8s.io/client-go`不再默认使用http://localhost:8080作为apiserver的地址。
- `kubectl run` 支持创建pod，不再支持使用之前已废弃的generator创建其他类型的资源。
- 移除已废弃的`kubectl rolling-update`命令，请使用`rollout`命令
- `–dry-run` 支持3个参数值`client`, `server`, 和`none`。`–dry-run=server`支持这些命令： `apply`, `patch`, `create`, `run`, `annotate`, `label`, `set`, `autoscale`, `drain`, `rollout undo`,  和`expose` 
- 新的`kubectl alpha debug`命令，可以[在pod中附临时的容器进行调试和排查问题](https://github.com/kubernetes/kubernetes/pull/88004)（需要启用1.16引入的`EphemeralContainers`特性）

#### hyperkube
Hyperkube 从 go 代码修改为 bash 脚本。

### Changelogs
[kubernetes 1.18 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#whats-new-major-themes)
[kubernetes 1.17 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#whats-new-major-themes)



## 1.16 chagnes since 1.14
### 重大更新
#### 集群稳定性和可用性改进
裸金属集群工具及HA等生产可用的特性都得到了改进和加强。
kubeadm对HA的支持进入beta阶段，用户可以使用```kubeadm init```和```kubeadm join```命令部署高可用的控制面。证书管理更加稳定和健壮，kubeadm可以在update集群时，在证书到期前无缝更新所有的证书：https://github.com/kubernetes/enhancements/issues/357  https://github.com/kubernetes/enhancements/issues/970

#### CSI持续改进
存储SIG继续致力于内建存储插件迁移到CSI接口，支持内建存储插件的大小调整，内联存储卷等特性，还引入了一些原本Kuebernetes存储子系统中不存在的alpha功能，例如存储卷克隆。
存储卷克隆允许用户在配置新存储卷时，指定另一PVC为"DataSource"。如果底层存储系统支持此项功能并在其CSI驱动程序实现了"CLONE_VOLUME"功能，则新存储卷将成为源存储卷的克隆：https://github.com/kubernetes/enhancements/issues/625
#### 特性
- 达到GA的特性：CRD，Admission Webhook，GCERegionalPersistentDisk, CustomResourcePublishOpenAPI, CustomResourceSubresources, CustomResourceValidation, CustomResourceWebhookConversion
- CSI 规范中支持调整卷大小的功能进入Beta

### 一般更新
- Kubernetes核心代码支持Go模块
- 继续为cloud-provider代码提取和组织进行准备。cloud-provider代码已经被移动至kubernetes/legacy-cloud-providers，以便后续删除与外部使用
- Kubectl get与describe命令支持扩展：https://github.com/kubernetes/enhancements/issues/515
- 节点支持第三方监控插件：https://github.com/kubernetes/enhancements/issues/606
- 发布新的alpha版调度框架，用于开发和管理插件，扩展调度器功能：https://github.com/kubernetes/enhancements/issues/624
- 继续弃用extensions/v1beta1、apps/v1beta1以及apps/v1beta2的API，这些扩展将在1.16版本中被彻底淘汰
- Kubelet增加Topology Manager组件，旨在协调资源分配决策，优化资源分配
- 支持IPv4/IPv6双栈，可以同时给Pod与服务分配v4和v6的地址
- alpha特性API Server网络代理
- 面向云控制器管理器迁移提供更多[扩展选项](https://github.com/kubernetes/enhancements/blob/master/keps/sig-cloud-provider/20190422-cloud-controller-manager-migration.md)
- 弃用extensions/v1beta1、apps/v1beta1以及apps/v1beta2 API

#### 已知问题
* 在1.15版本使用```--log-file```参数会有问题: 日志会被多次写入同一个文件，详情参见：https://github.com/kubernetes/kubernetes/issues/78734#issuecomment-501372131

#### 更新须知
- 集群
    - 这些标签不再在节点上设置： `beta.kubernetes.io/metadata-proxy-ready`, `beta.kubernetes.io/metadata-proxy-ready` 及`beta.kubernetes.io/kube-proxy-ds-ready` 
        * `ip-mask-agent`使用`node.kubernetes.io/masq-agent-ds-ready`作为node选择器，不再使用`beta.kubernetes.io/masq-agent-ds-ready` 
        * `kube-proxy`使用`node.kubernetes.io/kube-proxy-ds-ready`作为node选择器，不再使用`beta.kubernetes.io/kube-proxy-ds-ready` 
        * `metadata-proxy`使用`cloud.google.com/metadata-proxy-ready`作为node选择器，不再使用`beta.kubernetes.io/metadata-proxy-ready` 
* API Machinery
k8s.io/kubernetes和其他发布的组件，包括k8s.io/client-go和k8s.io/api等，现在包含Go模块文件，包括依赖库的版本信息。在以Go模块方式使用k8s.io/client-go时可以参考[go-modules](http://git.k8s.io/client-go/INSTALL.md#go-modules) 以及https://github.com/kubernetes/kubernetes/pull/74877
* Apps
 __hyperkube短别名已从代码中移除__ ，在编译hyperkube docker镜像时会创建这些别名：https://github.com/kubernetes/kubernetes/pull/76953
* Lifecycle
    * 废弃的kubeadm ```v1alpha3```配置被全部移除
    * kube-up.sh不再支持centos和local
* Storage
    * CSI卷不再设置```Node.Status.Volumes.Attached.DevicePath```字段，需要更新以来此字段的外部控制器
    * alpha版本的CRD被移除
    * 默认启用```StorageObjectInUseProtection``` admission[插件](https://github.com/kubernetes/kubernetes/pull/74610)。如果之前没有启用该插件，集群的行为可能会发生变化
    * CSI driver启用PodInfoOnMount后，在volume上下文会增加一个新的参数:`csi.storage.k8s.io/ephemeral`，允许driver在实现NodePublishVolume 时，case by case的判断当前volume是短暂存储还是持久的：https://github.com/kubernetes/kubernetes/pull/79983
    * VolumePVCDataSource（存储卷克隆功能） 进入beta：https://github.com/kubernetes/kubernetes/pull/81792
    * 把内建以及CSI volume的limit合为一个调度器preidicate: https://github.com/kubernetes/kubernetes/pull/77595
* kube-apiserver
    * 废弃参数 `--enable-logs-handler`，计划在v1.19移除
    * 废弃`--basic-auth-file`及相应的认证模式，未来计划移除
    * 废弃默认的service IP CIDR（10.0.0.0/24），计划半年后或者2个release后移除。必须使用`--service-cluster-ip-range`参数来制定service的IP段
* kube-scheduler
    * 使用`v1beta1` Events API。消费scheudler事件的工具需要使用 v1beta1 Event API
* kube-proxy
    * 移除参数`--conntrack-max`，可使用`--conntrack-min`和`--conntrack-max-per-core`来代替
    * 移除参数`--cleanup-iptables`
   * 移除`--resource-container`
* kubelet
    * 移除参数 `--allow-privileged`, `--host-ipc-sources`, `--host-pid-sources`,`--host-network-sources`，可以使用`PodSecurityPolicy`的准入控制器来代替
    * 废弃cAdvisor JSON接口
    * 移除`--containerized`
    * 不再支持通过`--node-labels`参数设置`kubernetes.io-`或`k8s.io-`为前缀的不被允许的标签
* kubectl
    * 移除`kubectl scale job`
    * 移除```kubectl exec```命令的```--pod/-p```参数
    * 移除`kubectl convert`命令
    * 移除`--include-uninitialized`
    * `kubectl cp`不再支持复制容器中的符号链接，可以使用如下命令代替：
local to pod: `tar cf - /tmp/foo | kubectl exec -i -n <some-namespace> <some-pod> -- tar xf - -C /tmp/bar`
pod to local: `kubectl exec -n <some-namespace> <some-pod> -- tar cf - /tmp/foo | tar xf - -C /tmp/bar`
* kubeadm
    * 废弃命令`kubeadm upgrade node config` `kubeadm upgrade node experimental-control-plane`，使用`kubeadm upgrade node`代替
    * 废弃参数`--experimental-control-plane`，使用 `--control-plane`代替
    * 废弃参数`--experimental-upload-certs`，使用 `--upload-certs`代替
    * 废弃命令`kubeadm config upload`，使用`kubeadm init phase upload-confi`代替
    * CoreDNS使用ready插件进行就绪检查
    * 废弃`proxy`插件，使用`forward`插件来代替
    * `kubernetes`插件移除`resyncperiod`选项
    * 废弃`upstream`选项，如果指定，将被忽略

### Changelogs
[kubernetes 1.16 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#whats-new-major-themes)
[kubernetes 1.15 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#whats-new-major-themes)



## 1.14 changes since 1.12
### 重大更新
* Container Storage Interface 进入 GA: https://github.com/kubernetes/kubernetes/pull/71020
* CoreDNS 替换 kube-dns 成为默认 DNS Server: https://github.com/kubernetes/kubernetes/pull/69883
* 使用 kubeadm 简化集群管理
* 支持 Windows Nodes 进入 stable: https://github.com/kubernetes/enhancements/issues/116
* 本地存储进入 GA: https://github.com/kubernetes/enhancements/issues/121#issuecomment-457396290
* Pid Limiting 进入 beta: http://github.com/kubernetes/kubernetes/pull/73651
* 支持 Pod Priority 和 Preemption: https://github.com/kubernetes/enhancements/issues/564

### 一般更新
* dry-run 进入 beta。dry-run 使用户可以模拟真实 API 请求，而不实际改变集群状态
* kubectl diff 进入 beta
* kubectl 插件注册进入 stable
* kubelet 插件机制进入 beta
* CSIPersistentVolume 进入 GA
* TaintBasedEviction 进入 beta
* kube-scheduler 可感知 volume topology，进入 stable
* 支持 out-of-tree CSI Volume plugins，进入 stable
* 支持第三方设备监控插件
* kube-scheduler subnet feasibility 进入 beta
* Pod Ready 支持自定义探测条件
* Node 内存支持 HugePage
* RuntimeClass 进入 beta
* Node OS/Arch labels 进入 GA
* node-leases 进入 beta
* kubelet resource metrics endpoint 进入 alpha，支持通过 prometheus 采集数据
* runAsGroup 进入 beta
* kubectl apply server-side 进入 alpha，可在服务端执行 apply 操作
* kubectl 支持 kustomize
* 支持在 pod 中配置 resolv.conf
* CSI volumes 支持 resizing
* CSI 支持 topology
* volume mount 支持设定子路径参数
* CSI 支持裸块设备
* CSI 支持本地 ephemeral volume

### 更新须知
* kube-apiserver
    * 不再支持 `etcd2`，默认 `--storage-backend=etcd3`
    * 废弃参数 `--etcd-quorum-read`
    * 废弃参数 `--storage-versions`
    * 废弃参数 `--repair-malformed-updates`
* kube-controller-manager
    * 废弃参数 `--insecure-experimental-approve-all-kubelet-csrs-for-group`
* kubelet
    * 废弃参数 `--google-json-key` 
    * 废弃参数 `--experimental-fail-swap-on`
* kube-scheduler
    * 不再支持 `componentconfig/v1alpha1`
* kubectl
    * 不再支持命令 `run-container` 
* taints
    * `node.alpha.kubernetes.io/notReady` 和 `node.alpha.kubernetes.io/unreachable` 不再支持，改为 `node.kubernetes.io/not-ready` 和 `node.kubernetes.io/unreachable`

### Changelogs
[kubernetes 1.14 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#kubernetes-v114-release-notes)
[kubernetes 1.13 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.13.md#kubernetes-113-release-notes)

## 1.12 changes since 1.10
### 重大更新
#### API
- CustomResources子资源现在进入 beta 阶段，并默认开启，可以对`/status`子资源更新除了 `.status` 字段（之前只允许对 .spec 和 .metadata 进行更新）。在启用`/status`子资源 时， `required` 和 `rescription`可用于 CRD OpenAPI验证schema。 另外，用户可以创建多个版本的 CustomResourceDefinitions，不需进行自动转换。可以通过CustomResourceDefinitions的`spec.additionalPrinterColumns`字段让`kubectl get`的输出包含额外的列。

- 支持`dry run`功能，允许用户可以看到某些命令的执行结果，而不需要真正提交相关的更改。

#### 认证授权
- RBAC聚合ClusterRoles进入GA阶段，client-go credentials插件进入Beta阶段，支持从外部插件获取TLS认证信息。
- 审计事件增加了如下注解，用户可以更清晰的了解审计决策的过程：
  * Authorization组件会设置`authorization.k8s.io/decision`(authorization决定allow 或 forbid)，及`authorization.k8s.io/reason`(做出这个决定的原因)
  * PodSecurityPolicy准入控制器会设置`podsecuritypolicy.admission.k8s.io/admit-policy`和`podsecuritypolicy.admission.k8s.io/validate-policy`，包含允许Pod准入相关的策略名称（PodSecurityPolicy同时可以限制hostPath类型的挂载点为只读模式）
- NodeRestriction准入控制器会禁止节点修改其对应的Node对象的污点信息，让用户更容易控制和追踪节点的污点设置情况

#### CLI命令行
CLI实现了新的插件机制，并提供了包含通用CLI工具的开发库方便插件开发者进行插件开发

#### 网络
- ipvs模式进入GA
- CoreDNS进入GA，代替kube-dns

#### 节点
- DynamicKubeletConfig进入Beta阶段
- cri-tools GA
- PodShareProcessNamespace进步Beta阶段
- 新增Alpha特性：RuntimeClass，CustomCFSQuotaPeriod 

#### 调度器
- Pod Priority及Preemption进入Beta阶段
- DaemonSet Pod的调度不再由DaemonSet控制器管理，而由默认调度器管理
- TaintNodeByCondition进步Beta阶段
- 默认开启本地镜像优选功能。在调度Pod时，本地已经拉取全部或者部分Pod所需镜像的节点会有更高的优先级，这样可以加速Pod启动

### 一般更新
- 进入GA的特性：ClusterRole，StorageObjectInUseProtection
- 进入Beta的特性：外部Cloud Provider

### 更新须知
- kube-apiserver
  - `--storage-version`参数被移除，由`--storage-versions`代替；同时`--storage-versions`也被废弃
  - `--endpoint-reconciler-type`默认值改为`lease`
  - 使用`--enable-admission-plugins`时，默认包含；使用`--admission-control`参数时，需要显示指定
- kubelet
  - 废弃`--rotate-certificates`参数，由配置文件的.RotateCertificates字段代替
- kubectl
  - 除`run-pod/v1`外，其他`kubectl run`的generator已废弃
  - `kubectl logs`移除`--interactive`参数
  - `--use-openapi-print-columns`已废弃，由`--server-print`代替

### Changelogs
[kubernetes 1.12 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.12.md#major-themes)
[kubernetes 1.11 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.11.md#kubernetes-111-release-notes)

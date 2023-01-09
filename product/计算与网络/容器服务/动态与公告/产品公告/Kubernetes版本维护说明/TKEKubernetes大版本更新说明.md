## 1.22 changes since 1.20
### 重大更新
#### PodSecurityPolicy 被废弃
PodSecurityPolicy 在1.21被废弃，未来会在1.25中移除。可以评估和迁移到 Pod Security Admission 或者第三方的准入插件。

#### 不可变 Secrets 和 ConfigMaps GA
Secret 或者 ConfigMap 被设置为不可变后（`immutable: true`），kubelet 不再 watch 这些对象的变化并重新挂载到容器内，可以降低 apiserver 的负载。该特性在1.21进入 GA。

#### CronJobs GA
CronJobs 在1.21进入 GA（batch/v1），并且默认启用性能更好的新版本控制器 CronJobControllerV2。

#### IPv4/IPv6 双栈支持进入 Beta
双栈网络允许 Pod、服务和节点可以获得 IPv4 及 IPv6 地址，在1.21中，双栈网络从 alpha 升级到 beta，并默认启用。

#### 优雅节点关闭
该特性1.21进入 beta 阶段，允许在关闭节点时，通知 kubelet，优雅终止节点上的 Pod。

#### 持久卷健康监控
1.21引入该 alpha 特性，允许对 PV 进行监视，掌握卷的运行状况，在卷变得不健康时进行标记，此时工作负载可以作出反应，避免数据从不健康的卷上写入或读取。

#### Server-side Apply GA
Server-side Apply 通过声明式配置帮助用户及控制器管理资源，包括以声明方式创建或修改对象等。Server-side Apply 在1.22进入进入 GA 阶段。

#### 外部凭证 GA
从1.22开始，外部凭证进入 GA 阶段，对交互式登录流程插件提供更好的支持，更多信息可以参考 [sample-exec-plugin](https://github.com/ankeesler/sample-exec-plugin)。

#### ETCD 更新至3.5.0
1.22默认使用 ETCD 3.5.0版本，该版本改进了安全性、性能、监控以及开发者体验，修复了多个 bug，以及结构化日志记录、内置日志轮转等重要新功能。

#### MemoryQoS
1.22开始支持 alpha 版本的 MemoryQoS 特性，开启后，将使用 Cgroups v2 API 管理和控制内存分配与隔离，在内存资源发生竞争时，保障工作负载的内存使用，提高工作负载与节点的可用性。该特性由腾讯云提出并贡献给社区。

#### 集群的 seccomp 默认配置
1.22为 kubelet 引入了 `SeccompDefault` alpha 特性，结合 `--seccomp-default` 参数及配置，kubelet 将使用 `RuntimeDefault` seccomp 配置，而不是 `Unconfined`，从而提高工作负载的安全性。

### 其他更新
- GA 的特性：
	- 1.21: EndpointSlice,Sysctls,PodDisruptionBudget
	- 1.22: CSIServiceAccountToken
- 进入 Beta 的特性：
	- 1.21: TTLAfterFinished
	- 1.22: SuspendJob,PodDeletionCost,NetworkPolicyEndPort
- 1.22引入了新的调度器打分插件 `NodeResourcesFit`，用于代替 `NodeResourcesLeastAllocated`， `NodeResourcesMostAllocated`，`RequestedToCapacityRatio` 这三个插件。
- 从1.22起，开启 alpha 特性 `APIServerTracing` 后，apiserver 支持分布式追踪；支持通过`--service-account-issuer` 参数设置多个 issuer，在变更 issuer 时，可以提供不间断服务。

### 废弃和移除
#### 移除的参数及功能
1. Service TopologyKeys 被废弃，可以使用 Topology Aware Hints。
2. kube-proxy
	- 从1.21开始，在 ipvs 模式时，不再自动设置 `net.ipv4.conf.all.route_localnet=1`。升级的节点会保留 `net.ipv4.conf.all.route_localnet=1`，但是新节点继承系统默认值（一般为0）。
	- 删除了 `--cleanup-ipvs` 参数；可以使用 `--cleanup` 参数。
3. kube-controller-manager
	- 从1.22开始，`--horizontal-pod-autoscaler-use-rest-clients` 参数被移除。
	- `--port` 及`--address` 参数不再起作用，将在 1.24 版本中被移除。
4. kube-scheduler：`--hard-pod-affinity-symmetric-weight` 及`--scheduler-name` 参数从1.22开始被移除，可使用 config 文件进行配置。
5. kubelet：`DynamicKubeletConfig` 特性被废弃，并被默认关闭，启动 kubelet 如配置了`--dynamic-config-dir` 参数，将收到告警。

#### 移除或废弃的版本
1. CronJob batch/v2alpha1 版本从1.21开始被移除
2. 从1.22开始以下类型的 Beta API 被移除：详情请参见 [Kubernetes 官网文档](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-22)。
	- rbac.authorization.k8s.io/v1beta1
	- admissionregistration.k8s.io/v1beta1
	- apiextensions.k8s.io/v1beta1
	- apiregistration.k8s.io/v1beta1
	- authentication.k8s.io/v1beta1
	- authorization.k8s.io/v1beta1
	- certificates.k8s.io/v1beta1
	- coordination.k8s.io/v1beta1
	- extensions/v1beta1 及 networking.k8s.io/v1beta1 ingress API

### Changelogs
- [kubernetes1.22changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#whats-new-major-themes)
- [kubernetes1.21changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.21.md#whats-new-major-themes)


## 1.20 changes since 1.18
### 重大更新
#### 新版 CronJob 控制器
1.20 引入了新版的 CronJob 控制器，使用 informer 机制来代替原来的轮询，优化了性能。可以在 `kube-controller-manager` 指定 `--feature-gates="CronJobControllerV2=true"` 来开启。在以后的版本中，会默认使用新版的控制器。

#### 弃用 dockershim
Dockershim 已经正式被弃用。kubernetes 对 Docker 的支持已弃用，将在将来的版本中删除。Docker 生成的遵循 OCI 规范的镜像可以继续在兼容 CRI 的运行时中运行。
更多信息可以参考：[Don't Panic: Kubernetes and Docker](https://kubernetes.io/blog/2020/12/02/dont-panic-kubernetes-and-docker/) , [Dockershim Deprecation FAQ](https://blog.k8s.io/2020/12/02/dockershim-faq/)
#### 结构化日志
对日志消息和 k8s 对象引用的结构都进行了标准化，让日志解析，处理，存储，查询和分析变得更加简单。klog 增加了两个方法来支持结构化日志： `InfoS`  ,  `ErrorS` 。
所有组件增加 `--logging-format` 参数，默认值是 `text` ，保持之前的格式。设置为 `json` 支持结构化日志，此时这些参数不再起作用：--add_dir_header, --alsologtostderr, --log_backtrace_at, --log_dir, --log_file, --log_file_max_size, --logtostderr, --skip_headers, --skip_log_headers, --stderrthreshold, --vmodule, --log-flush-frequency
#### Exec 探测的超时处理
有关 Exec 探测超时的一个长期存在的 bug 已修复，该 bug 可能会影响现有 Pod 定义。在此修复之前，timeoutSeconds 字段指定的超时并未被遵从，相反，探测器将无限期地运行，甚至超过其配置的截止时间，直到返回结果。在本次更改之后，如果未指定值，则探针仅默认应用 1 秒。如果执行探针耗费的时间超过 1 秒，那么现有的 Pod 定义就可能需要修改，显示指定 timeoutSeconds 字段。本次修复还添加了名为 `ExecProbeTimeout` 的开关，允许保留之前的行为（在后续发行版中，此功能将被锁定及删除）。要保留之前的行为，需要把 `ExecProbeTimeout` 设置为 `false` 。
更多信息，可以参考 [Configure Liveness, Readiness and Startup Probes - Configure Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#configure-probes)
#### 卷快照操作功能 GA
此功能提供了一种触发卷快照操作的标准方法，并允许用户以可移植的方式在任何 Kubernetes 环境和支持的存储 provider 上进行合并快照的操作。
此外，这些 Kubernetes 快照原语可以作为基础，解锁为 Kubernetes 开发高级企业级存储管理功能（包括应用程序或集群级备份解决方案）的能力。
请注意，快照支持需要 Kubernetes 集群部署快照控制器、快照 CRD 和验证 Webhook，以及支持快照功能的 CSI 驱动。

#### kubectl debug 进入 beta 阶段
 `kubectl alpha debug` 命令进入 beta 阶段，并被替换为 `kubectl debug` 。该功能支持直接从 kubectl 进行常见的调试工作，包括：
- 使用其他容器镜像或命令来创建 Pod 的副本，对启动时崩溃的工作负载进行故障排除。
- 通过在 Pod 新副本中或临时容器中，添加包含调试工具的新容器的方式，对 distroless 等不包含调试工具的容器进行故障排除。（临时容器 `EphemeralContainers` 是 Alpha 功能，默认未启用）
- 通过创建在主机命名空间中运行的容器并访问主机的文件系统，就可以在节点上排除故障。
请注意，作为新的内置命令，kubectl debug 优先于任何名为 "debug" 的 kubectl 插件，必须重命名受影响的插件。
 `kubectl alpha debug` 已弃用，并将在随后的版本中删除，需要替换为 `kubectl debug` 。更多信息，可以参考 [Debug Running Pods](https://kubernetes.io/docs/tasks/debug-application-cluster/debug-running-pod/)
 
#### API 优先级和公平性功能（API Priority and Fairness）进入 beta 阶段
1.18 引入的 API Priority and Fairness 功能，将在 1.20 版本默认启用，允许 `kube-apiserver` 按优先级对传入的请求进行分类。
#### PID 资源限制功能 GA
 `SupportNodePidsLimit`  （节点到 Pod 的 PID 隔离）和  `SupportPodPidsLimit`  （ 限制每个 Pod 的 PID 的能力）都已经到了 GA 阶段。
 
#### alpha 功能：节点优雅关机
用户和集群管理员都希望 Pod 将遵循预期的 Pod 生命周期，包括 Pod 的终止。但是当节点关机时，Pod 不遵循预期的 Pod 终止生命周期，并且不会正常终止，这可能会导致工作负载的某些问题。1.20 增加了 alpha 的  `GracefulNodeShutdown`  功能，使得 kubelet 能 监听到节点的系统关机事件，从而在系统关闭期间优雅终止 Pod。

#### CSIVolumeFSGroupPolicy 进入 beta 阶段
CSIDrivers 可以使用 `fsGroupPolicy` 字段来控制是否支持在 mount 时修改属主和权限。（ReadWriteOnceWithFSType，File，None）

#### ConfigurableFSGroupPolicy 进入 beta 阶段
支持非递归设置 fsgroup -  `PodFSGroupChangePolicy`  =  `OnRootMismatch`

### 其他更新
- 新增 cloud controller manager 组件。
- 达到 GA 的特性：
  - [RuntimeClass](https://github.com/kubernetes/enhancements/issues/585)
 `node.k8s.io/v1beta1` 被废弃，请使用 `node.k8s.io/v1` 
  - [内置 API 类型的默认值](https://github.com/kubernetes/enhancements/issues/1929)
  - [StartupProbe](https://github.com/kubernetes/enhancements/issues/950)
  - [Services 及 Endpoints 支持 AppProtocol 字段](https://github.com/kubernetes/enhancements/issues/1507)
  - [TokenRequest 及 TokenRequestProjection](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection)
  - SCTPSupport
  - Windows containerd 支持
  - Ingress
  废弃 `networking.k8s.io/v1beta1` （计划在 1.22 版本移除），由 `networking.k8s.io/v1` 代替。
  - seccomp
  seccomp 相关的注解  `seccomp.security.alpha.kubernetes.io/pod`  及  `container.seccomp.security.alpha.kubernetes.io/...` 被废弃（计划在 1.22 版本移除），可以直接在 Pod 及 container spec 中指定如下字段：
```
securityContext:
  seccompProfile:
    type: RuntimeDefault|Localhost|Unconfined ## choose one of the three
    localhostProfile: my-profiles/profile-allow.json ## only necessary if type == Localhost
```
  K8s 会自动转换注解和字段，不需要采取额外的操作来进行转换。
  - [节点证书自动轮换](https://github.com/kubernetes/enhancements/issues/266)
  - [限制节点 API 访问权限](https://github.com/kubernetes/enhancements/issues/279)
  Node 认证模式相关的特性全部实现。
  - [重构 Event API](https://github.com/kubernetes/enhancements/issues/383)
  为了缓解 Event 对系统性能的影响，以及增加更多字段以提供更有用的信息，对 Event API 进行了重新设计。这项工作在 1.19 完成。
  - [CertificateSigningRequest API](https://github.com/kubernetes/enhancements/issues/1513)
  除了之前的 `certificates.k8s.io/v1beta1` ，为 CertificateSigningRequest 新增版本 `certificates.k8s.io/v1` 。在使用 `certificates.k8s.io/v1` 时，
    - 必须指定 `spec.signerName` ，并且不可再使用 `kubernetes.io/legacy-unknown` 。
    - 必须指定 `spec.usages` ，不能包含重复值，并且取值只能是已知 usage。
    - 必须指定 `status.conditions[*].status` 。
    -  `status.certificate` 必须是 PEM 编码，并且只包含 `CERTIFICATE` 块。
- 进入 Beta 的特性：
以下特性进入 Beta 阶段，并默认启用。
  - EndpointSliceProxying
  kube-proxy 从 EndpointSlices 读取信息，而不再是 Endpoints，这可以很大程度上改善大集群的扩展性，并且为以后增加新特性提供了方便（例如拓扑感知路由）
  - KubeSchedulerConfiguration
  - HugePageStorageMediumSize
  - ImmutableEphemeralVolumes
  Secret 和 ConfigMap 卷可以标记为 immutable，在有大量 Secret 和 ConfigMap 卷时，可以大大减少对 apiserver 的压力
  - NodeDisruptionExclusion
  - NonPreemptingPriority
  - ServiceNodeExclusion
  - [RootCAConfigMap](https://github.com/kubernetes/enhancements/blob/master/keps/sig-auth/1205-bound-service-account-tokens/README.md)
  - [调度器中的 Pod 资源指标](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/#kube-scheduler-metrics)
  - ServiceAccountIssuerDiscovery

### 废弃和移除
#### 废弃版本

|废弃版本 |新版本 |
|:--|--|
|apiextensions.k8s.io/v1beta1 |apiextensions.k8s.io/v1 |
|apiregistration.k8s.io/v1beta1 |apiregistration.k8s.io/v1 |
|authentication.k8s.io/v1beta1 |authentication.k8s.io/v1 |
|authorization.k8s.io/v1beta1 |authorization.k8s.io/v1 |
|autoscaling/v2beta1 |autoscaling/v2beta2 |
|coordination.k8s.io/v1beta1 |oordination.k8s.io/v1 |
|storage.k8s.io/v1beta1 |storage.k8s.io/v1 |

#### kube-apiserver
1.  `componentstatus`  API 被废弃。这个 API 用来提供 etcd, kube-scheduler, 和 kube-controller-manager 的运行状态，但只在这些条件下才能工作：这些组件跟 apiserver 运行在一个节点，并且 kube-scheduler 和 kube-controller-manager 暴露了非安全的健康检查端口。
废弃这个 API 后，etcd 的健康检查被包含在 kube-apiserver 的健康检查中，kube-scheduler/kube-controller-manager 可以检查各自的健康检查接口。
2. apiserver 不再监听非安全端口。
 `--address` 及  `--insecure-bind-address`  参数可以设置但无效果； `--port` 及 `--insecure-port` 参数只能设置为 0。这些参数将在 1.24 版本移除。
3.  `TokenRequest`  及  `TokenRequestProjection` 进入 GA，kube-apiserver 需要设置以下参数：
  -  `--service-account-issuer`  , 标识该集群 API Server 的固定的 URL。
  -  `--service-account-key-file`  , 一个或者多个验证 token 的公钥。
  -  `--service-account-signing-key-file`  , 签发 service account 的私钥，可以与 `kube-controller-manager` 的 `--service-account-private-key-file` 参数使用相同的文件。

#### kubelet
1. 以下参数被移除：
	-  `--seccomp-profile-root` 
	-  `--cloud-provider` ,  `--cloud-config` ，使用 config 来代替
	-  `--really-crash-for-testing` ,  `--chaos-chance`
2. 已废弃的 `metrics/resource/v1alpha1`  endpoint 被移除，请使用 `metrics/resource`。

#### 其他移除
- `failure-domain.beta.kubernetes.io/zone`  及 `failure-domain.beta.kubernetes.io/region` 标签被废弃，请使用 `topology.kubernetes.io/zone` 及 `topology.kubernetes.io/region` 来代替。所有以 `failure-domain.beta...`  前缀的标签都需要使用对应的 `topology...` 开头的标签来代替。
- PodPreset 被移除，可以使用 webhook 来实现该功能。
- 不再支持 basic auth 鉴权方式。
- 不再支持在工作负载中直接使用腾讯云硬盘存储 (cbs inline) 挂载。
>? 1.18 升级 1.20 过程中无法保证对 [CSI 临时卷 (csi inline)](https://kubernetes.io/zh/docs/concepts/storage/ephemeral-volumes/#csi-ephemeral-volumes) 的成功挂载，如您的业务使用了 CSI 临时卷，建议转换为持久卷存储后再做升级。
>

### Changelogs
[kubernetes 1.20 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.20.md#whats-new-major-themes)
[kubernetes 1.19 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.19.md#whats-new-major-themes)



## 1.18 changes since 1.16
### 重大更新
#### cloud provider 标签功能达到稳定（GA）阶段
废弃标签及新标签如下表所示：

| 废弃标签 | 新标签 | 
|:---------|:---------|
| `beta.kubernetes.io/instance-type` | `node.kubernetes.io/instance-type` |
| `failure-domain.beta.kubernetes.io/region` |`topology.kubernetes.io/region` |
| `failure-domain.beta.kubernetes.io/zone` | `topology.kubernetes.io/zone` |




#### 卷快照（Volume Snapshot）功能进入 Beta 阶段
VolumeSnapshotDataSource 默认开启。详情请参阅 [releasing CSI volume snapshots to beta](https://kubernetes.io/blog/2019/12/09/kubernetes-1-17-feature-cis-volume-snapshot-beta/)。

#### CSI Migration 进入 Beta 阶段
CSIMigration 默认开启。详情请参阅 [CSI migration going to beta](https://kubernetes.io/blog/2019/12/09/kubernetes-1-17-feature-csi-migration-beta/)。

#### Kubernetes 拓扑管理器迎来 Beta 版
拓扑管理器功能（TopologyManager）在1.18中进入 Beta，可以让 CPU 与其他设备（例如 SR-IOV-VF）实现 NUMA 对齐，使工作负载能够支持低延迟的工作场景。
在引入拓扑管理器之前，CPU 与设备管理器只能彼此独立地做出资源分配决策，可能导致在多插座 CPU 系统中无法获取理想的资源分配结果，影响延迟敏感应用的性能。

#### Serverside Apply 进入 Beta 2阶段
Server-side Apply 在 Kubernetes 1.16版本被提升到 Beta 版，1.18引入第二个 Beta 版本（ServerSideApply），此版本会记录和管理所有新 Kubernetes 对象字段的变化，确保用户了解资源动态。

#### IngressClass 资源
`IngressClass` 资源描述在 Kubernetes 集群内的一种 Ingress 控制器类型。`Ingress` 资源新增 `ingressClassName` 字段，用于设置使用 `IngressClass` 的控制器名称，替代废弃的 `kubernetes.io/ingress.class` 标注。

### 其他更新
- Node Local DNSCache 达到 GA。
- IPv6进入 Beta 阶段。
- `kubectl debug`，Alpha 特性。
- `Windows CSI support`，Alpha 特性。
- `ImmutableEphemeralVolumes`，Alpha 特性（支持不可变 ConfigMap 和 Secret，不刷新对应的 volume）。
- 以下特性达到 GA：
  - `ScheduleDaemonSetPods`
  - `TaintNodesByCondition`
  - `WatchBookmark`
  - `NodeLease`
  - `CSINodeInfo`
  - `VolumeSubpathEnvExpansion`
  - `AttachVolumeLimit`
  - `ResourceQuotaScopeSelectors` 
  - `VolumePVCDataSource`
  - `TaintBasedEvictions`
  - `BlockVolume`、`CSIBlockVolume`
  - `Windows RunAsUserName`
- 进入 Beta 的特性：
  - `EndpointSlices`：默认关闭
  - `CSIMigrationAWS`：默认关闭
  - `StartupProbe`
  - `EvenPodsSpread`

### 废弃和移除
#### 移除的特性
以下特性被移除，默认开启且不可配置：
- `GCERegionalPersistentDisk`
- `EnableAggregatedDiscoveryTimeout`
- `PersistentLocalVolumes`
- `CustomResourceValidation`
- `CustomResourceSubresources`
- `CustomResourceWebhookConversion`
- `CustomResourcePublishOpenAPI`
- `CustomResourceDefaulting`

#### 其他移除
移除内置的 cluster role：
 - `system:csi-external-provisioner` 
 - `system:csi-external-attacher`

####  废弃的特性开关和参数
- 废弃默认的 service IP CIDR（`10.0.0.0/24`），必须通过 kube-apiserver 的 `--service-cluster-ip-range` 参数进行设置。
- 废弃 API 组 `rbac.authorization.k8s.io/v1alpha1` 和 `rbac.authorization.k8s.io/v1beta1`，计划在1.20版本中移除。请迁移到 `rbac.authorization.k8s.io/v1`。
- 废弃 `CSINodeInfo` 特性，该特性已经达到 GA 并默认开启。

### 参数及其他变更
#### kube-apiserver
- `--encryption-provider-config`：如果配置文件中指定 `cacheSize: 0`，则1.18之前的版本会自动设置为缓存1000个 key，1.18版本会报告配置验证错误。可通过设置 cacheSize 为负值来关闭缓存。
-  `--feature-gates`：以下特性默认开启，并不再支持通过命令行设置。
  - `PodPriority`
  - `TaintNodesByCondition`
  - `ResourceQuotaScopeSelectors` 
  - `ScheduleDaemonSetPods` 
- 不再支持以下资源版本（group version）：
    - `apps/v1beta1` 及 `apps/v1beta2`，请使用 `apps/v1`。
    - 其中，`extensions/v1beta1` 下的：
     -  `daemonsets`、`deployments` 及 `replicasets`，请使用 `apps/v1`。
     - `networkpolicies` 请使用 `networking.k8s.io/v1`。
     - `podsecuritypolicies` 请使用 `policy/v1beta1`。

#### kubelet
- `--enable-cadvisor-endpoints`：这个参数默认关闭。如果需要访问 cAdvisor v1 Json API，需要明确开启。
- 废弃参数 `--redirect-container-streaming`，并将在后续版本中移除。1.18只支持默认行为（通过 kubelet 代理 streaming 请求）。如果设置了 `--redirect-container-streaming=true` 则必须移除。
- 废弃 metrics endpoint `/metrics/resource/v1alpha1`，请使用 `/metrics/resource`。

#### kube-proxy
- 废弃以下参数：
    - 废弃 `--healthz-port`，请使用 `--healthz-bind-address`。
    - 废弃 `--metrics-port`，请使用 `--metrics-bind-address`。
- 增加特性开关 `EndpointSliceProxying`（默认关闭）来控制是否在 kube-proxy 中启用 EndpointSlices。特性开关 `EndpointSlice` 不再影响 kube-proxy 的行为。
- 增加以下参数配置 ipvs 连接的超时：
  - `--ipvs-tcp-timeout`
  - `--ipvs-tcpfin-timeout`
  - `--ipvs-udp-timeout`
- iptables 模式增加 IPv4/IPv6双协议栈支持。

#### kube-scheduler
- 废弃 `scheduling_duration_seconds` 指标：
 - 废弃 `scheduling_algorithm_predicate_evaluation_seconds`，替代为  `framework_extension_point_duration_seconds[extension_point="Filter"]`
 - 废弃 `scheduling_algorithm_priority_evaluation_seconds`，替代为 `framework_extension_point_duration_seconds[extension_point="Score"]`
- 在调度器 Policy API 中废弃 `AlwaysCheckAllPredicates`。

#### -enable-profiling 参数
为了对齐 `kube-apiserver`、`kube-controller-manager` 和 `kube-scheduler` ，[默认开启 profiling](https://github.com/kubernetes/kubernetes/pull/88663)。如需关闭 profiling，需指定参数 `--enable-profiling=false`。

#### kubectl
- 移除已废弃的 `--include-uninitialized` 参数。
- `kubectl` 和 `k8s.io/client-go` 不再默认使用 http://localhost:8080 作为 apiserver 的地址。
- `kubectl run` 支持创建 Pod，不再支持使用之前已废弃的 generator 创建其他类型的资源。
- 移除已废弃的 `kubectl rolling-update` 命令，请使用 `rollout` 命令。
- `–dry-run` 支持3个参数值 `client`、`server` 和 `none`。
- `–dry-run=server` 支持命令：`apply`、`patch`、`create`、`run`、`annotate`、`label`、`set`、`autoscale`、 `drain`、`rollout undo` 和 `expose`。
- 新的 `kubectl alpha debug` 命令，可以 [在 Pod 中附临时的容器进行调试和排查问题](https://github.com/kubernetes/kubernetes/pull/88004)（需要启用1.16引入的 `EphemeralContainers` 特性）。

#### hyperkube
Hyperkube 从 Go 代码修改为 bash 脚本。

### Changelogs
[kubernetes 1.18 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md#whats-new-major-themes)
[kubernetes 1.17 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.17.md#whats-new-major-themes)



## 1.16 changes since 1.14
### 重大更新
#### 集群稳定性和可用性改进
裸金属集群工具及 HA 等生产可用的特性都得到了改进和加强。
kubeadm 对 HA 的支持进入 beta 阶段，用户可以使用 `kubeadm init` 和 `kubeadm join` 命令部署高可用的控制面。证书管理更加稳定和健壮，kubeadm 可以在 update 集群时，在证书到期前无缝更新所有的证书。详情请参阅 [pr357](https://github.com/kubernetes/enhancements/issues/357) 和 [pr970](https://github.com/kubernetes/enhancements/issues/970)。

#### CSI 持续改进
存储 SIG 继续致力于内建存储插件迁移到 CSI 接口，支持内建存储插件的大小调整，内联存储卷等特性，还引入了一些原本 Kuebernetes 存储子系统中不存在的 alpha 功能，例如存储卷克隆。
存储卷克隆允许用户在配置新存储卷时，指定另一 PVC 为 “DataSource”。如果底层存储系统支持此项功能并在其 CSI 驱动程序实现了 “CLONE_VOLUME” 功能，则新存储卷将成为源存储卷的克隆。详情请参见 [pr625](https://github.com/kubernetes/enhancements/issues/625)。
#### 特性
- 达到 GA 的特性：
	- `CRD`
	- `Admission Webhook`
	- `GCERegionalPersistentDisk` 
	- `CustomResourcePublishOpenAPI` 
	- `CustomResourceSubresources`
	- `CustomResourceValidation`
	- `CustomResourceWebhookConversion`
- CSI 规范中支持调整卷大小的功能进入 Beta。

### 一般更新
- Kubernetes 核心代码支持 Go 模块。
- 继续为 cloud-provider 代码提取和组织进行准备。cloud-provider 代码已经被移动至 kubernetes/legacy-cloud-providers，以便后续删除与外部使用。
- [Kubectl get 与 describe 命令支持扩展](https://github.com/kubernetes/enhancements/issues/515)。
- [节点支持第三方监控插件](https://github.com/kubernetes/enhancements/issues/606)。
- 发布新的 alpha 版调度框架，用于开发和管理插件，扩展调度器功能。详情请参见 [pr624](https://github.com/kubernetes/enhancements/issues/624)。
- 继续弃用 extensions/v1beta1、apps/v1beta1以及 apps/v1beta2的API，这些扩展将在1.16版本中被彻底淘汰。
- Kubelet 增加 Topology Manager 组件，旨在协调资源分配决策，优化资源分配。
- 支持 IPv4/IPv6双栈，可同时给 Pod 与服务分配 v4和 v6的地址。
- alpha 特性 API Server 网络代理。
- 面向云控制器管理器迁移提供更多扩展选项。
- 弃用 extensions/v1beta1、apps/v1beta1以及 apps/v1beta2 API。

#### 已知问题
在1.15版本使用 `--log-file` 参数存在日志会被多次写入同一个文件的问题。详情请参阅 [pr78734](https://github.com/kubernetes/kubernetes/issues/78734#issuecomment-501372131)。

#### 更新须知
- **集群**
    - 以下标签不再在节点上设置：`beta.kubernetes.io/metadata-proxy-ready`、 `beta.kubernetes.io/metadata-proxy-ready` 及 `beta.kubernetes.io/kube-proxy-ds-ready`。
        * `ip-mask-agent` 使用 `node.kubernetes.io/masq-agent-ds-ready` 作为 node 选择器，不再使用 `beta.kubernetes.io/masq-agent-ds-ready`。
        * `kube-proxy` 使用 `node.kubernetes.io/kube-proxy-ds-ready` 作为 node 选择器，不再使用 `beta.kubernetes.io/kube-proxy-ds-ready`。  
        * `metadata-proxy` 使用 `cloud.google.com/metadata-proxy-ready` 作为 node 选择器，不再使用 `beta.kubernetes.io/metadata-proxy-ready`。  
- **API Machinery**
k8s.io/kubernetes 和其他发布的组件，包括 k8s.io/client-go 和 k8s.io/api 等，现在包含 Go 模块文件，包括依赖库的版本信息。在以 Go 模块方式使用 k8s.io/client-go 时可以参考 [go-modules](http://git.k8s.io/client-go/INSTALL.md#go-modules) 以及 [pr74877](https://github.com/kubernetes/kubernetes/pull/74877)。
- **Apps**
 **hyperkube 短别名已从代码中移除**，在编译 hyperkube docker 镜像时会创建这些别名，详情请参见 [pr76953](https://github.com/kubernetes/kubernetes/pull/76953)。
- **Lifecycle**
    - 废弃的 kubeadm `v1alpha3` 配置被全部移除。
    - kube-up.sh 不再支持 centos 和 local。
- **Storage**
    - CSI 卷不再设置 `Node.Status.Volumes.Attached.DevicePath` 字段，需要更新此字段的外部控制器。
    - alpha 版本的 CRD 被移除。
    - 默认启用 `StorageObjectInUseProtection` admission [插件](https://github.com/kubernetes/kubernetes/pull/74610)。如果之前没有启用该插件，集群的行为可能会发生变化。
    - CSI driver 启用 PodInfoOnMount 后，在 volume 上下文会增加一个新的参数：`csi.storage.k8s.io/ephemeral`，允许 driver 在实现 NodePublishVolume 时，逐个判断当前 volume 是短暂存储还是持久的，详情请参见 [pr79983](https://github.com/kubernetes/kubernetes/pull/79983)。
    - VolumePVCDataSource（存储卷克隆功能） 进入 beta，详情请参见 [pr81792]( https://github.com/kubernetes/kubernetes/pull/81792)。
    - 把内建以及 CSI volume 的 limit 合为一个调度器 preidicate，详情请参见 [pr77595]( https://github.com/kubernetes/kubernetes/pull/77595)。  
- **kube-apiserver**
    - 废弃参数 `--enable-logs-handler`，计划在 v1.19移除。
    - 废弃 `--basic-auth-file` 及相应的认证模式，未来计划移除。
    - 废弃默认的 service IP CIDR（10.0.0.0/24），计划半年后或者2个 release 后移除。必须使用 `--service-cluster-ip-range` 参数来制定 service 的 IP 段。
- **kube-scheduler**
使用 `v1beta1` Events API。消费 scheudler 事件的工具需要使用 v1beta1 Event API。
- **kube-proxy**
    - 移除参数`--conntrack-max`（可使用`--conntrack-min` 和`--conntrack-max-per-core` 来代替）。
    - 移除参数 `--cleanup-iptables`。
    - 移除 `--resource-container`。
- **kubelet**
    - 移除参数 `--allow-privileged`、`--host-ipc-sources`、`--host-pid-sources` 和 `--host-network-sources`（可以使用 `PodSecurityPolicy` 的准入控制器来代替）。
    - 废弃 cAdvisor JSON 接口。
    - 移除 `--containerized`。
    - 不再支持通过 `--node-labels` 参数设置 `kubernetes.io-` 或 `k8s.io-` 为前缀的不被允许的标签 。
- **kubectl**
    - 移除 `kubectl scale job`。
    - 移除 `kubectl exec` 命令的 `--pod/-p` 参数。
    - 移除 `kubectl convert` 命令。
    - 移除 `--include-uninitialized`。
    - `kubectl cp` 不再支持复制容器中的符号链接，可以使用如下命令代替：
     - `local to pod`：`tar cf - /tmp/foo | kubectl exec -i -n <some-namespace> <some-pod> -- tar xf - -C /tmp/bar`
     - `pod to local`：`kubectl exec -n <some-namespace> <some-pod> -- tar cf - /tmp/foo | tar xf - -C /tmp/bar`
- **kubeadm**
    - 废弃命令 `kubeadm upgrade node config` 和 `kubeadm upgrade node experimental-control-plane`，使用 `kubeadm upgrade node` 代替。
    - 废弃参数 `--experimental-control-plane`，使用 `--control-plane` 代替。
    - 废弃参数 `--experimental-upload-certs`，使用 `--upload-certs` 代替。
    - 废弃命令 `kubeadm config upload`，使用 `kubeadm init phase upload-confi` 代替。
    - CoreDNS 使用 ready 插件进行就绪检查。
    - 废弃 `proxy` 插件，使用 `forward` 插件来代替。
    - `kubernetes` 插件移除 `resyncperiod` 选项。
    - 废弃 `upstream` 选项，如果指定，将被忽略。

### Changelogs
[kubernetes 1.16 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.16.md#whats-new-major-themes)
[kubernetes 1.15 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#whats-new-major-themes)



## 1.14 changes since 1.12
### 重大更新
* [Container Storage Interface 进入 GA](https://github.com/kubernetes/kubernetes/pull/71020)。
* [CoreDNS 替换 kube-dns 成为默认 DNS Server]( https://github.com/kubernetes/kubernetes/pull/69883)。
* 使用 kubeadm 简化集群管理。
* [支持 Windows Nodes 进入 stable](https://github.com/kubernetes/enhancements/issues/116)。
* [本地存储进入 GA]( https://github.com/kubernetes/enhancements/issues/121#issuecomment-457396290)。
* [Pid Limiting 进入 beta](http://github.com/kubernetes/kubernetes/pull/73651)。
* [支持 Pod Priority 和 Preemption](https://github.com/kubernetes/enhancements/issues/564)。

### 一般更新
* dry-run 进入 beta（dry-run 使用户可以模拟真实 API 请求，而不实际改变集群状态）。
* kubectl diff 进入 beta。
* kubectl 插件注册进入 stable。
* kubelet 插件机制进入 beta。
* CSIPersistentVolume 进入 GA。
* TaintBasedEviction 进入 beta。
* kube-scheduler 可感知 volume topology，进入 stable。
* 支持 out-of-tree CSI Volume plugins，进入 stable。
* 支持第三方设备监控插件。
* kube-scheduler subnet feasibility 进入 beta。
* Pod Ready 支持自定义探测条件。
* Node 内存支持 HugePage。
* RuntimeClass 进入 beta。
* Node OS/Arch labels 进入 GA。
* node-leases 进入 beta。
* kubelet resource metrics endpoint 进入 alpha，支持通过 prometheus 采集数据。
* runAsGroup 进入 beta。
* kubectl apply server-side 进入 alpha，可在服务端执行 apply 操作。
* kubectl 支持 kustomize。
* 支持在 Pod 中配置 resolv.conf。
* CSI volumes 支持 resizing。
* CSI 支持 topology。
* volume mount 支持设定子路径参数。
* CSI 支持裸块设备。
* CSI 支持本地 ephemeral volume。

### 更新须知
* **kube-apiserver**
    * 不再支持 `etcd2`，默认 `--storage-backend=etcd3`。
    * 废弃参数 `--etcd-quorum-read`。
    * 废弃参数 `--storage-versions`。
    * 废弃参数 `--repair-malformed-updates`。
* **kube-controller-manager**
废弃参数 `--insecure-experimental-approve-all-kubelet-csrs-for-group`。
* **kubelet**
 * 废弃参数 `--google-json-key` 。
 * 废弃参数 `--experimental-fail-swap-on`。
* <b> kube-scheduler</b>
 不再支持 `componentconfig/v1alpha1`。
* **kubectl**
不再支持命令 `run-container`。  
* **taints**
不再支持 `node.alpha.kubernetes.io/notReady` 和 `node.alpha.kubernetes.io/unreachable`，改为 `node.kubernetes.io/not-ready` 和 `node.kubernetes.io/unreachable`。

### Changelogs
[kubernetes 1.14 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#kubernetes-v114-release-notes)
[kubernetes 1.13 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.13.md#kubernetes-113-release-notes)

## 1.12 changes since 1.10
### 重大更新
#### API 
- CustomResources 子资源现在进入 beta 阶段，并默认开启，可以对 `/status` 子资源更新除了 `.status` 字段（之前只允许对 .spec 和 .metadata 进行更新）。在启用 `/status` 子资源时，`required` 和 `description` 可用于 CRD OpenAPI 验证 schema。另外，用户可以创建多个版本的 CustomResourceDefinitions，不需进行自动转换。可以通过 CustomResourceDefinitions 的 `spec.additionalPrinterColumns` 字段让 `kubectl get` 的输出包含额外的列。
- 支持 `dry run` 功能，允许用户可以看到某些命令的执行结果，而不需要真正提交相关的更改。

#### 认证授权
- RBAC 聚合 ClusterRoles 进入 GA 阶段，client-go credentials 插件进入 Beta 阶段，支持从外部插件获取 TLS 认证信息。
- 审计事件增加了如下注解，用户可以更清晰的了解审计决策的过程：
  * Authorization 组件会设置 `authorization.k8s.io/decision`（authorization 决定 allow 或 forbid），及 `authorization.k8s.io/reason`（做出这个决定的原因）。
  * PodSecurityPolicy 准入控制器会设置 `podsecuritypolicy.admission.k8s.io/admit-policy` 和 `podsecuritypolicy.admission.k8s.io/validate-policy`，包含允许 Pod 准入相关的策略名称（PodSecurityPolicy 同时可以限制 hostPath 类型的挂载点为只读模式）。
- NodeRestriction 准入控制器会禁止节点修改其对应的 Node 对象的污点信息，让用户更容易控制和追踪节点的污点设置情况。

#### CLI 命令行
CLI 实现了新的插件机制，并提供了包含通用 CLI 工具的开发库方便插件开发者进行插件开发。

#### 网络
- ipvs 模式进入 GA。
- CoreDNS 进入 GA，代替 kube-dns。

#### 节点
- DynamicKubeletConfig 进入 Beta 阶段。
- cri-tools GA。
- PodShareProcessNamespace 进入 Beta 阶段。
- 新增 Alpha 特性：RuntimeClass，CustomCFSQuotaPeriod。

#### 调度器
- Pod Priority 及 Preemption 进入 Beta 阶段。
- DaemonSet Pod 的调度不再由 DaemonSet 控制器管理，而由默认调度器管理。
- TaintNodeByCondition 进入 Beta 阶段。
- 默认开启本地镜像优选功能。在调度 Pod 时，本地已经拉取全部或者部分 Pod 所需镜像的节点会有更高的优先级，这样可以加速 Pod 启动。

### 一般更新
- 进入 GA 的特性：ClusterRole，StorageObjectInUseProtection。
- 进入 Beta 的特性：外部 Cloud Provider。

### 更新须知
- **kube-apiserver**
  - `--storage-version` 参数被移除，由 `--storage-versions` 代替。同时 `--storage-versions` 也被废弃。
  - `--endpoint-reconciler-type` 默认值改为 `lease`。
  - 使用`--enable-admission-plugins` 时，默认包含。使用 `--admission-control` 参数时，需要显示指定。
- **kubelet**
  - 废弃 `--rotate-certificates` 参数，由配置文件的 .RotateCertificates 字段代替。
- **kubectl**
  - 除 `run-pod/v1` 外，其他 `kubectl run` 的 generator 已废弃。
  - `kubectl logs` 移除 `--interactive` 参数。
  - `--use-openapi-print-columns` 已废弃，由 `--server-print` 代替。

### Changelogs
[kubernetes 1.12 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.12.md#major-themes)
[kubernetes 1.11 changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.11.md#kubernetes-111-release-notes)

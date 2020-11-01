## K8S 的节点健康检测
在 Kubernetes 集群运行时，节点有时会因为组件问题、内核死锁、资源不足等原因不可用。Kubelet 默认对节点的 PIDPressure、MemoryPressure、DiskPressure 等资源状态进行监控，但是存在当 Kubelet 上报状态时节点已处于不可用状态的情况，甚至 Kubelet 可能已开始驱逐 Pod。在一些场景下，原生 Kubernetes 对节点健康的检测机制是不完善的，为了提前发现节点的问题，需要添加更加细致化的指标来描述节点的健康状态并且采取相应的恢复策略，实现智能运维，以节省开发和减轻运维人员的负担。

## node-problem-detector 介绍
NPD（node-problem-detector）是 Kubernetes 社区开源的集群节点的健康检测组件。NPD 提供了通过正则匹配系统日志或文件来发现节点异常的功能。用户可以通过自己的运维经验，配置可能产生异常问题日志的正则表达式，选择不同的上报方式。NPD 会解析用户的配置文件，当有日志能匹配到用户配置的正则表达式时，可以通过 NodeCondition、Event 或 Promethues Metric 等方式将检测到的异常状态上报。除了日志匹配功能，NPD 还给接受用户自己编写的自定义检测插件，用户可以开发自己的脚本或可执行文件集成到 NPD 的插件中，让 NPD 定期执行检测程序。

## TKE NPDPlus 插件介绍
在 TKE 中通过扩展组件的形式集成了 NPD，并且对 NPD 的能力做了增强，称为 NodeProblemDetectorPlus（NPDPlus）扩展组件。用户可以对已有集群一键部署 NPDPlus 扩展组件，也可以在创建集群的时候选择在创建集群的同时部署 NPDPlus。TKE 提取了可以通过特定形式发现节点异常的指标，并将其集成在 NPDPlus 中。例如可以在 NPDPlus 容器中检测 Kubelet 和 Docker 的 systemd 状态，以及检测主机的文件描述符和线程数压力等。具体指标如下所示：

| Condition Type  | 默认值  | 描述| 
|:---------|:---------|:---------|
| ReadonlyFilesystem |False |文件系统是否只读 |
|FDPressure |False |查看主机的文件描述符数量是否达到最大值的80% |
|FrequentKubeletRestart |False |Kubelet 是否在20Min内重启超过5次|
|CorruptDockerOverlay2| False| Dockerlmage 是否存在问题 |
|KubeletProblem |False| Kubelet service 是否 Running|
|KernelDeadlock |False| 内核是否存在死锁|
|FrequentDockerRestart |False |Docker 是否在20Min内重启超过5次|
|FrequentContainerdRestart |False |Containerd 是否在20Min内重启超过5次 |
|DockerdProblem |False |Docker service 是否 Running（若节点运行时为 Containerd，则一直为 False） |
|ContainerdProblem| False| Containerd service 是否 Running（若节点运行时为 Docker，则一直为 False）|
|ThreadPressure| False| 系统目前线程数是否达到最大值的90% |
|NetworkUnavailable| False |NTP service 是否 Running|
|SerfFailed| False| 分布式检测节点网络健康状态|



TKE 使用 NPDPlus 是为了能够提前发现节点的不可用状态，而不是当节点已经不健康后再上报状态。当用户在 TKE 集群中部署了 NPDPlus 后，使用命令 `kubectl describe node` 会发现多出了很多 Node Condition，如 FDPressure 表示该节点上已经使用的文件描述符数量是否已经达到机器允许最大值的80%；ThreadPressure 表示节点上的线程数是否已经达到机器允许的90% 等等。用户可以监控这些 Condition，当异常状态出现时，提前采取规避策略。

同时，K8S 目前认为节点 NotReady 的机制依赖于 kube-controller-manager 的参数设定，当节点网络完全不通的情况下 K8S 很难在秒级别发现节点的异常，这在一些场景下（如直播、在线会议等）是不能接受的。针对这种场景，NPDPlus 中继承了分布式节点健康检测功能，可以在秒级快速地检测节点网络状态，以及是否能与其他节点相互通信，同时不依赖与 K8S master 组件的通信。

## 节点自愈

采集节点的健康状态是为了能够在业务 Pod 不可用之前提前发现节点异常，从而运维或开发人员可以对 Docker、Kubelet 或节点进行修复。在 NPDPlus 中，为了减轻运维人员的负担，提供了根据采集到的节点状态从而进行不同自愈动作的能力。集群管理员可以根据节点不同的状态配置相应的自愈能力，如重启 Docker、重启 Kubelet 或重启 CVM 节点等。同时为了防止集群中的节点雪崩，在执行自愈动作之前做了严格的限流，防止节点大规模重启。同时为了防止集群中的节点雪崩，在执行自愈动作之前做了严格的限流。具体策略为：
- 在同一时刻只允许集群中的一个节点进行自愈行为，并且两个自愈行为之间至少间隔 1 分钟。
- 当有新节点添加到集群中时，会给节点 2 分钟的容忍时间，防止由于节点刚刚添加到集群的不稳定性导致错误自愈。
- 当节点触发重启 CVM 自愈动作后还处于异常状态时，则在 3 小时之内此节点不再执行任何自愈动作。

NPDPlus 会将执行过的所有自愈动作记录在 Node 的 Event 中，方便集群管理员了解在Node上发生的事件。
<img style="width:80%" src="https://main.qcloudimg.com/raw/f39e70300a001cb0ceb33a30499458c8.png" data-nonescope="true">

## 操作步骤

1. 登录腾讯云容器服务控制台，进入想要创建 NPDPlus 的集群。
2. 点击控制台左侧的组件管理，在组件管理中选中 NodeProblemDetectorPlus (节点异常检测Plus)。
3. 配置 NodeProblemDetectorPlus 参数，可以选择根据特定节点的状态执行不同的自愈动作。
4. 选择确定，点击完成即可一键创建。
<img style="width:80%" src="https://main.qcloudimg.com/raw/3661d74618efdb560a041b691e10c456.png" data-nonescope="true">

在集群的组建管理中查看到NPDPlus运行中说明 NPDPlus 运行成功:
<img style="width:80%" src="https://main.qcloudimg.com/raw/3a26dbd61f8f9f287d227093f7fa680e.png" data-nonescope="true">

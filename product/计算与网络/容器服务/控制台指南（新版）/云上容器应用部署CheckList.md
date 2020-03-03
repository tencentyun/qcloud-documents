## 简介

业务上云安全高效、稳定高可用是每一位涉云从业者的共同诉求。这一诉求实现的前提，离不开系统可用性、数据可靠性及运维稳定性三者的完美配合。本文将从评估项目、影响说明及评估参考三个角度为您阐述云上容器应用部署的各个检查项，以便帮助您扫除上云障碍、顺利高效地完成业务迁移至容器服务（TKE）。


## 检查项

### 系统可用性
<table>
	<th style="width:10%">类别</th><th style="width:32%">评估项目</th><th style="5%">类型</th><th style="width:38%">影响说明</th><th style="width:15%">评估参考</th>
    <tr>
        <td rowspan="6">集群</td>
				<td>创建集群前，结合业务场景提前规划节点网络和容器网络，避免后续业务扩容受限。</td>
				<td>网络规划</td>
				<td>集群所在子网或容器网段较小，将可能导致集群实际支持的可用节点数少于业务所需容量。</td>
				<td><li><a href="https://cloud.tencent.com/document/product/215/30313">网络规划</a></li><li><a href="https://cloud.tencent.com/document/product/457/9083">容器及节点网络设置</a></li></td>
    </tr>
    <tr>
        <td>创建集群前，提前梳理专线接入、对等连接、容器网段和子网网段等相关网段的规划，避免之后出现网段冲突，影响业务。</td>
				<td>网络规划</td>
				<td>简单组网场景按照页面提示配置集群相关网段，避免冲突；业务复杂组网
场景，例如对等连接、专线接入、VPN 等，网络规划不当将影响整体业务正常互访。
</td><td><a href="https://cloud.tencent.com/document/product/215/37053"> VPC 连接</a></td>
    </tr>
    <tr>
        <td>创建集群时，会自动新建并绑定默认安全组，支持根据业务需求设置自定义安全组规则。</td>
				<td>部署</td>
				<td>安全组是重要的安全隔离手段，不当的安全策略配置可能会引起安全相关的隐患及服务连通性等问题。</td><td><a href="https://cloud.tencent.com/document/product/457/9084">容器服务安全组设置</a></td>
    </tr>
    <tr>
        <td> Containerd 和 Docker 作为 TKE 当前支持的运行时组件，有不同的适用场景。创建集群时，请根据业务场景选择合适的容器运行时（Container Runtime）组件。</td><td>部署</td><td>集群一旦创建，便无法更改容器运行时，除非重新创建集群。</td><td><a href="https://cloud.tencent.com/document/product/457/35747">如何选择 Containerd 和 Docker</a></td>
    </tr>
	<tr>
        <td>默认情况下，Kube-proxy 使用 iptables 来实现 Service 到 Pod 之间的负载均衡。创建集群时，支持快速开启 IPVS 来承接流量并实现负载均衡。</td>
				<td>部署</td>
				<td>当前支持在创建集群时开启 IPVS，之后对全集群生效且将不可关闭。</td>
				<td><a href="https://cloud.tencent.com/document/product/457/32193">集群启用 IPVS</a></td>
    </tr>
	<tr>
        <td>创建集群时，根据业务场景选择合适的集群模式：独立集群、托管集群。</td><td>部署</td><td>托管集群的 Master 和 Etcd 不属于用户资源，由腾讯云技术团队集中管理和维护，用户无法修改 Master 和 Etcd 的部署规模和服务参数。如需修改，请选用独立部署模式集群。</td>
				<td><li><a href="https://cloud.tencent.com/document/product/457/32187">集群概述</a></li><li><a href="https://cloud.tencent.com/document/product/457/31013">集群的托管模式说明</a></li></td>
    </tr>
    <tr>
        <td rowspan="4">工作<br>负载</td>
				<td>创建工作负载时需设置 CPU 和内存的限制范围，提高业务的健壮性。</td>
				<td>部署</td>
				<td>同一个节点上部署多个应用，当未设置资源上下限的应用出现应用异常资源泄露问题时，将会导致其它应用分配不到资源而异常，且其监控信息将会出现误差。</td><td><a href="https://cloud.tencent.com/document/product/457/32813">设置工作负载的资源限制</a></td>    </tr>
    <tr>
        <td>创建工作负载时可设置容器健康检查：“容器存活检查”和“容器就绪检查”。</td><td>可靠性</td><td>容器健康检查未配置，会导致用户业务出现异常时 Pod 无法感知，从而导致不会自动重启恢复业务，最终将会出现 Pod 状态正常，但 Pod 中的业务异常的现象。</td><td><a href="https://cloud.tencent.com/document/product/457/9094">服务健康检查设置</a></td>
    </tr>
    <tr>
        <td>创建服务时需要根据实际访问需求选择合适的访问方式，目前支持以下四种：提供公网访问、仅在集群内访问、VPC 内网访问及主机端口访问。</td>
				<td>部署</td>
				<td>选择不当的访问方式，可能造成服务内外部访问逻辑混乱和资源浪费。</td><td><a href="https://cloud.tencent.com/document/product/457/31710">Service 管理</a></td>
    </tr>
    <tr>
        <td>工作负载创建时，避免单 Pod 副本数设置，请根据自身业务合理设置节点调度策略。</td>
				<td>可靠性</td>
				<td>如设置单 Pod 副本数，当节点异常或实例异常会导致服务异常。为确保您的 Pod  能够调度成功，请确保您在设置调度规则后，节点有空余的资源用于容器的调度。</td><td><li><a href="https://cloud.tencent.com/document/product/457/31705#.E8.B0.83.E6.95.B4-pod-.E6.95.B0.E9.87.8F">调整 Pod 数量</a></li><li><a href="https://cloud.tencent.com/document/product/457/32814">设置工作负载的调度规则</a></li></td>
    </tr>
</table>


### 数据可靠性
<table>
	<th style="width:10%">类别</th><th style="width:32%">评估项目</th><th style="5%">类型</th><th style="width:38%">影响说明</th><th style="width:15%">评估参考</th>
    <tr>
        <td>容器数据持久化</td><td>应用 Pod 数据存储，根据实际需求选择合适的数据卷类型。</td><td>可靠性</td><td>节点异常无法恢复时，存在本地磁盘中的数据无法恢复，而云存储此时可以提供极高的数据可靠性。</td><td><a href="https://cloud.tencent.com/document/product/457/31713">Volume 管理</a></td>
    </tr>
</table>

### 运维稳定性
<table>
   	<th style="width:10%">类别</th><th style="width:32%">评估项目</th><th style="5%">类型</th><th style="width:38%">影响说明</th><th style="width:15%">评估参考</th>
    <tr>
        <td rowspan="2">工程</td><td>CVM、VPC、子网及 CBS 等资源配额是否满足客户需求。</td><td>部署</td><td>配额不足将会导致创建资源失败，对于配置了自动扩容的用户尤其需要保障所使用的云服务配额充足。</td><td><li><a href="https://cloud.tencent.com/document/product/457/9087">购买集群配额限制</a></li><li><a href="https://cloud.tencent.com/document/product/215/20093">配额限制</a></li></td>
    </tr>
    <tr>
        <td>集群的节点上不建议用户随意修改内核参数、系统配置、集群核心组件版本、安全组及 LB 相关参数等。</td><td>部署</td><td>可能会导致 TKE 集群功能异常或安装在节点上的 Kubernetes 组件异常，节点状态变成不可用，无法部署应用到此节点。</td><td><a href="https://cloud.tencent.com/document/product/457/39539">容器服务高危操作</a></td>
    </tr>
	<tr>
        <td>主动<br>运维</td><td>容器服务提供多维度的监控和告警功能，同时结合云监控提供的基础资源监控，能保证更细的指标覆盖。配置监控告警，以便于异常时及时收到告警和故障定位。</td><td>监控</td><td>未配置监控告警，将无法建立容器集群性能的正常标准，在出现异常时无法及时收到告警，需要人工巡检环境。</td><td><li><a href="https://cloud.tencent.com/document/product/457/34182">设置告警</a></li><li><a href="https://cloud.tencent.com/document/product/457/34181">查看监控数据</a></li><li><a href="https://cloud.tencent.com/document/product/457/34183">监控及告警指标列表</a></li></td>
    </tr>
</table>

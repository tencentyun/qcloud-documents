## 概述
容器服务 TKE 包含托管集群及独立部署集群。若使用托管集群，则无需关注容灾，托管集群的 Master 由容器服务 TKE 内部维护。若使用独立集群，则 Master 节点由用户自行管理维护。
独立集群如需实现容灾，则首先应根据需求规划容灾方案，在创建集群时进行相应配置即可。本文介绍如何实现 TKE 独立集群 Master 的容灾，您可参考本文进行操作。

## 容灾实现思路
实现容灾应从物理部署层面切入，为避免因一次物理层面的故障导致多台 Master 异常，需将 Master 节点打散部署。可借助 [置放群组](https://cloud.tencent.com/document/product/213/15486) 来选择将 Master 从物理机、交换机或机架三种维度中其中一种来将 Master 打散，以避免底层硬件或软件故障导致多台 Master 异常。如对容灾要求非常高，还可以考虑将 Master 跨可用区部署，以避免在发生大规模故障时，整个数据中心不可用导致 Master 集体异常的情况。


## 使用置放群组打散 Master
1. 登录 [置放群组控制台](https://console.cloud.tencent.com/cvm/ps)，创建置放群组，详情请参见 [分散置放群组](https://cloud.tencent.com/document/product/213/17020)。如下图所示：
>!置放群组需与 TKE 独立集群在同一地域。
>
<img style="width:50%" src="https://main.qcloudimg.com/raw/a999a9d7a433c3476a5160f769d24b7f.png"></img>
置放群组层级如下，本文以选择“机架层级”为例：
<table>
<tr>
<th>置放群组层级</th><th>说明</th>
</tr>
<tr>
<td>物理机层级</td><td>独立集群 Master 使用云服务器部署，属于虚拟机，在物理机上运行。一台物理机可能运行有多台虚拟机，如果物理机发生故障，将影响在这台物理机上运行的所有虚拟机。使用这个层级可以将 Master 打散部署到不同物理机上，避免一台物理机故障导致多台 Master 异常。</td>
</tr>
<tr>
<td>交换机层级</td><td>多台不同物理机可能连接在相同的交换机上，如果交换机发生故障，可能影响多台物理机。使用这个层级以将 Master 打散部署到连到不同交换机的物理机上，避免交换机故障导致多台 Master 异常。</td>
</tr>
<tr>
<td>机架层级</td><td>多台不同物理机可能放置在同一个机架上，如果发生机架级别的意外，导致一台机架上多台物理机故障。使用这个层级以将 Master 打散部署到不同机架上的物理机上，避免发生机架级别的意外导致多台 Master 异常。</td>
</tr>
</table>
2. 参考 [创建集群](https://cloud.tencent.com/document/product/457/32189) 创建 TKE 独立集群。在 “Master&Etcd 配置”的“高级设置”中，勾选“将实例添加到分散置放群组” ，并选择已创建的置放群组。如下图所示：
<img style="width:50%" src="https://main.qcloudimg.com/raw/854becf1c40e0b8689c41460b0048caa.png"></img>
配置完成后，对应 Master 节点就会被打散部署到不同的机架上，实现机架级别的容灾。

## Master 跨可用区容灾
如果对容灾要求较高，避免因发生大规模故障时整个数据中心都不可用，导致所有 Master 异常，可选择将 Master 部署在不同可用区中。配置方法如下：
在创建集群，选择 “Master&Etcd 配置”时，在多个可用区添加机型即可。如下图所示：
<img style="width:50%" src="https://main.qcloudimg.com/raw/f6e2719abbb6f125c6674ebe11878fd3.png">

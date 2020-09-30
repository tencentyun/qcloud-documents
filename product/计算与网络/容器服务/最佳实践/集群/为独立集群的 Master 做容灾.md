## 概述

托管集群的 Master 由 TKE 内部维护，本身就有容灾，不需要担心。但如果是独立集群，Master 节点由用户自行管理维护，如果需要做容灾，需要先根据需求规划一下容灾方案，然后在创建集群的时候进行相应的配置，本文将介绍如何为 TKE 独立集群的 Master 做容灾。

### 容灾思路

如何达到 Master 节点的容灾效果呢？这个肯定要从物理的部署层面去考虑，避免一次物理层面的故障导致多台 Master 都挂掉，所以我们需要将 Master 节点打散部署。那如何从物理层面将 Master 节点打散呢？我们可以借助 [置放群组](https://cloud.tencent.com/document/product/213/15486) 来选择将 Master 从物理机、交换机或机架三种维度中其中一种来将 Master 打散以避免底层硬件/软件故障导致多台 Master 同时挂掉。如果对容灾要求非常高，还可以考虑将 Master 跨可用区部署，以避免发生大灾难时，整个数据中心不可用导致 Master 集体挂掉的情况。

## 使用置放群组打散 Master

首先，我们需要在 [置放群组控制台](https://console.cloud.tencent.com/cvm/ps) 创建一个置放群组 (注意地域要选在跟将要创建的 TKE 独立集群同一地域):

<img style="width:450px" src="https://main.qcloudimg.com/raw/a999a9d7a433c3476a5160f769d24b7f.png" data-nonescope="true">

选择其中一种层级:

1. 物理机层级: 独立集群 Master 使用云服务器部署，属于虚拟机，运行在物理机之上，一台物理机可能运行有多台虚拟机，如果物理机发生故障，将影响在这台物理机里运行的所有虚拟机。使用这个层级可以将 Master 打散部署到不同物理机上，避免一台物理机故障导致多台 Master 挂掉。
2. 交换机层级: 多台不同物理机可能连到相同的交换机上，如果交换机发生故障，可能影响多台物理机。使用这个层级以将 Master 打散部署到连到不同交换机的物理机上，避免交换机故障导致多台 Master 挂掉。
3. 机架层级：多台不同物理机可能放置在同一个机架上面，如果发生机架级别的意外，导致一台机架上多台物理机故障。使用这个层级以将 Master 打散部署到不同机架上的物理机上，避免发生机架级别的意外导致多台 Master 挂掉。

这里以机架层级为例，创建好置放群组，然后创建 TKE 独立集群，在 `Master&Etcd 配置-高级设置` 中，勾选 `将实例添加到分散置放群组` ，选择我们刚刚创建的置放群组:

<img style="width:450px" src="https://main.qcloudimg.com/raw/4a757b223c6831d33417d5e5409500bc.png" data-nonescope="true">

选好后，这一批的 Master 节点就会被打散部署到不同的机架上，实现机架级别的容灾。

## Master 跨可用区容灾

如果担心发生天灾或人祸导致整个数据中心都不可用，使得 Master 集体挂掉，可以选择将 Master 部署在不同可用区上，做法也很简单，选择 `Master&Etcd 配置` 时，在多个可用取添加机型即可:

<img style="width:450px" src="https://main.qcloudimg.com/raw/f6e2719abbb6f125c6674ebe11878fd3.png" data-nonescope="true">
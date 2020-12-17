## 引言

[TOC]

随着自研上云的深入，越来越多的有状态服务对于在TKE集群中使用云上存储能力的需求也越来越强烈。
目前腾讯云容器服务[TKE（Tencent Kubernetes Engine）](https://cloud.tencent.com/product/tke)已支持在TKE集群中的应用使用多种存储服务，包括[CBS](https://cloud.tencent.com/product/cbs "CBS")、[CFS](https://cloud.tencent.com/product/cfs)以及[COS](https://cloud.tencent.com/product/cos)。[TKE](https://cloud.tencent.com/product/tke)通过两种存储插件（In-Tree和CSI）来支持上述能力。
用户可以通过云控制台很方便地选择存储类型并创建对应的PV/PVC。但仍然会有一些问题困扰着大家，比如：TKE集群中是否支持扩容CBS云盘；如果集群跨可用区，如何避免集群中频繁出现挂载（attach）失败；TKE中是否支持快照功能；我的应用应该选择哪种类型存储；In-Tree和CSI都支持CBS，二者有和区别，是否能把之前使用In-Tree插件创建的云盘转变为CSI插件管理等。

对于TKE存储的相关问题，这里会详细介绍。接下来，我们先概览下Kubernetes持久化存储的流程。

## Kubernetes持久化存储流程

这里对Kubernetes持久化存储的流程做个概览，不深入各个组件。

![k8s存储流程图](https://main.qcloudimg.com/raw/4abaac3cc23743d15668955f75d11f2a.png)

创建一个使用了持久化存储的pod的流程包含以下步骤：

1. 用户创建一个引用PVC的pod（动态创建PV）；
2. **Scheduler**根据pod的配置、节点状态、PV配置等其他因素把pod调度到一个合适的node上；
3. **PV Controller** watch到PVC，调用Volume Plugin去创建PV，并绑定PV和PVC。如果是out-of-tree存储插件（如CSI），则创建PV实际是由external provisioner完成，之后PV Controller完成PV和PVC的bound；如果是in-tree插件，但是通过`kubernetes-sigs/sig-storage-lib-external-provisioner`实现了一个external provisioner，则与out-of-tree插件相同；如果是in-tree插件，且插件直接实现了相应的创删接口，则PV Controller直接调用in-tree插件的实现完成创建PV。
4. **AD Controller**对比asw和dsw状态，发现Volume需要被attach，则调用Volume Plugin的实现去attach。in-tree插件不需多说，如果是CSI插件，则AD Controller会先调用CSI in-tree代码创建VolumeAttachment对象，CSI插件的一个名为external-attacher的sidecar会watch该对象，watch到创建则调用CSI driver的相应方法(`ControllerPublishVolume`)来attach。
5. **VolumeManager**等到volume成功attach到节点后，开始调用Volume Plugin去进行mount操作。这个mount操作分为两步：第一步是格式化设备并把volume mount到一个global mount path（`/var/lib/kubelet/plugins`下），第二步是将bind mount刚才的global mount path到`/var/lib/kubelet/pods/${pod_UUID}/volumes`下。
6. **Kubelet**调用容器运行时启动容器，并且bind mount第5步中的mount path到容器中。

**（Provision -> Attach -> Mount; Unmount -> Detach -> Delete）**


## TKE存储插件及原理介绍

随着Kubernetes社区发展，TKE先后支持了In-Tree和CSI两种存储插件。二者在功能上的主要区别在于In-Tree存储插件仅支持在TKE集群使用CBS，而CSI支持使用CBS、CFS、COS。

| 类型    | 支持CBS | 支持CFS | 支持COS | 参考                                                        |
| ------- | ------- | ------- | ------- | ----------------------------------------------------------- |
| In-Tree | √       | ×       | ×       |                                                             |
| CSI     | √       | √       | √       | https://github.com/TencentCloud/kubernetes-csi-tencentcloud |

### In-Tree插件（QcloudCbs）

- kubernetes早期只支持以In-Tree的方式扩展存储插件，也就是插件在Kubernetes代码中实现。
- In-Tree插件名为`cloud.tencent.com/qcloud-cbs`，所以也可称为QcloudCbs，在TKE集群中有个默认的名为`cbs`的StorageClass。

```shell
NAME            PROVISIONER                    AGE
cbs (default)   cloud.tencent.com/qcloud-cbs   48m
```

#### 特性

In-Tree插件只实现了使用CBS的能力，其主要特性有：

- **静态数据卷**：即用户手动创建volme、PV对象、PVC对象
- **动态数据卷**：根据StorageClass配置来由插件控制创建和删除volume和PV
- **拓扑感知**：CBS不支持跨可用区挂载，在多可用区集群中，会先调度pod，然后去调度后的node的zone创建volume。
- **调度器感知节点maxAttachLimit**：腾讯云单个CVM上默认最多挂载20块CBS盘，调度器感知该限制，调度时过滤到要超过maxAttachLimit的节点。可以全局修改maxAttachLimit，但需要IaaS层先支持。

<table>
<tr><th style="width:10%">腾讯云存储</th><th style="width:20%">静态数据卷</th><th style="width:10%">动态数据卷</th><th style="width:30%">拓扑感知</th><th style="width:30%">调度器感知节点 maxAttachLimit</th></tr>
<tr>
  <td>腾讯云硬盘（CBS）</td><td>支持两种使用方式： <li>直接通过 volume 使用</li> <li>通过PV/PVC使用（**推荐**）</li></td><td>支持</td><td>支持。pod 调度后，在同一个可用区创建 volume。避免 CBS 跨可用区无法使用。</td><td>支持。云服务器(cvm)可以挂载的云硬盘(cbs)是有上限的。调度器调度 pod 时过滤掉超过最大可挂载 CBS 数量的节点。</td>
</table>



#### 原理简介

下面简单了解下In-Tree插件QcloudCbs的架构图，了解各相关组件分别完成何种工作。

![包含TKE cbs in-tree的存储架构图](https://main.qcloudimg.com/raw/cd54ec9ec42c5f8e08aa9ca6f686ee77.png)

上图是包含TKE In-Tree存储插件的Kubernetes存储架构图。图中绿色部分，皆属于In-Tree插件QcloudCbs的实现范畴。
由上述的[Kubernetes持久化存储流程](#Kubernetes持久化存储流程)可知要动态使用一个cbs pv，主要有三个过程：provision、attach、mount，而这三个过程是由不同组件负责的：

- **cbs-provisioner**负责volume的provision/delete。为了与Kubernetes代码解耦，cbs-provisioner是基于`kubernetes-sigs/sig-storage-lib-external-provisioner`实现的一个***external provisioner***，来provision和delete volume。PV Controller在这种模式下虽然不去provision/delete volume，但是还是会参与处理（比如PV和PVC的绑定）。
- **AD Controller**负责volume的attach/detach。Tencent Cloud Provider中封装云API，In-Tree插件调用Cloud Provider实现了attach/detach的具体逻辑，并提供给AD Controller调用。
- kubelet的**Volume Manager**负责volume的mount/unmount。In-Tree插件中实现MountDevice、SetUp等接口，Volume Manager调用其完成准备volume的最后一步。
- 另外，**Scheduler**中也有volume相关的逻辑，我们添加了一个predicate策略：**`MaxQcloudCbsVolumeCount`**，该策略主要实现***调度器感知节点maxAttachLimit***特性。而Scheduler原生的一个predicate策略：**`NoVolumeZoneConflictPred`**，是用来把pod调度到已有PV所在zone的节点，这可以避免云盘跨可用区挂载的问题；对于新建PV的话，避免云盘跨可用区挂载问题则由***拓扑感知***特性完成。


### CSI插件

CSI是Kubernetes社区扩展卷的标准和推荐方式。TKE的CSI插件包含CBS、CFS、COS三个driver，本节重点介绍CBS CSI driver，并与QcloudCbs进行对比。3个driver的静态pv和动态pv的支持情况如下表所示：

| 腾讯云存储      | 静态数据卷 | 动态数据卷 |
| --------------- | ---------- | ---------- |
| 云硬盘（CBS)    | 支持       | 支持       |
| 文件存储（CFS） | 支持       | 支持       |
| 对象存储（COS） | 支持       | 不支持     |


#### CBS CSI特性及与QcloudCbs对比

- CBS CSI比QcloudCbs多几个特性：volume在线扩容，volume快照和恢复。

| 存储插件             | 静态数据卷 | 动态数据卷 | 拓扑感知 | 调度器感知节点maxAttachLimit | 卷在线扩容 | 卷快照&恢复 |
| -------------------- | ---------- | ---------- | -------- | ---------------------------- | ---------- | ----------- |
| CBS CSI              | √          | √          | √        | √                            | √          | √           |
| QcloudCbs（In-Tree） | √          | √          | √        | √                            | ×          | ×           |


#### 原理简介

##### CSI原理简介

![enter image description here](https://main.qcloudimg.com/raw/2a3963c19f312276fd9ae8d6e6c309b3.png)

CSI原理参考上图。要实现一个CSI driver，一般需要实现以下3个gRPC services（CSI Controller Service可选）：

- ***CSI Identity Services***：提供driver信息（drivername，版本等）
- ***CSI Controller Services***（可选）：controller负责创删卷、attach/detach、扩容、快照等。涉及的方法如下：
  - CreateVolume/DeleteVolume
  - Controller[Publish|Unpublish]Volume (对应attach/detach)
  - CreateSnapshot/DeleteSnapshot/ListSnapshots
  - ControllerExpandVolume
- ***CSI Node Services***：负责向节点注册driver，mount/unmount。涉及的方法如下：
  - NodeStageVolume/NodeUnstageVolume（(un)mount device）
  - NodePublishVolume/NodeUpPublishVolume（(un)mount volume）

在我们实现之外，kuberntes Team还提供了多个外部组件，用于沟通k8s原生组件（apiserver、controller manager、kubelet）与自己实现的CSI driver。

- ***external-provisioner***：watch `PersistentVolumeClaim`（PVC）对象，调用driver的`CreateVolume/DeleteVolume`
- ***external-attacher***：watch `VolumeAttachment`对象，调用driver的`Controller[Publish|Unpublish]Volume`
- ***external-resizer***: watch `PersistentVolumeClaim`对象，调用driver的`ControllerExpandVolume`
- ***external-snapshotter***和***snapshot-controller***：snapshot-controller watch `VolumeSnapshot`和`VolumeSnapshotContent` CRD对象，external-snapshotter watch `VolumeSnapshotContent`对象。调用driver的`CreateSnapshot/DeleteSnapshot/ListSnapshots`
- ***node-driver-registrar***：使用`NodeGetInfo`获取driver信息，然后使用kubelet插件注册机制注册driver。

##### CBS CSI部署图

CBS CSI使用社区推荐部署方式，包含两个workload：

- 一个DaemonSet，也就是每个Node会有一个，我们可以简单称为`NodePlugin`，由CBS CSI Driver和node-driver-registrar两个容器组成。负责向节点注册driver，并提供mount的能力。
- 一个StatefulSet/Deployment，我们可以简称为`Controller`。由driver和多个sidecar（external-provisioner、external-attacher、external-resizer、external-snapshotter、snapshot-controller）一起构成，提供创删卷、attach/detach、扩容、快照等能力

![enter image description here](https://main.qcloudimg.com/raw/29f6e2e3b0791dad155423dbe62c4a94.png)

##### CBS CSI插件的mount是driver容器执行的，它是如何mount到Node上的？

- 答案是：挂载传播（Mount propagation）。挂载传播允许容器内的mount在容器外可见。参见https://stupefied-goodall-e282f7.netlify.app/contributors/design-proposals/node/propagation/
- CBS CSI的global mount阶段（NodeStageVolume）要把设备mount到`/var/lib/kubelet/plugins`的子目录下；之后bind mount阶段（NodePublishVolume）的target path是`/var/lib/kubelet/pods`。所以我们为这两个目录都设置了挂载传播（模式为`Bidirectional`）
  ![enter image description here](https://main.qcloudimg.com/raw/e0a60697277166f9a3954a26937c4ace.png)

## 使用推荐
- TKE集群版本为1.14+(包含1.14)，推荐使用CSI插件
- 需要在TKE集群中使用CFS和COS能力，使用CSI插件
- 需要在TKE集群中对CBS盘在线扩容和使用快照功能，使用CSI插件
- 已经使用了QcloudCbs（In-Tree插件）的，可以继续使用。（后续会通过Volume Migration统一到CBS CSI）


## 最佳实践
provisioner:
- cbs csi —— "com.tencent.cloud.csi.cbs"
- cbs intree —— "cloud.tencent.com/qcloud-cbs"

cbs csi的安装请[cbs csi文档](https://github.com/TencentCloud/kubernetes-csi-tencentcloud/blob/master/docs/README_CBS.md "cbs csi文档")，我们也已经在腾讯云控制台支持扩展组件安装

***本节最佳实践均以cbs csi插件为例，相应版本要求也是针对cbs csi插件***

### 1、如果集群节点跨zone，如何避免cbs云盘跨可用区挂载？
cbs云盘不支持跨可用区挂载到节点，所以在跨可用区的集群中推荐通过***拓扑感知***特性来避免跨可用区挂载的问题。

#### 1.1 使用前注意
- TKE集群版本>=1.14
- 确保csi插件为最新版本

#### 1.2 如何使用

使用方式很简单，在storageclass中设置`volumeBindingMode`为***`WaitForFirstConsumer`***，然后使用该storageClass即可。intree和csi插件均支持。
```yaml
kind: StorageClass
metadata:
  name: cbs-topo
parameters:
  type: cbs
provisioner: com.tencent.cloud.csi.cbs
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
```
#### 1.3 原理
拓扑感知调度需要多个k8s组件配合完成，包括scheduler、pv controller、external-provisioner。流程为：
1. pv controller watch到PVC对象，发现storageclass的volumeBindingMode为`WaitForFirstConsumer`，即不会马上处理该pvc的创建事件，等待scheduler处理；
2. scheduler调度完pod后，会将nodeName以annotation的方式打到PVC对象上: `volume.kubernetes.io/selected-node: 10.0.0.72`
3. pv controller获取到PVC对象的更新事件后，处理这个annotation(`volume.kubernetes.io/selected-node`)，根据nodeName获取Node对象，传入到provisioner中。
4. provisioner根据传过来的Node对象的label获取可用区（`failure-domain.beta.kubernetes.io/zone`），之后在对应zone创建pv，从而达到和pod相同可用区的效果，避免云盘和node在不同可用区而无法挂载。

### 2、如何在线扩容云盘？
TKE支持在线扩容PV，对应的云盘及文件系统，即不需要重启pod即可完成扩容。但，为了确保文件系统的稳定性，还是推荐先让云盘文件系统处于未mount情况下。为此，我们将提供两种扩容方式：
1. 不重启pod的情况下在线扩容
	- 这种情况下被扩容的云盘的文件系统被mount在节点上，如果I/O的话，有可能会出现文件系统扩容错误
2. 重启pod的情况下在线扩容
	- 这种情况下被扩容的云盘的文件系统被unmount了。可以避免上面的问题，***推荐这种方式***。

#### 2.1 使用前注意
- TKE集群版本>=1.16，详见[cbs csi文档](https://github.com/TencentCloud/kubernetes-csi-tencentcloud/blob/master/docs/README_CBS.md "cbs csi文档")
- 仅cbs csi插件支持扩容，确保csi插件为最新版本
- 可以在扩容前使用快照来备份数据，避免扩容失败导致数据丢失。参见[3.2.1 使用快照备份云硬盘](#3.2.1 使用快照备份云硬盘)

#### 2.2 如何使用
##### 2.2.1 创建允许扩容的StorageClass
在storageclass中设置`allowVolumeExpansion`为`true`
```yaml
allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: cbs-csi-expand
parameters:
  diskType: CLOUD_PREMIUM
provisioner: com.tencent.cloud.csi.cbs
reclaimPolicy: Delete
volumeBindingMode: Immediate
```

##### 2.2.2 不重启pod的情况下在线扩容
1、确认扩容前pv和文件系统状态，大小均为20G
```shell
$ kubectl exec ivantestweb-0 df /usr/share/nginx/html
Filesystem     1K-blocks  Used Available Use% Mounted on
/dev/vdd        20511312 45036  20449892   1% /usr/share/nginx/html

$ kubectl get pv pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS   REASON   AGE
pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c   20Gi       RWO            Delete           Bound    default/www1-ivantestweb-0   cbs-csi                 20h
```

2、执行以下命令修改PVC对象中的容量，扩容至30G
```shell
$ kubectl patch pvc www1-ivantestweb-0 -p '{"spec":{"resources":{"requests":{"storage":"30Gi"}}}}'
```
执行后稍等片刻，可以发现pv和文件系统已经扩容至30G：
```
$ kubectl exec ivantestweb-0 df /usr/share/nginx/html
Filesystem     1K-blocks  Used Available Use% Mounted on
/dev/vdd        30832548 44992  30771172   1% /usr/share/nginx/html

$ kubectl get pv pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS   REASON   AGE
pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c   30Gi       RWO            Delete           Bound    default/www1-ivantestweb-0   cbs-csi                 20h
```

##### 2.2.3 重启pod的情况下在线扩容

1、确认扩容前pv和文件系统状态，大小均为30G
```shell
$ kubectl exec ivantestweb-0 df /usr/share/nginx/html
Filesystem     1K-blocks  Used Available Use% Mounted on
/dev/vdd        30832548 44992  30771172   1% /usr/share/nginx/html


$ kubectl get pv pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c 
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS   REASON   AGE
pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c   30Gi       RWO            Delete           Bound    default/www1-ivantestweb-0   cbs-csi                 20h
```

2、使用下面命令给PV对象打标签，打一个非法zone，旨在下一步重启pod后pod无法调度到某个节点上
```shell
$ kubectl label pv pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c failure-domain.beta.kubernetes.io/zone=nozone
```

3、重启pod. 重启后由于pod对应的pv的标签表明的是非法zone，pod会处于Pending状态
```shell
$ kubectl delete pod ivantestweb-0

$ kubectl get pod ivantestweb-0
NAME            READY   STATUS    RESTARTS   AGE
ivantestweb-0   0/1     Pending   0          25s

$ kubectl describe pod ivantestweb-0
Events:
  Type     Reason            Age                 From               Message
  ----     ------            ----                ----               -------
  Warning  FailedScheduling  40s (x3 over 2m3s)  default-scheduler  0/1 nodes are available: 1 node(s) had no available volume zone.
```

4、修改PVC对象中的容量，扩容至40G
```shell
kubectl patch pvc www1-ivantestweb-0 -p '{"spec":{"resources":{"requests":{"storage":"40Gi"}}}}'
```

5、去掉PV对象之前打的标签，这样pod就能调度成功了。
```shell
$ kubectl label pv pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c failure-domain.beta.kubernetes.io/zone-
persistentvolume/pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c labeled
```
稍等片刻，pod running，对应的pv和文件系统也扩容成功，从30G扩容到40G了
```shell
$ kubectl get pod ivantestweb-0
NAME            READY   STATUS    RESTARTS   AGE
ivantestweb-0   1/1     Running   0          17m

$ kubectl get pv pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS   REASON   AGE
pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c   40Gi       RWO            Delete           Bound    default/www1-ivantestweb-0   cbs-csi                 20h

$ kubectl get pvc www1-ivantestweb-0
NAME                 STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
www1-ivantestweb-0   Bound    pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c   40Gi       RWO            cbs-csi        20h

$ kubectl exec ivantestweb-0 df /usr/share/nginx/html
Filesystem     1K-blocks  Used Available Use% Mounted on
/dev/vdd        41153760 49032  41088344   1% /usr/share/nginx/html

```


### 3、如何创建快照和使用快照来恢复卷？
#### 3.1 使用前注意
- TKE集群版本>=1.18，详见[cbs csi文档](https://github.com/TencentCloud/kubernetes-csi-tencentcloud/blob/master/docs/README_CBS.md "cbs csi文档")
- 仅cbs csi插件支持快照，确保csi插件镜像为最新版本

#### 3.2 如何使用
##### 3.2.1 使用快照备份云硬盘
1、使用下面yaml，创建`VolumeSnapshotClass`对象

```yaml
apiVersion: snapshot.storage.k8s.io/v1beta1
kind: VolumeSnapshotClass
metadata:
  name: cbs-snapclass
driver: com.tencent.cloud.csi.cbs
deletionPolicy: Delete
```
创建后显示：
```shell
$ kubectl get volumesnapshotclass
NAME            DRIVER                      DELETIONPOLICY   AGE
cbs-snapclass   com.tencent.cloud.csi.cbs   Delete           17m
```
2、使用下面yaml，创建
```yaml
apiVersion: snapshot.storage.k8s.io/v1beta1
kind: VolumeSnapshot
metadata:
  name: new-snapshot-demo
spec:
  volumeSnapshotClassName: cbs-snapclass
  source:
    persistentVolumeClaimName: csi-pvc
```
创建后稍等片刻，volumesnapshot和volumesnapshotcontent对象都创建成功，`READYTOUSE`为true：
```shell
$ kubectl get volumesnapshot
NAME                READYTOUSE   SOURCEPVC            SOURCESNAPSHOTCONTENT   RESTORESIZE   SNAPSHOTCLASS   SNAPSHOTCONTENT                                    CREATIONTIME   AGE
new-snapshot-demo   true         www1-ivantestweb-0                           10Gi          cbs-snapclass   snapcontent-ea11a797-d438-4410-ae21-41d9147fe610   22m            22m

$ kubectl get volumesnapshotcontent
NAME                                               READYTOUSE   RESTORESIZE   DELETIONPOLICY   DRIVER                      VOLUMESNAPSHOTCLASS   VOLUMESNAPSHOT      AGE
snapcontent-ea11a797-d438-4410-ae21-41d9147fe610   true         10737418240   Delete           com.tencent.cloud.csi.cbs   cbs-snapclass         new-snapshot-demo   22m
```
具体快照id在volumesnapshotcontent对象中，`status.snapshotHandle`(snap-e406fc9m)，可以根据这个快照id在腾讯云控制台确认快照是否存在
```shell
$ kubectl get volumesnapshotcontent snapcontent-ea11a797-d438-4410-ae21-41d9147fe610 -oyaml
apiVersion: snapshot.storage.k8s.io/v1beta1
kind: VolumeSnapshotContent
metadata:
  creationTimestamp: "2020-11-04T08:58:39Z"
  finalizers:
  - snapshot.storage.kubernetes.io/volumesnapshotcontent-bound-protection
  name: snapcontent-ea11a797-d438-4410-ae21-41d9147fe610
  resourceVersion: "471437790"
  selfLink: /apis/snapshot.storage.k8s.io/v1beta1/volumesnapshotcontents/snapcontent-ea11a797-d438-4410-ae21-41d9147fe610
  uid: 70d0390b-79b8-4276-aa79-a32e3bdef3d6
spec:
  deletionPolicy: Delete
  driver: com.tencent.cloud.csi.cbs
  source:
    volumeHandle: disk-7z32tin5
  volumeSnapshotClassName: cbs-snapclass
  volumeSnapshotRef:
    apiVersion: snapshot.storage.k8s.io/v1beta1
    kind: VolumeSnapshot
    name: new-snapshot-demo
    namespace: default
    resourceVersion: "471418661"
    uid: ea11a797-d438-4410-ae21-41d9147fe610
status:
  creationTime: 1604480319000000000
  readyToUse: true
  restoreSize: 10737418240
  snapshotHandle: snap-e406fc9m
```
##### 3.2.2 从快照恢复卷（云硬盘）
1、我们在3.2.1中创建的`VolumeSnapshot`的对象名为`new-snapshot-demo`，使用下面yaml来从快照恢复一个卷
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: restore-test
spec:
  storageClassName: cbs-csi
  dataSource:
    name: new-snapshot-demo
    kind: VolumeSnapshot
    apiGroup: snapshot.storage.k8s.io
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```
发现restore的pvc已经创建出来，diskid也在pv中（disk-gahz1kw1）
```shell
$ kubectl get pvc restore-test
NAME           STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
restore-test   Bound    pvc-80b98084-29a3-4a38-a96c-2f284042cf4f   10Gi       RWO            cbs-csi        97s

$ kubectl get pv pvc-80b98084-29a3-4a38-a96c-2f284042cf4f -oyaml
apiVersion: v1
kind: PersistentVolume
metadata:
  annotations:
    pv.kubernetes.io/provisioned-by: com.tencent.cloud.csi.cbs
  creationTimestamp: "2020-11-04T12:08:25Z"
  finalizers:
  - kubernetes.io/pv-protection
  name: pvc-80b98084-29a3-4a38-a96c-2f284042cf4f
  resourceVersion: "474676883"
  selfLink: /api/v1/persistentvolumes/pvc-80b98084-29a3-4a38-a96c-2f284042cf4f
  uid: 5321df93-5f21-4895-bafc-71538d50293a
spec:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 10Gi
  claimRef:
    apiVersion: v1
    kind: PersistentVolumeClaim
    name: restore-test
    namespace: default
    resourceVersion: "474675088"
    uid: 80b98084-29a3-4a38-a96c-2f284042cf4f
  csi:
    driver: com.tencent.cloud.csi.cbs
    fsType: ext4
    volumeAttributes:
      diskType: CLOUD_PREMIUM
      storage.kubernetes.io/csiProvisionerIdentity: 1604478835151-8081-com.tencent.cloud.csi.cbs
    volumeHandle: disk-gahz1kw1
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: topology.com.tencent.cloud.csi.cbs/zone
          operator: In
          values:
          - ap-beijing-2
  persistentVolumeReclaimPolicy: Delete
  storageClassName: cbs-csi
  volumeMode: Filesystem
status:
  phase: Bound
```

## 参考
- https://medium.com/velotio-perspectives/kubernetes-csi-in-action-explained-with-features-and-use-cases-4f966b910774
- https://github.com/kubernetes/community/blob/master/contributors/design-proposals/storage/container-storage-interface.md
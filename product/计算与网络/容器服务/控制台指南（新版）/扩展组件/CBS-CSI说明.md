## 操作场景


[CBS-CSI 组件](https://github.com/TencentCloud/kubernetes-csi-tencentcloud/blob/master/docs/README_CBS.md) 支持 TKE 集群通过控制台快捷选择存储类型，并创建对应块存储云硬盘类型的 PV 和 PVC。本文提供 CBS-CSI 组件功能特性等说明并介绍几种常见示例用法。


## 功能特性


| 功能| 说明 | 
|---------|---------|
|静态数据卷 | 支持手动创建 Volume、PV 对象及 PVC 对象 | 
| 动态数据卷| 支持通过 StorageClass 配置、创建和删除 Volume 及 PV 对象 | 
| 存储拓扑感知| 云硬盘不支持跨可用区挂载，在多可用区集群中，CBS-CSI 组件将先调度 Pod，后调度 Node 的 zone 创建 Volume | 
| 调度器感知节点 maxAttachLimit | 腾讯云单个云服务器上默认最多挂载20块云硬盘，调度器调度 Pod 时将过滤超过最大可挂载云硬盘数量的节点| 
| 卷在线扩容| 支持通过修改 PVC 容量字段，实现在线扩容（仅支持云硬盘类型） | 
| 卷快照和恢复| 支持通过快照创建数据卷 | 


## 组件说明


CBS-CSI 组件在集群内部署后，包含以下组件：

- DaemonSet：每个 Node 提供一个 DaemonSet，简称为 NodePlugin。由 CBS-CSI Driver 和 node-driver-registrar 两个容器组成，负责向节点注册 Driver，并提供挂载能力。
- StatefulSet 和 Deployment：简称为 Controller。由 Driver 和多个 Sidecar（external-provisioner、external-attacher、external-resizer、external-snapshotter、snapshot-controller）一起构成，提供创删卷、attach、detach、扩容、快照等能力。

![](https://main.qcloudimg.com/raw/f469674c69e02fc912b65d0babc001bd.png)



## 限制条件

- TKE 集群版本 ≥ 1.14
- 使用 CBS-CSI 组件后，才可在 TKE 集群中为云硬盘在线扩容和创建快照。
- 已经使用 QcloudCbs（In-Tree 插件）的 TKE 集群，可以继续正常使用。（后续将通过 Volume Migration 统一到 CBS CSI）



## 使用示例

### 示例1：通过 CBS-CSI 避免云硬盘跨可用区挂载


云硬盘不支持跨可用区挂载到节点，在跨可用区的集群环境中，推荐通过 CBS-CSI **拓扑感知**特性来避免跨可用区挂载问题。


#### 实现原理

拓扑感知调度需要多个 Kubernetes 组件配合完成，包括 Scheduler、PV controller、external-provisioner。具体流程如下：

1. PV controller 观察 PVC 对象，检查 Storageclass 的 VolumeBindingMode 是否为 **WaitForFirstConsumer**，如是，则不会立即处理该 PVC 的创建事件，等待 Scheduler 处理。
2. Scheduler 调度 Pod 后，会将 nodeName 以 annotation 的方式加入到 PVC 对象上 `volume.kubernetes.io/selected-node: 10.0.0.72`。
3. PV controller 获取到 PVC 对象的更新事件后，将开始处理 annotation（`volume.kubernetes.io/selected-node`），根据 nodeName 获取 Node 对象，传入到 external-provisioner 中。
4. external-provisioner 根据传过来的 Node 对象的 label 获取可用区（`failure-domain.beta.kubernetes.io/zone`）后在对应可用区创建 PV，达到和 Pod 相同可用区的效果，避免云硬盘和 Node 在不同可用区而无法挂载问题。





#### 前提条件

- 已安装1.14或以上版本的 [TKE 集群](https://cloud.tencent.com/document/product/457/32189)。
- 已将  [CBS-CSI](https://github.com/TencentCloud/kubernetes-csi-tencentcloud/blob/master/docs/README_CBS.md) 或 In-Tree 组件更新为最新版本。


#### 操作步骤

使用以下 YAML，在 Storageclass 中设置 volumeBindingMode 为 **WaitForFirstConsumer**。示例如下：

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

>?CBS-CSI 和 In-Tree 组件均支持该操作。


### 示例2：在线扩容云硬盘

TKE 支持在线扩容 PV、对应的云硬盘及文件系统，即不需要重启 Pod 即可完成扩容。为确保文件系统的稳定性，建议在云硬盘文件系统处于未挂载状态时进行操作。


#### 前提条件

- 已创建1.16或以上版本的 [TKE 集群](https://cloud.tencent.com/document/product/457/32189)。
- 已将 [CBS-CSI](https://github.com/TencentCloud/kubernetes-csi-tencentcloud/blob/master/docs/README_CBS.md) 更新为最新版本。
- （可选）为避免扩容失败导致数据丢失，可以在扩容前 [使用快照备份数据](#backup)。





#### 创建允许扩容的 StorageClass

使用以下 YAML 创建允许扩容的 StorageClass，在 Storageclass 中设置 `allowVolumeExpansion` 为 `true`。示例如下：
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


#### 在线扩容

提供以下两种扩容方式：

| 扩容方式 | 说明| 
|---------|---------|
|重启 Pod 的情况下在线扩容| 待扩容的云硬盘文件系统未被挂载，能够避免扩容出错以及方式2存在的问题。**推荐使用该方式进行扩容**。 | 
|不重启 Pod 的情况下在线扩容| 在节点上挂载着待扩容的云硬盘文件系统，如果存在 I/O 进程，将可能出现文件系统扩容错误。| 




<dx-tabs>
::: 重启Pod情况下在线扩容
1. 执行以下命令，确认扩容前 PV 和文件系统状态。示例如下，PV 和文件系统大小均为30G：
<dx-codeblock>
::: plaintext
$ kubectl exec ivantestweb-0 df /usr/share/nginx/html
Filesystem     1K-blocks  Used Available Use% Mounted on
/dev/vdd        30832548 44992  30771172   1% /usr/share/nginx/html

$ kubectl get pv pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c 
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS   REASON   AGE
pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c   30Gi       RWO            Delete           Bound    default/www1-ivantestweb-0   cbs-csi                 20h
:::
</dx-codeblock>
2. 执行以下命令，为 PV 对象打上一个非法 zone 标签，旨在下一步重启 Pod 后，使 Pod 无法调度到某个节点上。示例如下：
<dx-codeblock>
::: plaintext
$ kubectl label pv pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c failure-domain.beta.kubernetes.io/zone=nozone
:::
</dx-codeblock>
3. 执行以下命令重启 Pod，重启后由于 Pod 对应的 PV 的标签表明的是非法 zone，Pod 将处于 Pending 状态。示例如下：
<dx-codeblock>
::: plaintext
$ kubectl delete pod ivantestweb-0

$ kubectl get pod ivantestweb-0
NAME            READY   STATUS    RESTARTS   AGE
ivantestweb-0   0/1     Pending   0          25s

$ kubectl describe pod ivantestweb-0
Events:
  Type     Reason            Age                 From               Message
  ----     ------            ----                ----               -------
  Warning  FailedScheduling  40s (x3 over 2m3s)  default-scheduler  0/1 nodes are available: 1 node(s) had no available volume zone.
:::
</dx-codeblock>
4. 执行以下命令，修改 PVC 对象中的容量，将容量扩容至40G。示例如下：
<dx-codeblock>
::: plaintext
kubectl patch pvc www1-ivantestweb-0 -p '{"spec":{"resources":{"requests":{"storage":"40Gi"}}}}'
:::
</dx-codeblock>
5. 执行以下命令，去除 PV 对象之前打上的标签， 标签去除之后 Pod 即可调度成功。示例如下：
<dx-codeblock>
::: plaintext
$ kubectl label pv pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c failure-domain.beta.kubernetes.io/zone-
persistentvolume/pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c labeled
:::
</dx-codeblock>
6. 执行以下命令，可以查看到 Pod 状态为 Running、对应的 PV 和文件系统扩容成功，从30G扩容到40G。示例如下：
<dx-codeblock>
::: plaintext
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
:::
</dx-codeblock>
:::
::: 不重启Pod情况下在线扩容
1. 执行以下命令，确认扩容前 PV 和文件系统状态。示例如下，PV 和文件系统大小均为20G：
<dx-codeblock>
::: plaintext
$ kubectl exec ivantestweb-0 df /usr/share/nginx/html
Filesystem     1K-blocks  Used Available Use% Mounted on
/dev/vdd        20511312 45036  20449892   1% /usr/share/nginx/html

$ kubectl get pv pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS   REASON   AGE
pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c   20Gi       RWO            Delete           Bound    default/www1-ivantestweb-0   cbs-csi                 20h
:::
</dx-codeblock>
2. 执行以下命令，修改 PVC 对象中的容量，将容量扩容至30G。示例如下：
<dx-codeblock>
::: plaintext
$ kubectl patch pvc www1-ivantestweb-0 -p '{"spec":{"resources":{"requests":{"storage":"30Gi"}}}}'
:::
</dx-codeblock>
3. 执行以下命令，可以查看到 PV 和文件系统已扩容至30G。示例如下：
<dx-codeblock>
::: plaintext
$ kubectl exec ivantestweb-0 df /usr/share/nginx/html
Filesystem     1K-blocks  Used Available Use% Mounted on
/dev/vdd        30832548 44992  30771172   1% /usr/share/nginx/html
$ kubectl get pv pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                        STORAGECLASS   REASON   AGE
pvc-e193201e-6f6d-48cf-b96d-ccc09225cf9c   30Gi       RWO            Delete           Bound    default/www1-ivantestweb-0   cbs-csi                 20h
:::
</dx-codeblock>
:::
</dx-codeblock>
</dx-tabs>




### 示例3：创建快照和使用快照来恢复卷[](id:backup)


#### 前提条件


- 已创建1.18或以上版本的 [TKE 集群](https://cloud.tencent.com/document/product/457/32189)。
- 已安装最新版的 [CBS-CSI](https://github.com/TencentCloud/kubernetes-csi-tencentcloud/blob/master/docs/README_CBS.md "cbs csi文档") 组件。
- 在 [访问管理](https://console.cloud.tencent.com/cam/role) 控制台完成对 `TKE_QCSRole` 角色授予 CBS快照操作的相关权限，详情请参考 [快照授权](#authorize)。




#### 使用快照备份云硬盘

1. 使用以下 YAML，创建 VolumeSnapshotClass 对象。示例如下：
<dx-codeblock>
::: yaml
apiVersion: snapshot.storage.k8s.io/v1beta1
kind: VolumeSnapshotClass
metadata: 
  name: cbs-snapclass
driver: com.tencent.cloud.csi.cbs
deletionPolicy: Delete
:::
</dx-codeblock>
2. 创建后，执行以下命令查看 VolumeSnapshotClass 对象信息。示例如下：
```plaintext
$ kubectl get volumesnapshotclass
NAME            DRIVER                      DELETIONPOLICY   AGE
cbs-snapclass   com.tencent.cloud.csi.cbs   Delete           17m
```
3. [](id:volumeSnapshot)本文以 `new-snapshot-demo` 快照名为例使用以下 YAML，创建 VolumeSnapshot。示例如下：
<dx-codeblock>
::: yaml
apiVersion: snapshot.storage.k8s.io/v1beta1
kind: VolumeSnapshot
metadata: 
  name: new-snapshot-demo
spec: 
  volumeSnapshotClassName: cbs-snapclass
  source: 
    persistentVolumeClaimName: csi-pvc
:::
</dx-codeblock>
4. 执行以下命令，查看 Volumesnapshot 和 Volumesnapshotcontent 对象是否创建成功，若 `READYTOUSE` 为 true，则创建成功。示例如下：
```plaintext
$ kubectl get volumesnapshot
NAME                READYTOUSE   SOURCEPVC            SOURCESNAPSHOTCONTENT   RESTORESIZE   SNAPSHOTCLASS   SNAPSHOTCONTENT                                    CREATIONTIME   AGE
new-snapshot-demo   true         www1-ivantestweb-0                           10Gi          cbs-snapclass   snapcontent-ea11a797-d438-4410-ae21-41d9147fe610   22m            22m

$ kubectl get volumesnapshotcontent
NAME                                               READYTOUSE   RESTORESIZE   DELETIONPOLICY   DRIVER                      VOLUMESNAPSHOTCLASS   VOLUMESNAPSHOT      AGE
snapcontent-ea11a797-d438-4410-ae21-41d9147fe610   true         10737418240   Delete           com.tencent.cloud.csi.cbs   cbs-snapclass         new-snapshot-demo   22m
```
5. 执行以下命令，可以获取 Volumesnapshotcontent 对象的快照 ID，字段是 `status.snapshotHandle`（如下为 snap-e406fc9m），可以根据快照 ID 在 [容器服务控制台](https://console.cloud.tencent.com/tke2) 确认快照是否存在。示例如下：
<dx-codeblock>
:::  plaintext
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
:::
</dx-codeblock>

#### 从快照恢复卷（云硬盘）

1. 本文以上述 [步骤](#volumeSnapshot) 中创建的 VolumeSnapshot 的对象名为 `new-snapshot-demo` 为例，使用以下 YAML 从快照恢复卷。示例如下：
<dx-codeblock>
::: yaml
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
:::
</dx-codeblock>
2. 执行以下命令，查看恢复的 PVC 已成功创建，从 PV 中可以查看到对应的 diskid（如下为 disk-gahz1kw1）。示例如下：
<dx-codeblock>
:::  plaintext
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
:::
</dx-codeblock>

## 相关操作
### 快照授权 [](id:authorize)


使用 CBS-CSI 插件的 [创建快照和使用快照来恢复卷](#backup) 功能时，需给容器服务角色 `TKE_QCSRole` 授予快照等相关资源的操作。

#### 步骤1：创建自定义策略
1. 登录 [访问管理](https://console.cloud.tencent.com/cam/role)  控制台，选择左侧导航栏的**策略**。
2. 在“策略”列表页面中，单击**新建自定义策略**，创建策略方式选择**按策略生成器创建**。
3. 在“编辑策略”列表页面中选择**JSON**，将如下代码复制并替换到文本框中，并点击“下一步”。
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cvm:CreateSnapshot",
                "cvm:DeleteSnapshot",
                "cvm:DescribeSnapshots"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```

4. 在“关联用户/用户组”页面指定策略名称。此处设置为 `QcloudAccessForTKERoleInCBSSnapshot` 并关联用户/用户组。
5. 单击**确定**即可完成自定义策略的设定。


#### 步骤2：绑定策略到角色
1. 登录 [访问管理](https://console.cloud.tencent.com/cam/role)  控制台，选择左侧导航栏的**角色**。
2. 在“角色”列表页面中，搜索 TKE_QCSRole 进入该角色管理页面。
3. 选择 “TKE_QCSRole” 页面中的**关联策略**，并在弹出的“风险提醒”窗口中进行确认。如下图所示：
![](https://main.qcloudimg.com/raw/5cf2f5e7f0b180ff81da622cf40b3467.png)
4. 在弹出的“关联策略”窗口中，选择自定义 `QcloudAccessForTKERoleInCBSSnapshot` 策略。
5. 单击**确定**即可完成授权。

#### 权限内容

| 权限名称 | 权限说明 |
|---------|---------|
| cvm:CreateSnapshot | 创建快照 |
| cvm:DeleteSnapshot | 删除快照 |
| cvm:DescribeSnapshots | 描述快照列表 |

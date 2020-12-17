## CBS-CSI说明

### 使用场景

安装该组件后，您可以在集群内通过云控制台很方便地选择存储类型并创建对应块存储云硬盘类型的PV/PVC。

### CBS-CSI功能

- *静态数据卷*：即手动创建volme、PV对象、PVC对象
- *动态数据卷*：根据StorageClass配置来由插件控制创建和删除volume和PV
- *存储拓扑感知*：CBS不支持跨可用区挂载，在多可用区集群中，会先调度pod，然后去调度后的node的zone创建v
- *调度器感知节点maxAttachLimi*：
- *卷在线扩容*： 通过修改pvc容量字段，实现在线扩容（注：仅支持云硬盘类型）
- *卷快照&恢复*：通过快照创建数据卷

### CBS-CSI使用限制

- TKE集群版本为1.14+
- 需要在TKE集群中对CBS盘在线扩容和使用快照功能，使用CSI插件
- 已经使用了QcloudCbs（In-Tree插件）的，可以继续使用。（后续会通过Volume Migration统一到CBS CSI）

### CBS-CS部署组件

将在集群内部署以下组件：

- 一个DaemonSet，也就是每个Node会有一个，我们可以简单称为 NodePlugin，由CBS CSI Driver和node-driver-registrar两个容器组成。负责向节点注册driver，并提供mount的能力。
- 一个StatefulSet/Deployment，我们可以简称为 Controller。由driver和多个sidecar（external-provisioner、external-attacher、external-resizer、external-snapshotter、snapshot-controller）一起构成，提供创删卷、attach/detach、扩容、快照等能力

![](https://main.qcloudimg.com/raw/f469674c69e02fc912b65d0babc001bd.png)

## CBS-CSI使用示例

### 1、如果集群节点跨zone，如何避免cbs云盘跨可用区挂载？

cbs云盘不支持跨可用区挂载到节点，所以在跨可用区的集群中推荐通过***拓扑感知***特性来避免跨可用区挂载的问题。

#### 1.1 使用前注意

- TKE集群版本>=1.14
- 确保intree或csi插件为最新版本

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

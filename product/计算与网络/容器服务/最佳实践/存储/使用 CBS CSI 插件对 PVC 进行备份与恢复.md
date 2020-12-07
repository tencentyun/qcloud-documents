## 背景

如果想要对 PVC 的数据盘创建快照来备份数据，或者将快照备份的数据恢复到新的 PVC 中，可以使用 CBS CSI 插件来实现，本文将介绍如何利用 CBS CSI 插件实现 PVC 的数据备份与恢复。

## 前提条件

* 使用 TKE 集群或在腾讯云上自建 K8S 集群，且集群版本 >= 1.18。
* 安装了 CSI 插件，参考 [官方文档](https://github.com/TencentCloud/kubernetes-csi-tencentcloud/blob/master/docs/README_CBS.md)。

## 备份 PVC

### 创建 VolumeSnapshotClass

使用下面 yaml，创建 `VolumeSnapshotClass` 对象:

``` yaml
apiVersion: snapshot.storage.k8s.io/v1beta1
kind: VolumeSnapshotClass
metadata:
  name: cbs-snapclass
driver: com.tencent.cloud.csi.cbs
deletionPolicy: Delete
```

创建后检查下：

``` bash
$ kubectl get volumesnapshotclass
NAME            DRIVER                      DELETIONPOLICY   AGE
cbs-snapclass   com.tencent.cloud.csi.cbs   Delete           17m
```

### 创建 VolumeSnapshot 为 PVC 创建快照

使用下面 yaml，创建 `VolumeSnapshot` 对象:

``` yaml
apiVersion: snapshot.storage.k8s.io/v1beta1
kind: VolumeSnapshot
metadata:
  name: new-snapshot-demo
spec:
  volumeSnapshotClassName: cbs-snapclass # 引用前面创建的 VolumeSnapshotClass
  source:
    persistentVolumeClaimName: ssd-pvc # 替换成要备份的 pvc 名称
```

创建后稍等片刻，volumesnapshot 和 volumesnapshotcontent 对象都创建成功，`READYTOUSE` 为true：

``` bash
$ kubectl get volumesnapshot
NAME                READYTOUSE   SOURCEPVC   SOURCESNAPSHOTCONTENT   RESTORESIZE   SNAPSHOTCLASS   SNAPSHOTCONTENT                                    CREATIONTIME   AGE
new-snapshot-demo   true         ssd-pvc                             20Gi          cbs-snapclass   snapcontent-170b2161-f158-4c9e-a090-a38fdfd84a3e   2m36s          2m50s
$ kubectl get volumesnapshotcontent
NAME                                               READYTOUSE   RESTORESIZE   DELETIONPOLICY   DRIVER                      VOLUMESNAPSHOTCLASS   VOLUMESNAPSHOT      AGE
snapcontent-170b2161-f158-4c9e-a090-a38fdfd84a3e   true         21474836480   Delete           com.tencent.cloud.csi.cbs   cbs-snapclass         new-snapshot-demo   3m3s
```

具体快照 id 在 volumesnapshotcontent 对象中，字段是 `status.snapshotHandle` (snap-rsk8v75j)，可以根据这个快照 id 在腾讯云控制台确认快照是否存在

``` bash
$ kubectl get volumesnapshotcontent -o yaml snapcontent-170b2161-f158-4c9e-a090-a38fdfd84a3e
...
status:
  creationTime: 1607331318000000000
  readyToUse: true
  restoreSize: 21474836480
  snapshotHandle: snap-rsk8v75j
```

## 从快照恢复数据到新 PVC

我们在前面创建的 `VolumeSnapshot` 的对象名为 `new-snapshot-demo`，使用下面 yaml 来从快照恢复数据到新的 PVC 中:

``` yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: restore-test
spec:
  storageClassName: ssd-csi # storage class 根据自身需求自定义
  dataSource:
    name: new-snapshot-demo # 引用前面创建的 VolumeSnapshot
    kind: VolumeSnapshot
    apiGroup: snapshot.storage.k8s.io
  accessModes:
    - ReadWriteOnce # CBS 是块存储，只支持单机读写
  resources:
    requests:
      storage: 50Gi # 建议大小与被恢复的 PVC 写成一致
```

可以看到 pvc 已经创建并绑定 pv，从 pv 中也可以看到对应的 diskid (disk-ju0hw7no):

``` bash
$ kubectl get pvc restore-test
NAME           STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
restore-test   Bound    pvc-940edf09-d622-4126-992b-0a209f048c7d   60Gi       RWO            ssd-topology   6m8s
$ kubectl get pv pvc-940edf09-d622-4126-992b-0a209f048c7d -o yaml
...
spec:
...
    volumeHandle: disk-ju0hw7no
...
```

如果 StorageClass 使用了拓扑感知(先调度 Pod 再创建 PV)，即指定 `volumeBindingMode: WaitForFirstConsumer`，则需要先部署 Pod (需挂载 PVC) 才会触发创建 PV (从快照创建新的 CBS 并与 PV 绑定)。
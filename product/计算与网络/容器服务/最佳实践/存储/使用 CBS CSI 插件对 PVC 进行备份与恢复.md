## 操作场景

如需为 PVC 数据盘创建快照来备份数据，或者将备份的快照数据恢复到新的 PVC 中，可以通过 CBS-CSI 插件来实现，本文将介绍如何利用 CBS-CSI 插件实现 PVC 的数据备份与恢复。


## 前提条件

- 已创建 [TKE 集群](https://cloud.tencent.com/document/product/457/32189) 或已在腾讯云自建 Kubernetes 集群，集群版本 >= 1.18。
- 已安装 [CBS-CSI 插件](https://github.com/TencentCloud/kubernetes-csi-tencentcloud/blob/master/docs/README_CBS.md)。
- 在 [访问管理](https://console.cloud.tencent.com/cam/role) 控制台完成对 `TKE_QCSRole` 角色授予 CBS 快照操作的相关权限，详情请参考 [快照授权](https://cloud.tencent.com/document/product/457/51099#authorize)。

## 操作步骤

### 备份 PVC

#### 创建 VolumeSnapshotClass

1. 使用以下 YAML，创建 VolumeSnapshotClass 对象。示例如下：
```yaml
apiVersion: snapshot.storage.k8s.io/v1beta1
kind: VolumeSnapshotClass
metadata:
      name: cbs-snapclass
driver: com.tencent.cloud.csi.cbs
deletionPolicy: Delete
```
2. 执行以下命令，检查 VolumeSnapshotClass 是否创建成功。示例如下：
```bash
$ kubectl get volumesnapshotclass
NAME            DRIVER                      DELETIONPOLICY   AGE
cbs-snapclass   com.tencent.cloud.csi.cbs   Delete           17m
```

#### 创建 PVC 快照 VolumeSnapshot

1. [](id:volumesnapshot)本文以 `new-snapshot-demo` 快照名为例创建 VolumeSnapshot。使用以下 YAML，创建 VolumeSnapshot 对象。示例如下：
```yaml
apiVersion: snapshot.storage.k8s.io/v1beta1
kind: VolumeSnapshot
metadata:
      name: new-snapshot-demo
spec:
      volumeSnapshotClassName: cbs-snapclass # 引用上述步骤创建的 VolumeSnapshotClass
      source:
        persistentVolumeClaimName: ssd-pvc # 替换成需要备份的 pvc 名称
```
2. 执行以下命令，查看 Volumesnapshot 和 Volumesnapshotcontent 对象是否创建成功，若 `READYTOUSE` 为 true，则创建成功。示例如下：
```plaintext
$ kubectl get volumesnapshot
NAME                READYTOUSE   SOURCEPVC   SOURCESNAPSHOTCONTENT   RESTORESIZE   SNAPSHOTCLASS   SNAPSHOTCONTENT                                    CREATIONTIME   AGE
new-snapshot-demo   true         ssd-pvc                             20Gi          cbs-snapclass   snapcontent-170b2161-f158-4c9e-a090-a38fdfd84a3e   2m36s          2m50s
$ kubectl get volumesnapshotcontent
NAME                                               READYTOUSE   RESTORESIZE   DELETIONPOLICY   DRIVER                      VOLUMESNAPSHOTCLASS   VOLUMESNAPSHOT      AGE
snapcontent-170b2161-f158-4c9e-a090-a38fdfd84a3e   true         21474836480   Delete           com.tencent.cloud.csi.cbs   cbs-snapclass         new-snapshot-demo   3m3s
```
3. 执行以下命令，可以获取 Volumesnapshotcontent 对象的快照 ID，字段是 `status.snapshotHandle`（如下为 snap-rsk8v75j），可以根据快照 ID 在 [容器服务控制台](https://console.cloud.tencent.com/tke2) 确认快照是否存在。示例如下：
```plaintext
$ kubectl get volumesnapshotcontent -o yaml snapcontent-170b2161-f158-4c9e-a090-a38fdfd84a3e
...
status:
  creationTime: 1607331318000000000
  readyToUse: true
  restoreSize: 21474836480
  snapshotHandle: snap-rsk8v75j
```

### 从快照恢复数据到新 PVC

1. 本文以上述 [步骤](#volumesnapshot) 创建的 VolumeSnapshot 对象名称 `new-snapshot-demo` 为例，使用以下 YAML 从快照恢复数据到新的 PVC 中。示例如下：
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
      name: restore-test
spec:
      storageClassName: ssd-csi # storage class 根据自身需求自定义
      dataSource:
        name: new-snapshot-demo # 引用上述步骤创建的 VolumeSnapshot
        kind: VolumeSnapshot
        apiGroup: snapshot.storage.k8s.io
      accessModes:
        - ReadWriteOnce # CBS 为块存储，只支持单机读写
      resources:
        requests:
          storage: 50Gi # 建议大小与被恢复的 PVC 写成一致
```
2. 执行以下命令，可以查看 PVC 已经创建并绑定 PV，从 PV 中也可以查看到对应的 diskid（如下为 disk-ju0hw7no）。示例如下：
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
>? 如果 StorageClass 使用了拓扑感知（先调度 Pod 再创建 PV），即指定 `volumeBindingMode: WaitForFirstConsumer`，则需要先部署 Pod（需挂载 PVC）才会触发创建 PV（从快照创建新的 CBS 并与 PV 绑定）。

## 概述

Kubernetes 抽象 PV（PersistentVolume）和 PVC（PersistentVolumeClaim）来挂载和使用存储。详见 [Kubernetes 官网文档](https://kubernetes.io/zh-cn/docs/concepts/storage/)。

- PV（Persistent Volume）：PV 对存储资源的封装，描述一个容器集群里的持久化存储卷，属于容器集群级别资源。
- PVC（Persistent Volume Claim）：PVC 对存储资源的申领，PVC 会消耗容器集群里的 PV 资源，若容器集群里无 PV 资源，会动态创建 PV 资源及底层存储。在 Pod 中关联 PVC，即可让 Pod 使用到存储资源。
- StorageClass 描述了容器集群里的 PV 和 PVC 的类型，PV 可基于 StorageClass 自动创建，减少创建并维护 PV 的工作，动态创建 PVC/PV 时需要指定 StorageClass。

数据加速器 GooseFSx 实现两种持久卷 PV类型：Local PV 和 CSI PV。

- Local PV（Local Persistent Volume）：Kubernetes 直接使用宿主机的挂载 GooseFSx 的目录，来持久化存储容器的数据。
- CSI PV：Kubernetes 采用 CSI（容器存储接口 Container Storage Interface，CSI）协议动态挂载 GooseFSx，来持久化存储容器的数据。

由于 GooseFSx 已在容器集群宿主机上挂载 GooseFSx 共享目录，使用 Local PV 更直接、更高效，推荐使用 Local PV 方式。


## 前提条件

- 已创建容器集群。例如，腾讯云 TKE（Tencent Kubernetes Engine，TKE）容器集群或者自建K8S（Kubernetes）容器集群。
- 容器集群和 GooseFSx 实例在同一个 VPC、同一个子网里。
- 容器集群宿主机的操作系统与 GooseFSx 兼容，可参见 [GooseFSx 兼容性列表](https://cloud.tencent.com/document/product/1424/77960)。
- 容器集群宿主机已挂载 GooseFSx 共享目录，参见 [GooseFSx 创建客户端](https://cloud.tencent.com/document/product/1424/77956)。


## 使用限制

1. GooseFSx 暂不支持 [TKE 超级节点](https://cloud.tencent.com/document/product/457/74014)，请使用 [TKE 节点池](https://cloud.tencent.com/document/product/457/43719) 来实现动态伸缩。 
2. GooseFSx 暂不支持基于 StorageClass 动态创建 PV。




## Local PV 操作步骤

### 1. 定义 PV 持久化卷的 yaml 文件样例 `local_goosefsx_pv.yaml`

>!请将里面的 local: path 更换成 GooseFSx 在宿主机上的挂载目录。


```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: csi-goosefsx-local-pv
spec:
  accessModes:
  - ReadWriteMany
  capacity:
    storage: 10Gi
  volumeMode: Filesystem
  persistentVolumeReclaimPolicy: Delete
  storageClassName: local-storage
  local:
(将此处的path更换成宿主机挂载GooseFSx的路径，然后删除此句提醒)
    path: /goosefsx/x_c60_ow1j60r9_proxy
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/arch
          operator: In
          values:
          - amd64
```

关键参数说明如下：


|参数  |   说明  |
|----|----|
|name: csi-goosefsx-local-pv   | 定义持久卷名称，根据实际情况进行修改。|
|accessModes:  - ReadWriteMany|定义访问模式，“ReadWriteMany” 是指可被多个节点以读写方式挂载。|
|storage: 10Gi|定义存储容量，“10Gi” 是10GiB 存储容量，此参数不会限制文件系统所供给的容量；实际存储容量是购买 GooseFSx 的容量，并随 GooseFSx 扩容而动态扩展；例如，购买 GooseFSx 容量是4.5TiB，存储容量是4.5TiB，非10GiB，扩容 GooseFSx 容量到9TiB，存储容量是9TiB。|
|volumeMode: Filesystem|定义持久卷模式，是文件系统。|
|persistentVolumeReclaimPolicy: Delete|  定义回收策略，删除。|
|storageClassName: local-storage |   定义持久卷所属的类 “local-storage”，持久卷申领必须属于同一个类 “local-storage”；名称 “local-storage” 与 storageclass 存储类文件的 name “local-storage”保持一致。|
|local: path: /goosefsx/x_c60_ow1j60r9_proxy  |   定义容器的存储空间来自宿主机的目录路径 “/goosefsx/x_c60_ow1j60r9_proxy”，即 GooseFSx 在宿主机上的挂载目录，根据实际情况进行修改。|
|nodeAffinity|  定义节点亲和性。|

### 2. 定义 PVC 持久化卷申领的 yaml 文件样例 `local_goosefsx_pvc.yaml`

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-goosefsx-pvc
spec:
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 10Gi
  storageClassName: local-storage
```


关键参数说明如下：


|参数  |   说明  |
|----|----|
|name: local-goosefsx-pvc|   定义持久卷申领的名称，根据实际情况进行修改。|
|accessModes:  - ReadWriteMany|  定义访问模式，与定义持久卷一样。|
|resources: requests: storage: 10Gi|   定义存储容量，“10Gi” 是10GiB 存储容量，此参数不会限制文件系统所提供的容量；实际存储容量是购买 GooseFSx 的容量，并随 GooseFSx 扩容而动态扩展；例如，购买 GooseFSx 容量是4.5TiB，存储容量是4.5TiB，非10GiB，扩容 GooseFSx 容量到9TiB，存储容量是9TiB。|
|storageClassName: local-storage|   定义持久卷申领 所属的类 “local-storage”，持久卷必须属于同一个类 “local-storage”；名称 “local-storage” 与 storageclass 存储类文件的 name “local-storage”保持一致。|


### 3. 定义 StorageClass 存储类的 yaml 文件样例 `local_goosefsx_storageclass.yaml`

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: local-storage
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer
```


关键参数说明如下：

|参数  |   说明  |
|----|----|
|name: local-storage|定义存储类的名称为 “local-storage”，PV 持久化卷的 yaml 文件和 PVC 持久化卷申领的 yaml 文件会用上。|
|provisioner: kubernetes.io/no-provisioner|定义 PV 持久化卷的 provisioner，GooseFSx 的 PV 持久化卷比较简单，不需要通过 StorageClass 来自动创建 PV 持久化卷。|
|volumeBindingMode：WaitForFirstConsumer|定义卷绑定模式，该模式将延迟 PersistentVolume 的绑定和制备，直到使用该 PersistentVolumeClaim 的 Pod 被创建。|


### 4. 执行命令创建 StorageClass、PV 和 PVC

执行如下命令创建 StorageClass：

```yaml
kubectl apply -f local_goosefsx_storageclass.yaml
```

![](https://qcloudimg.tencent-cloud.cn/raw/71c5b30b9c9377cb463c4c9e8cd7b15f.png)

执行如下命令创建 PV：

```yaml
kubectl apply -f local_goosefsx_pv.yaml
```

![](https://qcloudimg.tencent-cloud.cn/raw/631386d7da24542abfbb1f5800a4e66b.png)

执行如下命令创建 PVC：

```yaml
kubectl apply -f local_goosefsx_pvc.yaml
```

![](https://qcloudimg.tencent-cloud.cn/raw/19d7b1a783af0608f293a74ccc61456f.png)


### 5. 部署 Pod 挂载该 PVC

挂载该 PVC 的 Pod 的 yaml 文件样例 `local_goosefsx_pod.yaml` 如下：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    k8s-app: local-goosefsx-dp
  name: local-goosefsx-dp
spec:
  replicas: 1
  selector:
    matchLabels:
      k8s-app: local-goosefsx-pod
  template:
    metadata:
      labels:
        k8s-app: local-goosefsx-pod
    spec:
      containers:
        - image: nginx
          name: local-goosefsx-pod
          volumeMounts:
            - mountPath: /local-goosefsx
              name: local-goosefsx-pv
      volumes:
        - name: local-goosefsx-pv
          persistentVolumeClaim:
            claimName: local-goosefsx-pvc
```


部署 Pod：

```yaml
kubectl apply -f local_goosefsx_pod.yaml
```

![](https://qcloudimg.tencent-cloud.cn/raw/0a43e8862406319ce2d086c391835bef.png)

查看 Pod 是否处于 ready 状态：

```yaml
kubectl get pod
```

![](https://qcloudimg.tencent-cloud.cn/raw/1bfd5ebc7ec5d65aeeadf6ae0aa1de22.png)

登录到 Pod，查看挂载点是否正确，查看挂载点是否在线：

```yaml
kubectl exec -ti local-goosefsx-dp-7fb9b9f877-fcttx   -- /bin/sh
```

![](https://qcloudimg.tencent-cloud.cn/raw/ed9eb0023f636735992b4e0f4304ee40.png)




## CSI PV 操作步骤

静态创建 PV、PVC，不需要定义 StorageClass。

另外，需要定义 CSI 的3个 yaml 文件。CSI 代码已打入 TKE 镜像，您无需关注。


### 1. 定义 PV 的 yaml 文件

定义 PV 的 yaml 文件样例 `pv.yaml` ：
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: csi-goosefsx-pv
spec:
  accessModes:
  - ReadWriteMany
  capacity:
    storage: 10Gi
  csi:
    driver: com.tencent.cloud.csi.goosefsx
    volumeHandle: csi-goosefsx-pv
  storageClassName: ""
```


### 2. 定义 PVC 的 yaml 文件

定义 PVC 的 yaml 文件样例 `pvc.yaml` ：

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: csi-goosefsx-pvc
spec:
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 10Gi
  volumeName: csi-goosefsx-pv
  storageClassName: ""

```




### 3. 定义 CSI driver 的 yaml 文件

定义  CSI driver 的 yaml 文件样例 `csi-driver.yaml` ：
```yaml
apiVersion: storage.k8s.io/v1
kind: CSIDriver
metadata:
  name: com.tencent.cloud.csi.goosefsx
spec:
  attachRequired: false
  podInfoOnMount: false
  fsGroupPolicy: File

```


### 4. 定义 CSI node 的 yaml 文件

定义 CSI node 的 yaml 文件样例 `csi-node.yaml` ：

>!请将里面的 fileSystemId 更换成宿主机挂载的文件系统 ID。

```yaml
kind: DaemonSet
apiVersion: apps/v1
metadata:
  name: csi-goosefsx-node
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: csi-goosefsx-node
  template:
    metadata:
      labels:
        app: csi-goosefsx-node
    spec:
      serviceAccount: csi-goosefsx-node
      priorityClassName: system-node-critical
      hostNetwork: true
      hostPID: true
      containers:
        - name: driver-registrar
          image: ccr.ccs.tencentyun.com/tkeimages/csi-node-driver-registrar:v2.0.1
          lifecycle:
            preStop:
              exec:
                command: ["/bin/sh", "-c", "rm -rf /registration/com.tencent.cloud.csi.goosefex /registration/com.tencent.cloud.csi.goosefsx-reg.sock"]
          args:
            - "--v=5"
            - "--csi-address=$(ADDRESS)"
            - "--kubelet-registration-path=/var/lib/kubelet/plugins/com.tencent.cloud.csi.goosefsx/csi.sock"
          env:
            - name: ADDRESS
              value: /plugin/csi.sock
            - name: KUBE_NODE_NAME
              valueFrom:
                fieldRef:
                  fieldPath: spec.nodeName
          volumeMounts:
            - name: plugin-dir
              mountPath: /plugin
            - name: registration-dir
              mountPath: /registration
        - name: goosefsx
          securityContext:
            privileged: true
            capabilities:
              add: ["SYS_ADMIN"]
            allowPrivilegeEscalation: true
          image: ccr.ccs.tencentyun.com/qcloud_goosefsx/goosefsx-csi:v1.0.1
          args:
            - "--v=5"
            - "--logtostderr=true"
            - "--nodeID=$(NODE_ID)"
            - "--endpoint=$(CSI_ENDPOINT)"
(将此处的fileSystemId更换成宿主机挂载的文件系统ID，然后删除此句提醒)
            - "--filesystemId=x_c60_s1bz66l4"
          env:
            - name: NODE_ID
              valueFrom:
                fieldRef:
                  fieldPath: spec.nodeName
            - name: CSI_ENDPOINT
              value: unix://plugin/csi.sock
          volumeMounts:
            - name: plugin-dir
              mountPath: /plugin
            - name: goosefsx-mount-dir
              mountPath: /goosefsx
              mountPropagation: "Bidirectional"
            - name: pods-mount-dir
              mountPath: /var/lib/kubelet/pods
              mountPropagation: "Bidirectional"
      volumes:
        - name: plugin-dir
          hostPath:
            path: /var/lib/kubelet/plugins/com.tencent.cloud.csi.goosefsx
            type: DirectoryOrCreate
        - name: registration-dir
          hostPath:
            path: /var/lib/kubelet/plugins_registry
            type: Directory
        - name: pods-mount-dir
          hostPath:
            path: /var/lib/kubelet/pods
            type: Directory
        - name: goosefsx-mount-dir
          hostPath:
            path: /goosefsx
            type: Directory

```


### 5. 定义 CSI rbac 的 yaml 文件

定义 CSI rbac 的 yaml 文件样例 `csi-rbac.yaml` ：

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: csi-goosefsx-node
  namespace: kube-system

---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: csi-goosefsx-node
rules:
  - apiGroups: [""]
    resources: ["persistentvolumeclaims/status"]
    verbs: ["patch", "update"]
  - apiGroups: [""]
    resources: ["configmaps", "events", "persistentvolumes","persistentvolumeclaims"]
    verbs: ["get", "list", "watch", "update", "patch"]
  - apiGroups: [""]
    resources: ["pods", "nodes"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["storageclasses"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["volumeattachments"]
    verbs: ["get", "list", "watch", "update"]
  - apiGroups: [""]
    resources: ["events"]
    verbs: ["list", "watch", "create", "update", "patch"]
  - apiGroups: ["coordination.k8s.io"]
    resources: ["leases"]
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]

---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: csi-goosefsx-node
subjects:
  - kind: ServiceAccount
    name: csi-goosefsx-node
    namespace: kube-system
roleRef:
  kind: ClusterRole
  name: csi-goosefsx-node
  apiGroup: rbac.authorization.k8s.io

```


### 6. 执行命令完成创建 CSI、PV 和 PVC

执行如下命令配置 rbac、driver 和 node：

```yaml
kubectl apply -f csi-rbac.yaml
kubectl apply -f csi-driver.yaml
kubectl apply -f csi-node.yaml
```

执行如下命令查看工作是否正常：

```yaml
kubectl get ds -n kube-system
```

执行如下命令创建 PV 和 PVC：

```yaml
kubectl apply -f pv.yaml
kubectl apply -f pvc.yaml
```


### 7. 部署 Pod 挂载该 PVC

Pod 挂载该 PVC 的 `pod.yaml` 文件，样例如下：

>!将里面的 claimName 替换相应的 PVC 名称，即定义 PVC 的 yaml 文件（例如，pvc.yaml 文件样例）的 name: csi-goosefsx-pvc 。


```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    k8s-app: csi-goosefsx-pod
  name: csi-goosefsx-pod
spec:
  replicas: 1
  selector:
    matchLabels:
      k8s-app: csi-goosefsx-pod
  template:
    metadata:
      labels:
        k8s-app: csi-goosefsx-pod
    spec:
      containers:
        - image: nginx
          name: csi-goosefsx-pod
          volumeMounts:
            - mountPath: /csi-goosefsx
              name: csi-goosefsx
      volumes:
        - name: csi-goosefsx
          persistentVolumeClaim:
            claimName: csi-goosefsx-pvc

```

部署 Pod：


```yaml
kubectl apply -f pod.yaml
```


查看 Pod 是否处于 ready 状态：

```yaml
kubectl get pod
```

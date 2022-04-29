

## 操作场景

为 TKE 集群挂载 CFS Turbo 类型存储，可以通过安装 `kubernetes-csi-tencentloud` 组件来实现。该组件基于私有协议将腾讯云 CFS Turbo 文件系统挂载到工作负载，目前仅支持静态配置。CFS 存储类型请参考 [文件存储类型及性能规格](https://cloud.tencent.com/document/product/582/38112)。  

## 前提条件

已创建 TKE 集群或已在腾讯云自建 Kubernetes 集群，集群版本 >=1.14。  

## 操作步骤

### 创建文件系统 [](id:create-cfs)

创建 CFS Turbo 文件系统，具体操作请参见 [创建文件系统](https://cloud.tencent.com/document/product/582/9132)。  

>! 文件系统创建后，需将集群网络（vpc-xx）关联到文件系统的 [云联网](https://cloud.tencent.com/document/product/877/18747)（可在文件系统挂载点信息中查看）。  


### 部署 RBAC 策略

如果您需要挂载 CFS Turbo 存储卷，需执行 `kubectl apply -f  csi-node-rbac.yaml` 命令在集群中先部署 RBAC 策略，csi-node-rbac.yaml 代码参考如下：

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: cfsturbo-csi-node-sa
  namespace: kube-system
---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: cfsturbo-csi-node-role
rules:
  - apiGroups: [""]
    resources: ["persistentvolumes", "endpoints", "configmaps"]
    verbs: ["get", "list", "watch", "create", "delete", "update"]
  - apiGroups: [""]
    resources: ["persistentvolumeclaims", "nodes"]
    verbs: ["get", "list", "watch", "update"]
  - apiGroups: [""]
    resources: ["events"]
    verbs: ["get", "list", "watch", "create", "update", "patch"]
  - apiGroups: [""]
    resources: ["secrets", "namespaces"]
    verbs: ["get", "list"]
  - apiGroups: [""]
    resources: ["nodes", "pods"]
    verbs: ["get", "list", "watch", "update"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["volumeattachments", "volumeattachments"]
    verbs: ["get", "list", "watch", "update", "patch"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["storageclasses"]
    verbs: ["get", "list", "watch"]
---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: cfsturbo-csi-node-rolebinding
subjects:
  - kind: ServiceAccount
    name: cfsturbo-csi-node-sa
    namespace: kube-system
roleRef:
  kind: ClusterRole
  name: cfsturbo-csi-node-role
  apiGroup: rbac.authorization.k8s.io
```

### 部署 Node Plugin

1. 执行 `kubectl apply -f csidriver.yaml` 命令，csidriver.yaml 代码参考如下：
```yaml
apiVersion: storage.k8s.io/v1beta1
kind: CSIDriver
metadata:
  name: com.tencent.cloud.csi.cfsturbo
spec:
  attachRequired: false
  podInfoOnMount: false
```

2.  执行 `kubectl apply -f csi-node.yaml` 命令，csi-node.yaml 代码参考如下：
```yaml
# This YAML file contains driver-registrar & csi driver nodeplugin API objects
# that are necessary to run CSI nodeplugin for cfsturbo
kind: DaemonSet
apiVersion: apps/v1
metadata:
  name: cfsturbo-csi-node
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: cfsturbo-csi-node
  template:
    metadata:
      labels:
        app: cfsturbo-csi-node
    spec:
      serviceAccount: cfsturbo-csi-node-sa
      hostNetwork: true
      containers:
        - name: driver-registrar
          image: ccr.ccs.tencentyun.com/tkeimages/csi-node-driver-registrar:v1.2.0
          lifecycle:
            preStop:
              exec:
                command: ["/bin/sh", "-c", "rm -rf /registration/com.tencent.cloud.csi.cfsturbo /registration/com.tencent.cloud.csi.cfsturbo-reg.sock"]
          args:
            - "--v=5"
            - "--csi-address=/plugin/csi.sock"
            - "--kubelet-registration-path=/var/lib/kubelet/plugins/com.tencent.cloud.csi.cfsturbo/csi.sock"
          env:
            - name: KUBE_NODE_NAME
              valueFrom:
                fieldRef:
                  fieldPath: spec.nodeName
          volumeMounts:
            - name: plugin-dir
              mountPath: /plugin
            - name: registration-dir
              mountPath: /registration
        - name: cfsturbo
          securityContext:
            privileged: true
            capabilities:
              add: ["SYS_ADMIN"]
            allowPrivilegeEscalation: true
          image: ccr.ccs.tencentyun.com/tkeimages/csi-tencentcloud-cfsturbo:v1.2.2
          args :
            - "--nodeID=$(NODE_ID)"
            - "--endpoint=$(CSI_ENDPOINT)"
          env:
            - name: NODE_ID
              valueFrom:
                fieldRef:
                  fieldPath: spec.nodeName
            - name: CSI_ENDPOINT
              value: unix://plugin/csi.sock
          imagePullPolicy: "IfNotPresent"
          volumeMounts:
            - name: plugin-dir
              mountPath: /plugin
            - name: pods-mount-dir
              mountPath: /var/lib/kubelet/pods
              mountPropagation: "Bidirectional"
            - name: global-mount-dir
              mountPath: /etc/cfsturbo/global
              mountPropagation: "Bidirectional"
      volumes:
        - name: plugin-dir
          hostPath:
            path: /var/lib/kubelet/plugins/com.tencent.cloud.csi.cfsturbo
            type: DirectoryOrCreate
        - name: pods-mount-dir
          hostPath:
            path: /var/lib/kubelet/pods
            type: Directory
        - name: registration-dir
          hostPath:
            path: /var/lib/kubelet/plugins_registry
            type: Directory
        - name: global-mount-dir
          hostPath:
            path: /etc/cfsturbo/global
            type: DirectoryOrCreate
```


### 使用 CFS Turbo 存储卷

1. 创建 CFS Turbo 文件系统，具体操作请参见 [创建文件系统](#create-cfs)。  
2. 使用以下模板创建 CFS Turbo 类型的 PV。  
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-cfsturbo
spec:
  accessModes:
  - ReadWriteMany
  capacity:
    storage: 10Gi
  csi:
    driver: com.tencent.cloud.csi.cfsturbo
	  # volumeHandle in PV must be unique, use pv name is better
    volumeHandle: pv-cfsturbo
    volumeAttributes: 
      # cfs turbo server ip
      host: 10.0.0.116
      # cfs turbo fsid (not cfs id)
      fsid: xxxxxxxx
      # cfs turbo rootdir
      rootdir: /cfs
      # cfs turbo subPath
      path: /
      proto: lustre
  storageClassName: ""
```
参数说明：  
  - **metadata.name**: 创建 PV 名称。  
  - **spec.csi.volumeHandle**: 与 PV 名称保持一致。   
  - **spec.csi.volumeAttributes.host**: 文件系统 ip 地址，可在文件系统挂载点信息中查看。   
  - **spec.csi.volumeAttributes.fsid**: 文件系统 fsid（非文件系统 id），可在文件系统挂载点信息中查看（挂载命令中 “tcp0:/” 之后 “/cfs” 之前的那一段字符串，如下图）。
  - **spec.csi.volumeAttributes.rootdir**: 文件系统根目录，不填写默认为 “/cfs”（挂载到 “/cfs” 目录可相对提高整体挂载性能）。如需指定根目录挂载，须确保该根目录在文件系统中存在。
  - **spec.csi.volumeAttributes.path**: 文件系统子目录，不填写默认为 “/”。如需指定子目录挂载，须确保该子目录在文件系统 rootdir 中存在。容器最终访问到的是文件系统中 rootdir+path 目录（默认为 “/cfs/” 目录）。
  - **spec.csi.volumeAttributes.proto**：文件系统默认挂载协议。  
![](https://qcloudimg.tencent-cloud.cn/raw/357dd592683ac766f8e6b4c653a27951.png)
>! 使用 `lustre` 协议挂载 CFS Turbo 卷需预先在集群节点内根据操作系统内核版本安装对应客户端，详情请参考 [在 Linux 客户端上使用 CFS Turbo 文件系统](https://cloud.tencent.com/document/product/582/54765)；


3. 使用以下模板创建 PVC 绑定 PV。  
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-cfsturbo
spec:
  storageClassName: ""
  volumeName: pv-cfsturbo
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 10Gi
```
参数说明：  
  - **metadata.name**: 创建 PVC 名称。  
  - **spec.volumeName**: 与上一步中创建 PV 名称保持一致。  


4. 使用以下模板创建 Pod 挂载 PVC。  
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx 
spec:
  containers:
  - image: ccr.ccs.tencentyun.com/qcloud/nginx:1.9
    imagePullPolicy: Always
    name: nginx
    ports:
    - containerPort: 80
      protocol: TCP
    volumeMounts:
      - mountPath: /var/www
        name: data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: pvc-cfsturbo
```

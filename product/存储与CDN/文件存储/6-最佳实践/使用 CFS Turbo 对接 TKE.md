## 简介
本文为您介绍如何使用 CFS Turbo 对接容器服务（Tencent Kubernetes Engine，TKE）集群。


## 前提条件

- TKE 的宿主机节点满足 Turbo 系列兼容的操作系统。
- 已在所有 TKE 节点安装 Turbo 的私有客户端，推荐使用 pshell 工具进行批量操作。
相关的操作系统兼容列表及私有客户端安装方式，可参考 [在 Linux 客户端上使用 CFS Turbo 文件系统](https://cloud.tencent.com/document/product/582/54765) 文档。

## 操作步骤

### 下载和配置 kubectl

1. 参考 [kubectl 官方文档](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)，下载 kubectl。
2. 登录容器服务控制台，选择左侧导航栏中的**[集群](https://console.cloud.tencent.com/tke2/cluster)**。
3. 在“集群管理”页面，选择需要对接的集群 ID，进入集群详情页。
4. 在集群详情页面，选择左侧**基本信息**，进入基本信息页面。
5. 在“集群APIServer信息”栏中，单击**下载**，将 kubeconfig 文件保存至默认环境变量地址中，并命名为 config，即`/usr/local/bin/config`。
![](https://main.qcloudimg.com/raw/7ae1ece13d759989ecdabe7cf7feeda0.png)
6. <span id="step6"></span>在“集群APIServer信息”栏中，将内网访问设置为 ![](https://main.qcloudimg.com/raw/557ab76a34a9a1af96a81237e12882c3.png)，单击 ![](https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png)，复制配置 host 的命令。
7. 切换至访问机，并在访问机上执行 [步骤6](#step6) 复制的命令。
8. 执行如下命令，配置环境变量。
```
vi /etc/profile
KUBECONFIG=/usr/local/bin/config
PATH=$PATH
export KUBECONFIG
export PATH
```
7. 执行如下命令，验证 kubectl 是否完成安装。
```
kubectl get node
```
返回如下结果，即表示完成安装。
![](https://main.qcloudimg.com/raw/8bc11f2f8951c7e6037763dbe1bf190c.png)



### 通过 yaml 文件创建挂载 Turbo 的 POD

1. 阅读 [TKE Turbo 插件的说明文档](https://github.com/TencentCloud/kubernetes-csi-tencentcloud/blob/master/docs/README_CFSTURBO.md)，并 [下载](https://github.com/TencentCloud/kubernetes-csi-tencentcloud) 脚本文件。
2. 进入 `kubernetes-csi-tencentcloud/deploy/cfsturbo/kubernetes/` 目录，分别将 csi-node-rbac.yaml、csi-node.yaml 和 csidriver-new.yaml 文件上传至 kubectl 管理节点。
3. 进入 `kubernetes-csi-tencentcloud/deploy/cfsturbo/examples/` 目录，下载 pv.yaml、pvc.yaml、 
pod.yaml 这三个示例文件。
4. 根据实际 PV、PVC、POD 的相关属性（如名称、镜像地址等），修改 pv.yaml、pvc.yaml、 
pod.yaml 文件。
yaml 示例如下：
```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: csi-cfsturbo-pv
spec:
  accessModes:
  - ReadWriteMany
  capacity:
    storage: 10Gi
  csi:
    driver: com.tencent.cloud.csi.cfsturbo
    # volumeHandle in PV must be unique, use pv name is better
    volumeHandle: csi-cfsturbo-pv
    volumeAttributes:
      # cfs turbo proto
      proto: lustre
      # cfs turbo rootdir
      rootdir: /cfs
      # cfs turbo fsid (not cfs id)
      fsid: d3dcc487
      # cfs turbo server ip
      host: 10.0.1.16
      # cfs turbo subPath
      path: /
  storageClassName: ""
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: csi-cfsturbo-pvc
spec:
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 10Gi
  # You can specify the pv name manually or just let kubernetes to bind the pv and pvc.
  volumeName: csi-cfsturbo-pv
  # cfsturbo only supports static provisioning, the StorageClass name should be empty.
  storageClassName: ""
---
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    k8s-app: csi-cfsturbo-pod
  name: csi-cfsturbo-pod
spec:
  replicas: 1
  selector:
    matchLabels:
      k8s-app: csi-cfsturbo-pod
  template:
    metadata:
      labels:
        k8s-app: csi-cfsturbo-pod
    spec:
      containers:
        - image: nginx
          name: csi-cfsturbo-pod
          volumeMounts:
            - mountPath: /csi-cfsturbo
              name: csi-cfsturbo
      volumes:
        - name: csi-cfsturbo
          persistentVolumeClaim:
            # Replaced by your pvc name.
            claimName: csi-cfsturbo-pvc
```
以此挂载指令为例：
```
sudo mount.lustre -o sync,user_xattr 10.0.1.16@tcp0:/d3dcc487/cfs /path/to/mount
```
关键参数说明如下：
 - proto:lustre, 请保持此参数不要进行修改。
 - roodir:/cfs，请保持此参数不要进行修改。
 - fsid:d3dcc487，此处的 fsid 不是 CFSID，需要填写挂载路径里的信息。
 - host:10.0.1.16，挂载点 IP。
 - path 可根据实际需要挂载的子目录进行调整，若直接挂载根目录则填写"/"。
5. 在上传脚本文件的目录下，依次执行如下命令。
 - 配置 RBAC。
```
kubectl apply -f csi-node-rbac.yaml
```
 - 配置节点 CSI 插件。
```
kubectl apply -f csidriver-new.yaml
```
```
kubectl apply -f csi-node.yaml
```
 - 创建 PV、PVC、POD。
```
kubectl create -f pv.yaml
kubectl create -f pvc.yaml
kubectl create -f pod.yaml
```
6. 执行如下命令，查看 POD 状态。
```
kubectl get pod -n default -o wide
```
返回如下结果，即表示创建成功。
![](https://main.qcloudimg.com/raw/5e7014090522b1667afcc0b7d351fef9.png)
若状态（STATUS）持续为 ContainerCreating，即表示创建失败。您可在 TKE 控制台的事件中，查看失败原因。

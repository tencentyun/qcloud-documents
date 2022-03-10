## 概述

在 Fluid 中可以通过 nodeselector 来指定 master 节点的部署，例如选择部署 master 到性能较好的 k8s 机器上。

下面将向您简单地介绍上述特性。

## 前提条件

在运行该示例之前，请参考 [安装](https://cloud.tencent.com/document/product/436/59493) 文档完成安装，并检查 Fluid 各组件正常运行：

```shell
$ kubectl get pod -n fluid-system
goosefsruntime-controller-5b64fdbbb-84pc6   1/1     Running   0          8h
csi-nodeplugin-fluid-fwgjh                  2/2     Running   0          8h
csi-nodeplugin-fluid-ll8bq                  2/2     Running   0          8h
dataset-controller-5b7848dbbb-n44dj         1/1     Running   0          8h
```

通常来说，您会看到一个名为 `dataset-controller` 的 Pod、一个名为 `goosefsruntime-controller` 的 Pod 和多个名为`csi-nodeplugin`的 Pod 正在运行。其中 `csi-nodeplugin` 这些 Pod 的数量取决于您的 Kubernetes 集群中结点的数量。

## 新建工作环境

```shell
$ mkdir <any-path>/co-locality
$ cd <any-path>/co-locality
```
## 示例

### 查看全部结点
```shell
$ kubectl get nodes
NAME                       STATUS   ROLES    AGE     VERSION
192.168.1.146   Ready    <none>   7d14h  v1.18.4-tke.13
192.168.1.147   Ready    <none>   7d14h  v1.18.4-tke.13
```

### 使用标签标识结点

```shell
$ kubectl label nodes 192.168.1.146 hbase-cache=true
```

### 再次查看结点

```shell
$ kubectl get node -L hbase-cache
NAME                       STATUS   ROLES    AGE     VERSION            HBASE-CACHE
192.168.1.146   Ready    <none>   7d14h  v1.18.4-tke.13   true
192.168.1.147   Ready    <none>   7d14h  v1.18.4-tke.13
```

### 检查待创建的 Dataset 资源对象
```yaml
apiVersion: data.fluid.io/v1alpha1
kind: Dataset
metadata:
  name: hbase
spec:
  mounts:
    - mountPoint: https://mirrors.tuna.tsinghua.edu.cn/apache/hbase/stable/
      name: hbase
```

>? 为了方便用户进行测试，mountPoint 这里使用的是 Web UFS，使用 COS 作为 UFS 可参见 [使用 GooseFS 挂载 COS（COSN）](https://cloud.tencent.com/document/product/436/56413#.E4.BD.BF.E7.94.A8-goosefs-.E6.8C.82.E8.BD.BD-cos.EF.BC.88cosn.EF.BC.89-.E6.88.96.E8.85.BE.E8.AE.AF.E4.BA.91-hdfs.EF.BC.88chdfs.EF.BC.89)。
>

### 创建 Dataset 资源对象

```shell
$ kubectl create -f dataset.yaml
dataset.data.fluid.io/hbase created
```

### 检查待创建的 GooseFSRuntime 资源对象
```yaml
apiVersion: data.fluid.io/v1alpha1
kind: GooseFSRuntime
metadata:
  name: hbase
spec:
  replicas: 1
  tieredstore:
    levels:
      - mediumtype: MEM
        path: /dev/shm
        quota: 2G
        high: "0.8"
        low: "0.7"
  master:
    nodeSelector:
      hbase-cache: "true"
```
该配置文件片段中，包含了许多与 GooseFS 相关的配置信息，这些信息将被 Fluid 用来启动一个 GooseFS 实例。上述配置片段中的`spec.replicas`属性被设置为1，这表明 Fluid 将会启动一个包含1个 GooseFS Master 和1个 GooseFS Worker 的 GooseFS 实例。

### 创建 GooseFSRuntime 资源并查看状态

```shell
$ kubectl create -f runtime.yaml
goosefsruntime.data.fluid.io/hbase created



$ kubectl get pod -o wide
NAME                 READY   STATUS    RESTARTS   AGE    IP              NODE                       NOMINATED NODE   READINESS GATES
hbase-fuse-42csf     1/1     Running   0          104s   192.168.1.146   192.168.1.146   <none>           <none>
hbase-master-0       2/2     Running   0          3m3s   192.168.1.147   192.168.1.146   <none>           <none>
hbase-worker-l62m4   2/2     Running   0          104s   192.168.1.146   192.168.1.146   <none>           <none>
```

在此处可以看到，master 成功启动并且运行在具有指定标签（即`hbase-cache=true`）的结点之上。

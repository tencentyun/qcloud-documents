## 概述

单个 master 的稳定性可能较低，在一些线上提供服务的场景，需要使用多 master 来保证容错率。GooseFSRuntme 提供以 3 master 的形式来提供容错，通过 Raft 协议来进行选举，raft 是工程上使用较为广泛的强一致性、去中心化、高可用的分布式协议。

下面将为您简单地介绍上述特性。

## 前提条件

在运行该示例之前，请参考 [安装](https://cloud.tencent.com/document/product/436/59493) 文档完成安装，并检查 Fluid 各组件正常运行：

```shell
$ kubectl get pod -n fluid-system
goosefsruntime-controller-5b64fdbbb-84pc6   1/1     Running   0          8h
csi-nodeplugin-fluid-fwgjh                  2/2     Running   0          8h
csi-nodeplugin-fluid-ll8bq                  2/2     Running   0          8h
csi-nodeplugin-fluid-dhz7d                  2/2     Running   0          8h
dataset-controller-5b7848dbbb-n44dj         1/1     Running   0          8h
jindoruntime-controller-654fb74447-cldsv    1/1     Running   0          8h
```

通常来说，您会看到一个名为 `dataset-controller` 的 Pod、一个名为 `goosefsruntime-controller` 的 Pod 和多个名为 `csi-nodeplugin` 的 Pod 正在运行。其中，`csi-nodeplugin` 这些 Pod 的数量取决于您的 Kubernetes 集群中结点的数量。

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
192.168.1.145   Ready    <none>   7d14h   v1.18.4-tke.13
192.168.1.146   Ready    <none>   7d14h   v1.18.4-tke.13
192.168.1.147   Ready    <none>   7d14h   v1.18.4-tke.13
```


### 检查待创建的 Dataset 资源对象

```shell
apiVersion: data.fluid.io/v1alpha1
kind: Dataset
metadata:
  name: hbase
spec:
  mounts:
    - mountPoint: https://mirrors.tuna.tsinghua.edu.cn/apache/hbase/stable/
      name: hbase
```
TODO
>? mountPoint 这里为了方便用户进行实验使用的是 Web UFS，使用 COS 作为 UFS 可见 []()。
>

### 创建 Dataset 资源对象

```shell
$ kubectl create -f dataset.yaml
dataset.data.fluid.io/hbase created
```

### 检查待创建的 GooseFSRuntime 资源对象

```shell
apiVersion: data.fluid.io/v1alpha1
kind: GooseFSRuntime
metadata:
  name: hbase
spec:
  replicas: 3
  tieredstore:
    levels:
      - mediumtype: HDD
        path: /mnt/disk1
        quota: 2G
        high: "0.8"
        low: "0.7"
  master:
    replicas: 3
```

我们通过指定 `spec.master.replicas=3` 来开启 Raft 3 master 模式，目前只支持3个 master 形式。

### 创建GooseFSRuntime资源并查看状态

```shell
$ kubectl create -f runtime.yaml
goosefsruntime.data.fluid.io/hbase created

$ kubectl get pod
NAME                          READY   STATUS    RESTARTS   AGE
hbase-fuse-4v9mq     1/1     Running   0          84s
hbase-fuse-5kjbj     1/1     Running   0          84s
hbase-fuse-tp2q2     1/1     Running   0          84s
hbase-master-0       1/1     Running   0          104s
hbase-master-1       1/1     Running   0          102s
hbase-master-2       1/1     Running   0          100s
hbase-worker-cx8x7   1/1     Running   0          84s
hbase-worker-fjsr6   1/1     Running   0          84s
hbase-worker-fvpgc   1/1     Running   0          84s
```

### 查看 GooseFSRuntime 状态

```shell
NAME     MASTER PHASE   WORKER PHASE   FUSE PHASE   AGE
hbase   Ready           Ready            Ready     15m
```

确认 `PHASE` 全部为 Ready。

### 查看 Raft 状态 leader/follower

登录其中一个 master 的 pod：

```shell
$ kubectl exec -ti hbase-master-0 bash
$ goosefs fs masterInfo
```

可以看到其中一个节点是 `LEADER`，其余两个是 `FOLLOWER`：

```shell
current leader master: hbase-master-0:26000
All masters: [hbase-master-0:26000, hbase-master-1:26000, hbase-master-2:26000]
```

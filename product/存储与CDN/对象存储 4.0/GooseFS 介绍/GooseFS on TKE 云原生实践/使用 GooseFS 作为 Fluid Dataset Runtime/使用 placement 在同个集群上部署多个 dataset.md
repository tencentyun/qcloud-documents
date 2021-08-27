通过 GooseFS 和 [Fuse](https://github.com/libfuse/libfuse)，Fluid 为用户提供了一种更为简单的文件访问接口，使得任意运行在 Kubernetes 集群上的程序能够像访问本地文件一样轻松访问存储在远程文件系统中的文件。Fluid 针对数据集进行全生命周期的管理和隔离，尤其对于短生命周期应用（例如数据分析任务、机器学习任务），用户可以在集群中大规模部署。


## 前提条件

在运行该示例之前，请参考 [安装](https://cloud.tencent.com/document/product/436/59493) 文档完成安装，并检查 Fluid 各组件正常运行：
```shell
$ kubectl get pod -n fluid-system
NAME                                  READY   STATUS    RESTARTS   AGE
goosefsruntime-controller-5b64fdbbb-84pc6   1/1     Running   0          8h
csi-nodeplugin-fluid-fwgjh                  2/2     Running   0          8h
csi-nodeplugin-fluid-ll8bq                  2/2     Running   0          8h
dataset-controller-5b7848dbbb-n44dj         1/1     Running   0          8h
```

通常来说，您会看到一个名为 `dataset-controller` 的 Pod、一个名为 `goosefsruntime-controller `的 Pod 和多个名为 `csi-nodeplugin` 的 Pod 正在运行。其中 `csi-nodeplugin` 这些 Pod 的数量取决于您的 Kubernetes 集群中结点的数量。


## 运行示例
**对某个节点打标签**

```shell
$ kubectl  label node 192.168.0.199 fluid=multi-dataset
```

>? 在接下来的步骤中，我们将使用 `NodeSelector` 来管理 Dataset 调度的节点，这里仅做测试使用。
>

**查看待创建的 Dataset 资源对象**

- dataset.yaml
<dx-codeblock>
::: yaml yaml
apiVersion: data.fluid.io/v1alpha1
kind: Dataset
metadata:
  name: hbase
spec:
  mounts:
    - mountPoint: https://mirrors.tuna.tsinghua.edu.cn/apache/hbase/stable/
      name: hbase
  nodeAffinity:
    required:
      nodeSelectorTerms:
        - matchExpressions:
            - key: fluid
              operator: In
              values:
                - "multi-dataset"
  placement: "Shared" // 设置为 Exclusive 或者为空则为独占节点数据集
:::
</dx-codeblock>
- dataset1.yaml
<dx-codeblock>
::: yaml yaml
apiVersion: data.fluid.io/v1alpha1
kind: Dataset
metadata:
  name: spark
spec:
  mounts:
    - mountPoint: https://mirrors.bit.edu.cn/apache/spark/
      name: spark
  nodeAffinity:
    required:
      nodeSelectorTerms:
        - matchExpressions:
            - key: fluid
              operator: In
              values:
                - "multi-dataset"
  placement: "Shared" 
:::
</dx-codeblock>

>? 为了方便用户进行测试，mountPoint 这里使用的是 Web UFS，使用 COS 作为 UFS 可见 [使用 GooseFS 挂载 COS（COSN)](https://cloud.tencent.com/document/product/436/56413#.E4.BD.BF.E7.94.A8-goosefs-.E6.8C.82.E8.BD.BD-cos.EF.BC.88cosn.EF.BC.89-.E6.88.96.E8.85.BE.E8.AE.AF.E4.BA.91-hdfs.EF.BC.88chdfs.EF.BC.89)。
>

**创建 Dataset 资源对象**

```shell
$ kubectl apply -f dataset.yaml
dataset.data.fluid.io/hbase created
$ kubectl apply -f dataset1.yaml
dataset.data.fluid.io/spark created
```


**查看 Dataset 资源对象状态**

```shell
$ kubectl get dataset
NAME    UFS TOTAL SIZE   CACHED   CACHE CAPACITY   CACHED PERCENTAGE   PHASE      AGE
hbase                                                                  NotBound   6s
spark                                                                  NotBound   4s
```
如上所示，`status`中的`phase`属性值为`NotBound`，这意味着该`Dataset`资源对象目前还未与任何`GooseFSRuntime`资源对象绑定，接下来，我们将创建一个`GooseFSRuntime`资源对象。


**查看待创建的 GooseFSRuntime 资源对象**

- runtime.yaml
<dx-codeblock>
::: yaml yaml
apiVersion: data.fluid.io/v1alpha1
kind: GooseFSRuntime
metadata:
  name: hbase
spec:
  replicas: 1
  tieredstore:
    levels:
      - mediumtype: SSD
        path: /mnt/disk1
        quota: 2G
        high: "0.8"
        low: "0.7"
:::
</dx-codeblock>
- runtime-1.yaml
<dx-codeblock>
::: yaml yaml
apiVersion: data.fluid.io/v1alpha1
kind: GooseFSRuntime
metadata:
  name: spark
spec:
  replicas: 1
  tieredstore:
    levels:
      - mediumtype: SSD
        path: /mnt/disk2/
        quota: 4G
        high: "0.8"
        low: "0.7"
:::
</dx-codeblock>

**创建 GooseFSRuntime 资源对象**
```shell
$ kubectl create -f runtime.yaml
goosefsruntime.data.fluid.io/hbase created


# 等待 Dataset hbase 全部组件 Running 
$ kubectl get pod -o wide | grep hbase
NAME                              READY   STATUS    RESTARTS   AGE   IP              NODE                       NOMINATED NODE   READINESS GATES
hbase-fuse-jl2g2           1/1     Running   0          2m24s   192.168.0.199   192.168.0.199   <none>           <none>
hbase-master-0             2/2     Running   0          2m55s   192.168.0.200   192.168.0.200   <none>           <none>
hbase-worker-g89p8         2/2     Running   0          2m24s   192.168.0.199   192.168.0.199   <none>           <none>

$ kubectl create -f runtime1.yaml
goosefsruntime.data.fluid.io/spark created
```

**检查 GooseFSRuntime 资源对象是否已经创建**

```shell
$ kubectl get goosefsruntime
NAME    MASTER PHASE   WORKER PHASE   FUSE PHASE   AGE
hbase   Ready          Ready          Ready        2m14s
spark   Ready          Ready          Ready        58s
```

`GooseFSRuntime`是另一个 Fluid 定义的 CRD。一个 `GooseFSRuntime` 资源对象描述了在 Kubernetes 集群中运行一个 GooseFS 实例所需要的配置信息。


等待一段时间，让 GooseFSRuntime 资源对象中的各个组件得以顺利启动，您会看到类似以下状态：


```shell
$ kubectl get pod -o wide
NAME                        READY   STATUS    RESTARTS   AGE     IP              NODE                       NOMINATED NODE   READINESS GATES
hbase-fuse-jl2g2     1/1     Running   0          2m24s   192.168.0.199   192.168.0.199   <none>           <none>
hbase-master-0       2/2     Running   0          2m55s   192.168.0.200   192.168.0.200   <none>           <none>
hbase-worker-g89p8   2/2     Running   0          2m24s   192.168.0.199   192.168.0.199   <none>           <none>
spark-fuse-5z49p     1/1     Running   0          19s     192.168.0.199   192.168.0.199   <none>           <none>
spark-master-0       2/2     Running   0          50s     192.168.0.200   192.168.0.200   <none>           <none>
spark-worker-96ksn   2/2     Running   0          19s     192.168.0.199   192.168.0.199   <none>           <none>
```
注意上面不同的 Dataset 的 worker 和 fuse 组件可以正常的调度到相同的节点 `192.168.0.199`。

**再次查看 Dataset 资源对象状态**

```shell
$ kubectl get dataset 
NAME    UFS TOTAL SIZE   CACHED   CACHE CAPACITY   CACHED PERCENTAGE   PHASE   AGE
hbase   443.89MiB        0.00B    2.00GiB          0.0%                Bound   11m
spark   1.92GiB          0.00B    4.00GiB          0.0%                Bound   9m38s
```

因为已经与一个成功启动的 GooseFSRuntime 绑定，该 Dataset 资源对象的状态得到了更新，此时 `PHASE` 属性值已经变为 `Bound` 状态。通过上述命令可以获知有关资源对象的基本信息


**查看 GooseFSRuntime 状态**

```shell
$ kubectl get goosefsruntime -o wide
NAME    READY MASTERS   DESIRED MASTERS   MASTER PHASE   READY WORKERS   DESIRED WORKERS   WORKER PHASE   READY FUSES   DESIRED FUSES   FUSE PHASE   AGE
hbase   1               1                 Ready          1               1                 Ready          1             1               Ready        11m
spark   1               1                 Ready          1               1                 Ready          1             1               Ready        9m52s
```

>? `GooseFSRuntime` 资源对象的 `status` 中包含了更多更详细的信息。
>

**查看与远程文件关联的 PersistentVolume 以及 PersistentVolumeClaim**

```shell
$ kubectl get pv
NAME    CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM           STORAGECLASS   REASON   AGE
hbase   100Gi      RWX            Retain           Bound    default/hbase                           4m55s
spark   100Gi      RWX            Retain           Bound    default/spark                           51s
```

```shell
$ kubectl get pvc
NAME    STATUS   VOLUME   CAPACITY   ACCESS MODES   STORAGECLASS   AGE
hbase   Bound    hbase    100Gi      RWX                           4m57s
spark   Bound    spark    100Gi      RWX                           53s
```

`Dataset`资源对象准备完成后（即与 GooseFS 实例绑定后），与该资源对象关联的 PV，PVC 已经由 Fluid 生成，应用可以通过该 PVC 完成远程文件在 Pod 中的挂载，并通过挂载目录实现远程文件访问。

## 远程文件访问

**查看待创建的应用**

- nginx.yaml
<dx-codeblock>
::: yaml yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-hbase
spec:
  containers:
    - name: nginx
      image: nginx
      volumeMounts:
        - mountPath: /data
          name: hbase-vol
  volumes:
    - name: hbase-vol
      persistentVolumeClaim:
        claimName: hbase
  nodeName: 192.168.0.199
:::
</dx-codeblock>
- nginx1.yaml
<dx-codeblock>
::: yaml yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-spark
spec:
  containers:
    - name: nginx
      image: nginx
      volumeMounts:
        - mountPath: /data
          name: hbase-vol
  volumes:
    - name: hbase-vol
      persistentVolumeClaim:
        claimName: spark
  nodeName: 192.168.0.199
:::
</dx-codeblock>

**启动应用进行远程文件访问**
```shell
$ kubectl create -f nginx.yaml
$ kubectl create -f nginx1.yaml
```

登录 Nginx hbase Pod：

```shell
$ kubectl exec -it nginx-hbase -- bash
```

查看远程文件挂载情况：

```shell
$ ls -lh /data/hbase
total 444M
-r--r----- 1 root root 193K Sep 16 00:53 CHANGES.md
-r--r----- 1 root root 112K Sep 16 00:53 RELEASENOTES.md
-r--r----- 1 root root  26K Sep 16 00:53 api_compare_2.2.6RC2_to_2.2.5.html
-r--r----- 1 root root 211M Sep 16 00:53 hbase-2.2.6-bin.tar.gz
-r--r----- 1 root root 200M Sep 16 00:53 hbase-2.2.6-client-bin.tar.gz
-r--r----- 1 root root  34M Sep 16 00:53 hbase-2.2.6-src.tar.gz
```

登录 Nginx spark Pod：
```shell
$ kubectl exec -it nginx-spark -- bash
```

查看远程文件挂载情况：

```shell
$ ls -lh /data/spark/
total 1.0K
dr--r----- 1 root root 7 Oct 22 12:21 spark-2.4.7
dr--r----- 1 root root 7 Oct 22 12:21 spark-3.0.1
$ du -h /data/spark/
999M	/data/spark/spark-3.0.1
968M	/data/spark/spark-2.4.7
2.0G	/data/spark/
```

登出 Nginx Pod：

```shell
$ exit
```

正如您所见，WebUFS 上所存储的全部文件像本地文件一样无区别地存在于某个 Pod 中，并且可以被该 Pod 十分方便地访问。

## 远程文件访问加速

为了演示在访问远程文件时，您能获得多大的加速效果，我们提供了一个测试作业的样例：

**查看待创建的测试作业**

- app.yaml
<dx-codeblock>
::: yaml yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: fluid-copy-test-hbase
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
        - name: busybox
          image: busybox
          command: ["/bin/sh"]
          args: ["-c", "set -x; time cp -r /data/hbase ./"]
          volumeMounts:
            - mountPath: /data
              name: hbase-vol
      volumes:
        - name: hbase-vol
          persistentVolumeClaim:
            claimName: hbase
      nodeName: 192.168.0.199
:::
</dx-codeblock>
- app1.yaml
<dx-codeblock>
::: yaml yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: fluid-copy-test-spark
spec:
  template:
    spec:
      restartPolicy: OnFailure
      containers:
        - name: busybox
          image: busybox
          command: ["/bin/sh"]
          args: ["-c", "set -x; time cp -r /data/spark ./"]
          volumeMounts:
            - mountPath: /data
              name: spark-vol
      volumes:
        - name: spark-vol
          persistentVolumeClaim:
            claimName: spark
      nodeName: 192.168.0.199
:::
</dx-codeblock>


**启动测试作业**

```shell
$ kubectl create -f app.yaml
job.batch/fluid-copy-test-hbase created
$ kubectl create -f app1.yaml
job.batch/fluid-copy-test-spark created
```

hbase 任务程序会执行 `time cp -r /data/hbase ./` 的 shell 命令，其中 `/data/hbase` 是远程文件在 Pod 中挂载的位置，该命令完成后会在终端显示命令执行的时长。

spark 任务程序会执行 `time cp -r /data/spark ./` 的 shell 命令，其中 `/data/spark` 是远程文件在 Pod 中挂载的位置，该命令完成后会在终端显示命令执行的时长。

等待一段时间，待该作业运行完成，作业的运行状态可通过以下命令查看：

```shell
$ kubectl get pod -o wide | grep copy 
fluid-copy-test-hbase-r8gxp   0/1     Completed   0          4m16s   172.29.0.135    192.168.0.199   <none>           <none>
fluid-copy-test-spark-54q8m   0/1     Completed   0          4m14s   172.29.0.136    192.168.0.199   <none>           <none>
```

如果看到如上结果，则说明该作业已经运行完成。

>!  `fluid-copy-test-hbase-r8gxp` 中的 `r8gxp` 为作业生成的标识，在您的环境中，这个标识可能不同，接下来的命令中涉及该标识的地方请以您的环境为准。
>

**查看测试作业完成时间**


```shell
$ kubectl  logs fluid-copy-test-hbase-r8gxp
+ time cp -r /data/hbase ./
real    3m 34.08s
user    0m 0.00s
sys     0m 1.24s
$ kubectl  logs fluid-copy-test-spark-54q8m
+ time cp -r /data/spark ./
real    3m 25.47s
user    0m 0.00s
sys     0m 5.48s
```


可见，第一次远程文件读取 hbase 耗费了接近3分34秒的时间，读取 spark 耗费接近3分25秒的时间。


**查看 Dataset 资源对象状态**


```shell
$ kubectl get dataset
NAME    UFS TOTAL SIZE   CACHED      CACHE CAPACITY   CACHED PERCENTAGE   PHASE   AGE
hbase   443.89MiB        443.89MiB   2.00GiB          100.0%              Bound   30m
spark   1.92GiB          1.92GiB     4.00GiB          100.0%              Bound   28m
```

现在，所有远程文件都已经被缓存在了 GooseFS 中。

**再次启动测试作业**

```shell
$ kubectl delete -f app.yaml
$ kubectl create -f app.yaml
$ kubectl delete -f app1.yaml
$ kubectl create -f app1.yaml
```

由于远程文件已经被缓存，此次测试作业能够迅速完成：

```shell
$ kubectl get pod -o wide| grep fluid
fluid-copy-test-hbase-sf5md   0/1     Completed   0          53s   172.29.0.137    192.168.0.199   <none>           <none>
fluid-copy-test-spark-fwp57   0/1     Completed   0          51s   172.29.0.138    192.168.0.199   <none>           <none>
```

```shell
$ kubectl  logs fluid-copy-test-hbase-sf5md
+ time cp -r /data/hbase ./
real    0m 0.36s
user    0m 0.00s
sys     0m 0.36s
$ kubectl  logs fluid-copy-test-spark-fwp57
+ time cp -r /data/spark ./
real    0m 1.57s
user    0m 0.00s
sys     0m 1.57s
```

同样的文件访问操作，hbase 仅耗费了0.36秒，spark仅耗费了1.57秒。

这种大幅度的加速效果归因于 GooseFS 所提供的强大的缓存能力，这种缓存能力意味着，只要您访问某个远程文件一次，该文件就会被缓存在 GooseFS 中，您的所有接下来的重复访问都不再需要读取远程文件，而是从 GooseFS 中直接获取数据。

## 环境清理
```shell
$ kubectl delete -f .
$ kubectl label node 192.168.0.199 fluid-
```

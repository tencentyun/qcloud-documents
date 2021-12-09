## 前提条件

- 已下载安装 [Fluid](https://github.com/fluid-cloudnative/fluid)（version >= 0.6.0）
>! 单击下载 [fluid-0.6.0.tgz](https://cos-data-lake-release-1253960454.cos.ap-guangzhou.myqcloud.com/fluid.tgz) 安装包。
>
- 请参见 [安装](https://cloud.tencent.com/document/product/436/59493) 文档完成 Fluid 安装。

## 创建 Dataset 和 GooseFSRuntime

1. 创建一个 resource.yaml 文件，里面包含如下内容：
 - 包含数据集及 ufs 的 dataset 信息。
 - 创建一个 Dataset CRD 对象，描述了数据集的来源，例如示例中的 test-bucket。
 - 创建一个 GooseFSRuntime，相当于启动一个 GooseFS 的集群来提供缓存服务。

 ```yaml
apiVersion: data.fluid.io/v1alpha1
kind: Dataset
metadata:
  name: hadoop
spec:
  mounts:
    - mountPoint: cosn://test-bucket/
      options:
        fs.cosn.userinfo.secretId: <COS_SECRET_ID>
        fs.cosn.userinfo.secretKey: <COS_SECRET_KEY>
        fs.cosn.bucket.region: <COS_REGION>
        fs.cosn.impl: org.apache.hadoop.fs.CosFileSystem
        fs.AbstractFileSystem.cosn.impl: org.apache.hadoop.fs.CosN
        fs.cosn.userinfo.appid: <COS_APP_ID>
  name: hadoop
	
---
apiVersion: data.fluid.io/v1alpha1
kind: GooseFSRuntime
metadata:
  name: hadoop
spec:
  replicas: 2
  tieredstore:
    levels:
      - mediumtype: HDD
        path: /mnt/disk1
        quota: 100G
        high: "0.9"
        low: "0.2"
```
为了 AK 等密钥信息的安全性，建议使用 secret 来保存相关密钥信息，secret 使用请参考 <a href="https://cloud.tencent.com/document/product/436/59502">使用参数加密</a>。
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
stringData:
  fs.cosn.userinfo.secretId: <COS_SECRET_ID>
  fs.cosn.userinfo.secretKey: <COS_SECRET_KEY>
---
apiVersion: data.fluid.io/v1alpha1
kind: Dataset
metadata:
  name: hadoop
spec:
  mounts:
    - mountPoint: cosn://yourbucket/
      options:
        fs.cosn.bucket.region: <COS_REGION>
        fs.cosn.impl: org.apache.hadoop.fs.CosFileSystem
        fs.AbstractFileSystem.cosn.impl: org.apache.hadoop.fs.CosN
        fs.cosn.userinfo.appid: <COS_APP_ID>
      name: hadoop
      encryptOptions:
        - name: fs.cosn.userinfo.secretId
          valueFrom:
            secretKeyRef:
              name: mysecret
              key: fs.cosn.userinfo.secretId
        - name: fs.cosn.userinfo.secretKey
          valueFrom:
            secretKeyRef:
              name: mysecret
              key: fs.cosn.userinfo.secretKey
---
apiVersion: data.fluid.io/v1alpha1
kind: GooseFSRuntime
metadata:
  name: hadoop
spec:
  replicas: 2
  tieredstore:
    levels:
      - mediumtype: SSD
        path: /mnt/disk1
        quota: 100G
        high: "0.9"
        low: "0.2"
```
 - Dataset：
    - mountPoint：表示挂载 UFS 的路径，路径中不需要包含 endpoint 信息。
    - options：在 options 需要指定存储桶的必要信息，具体可参考 [API 术语信息](https://cloud.tencent.com/document/product/436/7751)。
    - fs.cosn.userinfo.secretId/fs.cosn.userinfo.secretKey：拥有权限访问该 COS 存储桶的密钥信息。
 - GooseFSRuntime：更多 API 可参考 [api_doc.md](https://github.com/fluid-cloudnative/fluid/blob/master/docs/en/dev/api_doc.md)。
    - replicas：表示创建 GooseFS 集群节点的数量。
    - mediumtype： GooseFS 支持 HDD/SSD/MEM 三种类型缓存介质，提供多级缓存配置。
    - path：存储路径。
    - quota：缓存最大容量。
    - high：水位上限大小。
    - low：水位下限大小。
2.  执行命令，创建 GooseFSRuntime：
```shell
$ kubectl create -f resource.yaml
```
3.  查看部署的 GooseFSRuntime 情况，显示全部为 Ready 状态表示部署成功。
```shell
$ kubectl get goosefsruntime hadoop
NAME     MASTER PHASE   WORKER PHASE   FUSE PHASE   AGE
hadoop    Ready           Ready           Ready     62m
```
4. 查看 dataset 的情况，显示 Bound 状态表示 dataset 绑定成功。
```shell
$ kubectl get dataset hadoop
NAME     UFS TOTAL SIZE   CACHED   CACHE CAPACITY   CACHED PERCENTAGE   PHASE   AGE
hadoop       210.00MiB       0.00B    180.00GiB              0.0%          Bound   1h
```
5. 查看 PV、PVC 创建情况，GooseFSRuntime 部署过程中会自动创建 PV 和 PVC。
```shell
$ kubectl get pv,pvc
NAME                      CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM            STORAGECLASS   REASON   AGE
persistentvolume/hadoop   100Gi      RWX            Retain           Bound    default/hadoop                           58m

NAME                           STATUS   VOLUME   CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/hadoop   Bound    hadoop   100Gi      RWX                           58m
```

## 检查服务是否正常

1. 登录到 master/worker pod 上。观察是否可以正常 list 文件。
```shell
$ kubectl get pod
NAME                              READY   STATUS      RESTARTS   AGE
hadoop-fuse-svz4s         1/1     Running     0          23h
hadoop-master-0           1/1     Running     0          23h
hadoop-worker-2fpbk       1/1     Running     0          23h
```
 ```shell
$ kubectl exec -ti hadoop-goosefs-master-0 bash
goosefs fs ls /hadoop
```
2. 登录到 fuse pod 上。观察是否可以正常 list 文件。
```shell
$ kubectl exec -ti hadoop-goosefs-fuse-svz4s bash
cd /runtime-mnt/goosefs/<namespace>/<DatasetName>/goosefs-fuse/<DatasetName>
```

## 创建应用容器体验加速效果

您可以通过创建应用容器来使用 GooseFS 加速服务，或者提交机器学习作业来进行体验相关功能。如下，创建一个应用容器 app.yaml 用于使用该数据集。我们将多次访问同一数据，并比较访问时间来展示 GooseFSRuntime 的加速效果。
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: demo-app
spec:
  containers:
    - name: demo
      image: nginx
      volumeMounts:
        - mountPath: /data
          name: hadoop
  volumes:
    - name: hadoop
      persistentVolumeClaim:
        claimName: hadoop
```

1. 使用 kubectl 完成创建应用。
```shell
$ kubectl create -f app.yaml
```
2. 查看文件大小。
```shell
$ kubectl exec -it demo-app -- bash
$ du -sh /data/hadoop/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2 
210M	/data/hadoop/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2 
```
3. 进行文件的 cp 观察时间消耗了18s：
```shell
$ time cp /data/hadoop/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2 /dev/null

real	0m18.386s
user	0m0.002s
sys	  0m0.105s
```
4. 查看此时 dataset 的缓存情况，发现210MB的数据已经都缓存到了本地。
```shell
$ kubectl get dataset hadoop
NAME     UFS TOTAL SIZE   CACHED   CACHE CAPACITY   CACHED PERCENTAGE   PHASE   AGE
hadoop   210.00MiB       210.00MiB    180.00GiB        100.0%           Bound   1h
```
5. 为了避免其他因素（例如 page cache）对结果造成影响，我们将删除之前的容器，新建相同的应用，尝试访问同样的文件。由于此时文件已经被 GooseFS 缓存，可以看到第二次访问所需时间远小于第一次。
```shell
$ kubectl delete -f app.yaml && kubectl create -f app.yaml
```
6. 进行文件的拷贝观察时间，发现消耗48ms，整个拷贝的时间缩短了300倍。
```shell
$ time cp /data/hadoop/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2  /dev/null

real	0m0.048s
user	0m0.001s
sys	  0m0.046s
```

## 清理环境

```shell
$ kubectl delete -f resource.yaml
```

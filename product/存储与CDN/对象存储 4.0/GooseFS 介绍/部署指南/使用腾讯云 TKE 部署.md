使用 TKE 部署 GooseFS 需要借助 [开源组件 Fluid](https://github.com/fluid-cloudnative/fluid) 部署，TKE 应用市场已上架。部署包括两步：

1. 通过 [Fluid helm chart](https://console.cloud.tencent.com/tke2/market/detail?chart=fluid&project=qcloud-stable&clusterType=tke) 部署 controller。
2. 通过 kubectl 创建 Dataset 和 GooseFS runtime。


## 准备事项
1.  拥有腾讯云 TKE 集群。
2.  已安装 kubectl，版本 v1.18及以上。

## 安装步骤

1. 在 [TKE 应用市场](https://console.cloud.tencent.com/tke2/market) 找到 fluid 应用。
![](https://main.qcloudimg.com/raw/879a2413fee05c39cc3ff8d2fd41f80b.png)
2. 安装 Fluid Controller。
![](https://main.qcloudimg.com/raw/ffbc185e04789cb5a679b8e32ec92d59.jpg)
3. 检查 controller 组件。在左侧【集群】中找到对应集群，如果看到了两个 controller，则说明 fluid 组件安装成功。
![](https://main.qcloudimg.com/raw/27f12c25ac4da44eace986eddf356691.png)


## 操作演示

### 1. 集群访问授权

```shell
[root@master01 run]# export KUBECONFIG=xxx/cls-xxx-config (从tke控制台页面，下载集群凭证到某个目录）
```

>! 集群 API Server 需要开启外网访问权限。
>

### 2. 创建 UFS 数据集 Dataset（COS 为例）

先创建 secret.yaml 用于加密， 模版如下：

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
stringData:
  fs.cosn.userinfo.secretKey: xxx
  fs.cosn.userinfo.secretId:xxx
```

创建secret：
```shell
[root@master01 ~]# kubectl apply  -f secret.yaml
secret/mysecret created
```

dataset.yaml 模版如下：
```yaml
apiVersion: data.fluid.io/v1alpha1
kind: Dataset
metadata:
  name: slice1
spec:
  mounts:
  - mountPoint: cosn://{your bucket}
    name: slice1
    options:
      fs.cosn.bucket.region: ap-beijing
      fs.cosn.impl: org.apache.hadoop.fs.CosFileSystem
      fs.AbstractFileSystem.cosn.impl: org.apache.hadoop.fs.CosN
      fs.cosn.userinfo.appid: "${your appid}"
    encryptOptions:
      - name: fs.cosn.userinfo.secretKey
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: fs.cosn.userinfo.secretKey
      - name: fs.cosn.userinfo.secretId
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: fs.cosn.userinfo.secretId
```

创建 dataset
```shell
[root@master01 run]# kubectl apply -f dataset.yaml 
dataset.data.fluid.io/slice1 created
```

查询 Dataset 状态，处于 NotBond 状态：
```shell
[root@master01 run]# kubectl get dataset
NAME     UFS TOTAL SIZE   CACHED   CACHE CAPACITY   CACHED PERCENTAGE   PHASE      AGE
slice1 
                                                                 NotBound   11s
```

### 3. 创建 runtime

runtime.yaml 模板如下：

```yaml
apiVersion: data.fluid.io/v1alpha1
kind: GooseFSRuntime
metadata:
  name: slice1
spec:
  replicas: 1
  data:
    replicas: 1
  goosefsVersion:
    imagePullPolicy: Always
    image: ${img_uri}
    imageTag: ${tag}
  tieredstore:
    levels:
      - mediumtype: MEM
        path: /dev/shm
        quota: 1Gi
        high: "0.95"
        low: "0.7"
  properties:
    # goosefs user
    goosefs.user.file.writetype.default: MUST_CACHE
  master:
    replicas: 1
    journal:
      volumeType: hostpath
    jvmOptions:
      - "-Xmx40G"
      - "-XX:+UnlockExperimentalVMOptions"
      - "-XX:ActiveProcessorCount=8"
  worker:
    jvmOptions:
      - "-Xmx12G"
      - "-XX:+UnlockExperimentalVMOptions"
      - "-XX:MaxDirectMemorySize=32g"
      - "-XX:ActiveProcessorCount=8"
    resources:
      limits:
        cpu: 8
  fuse:
    imagePullPolicy: Always
    image: ${fuse_uri}
    imageTag: ${tag_num}
    env:
      MAX_IDLE_THREADS: "32"
    jvmOptions:
      - "-Xmx16G"
      - "-Xms16G"
      - "-XX:+UseG1GC"
      - "-XX:MaxDirectMemorySize=32g"
      - "-XX:+UnlockExperimentalVMOptions"
      - "-XX:ActiveProcessorCount=24"
    resources:
      limits:
        cpu: 16
    args:
      - fuse
      - --fuse-opts=kernel_cache,ro,max_read=131072,attr_timeout=7200,entry_timeout=7200,nonempty
```

创建 runtime：
```shell
[root@master01 run]# kubectl apply -f runtime.yaml 
goosefsruntime.data.fluid.io/slice1 created
```

检查 goosefs 组件状态：

```shell
[root@master01 run]# kubectl get pods
NAME                  READY   STATUS    RESTARTS   AGE
slice1-fuse-xsvwj     1/1     Running   0          37s
slice1-master-0       2/2     Running   0          118s
slice1-worker-fzpdw   2/2     Running   0          37s
```

### 4. 预热数据

dataload.yaml 预热组件如下：

```yaml
apiVersion: data.fluid.io/v1alpha1
kind: DataLoad
metadata:
  name: slice1-dataload
spec:
  dataset:
    name: slice1
    namespace: default
```

此时 Dataset 处于 Bond 状态，Cached 比例是0%。

```shell
[root@master01 run]# kubectl get dataset
NAME     UFS TOTAL SIZE   CACHED   CACHE CAPACITY   CACHED PERCENTAGE   PHASE   AGE
slice1   97.67MiB         0.00B    4.00GiB          0.0%                Bound   31m
```

执行数据预热：

```shell
[root@master01 run]# kubectl apply -f dataload.yaml 
dataload.data.fluid.io/slice1-dataload created
```

查看数据预热进度：

```shell
[root@master01 run]# kubectl get dataset --watch
NAME     UFS TOTAL SIZE   CACHED     CACHE CAPACITY   CACHED PERCENTAGE   PHASE   AGE
slice1   97.67MiB         52.86MiB   4.00GiB          54.1%               Bound   39m
slice1   97.67MiB         53.36MiB   4.00GiB          54.6%               Bound   39m
slice1   97.67MiB         53.36MiB   4.00GiB          54.6%               Bound   39m
slice1   97.67MiB         53.87MiB   4.00GiB          55.2%               Bound   39m
slice1   97.67MiB         53.87MiB   4.00GiB          55.2%               Bound   39m
```

数据预热完成100%：

```shell
[root@master01 run]# kubectl get dataset --watch
NAME     UFS TOTAL SIZE   CACHED     CACHE CAPACITY   CACHED PERCENTAGE   PHASE   AGE
slice1   97.67MiB         97.67MiB   4.00GiB          100.0%              Bound   44m
```


### 5. 检查数据

```shell
[root@master01 run]# kubectl get pods
NAME                               READY   STATUS      RESTARTS   AGE
slice1-dataload-loader-job-km6mg   0/1     Completed   0          12m
slice1-fuse-xsvwj                  1/1     Running     0          17m
slice1-master-0                    2/2     Running     0          19m
slice1-worker-fzpdw                2/2     Running     0          17m
```

进入 goosefs master 容器：

```shell
[root@master01 run]# kubectl exec -it slice1-master-0 -- /bin/bash
Defaulting container name to goosefs-master.
```

列出 goosefs 目录：

```shell
[root@VM-2-40-tlinux goosefs-1.0.0-SNAPSHOT-noUI-noHelm]# goosefs fs ls /slice1
          10240       PERSISTED 06-25-2021 16:45:11:809 100% /slice1/p1
              1       PERSISTED 05-24-2021 16:07:37:000  DIR /slice1/a
          10000       PERSISTED 05-26-2021 19:29:05:000  DIR /slice1/p2
```

查看某个具体文件：
```shell
[root@VM-2-40-tlinux goosefs-1.0.0-SNAPSHOT-noUI-noHelm]# goosefs fs ls /slice1/a/
             12       PERSISTED 06-25-2021 16:45:11:809 100% /slice1/a/1.xt
```


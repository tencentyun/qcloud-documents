
## 说明
使用TKE部署GooseFS需要借助开源[Fluid]((https://github.com/fluid-cloudnative/fluid "Fluid") 组件部署, TKE应用市场已上架。部署包括两步，第一步通过[Fluid helm chart]((https://console.cloud.tencent.com/tke2/market/detail?chart=fluid&project=qcloud-stable&clusterType=tke "Fluid helm chart")部署controller； 第二步通过kubectl创建Dataset和 GooseFS runtime.
## 准备事项
#### 1.  拥有腾讯云TKE集群
#### 2.  已安装kubectl， 版本v1.18及以上

## 安装步骤
1. TKE应用市场找到fluid应用
![image](https://user-images.githubusercontent.com/5255905/123408283-6989e480-d5df-11eb-811d-0fb9b275a0a1.png)


2. 安装Fluid Controller
![image](https://user-images.githubusercontent.com/5255905/123408326-77d80080-d5df-11eb-9425-f6ce1a082b8d.png)


3. 检查controller组件
![image](https://user-images.githubusercontent.com/5255905/123408362-82929580-d5df-11eb-90f1-8978f3ffcb5c.png)

找到对应集群， 看到两个controller说明fluid组件安装成功

## 操作演示
#### 1. 集群访问授权
```shell
[root@master01 run]# export KUBECONFIG=xxx/cls-xxx-config (从tke控制台页面，下载集群凭证到某个目录）
```
注意：集群API Server开启外网访问权限
#### 2. 创建UFS数据集Dataset(cos为例)
dataset.yaml模板如下

先创建secret.yaml用于加密
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
stringData:
  fs.cosn.userinfo.secretKey: xxx
  fs.cosn.userinfo.secretId:xxx
```

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
      fs.cos.app.id: "your appid"
    encryptOptions:
      - name: fs.cosn.userinfo.secretKey
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: fs.cosn.userinfo.secretKey
      - name: fs.cosn.userinfo.secretId
        valueFrom:
          secretKeyRef:
```

```shell
创建Dataset
[root@master01 run]# kubectl apply -f dataset.yaml 
dataset.data.fluid.io/slice1 created
```

查询Dataset状态， 处于NotBond状态
```shell
[root@master01 run]# kubectl get dataset
NAME     UFS TOTAL SIZE   CACHED   CACHE CAPACITY   CACHED PERCENTAGE   PHASE      AGE
slice1 
                                                                 NotBound   11s
```

#### 3. 创建runtime

runtime.yaml 模版如下

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
    image: {img_uri}
    imageTag: {tag}
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
    image: {fuse_uri}
    imageTag: {tag_num}
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

创建runtime
```shell
[root@master01 run]# kubectl apply -f runtime.yaml 
goosefsruntime.data.fluid.io/slice1 created
```

检查goosefs组件状态
```shell
[root@master01 run]# kubectl get pods
NAME                  READY   STATUS    RESTARTS   AGE
slice1-fuse-xsvwj     1/1     Running   0          37s
slice1-master-0       2/2     Running   0          118s
slice1-worker-fzpdw   2/2     Running   0          37s
```

##### 4. 预热数据
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

此时Dataset处于Bond状态, Cached比例是0%
```shell
[root@master01 run]# kubectl get dataset
NAME     UFS TOTAL SIZE   CACHED   CACHE CAPACITY   CACHED PERCENTAGE   PHASE   AGE
slice1   97.67MiB         0.00B    4.00GiB          0.0%                Bound   31m
```

执行数据预热
```shell
[root@master01 run]# kubectl apply -f dataload.yaml 
dataload.data.fluid.io/slice1-dataload created
```

查看数据预热进度
```shell
[root@master01 run]# kubectl get dataset --watch
NAME     UFS TOTAL SIZE   CACHED     CACHE CAPACITY   CACHED PERCENTAGE   PHASE   AGE
slice1   97.67MiB         52.86MiB   4.00GiB          54.1%               Bound   39m
slice1   97.67MiB         53.36MiB   4.00GiB          54.6%               Bound   39m
slice1   97.67MiB         53.36MiB   4.00GiB          54.6%               Bound   39m
slice1   97.67MiB         53.87MiB   4.00GiB          55.2%               Bound   39m
slice1   97.67MiB         53.87MiB   4.00GiB          55.2%               Bound   39m
```

数据预热完成100%
```shell
[root@master01 run]# kubectl get dataset --watch
NAME     UFS TOTAL SIZE   CACHED     CACHE CAPACITY   CACHED PERCENTAGE   PHASE   AGE
slice1   97.67MiB         97.67MiB   4.00GiB          100.0%              Bound   44m
```


#### 5. 检查数据

```shell
[root@master01 run]# kubectl get pods
NAME                               READY   STATUS      RESTARTS   AGE
slice1-dataload-loader-job-km6mg   0/1     Completed   0          12m
slice1-fuse-xsvwj                  1/1     Running     0          17m
slice1-master-0                    2/2     Running     0          19m
slice1-worker-fzpdw                2/2     Running     0          17m
```

进入goosefs master容器
```shell
[root@master01 run]# kubectl exec -it slice1-master-0 -- /bin/bash
Defaulting container name to goosefs-master.
```

list goosefs 目录
```shell
[root@VM-2-40-tlinux goosefs-1.0.0-SNAPSHOT-noUI-noHelm]# goosefs fs ls /slice1
          10240       PERSISTED 06-25-2021 16:45:11:809 100% /slice1/p1
              1       PERSISTED 05-24-2021 16:07:37:000  DIR /slice1/a
          10000       PERSISTED 05-26-2021 19:29:05:000  DIR /slice1/p2
```

查看某个具体文件
```shell
[root@VM-2-40-tlinux goosefs-1.0.0-SNAPSHOT-noUI-noHelm]# goosefs fs ls /slice1/a/
             12       PERSISTED 06-25-2021 16:45:11:809 100% /slice1/a/1.xt
```



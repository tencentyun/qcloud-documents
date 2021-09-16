 [弹性容器服务（Elastic Kubernetes Service，EKS）](https://cloud.tencent.com/document/product/457/39804) 是腾讯云容器服务推出的无须用户购买节点即可部署工作负载的容器服务模式。EKS 完全兼容原生 Kubernetes，支持使用原生方式购买及管理资源，按照容器真实使用的资源量计费。EKS 还扩展支持腾讯云的存储及网络等产品，同时确保用户容器的安全隔离、开箱即用。

使用腾讯云 EKS 部署 GooseFS 可以充分利用 EKS 的弹性计算资源，构建按需按秒付费的对象存储（Cloud Object Storage，COS）存储访问加速服务。

## 架构说明

下图展示了使用腾讯云 EKS 部署 GooseFS 的通用架构。
![](https://main.qcloudimg.com/raw/edccf984a806e02a53dd2f88a6fb4728.jpg)

如图中所示，整个架构由 EKS 托管组件、用户资源池和 COS 存储三大部分组成。其中用户资源池主要用于部署 GooseFS 集群，COS 存储作为远端存储系统，也支持替换为云 HDFS 这一公有云存储服务。具体构架过程中：
- GooseFS Master 和 Worker 都以 Kubernetes Statefulset 类型进行资源部署
- 使用 Fluid 拉起 GooseFS 集群
- Fuse Client 集成在用户 Pod 的沙箱（Sandbox）中
- 使用方式上保持与在标准 Kubernetes 一致

## 操作步骤

### 环境准备

1. 创建 EKS 集群，具体操作请参见 [创建集群](https://cloud.tencent.com/document/product/457/39813)。
2. 开启集群访问，按实际情况选择内网或者外网，具体说明请参见 [连接集群](https://cloud.tencent.com/document/product/457/39814)。
3. 执行 `kubectl get ns` 指令，确认集群可以使用：
<dx-codeblock>
::: shell shell
   -> goosefs kubectl get ns
   NAME              STATUS   AGE
   default           Active   7h31m
   kube-node-lease   Active   7h31m
   kube-public       Active   7h31m
   kube-system       Active   7h31m
:::
</dx-codeblock>
4. 获取 `helm`，可参考 [Helm 官方文档](https://helm.sh/docs/intro/install/#from-the-binary-releases) 进行操作。

### 安装 GooseFS 

1. 输入 `helm install` 指令安装 chart 包，安装 fluid：
<dx-codeblock>
::: shell shell
   -> goosefs helm install fluid ./charts/fluid-on-tke
   NAME: fluid
   LAST DEPLOYED: Tue Jul  6 17:41:20 2021
   NAMESPACE: default
   STATUS: deployed
   REVISION: 1
   TEST SUITE: None
:::
</dx-codeblock>
2. 查看 `fluid` 相关的 pod 状态：
<dx-codeblock>
::: shell shell
   -> goosefs kubectl -n fluid-system get pod
   NAME                                         READY   STATUS    RESTARTS   AGE
   alluxioruntime-controller-78877d9d47-p2pv6   1/1     Running   0          59s
   dataset-controller-5f565988cc-wnp7l          1/1     Running   0          59s
   goosefsruntime-controller-6c55b57cd6-hr78j   1/1     Running   0          59s
:::
</dx-codeblock>
3. 创建 `dataset`，按实际需要修改相关变量，并执行 `kubectl apply -f dataset.yaml` 指令应用 `dataset`：
<dx-codeblock>
::: yaml yaml
   apiVersion: data.fluid.io/v1alpha1
   kind: Dataset
   metadata:
     name: ${dataset-name}
   spec:
     mounts:
     - mountPoint: cosn://${bucket-name}
       name: ${dataset-name}
       options:
         fs.cosn.userinfo.secretKey: XXXXXXX
         fs.cosn.userinfo.secretId: XXXXXXX
         fs.cosn.bucket.region: ap-${region}
         fs.cosn.impl: org.apache.hadoop.fs.CosFileSystem
         fs.AbstractFileSystem.cosn.impl: org.apache.hadoop.fs.CosN
         fs.cos.app.id: ${user-app-id}
:::
</dx-codeblock>
4. 创建 `GooseFS` 集群，使用以下 yaml，并执行 `kubectl apply -f runtime.yaml`：
<dx-codeblock>
::: yaml yaml
    apiVersion: data.fluid.io/v1alpha1
    kind: GooseFSRuntime
    metadata:
      name: slice1
      annotations:
        master.goosefs.eks.tencent.com/model: c6
        worker.goosefs.eks.tencent.com/model: c6
    spec:
      replicas: 6 # worker 数量，虽然控制器支持扩容，但是goosefs当前不支持数据的自动re-balance
      data:
        replicas: 1  # goosefs 数据副本数
      goosefsVersion:
        imagePullPolicy: Always
        image: ccr.ccs.tencentyun.com/cosdev/goosefs   # goosefs 集群使用的镜像以及版本
        imageTag: v1.0.1
      tieredstore:
        levels:
          - mediumtype: MEM # 支持MEM，HDD，SSD 分别对应 内存，高效云盘，SSD云盘
            path: /data
            quota: 5G   # 无论内存还是云盘都会生效，云盘最低为10G
            high: "0.95"
            low: "0.7"
      properties:
        goosefs.user.streaming.data.timeout: 5s
        goosefs.job.worker.threadpool.size: "22"
        goosefs.master.journal.type: UFS        # UFS或者EMBEDDED,单master时使用UFS
    #    goosefs.worker.network.reader.buffer.size: 128MB
        goosefs.user.block.size.bytes.default: 128MB
    #    goosefs.user.streaming.reader.chunk.size.bytes: 32MB
    #    goosefs.user.local.reader.chunk.size.bytes: 32MB
        goosefs.user.metrics.collection.enabled: "false"
        goosefs.user.metadata.cache.enabled: "true"
        goosefs.user.metadata.cache.expiration.time: "2day"
      master:
        # 设定POD对应的虚拟机的规格，必填参数，不填写默认 1c1g
        resources:
          requests:
            cpu: 8
            memory: "16Gi"
          limits:
            cpu: 8
            memory: "16Gi"
        replicas: 1
    #    journal:
    #      volumeType: pvc
    #      storageClass: goosefs-hdd
        jvmOptions:
          - "-Xmx12G"
          - "-XX:+UnlockExperimentalVMOptions"
          - "-XX:ActiveProcessorCount=8"
          - "-Xms10G"
      worker:
        jvmOptions:
          - "-Xmx28G"
          - "-Xms28G"
          - "-XX:+UnlockExperimentalVMOptions"
          - "-XX:MaxDirectMemorySize=28g"
          - "-XX:ActiveProcessorCount=8"
        resources:
          requests:
            cpu: 16
            memory: "32Gi"
          limits:
            cpu: 16
            memory: "32Gi"
      fuse:
        jvmOptions:
          - "-Xmx4G"
          - "-Xms4G"
          - "-XX:+UseG1GC"
          - "-XX:MaxDirectMemorySize=4g"
          - "-XX:+UnlockExperimentalVMOptions"
          - "-XX:ActiveProcessorCount=24"
:::
</dx-codeblock>
5. 检查集群状态以及 PVC 状态：
<dx-codeblock>
::: shell shell
   -> goosefs kubectl get pod
   NAME              READY   STATUS    RESTARTS   AGE
   slice1-master-0   2/2     Running   0          8m8s
   slice1-worker-0   2/2     Running   0          8m8s
   slice1-worker-1   2/2     Running   0          8m8s
   slice1-worker-2   2/2     Running   0          8m8s
   slice1-worker-3   2/2     Running   0          8m8s
   slice1-worker-4   2/2     Running   0          8m8s
   slice1-worker-5   2/2     Running   0          8m8s
   -> goosefs kubectl get pvc
   slice1 Bound default-slice1 100Gi ROX fluid 7m37s       # PVC名称与dataset名称一致，100Gi是一个虚拟值用作占位
:::
</dx-codeblock>


### 数据加载
预加载数据只需要使用如下的 yaml 创建一个 resource 即可，yaml 示例如 `kubectl apply -f dataload.yaml`，执行后对应的响应示例如下：
```
   apiVersion: data.fluid.io/v1alpha1
   kind: DataLoad
   metadata:
     name: slice1-dataload
   spec:
     # 配置需要执行数据加载的 dataset信息
     dataset:
       name: slice1
       namespace: default
```

创建后，可以通过 `kubectl get dataload slice1-dataload` 观察状态。

### 业务 Pod 挂载 PVC

用户业务容器按照 k8s 标准用法使用，具体请参见 [Kubernetes 官方文档](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)。

### 销毁 GooseFS 集群

销毁 GooseFS 集群可以通过 `delete` 指令进行删除，可以指定删除 master 和 worker 节点。**该操作属高危操作，请确保业务 pod 中没有对 Goosefs 的 IO 操作之后执行。**
```
   -> goosefs kubectl get sts
   NAME            READY   AGE
   slice1-master   1/1     14m
   slice1-worker   6/6     14m
   -> goosefs kubectl delete sts slice1-master slice1-worker
   statefulset.apps "slice1-master" deleted
   statefulset.apps "slice1-worker" deleted
```

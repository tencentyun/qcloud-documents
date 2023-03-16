## 简介

Container Storage Interface（CSI）是由 Kubernetes、Docker 等社区推出的一个行业标准接口规范，是用于将文件系统或者块存储暴露给 Kubernetes 之类的容器编排系统（CO）上的容器化工作负载的标准。

Kubernetes-csi-tencentcloud CHDFS 插件实现了 CSI 接口，可以将 COS 元数据加速桶作为文件系统提供给 Kubernetes。您可以快速的在容器集群中通过标准原生 Kubernetes 以 CHDFS-FUSE 的形式使用 COS 元数据加速桶，详情请参见 [CHDFS-FUSE 工具介绍](https://github.com/tencentyun/chdfs-fuse)。CHDFS-FUSE 插件能够将腾讯云 COS 元数据加速桶挂载到对应工作负载中，目前只支持 **Static Provisioning** 模式（即为一个已有的元数据加速桶创建 pv，并创建对应 pvc 来使用它）。


## 环境准备

- 需要准备 **Kubernetes 版本大于等于 1.14** 的集群，推荐 [腾讯云 TKE 集群](https://cloud.tencent.com/document/product/457/54231)。
- 在已开启元数据加速的存储桶中，单击**性能配置 > HDFS 用户配置**，配置 Kubernetes 集群的 VPC 网络。
  ![image-20230215194533905](https://qcloudimg.tencent-cloud.cn/raw/84284bf9401bb3d6a5ac8a3a6ddb0079.png)

## 使用方法

### 插件下载

[前往 Github 下载插件](https://github.com/TencentCloud/kubernetes-csi-tencentcloud)，将 Kubernetes-csi-tencentcloud CHDFS 插件安装于集群中。

### 插件部署

1. 通过执行以下命令来部署 chdfs 插件。

 - 若集群 k8s 版本 >= 1.20，则命令如下：
```shell
kubectl apply -f  deploy/chdfs/kubernetes/csidriver-new.yaml
kubectl apply -f  deploy/chdfs/kubernetes/csi-node-rbac.yaml
kubectl apply -f  deploy/chdfs/kubernetes/csi-node.yaml
```
 - 若集群 k8s 版本 < 1.20，则命令如下：
```shell
kubectl apply -f  deploy/chdfs/kubernetes/csidriver-old.yaml
kubectl apply -f  deploy/chdfs/kubernetes/csi-node-rbac.yaml
kubectl apply -f  deploy/chdfs/kubernetes/csi-node.yaml
```

2. 通过执行以下命令来查看插件是否处于 Running 状态：
```shell
kubectl get po -n kube-system | grep chdfs
csi-chdfs-node-fcwd4                 2/2     Running   0          23m
```

### 插件使用

1. 编辑插件配置
```shell
vim ./deploy/chdfs/examples/pv.yaml 
```
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: csi-chdfs-pv
spec:
  accessModes:
  - ReadWriteMany
  capacity:
    storage: 10Gi
  csi:
    driver: com.tencent.cloud.csi.chdfs
    # 指定一个唯一的 volumeHandle，如 pv 名称或文件系统 id
    volumeHandle: csi-chdfs-pv
    volumeAttributes:
      # 允许其他用户访问，可选 true 或 false
      allowother: "true"
      # 任何对内存的修改都会实时同步到 CHDFS，可选 true 或 false
      sync: "false"
      # 显示调用 fuse 接口的详细信息，可选 true 或 false
      debug: "true"
      # chdfs 挂载点的挂载地址，例如 cosn-test-1250000000.chdfs.ap-guangzhou.myqcloud.com
      url: "cosn-test-1250000000.chdfs.ap-guangzhou.myqcloud.com"
      # Additional args.
      additional_args: ""
  storageClassName: ""
~                       
```
参数说明：

 - **allowother**：是否允许其他用户访问。
 - **sync**：是否将内存的任何修改都实时同步到元数据加速桶中。
 - **debug**：是否在日志中显示详细的 fuse 接口调用。
 - **url**：参数中填入正确的桶名和地域，例如 `cosn-test-1250000000.chdfs.ap-guangzhou.myqcloud.com`。
 - **additional_args**：chdfs 支持自定义挂载参数，各参数间以空格隔开，例如 `client.renew-session-lease-time-sec=100 cache.read.read-ahead-block-num=100`。支持参数及说明如下：

| 名称                                | 默认值      | 描述                                                         |
| ----------------------------------- | ----------- | ------------------------------------------------------------ |
| security.ssl-ca-path                | -           | CA 路径，例如 /etc/ssl/certs/ca-bundle.crt                   |
| client.renew-session-lease-time-sec | 10          | 会话续租时间（s）                                            |
| client.mount-sub-dir                | 根目录      | 挂载子目录                                                   |
| client.user                         | 当前用户名  | 用户名                                                       |
| client.group                        | 当前组名    | 组名                                                         |
| client.force-sync                   | false       | 强制 sync 开关，不依赖“-o sync”                              |
| cache.update-sts-time-sec           | 30          | 数据读写临时密钥刷新时间（s）                                |
| cache.cos-client-timeout-sec        | 5           | 数据上传/下载超时时间（s）                                   |
| cache.inode-attr-expired-time-sec   | 30          | inode 属性缓存有效时间（s）                                  |
| cache.read.block-expired-time-sec   | 10          | 【读操作】单 Fd 数据读缓存有效时间（s）（block 粒度）        |
| cache.read.max-block-num            | 256         | 【读操作】单 Fd 数据读缓存 block 最大数量                    |
| cache.read.read-ahead-block-num     | 15          | 【读操作】单 Fd 预读 block 数量（read-ahead-block-num < max-block-num） |
| cache.read.max-cos-load-qps         | 1024        | 【读操作】多 Fd 数据下载最大 QPS（QPS * 1MB < 网卡带宽）     |
| cache.read.load-thread-num          | 128         | 【读操作】多 Fd 数据下载 worker 数量                         |
| cache.read.select-thread-num        | 64          | 【读操作】多 Fd 元数据查询 worker 数量                       |
| cache.read.rand-read                | false       | 【读操作】随机读场景开关                                     |
| cache.write.max-mem-table-range-num | 32          | 【写操作】单 Fd 当前数据写缓存 range 最大数量                |
| cache.write.max-mem-table-size-mb   | 64          | 【写操作】单 Fd 当前数据写缓存最大容量（MB）                 |
| cache.write.max-cos-flush-qps       | 256         | 【写操作】多 Fd 数据上传最大 QPS（QPS * 4MB < 网卡带宽）     |
| cache.write.flush-thread-num        | 128         | 【写操作】多 Fd 数据上传 worker 数量                         |
| cache.write.commit-queue-len        | 100         | 【写操作】单 Fd 元数据提交队列长度                           |
| cache.write.max-commit-heap-size    | 500         | 【写操作】单 Fd 元数据提交最大容量（无需设置）               |
| cache.write.auto-merge              | true        | 【写操作】单 Fd 写时自动合并文件碎片开关                     |
| cache.write.auto-sync               | false       | 【写操作】单 Fd 写时自动刷脏页开关                           |
| cache.write.auto-sync-time-ms       | 1000        | 【写操作】单 Fd 写时自动刷脏页时间周期（ms）                 |
| log.level                           | info        | 日志级别                                                     |
| log.file.filename                   | default.log | 日志文件名                                                   |
| log.file.log-rotate                 | true        | 日志分割                                                     |
| log.file.max-size                   | -           | 单个日志文件最大容量（MB）                                   |
| log.file.max-days                   | -           | 单个日志文件保存最长时间（天）                               |
| log.file.max-backups                | -           | 历史日志文件最多文件数量                                     |


2. 通过执行以下命令来创建 pv：
```shell
# 在 pv 所支持参数中，只有 url 是必须配置的。
kubectl apply -f deploy/chdfs/examples/pv.yaml
```

3. 通过执行以下命令来创建 pvc：
```shell
kubectl apply -f deploy/chdfs/examples/pvc.yaml
```

4. 通过执行以下命令来查看 pvc 与 pv 的绑定状态：
```
kubectl get pvc csi-chdfs-pvc
```
![image-20230215194533905](https://qcloudimg.tencent-cloud.cn/raw/74be024c61300613f121fff42cf78819.png)

5. 通过执行以下命令来创建 pod：
```shell
kubectl apply -f deploy/chdfs/examples/pod.yaml
```

6. 通过执行以下命令来查看 pod 是否处于 Running 状态：
```shell
kubectl get pod
```
![image-20230215194533905](https://qcloudimg.tencent-cloud.cn/raw/73490942b3d21731e140f9c071a6393f.png)

7. 查看文件系统挂载情况，可以看到文件系统被成功挂载：
```shell
df -h 
```
![image-20230215211144396](https://qcloudimg.tencent-cloud.cn/raw/afd113649d54e28c59f54c4943ea73a2.png)

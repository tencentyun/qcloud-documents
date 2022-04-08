## 操作场景

[腾讯云容器服务](https://cloud.tencent.com/product/tke) （Tencent Kubernetes Engine，TKE）是高度可扩展的高性能容器管理服务，提供多种应用发布方式和持续交付能力并支持微服务架构，解决用户开发、测试及运维过程的环境问题、帮助用户降低成本，提高效率。

使用容器的业务，例如业务应用部署、DevOps、机器学习、弹性伸缩等场景下，通常有大量配置文件、模型文件、日志数据、文档附件等需要多个容器共享访问。特别是机器学习、智能推荐、日志数据处理场景下，除了基础的数据共享，更要求共享存储可以提供高并发访问、高吞吐、高 IOPS、低延时的服务。文件存储（Cloud File Storage，CFS）只需在容器上简单配置及挂载，就可提供上述共享存储特性，特别适合搭配容器业务使用。本文将介绍如何在 TKE 上使用 CFS。

## 前提条件
本指引的前提是您已经创建好容器集群。若您还未创建容器服务，请参见 [部署容器服务](https://cloud.tencent.com/document/product/457/11741) 操作指引，先行创建容器。



## 申请 CFS 文件存储资源并获取挂载点 IP

- 若您还未拥有文件系统，则请按照 [创建文件系统](https://cloud.tencent.com/document/product/582/9132) 指引创建一个文件系统，创建时请注意 VPC 网络的选择需要与您的容器母机在相同的 VPC 下，以保障网络的互通。 
- 若您已经拥有与容器服务同在一个 VPC 下的文件系统，您可以前往 “[文件系统详情](https://console.cloud.tencent.com/cfs/fs)” 页面获取挂载点 IP 。

## 配置挂载 CFS 文件系统

#### 步骤1：Node 上启动 NFS 客户端

挂载前，请确保系统中已经安装了`nfs-utils`或`nfs-common`，安装方法如下：

- CentOS
```plaintext
sudo yum install nfs-utils
```
- Ubuntu 
```plaintext
sudo apt-get install nfs-common
```

#### 步骤2：创建 PV
执行以下命令创建一个类型为 CFS 的 PesistentVolume。
```plaintext
apiVersion: v1
kind: PersistentVolume
metadata:
  name: cfs
spec:
  capacity:
    storage: 10Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Retain
  mountOptions:
    - hard
    - nfsvers=4
  nfs:
    path: /
    server: 10.0.1.41
```
>?
> - nfs.server：为上面已经获取到的 CFS 文件系统的挂载点 IP，本例子中假设文件系统 IP 为10.0.1.41。
> - nfs.path：为 CFS 文件系统的根目录或者子目录，本案例以根目录为例。
>


#### 步骤3：创建 PVC
接下来，创建 PersistentVolumeClaim ，来请求绑定已经创建好的 PersistentVolume。

```plaintext
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
   name: cfsclaim
spec:
   accessModes:
		   - ReadWriteMany
   volumeMode: Filesystem
   storageClassName: ""
   resources:
     requests:
       storage: 10Gi
```

#### 步骤4：创建 pod
创建一个 Pod 应用来申明挂载使用该数据卷。

```plaintext
kind: Pod
apiVersion: v1
metadata:
  name: mypod
spec:
  containers:
    - name: myfrontend
      image: nginx
      volumeMounts:
      - mountPath: "/var/www/html"
        name: mypd
  volumes:
    - name: mypd
      persistentVolumeClaim:
        claimName: cfsclaim
```
完成上述步骤后，您就可以在新建的 Pod 中使用该文件系统了。


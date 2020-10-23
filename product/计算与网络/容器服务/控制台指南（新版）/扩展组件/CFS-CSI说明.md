## CFS-CSI

### 组件介绍
kubernetes-csi-tencentloud CFS 插件实现 CSI 的接口。它可帮助您容器集群中使用腾讯云文件存储。

> ! 1.12 集群需要修改 kubelet 配置，增加\`--feature-gates=KubeletPluginsWatcher=false\`。

#### 在集群内部署的kubernetes对象
在集群内部署 CFS-CSI Add-on , 将在集群内部署以下 Kubernetes 对象：

| kubernetes对象名称             | 类型                       | 默认占用资源 | 所属Namespaces |
| -------------------------- | ------------------------ | ------ | ------------ |
| csi-attacher-cfsplugin  | StatefulSet | \      | \            |kube-system 
| csi-provisioner-cfsplugin         | StatefulSet       | \      | kube-system             |
| csi-nodeplugin-cfsplugin         | DaemonSet              | \      | kube-system            |
| csi-attacher-cfsplugin	          | Service           | \      | kube-system       |
| csi-provisioner-cfsplugin | Service              | 1C2G   | kube-system      |

### CFS-CSI使用场景
文件存储（Cloud File Storage）提供了可扩展的共享文件存储服务，可与腾讯云的 CVM 、容器、批量计算等服务搭配使用。CFS 提供了标准的 NFS 及 CIFS/SMB 文件系统访问协议，为多个 CVM 实例或其他计算服务提供共享的数据源，支持弹性容量和性能的扩展，现有应用无需修改即可挂载使用，是一种高可用、高可靠的分布式文件系统，适合于大数据分析、媒体处理和内容管理等场景。
文件存储接入简单，您无需调节自身业务结构，或者是进行复杂的配置。只需三步即可完成文件系统的接入和使用：创建文件系统，启动服务器上文件系统客户端，挂载创建的文件系统。

通过 CFS-CSI 扩展组件，您可以快速在容器集群中通过标准原生 Kubernetes 使用 CFS。详细可查看[CFS使用场景](https://cloud.tencent.com/document/product/582/9129)

### CFS-CSI 限制条件
1. CFS 本身限制可查看[ CFS 系统限制](https://cloud.tencent.com/document/product/582/9135)。
2. 在 TKE 中使用 CFS, 需要在集群内安装该扩展组件，将占用一定的系统资源。

### CFS-CSI 使用方法
#### 1. 安装并设置 CFS 扩展组件

1. 登录[ 容器服务控制台 ](https://console.qcloud.com/tke2)。
2. 单击左侧导航栏中的【集群】，进入集群管理界面。
3. 单击需新建组件的集群 ID，进入集群详情页，在该页面左侧栏中选择【组件管理】。
4. 单击【新建】，进入“新建组件”页面。
5. 勾选【CFS（腾讯云文件存储）】，单击【完成】即可。

#### 2. 创建 CFS 类型 StroageClass

1. 进入需要使用 CFS 的集群详情页，点击【存储】<【StorageClass】。

2. 在 StorageClass 列表页，单击【新建】，创建 CFS 类型的 StorageClass。如下图所示：

![](https://main.qcloudimg.com/raw/ef128d1f27b6d3089ee8654f4080d8dc.png)

#### 3. 创建PersistentPerVolumeClaim

1. 进入需要使用 CFS 的集群详情页，点击【存储】<【PersistentVolumeClaim】。

2. 创建 CFS 类型 PersistentVolumeClaim，选择上述创建的 StorageClass。

#### 4. 创建工作负载

1. 进入需要使用 CFS 的集群详情页，创建工作负载。


2. 数据卷选择使用已有 PVC, 选择上述创建的 PVC。

3. 挂载到指定的路径，单击【完成】即可。

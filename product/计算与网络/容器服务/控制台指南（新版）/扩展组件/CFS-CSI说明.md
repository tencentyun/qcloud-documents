
## 简介
### 组件介绍
Kubernetes-csi-tencentloud CFS 插件实现 CSI 的接口，可帮助您在容器集群中使用腾讯云文件存储。

> ! 1.12 集群需要修改 kubelet 配置，增加 `\--feature-gates=KubeletPluginsWatcher=false\`。

### 部署在集群内的 Kubernetes 对象

| kubernetes对象名称             | 类型                       | 默认占用资源 | 所属Namespaces |
| -------------------------- | ------------------------ | ------ | ------------ |
| csi-provisioner-cfsplugin         | StatefulSet       | -      | kube-system             |
| csi-nodeplugin-cfsplugin         | DaemonSet              | -      | kube-system            |
| csi-provisioner-cfsplugin | Service              | 1C2G   | kube-system      |

## 使用场景
文件存储 CFS 提供了可扩展的共享文件存储服务，可与腾讯云 CVM、容器服务 TKE、批量计算等服务搭配使用。CFS 提供了标准的 NFS 及 CIFS/SMB 文件系统访问协议，为多个 CVM 实例或其他计算服务提供共享的数据源，支持弹性容量和性能的扩展，现有应用无需修改即可挂载使用，是一种高可用、高可靠的分布式文件系统，适合于大数据分析、媒体处理和内容管理等场景。

CFS 接入简单，您无需调节自身业务结构，或者是进行复杂的配置。只需三步即可完成文件系统的接入和使用：创建文件系统，启动服务器上文件系统客户端，挂载创建的文件系统。通过 CFS-CSI 扩展组件，您可以快速在容器集群中通过标准原生 Kubernetes 使用 CFS，详情请参见 [CFS 使用场景](https://cloud.tencent.com/document/product/582/9129)。

## 限制条件
- CFS 自身限制可参见 [CFS 系统限制](https://cloud.tencent.com/document/product/582/9135)。
- 在 TKE 中使用 CFS，需要在集群内安装该扩展组件，这将占用一定的系统资源。

## 操作步骤
### 安装并设置 CFS 扩展组件

1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，在左侧导航栏中选择**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 CFS。
5. 单击**完成**即可创建组件。



### 创建 CFS 类型 StroageClass
1. 在“集群管理”页面单击使用 CFS 的集群 ID，进入集群详情页。
2. 在左侧导航栏中选择**存储** > **StorageClass**，单击**新建**进入 “新建StorageClass” 页面。
3. 根据实际需求，创建 CFS 类型的 StorageClass。如下图所示：
![](https://main.qcloudimg.com/raw/ef128d1f27b6d3089ee8654f4080d8dc.png)
4. 单击**创建StorageClass**，完成创建。

### 创建 PersistentVolumeClaim
1. 在“集群管理”页面单击使用 CFS 的集群 ID，进入集群详情页。
2. 在左侧导航栏中选择**存储** > **PersistentVolumeClaim**，单击**新建**进入 “新建PersistentVolumeClaim” 页面。
3. 根据实际需求，创建 CFS 类型 PersistentVolumeClaim，选择上述步骤创建的 StorageClass。
4. 单击**创建PersistentVolumeClaim**，完成创建。





### 创建工作负载
1. 在“集群管理”页面单击使用 CFS 的集群 ID，进入集群详情页。
2. 在左侧导航栏中选择**工作负载** > **Deployment**，单击**新建**进入 “新建Workload” 页面。
3. 根据实际需求，数据卷选择**使用已有PVC**，并选择上述已创建的 PVC。
4. 挂载到容器的指定路径后，单击**创建Workload**完成创建。



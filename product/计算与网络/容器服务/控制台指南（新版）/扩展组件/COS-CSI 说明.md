## 简介
### 组件介绍
Kubernetes-csi-tencentcloud COS 插件实现 CSI 的接口，可帮助您在容器集群中使用腾讯云对象存储 COS。


### 在集群内部署的 Kubernetes 对象
在集群内部署 COS-CSI Add-on，将在集群内部署以下 Kubernetes 对象：

| Kubernetes 对象名称             | 类型                       | 默认占用资源 | 所属 Namespaces |
| -------------------------- | ------------------------ | ------ | ------------ |
| csi-cosplugin-external-runner  | StatefulSet | -     | -           |kube-system |
| csi-coslauncher        | DaemonSet       | -    | kube-system             |
| csi-cosplugin        | DaemonSet              | -     | kube-system            |
| csi-cosplugin-external-runner	          | Service           | -      | kube-system       |
| csi-cos-tencentcloud-token | Secret              | -  | kube-system      |

## 使用场景

对象存储（Cloud Object Storage，COS）是腾讯云提供的一种存储海量文件的分布式存储服务，用户可通过网络随时存储和查看数据。腾讯云 COS 使所有用户都能使用具备高扩展性、低成本、可靠和安全的数据存储服务。

通过 COS-CSI 扩展组件，您可以快速的在容器集群中通过标准原生 Kubernetes 以 COSFS 的形式使用 COS，详情请参见 [ COSFS 工具介绍](https://cloud.tencent.com/document/product/436/6883)。

## 限制条件

- 支持 Kubernetes 1.10 以上版本的集群。
- Kubernetes 1.12 版本的集群需要增加 kubelet 配置：`--feature-gates=KubeletPluginsWatcher=false`。
- COSFS 本身限制，详情请参见[ COSFS 局限性](https://cloud.tencent.com/document/product/436/6883#.E5.B1.80.E9.99.90.E6.80.A7)。
- 在 TKE 中使用 COS，需要在集群内安装该扩展组件，将占用一定的系统资源。
- 节点滚动升级时，由于 cos-csi 的副本数为1，可能会造成组件在集群升级过程中短期不可用。升级完成后，需要更新 addon。
- COS 和 CFS 容量设置仅用于 PVC 匹配 PV。


## 使用方法

### 安装 COS 扩展组件
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的【集群】。
2. 在“集群管理”页面上方选择目标集群所在地域下的集群 ID，进入集群详情页。
3. 在集群详情页左侧导航栏中单击【组件管理】，进入【组件管理】页面。
4. 在“组件管理”页面，单击【新建】，进入【新建组件】页面。
5. 在“新建组件”页面，选择【COS】，单击【完成】即可安装成功。





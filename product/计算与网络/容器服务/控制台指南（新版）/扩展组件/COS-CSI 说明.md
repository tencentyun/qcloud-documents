## 简介
### 组件介绍
Kubernetes-csi-tencentcloud COS 插件实现 CSI 的接口，可帮助您在容器集群中使用腾讯云对象存储 COS。


### 部署在集群内的 Kubernetes 对象


| Kubernetes 对象名称             | 类型                       | 默认占用资源 | 所属 Namespaces |
| -------------------------- | ------------------------ | ------ | ------------ |
| csi-coslauncher        | DaemonSet       | -    | kube-system             |
| csi-cosplugin        | DaemonSet              | -     | kube-system            |
| csi-cos-tencentcloud-token | Secret              | -  | kube-system      |

## 使用场景

对象存储（Cloud Object Storage，COS）是腾讯云提供的一种存储海量文件的分布式存储服务，用户可通过网络随时存储和查看数据。腾讯云 COS 使所有用户都能使用具备高扩展性、低成本、可靠和安全的数据存储服务。

通过 COS-CSI 扩展组件，您可以快速的在容器集群中通过标准原生 Kubernetes 以 COSFS 的形式使用 COS，详情请参见 [ COSFS 工具介绍](https://cloud.tencent.com/document/product/436/6883)。

## 限制条件

- 支持 Kubernetes 1.10 以上版本的集群。
- Kubernetes 1.12 版本的集群需要增加 kubelet 配置：`--feature-gates=KubeletPluginsWatcher=false`。
- COSFS 本身限制，详情请参见[ COSFS 局限性](https://cloud.tencent.com/document/product/436/6883#.E5.B1.80.E9.99.90.E6.80.A7)。
- 在 TKE 中使用 COS，需要在集群内安装该扩展组件，将占用一定的系统资源。



## 使用方法

### 安装 COS 扩展组件

1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，在左侧导航栏中选择**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 COS。
5. 单击**完成**即可创建组件。


### 使用对象存储 COS
您可在 TKE 集群中为工作负载挂载对象存储，详情请参见 [使用对象存储 COS](https://cloud.tencent.com/document/product/457/44232#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4)。


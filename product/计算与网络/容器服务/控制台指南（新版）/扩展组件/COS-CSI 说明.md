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

## 使用方法

### 安装 COS 扩展组件
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，选择左侧导航栏中的【扩展组件】。
2. “扩展组件”管理页面上方，选择地域及需使用 COS 的集群，并单击【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/1f8b6617a0c351b91bd40c8f093e86c6.png)
3. 在“新建扩展组件”页面，选择【COS】，并单击【完成】即可安装成功。



### 创建 Secret<span ID="StepTwo"></span>
您可通过控制台及 kubectl 两种方式创建能够挂载 COS 访问凭证的 Secret。
>?以下两种创建方式中所需的 SecretId 和 SecretKey 值，可前往腾讯云访问管理控制台中的 [API密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取。


#### 通过控制台创建 
1. 登录容器服务控制台，选择左侧导航栏中的【[集群](https://console.cloud.tencent.com/tke2/cluster)】。
2. 选择需使用 COS 的集群 ID，进入待创建 Secret 集群的 “Deployment” 页面。
3. 选择左侧导航栏中的【配置管理】>【Secret】，进入 “Secret” 管理页面。
4. 在 “Secret” 管理页面，单击【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/d66e7a5713ac31e7b0dc8b3eb1067c3c.png)
5. 在 “新建Secret” 页面，请按需参考以下信息进行设置：
 - **名称**：请输入自定义名称，本文以 demo 为例。
 - **Secret类型**：本文选择 【Opaque】类型，该类型适用于保存秘钥证书和配置文件，Value 将以 base64 格式编码。
 - **生效范围**：勾选【指定命名空间】，选择当前集群下命名空间 kube-system。
 - **内容**：设置 `SecretId` 和 `SecretKey` 两个变量。
6. 单击【创建Secret】，即可完成创建。

#### 通过 YAML 创建
您可通过  YAML 手动创建 Secret，示例如下：
```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  # Replaced by your secret name.
  name: cos-secret
  # Replaced by your secret namespace.
  namespace: kube-system
data:
  # Replaced by your temporary secret file content. You can generate a temporary secret key with these docs:
  # Note: The value must be encoded by base64.
  SecretId: VWVEJxRk5Fb0JGbDA4M...(base64 encode) 
  SecretKey: Qa3p4ZTVCMFlQek...(base64 encode)
```

### 创建 PersistentVolume<span ID="StepThree"></span>
1. 登录容器服务控制台，选择左侧导航栏中的【[集群](https://console.cloud.tencent.com/tke2/cluster)】。
2. 选择需使用 COS 的集群 ID，进入待创建 Secret 集群的 “Deployment” 页面。
3. 选择左侧导航栏中的【存储】>【PersistentVolume】，进入 “PersistentVolume” 管理页面并参考  [静态创建 PV](https://cloud.tencent.com/document/product/457/31712#.E9.9D.99.E6.80.81.E5.88.9B.E5.BB.BA-pv) 步骤进行创建。
在“新建PersistentVolume”页面，请按需参考以下信息进行设置。如下图所示：
![](https://main.qcloudimg.com/raw/6b2bf55296d2fbfd557a09e691e1f568.png)
  - **来源设置**：本文以选择【静态创建】为例。
  - **名称**：输入自定义名称，本文以 test 为例。
  - **Provisioner**：本文选择【对象存储COS】。
  - **读写权限**：请按需选择。
  - **Secret**：选择 [ 创建 Secret ](#StepTwo) 中已创建的 Secret。
  - **存储桶**：根据实际需求进行选择。当没有合适的存储桶可用时，请参考 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档前往对象存储 [存储桶列表页](https://console.cloud.tencent.com/cos5/bucket) 进行新建。
4. 单击【创建PersistentVolume】，即可完成创建。

### 创建 PersistentVolumeClaim<span ID="StepFour"></span>
1. 登录容器服务控制台，选择左侧导航栏中的【[集群](https://console.cloud.tencent.com/tke2/cluster)】。
2. 选择需使用 COS 的集群 ID，进入待创建 Secret 集群的 “Deployment” 页面。
3. 选择左侧导航栏中的【存储】>【PersistentVolumeClaim】，进入 “PersistentVolumeClaim” 管理页面并参考 [创建 PVC](https://cloud.tencent.com/document/product/457/31712#.E5.88.9B.E5.BB.BA-pvc.3Cspan-id.3D.22createpvc2.22.3E.3C.2Fspan.3E) 步骤进行创建。
在 “新建PersistentVolume” 页面，根据实际需求，进行如下参数设置。如下图所示：
>?其中 “**Provisioner**” 选择 【对象存储COS】，“**PersistentVolume**” 选择在 [创建 PersistentVolume](#StepThree) 中已创建的 PV。
>
![](https://main.qcloudimg.com/raw/496d215711f65645b237189c35f7e17f.png)
4. 单击【创建PersistentVolumeClaim】，即可完成创建。

### 创建工作负载
1. 参考 [创建 Workload 使用 PVC 数据卷](https://cloud.tencent.com/document/product/457/31712#.E5.88.9B.E5.BB.BA-workload-.E4.BD.BF.E7.94.A8-pvc-.E6.95.B0.E6.8D.AE.E5.8D.B7) 步骤，进入需要使用 COS 的集群详情页面，进行工作负载创建。
2. 在 “数据卷” 中，单击【添加数据卷】，添加数据卷。
3. 在添加数据卷中，选择【使用已有PVC】方式，填写名称，选择 [创建 PersistentVolumeClaim](#StepFour) 中已创建的 PVC。如下图所示：
![](https://main.qcloudimg.com/raw/f481aa5d64ea20bcd8941c1cebdc8e8e.png)
4. 单击【创建Workload】，即可完成创建。

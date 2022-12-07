## 操作场景
本文档旨在帮助大家了解如何快速创建一个容器集群内的 Nginx 服务。

## 前提条件
- 已 [注册腾讯云账户](https://cloud.tencent.com/register)。
-  已创建集群。关于创建集群，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。

## 操作步骤

### 创建 Nginx 服务
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 在“集群管理”页面，选择需创建服务的集群 ID，进入集群的工作负载 “Deployment” 页面。
3. 在 “Deployment” 页面，单击**新建**。参数详情见 [创建 Deployment](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment)。
4. 在“新建Workload” 页面，根据以下信息，设置工作负载基本信息。如下图所示：
![](https://main.qcloudimg.com/raw/3fcdfdf43094e02d0fd733b1c5e8ba1b.png)
  - **工作负载名**：本文以 nginx 为例。
  -  **描述**：填写工作负载的相关信息。
  -  **标签**：本例中标签默认值为 k8s-app = **nginx**。
  -  **命名空间**：根据实际需求进行选择。
  -  **类型**：本例中以 “Deployment（可扩展的部署 Pod）”为例。
  -  **数据卷**：根据实际需求设置工作负载的挂载卷，详情见 [存储卷使用说明](https://cloud.tencent.com/document/product/457/31713)。
5. 参考以下信息设置“实例内容器”。如下图所示：
![](https://main.qcloudimg.com/raw/5c750650b8d6df2c5158db3151205894.png)
主要参数信息如下：
  - **名称**：输入实例内容器名称，本文以 test 为例。
  - **镜像**：单击**选择镜像**，在弹出框中选择**Docker Hub镜像** > **nginx** ，并单击**确定**。
  - **镜像版本（Tag）**：使用默认值 `latest`。
  - **镜像拉取策略**：提供 Always、IfNotPresent、Never 三种策略，请按需选择，本文以不进行设置使用默认策略为例。
6. 在“实例数量”中，根据以下信息设置服务的实例数量。本文以**手动调节**为例，实例数量设置为1。如下图所示：
![](https://main.qcloudimg.com/raw/08f24d05d98670d6c2566d688388941f.png)
7. 根据以下提示，进行工作负载的访问设置。如下图所示：   
![](https://main.qcloudimg.com/raw/865b5b9de1f922ac2fc46cd3f7d8e334.png)
 - **Service**：勾选“启用”。
 - **服务访问方式**：选择“提供公网访问”。
 - **负载均衡器**：根据实际需求进行选择。
 - **端口映射**：选择 TCP 协议，将容器端口和服务端口都设置为80 。
>!服务所在集群的安全组需要放通节点网络及容器网络，同时需要放通30000 - 32768端口，否则可能会出现容器服务无法使用问题，详情请参见 [容器服务安全组设置](https://cloud.tencent.com/document/product/457/9084)。
8. 单击**创建Workload**，完成 Nginx 服务的创建。


### 访问 Nginx 服务

可通过以下两种方式访问 Nginx 服务。

#### 通过**负载均衡 IP** 访问 Nginx 服务

1. 单击左侧导航栏中 **[集群](https://console.cloud.tencent.com/tke2/cluster)**，进入 “集群管理” 页面。
2. 单击 Nginx 服务所在的集群 ID，选择**服务** > **Service**。
3. 在服务管理页面，复制 Nginx 服务的负载均衡 IP，如下图所示：
![](https://main.qcloudimg.com/raw/91a91da5197a2447205cbe09c5484081.png)
4. 在浏览器地址栏输入负载均衡 IP，按 “**Enter**” 即可访问服务。

#### 通过服务名称访问 Nginx 服务

集群内的其他服务或容器可以直接通过服务名称访问。

### 验证 Nginx 服务
服务创建成功，访问服务时直接进入 Nginx 服务器的默认欢迎页。如下图所示：
![](https://main.qcloudimg.com/raw/156e6d3b804e6b214ef7600fee4fa9c1.png)

### 更多 Nginx 设置
若容器创建失败，可查看 [事件常见问题](https://cloud.tencent.com/document/product/457/8187)。

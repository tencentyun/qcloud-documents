## 操作场景
WordPress 是使用 PHP 语言开发的博客平台。用户可以在支持 PHP 和 MySQL 数据库的服务上架设属于自己的网站，也可以把 WordPress 当作一个内容管理系统来使用。

本文档旨在介绍如何使用 Docker Hub 官方镜像 `wordpress` 来创建一个公开访问的 WordPress 网站。


## 前提条件
>!
>- `wordpress` 该镜像中包含了 WordPress 所有的运行环境，直接拉取创建服务即可。
>- 创建单实例版的 WordPress 仅供测试使用，不能保证数据的持久化存储。建议您使用自建的 MySQL 或使用腾讯云数据库 TencentDB 来保存您的数据，详情请见 [使用 TencentDB 的 WordPress](/doc/product/457/7447)。  
>
- 已 [注册腾讯云账户](https://cloud.tencent.com/register)。
- 已创建 TKE 标准集群。操作详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。

## 操作步骤
### 创建 WordPress 服务
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 在“集群管理”页面，选择需创建服务的集群 ID，进入集群的基本信息页面。
3. 在**工作负载 > Deployment** 页面，单击**新建**。参数详情见 [创建 Deployment](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment)。
4. 在“新建Deployment” 页面，根据以下信息，设置工作负载基本信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a740583cf9b32f5fc3c7d036eab3dc6e.png)
 - **工作负载名**：输入要创建的工作负载的名称，本文以 wordpress 为例。
 - **描述**：填写工作负载的相关信息。
 - **标签**：本例中标签默认值为 `k8s-app = wordpress`。
 - **命名空间**：根据实际需求进行选择。
 - **数据卷**：根据实需求设置工作负载的挂载卷，详情请参见 [Volume 管理](https://cloud.tencent.com/document/product/457/31713)。
5. 参考以下信息设置“实例内容器”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/1630461eba816842c0ac1e5fd48551f3.png)
主要参数信息如下：
  - **名称**：输入实例内容器名称，本文以 test 为例。
  - **镜像**：单击**选择镜像**，在弹框中选择**Docker Hub镜像** > **wordpress** ，并单击**确定**。
  - **镜像版本（Tag）**：使用默认值 `latest`。
  - **镜像拉取策略**：提供 Always、IfNotPresent、Never 三种策略，请按需选择，本文以**不进行设置使用默认策略**为例。
6. 在“实例数量”中，根据以下信息设置服务的实例数量。本文以**手动调节**为例，实例数量设置为1。如下图所示：
![](https://main.qcloudimg.com/raw/08f24d05d98670d6c2566d688388941f.png)
7. 根据以下提示，进行工作负载的访问设置。如下图所示：   
![](https://qcloudimg.tencent-cloud.cn/raw/c46e4edd5970f17e91d7cec4f47e905e.png)
 - **Service**：勾选“启用”。
 - **服务访问方式**：选择“公网LB访问”。
 - **负载均衡器**：根据实际需求进行选择。
 - **端口映射**：选择 TCP 协议，将容器端口和服务端口都设置为80 。
>!服务所在集群的安全组需要放通节点网络及容器网络，同时需要放通30000 - 32768端口，否则可能会出现容器服务无法使用问题，详情请参见 [容器服务安全组设置](https://cloud.tencent.com/document/product/457/9084)。
8. 单击**创建Deployment**，完成 wordpress 服务的创建。
 


###  访问 WordPress 服务

可通过以下两种方式访问 WordPress 服务。

#### 通过负载均衡 IP 来访问 WordPress 服务
1. 单击左侧导航栏中 **[集群](https://console.cloud.tencent.com/tke2/cluster)**，进入“集群管理”页面。
2. 单击 WordPress 服务所在的集群 ID，选择**服务与路由** > **Service**。
3. 在 Service 列表页面，复制 WordPress 服务的负载均衡 IP，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ddc96604e450b89a925a3a93260ea136.png)
4. 在浏览器地址栏输入负载均衡 IP，按 “**Enter**” 即可访问服务。

#### 通过服务名称访问服务
集群内的其他服务或容器可以直接通过服务名称访问。

### 验证 WordPress 服务
服务创建成功，访问服务时直接进入 WordPress 服务器的配置页。如下图所示：
![](https://main.qcloudimg.com/raw/4ccbffc42a7f9381e2595175ea32be65.png)

### 更多 WordPress 设置
若容器创建失败，可查看 [事件常见问题](https://cloud.tencent.com/document/product/457/8187)。

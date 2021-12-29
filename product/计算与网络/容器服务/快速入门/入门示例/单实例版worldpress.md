## 操作场景
WordPress 是使用 PHP 语言开发的博客平台。用户可以在支持 PHP 和 MySQL 数据库的服务上架设属于自己的网站，也可以把 WordPress 当作一个内容管理系统来使用。

本文档旨在介绍如何使用 Docker Hub 官方镜像 `wordpress` 来创建一个公开访问的 WordPress 网站。


## 前提条件
>!
>- `wordpress` 该镜像中包含了 WordPress 所有的运行环境，直接拉取创建服务即可。
>- 创建单实例版的 WordPress 仅供测试使用，不能保证数据的持久化存储。建议您使用自建的 MySQL 或使用腾讯云数据库 TencentDB 来保存您的数据，详情请见 [使用 TencentDB 的 WordPress](/doc/product/457/7447)。 
>
- 已 [注册腾讯云账户](https://cloud.tencent.com/register)。
- 已创建集群。有关创建集群，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。

## 操作步骤
### 创建 WordPress 服务
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 在“集群管理”页面，选择需创建服务的集群 ID，进入集群的工作负载 “Deployment” 页面并单击**新建**。如下图所示：
![](https://main.qcloudimg.com/raw/19997a6644943a2c6ec1587404eb8ca0.png)
3. 在“新建Workload” 页面，根据以下信息，设置工作负载基本信息。如下图所示：
![](https://main.qcloudimg.com/raw/119ceb8dd65d01df363a637361541d7a.png)
 - **工作负载名**：输入要创建的工作负载的名称，本文以 wordpress 为例。
 - **描述**：填写工作负载的相关信息。
 - **标签**：key = value 键值对，本例中标签默认值为 k8s-app = **wordpress**。
 - **命名空间**：根据实际需求进行选择。
 - **类型**：根据实际需求进行选择。
 - **数据卷**：根据实需求设置工作负载的挂载卷，详情请参见 [Volume 管理](https://cloud.tencent.com/document/product/457/31713)。
4. 根据以下提示，设置**实例内容器**。如下图所示：
![](https://main.qcloudimg.com/raw/ca7ec78c92dd1ed6648c27f7f6dbbae6.png)
主要参数信息如下，其余选项保持默认值：
 - **名称**：输入自定义容器名称，本文以 test 为例。
 - **镜像**：输入 `wordpress`。
 - **镜像版本（Tag）**：输入 latest。
 - **镜像拉取策略**：提供以下3种策略，请按需选择，本文以不进行设置使用默认策略为例。
若不设置镜像拉取策略，当镜像版本为空或 `latest` 时，使用 Always 策略，否则使用 IfNotPresent 策略。
    - **Always**：总是从远程拉取该镜像。
    - **IfNotPresent**：默认使用本地镜像，若本地无该镜像则远程拉取该镜像。
    - **Never**：只使用本地镜像，若本地没有该镜像将报异常。
6. 根据以下提示，设置服务的实例数量。如下图所示：
![](https://main.qcloudimg.com/raw/08f24d05d98670d6c2566d688388941f.png)
 - **手动调节**：设定实例数量，本文实例数量设置为1。可单击“+”或“-”控制实例数量。
 - **自动调节**：满足任一设定条件，则自动调节实例（pod）数目。详情请参见 [服务自动扩缩容](https://cloud.tencent.com/document/product/457/14209)。
8. 根据以下提示，进行工作负载的**访问设置（Service）**。
 - **Service**：勾选“启用”。
 - **服务访问方式**：选择“公网LB访问”。
 - **负载均衡器**：根据实际需求进行选择。
 - **端口映射**：选择 TCP 协议，将容器端口和服务端口都设置为80。
>!服务所在集群的安全组需要放通节点网络及容器网络，同时需要放通30000 - 32768端口，否则可能会出现容器服务无法使用问题。详情参见 [容器服务安全组设置](https://cloud.tencent.com/document/product/457/9084)。
9. 单击**创建Workload**，完成 wordpress 服务的创建。


###  访问 WordPress 服务

可通过以下两种方式访问 WordPress 服务。

#### 通过负载均衡 IP 来访问 WordPress 服务
1. 单击左侧导航栏中 **[集群](https://console.cloud.tencent.com/tke2/cluster)**，进入“集群管理”页面。
2. 单击 WordPress 服务所在的集群 ID，选择**服务与路由** > **Service**。
3. 进入服务管理页面，复制 WordPress 服务的负载均衡 IP，如下图所示：
![](https://main.qcloudimg.com/raw/29c21308a87d3f252ff3b0a2e9893822.png)
4. 在浏览器地址栏输入负载均衡 IP，按 “**Enter**” 即可访问服务。

#### 通过服务名称访问服务
集群内的其他服务或容器可以直接通过服务名称访问。

### 验证 WordPress 服务
服务创建成功，访问服务时直接进入 WordPress 服务器的配置页。如下图所示：
![](https://main.qcloudimg.com/raw/4ccbffc42a7f9381e2595175ea32be65.png)

### 更多 WordPress 设置
若容器创建失败，可查看 [事件常见问题](https://cloud.tencent.com/document/product/457/8187)。


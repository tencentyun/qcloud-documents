## 操作场景
本文档旨在帮助大家了解如何快速创建一个容器集群内的 nginx 服务。

## 前提条件
>- 已 [注册腾讯云账户](https://cloud.tencent.com/register)。
>-  已创建集群。关于创建集群，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。

## 操作步骤

### 创建 Nginx 服务

1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2) 。
2. 单击左侧导航栏中【[集群](https://console.cloud.tencent.com/tke2/cluster)】，进入“集群管理”页面。
3. 单击需要创建服务的集群 ID，进入工作负载 Deployment 详情页，选择【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/812eca17f3943d661f3bc70573367ae6.png)
4. 在“新建Workload”页面，根据以下提示，设置工作负载基本信息。如下图所示：
 - **工作负载名**：输入要创建的工作负载的名称，本文以 nginx 为例。
 - **描述**：填写工作负载的相关信息。
 - **标签**：key = value 键值对，本例中标签默认值为 k8s-app = **nginx** 。
 - **命名空间**：根据实际需求进行选择。
 - **类型**：根据实际需求进行选择。
 - **数据卷**：根据实需求设置工作负载的挂载卷，详情请参见 [Volumne 管理](https://cloud.tencent.com/document/product/457/31713)。
![](https://main.qcloudimg.com/raw/bfb910953eca3845de6436c8b9b26191.png)
5. 设置**实例内容器**，输入实例内容器名称，本文以 test 为例。
6. 单击【选择镜像】（其余选项保持默认设置）。如下图所示：
 ![](https://main.qcloudimg.com/raw/5426739b6bd36ce40388ee9b1478f4f5.png)
在弹出框中选择【DockerHub镜像】> **nginx** ，并单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/8d69dc01860cbfc28f5a881b4d42bba4.png)
6. 根据以下提示，设置服务的实例数量。如下图所示：
 - **手动调节**：设定实例数量，本文实例数量设置为1。可单击“+”或“-”控制实例数量。
 - **自动调节**：满足任一设定条件，则自动调节实例（pod）数目。详情请参见 [服务自动扩缩容](https://cloud.tencent.com/document/product/457/14209)。
 ![](https://main.qcloudimg.com/raw/10129daba44bfa7d7573c968cab8c4a4.png)
7.   根据以下提示，进行工作负载的访问设置。如下图所示：   
 - **Service**：勾选“启用”。
 - **服务访问方式**：选择“提供公网访问”。
 - **负载均衡器**：根据实际需求进行选择。
 - **端口映射**：选择 TCP 协议，将容器端口和服务端口都设置为80 。
 ![](https://main.qcloudimg.com/raw/3f722201e228c2bebc63cad0ea3d76c7.png)
 >!服务所在集群的安全组需要放通节点网络及容器网络，同时需要放通30000 - 32768端口，否则可能会出现容器服务无法使用问题，详情请参见 [容器服务安全组设置](https://cloud.tencent.com/document/product/457/9084)。
8. 单击【创建Workload】，完成 nginx 服务的创建。


### 访问 Nginx 服务

可通过以下两种方式访问 nginx 服务。

#### 通过**负载均衡 IP** 访问 nginx 服务

1. 单击左侧导航栏中【[集群](https://console.cloud.tencent.com/tke2/cluster)】，进入 “集群管理” 页面。
2. 单击 Nginx 服务所在的集群 ID，选择【服务】>【Service】。
3. 在服务管理页面，复制 Nginx 服务的负载均衡 IP，如下图所示：
![](https://main.qcloudimg.com/raw/7e491f937ce63a099aa749c4e1947f5b.png)
4. 在浏览器地址栏输入负载均衡 IP，按 “**Enter**” 即可访问服务。

#### 通过服务名称访问 nginx 服务

集群内的其他服务或容器可以直接通过服务名称访问。

### 验证 nginx 服务
服务创建成功，访问服务时直接进入 nginx 服务器的默认欢迎页。如下图所示：
![](https://main.qcloudimg.com/raw/37246241fe0abd1d3796c080b1661217.png)

### 更多 Nginx 设置
- 可查看 [使用腾讯云容器服务来构建简单 web service ](https://cloud.tencent.com/community/article/223421)。
- 若容器创建失败，可查看 [事件常见问题](https://cloud.tencent.com/document/product/457/8187)。

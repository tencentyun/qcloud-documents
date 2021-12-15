## 操作场景

如果您的业务需要进行深度学习、高性能计算等场景，您可以使用腾讯云容器服务支持 GPU 功能，通过该功能可以帮助您快速使用 GPU 容器。
启用 GPU 调度有以下两种方式：
- [在集群中添加 GPU 节点](#addGPUNodesatCluster)
 - [新建 GPU 云服务器](#createGPUServer)
 - [添加已有 GPU 云服务器](#addGPUServer)
- [创建 GPU 服务的容器](#createGPUServiceContainer)
 - [通过控制台方式创建](#consoleCreate)
 - [通过应用或 Kubectl 命令创建](#appOrKubectlCreate)

## 前提条件
已登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。

## 注意事项
- 仅在集群 Kubernetes 版本大于**1.8.\***时，支持使用 GPU 调度。
- 容器之间不共享 GPU，每个容器均可以请求一个或多个 GPU。无法请求 GPU 的一小部分。
- 建议搭配亲和性调度来使用 GPU 功能。

## 操作步骤

[](id:addGPUNodesatCluster)
### 在集群中添加 GPU 节点

添加 GPU 节点有以下两种方法：
- [新建 GPU 云服务器](#createGPUServer)
- [添加已有 GPU 云服务器](#addGPUServer)

[](id:createGPUServer)
#### 新建 GPU 云服务器

1. 在左侧导航栏中，单击 **[集群](https://console.cloud.tencent.com/tke2/cluster?rid=4)**，进入 “集群管理” 页面。
2. 在需要创建 GPU 云服务器的集群行中，单击**新建节点**。
3. 在 “选择机型” 页面，将 “实例族” 设置为 “**GPU机型**”，并选择 GPU 计算型的实例类型。如下图所示：
![](https://main.qcloudimg.com/raw/b87afa4e56553e00d4f77ac59a0cdb45.png)
4. 按照页面提示逐步操作，完成创建。
>? 在进行 “云服务器配置” 时，TKE 将自动根据选择的机型进行 GPU 的驱动安装等初始流程，您无需关心基础镜像。 

[](id:addGPUServer)
#### 添加已有 GPU 云服务器

1. 在左侧导航栏中，单击 **[集群](https://console.cloud.tencent.com/tke2/cluster?rid=4)**，进入 “集群管理” 页面。
2. 在需要添加已有 GPU 云服务器的集群行中，单击**添加已有节点**。
3. 在 “选择节点” 页面，勾选已有的 GPU 节点，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/7080762e4f9f211ab7a4ef34e0db5a94.png)
4. 按照页面提示逐步操作，完成添加。
>? 在进行 “云服务器配置” 时，TKE 将自动根据选择的机型进行 GPU 的驱动安装等初始流程，您无需关心基础镜像。

[](id:createGPUServiceContainer)
### 创建 GPU 服务的容器

创建 GPU 服务的容器有以下两种方法：
- [通过控制台方式创建](#consoleCreate)
- [通过应用或 Kubectl 命令创建](#appOrKubectlCreate)

[](id:consoleCreate)
#### 通过控制台方式创建

1. 在左侧导航栏中，单击 **[集群](https://console.cloud.tencent.com/tke2/cluster?rid=4)**，进入 “集群管理” 页面。
2. 单击需要创建工作负载的集群 ID/名称，进入待创建工作负载的集群管理页面。
3. 在 “工作负载” 下，任意选择工作负载类型，进入对应的信息页面。例如，选择**工作负载** > **DaemonSet**，进入 DaemonSet 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/6729777e09dba0fc65228fdbb2f9191c.png)
4. 单击**新建**，进入 “新建Workload” 页面。
5. 根据页面信息，设置工作负载名、命名空间等信息。并在 “GPU限制” 中，设置 GPU 限制的数量。如下图所示：
![](https://main.qcloudimg.com/raw/8f0fa686061fbc11a1d1abf11107a03d.png)
6. 单击**创建Workload**，完成创建。

[](id:appOrKubectlCreate)
#### 通过应用或 Kubectl 命令创建

您可以通过应用或 Kubectl 命令创建，在 YAML 文件中添加 GPU 字段。如下图所示：
![](https://main.qcloudimg.com/raw/4dcfc0516d8d7871ce224437c4bfac4b.png)



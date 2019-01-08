## 操作场景

如果您的业务需要进行深度学习、高性能计算等场景，您可以使用腾讯云容器服务支持 GPU 功能，通过该功能可以帮助您快速使用 GPU 容器。如需要开通 GPU 功能，您可以 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=350&source=0&data_title=容器服务TKE&step=1) 进行申请。

## 前提条件

已登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。

## 注意事项
- 仅在集群 Kubernetes 版本大于**1.8.\***时，支持使用 GPU 调度。
- 当前 GPU 仅支持 CentOS 系统，请确认您的集群的操作系统是否为 CentOS 系统。
- 容器之间不共享 GPU，每个容器均可以请求一个或多个 GPU，但无法请求 GPU 的一小部分。
- 建议搭配亲和性调度来使用 GPU 功能。

## 操作指南

### 在集群中添加 GPU 节点

添加 GPU 节点有以下两种方法：
- [新建 GPU 云服务器](#createGPUServer)
- [添加已有 GPU 云服务器](#addGPUServer)

<span id="createGPUServer"></span>
#### 新建 GPU 云服务器

1. 在左侧导航栏中，单击【[集群](https://console.cloud.tencent.com/tke2/cluster?rid=4)】，进入 “集群管理” 页面。
2. 在需要创建 GPU 云服务器的集群行中，单击【新建节点】。
3. 在 “选择机型” 页面，将 “实例族” 设置为 “**GPU机型**”，并选择 GPU 计算型的实例类型。如下图所示：
![](https://main.qcloudimg.com/raw/4cb5eb503fb90aecc83911c84390bedf.png)
4. 单击【下一步】。
5. 在 “云主机配置” 页面，将 “操作系统” 设置为 GPU 类型的操作系统。如下图所示：
![](https://main.qcloudimg.com/raw/e115cd7f822353b8d0e9a2b349a8a43c.png)
6. 按照页面提示逐步操作，完成创建。

<span id="addGPUServer"></span>
#### 添加已有 GPU 云服务器

1. 在左侧导航栏中，单击【[集群](https://console.cloud.tencent.com/tke2/cluster?rid=4)】，进入 “集群管理” 页面。
2. 在需要添加已有 GPU 云服务器的集群行中，单击【添加已有节点】。
3. 在 “选择节点” 页面，勾选已有的 GPU 节点，单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/cd222f6e694f281662ccc8df289816c6.png)
4. 在 “云主机配置” 页面，将 “操作系统” 设置为 GPU 类型的操作系统。如下图所示：
![](https://main.qcloudimg.com/raw/f25f7ec3b504f346c6271ca73cf2ceb3.png)
5. 按照页面提示逐步操作，完成添加。

### 创建 GPU 服务的容器

创建 GPU 服务的容器有以下两种方法：
- [通过控制台方式创建](#consoleCreate)
- [通过应用或 Kubectl 命令创建](#appOrKubectlCreate)

<span id="consoleCreate"></span>
#### 通过控制台方式创建

1. 在左侧导航栏中，单击【[集群](https://console.cloud.tencent.com/tke2/cluster?rid=4)】，进入 “集群管理” 页面。
2. 单击需要创建 Workload 的集群 ID/名称，进入待创建 Workload 的集群管理页面。
3. 在 “工作负载” 下，任意选择 Workload 类型，进入对应的信息页面。例如，选择 “工作负载” > “DaemonSet”，进入 DaemonSet 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/73b214fcb0cf26e569310894dd44c512.png)
4. 单击【新建】，进入 “新建Workload” 页面。
5. 根据页面信息，设置工作负载名、命名空间等信息。并在 “GPU限制” 中，设置 GPU 限制的数量。如下图所示：
![](https://main.qcloudimg.com/raw/a768a0610894587528573f959277ab9f.png)
6. 单击【创建Workload】，完成创建。

<span id="appOrKubectlCreate"></span>
#### 通过应用或 Kubectl 命令创建

您可以通过应用或 Kubectl 命令创建，在 YAML 文件中添加 GPU 字段。如下图所示：
![](https://main.qcloudimg.com/raw/2f2b3a751fd4bc0a3d443d7495fb1050.png)


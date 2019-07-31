## 操作场景
如果您的业务需要进行深度学习、高性能计算等场景，您可以使用腾讯云容器服务支持 GPU 功能，通过该功能可以帮助您快速使用 GPU 容器。
创建 GPU 云服务器有以下两种方式：
- [新建 GPU 云服务器](#createGPUService)
- [添加已有 GPU 云服务器](#addGPUService)


## 使用限制
- 添加的节点需要选择 GPU 机型，选择 GPU 相关镜像。
- TKE 仅在集群 kubernetes 版本大于**1.8.\***时支持使用 GPU 调度。
- 容器之间不共享 GPU，每个容器可以请求一个或多个 GPU。无法请求 GPU 的一小部分。

## 操作步骤

<span id="createGPUService"></span>
### 新建 GPU 云服务器

具体操作请参考 [创建集群](https://cloud.tencent.com/document/product/457/32189)。创建过程中，请注意以下两点：
- 在 “选择机型” 页面，将 “Node机型” 中的 “机型” 设置为 GPU 机型。如下图所示：
![](https://main.qcloudimg.com/raw/75841abda27c525c4eef1ce15d5c32be.png)
- 在 “云服务器配置” 页面，TKE 将自动根据选择的机型进行 GPU 的驱动安装等初始流程，您无需关心基础镜像。 

<span id="addGPUService"></span>
### 添加已有 GPU 云服务器

具体操作请参考 [添加已有节点](https://cloud.tencent.com/document/product/457/32203#addExistingNode)。添加过程中，请注意以下两点：
- 在 “选择节点” 页面，勾选已有的 GPU 节点。如下图所示：
![](https://main.qcloudimg.com/raw/f4c849c61dac096b9a0535bf6e7a2b9e.png)
- 在 “云服务器配置” 页面，TKE 将自动根据选择的机型进行 GPU 的驱动安装等初始流程，您无需关心基础镜像。 


## 操作场景
如果您的业务需要进行深度学习、高性能计算等场景，您可以使用腾讯云容器服务支持 GPU 功能，通过该功能可以帮助您快速使用 GPU 容器。
创建 GPU 云服务器有以下多种方式：
- [新建 GPU 云服务器](#createGPUService)
- [添加已有 GPU 云服务器](#addGPUService)
- [新建GPU节点池](https://cloud.tencent.com/document/product/457/43735)


## 使用限制
- 添加的节点需要选择 GPU 机型，可根据需求选择自动安装 GPU 驱动，详情可参见 [GPU驱动](#newGPUService)。
- TKE 仅在集群 kubernetes 版本大于**1.8.\***时支持使用 GPU 调度。
- 默认情况下，容器之间不共享 GPU，每个容器可以请求一个或多个 GPU。无法请求 GPU 的一小部分。
- 当前独立集群的**Master节点**暂不支持设置为 GPU 机型。

## 操作步骤

[](id:createGPUService)
### 新建 GPU 云服务器

具体操作请参考 [新增节点](https://cloud.tencent.com/document/product/457/32203#.E6.96.B0.E5.BB.BA.E8.8A.82.E7.82.B9)。创建 GPU 机器过程中，请特别关注以下 GPU 的特殊参数：
#### 机型
在 “选择机型” 页面，将 “Node机型” 中的 “机型” 设置为 GPU 机型。

#### GPU驱动、CUDA版本、cuDNN版本[](id:newGPUService)
设置机型后, 可以根据需求选择 GPU 驱动的版本、CUDA 版本、cuDNN 版本。如下图所示：
![](https://main.qcloudimg.com/raw/1869ca364f14446013570f9398bf1315.jpg)
<dx-alert infotype="explain" title="">
- 勾选“后台自动安装GPU驱动”，将在系统启动时进行自动安装，预计耗时15-25分钟。
- 支持的驱动版本由 OS 以及 GPU 机型共同决定，详情可参见 [GPU 后装驱动版本列表](https://cloud.tencent.com/document/product/560/30211#gpu-.E9.A9.B1.E5.8A.A8.E9.A2.84.E8.A3.85.E4.BF.A1.E6.81.AF.3Cspan-id.3D.22preloadgpudrive.22.3E.3C.2Fspan.3E)。
- 如果您未勾选“后台自动安装GPU驱动”，为了保证 GPU 机型的正常使用，针对某些低版本 OS，将会为您默认安装 GPU 驱动，完整的默认驱动版本信息可参考下表：
<table>
<thead>
<tr>
<th>OS名称</th>
<th>默认安装驱动版本</th>
</tr>
</thead>
<tbody><tr>
<td>CentOS 7.6、Ubuntu 18、Tencent Linux2.4</td>
<td>450</td>
</tr>
<tr>
<td>Centos 7.2 (不推荐)</td>
<td>384.111</td>
</tr>
<tr>
<td>Ubuntu 16 (不推荐）</td>
<td>410.79</td>
</tr>
</tbody></table>
</dx-alert>




#### MIG
开启 MIG（Multi-Instance GPU）特性后，一颗 A100 GPU 将被划分为七个独立的 GPU 实例，帮助您在多个作业并行的场景下提高 GPU 利用率，详情可参见 [NVIDIA 官网指南](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html)。
<dx-alert infotype="notice" title="">
使用 MIG 功能，必须满足如下限制：
<li>GPU 机型为 GT4。</li>
<li>在控制台上勾选了 “后台自动安装GPU驱动” 并且配置了 GPU 版本，CUDA 版本和 cuDNN 版本。</li>
</dx-alert>






[](id:addGPUService)
### 添加已有 GPU 云服务器

具体操作请参考 [添加已有节点](https://cloud.tencent.com/document/product/457/32203#addExistingNode)。添加过程中，请注意以下两点：
- 在 “选择节点” 页面，勾选已有的 GPU 节点。如下图所示：
![](https://main.qcloudimg.com/raw/f4c849c61dac096b9a0535bf6e7a2b9e.png)
- 按需配置自动安装 GPU 驱动、MIG 等参数。



## 简介

创建好 AI 环境以后，您可以自行拼装 AI 组件，搭建 AI 平台。本文档将介绍如何对 AI 组件进行增删改查：
>!AI 组件底层基于 [Helm Chart](https://helm.sh) 实现。创建 AI 环境后，不建议您前往应用市场相关页面管理 AI 组件，请**直接在 AI 环境**管理 AI 组件，以免造成数据不一致的情况。
>
## AI 组件列表

| 组件名称 | 业务场景 | 组件介绍 |
|---------|---------|---------|
| [TF Operator](https://cloud.tencent.com/document/product/457/62632) | 模型训练 | 安装后，用户可以运行 TF 单机 / 分布式训练任务。|
| [PyTorch Operator](https://cloud.tencent.com/document/product/457/62633) | 模型训练 | 安装后，用户可以运行 PyTorch 单机 / 分布式训练任务。 |
| [MPI Operator](https://cloud.tencent.com/document/product/457/62634) | 弹性训练 | 用户可以运行弹性训练任务，充分利用算力资源。 |
| [Fluid](https://cloud.tencent.com/document/product/457/62631) | 缓存加速 | Fluid 通过使用分布式缓存引擎（GooseFS/Alluxio）为云上应用提供数据预热与加速，同时可以保障缓存数据的可观测性，可迁移性和自动化的水平扩展。 |
| [Elastic Jupyter Operator](https://cloud.tencent.com/document/product/457/62635) | 算法调试 | 为用户按需提供弹性的 Jupyter Notebook 服务，按需分配计算资源。 |

## AI 组件生命周期管理
### 创建 AI 组件
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**云原生 AI**。
2. 在 “AI 环境” 列表页面，选择目标 AI 环境 ID，进入该 AI 环境 “基本信息” 页面。
3. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
4. 单击**新建**，进入 “新建 AI 组件” 页面，参考以下提示进行设置。如下图所示：
![](https://main.qcloudimg.com/raw/37782a7636e261a497af60058da3c8ec.jpg)
主要参数信息如下：
	- 组件名：自定义组件名称。
	- 命名空间：安装组件的命名空间
	- Chart：对应组件的安装包，一次只能安装一个组件。
	- 参数：和组件配置有关的参数，创建组件以后仍然可以参考 “更新 AI 组件” 指引来更新相关参数。
5. 单击**完成**即可创建 AI 组件。

### 查看 AI 组件

成功创建 AI 环境后，可以在 AI 环境内查看已经安装的 AI 组件列表，如下图所示：
![](https://main.qcloudimg.com/raw/6f44c5298a17030f76ab6b70460010ba.jpg)

### 删除 AI 组件

1. 选择某个 AI 环境 id，进入 AI 环境的 “基本信息” 页面。
2. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
3. 选择需更新的组件所在行右侧的**删除**。
4. 在弹出的 “删除组件” 弹窗中，阅读删除说明并单击**确定**完成删除。
![](https://main.qcloudimg.com/raw/11b59b30942699913203d4acf53dbc5c.jpg)

### 更新 AI 组件

1. 选择某个 AI 环境 id，进入 AI 环境的 “基本信息” 页面。
2. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
3. 选择需更新的组件所在行右侧的**更新配置**。
4. 在弹出的 “更新组件” 页面中，按需进行组件参数配置，并单击**完成**。







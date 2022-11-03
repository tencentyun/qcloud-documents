## 背景

本文为您介绍如何搭配腾讯云数据开发治理平台Wedata和TI-kit CLI工具，进行任务周期性调度，该功能适用于同时有数据治理需求和机器学习需求的业务场景，可以在Wedata页面进行数据开发任务和机器学习任务的统一调度。

## 操作流程

您可以按照如下最佳实践流程实现TI-ONE和Wedata平台（数据开发治理平台 WeData是位于云端的一站式数据开发治理平台,详细介绍请查看[文档](https://cloud.tencent.com/document/product/1267/47990)）的对接。TIONE机器学习任务调度能力当前仅支持Wedata广州地域的企业版。

### 步骤一 准备工作

1. 创建用户及项目

在Wedata产品内需要首先创建用户及项目，详情操作指引请查看[文档](https://cloud.tencent.com/document/product/1267/72455)。

2. 配置自定义调度资源组

启用TIONE对接功能需要首先配置企业版自定义调度资源组，详情操作指引请查看[文档](https://cloud.tencent.com/document/product/1267/72631#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B0.83.E5.BA.A6.E8.B5.84.E6.BA.90.E7.BB.84.E5.88.97.E8.A1.A8)。


### 步骤二 初始化环境

在Wedata项目空间中添加执行资源组，添加服务器后需要同时安装Wedata Agent和TI-ONE CLI机器学习环境。登录机器安装完毕之后，可以看到资源组节点的状态为正常。

![](https://qcloudimg.tencent-cloud.cn/raw/07d26389109ab8640cc79c6b400e6e12.png)
![](https://qcloudimg.tencent-cloud.cn/raw/f7d5e9372cc6a1803416a55f11c1560b.png)

### 步骤三 添加数据源

在Wedata项目空间中添加数据源，添加一个HDFS或者HIVE的数据源，测试联通性，需要注意，创建完成后，要授权给需要使用的项目。数据源创建详细操作指引请查看[文档](https://cloud.tencent.com/document/product/1267/72456)。
![](https://qcloudimg.tencent-cloud.cn/raw/b53a127290657758bf80f1dc27abc733.png)
![](https://qcloudimg.tencent-cloud.cn/raw/4e075398b8b9cb16949d9b922c7f2aac.png)

### 步骤四 机器学习节点配置

1. 进入数据开发-编排空间，创建工作流，在工作流编排面板中，点击TI-ONE机器学习节点创建。
![](https://qcloudimg.tencent-cloud.cn/raw/d01684e2385982680091b33166ca3664.png)
![](https://qcloudimg.tencent-cloud.cn/raw/8d230b22547c408148093107cc8dd3bc.png)
2. Wedata中的机器学习节点本质上是一个安装了机器学习任务执行环境Tikit的Shell节点，用户需要在这个节点中编写Tikit命令，用于调度TIONE算力提交训练任务。
3. 进入节点配置页面后，单击“机器学习属性”，可进行数据源配置和算法开发配置。其中数据源配置可下拉选择当前训练任务所关联的数据源（若机器学习节点上游连接了其他节点，可在下方展示上游父任务数据源），下拉后会展示数据源ID，该ID可用于脚本开发和训练任务提交。
4. 在提交训练任务前，我们需要准备训练代码，TIONE提供轻量便捷的交互式开发环境Notebook，可点击右侧进入TIONE Notebook进行代码编写（跳转至TIONE Notebook实例创建页面后，会默认带上选中数据源的网络信息，若数据源为HDFS，也会默认在数据目录中选中该数据源）。若当前机器学习任务关联了某个Notebook实例，可直接下拉选中，页面会显示快速跳转链接和实例运行状态。
![](https://qcloudimg.tencent-cloud.cn/raw/1ff9e16513cd2a2a256ec868e802a43c.png)

### 步骤五 使用TICLI编写训练任务提交命令

1.进入机器学习节点后，使用前请先执行tikit init --secretid=xxx --secretkey=xxx，进行初始化。secretId和secretKey是腾讯云的访问密钥，获取方式：进入控制台，点击右上角头像，进入【访问管理】-【API密钥管理】获取。
2.使用前输入tikit -h，获tikit CLI工具各命令的运行方式。
![](https://qcloudimg.tencent-cloud.cn/raw/53e7a40655090cc07b38d342d6a959f5.png)
3.根据当前所需的任务类型提交任务，可在当前shell节点运行命令测试，任务提交后可在运行日志中打印对应的TIONE任务URL，可前往TIONE控制台查看训练任务详情。

### 步骤六 提交工作流进行周期调度
当完成工作流开发后，可以配置工作流周期调度参数，并且将工作流整体提交。提交完成后，可在【任务运维】模块查看工作流和任务，当生成周期性实例后，可在【实例运维】页面查看实例详情。调度相关详细操作指引请查看[文档](https://cloud.tencent.com/document/product/1267/72586)。
![](https://qcloudimg.tencent-cloud.cn/raw/ef891a7385b6016d3d65a9ace6942144.png)
![](https://qcloudimg.tencent-cloud.cn/raw/eaa109530ebbed30ea1e2efe13f2d726.png)
![](https://qcloudimg.tencent-cloud.cn/raw/47deeabec9632d6d0561af1e3d1bcd0e.png)
![](https://qcloudimg.tencent-cloud.cn/raw/336839335f06074c24795821a85726ed.png)

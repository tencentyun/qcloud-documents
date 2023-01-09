## 背景
本文为您介绍如何搭配腾讯云数据开发治理平台 Wedata 和 TI-kit CLI 工具，进行任务周期性调度，该功能适用于同时有数据治理需求和机器学习需求的业务场景，可以在 Wedata 页面进行数据开发任务和机器学习任务的统一调度。

## 操作流程
您可以按照如下最佳实践流程实现 TI-ONE 和 Wedata 平台（数据开发治理平台 WeData 是位于云端的一站式数据开发治理平台，详细介绍请查看 [文档](https://cloud.tencent.com/document/product/1267/47990)）的对接。TI-ONE 机器学习任务调度能力当前仅支持 Wedata 广州地域的企业版。

### 步骤一 准备工作
1. 创建用户及项目
在 Wedata 产品内需要首先创建用户及项目，详情操作指引请查看 [创建用户及项目](https://cloud.tencent.com/document/product/1267/72455)。

2. 配置自定义调度资源组
启用 TI-ONE 对接功能需要首先配置企业版自定义调度资源组，详情操作指引请查看 [自定义调度资源组列表](https://cloud.tencent.com/document/product/1267/72631#.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B0.83.E5.BA.A6.E8.B5.84.E6.BA.90.E7.BB.84.E5.88.97.E8.A1.A8)。

### 步骤二 初始化环境
在 Wedata 项目空间中添加执行资源组，添加服务器后需要同时安装 Wedata Agent 和 TI-ONE CLI 机器学习环境。登录机器安装完毕之后，可以看到资源组节点的状态为正常。
![](https://qcloudimg.tencent-cloud.cn/raw/f62e6c9fd3e591943c3c75fab3f3169d.png)

### 步骤三 添加数据源
在 Wedata 项目空间中添加数据源，添加一个 HDFS 或者 HIVE 的数据源，测试联通性，需要注意，创建完成后，要授权给需要使用的项目。数据源创建详细操作指引请查看[文档](https://cloud.tencent.com/document/product/1267/72456)。
![](https://qcloudimg.tencent-cloud.cn/raw/d034ad2833f29a2407e4d47ea47e5970.png)

### 步骤四 机器学习节点配置
1. 进入**数据开发** > **编排空间**，创建工作流，在工作流编排面板中，单击 **TI-ONE 机器**学习节点创建。
![](https://qcloudimg.tencent-cloud.cn/raw/b1d6f87552f9ccf7f5e152cad2eb929e.png)
![](https://qcloudimg.tencent-cloud.cn/raw/e3a2af2c595fb7255a6e07bfadf0bfc4.png)
2. Wedata中的机器学习节点本质上是一个安装了机器学习任务执行环境Tikit的Shell节点，用户需要在这个节点中编写Tikit命令，用于调度TIONE算力提交训练任务。
3. 进入节点配置页面后，单击**机器学习属性**，可进行数据源配置和算法开发配置。其中数据源配置可下拉选择当前训练任务所关联的数据源（若机器学习节点上游连接了其他节点，可在下方展示上游父任务数据源），下拉后会展示数据源 ID，该 ID可用于脚本开发和训练任务提交。
4. 在提交训练任务前，我们需要准备训练代码，TIONE 提供轻量便捷的交互式开发环境 Notebook，可点击右侧进入 TIONE Notebook 进行代码编写（跳转至 TIONE Notebook 实例创建页面后，会默认带上选中数据源的网络信息，若数据源为 HDFS，也会默认在数据目录中选中该数据源）。若当前机器学习任务关联了某个 Notebook 实例，可直接下拉选中，页面会显示快速跳转链接和实例运行状态。
![](https://qcloudimg.tencent-cloud.cn/raw/ab89144eb3862fd38903d35cabcdf294.png)


### 步骤五 使用 TICLI 编写训练任务提交命令
1. 进入机器学习节点后，使用前请先执行 `tikit init --secretid=xxx --secretkey=xxx`，进行初始化。secretId 和 secretKey 是腾讯云的访问密钥，获取方式：进入控制台，单击右上角头像，进入**访问管理** >  **API 密钥管理**获取。
2. 使用前输入tikit -h，获 tikit CLI 工具各命令的运行方式。
3. 根据当前所需的任务类型提交任务，可在当前 shell 节点运行命令测试，任务提交后可在运行日志中打印对应的 TI-ONE 任务 URL，可前 [TI-ONE 控制台](https://console.cloud.tencent.com/tione/v2) 查看训练任务详情。


### 步骤六 提交工作流进行周期调度
当完成工作流开发后，可以配置工作流周期调度参数，并且将工作流整体提交。提交完成后，可在**任务运维**模块查看工作流和任务，当生成周期性实例后，可在**实例运维**页面查看实例详情。调度相关详细操作指引请查看 [工作流列表](https://cloud.tencent.com/document/product/1267/72586)。
![](https://qcloudimg.tencent-cloud.cn/raw/4b9630fa5baea6bd1dbc9c750ecff89e.png)
![](https://qcloudimg.tencent-cloud.cn/raw/f69a199d72651feabc466c0febf6b8d8.png)
![](https://qcloudimg.tencent-cloud.cn/raw/f9159149f0f586601023f316e2b2ee91.png)

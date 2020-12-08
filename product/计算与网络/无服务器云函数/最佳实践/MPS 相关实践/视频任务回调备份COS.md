## 操作场景
在本文档示例中，我们用到了视频处理（MPS），云函数（SCF）。其中，MPS 主要用于视频处理任务，SCF 主要提供回调消息处理。

## 操作步骤
<span id="step01"></span>
### 创建云函数 SCF
1. 登录云函数控制台，选择左侧导航栏中的【[函数服务](https://console.cloud.tencent.com/scf/list)】。
2. 在“函数服务”页面上方选择**北京**地域，并单击【新建】进入新建函数页面。
设置以下参数信息，并单击【下一步】。如下图所示：
 - **函数名称**：命名为 “MPSToCOS”。
 - **运行环境**：选择 “Python 2.7”。
 - **创建方式**：选择【模板函数】。
 - **模糊搜索**：输入“MPS消息转储至COS”，并进行搜索。
单击模板中的【查看详情】，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。
![](https://main.qcloudimg.com/raw/f7032bb3ad0e9081705e1f8d64ed42ff.png)
4. 保持默认配置，单击【完成】，完成函数的创建。

<span id="step02"></span>
#### 配置 MPS 触发器
在触发器页面，选择【新建触发器】。在弹出的“新建触发器”窗口中添加MPS触发器。如下图所示：
![](https://main.qcloudimg.com/raw/096c1fb010826afb6f03e1402890d97e.png)
主要参数信息如下，其余配置项请保持默认：
- **事件类型**：MPS 触发器以账号维度的事件类型推送 Event 事件，目前支持工作流任务（WorkflowTask）和视频编辑任务（EditMediaTask）两种事件类型触发。
- **事件处理**：MPS 触发器以服务维度产生的事件作为事件源，不区分地域，资源等属性。每个账号只允许两类事件分别绑定单个函数。如需多个函数并行处理任务，请参考[函数间调用 SDK](https://cloud.tencent.com/document/product/583/37316)
>?初次创建 MPS 触发器，需点击的【SCF_QcsRole】【MPS_QcsRole】链接对相关服务角色进行授权。
 
<span id="step05"></span>
### 测试函数功能
1. 在 MPS 控制台执行 MPS 的视频处理工作流。
2. 切换至 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=8&ns=default)，查看执行结果。
在函数详情页面中选择【日志查询】页签，可以看到打印出的日志信息。如下图所示：
![](https://main.qcloudimg.com/raw/b4d8dd0a4a236ab4cb35f2e7d3160649.png)
3. 切换至对象存储 COS 控制台，查看数据转储及加工结果。
>?您可以根据自身的需求编写具体的数据加工处理方法。

通过视频处理 MPS，将 MPS 产生的回调任务通过 SCF 及时备份至 COS 是一个标准的方案，视频处理 MPS 在云函数 SCF 中配置了模板供用户使用。我们用到了视频处理（MPS）和云函数（SCF）。其中 MPS 主要用于视频处理任务，SCF 提供回调消息处理，COS 主要提供终端永久性存储能力。

## 操作步骤
### 步骤1：创建 SCF 云函数
1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf/list)，选择左侧导航栏中的 **[函数服务](https://console.cloud.tencent.com/scf/list)**。
![](https://main.qcloudimg.com/raw/29cd2fc9d699ac2af763749c2e67a472.png)
2. 在函数服务页面上方选择**北京**地域，并单击**新建**进入新建函数页面。
3. 设置以下参数信息，如下图所示：
  - **创建方式**：选择模板创建。
  - **模糊搜索**：输入“CLS 消息转储至 COS”，并进行搜索。
![](https://qcloudimg.tencent-cloud.cn/raw/2784f7c228aa8fb10272e7fba499afda.png)
>? 单击模板中的**查看详情**，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。
4. 单击**下一步**，进入函数配置页。
![](https://qcloudimg.tencent-cloud.cn/raw/767c1b80fdfa7717efca4ddf6254cf6d.png)
5. 保持默认配置请单击**完成**，即完成函数的创建。

### 步骤2：配置 MPS 触发器
1. 在 **[云函数控制台](https://console.cloud.tencent.com/scf)** 页面，选择左侧导航栏中的 **[函数服务](https://console.cloud.tencent.com/scf/list)**，单击对应的函数名后，将跳转至此函数的详情页。
![](https://main.qcloudimg.com/raw/ac998f631557ea2214d66c2be9faaf5a.png)
2. 单击**触发管理**>**创建触发器**将弹出的创建触发器窗口，触发方式请选择 “MPS 触发器”。
![](https://main.qcloudimg.com/raw/e067ef8e3e09c07b723d041193b66c62.png)
主要参数信息如下，其余配置项请保持默认：
  - **事件类型**：MPS 触发器以账号维度的事件类型推送 Event 事件，目前支持工作流任务（WorkflowTask）和视频编辑任务（EditMediaTask）两种事件类型触发。
>?
>- 初次创建 MPS 触发器将提示相关服务角色状态异常，请按提示单击对应服务**SCF_QcsRole**、**MPS_QcsRole**进行授权。
>![](https://main.qcloudimg.com/raw/e6a5802db5fe9e054c2c50020f0403b1.png)
>- MPS 触发器以服务维度产生的事件作为事件源，不区分地域、资源等属性。每个账号只允许两类事件分别绑定单个函数。如需多个函数并行处理任务，请参见 [函数间调用 SDK](https://cloud.tencent.com/document/product/583/37316)。
3. 单击**提交**后，即完成 MPS 触发器配置。
![](https://main.qcloudimg.com/raw/6a7d7009e36538491683173553b809fd.png)


### 步骤3：测试函数功能
1. 在 **[MPS 控制台](https://console.cloud.tencent.com/mps)** 执行 MPS 的视频处理工作流。
2. 切换至 **[云函数控制台](https://console.cloud.tencent.com/scf/list?rid=8&ns=default)**，查看执行结果。
在函数详情页面中选择**日志查询**页签，可以看到打印出的日志信息。如下图所示：
![](https://main.qcloudimg.com/raw/f5d10848b674f137826689ac1dc28c8a.png)
3. 切换至 [对象存储 COS 控制台](https://console.cloud.tencent.com/cos5)，查看数据转储及加工结果。

>?您可以根据自身的需求编写具体的数据加工处理方法。

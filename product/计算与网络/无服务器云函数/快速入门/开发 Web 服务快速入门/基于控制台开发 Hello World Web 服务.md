本文向您介绍如何通过腾讯云控制台快速创建一个事件函数。
相较于事件函数，SCF 提供 Web 函数专注优化 Web 服务场景，[点此了解](https://cloud.tencent.com/document/product/583/56125) 快速创建一个 Web 函数。


## 步骤1：注册腾讯云账号

如果您已在腾讯云注册，可忽略此步骤。

<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F" target="_blank"  style="color: white; font-size:13px;">点此注册腾讯云账号</a></div>

## 步骤2：在线充值

云函数服务新用户开通前三个月每月可享受一定量的免费资源使用量及免费调用次数。云函数支持多种计费方式，包括后付费（按量计费）与预付费（套餐包/资源包）。如需通过云函数使用其他后付费云上资源，请参考 [在线充值](https://cloud.tencent.com/document/product/555/7425) 文档充值账号后进行购买。



## 步骤3：服务授权

在 [腾讯云控制台](https://console.cloud.tencent.com/) 中，选择**云产品** > **云函数**，进入 Serverless 控制台，按照界面提示为云函数授权。（如果您已为云函数授权，请跳过该步骤。）

<div style="background-color:#00A4FF; width: 150px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/scf/index?rid=1" target="_blank"  style="color: white; font-size:13px;">点此进行服务授权</a></div>



## 步骤4：创建函数

<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/scf/list-create?rid=1&ns=default&createType=empty" target="_blank"  style="color: white; font-size:13px;">点此进入创建函数页面</a></div>

<br>



1. 单击左侧导航栏**函数服务**，进入“函数服务”页面。
2. 在页面上方选择**广州**地域，单击**新建**。如下图所示： 
![](https://qcloudimg.tencent-cloud.cn/raw/ac5c98e4aec9ab8df2d482adf080621d.png)
3. 在“新建函数”页面，选择“从头开始”。如下图所示：  
![](https://qcloudimg.tencent-cloud.cn/raw/0b7ce2958073fda07c5c053b6117bd8a.png)
4. 配置函数基础信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/45746d8e4ba441fb1feae6c1c37251b8.png)
	- **函数类型**：选择“事件函数”。
	- **函数名称**：函数名称默认填充，可根据需要自行修改。
	- **地域**：地域默认填充，可根据需要自行修改。
	- **运行环境**：默认填充 Python 3.7，可根据需要自行修改。
	- **时区**：云函数内默认使用 UTC 时间，您可以通过配置环境变量 TZ 修改。在您选择时区后，将自动添加对应时区的 TZ 环境变量。
5. 函数代码、日志配置、高级配置保持默认。
6. 配置触发器。在“创建触发器”中选择**自定义创建**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/89475d836f4bc65b76b5a226231e64f7.png)
  - **触发方式**：选择 “API网关触发”。
  - **集成响应**：取消勾选“启用集成响应”。
  其它参数保持默认配置。
7. 单击**完成**。您可以在 [函数服务](https://console.cloud.tencent.com/scf/list?rid=1&ns=default) 页面查看已创建的函数。

## 步骤5：云端测试
<dx-tabs>
::: 函数部署测试
在“函数管理”页中，选择**函数代码**，单击**测试**，运行代码并返回测试结果。如下图所示： 
![](https://qcloudimg.tencent-cloud.cn/raw/7b141f293793d2eafdfe053a0f2e38bf.png)
<dx-alert infotype="explain" title="">
- 如果您需要更换测试模板或模板中的内容。可直接编辑函数内容，或者选择**当前测试模板**，更换后单击**保存**即可生效。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/575f2078a73f083cf76ff082bdc2aa2a.png)
- 不同的测试模板分别模拟不同的触发器消息源，且不同的触发器和云函数之间传递的消息均为约定好的数据结构。具体内容可参考 [触发器介绍](https://cloud.tencent.com/document/product/583/9705)。
</dx-alert>


返回结果如下所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6cdf0c4855856dd72d38e02a173e44e0.png)
在本次测试过程中，云函数会在 `main_handler` 的 `event` 参数中，获取 “Hello World事件模板” 的数据结构。
```
{
  "key1": "test value 1",
  "key2": "test value 2"
}
```

:::
::: 触发器配置测试
在“触发管理”页中，查看触发器详情。
1. 触发器创建成功后，会在该函数的“触发管理”页面生成访问路径。如下图所示： 
![](https://qcloudimg.tencent-cloud.cn/raw/0d69dad74be1f4c2a67e595bf21f94ff.png)
2. 在浏览器里打开该访问路径，显示 "Hello World"，则说明函数部署成功。
:::
</dx-tabs>


## 步骤6：查看日志与监控
<dx-tabs>
::: 查看日志
在已创建函数的详情页面，选择左侧的**日志查询**，即可查看函数详细日志。如下图所示： 
![](https://qcloudimg.tencent-cloud.cn/raw/28b7f92967f8fb08d206da2866fa02b1.png)
更多关于日志信息请参见 [函数日志](https://cloud.tencent.com/document/product/583/36143)。

:::
::: 查看监控
在“函数管理”页中，选择已创建函数的**监控信息**，即可查看函数调用次数/运行时间等情况。如下图所示： 

<dx-alert infotype="notice" title="">
监控统计的粒度最小为1分钟。您需要等待1分钟后，才可查看当次的监控记录。

</dx-alert>



![](https://main.qcloudimg.com/raw/a1c2a3873b7701828d6824adae63d192.png)
更多关于监控信息请参见 [监控指标说明](https://cloud.tencent.com/document/product/583/32686)。
:::
::: 配置告警
在已创建函数的详情页面，单击**前往新增告警**为云函数配置告警策略，对函数运行状态进行监控。如下图所示： 
![](https://main.qcloudimg.com/raw/c66c54b341892d23982c7372ee0fed2f.png)
更多关于配置告警请参见 [告警配置说明](https://cloud.tencent.com/document/product/583/30133)。

:::
</dx-tabs>


## 步骤7：删除函数
函数运行后即开始消耗资源，为避免产生不必要的费用，此步骤向您介绍如何清除所有资源。
1. 选择左侧导航栏中的**函数服务**，在“函数服务”页面勾选需删除的函数后，单击**删除**。如下图所示： 
![](https://qcloudimg.tencent-cloud.cn/raw/53c874a7667a52d733b77acfd1ea6f58.png)
2. 在“删除函数”弹窗中确认信息后，单击**确定**即可删除函数。



## 遇到问题
请参考 [常见问题](https://cloud.tencent.com/document/product/583/9180) 查看解决方案。
如果仍不能解决，您可以通过 [在线咨询](https://cloud.tencent.com/act/event/Online_service) 来寻求帮助。

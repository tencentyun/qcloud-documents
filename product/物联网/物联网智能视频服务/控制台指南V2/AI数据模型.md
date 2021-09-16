
## 操作场景

提供丰富的 AI 算法模型实现具体场景的智能解析及应用，实现云边协同智能应用。

## 操作步骤

### 申请 AI 模型

使用物联网智能视频服务（消费版） AI 服务前，需要先在控制台申请具体的 AI 模型，并将 AI 模型与物联网智能视频服务（消费版）控制台创建的产品绑定，具体申请流程如下：

1.	登录 [物联网智能视频服务（消费版）控制台](https://console.cloud.tencent.com/iot-video)，选择左侧菜单栏【AI 数据模型】<【AI 模型市场】，进入“AI 模型市场页面”。
>?目前模型市场提供人形检测模型。
>
   ![](https://main.qcloudimg.com/raw/5ab8835e8c0e9baf6c15958f22389746.png)
2.	单击【人形检测模型】，进入产品的模型申请列表页。
3.	单击需要绑定的产品右侧【申请】，页面右上角将提示“提交申请成功”，即可为该产品申请对应的模型。
![](https://main.qcloudimg.com/raw/e763b5b8466af44026f8537eabb86fba.jpg)
4.	收到相关申请后，腾讯云专业人员将在3个工作日内完成审批，并完成配置模型调用次数等工作。

### 配置 Ckafka

AI 模型的推理结果将输出到用户配置的 Ckafka。完成 AI 模型的申请后，需要为它设置 Ckafka 地址，操作流程如下：

1.	单击【我的 AI 模型】，进入“我的 AI 模型”页面。
<img src="https://main.qcloudimg.com/raw/795495f4de73be89f185a637131717f4.jpg" style="width: 500px;"></img>
2.	单击产品右侧【配置 Ckafka】>【编辑】进入配置 Ckafka 配置页面，填入相关信息。
<img src="https://main.qcloudimg.com/raw/d872ec5383b496aadd54d3722e6bc952.jpg" style="width: 500px;"></img>
3. 单击【保存配置】>【确定】即可完成 Ckafka 配置。

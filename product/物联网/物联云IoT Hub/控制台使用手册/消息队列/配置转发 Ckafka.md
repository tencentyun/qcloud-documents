## 操作场景
本文档指导您如何授权访问消息队列（CKafka）和配置消息队列 CKafka。

## 前提条件
物联网通信账号必须为第一次使用消息队列 CKafka。

## 操作步骤
### 授权访问
1. 登录物联网通信控制台，选择【产品列表】>【消息队列】，单击【授权访问消息队列（CKafka）】。
2. 授权成功之后会进入配置消息队列页面。
![](https://main.qcloudimg.com/raw/18ebabb52a1e61270193e87edee1feda.png)

### 配置消息队列
#### 配置推送类型
1. 在配置消息队列页面，根据需求勾选消息类型，CKafka 配置消息类型有以下两种。
  - 设备上报消息
  - 设备状态变化通知
2. 完成消息类型选择后，单击【立即开通】。
3. 此时会弹出确认保存的窗口。单击【确定】后，物联网通信会立即向默认队列 `topic-iot-{productID}` 推送选择的消息类型。

>! 
- 消息类型不能配置空选项。
- 修改消息类型不能和上次配置的消息类型相同。

 ![](https://main.qcloudimg.com/raw/a1c77802fe5f4faefabebfbff5eb4979.png) 



#### 配置推送实例
>?若当前账号没有实例，可前往 [CKafka](https://console.cloud.tencent.com/ckafka) 购买和创建实例。

1. 在消息队列页面，选择需要推送的实例。
2. 实例创建成功后，消息队列页面就会展示订阅的详细信息，您可以在该页面修改订阅的消息类型、修改实例类型，如下图红框部分所示：
![](https://main.qcloudimg.com/raw/3f345181b089fdc96e25327f5b8807ec.png)
3. 实例创建成功后，消息队列页面就会展示订阅的详细信息，您也可以在该页面修改订阅的消息类型和推送实例。如下图红框部分所示：
![](https://main.qcloudimg.com/raw/9bca2d06398c2bc0802a52989d6f78b6.png)



### 删除消息队列
如果您想删除当前消息队列配置，可单击【删除当前配置】，即可完成删除。
![](https://main.qcloudimg.com/raw/a94cd916a39715edb1118dd01fa4cf02.png)


消息队列的 SDK 使用说明，您可以参照消息队列提供的 [使用入门](https://cloud.tencent.com/document/product/597/10112) 文档。

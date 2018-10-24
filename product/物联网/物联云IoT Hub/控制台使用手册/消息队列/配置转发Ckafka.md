## 授权访问消息队列(CKafka)
如果物联网通信帐号是第一次使用消息队列CKafka，就会显示【授权访问消息队列(CKafka)】按钮。点击进行授权，授权成功之后会进入配置消息队列页面。
![](https://main.qcloudimg.com/raw/18ebabb52a1e61270193e87edee1feda.png)

## 配置消息队列
### 配置推送类型
CKafka 配置消息类型有两个选项：“设备上报消息”和“设备状态变化通知”。根据需求勾选消息类型后，点击【立即开通】按钮，此时会弹出确认保存的窗口。点击【确定】后，物联网通信会立即向默认队列```topic-iot-{productID}``` 推送选择的消息类型。
> **注意：**
> 
> 1. 消息类型不能配置空选项；
> 2. 修改消息类型不能和上次配置的消息类型相同。

### 配置推送实例
选择需要推送的实例。若当前帐号没有实例，可前往 [CKafka](https://console.cloud.tencent.com/ckafka) 购买和创建实例。创建成功后消息队列页面就会展示订阅的详细信息，用户也可以在该页面修改订阅的消息类型、修改实例类型，如下图红框部分所示。

![](https://main.qcloudimg.com/raw/a1c77802fe5f4faefabebfbff5eb4979.png)


创建成功后消息队列页面就会展示订阅的详细信息，用户也可以在该页面修改订阅的消息类型和推送实例。
![](https://main.qcloudimg.com/raw/3f345181b089fdc96e25327f5b8807ec.png)

![](https://main.qcloudimg.com/raw/9bca2d06398c2bc0802a52989d6f78b6.png)

## 删除消息队列
点击【删除当前配置】即可删除当前消息队列配置。
![](https://main.qcloudimg.com/raw/a94cd916a39715edb1118dd01fa4cf02.png)


## CKafka 接收消息的 SDK 介绍
消息队列的 SDK 使用可以参照消息队列提供的 [使用入门](https://cloud.tencent.com/document/product/597/10112)。

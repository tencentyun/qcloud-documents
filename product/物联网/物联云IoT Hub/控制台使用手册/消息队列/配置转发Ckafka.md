## 授权访问消息队列(CKafka)
如果物联网通信帐号是第一次使用消息队列CKafka，就会显示【授权访问消息队列(CKafka)】按钮。点击进行授权，授权成功之后会进入配置消息队列页面。
![](https://main.qcloudimg.com/raw/e5c355e89338c25d6f1d6a081706b331.png)

## 配置消息队列
### 配置推送类型
CKafka 配置消息类型有两个选项：“设备上报消息”和“设备状态变化通知”。根据需求勾选消息类型后，点击【立即开通】按钮，此时会弹出确认保存的窗口。点击【确定】后，物联网通信会立即向默认队列```topic-iot-{productID}``` 推送选择的消息类型。
> **注意：**
> 
> 1. 消息类型不能配置空选项；
> 2. 修改消息类型不能和上次配置的消息类型相同。

![](https://main.qcloudimg.com/raw/afc789d04115761b738ddce25243911c.png)

### 配置推送实例
选择需要推送的实例。若当前帐号没有实例，可前往 [CKafka](https://console.cloud.tencent.com/ckafka) 购买和创建实例。创建成功后消息队列页面就会展示订阅的详细信息，用户也可以在该页面修改订阅的消息类型、修改实例类型，如下图红框部分所示。
![](https://main.qcloudimg.com/raw/9c9ab874b0619095bb6a4925ef355aec.png)

## CKafka 接收消息的 SDK 介绍
消息队列的 SDK 使用可以参照消息队列提供的 [使用入门](https://cloud.tencent.com/document/product/597/10112)。

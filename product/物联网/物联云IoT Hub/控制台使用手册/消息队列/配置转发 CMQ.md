

## 操作场景
本文档指导您如何授权访问消息队列（CMQ）和配置消息队列 CMQ。

## 前提条件
物联网通信账号必须为第一次使用消息队列 CMQ。

## 操作步骤
### 授权访问
1. 登录 [物联网通信控制台](https://console.cloud.tencent.com/iothub)，选择【产品列表】>【消息队列】，单击【授权访问消息队列（CMQ）】。
2. 授权成功之后会进入配置消息队列页面。
![](https://main.qcloudimg.com/raw/c27554c0ba6f9a65f88c63a9804c6786.png)

### 配置消息队列
1. 在配置消息队列页面，根据需求勾选消息类型，消息队列 CMQ 配置消息类型有以下两种。
 - 设备上报消息
 - 设备状态变化通知
2. 完成消息类型选择后，选择 CMQ 的地域和队列，单击【保存配置】。
3. 此时会弹出确认保存的窗口。单击【确定】后，物联网通信将会向您选择的 Topic（如果没有选择 Topic 则会向默认队列queue-iot-{productID}） 推送选择的消息类型。


>!
- 消息类型不能配置空选项.。
- 修改消息类型不能和上次配置的消息类型相同。
- 创建成功后消息队列页面就会展示订阅的详细信息，您可以在该页面修改订阅的消息类型。

### 删除消息队列
如果您想删除当前消息队列配置，可单击【删除当前配置】，即可完成删除。


## 相关信息
#### SDK 介绍
CMQ 接收消息的相关 SDK 介绍如下：
消息队列 CMQ 提供了如下两个接口从队列中**读取消息**：
- [ReceiveMessage](https://cloud.tencent.com/document/product/406/5839)：一次从队列中读取一条消息。
- [BatchReceiveMessage](https://cloud.tencent.com/document/product/406/5924)：一次从队列中读取多条消息。

消息队列的消息在读取后，需主动删除消息，才能将消息从消息队列中去掉：
- [DeleteMessage](https://cloud.tencent.com/document/api/406/5840)：从队列中删除一条消息。
- [BatchDeleteMessage](https://cloud.tencent.com/document/api/406/5841)：从队列中删除多条消息，一次最多删除16条。

消息队列的 SDK DEMO 使用，更新详情请参见消息队列提供的 [SDK DEMO 文档](https://cloud.tencent.com/document/product/406/6107)。


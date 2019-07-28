## 操作场景
本文档指导您如何授权访问消息队列（CMQ）和配置消息队列 CMQ。


## 前提条件
物联网通信账号必须为第一次使用消息队列 CMQ。



## 操作步骤
### 授权访问
1. 登录物联网通信控制台，选择【产品列表】>【消息队列】，单击【授权访问消息队列（CMQ）】。
2. 授权成功之后会进入配置消息队列页面。
![](https://main.qcloudimg.com/raw/1a0c70c7b450606a2a36126729ca94bb.png)

### 配置消息队列
1. 在配置消息队列页面，根据需求勾选消息类型，消息队列 CMQ 配置消息类型有以下两种。
 - 设备上报消息
 - 设备状态变化通知
2. 完成消息类型选择后，单击【保存配置】。
3. 此时会弹出确认保存的窗口。单击【确定】后，物联网通信将会向默认队列`queue-iot-{productID}` 推送选择的消息类型。

>!
- 消息类型不能配置空选项.。
- 修改消息类型不能和上次配置的消息类型相同。

![](https://main.qcloudimg.com/raw/6cd86325e42790cc56c3e9447ceb0caa.png)
4. 创建成功后消息队列页面就会展示订阅的详细信息，您可以在在该页面修改订阅的消息类型。
![](https://main.qcloudimg.com/raw/d3c09f0b71dbc4ff09d5af4305218626.png)

### 删除消息队列
如果您想删除当前消息队列配置，可单击【删除当前配置】，即可完成删除。
![](https://main.qcloudimg.com/raw/a94cd916a39715edb1118dd01fa4cf02.png)

###  SDK 介绍
CMQ 接收消息的相关 SDK 介绍如下：
消息队列 CMQ 提供了如下两个接口从队列中**读取消息**：
- [ReceiveMessage](https://cloud.tencent.com/document/product/406/5839)：一次从队列中读取一条消息。
- [BatchReceiveMessage](https://cloud.tencent.com/document/product/406/5924)：一次从队列中读取多条消息。
    
消息队列的消息在读取后，需主动 **删除消息** 才能把消息从消息队列中去掉：   
- [DeleteMessage](https://cloud.tencent.com/document/api/406/5840)：从队列中删除一条消息。
- [BatchDeleteMessage](https://cloud.tencent.com/document/api/406/5841)：从队列中删除多条消息，一次最多删除16条。
    
消息队列的 SDK demo 使用，请参照消息队列提供的 [SDK demo](https://cloud.tencent.com/document/product/406/6107) 文档。

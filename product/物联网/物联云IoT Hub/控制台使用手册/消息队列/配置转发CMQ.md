## 授权访问消息队列(CMQ)
如果物联网通信帐号是第一次使用 CMQ，就会显示【授权访问消息队列(CMQ)】按钮。点击进行授权，授权成功之后会进入配置消息队列页面。
![](https://main.qcloudimg.com/raw/1a0c70c7b450606a2a36126729ca94bb.png)

## 配置消息队列
CMQ 配置消息类型有两个选项：“设备上报消息”和“设备状态变化通知”。根据需求勾选消息类型后，点击【保存配置】按钮，此时会弹出确认保存的窗口。点击【确定】后，物联网通信将会向默认队列```queue-iot-{productID}``` 推送选择的消息类型。
> **注意：**
> 
> 1. 消息类型不能配置空选项；
> 2. 修改消息类型不能和上次配置的消息类型相同。

![](https://main.qcloudimg.com/raw/6cd86325e42790cc56c3e9447ceb0caa.png)
创建成功后消息队列页面就会展示订阅的详细信息，用户也可以在该页面修改订阅的消息类型。
![](https://main.qcloudimg.com/raw/d3c09f0b71dbc4ff09d5af4305218626.png)

## 删除消息队列
点击【删除当前配置】即可删除当前消息队列配置。
![](https://main.qcloudimg.com/raw/a94cd916a39715edb1118dd01fa4cf02.png)

## CMQ 接收消息的 SDK 介绍
- 消息队列 CMQ 提供了如下两个接口从队列中 **读取消息**：
    [ReceiveMessage](https://cloud.tencent.com/document/product/406/5839)：一次从队列中读取一条消息。
    [BatchReceiveMessage](https://cloud.tencent.com/document/product/406/5924)：一次从队列中读取多条消息。
    
- 消息队列的消息在读取后，需主动 **删除消息** 才能把消息从消息队列中去掉：   
    [DeleteMessage](https://cloud.tencent.com/document/api/406/5840)：从队列中删除一条消息。
    [BatchDeleteMessage](https://cloud.tencent.com/document/api/406/5841)：从队列中删除多条消息，一次最多删除16条。
    
- 消息队列的 SDK demo 使用可以参照消息队列提供的 [SDK demo](https://cloud.tencent.com/document/product/406/6107)。

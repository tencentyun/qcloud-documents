## 授权访问消息队列(CMQ)
如果物联云帐号是第一次使用 CMQ，就会显示【授权访问消息队列(CMQ)】按钮。点击进行授权，授权成功之后会进入配置消息队列页面。
![](https://mc.qcloudimg.com/static/img/02d2649358e55c252f1d186bbe5d0e73/cmqbutton.png)

## 配置消息队列
CMQ 配置消息类型有两个选项：“设备上报消息”和“设备状态变化通知”。根据需求勾选消息类型后，点击【保存配置】按钮，此时会弹出确认保存的窗口。点击【确定】后，物联云将会向默认队列```queue-iot-{productID}``` 推送选择的消息类型。
> **注意：**
> 
> 1. 消息类型不能配置空选项；
> 2. 修改消息类型不能和上次配置的消息类型相同。

![](https://mc.qcloudimg.com/static/img/fcd5be040760ba6b59e4f6fdbf6042f3/cmq_save1.png)
创建成功后消息队列页面就会展示订阅的详细信息，用户也可以在该页面修改订阅的消息类型。
![](https://mc.qcloudimg.com/static/img/11e0a34d57cb71b2d3f928821c6ea587/cmq_detail_show.png)

## CMQ 接收消息的 SDK 介绍
- 消息队列 CMQ 提供了如下两个接口从队列中 **读取消息**：
	[ReceiveMessage](https://cloud.tencent.com/document/product/406/5839)：一次从队列中读取一条消息
	[BatchReceiveMessage](https://cloud.tencent.com/document/product/406/5924)：一次从队列中读取多条消息
	
- 消息队列的消息在读取后，需主动 **删除消息** 才能把消息从消息队列中去掉：	
	[DeleteMessage](https://cloud.tencent.com/document/api/406/5840)：从队列中删除一条消息
	[BatchDeleteMessage](https://cloud.tencent.com/document/api/406/5841)：从队列中删除多条消息，一次最多删除16条
	
- 消息队列的 SDK demo 使用可以参照消息队列提供的 [SDK demo](https://cloud.tencent.com/document/product/406/6107)。

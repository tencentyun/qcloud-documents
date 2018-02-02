### 消息队列 CMQ

#### 授权访问消息队列（CMQ）

如果物联云帐号是第一次使用CMQ，请点击【授权访问消息队列(CMQ)】对账号进行，点击进行授权，授权成功之后会进入配置消息队列页面。

![](https://mc.qcloudimg.com/static/img/02d2649358e55c252f1d186bbe5d0e73/cmqbutton.png)

#### 配置消息队列

配置消息类型有两个选项：

- 设备上报消息

- 设备状态变化通知

根据需求进行勾选消息类型后点击【保存配置】按钮，此时会弹出确认保存的窗口，确认之后物联云将会向默认队列：```queue-iot-{productID}``` 推送选择的消息类型。

![](https://mc.qcloudimg.com/static/img/fcd5be040760ba6b59e4f6fdbf6042f3/cmq_save1.png)

创建成功后消息队列页面就会展示订阅的详细信息，用户也可以在该页面修改订阅的消息类型。

![](https://mc.qcloudimg.com/static/img/11e0a34d57cb71b2d3f928821c6ea587/cmq_detail_show.png)

> **注意：**
> 
> 1. 消息类型不能配置空选项；
> 2. 修改消息类型不能和上次配置的消息类型相同。

#### CMQ 接收消息的 SDK 介绍

- 消息队列CMQ提供了如下两个接口来从队列中**读取消息**：

	[ReceiveMessage](https://cloud.tencent.com/document/product/406/5839) :    一次从队列中读取一条消息

	[BatchReceiveMessage](https://cloud.tencent.com/document/product/406/5924) :    一次从队列中读取多条消息

- 消息队列的消息在读取后，依然会在消息队列中，需要主动**删除消息**才能把消息从消息队列中去掉。
	
	[**DeleteMessage**](https://cloud.tencent.com/document/api/406/5840) :            从队列中删除一条消息
	
	[**BatchDeleteMessage**](https://cloud.tencent.com/document/api/406/5841) :       从队列中删除多条消息，一次最多删除16条

- 消息队列的SDK demo

	接口的使用可以参照消息队列提供的 [SDK demo](https://cloud.tencent.com/document/product/406/6107)

### 其他说明

点击使用教程链接即可查看消息队列使用教程

![](https://mc.qcloudimg.com/static/img/e21921638587d6d2d19c688df2d4b5e6/shiyong_jiaocheng.png)

### 延伸阅读

![](https://mc.qcloudimg.com/static/img/1a81bad91b5096f30ef8c44c33c60cf9/xiaoxiduilie_pro.png)

点击官网产品栏目中的 [消息队列](https://cloud.tencent.com/document/product/634/12724) 了解腾讯云互联网中间件消息队列产品。
## 服务端订阅功能简介
服务端订阅功能为用户提供了一种可靠的设备与第三方服务端之间的异步通信通信机制。开启此功能后，物联云后台会将产品下所有设备的指定消息都转发到腾讯云的消息队列CMQ中，然后第三方用户使用消息队列CMQ提供的SDK从消息队列中拉取消息。如何使用消息队列CMQ的SDK来拉取消息，可以查看文末"参考"部分关于消息队列接收消息SDK介绍。下面是服务端订阅功能的示意图。


![image](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/iot_server_subs.png)


## 适用场景
服务端订阅功能最大的特点是与腾讯云的消息队列CMQ服务结合，提供了可靠的消息存储与传输机制。消息队列CMQ甚至可以和其它腾讯云的计算模块连通，提供无缝的计算服务。基于服务端订阅功能的特点，它适用于以下场景：

1. 需要快速稳定的接收设备消息，特别是设备会产生海量消息或者消息量在不同时间点会有很大的波动时
2. 需要实时地处理设备状态消息，保证设备状态信息不会丢失
3. 需要与其它腾讯云计算模块连接，处理海量设备信息



## 转发的消息类型
目前服务端订阅功能会转发如下两种消息类型：
- 设备状态通知
- 设备上报消息

**设备状态通知：** 即设备的上下线变化通知，以及物联网套件产生的一些系统通知。<br>
**设备上报消息：** 即设备发布到Topic的所有消息。开通产品的服务端订阅功能并且在参数配置页面勾选"设备上报消息"选项后，物联云后台就会把该产品下所有设备发布到Topic中的消息都转发到消息队列CMQ中。


## 消息格式

上报到消息队列的消息格式采用json字符串的形式，格式如下所示:
```
{
    "MsgType":"Publish",
    "Event":"",
    "Topic":"iot-product/iot-device/update",
    "Seq":244,
    "PayloadLen":121,
    "DeviceId":"144115205259838664",
    "ProductName":"iot-product",
    "DeviceName":"iot-device",
    "Payload":"eyJhY3Rpb24iOiAicmVwb3J0IiwgInRhcmdldERldmljZSI6ICJhYyIsICJkZXZJZCI6MTQ0MTE1MjA1MjU5ODM4NjY0LCAiZGF0YSI6eyJjdXJyZW50IjoyNTExLCAidGVtcCI6MjczMSwgIndhcm5pbmciOjF9fQ=="
}
```

下面是各个字段的含义：<br>
**MsgType**: 上报的消息类型，取值为"Publish"或"Status"，代表设备上报消息和设备状态通知<br>
**Event**:  当MsgType为Status时该字段才有效，代表状态通知的事件，比如取值为"Online"代表上线，"Offline"代表下线<br>
**Topic**:  Publish消息的主题<br>
**Seq**:    消息的序列号<br>
**PayloadLen**:  消息内容Payload的长度<br>
**DeviceId**:    设备ID<br>
**ProductName**:    产品名<br>
**DeviceName**: 设备名<br>
**Payload**:    消息内容，是一个用Base64编码的字符串。<br>


## 开通服务端订阅的过程示例

**一、授权访问消息队列CMQ**<br>
如果物联云帐号是第一次使用服务端订阅，就会显示【授权访问消息队列(CMQ)】按钮。

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/TIM截图20171127104957.png)

点击进行授权，授权成功之后会进入配置消息队列页面。。

**二、配置消息队列**<br>
配置消息队列有两个选项：
1) 设备上报消息
2) 设备状态变化通知
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/TIM截图20171127105037.png)

此处可以根据需求进行勾选，完成之后点击【保存配置】按钮。此时，会弹出确认保存的窗口，提示保存之后，物联云会立即向 _**默认队列**_ 推送选择的消息类型。

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/TIM截图20171127105105.png)


**三、 开通成功，展示订阅信息**<br>
创建成功后服务端订阅页面就会展示订阅的地区，队列名，角色名和消息类型。
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/TIM截图20171127105225.png)

**四、 修改消息类型**<br>
点击消息类型一行上的【修改消息类型】按钮。即可进行消息类型修改。

> **注意:**
> 1) 消息类型不能配置空选项；
> 2) 修改消息类型不能和上次配置的消息类型相同。

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/TIM截图20171127105248.png)

点击【保存修改】按钮即可保存当前修改的消息类型。
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/TIM截图20171127105327.png)


## 参考


#### 消息队列接收消息的SDK介绍
**一、 读取消息**<br>
消息队列CMQ提供了如下两个接口来从队列中读取消息：
- **ReceiveMessage**            一次从队列中读取一条消息
- **BatchReceiveMessage**       一次从队列中读取多条消息

两个接口都提供http和https两种访问方式，接口的详细说明可以见<br>
ReceiveMessage
https://cloud.tencent.com/document/product/406/5839 <br>
BatchReceiveMessage
https://cloud.tencent.com/document/product/406/5924

**二、 删除消息**<br>
消息队列的消息在读取后，依然会在消息队列中，需要主动删除消息才能把消息从消息队列中去掉。
- **DeleteMessage**            从队列中删除一条消息
- **BatchDeleteMessage**        从队列中删除多条消息，一次最多删除16条

接口的详细说明可以见<br>
ReceiveMessage
https://cloud.tencent.com/document/api/406/5840 <br>
BatchReceiveMessage
https://cloud.tencent.com/document/api/406/5841

**三、 消息队列的SDK demo**<br>
接口的使用可以参照消息队列提供的SDK demo。<br>
https://cloud.tencent.com/document/product/406/6107




本文将指导您的客户端如何使用 IM （即时通讯）功能，在房间内收发消息。

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/PC/demo_msg.zip)

## 相关概念

 * [群组系统](/document/product/647/16792#.E7.BE.A4.E7.BB.84.E7.B3.BB.E7.BB.9F)

|类型|名称|类|描述|
|--|--|--|--|
|TEXT|文本消息|MessageTextElem|消息内容为一个字符串（String 类型）|
|CUSTOM|自定义消息|MessageCustomElem|消息内容包含 data 和 ext 字段，其中可以放入用户自定义的数据|
|IMAGE|图片|MessageImageElem|消息内容为发送\接收的图片信息|
|FACE|表情消息|MessageFaceElem|表情消息一般传输一个表情的索引值，收到索引后，显示对应的表情|

## 开启IM功能
初始化 SDK
```c++
GetILive()->init(SDKAppId, AccountType, false);
```

这里最后一个参数 imSupport 被设置为 false，此参数表示是否使用 IM 功能；要使用 IM 收发消息，就需要开启 IM 功能，即此参数设置为 true,即
```c++
GetILive()->init(SDKAppId, AccountType, true);
```

启用 IM 功能后，用户创建房间将会创建对应的 IM 群组，群组类型可以在创建房间参数中指定( iLiveRoomOption的groupType ),一般使用 E_AVChatRoom_Group，即默认值；

> 创建房间的用户退出房间，将会解散对应的IM群组。

## 设置消息监听

开启 IM 功能情况下，要收到消息，需要设置接收消息的回调函数。
```c++
//接收消息回调
void OnMessageCallback(const Message &msg, void* data)
{
	for (int i=0; i<msg.elems.size(); ++i)
	{
		MessageElem *pElem = msg.elems[i];
		if (pElem->type == TEXT)
		{
			MessageTextElem *elem = dynamic_cast<MessageTextElem*>(pElem);
			printf("recv msg from %s : %s\n", msg.sender.c_str(), elem->content.c_str());
		}
	}
}
GetILive()->setMessageCallBack(OnMessageCallback, NULL);
```

## 发送消息
要往群里发送消息，只需要调用 sendGroupMessage() 接口即可，例如要往群里发送文本消息，代码如下：
```c++
Message msg;
MessageTextElem *elem = new MessageTextElem("这里是文本消息内容");
msg.elems.push_back(elem);
GetILive()->sendGroupMessage(msg, [](void* data) {
	//发送消息成功
}, [](const int code, const char* desc, void* data) {
	//发送消息失败
}, NULL);
```

## 源码说明
本例 Demo，新建了两个项目，一个创建房间( Creator )，一个加入房间( Joiner )；两个用户都开一个定时器，定时往群里发送消息，收到消息后，都将其打印输出到控制台。

## 运行结果

![](https://main.qcloudimg.com/raw/6cb42880b4fa9b911bd8386139ecfb04.png)

![](https://main.qcloudimg.com/raw/54addf7999d3f78fca42a0636397d768.png)

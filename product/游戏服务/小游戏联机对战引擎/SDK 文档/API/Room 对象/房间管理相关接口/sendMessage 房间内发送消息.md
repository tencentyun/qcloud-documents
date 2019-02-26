### sendMessage 房间内发送消息
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|sendMessagePara|SendMessagePara|发送消息参数|
|callback|```ReqCallback<lagame.RoomChatRsp>```|发送消息回调|

SendMessagePara 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|recvUserList|string[]|接收消息玩家ID数组|
|message|string|消息内容|

lagame.RoomChatRsp 暂未定义任何字段。

调用结果将在 callback 中异步返回。调用成功后玩家和全部接收消息的玩家将收到 receiveMessageBroadcast 广播。

**返回值说明**

同步返回该次请求的序列号，类型为 number。

**使用示例**
```
const sendMessagePara = {
	recvUserList: ["xxxxxxxx1", "xxxxxxxx2"],
	message: "hello",
};

let seq = room.sendMessage(sendMessagePara, event => console.log(event));
```


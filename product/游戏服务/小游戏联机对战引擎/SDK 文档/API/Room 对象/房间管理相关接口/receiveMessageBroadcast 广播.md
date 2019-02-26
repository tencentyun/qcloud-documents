### receiveMessageBroadcast 广播

**参数说明**

|参数名|类型|描述|
|:---|---|---|---|
|event|```ResponseEvent<lagame.BroadcastRoomChatRsp>```|回调参数|

lagame.BroadcastRoomChatRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|sendUser|string|发送者ID|
|message|string|消息内容|
|roomId|number|房间ID|

receiveMessageBroadcast 广播表示收到来自 ID 为 sendUser 的玩家消息。

**返回值说明**

无

**使用示例**

```
room.receiveMessageBroadcast = event => console.log("新消息", event.data.message);
```


### joinRoomBroadcast 广播

**参数说明**

|参数名|类型|描述|
|:---|---|---|---|
|event|```ResponseEvent<lagame.BroadcastJoinRoomRsp>```|回调参数|

lagame.BroadcastJoinRoomRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|roomInfo|lagame.RoomInfo|房间信息|
|joinOpenId|string|加房玩家ID|

joinRoomBroadcast 广播表示该房间有新玩家加入。房间内全部成员都会收到该广播。

**返回值说明**

无


**使用示例**

```
room.joinRoomBroadcast = event => console.log("新玩家加入", event.joinOpenId);
```


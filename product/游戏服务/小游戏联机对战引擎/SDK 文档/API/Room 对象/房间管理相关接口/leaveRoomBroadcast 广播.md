### leaveRoomBroadcast 广播

**参数说明**

|参数名|类型|描述|
|:---|---|---|---|
|event|```ResponseEvent<lagame.BroadcastLeaveRoomRsp>```|回调参数|

lagame.BroadcastLeaveRoomRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|roomInfo|lagame.RoomInfo|房间信息|
|leaveOpenId|string|加房玩家ID|

leaveRoomBroadcast 广播表示该房间有玩家退出。房间内全部成员都会收到该广播。

**返回值说明**

无


**使用示例**

```
room.leaveRoomBroadcast = event => console.log("玩家退出", event.leaveOpenId);
```


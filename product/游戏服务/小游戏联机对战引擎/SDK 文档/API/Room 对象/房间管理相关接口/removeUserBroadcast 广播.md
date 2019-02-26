### removeUserBroadcast 广播

**参数说明**

|参数名|类型|描述|
|:---|---|---|---|
|event|```ResponseEvent<lagame.BroadcastKickUserRsp>```|回调参数|

lagame.BroadcastKickUserRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|roomInfo|lagame.RoomInfo|房间信息|
|kickedOpenId|string|被移除玩家ID|
|owner|string|房主ID|

removeUserBroadcast 广播表示有玩家被房主移除。房间内全部成员都会收到该广播。

**返回值说明**

无

**使用示例**

```
room.removeUserBroadcast = event => console.log("玩家被移除", event.kickedOpenId);
```


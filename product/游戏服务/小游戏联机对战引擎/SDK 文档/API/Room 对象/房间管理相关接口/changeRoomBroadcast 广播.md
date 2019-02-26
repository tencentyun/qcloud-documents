### changeRoomBroadcast 广播

**参数说明**

|参数名|类型|描述|
|:---|---|---|---|
|event|```ResponseEvent<lagame.BroadcastChangePropertiesRsp>```|回调参数|

lagame.BroadcastChangePropertiesRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|roomInfo|lagame.RoomInfo|房间信息|
|owner|string|房主ID|

changeRoomBroadcast 广播表示房主修改了该房间属性。房间内全部成员都会收到该广播。

**返回值说明**

无

**使用示例**

```
room.changeRoomBroadcast = event => console.log("房间属性变更", event.roomInfo);
```


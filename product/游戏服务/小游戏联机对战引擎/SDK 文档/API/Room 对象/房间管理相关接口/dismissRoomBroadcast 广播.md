### dismissRoomBroadcast 广播

**参数说明**

|参数名|类型|描述|
|:---|---|---|---|
|event|```ResponseEvent<lagame.BroadcastDismissRoomRsp>```|回调参数|

lagame.BroadcastDismissRoomRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|roomId|number|房间ID|
|owner|string|房主ID|

dismissRoomBroadcast 广播表示房主解散了该房间。房间内全部成员都会收到该广播。

**返回值说明**

无

**使用示例**

```
room.dismissRoomBroadcast = event => console.log("房间已解散");
```



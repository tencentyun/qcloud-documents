### changeUserStateBroadcast 广播

**参数说明**

|参数名|类型|描述|
|:---|---|---|---|
|event|```ResponseEvent<lagame.BroadcastChangeUserStateRsp>```|回调参数|

lagame.BroadcastChangeUserStateRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|changeUser|string|玩家ID|
|customStatus|number|玩家状态|
|roomId|number|房间ID|
|roomInfo|lagame.RoomInfo|房间信息|

changeUserStateBroadcast 广播表示房间内 ID 为 changeUser 的玩家状态发生变化。玩家状态由开发者自定义。

**返回值说明**

无

**使用示例**

```
room.changeUserStateBroadcast = event => {
	console.log("玩家状态变化", event.data.changeUser);
};
```
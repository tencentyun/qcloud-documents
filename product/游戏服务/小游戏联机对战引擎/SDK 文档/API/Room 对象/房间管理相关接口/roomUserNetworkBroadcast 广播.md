### roomUserNetworkBroadcast 广播

**参数说明**

|参数名|类型|描述|
|:---|---|---|---|
|event|```ResponseEvent<lagame.BroadcastChangeUserNetworkStateRsp>```|回调参数|

lagame.BroadcastChangeUserNetworkStateRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|changeUser|string|玩家ID|
|networkState|lagame.NetworkState|网络状态，有四种情况，参考“枚举类型”一节|
|roomId|number|房间ID|
|roomInfo|lagame.RoomInfo|房间信息|

roomUserNetworkBroadcast 广播表示 ID 为 changeUser 的玩家网络状态发生变化。玩家在房间中、游戏中的网络变化都会触发该广播，因此 networkState 将有四中情况，分别表示房间中上下线、游戏中上下线。注意与 UserInfo 中的 networkState 区分，后者只表示玩家在房间中的网络状态。

**返回值说明**

无

**使用示例**

```
room.roomUserNetworkBroadcast = event => {
	if (event.data.networkState === MBS.ENUM.NetworkState.ROOM_OFFLINE)
		console.log("玩家上线");
};
```

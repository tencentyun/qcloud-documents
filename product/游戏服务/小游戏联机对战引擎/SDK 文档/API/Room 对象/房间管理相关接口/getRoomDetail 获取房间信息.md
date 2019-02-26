### getRoomDetail 获取房间信息
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|callback|```ReqCallback<lagame.SelectRoomRsp>```|获取房间信息回调|

lagame.SelectRoomRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|
|gameId|number|游戏ID|
|roomId|number|房间ID|
|roomInfo|lagame.RoomInfo|房间信息|
|userLocate|lagame.UserLocate|玩家位置，参考“枚举类型”一节|
|networkState|lagame.NetworkState|该玩家网络状态，参考“枚举类型”一节|

该接口获取的是玩家所在房间信息，玩家只能加入一个房间。调用结果将在 callback 中异步返回。

该接口也可用于检查玩家是否已经加入房间（比如重新打开游戏时），如果未加入任何房间，lagame.SelectRoomRsp 中的字段 userLocate 将为 0。

操作成功后，roomInfo 属性将更新。

**返回值说明**

同步返回该次请求的序列号，类型为 number。

**使用示例**
```
const seq = room.getRoomDetail(event => {
	if (event.code !== 0) {
		return;
	}
	if (event.data.userLocate === 0) {
		console.log("玩家不在房间内");
	} else {
		console.log("房间名", event.data.roomInfo.roomName);
	}
});
```


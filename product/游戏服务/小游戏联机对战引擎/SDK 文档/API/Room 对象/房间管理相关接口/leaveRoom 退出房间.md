### leaveRoom 退出房间
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|para|object|预留参数，传{}即可|
|callback|```ReqCallback<lagame.LeaveRoomRsp>```|退出房间回调|

lagame.LeaveRoomRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomInfo|lagame.RoomInfo|房间信息|

leaveRoom 调用结果将在 callback 中异步返回。退出成功后，房间内全部成员都会都到一条玩家退出房间广播 leaveRoomBroadcast。

操作成功后，roomInfo 属性将更新。

**返回值说明**

同步返回该次请求的序列号，类型为 number。

**使用示例**
```
const seq = room.leaveRoom({}, event => {
	if (event.code === 0) {
		console.log("退房成功");
	}
});
```


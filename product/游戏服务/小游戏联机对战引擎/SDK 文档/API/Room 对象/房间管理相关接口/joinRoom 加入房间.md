### joinRoom 加入房间
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|joinRoomPara|JoinRoomPara|加入房间参数|
|callback|```ReqCallback<lagame.JoinRoomRsp>```|加入房间回调|

JoinRoomPara 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomId|number|房间ID|
|userInfo|UserInfo|申请加入房间的用户信息|

lagame.JoinRoomRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomId|string|房间ID|
|roomInfo|lagame.RoomInfo|房间信息|
|gameId|number|游戏ID|

joinRoom 调用结果将在 callback 中异步返回。加房成功后，房间内全部成员都会都到一条玩家加入房间广播 joinRoomBroadcast。

操作成功后，roomInfo 属性将更新。

**返回值说明**

同步返回该次请求的序列号，类型为 number。

**使用示例**
```
const userInfo = {
	userName: "Tom",
	customStatus: 1,
	profile: "https://xxx.com/icon.png",
};

const roomId = 12345678;

const joinRoomPara = {
	roomId,
	userInfo,
};

const seq = room.joinRoom(joinRoomPara, event => console.log(event));
```


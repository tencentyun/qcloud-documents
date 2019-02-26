### createRoom 创建房间
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|createRoomPara|CreateRoomPara|房间参数|
|callback|```ReqCallback<lagame.CreateRoomRsp>```|创建房间回调|

CreateRoomPara 定义如下：

|字段名|类型|描述|可选|
|:---|---|---|---|
|roomName|string|房间名称| |
|maxUsers|number|房间最大玩家数量| |
|roomType|string|房间类型| |
|viewer|boolean|是否支持观战| |
|invitedFlag|boolean|是否支持邀请码| |
|properties|string|自定义房间属性，如房间状态等| |
|userInfo|UserInfo|玩家信息| |
|privateFlag|boolean|是否私有| |
|frameRate|number|帧率，取值 5 ~ 30，默认 15|是|

UserInfo 定义如下：

|字段名|类型|描述|
|:---|---|---|
|userName|string|玩家昵称|
|customStatus|number|自定义玩家状态|
|profile|string|自定义玩家信息|

lagame.CreateRoomRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomId|number|房间ID|
|roomInfo|lagame.RoomInfo|房间信息|
|gameId|number|游戏ID|

createRoom 调用结果将在 callback 中异步返回。

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

const createRoomPara = {
	roomName: "房间名",
	maxUsers: 5,
	roomType: 1,
	viewer: false,
	invitedFlag: true,
	properties: "WAIT",
	actions: 1,
	userInfo: userInfo,
	privateFlag: false,
	frameRate: 20,
};

const seq = room.createRoom(createRoomPara, event => console.log(event));
```


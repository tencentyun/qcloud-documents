### changeRoom 修改房间
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|changeRoomPara|ChangeRoomPara|房间变更参数|
|callback|```ReqCallback<lagame.ChangeRoomRsp>```|修改房间回调|

ChangeRoomPara 定义如下：

|字段名|类型|描述|可选|
|:---|---|---|---|
|roomName|string|房间名称|是|
|owner|string|房主ID|是|
|maxUsers|number|房间最大玩家数量|是|
|roomType|string|房间类型|是|
|viewer|boolean|是否支持观战|是|
|invitedFlag|boolean|是否支持邀请码|是|
|properties|string|自定义房间属性|是|
|privateFlag|boolean|是否私有|是|

lagame.ChangeRoomRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|
|gameId|number|游戏ID|
|openId|string|玩家ID|
|roomId|number|房间ID|
|roomInfo|lagame.RoomInfo|房间信息|

changeRoom 调用结果将在 callback 中异步返回。修改成功后，房间内全部成员都会都到一条修改房间广播 changeRoomBroadcast。

操作成功后，roomInfo 属性将更新。

只有房主拥有修改房间权限，通过修改”房主ID“可以切换房主。

**返回值说明**

同步返回该次请求的序列号，类型为 number。

**使用示例**
```
const changeRoomPara = {
	roomName: "房间名",
	maxUsers: 10,
};

const seq = room.changeRoom(changeRoomPara, event => console.log(event));
```


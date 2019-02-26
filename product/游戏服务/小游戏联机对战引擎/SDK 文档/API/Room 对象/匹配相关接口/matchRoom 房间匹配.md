### matchRoom 房间匹配
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|matchRoomPara|MatchRoomPara|房间匹配参数|
|callback|```ReqCallback<lagame.MatchRoomSimpleRsp>```|房间匹配回调|

MatchRoomPara 定义如下：

|字段名|类型|描述|
|:---|---|---|
|userInfo|UserInfo|用户信息|
|maxUsers|number|最大房间人数|
|roomType|string|房间的类型|

lagame.MatchRoomSimpleRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomInfo|lagame.RoomInfo|房间信息|

调用该接口后将发起房间匹配，匹配结果将在 callback 中异步返回。

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

const matchRoomPara = {
	userInfo,
	maxUsers: 5,
	roomType: "1",
};

const seq = room.matchRoom(matchRoomPara, event => {
	if (event.code !=== 0) {
		console.log("匹配失败", event.code);
	}
});
```

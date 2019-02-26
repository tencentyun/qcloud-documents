### matchUsers 多人匹配
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|matchUsersPara|MatchUsersPara|多人匹配参数|
|callback|```ReqCallback<lagame.MatchUsersSimpleRsp>```|多人匹配回调|

MatchUsersPara 定义如下：

|字段名|类型|描述|可选|
|:---|---|---|---|
|matchUserInfo|MatchUserInfo|用户信息| |
|maxUsers|number|最大房间人数| |
|roomType|string|房间的类型| |
|scoreMatch|boolean|是否按分数匹配| |
|score|number|分数|是|
|scoreError|number|分数误差|是|

MatchUserInfo 定义如下：

|字段名|类型|描述|
|:---|---|---|
|userName|string|玩家昵称|
|customStatus|number|自定义玩家状态|
|profile|string|自定义玩家信息|
|matchProps|string|预留字段，忽略|

lagame.MatchUsersSimpleRsp 暂未定义任何字段。

调用该接口后将发起多人在线匹配，callback 将异步返回调用结果。返回码为 0 表示匹配成功，Room 对象内部 roomInfo 属性将自动更新。

如果 scoreMatch 为 true，则需要设置 score、scoreError，这两个参数设置了该玩家可接受的匹配玩家分数范围。比如匹配参数 score = 10，scoreError = 3，该玩家将匹配分数在 7 ~ 13 之间的玩家。

操作成功后，roomInfo 属性将更新。

**返回值说明**

同步返回该次请求的序列号，类型为 number。

**使用示例**
```
const matchUserInfo = {
	userName: "Tom",
	customStatus: 1,
	profile: "https://xxx.com/icon.png",
};

const matchUsersPara = {
	matchUserInfo,
	maxUsers: 5,
	roomType: "1",
	scoreMatch: true,
	score: 10,
	scoreError: 3,
};
// 发起匹配
const seq = room.matchUsers(matchUsersPara, event => {
	if (event.code !=== 0) {
		console.log("匹配失败", event.code);
	} else {
		console.log("匹配成功", room.roomInfo);
	}
});
```


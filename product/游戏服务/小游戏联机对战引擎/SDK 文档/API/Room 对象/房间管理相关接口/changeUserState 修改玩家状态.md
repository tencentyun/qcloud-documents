### changeUserState 修改玩家状态
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|changeUserStatePara|ChangeUserStatePara|修改玩家状态参数|
|callback|```ReqCallback<lagame.ChangeUserStateRsp>```|修改玩家状态回调|

ChangeUserStatePara 定义如下：

|字段名|类型|描述|
|:---|---|---|
|customStatus|number|玩家状态|

lagame.ChangeUserStateRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomInfo|lagame.RoomInfo|房间信息|

修改玩家状态是修改 UserInfo 中的 customStatus 字段，玩家的状态由开发者自定义。每个玩家只能修改自己的状态，调用结果将在 callback 中异步返回。修改成功后，房间内全部成员都会都到一条修改玩家状态广播 changeUserStateBroadcast。

操作成功后，roomInfo 属性将更新。

**返回值说明**

同步返回该次请求的序列号，类型为 number。

**使用示例**
```
const changeUserStatePara = {
	customStatus: 2,
};

const seq = room.changeUserState(changeUserStatePara, event => console.log(event));
```


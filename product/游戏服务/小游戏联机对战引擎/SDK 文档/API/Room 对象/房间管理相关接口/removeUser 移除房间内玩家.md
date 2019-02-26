### removeUser 移除房间内玩家
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|removeUserPara|RemoveUserPara|移除玩家参数|
|callback|```ReqCallback<lagame.RemoveUserRsp>```|移除玩家回调|

RemoveUserPara 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|removeOpenId|string|被移除玩家 ID|

lagame.RemoveUserRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomInfo|lagame.RoomInfo|房间信息|

调用结果将在 callback 中异步返回。移除玩家成功后，房间内全部成员都会都到一条移除玩家广播 removeUserBroadcast。

操作成功后，roomInfo 属性将更新。

**返回值说明**

同步返回该次请求的序列号，类型为 number。

**使用示例**
```
const removeUserPara = {
	removeOpenId: "xxxxxx",
};

const seq = room.removeUser(removeUserPara, event => console.log(event));
```


### dismissRoom 解散房间
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|para|object|预留参数，传{}即可|
|callback|```ReqCallback<lagame.DismissRoomRsp>```|解散房间回调|

lagame.DismissRoomRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomId|string|房间ID|

dismissRoom 调用结果将在 callback 中异步返回。解散成功后，房间内全部成员都会都到一条解散房间广播 dismissRoomBroadcast。

操作成功后，roomInfo 属性将更新。

只有房主拥有解散房间权限。

**返回值说明**

同步返回该次请求的序列号，类型为 number。

**使用示例**
```
const seq = room.dismissRoom({}, event => {
	if (event.code === 0) {
		console.log("解散成功");
	}
});
```


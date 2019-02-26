### getRoomList 获取房间列表
**参数说明**

|参数名|类型|描述|
|:---|---|---|
|getRoomListPara|GetRoomListPara|获取房间列表参数|
|callback|```ReqCallback<lagame.SelectRoomListRsp>```|获取房间列表回调|

GetRoomListPara 定义如下：

|字段名|类型|描述|
|:---|---|---|---|
|pageNo|number|页号，从1开始|
|pageSize|number|每页数量|

lagame.SelectRoomListRsp 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomList|lagame.RoomInfo[]|房间列表|
|gameId|number|游戏ID|
|total|number|房间总数|

调用结果将在 callback 中异步返回。

**注意**：该接口为 Room 的静态方法，只能通过 ```Room.getRoomList``` 方式调用，Room 实例无法直接访问该方法。

**返回值说明**

同步返回该次请求的序列号，类型为 number。

**使用示例**
```
const getRoomListPara = {
	pageNo: 1,
	pageSize: 10,
};

// 不要使用 room.getRoomList
// 直接使用 Room 对象
const seq = Room.getRoomList(getRoomListPara, event => console.log(event));
```


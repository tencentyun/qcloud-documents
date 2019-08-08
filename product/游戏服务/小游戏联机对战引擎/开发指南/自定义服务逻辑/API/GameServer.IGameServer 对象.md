
GameServer.IGameServer 对象即实时服务器接口。提供了接收客户端消息、监听房间广播相关接口。

### mode 属性

**描述**
mode 是实时服务器处理客户端消息的模式。可以取值为 "sync" 或 "async"。

- 当 mode 为 "sync" 时，实时服务器将使用同步模式处理客户端消息。开发者在 onRecvFromClient 回调中必须显式调用 SDK.exitAction 方法，游戏 Server 才能处理下一条 onRecvFromClient 广播。
- 当 mode 为 "async" 时，实时服务器将使用异步模式处理客户端消息。每次监听到 onRecvFromClient 广播时都将执行回调函数。

**使用示例**

```
const gameServer = {};
gameServer.mode = "async";
```

### onInitGameData 接口

**描述**

初始化游戏数据时的回调接口。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|args|{ room: IRoomInfo; }|回调参数|

IRoomInfo 定义如下：

|字段名|类型|描述|
|:---|---|---|
|id|number|房间 ID|
|name|string|房间名称|
|type|string|房间类型|
|createType|CreateType|创建房间方式，参考 [枚举类型](https://cloud.tencent.com/document/product/1038/33333) 一节|
|maxPlayers|number|房间最大玩家数量|
|owner|string|房主 ID|
|isPrivate|boolean|是否私有|
|customProperties|string|房间自定义属性|
|playerList|IPlayerInfo[]|玩家列表|
|teamList|ITeamInfo[]|团队属性|
|frameSyncState|FrameSyncState|房间状态，参考 [枚举类型](https://cloud.tencent.com/document/product/1038/33333) 一节|
|frameRate|number|帧率|
|routeId|string|路由ID|
|createTime|number|房间创建时的时间戳，秒|
|startGameTime|number|开始帧同步时的时间戳，秒|

ITeamInfo 定义如下：

|字段名|类型|描述|
|:---|---|---|
|id|string|队伍 ID|
|name|string|队伍名称|
|minPlayers|number|队伍最小人数|
|maxPlayers|number|队伍最大人数|

IPlayerInfo 定义如下：

|字段名|类型|描述|
|:---|---|---|
|id|string|玩家 ID|
|name|string|玩家昵称|
|teamId|string|队伍 ID|
|customPlayerStatus|number|自定义玩家状态|
|customProfile|string|自定义玩家信息|
|commonNetworkState|NetworkState|玩家在房间的网络状态，参考 [枚举类型](https://cloud.tencent.com/document/product/1038/33333) 一节，只取房间中的两种状态|
|relayNetworkState|NetworkState|玩家在游戏中的网络状态，参考 [枚举类型](https://cloud.tencent.com/document/product/1038/33333) 一节，只取游戏中的两种状态|

**返回值说明**

在该接口需要返回一个 GameData 类型数据，该数据会作为游戏初始化数据，在整个房间被销毁之前都能使用。

GameData 默认为 object 类型，开发者可以根据需要进行自定义。

>? onInitGameData 方法是在 onCreateRoom 之后，收到 onRecvFromClient 广播时检查 gameData：如果 gameData 为空，先执行 onInitGameData 再执行 onRecvFromClient；如果 gameData 不为空，只执行 onRecvFromClient。

**使用示例**

```
const gameServer = {};
gameServer.onInitGameData = args => {
    return { room: args.room };
};
```

### onRecvFromClient 接口

**描述**

接收玩家消息回调接口。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|args|ActionArgs&lt;UserDefinedData&gt;|回调参数|

ActionArgs 定义请参考 [ActionArgs 对象](https://cloud.tencent.com/document/product/1038/34992)。

UserDefinedData 即玩家的消息类型，类型为 object。开发者可以根据需要进行自定义。

**返回值说明**

无。

>? mode 为 "sync" 时需要在该回调里面显式调用 args.SDK.exitAction 方法才能继续处理下一条 onRecvFromClient 广播消息。

**使用示例**

```
const gameServer = {};
gameServer.mode = "sync";
gameServer.onRecvFromClient = args => {
    args.SDK.sendData({ playerIdList: [], data: { msg: "hello" } });
    args.SDK.exitAction();
};
```

### onCreateRoom 接口

**描述**

创建房间广播回调接口。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|args|ActionArgs&lt;ICreateRoomBst&gt;|回调参数|

ICreateRoomBst 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomInfo|IRoomInfo|房间信息|

**返回值说明**

无。

**使用示例**

```
const gameServer = {};
gameServer.onCreateRoom = args => {
    args.SDK.logger.debug("onCreateRoom");
};
```

### onJoinRoom 接口

**描述**

玩家加房广播回调接口。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|args|ActionArgs&lt;IJoinRoomBst&gt;|回调参数|

IJoinRoomBst 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomInfo|IRoomInfo|房间信息|
|joinPlayerId|string|加房玩家 ID|

**返回值说明**

无。

**使用示例**

```
const gameServer = {};
gameServer.onJoinRoom = args => {
    args.SDK.logger.debug("onJoinRoom");
};
```

### onLeaveRoom 接口

**描述**

玩家退房广播回调接口。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|args|ActionArgs&lt;ILeaveRoomBst&gt;|回调参数|

ILeaveRoomBst 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomInfo|IRoomInfo|房间信息|
|leavePlayerId|string|退房玩家 ID|

**返回值说明**

无。

**使用示例**

```
const gameServer = {};
gameServer.onLeaveRoom = args => {
    args.SDK.logger.debug("onLeaveRoom");
};
```

### onRemovePlayer 接口

**描述**

移除玩家广播回调接口。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|args|ActionArgs&lt;IRemovePlayerBst&gt;|回调参数|

IRemovePlayerBst 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomInfo|IRoomInfo|房间信息|
|removePlayerId|string|被移除玩家 ID|

**返回值说明**

无。

**使用示例**

```
const gameServer = {};
gameServer.onRemovePlayer = args => {
    args.SDK.logger.debug("onRemovePlayer");
};
```

### onChangeRoom 接口

**描述**

修改房间属性广播回调接口。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|args|ActionArgs&lt;IChangeRoomBst&gt;|回调参数|

IChangeRoomBst 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomInfo|IRoomInfo|房间信息|

**返回值说明**

无。

**使用示例**

```
const gameServer = {};
gameServer.onChangeRoom = args => {
    args.SDK.logger.debug("onChangeRoom");
};
```

### onChangeCustomPlayerStatus 接口

**描述**

修改玩家自定义状态广播回调接口。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|args|ActionArgs&lt;IChangeCustomPlayerStatusBst&gt;|回调参数|

IChangeCustomPlayerStatusBst 定义如下：

|字段名|类型|描述|
|:---|---|---|
|changePlayerId|string|玩家 ID|
|customPlayerStatus|number|玩家状态|
|roomInfo|IRoomInfo|房间信息|

**返回值说明**

无。

**使用示例**

```
const gameServer = {};
gameServer.onChangeCustomPlayerStatus = args => {
    args.SDK.logger.debug("onChangeCustomPlayerStatus");
};
```

### onChangePlayerNetworkState 接口

**描述**

玩家网络状态变化广播回调接口。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|args|ActionArgs&lt;IChangePlayerNetworkStateBst&gt;|回调参数|

IChangePlayerNetworkStateBst 定义如下：

|字段名|类型|描述|
|:---|---|---|
|changePlayerId|string|玩家 ID|
|networkState|NetworkState|网络状态，有四种情况，参考 [枚举类型](https://cloud.tencent.com/document/product/1038/33333) 一节|
|roomInfo|IRoomInfo|房间信息|

**返回值说明**

无。

**使用示例**

```
const gameServer = {};
gameServer.onChangePlayerNetworkState = args => {
    args.SDK.logger.debug("onChangePlayerNetworkState");
};
```

### onDestroyRoom 接口

**描述**

销毁房间广播回调接口。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|args|ActionArgs&lt;IDestroyRoomBst&gt;|回调参数|

IDestroyRoomBst 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomInfo|IRoomInfo|房间信息|

**返回值说明**

无。

**使用示例**

```
const gameServer = {};
gameServer.onDestroyRoom = args => {
    args.SDK.logger.debug("onDestroyRoom");
};
```

### onStartFrameSync 接口

**描述**

开始帧同步广播回调接口。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|args|ActionArgs&lt;IStartFrameSyncBst&gt;|回调参数|

IStartFrameSyncBst 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomInfo|MGOBE.types.RoomInfo|房间信息|

**返回值说明**
无。

**使用示例**

```
const gameServer = {};
gameServer.onStartFrameSync = args => {
    args.SDK.logger.debug("onStartFrameSync");
};
```

### onStopFrameSync 接口

**描述**

停止帧同步广播回调接口。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|args|ActionArgs&lt;IStopFrameSyncBst&gt;|回调参数|

IStopFrameSyncBst 定义如下：

|字段名|类型|描述|
|:---|---|---|
|roomInfo|MGOBE.types.RoomInfo|房间信息|

**返回值说明**
无。

**使用示例**

```
const gameServer = {};
gameServer.onStopFrameSync = args => {
    args.SDK.logger.debug("onStopFrameSync");
};
```

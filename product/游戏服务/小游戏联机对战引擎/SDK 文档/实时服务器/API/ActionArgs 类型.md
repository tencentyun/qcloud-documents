>!由于产品逻辑已无法满足当前游戏技术发展，游戏联机对战引擎 MGOBE 将于2022年7月1日下线，请您在2022年6月30日前完成服务迁移。

ActionArgs 是一个模板类型，其 TypeScript 定义如下：
```
export interface ActionArgs<T> {
    sender: string;
    actionData: T;
    gameData: GameData;
    room: IRoomInfo;
    exports: { data: GameData; };
    SDK: {
        sendData: (data: { playerIdList: string[]; data: UserDefinedData; }, resendConf?: { timeout: number; maxTry: number; }) => void;
        dispatchAction: (actionData: UserDefinedData) => void;
        clearAction: () => void;
        exitAction: () => void;

        getRoomByRoomId: (getRoomByRoomIdPara: IGetRoomByRoomIdPara, callback?: ReqCallback<IGetRoomByRoomIdRsp>) => void;
        changeRoom: (changeRoomPara: IChangeRoomPara, callback?: ReqCallback<IChangeRoomRsp>) => void;
        changeCustomPlayerStatus: (changeCustomPlayerStatusPara: IChangeCustomPlayerStatusPara, callback?: ReqCallback<IChangeCustomPlayerStatusRsp>) => void;
        removePlayer: (removePlayerPara: IRemovePlayerPara, callback?: ReqCallback<IRemovePlayerRsp>) => void;

        logger: {
            debug: (...args: any[]) => void;
            info: (...args: any[]) => void;
            error: (...args: any[]) => void;
        };
    };
}
```

因此，模板类型指定了 actionData 的类型。例如，在 gameServer.onRecvFromClient 接口中，入参是 ActionArgs&lt;UserDefinedData&gt; 类型，表明 actionData 类型为 UserDefinedData。

### sender 属性

**描述**
该属性在 gameServer.onRecvFromClient 中有效，其类型为 string，表示消息发送者的玩家 ID。


### actionData 属性
**描述**
该属性在 gameServer 不同回调中的类型不同，表示该回调的响应数据。例如，在 gameServer.onRecvFromClient 中表示玩家发送给实时服务器的数据；在 onJoinRoom 表示加房广播数据；在 onLeaveRoom 中表示玩家退房广播数据。

### gameData 属性

**描述**
该属性类型为 GameData，表示游戏数据，您可以用来实现游戏状态同步等功能。在第一次执行 gameServer.onCreateRoom 时会被初始化，在执行 gameServer.onDestroyRoom 时会被销毁。

### room 属性

**描述**
该属性类型为 [IRoomInfo](https://cloud.tencent.com/document/product/1038/34991#oninitgamedata-.E6.8E.A5.E5.8F.A3)，表示当前房间信息。

### exports 属性

**描述**
该属性类型为 object，包含了一个类型为 GameData 的子属性 data，用于更新游戏数据 gameData。

如果您需要重新给 gameData 赋值，可以参考以下代码：

```
const newData = {};
exports.data = newData;
// ...
// 执行完回调函数之后，gameData 指向 newData
```

### SDK 属性

**描述**
该属性类型为 object，包含了一系列实时服务器提供的方法。

#### SDK.sendData 方法

**描述**
实时服务器向客户端推送消息。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|data|{ playerIdList: string[]; data: UserDefinedData; }|消息内容|



<dx-alert infotype="explain" title="">
- data.playerIdList 表示接收消息的玩家 ID 列表。数组为空表示发给房间内全部玩家。
- data.data 为具体消息，类型为 UserDefinedData，即 object。
</dx-alert>




**返回值说明**

无。

**使用示例**

```
// 例子1：发给房间列表中第一个玩家
const id = room.playerList[0].id;
let data1 =  { playerIdList: [id], data: { msg: "hello" } };
SDK.sendData(data1);

// 例子2：发给房间全部玩家
let data2 =  { playerIdList: [], data: { msg: "hello" } };
SDK.sendData(data2);
```

#### SDK.dispatchAction 方法

**描述**

模拟客户端给实时服务器发送数据。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|actionData|UserDefinedData|消息内容|

**返回值说明**

无。



<dx-alert infotype="explain" title="">
使用该方法后，下次 gameServer.onRecvFromClient 接口回调将处理该方法发送的消息。
</dx-alert>



**使用示例**

```
let actionData =  { data: "hello" };
SDK.dispatchAction(actionData);
```

#### SDK.clearAction 方法

**描述**

清空 onRecvFromClient 队列。

**参数说明**

无。

**返回值说明**

无。



<dx-alert infotype="explain" title="">
当 gameServer.mode 为 "sync" 时，gameServer.onRecvFromClient 广播会保存在一个队列里面，在 gameServer.onRecvFromClient 回调函数中通过调用 SDK.exitAction 才能处理下一条 gameServer.onRecvFromClient 广播。SDK.clearAction 作用就是清空 gameServer.onRecvFromClient 队列，可用于游戏结束后实时服务器忽略客户端消息的场景。
</dx-alert>



**使用示例**

```
SDK.clearAction();
```

#### SDK.exitAction 方法

**描述**

结束 gameServer.onRecvFromClient 方法。

**参数说明**

无。

**返回值说明**

无。



<dx-alert infotype="explain" title="">
当 gameServer.mode 为 "sync" 时，需要在 gameServer.onRecvFromClient 回调里面显式调用 SDK.exitAction 方法才能继续处理下一条 gameServer.onRecvFromClient 广播消息。
</dx-alert>



**使用示例**

```
SDK.exitAction();
```

### SDK.logger 属性

**描述**
logger 是 SDK 提供的日志记录能力，可以使用 logger.debug、logger.info、logger.error 三种日志级别进行记录。记录的日志可以在 MGOBE 控制台的实时服务器页面查看。



#### SDK.getRoomByRoomId 方法

**描述**

根据房间 ID 查询房间信息。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|getRoomByRoomIdPara|IGetRoomByRoomIdPara|请求参数|
|callback|[ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)&lt;IGetRoomByRoomIdRsp&gt;|回调函数|

IGetRoomByRoomIdPara 定义如下：

|属性名|类型/值|描述|
|:---|---|---|
|roomId|string|房间 ID|

IGetRoomByRoomIdRsp 定义如下：

|属性名|类型/值|描述|
|:---|---|---|
|roomInfo|[IRoomInfo](https://cloud.tencent.com/document/product/1038/34991#oninitgamedata-.E6.8E.A5.E5.8F.A3)|房间信息|


**返回值说明**

无。



<dx-alert infotype="explain" title="">
调用该接口需要在 mgobexsCode 配置正确的游戏 ID 和后端密钥。
</dx-alert>




**使用示例**

```
const getRoomByRoomIdPara = { roomId: "xxx", };
SDK.getRoomByRoomId(getRoomByRoomIdPara, event => {
    console.log(event.code, event.data);

    if (event.code === 0) {
        // 操作成功
        const roomInfo = event.data.roomInfo;
    }
});
```

#### SDK.changeRoom 方法

**描述**
修改指定房间的房间信息。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|changeRoomPara|IChangeRoomPara|请求参数|
|callback|[ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)&lt;IChangeRoomRsp&gt;|回调函数|

IChangeRoomPara 定义如下：

|属性名|类型/值|描述|是否必填|
|:---|---|---|---|
|roomId|string|房间 ID|是|
|roomName|string|房间名称|否|
|owner|string|房主 ID|否|
|isPrivate|boolean|是否私有|否|
|isForbidJoin|boolean|是否禁止加入房间|否|
|customProperties|string|自定义房间属性|否|

IChangeRoomRsp 定义如下：

|属性名|类型/值|描述|
|:---|---|---|
|roomInfo|[IRoomInfo](https://cloud.tencent.com/document/product/1038/34991#oninitgamedata-.E6.8E.A5.E5.8F.A3)|房间信息|

**返回值说明**

无。



<dx-alert infotype="explain" title="">
调用该接口需要在 mgobexsCode 配置正确的游戏 ID 和后端密钥。
</dx-alert>



**使用示例**

```
const changeRoomPara = { roomId: "xxx", roomName: "xxx" };
SDK.changeRoom(changeRoomPara, event => {
    console.log(event.code, event.data);

    if (event.code === 0) {
        // 操作成功
        const roomInfo = event.data.roomInfo;
    }
});
```

#### SDK.changeCustomPlayerStatus 方法

**描述**
修改指定房间的玩家自定义状态。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|changeCustomPlayerStatusPara|IChangeCustomPlayerStatusPara|请求参数|
|callback|[ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)&lt;IChangeCustomPlayerStatusRsp&gt;|回调函数|

IChangeCustomPlayerStatusPara 定义如下：

|属性名|类型/值|描述|
|:---|---|---|
|roomId|string|房间 ID|
|playerId|string|玩家 ID|
|customPlayerStatus|number|玩家自定义状态|

IChangeCustomPlayerStatusRsp 定义如下：

|属性名|类型/值|描述|
|:---|---|---|
|roomInfo|[IRoomInfo](https://cloud.tencent.com/document/product/1038/34991#oninitgamedata-.E6.8E.A5.E5.8F.A3)|房间信息|

**返回值说明**

无。

<dx-alert infotype="explain" title="">
调用该接口需要在 mgobexsCode 配置正确的游戏 ID 和后端密钥。
</dx-alert>



**使用示例**

```
const changeCustomPlayerStatusPara = { roomId: "xxx", playerId: "xxx", customPlayerStatus: 1 };
SDK.changeCustomPlayerStatus(changeCustomPlayerStatusPara, event => {
    console.log(event.code, event.data);

    if (event.code === 0) {
        // 操作成功
        const roomInfo = event.data.roomInfo;
    }
});
```

#### SDK.removePlayer 方法

**描述**
在指定房间踢除玩家。

**参数说明**

|参数名|类型|描述|
|:---|---|---|
|removePlayerPara|IRemovePlayerPara|请求参数|
|callback|[ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)&lt;IRemovePlayerRsp&gt;|回调函数|

IRemovePlayerPara 定义如下：

|属性名|类型/值|描述|
|:---|---|---|
|roomId|string|房间 ID|
|removePlayerId|string|玩家 ID|

IRemovePlayerRsp 定义如下：

|属性名|类型/值|描述|
|:---|---|---|
|roomInfo|[IRoomInfo](https://cloud.tencent.com/document/product/1038/34991#oninitgamedata-.E6.8E.A5.E5.8F.A3)|房间信息|

**返回值说明**

无。



<dx-alert infotype="explain" title="">
调用该接口需要在 mgobexsCode 配置正确的游戏 ID 和后端密钥。
</dx-alert>



**使用示例**

```
const removePlayerPara = { roomId: "xxx", removePlayerId: "xxx" };
SDK.removePlayer(removePlayerPara, event => {
    console.log(event.code, event.data);

    if (event.code === 0) {
        // 操作成功
        const roomInfo = event.data.roomInfo;
    }
});
```


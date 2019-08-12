

ActionArgs 是一个模板类型，其 TypeScript 定义如下：
```
interface ActionArgs<T> {
    sender: string;
    actionData: T;
    gameData: GameData;
    room: IRoomInfo;
    exports: { data: GameData; };
    SDK: {
        sendData: (data: { playerIdList: string[]; data: UserDefinedData; }) => void;
        dispatchAction: (actionData: UserDefinedData) => void;
        clearAction: () => void;
        exitAction: () => void;
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
该属性类型为 GameData，表示游戏数据，开发者可以用来实现游戏状态同步等功能。在第一次执行 gameServer.onRecvFromClient 时会被初始化，在执行 gameServer.onDestroyRoom 时会被销毁。

### room 属性

**描述**
该属性类型为 IRoomInfo，表示当前房间信息。

### exports 属性

**描述**
该属性类型为 object，包含了一个类型为 GameData 的子属性 data，用于更新游戏数据 gameData。

如果开发者需要重新给 gameData 赋值，可以参考以下代码：

```
exports.data = {};
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

>?
- data.playerIdList 表示接收消息的玩家列表。数组为空表示发给房间内全部玩家。
- data.data 为具体消息，类型为 UserDefinedData，即 object。

**返回值说明**

无。

**使用示例**

```
let data =  { playerIdList: [], data: { msg: "hello" } };
SDK.sendData(data);
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

>?使用该方法后，下次 gameServer.onRecvFromClient 接口回调将处理该方法发送的消息。

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

>?当 gameServer.mode 为 "sync" 时，gameServer.onRecvFromClient 广播会保存在一个队列里面，在 gameServer.onRecvFromClient 回调函数中通过调用 SDK.exitAction 才能处理下一条 gameServer.onRecvFromClient 广播。SDK.clearAction 作用就是清空 gameServer.onRecvFromClient 队列，可用于游戏结束后实时服务器忽略客户端消息的场景。

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

>?当 gameServer.mode 为 "sync" 时，需要在 gameServer.onRecvFromClient 回调里面显式调用 SDK.exitAction 方法才能继续处理下一条 gameServer.onRecvFromClient 广播消息。

**使用示例**

```
SDK.exitAction();
```

### logger 属性

**描述**
logger 是 SDK 提供的日志记录能力，可以使用 logger.debug、logger.info、logger.error 三种日志级别进行记录。记录的日志可以在 MGOBE 控制台的实时服务器页面查看。

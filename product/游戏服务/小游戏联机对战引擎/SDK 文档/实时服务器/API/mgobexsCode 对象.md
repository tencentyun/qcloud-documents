
mgobexsCode 对象是自定义服务的入口，开发者需要在代码中导出该对象。

### gameServer 属性

#### 描述

gameServer 是 mgobexsCode 对象的一个属性，类型为 [GameServer.IGameServer](https://cloud.tencent.com/document/product/1038/34991) 。开发者需要实现一个 [GameServer.IGameServer](https://cloud.tencent.com/document/product/1038/34991) 对象，并赋值给 gameServer。

#### 使用示例

```
const gameServer = {
    // 消息模式
    mode: 'sync',
    // 初始化游戏数据
    onInitGameData: function () {
        return {};
    },
    // 监听客户端数据
    onRecvFromClient: function onRecvFromClient(args) {
        args.SDK.logger.debug("onRecvFromClient");
        // 发送消息给客户端
        args.SDK.sendData({ playerIdList: [], data: { msg: "hello" } });
        args.SDK.exitAction();
    }
};

exports.mgobexsCode = {
    gameServer
};
```

### logLevelSDK 属性

#### 描述

logLevelSDK 是 mgobexsCode 对象的一个属性，类型为字符串，表示实时服务器内部日志的打印级别。只能填写以下值：

|值|含义|
|---|---|
|debug+|打印 debug、info、error|
|info+|打印 info、error|
|error+|打印 error|

#### 使用示例

```
exports.mgobexsCode = {
    logLevelSDK: "debug+",
    gameServer
};
```

### logLevel 属性

#### 描述

logLevel 是 mgobexsCode 对象的一个属性，类型为字符串，表示开发者代码内使用 ActionArgs.SDK.logger 时的日志打印级别。只能填写以下值：

|值|含义|
|---|---|
|debug+|打印 debug、info、error|
|info+|打印 info、error|
|error+|打印 error|

#### 使用示例

```
exports.mgobexsCode = {
    logLevel: "debug+",
    gameServer
};
```



mgobexsCode 对象是实时服务器的入口，您需要在代码中导出该对象。

### gameServer 属性

#### 描述

gameServer 是 mgobexsCode 对象的一个属性，类型为 [GameServer.IGameServer](https://cloud.tencent.com/document/product/1038/34991) 。您需要实现一个 [GameServer.IGameServer](https://cloud.tencent.com/document/product/1038/34991) 对象，并赋值给 gameServer。

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
|error+|打印 error（默认值）|

#### 使用示例

```
exports.mgobexsCode = {
    logLevelSDK: "debug+",
    gameServer
};
```

### logLevel 属性

#### 描述

logLevel 是 mgobexsCode 对象的一个属性，类型为字符串，表示您代码内使用 ActionArgs.SDK.logger 时的日志打印级别。只能填写以下值：

|值|含义|
|---|---|
|debug+|打印 debug、info、error|
|info+|打印 info、error|
|error+|打印 error（默认值）|

#### 使用示例

```
exports.mgobexsCode = {
    logLevel: "debug+",
    gameServer
};
```



### onInitGameServer 属性

#### 描述
onInitGameServer 是 mgobexsCode 对象的一个属性，类型为 function。该函数在实时服务器初始化后会被调用，您可以在该函数内初始化 TCB 实例。

#### 参数说明

|参数名|类型|描述|
|:---|---|---|
|tcb|object|腾讯云云开发模块|

#### 返回值说明
无。

#### 使用示例

```
exports.mgobexsCode = {
    onInitGameServer: (tcb) => {
        // 可以在此初始化 TCB
        const tcbApp = tcb.init({
            secretId: "请填写腾讯云 API 密钥 ID",
            secretKey: "请填写腾讯云 API 密钥 KEY",
            env: "请填写云开发环境 ID",
            serviceUrl: 'http://tcb-admin.tencentyun.com/admin',
            timeout: 5000,
        });
    },
    gameServer
};
```

### gameInfo 属性

#### 描述
gameInfo 是 mgobexsCode 对象的一个属性，类型为 object。您如果需要在实时服务器调用 getRoomByRoomId、changeRoom、changeCustomPlayerStatus、removePlayer 方法需要实现该对象。该对象属性如下：

|属性名|类型|描述|
|:---|---|---|
|gameId|string|游戏 ID，从控制台获取|
|serverKey|string|后端密钥，从控制台获取|

#### 使用示例

```
exports.mgobexsCode = {
	gameInfo: {
		gameId: "请填写游戏 ID，从控制台获取",
		serverKey: "请填写后端密钥，从控制台获取",
	},
    gameServer
};
```



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
    onClientData: function onClientData(args) {
        args.SDK.logger.debug("onClientData");
        // 发送消息给客户端
        args.SDK.sendData({ playerIdList: [], data: { msg: "hello" } });
        args.SDK.exitAction();
    }
};

exports.mgobexsCode = {
    gameServer
};
```

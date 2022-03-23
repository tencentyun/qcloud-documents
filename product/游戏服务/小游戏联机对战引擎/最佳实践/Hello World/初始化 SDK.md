>!由于产品逻辑已无法满足当前游戏技术发展，游戏联机对战引擎 MGOBE 将于2022年7月1日下线，请您在2022年6月30日前完成服务迁移。


## 操作场景
本文档指导您如何初始化 SDK。

## 操作步骤
1. 在 game.js 文件中，将启动页改为 MainView。
2. 完成 SDK 监听器初始化、实例化 Room 对象。玩家 playerId 通过使用 Util.js 中的 mockPlayerId 方法生成。

game.js 最终代码如下所示：

```

// 导入 MGOBE.js
import "./MGOBE.js";
// 获取 Room、Listener 对象
const { Room, Listener, ErrCode, ENUM } = MGOBE;

import * as Util from "./Util.js";
const Global = Util.Global;

// 导入页面
import "./view/MainView.js";
import "./view/RoomView.js";
import "./view/GameView.js";

const gameInfo = {
    // 随机生成 玩家 ID
    openId: Util.mockOpenId(),
    // 替换 为控制台上的“游戏 ID”
    gameId: "xxxxxx",
    // 替换 为控制台上的“游戏 Key”
    secretKey: 'xxxxxxxxxxxxxxxxxxx',
};

const config = {
    // 替换 为控制台上的“域名”
    url: 'xxxxxx.wxlagame.com',
    reconnectMaxTimes: 5,
    reconnectInterval: 1000,
    resendInterval: 1000,
    resendTimeout: 10000,
    isAutoRequestFrame: true,
};

// 初始化 Listener
Listener.init(gameInfo, config, event => {
    if (event.code === ErrCode.EC_OK) {

        console.log("初始化成功");

        // 接收广播
        Listener.add(room);

        // 启动页为 MainView
        new Global.MainView();
    } else {
        console.error("初始化失败", event);
    }
});

// 实例化 Room 对象
const room = new Room();

// 保存常用对象的引用
Global.room = room;
Global.ErrCode = ErrCode;
Global.ENUM = ENUM;
Global.gameInfo = gameInfo;

```



## 操作场景
本文档指导您如何使用小游戏联机对战引擎 SDK。


## 前提条件
请在小游戏联机对战引擎控制台创建小游戏实例并开通联机对战服务，获取保存游戏 gameId 和 secretKey。SDK 需要对这两个参数进行校验。

## 操作步骤

### 1. 设置请求域名

>!出于安全考虑，微信小程序/小游戏会限制请求域名，所有的 HTTPs、WebSocket、上传、下载请求域名都需要在 [微信公众平台](https://mp.weixin.qq.com) 进行配置。因此，在正式接入小游戏联机对战引擎 SDK 前，需要在开发者的微信公众平台配置 socket 合法域名。

1. 登录 [微信公众平台](https://mp.weixin.qq.com)，选择左侧菜单栏【开发】>【开发设置】。
2. 进入小游戏联机对战引擎控制台，将控制台获取的游戏域名信息复制保存。
3. 进入开发设置详情页，在服务器域名中添加一条“socket 合法域名”记录。

![控制台游戏信息](https://main.qcloudimg.com/raw/d9148b71fbc9d377d440e645fa7e2a1e.png)
![微信公共平台](https://main.qcloudimg.com/raw/40e50b0457f1928efe98e2665d396c32.png)




### 2. 导入 SDK

SDK 文件包含 MGOBE.js 和 MGOBE.d.ts，即源代码文件和定义文件。在 MGOBE.js 中，SDK 接口被全局注入到 window 或 global 对象下。因此，只需要在使用 SDK 接口之前执行 MGOBE.js 文件即可。

#### 2.1 微信小游戏原生环境
在微信原生环境中，只需要将 MGOBE.js 放到项目下任意位置，在  game.js 中 import SDK 文件后即可使用 MGOBE 的方法。
```
// 只需要在使用 MGOBE 之前 import 一次该文件
import "./js/libs/MGOBE.js";
// 直接使用 MGOBE
const { Room, Listener, ErrCode, ENUM, DebuggerLog } = MGOBE;
```

![微信原生环境](https://main.qcloudimg.com/raw/db99a5a7a6103aec2219fc8df5c7c202.png)

也可以使用 import/from、require 语法显式导入 MGOBE 模块：
```
// 使用 import/from
import * as MGOBE from "./js/libs/MGOBE.js";
const { Room, Listener, ErrCode, ENUM, DebuggerLog } = MGOBE;

// 或者
import { Room, Listener, ErrCode, ENUM, DebuggerLog } from "./js/libs/MGOBE.js";
```
```
// 使用 require
const MGOBE = require("./js/libs/MGOBE.js");
const { Room, Listener, ErrCode, ENUM, DebuggerLog } = MGOBE;

// 或者
const { Room, Listener, ErrCode, ENUM, DebuggerLog } = require("./js/libs/MGOBE.js");
```

#### 2.2 TypeScript 环境

在 Laya、Cocos 等支持直接使用 TypeScript 进行开发的集成环境中，可以使用 TypeScript 自带的 import 语法导入 SDK。由于 TypeScript 支持 .d.ts 定义文件，为了方便开发，可以将 MGOBE.js 和 MGOBE.d.ts 一同复制到项目中，然后调用 import 语句即可。下面以 Cocos Creator 和 LayaAir IDE 为例：

**Cocos Creator：**
```
import { gameInfo, config } from "./Global";

const {ccclass, property} = cc._decorator;

// 使用 MGOBE 接口前导入 SDK
import "./MGOBE/MGOBE.js";

const Listener = MGOBE.Listener;
const Room = MGOBE.Room;

@ccclass
export default class Helloworld extends cc.Component {


    start () {
		// 直接使用 MGOBE 接口
		// TypeScript 下可以显示提示功能
		Listener.init(gameInfo, config);
    }
}
```
![Cocos Creator](https://main.qcloudimg.com/raw/5665b37c207102eede0a58140c66d8ec.png)

**LayaAir IDE：**
```
// 只需要在使用 MGOBE 之前 import 一次该文件
import "../libs/js/MGOBE";
// 直接使用 MGOBE
const { Room, Listener, ErrCode, ENUM, DebuggerLog } = MGOBE;
```
![LayaAir IDE](https://main.qcloudimg.com/raw/d789bacefb48b0a2b0a37ebdd644e260.png)

此外，在 LayaAir IDE 中，也可以直接在 bin/index.js 中直接使用 loadLib 函数导入 MGOBE.js，让 SDK 文件先执行一遍即可。

在 TypeScript 环境中，也可以使用 import/from 语法导入 MGOBE.js，但由于 TS 导入 .d.ts 的优先级高于导入 .js，所以需要把 MGOBE.js 和 MGOBE.d.ts 文件放在不同文件夹，然后使用 import/from 导入 .js 文件，这种导入将无法使用 .d.ts 提示：
```
// import/from 导入 .js，无法使用 .d.ts 提示
import * as MGOBE from "../libs/js/MGOBE";
const { Room, Listener, ErrCode, ENUM, DebuggerLog } = MGOBE;
```

### 3. 初始化监听器 Listener

在使用 MGOBE API 接口时，主要用到 Listener 对象和 Room 对象。导入 SDK 后，需要先初始化 Listener 对象。
```
const gameInfo = {
	version: 'v1.0',
	gameId: 1234567890,// 替换为控制台上的“游戏ID”
	openId: 'xxxxxx',
	wxAppid: 'xxxxxx',
	secretKey: 'xxxxxx',// 替换为控制台上的“密钥”
};

const config = {
	url: 'xxxxxxx.com',// 替换为控制台上的“域名”
	reconnectMaxTimes: 5,
	reconnectInterval: 1000,
	resendInterval: 1000,
	resendTimeout: 10000,
};

Listener.init(gameInfo, config);
```

调用 Listener.init 时，需要传入游戏信息 gameInfo 和游戏配置 config 两个参数。
- gameInfo.gameId、gameInfo.secretKey 和 config.url 都需要根据控制台上的信息传入。
- gameInfo.openId 为玩家唯一 ID，比如微信小游戏平台上的 OpenID。
- 其它字段由开发者自定义。

每个字段的具体含义可以参考 [Listener 对象](https://cloud.tencent.com/document/product/1038/33323)。

### 4. 实例化 Room 对象

在开发游戏过程中的大部分业务接口都位于 Room 对象中。由于每个玩家只能加入一个房间，在游戏生命周期中可以实例化一个 Room 对象进行接口调用：

```
const room = new Room();
```

实例化 Room 后，可以调用 getRoomDetail 接口来检查玩家是否已经加房，适用于应用重启后需要恢复玩家状态的场景。

```
// 查询玩家自己的房间
room.getRoomDetail(event => {
	if (event.code !== 0) {
		return;
	}
	if (event.data.userLocate === 0) {
		console.log("玩家不在房间内");
	} else {
		// 玩家已在房间内
		console.log("房间名", event.data.roomInfo.roomName);
	}
});
```

后续的创建房间、加房、匹配等接口调用直接利用 room 实例即可。
>!getRoomList 接口是 Room 对象的静态方法，需要使用 Room.getRoomList 进行调用。Room 的实例无法直接访问 getRoomList。（ getRoomList 本质上属于构造器的属性 ）。

### 5. Room 接收广播

一个房间对象会有很多广播事件与其相关，比如该房间有新成员加入、房间属性变化、房间开始对战等广播。Room 实例需要在 Listener 中注册广播监听，并且实现广播的回调函数。

#### 注册广播监听

```
const room = new Room();
// 监听
Listener.add(room);
```

#### 设置广播回调函数

```
// 广播：房间有新玩家加入
room.joinRoomBroadcast = event => console.log("新玩家加入", event.joinOpenId);
// 广播：房间有玩家退出
room.leaveRoomBroadcast = event => console.log("玩家退出", event.leaveOpenId);
// 广播：房间被解散
room.dismissRoomBroadcast = event => console.log("房间被解散");
// 其他广播
// ...
```

其他广播接口可以参考 [Room 对象](https://cloud.tencent.com/document/product/1038/33325)。

#### 移除监听
如果不想再接收该 Room 实例的广播，可以从 Listener 中移除：
```
// 移除监听
Listener.remove(room);
```

### 6. 游戏对战

如果玩家已经加入房间，可以通过帧同步功能进行游戏对战。游戏过程中用到的接口有发送帧消息、帧广播，开发者可以利用这两个接口进行帧同步。帧广播的开始、结束需要使用房间的 startFrameSync、stopFrameSync 接口。


#### 开始帧同步
使用 room.startFrameSync 接口可以开启帧广播。房间内任意一个玩家成功调用该接口将导致全部玩家开始接收帧广播。

```
// 发起请求
room.startFrameSync({}, event => {
	if (event.code === ErrCode.EC_OK) {
		console.log("请求成功");
	}
});
// 广播：开始帧同步
room.startGameBroadcast = event => console.log("开始帧同步");
```

#### 发送帧消息
玩家收到帧同步开始广播后可以发送帧消息，后台会将每个玩家的帧消息组合后广播给每个玩家。

```
const frame = {x: 100, y: 100, dir: 30, id: "xxxxxxxx"};
room.sendFrame(frame, event => {
	if (event.code === ErrCode.EC_OK) {
		console.log("发送成功");
	}
});
```

#### 接收帧广播
开发者可设置 room.frameBroadcast 广播回调函数获得帧广播数据。

```
// 广播：收到帧消息
room.frameBroadcast = event => {
	console.log("帧广播", event.data);
};
```

#### 停止帧同步
使用 room.stopFrameSync 接口可以停止帧广播。房间内任意一个玩家成功调用该接口将导致全部玩家停止接收帧广播。

```
// 发起请求
room.stopFrameSync({}, event => {
	if (event.code === ErrCode.EC_OK) {
		console.log("请求成功");
	}
});
// 广播：停止帧同步
room.stopGameBroadcast = event => console.log("停止帧同步");
```

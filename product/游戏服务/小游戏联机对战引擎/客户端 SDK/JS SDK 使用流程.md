>!由于产品逻辑已无法满足当前游戏技术发展，游戏联机对战引擎 MGOBE 将于2022年7月1日下线，请您在2022年6月30日前完成服务迁移。


## 操作场景

本文档指导您如何使用游戏联机对战引擎 JS SDK。

## 前提条件
- 已在游戏联机对战引擎控制台创建游戏，并开通联机对战服务，详情可参见 [开通服务](https://cloud.tencent.com/document/product/1038/33299)。
- 已获取游戏 gameID 和 secretKey，您可在游戏概览的基本信息里查看。JS SDK 需要对这两个参数进行校验。

## 操作步骤

### 设置 request 和 socket 域名


<dx-alert infotype="notice" title="">
出于安全考虑，微信小程序/小游戏会限制请求域名，所有的 HTTPS、WebSocket、上传、下载请求域名都需要在 [微信公众平台](https://mp.weixin.qq.com) 进行配置。因此，在正式接入游戏联机对战引擎 JS SDK 前，需要您在微信公众平台配置合法域名。
</dx-alert>



1. 需要配置的域名包含一条 request 域名和两条 socket 域名记录。您在游戏联机对战引擎控制台上获取域名后，需要配置该域名的默认端口、 5443 端口两条记录。
```
// request 域名
report.wxlagame.com
// socket 域名
xxx.wxlagame.com
xxx.wxlagame.com:5443
```	
2. 进入 [游戏联机对战引擎控制台](https://console.cloud.tencent.com/minigamecloud)，将控制台获取的游戏域名信息复制保存。
3. 登录 [微信公众平台](https://mp.weixin.qq.com)，选择左侧菜单栏**开发**>**开发设置**。
4. 进入开发设置详情页，在 “服务器域名” 中添加合法域名记录。如下图所示：
![微信公共平台](https://main.qcloudimg.com/raw/e17421702e5e79ade528a074b047b184.png)

### 导入 JS SDK
JS SDK 文件包含 MGOBE.js 和 MGOBE.d.ts，即源代码文件和定义文件。在 MGOBE.js 中，JS SDK 接口被全局注入到 Window 对象下。因此，只需要在使用 JS SDK 接口之前执行 MGOBE.js 文件即可。单击进入 JS [SDK 下载](https://cloud.tencent.com/document/product/1038/33406) 页面。

#### 微信小游戏原生环境

在微信原生环境中，您只需将 MGOBE.js 放到项目下任意位置，在 game.js 中 import JS SDK 文件后即可使用 MGOBE 的方法。导入示例代码如下：

```
// 只需要在使用 MGOBE 之前 import 一次该文件
import "./js/libs/MGOBE.js";
// 直接使用 MGOBE
const { Room, Listener, ErrCode, ENUM, DebuggerLog } = MGOBE;
```

界面示例如下图所示：
![微信原生环境](https://main.qcloudimg.com/raw/db99a5a7a6103aec2219fc8df5c7c202.png)

您也可以使用 import/from、require 语法显式导入 MGOBE 模块。
import/from 代码示例如下：

```
// 使用 import/from
import * as MGOBE from "./js/libs/MGOBE.js";
const { Room, Listener, ErrCode, ENUM, DebuggerLog } = MGOBE;

// 或者
import { Room, Listener, ErrCode, ENUM, DebuggerLog } from "./js/libs/MGOBE.js";
```

require 代码示例如下：

```
// 使用 require
const MGOBE = require("./js/libs/MGOBE.js");
const { Room, Listener, ErrCode, ENUM, DebuggerLog } = MGOBE;

// 或者
const { Room, Listener, ErrCode, ENUM, DebuggerLog } = require("./js/libs/MGOBE.js");
```

#### TypeScript 环境

在 Laya、Cocos 等支持直接使用 TypeScript 进行开发的集成环境中，您可以使用 TypeScript 自带的 import 语法导入 JS SDK。由于 TypeScript 支持 .d.ts 定义文件，为了方便开发，您可以将 MGOBE.js 和 MGOBE.d.ts 一同复制到项目中，再调用 import 语句即可。以 Cocos Creator 和 LayaAir IDE 为例：

**Cocos Creator：**

```
import { gameInfo, config } from "./Global";

const {ccclass, property} = cc._decorator;

// 使用 MGOBE 接口前导入 JS SDK
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

界面示例如下图所示：
![Cocos Creator](https://main.qcloudimg.com/raw/5665b37c207102eede0a58140c66d8ec.png)

**LayaAir IDE：**

```
// 只需要在使用 MGOBE 之前 import 一次该文件
import "../libs/js/MGOBE";
// 直接使用 MGOBE
const { Room, Listener, ErrCode, ENUM, DebuggerLog } = MGOBE;
```

界面示例如下图所示：
![LayaAir IDE](https://main.qcloudimg.com/raw/d789bacefb48b0a2b0a37ebdd644e260.png)

此外，在 LayaAir IDE 中，您也可以直接在 bin/index.js 中直接使用 loadLib 函数导入 MGOBE.js，让 JS SDK 文件先执行一遍即可。
在 TypeScript 环境中，您也可以使用 import/from 语法导入 MGOBE.js，但由于 TS 导入 .d.ts 的优先级高于导入 .js，所以您需要将 MGOBE.js 和 MGOBE.d.ts 文件放在不同文件夹，并使用 import/from 导入 .js 文件。


<dx-alert infotype="notice" title="">
使用 import/from 语法方式导入 .js 将无法使用 .d.ts 提示。
</dx-alert>



```

// import/from 导入 .js，无法使用 .d.ts 提示
import * as MGOBE from "../libs/js/MGOBE";
const { Room, Listener, ErrCode, ENUM, DebuggerLog } = MGOBE;

```


### Egret 环境
1. 使用 Egret Wing 打开项目，在 libs 文件夹下，创建 MGOBE 文件夹，将 MGOBE.js、MGOBE.d.ts 拷贝到 MGOBE  文件夹。
2. 编辑 egretProperties.json 文件，在 modules 数组中新增 MGOBE 库的描述。
```
	{
		"name": "MGOBE",
		"path": "./libs/MGOBE"
	}
```
3. 运行编译引擎，完成 MGOBE SDK 的导入工作。在项目代码中可以直接使用 MGOBE 对象。
![Egret IDE](https://main.qcloudimg.com/raw/edaeb32d9b259ee534106a7d67262945.png)




### 初始化监听器 Listener

在使用 MGOBE API 接口时，主要用到 Listener 对象和 Room 对象。导入 JS SDK 后，需要先初始化 Listener 对象。

```
const gameInfo = {
	openId: 'xxxxxx',
	gameId: "xxxxxx",// 替换为控制台上的“游戏 ID”
	secretKey: 'xxxxxx',// 替换为控制台上的“游戏 key”
};

const config = {
	url: 'xxx.wxlagame.com',// 替换为控制台上的“域名”
	reconnectMaxTimes: 5,
	reconnectInterval: 1000,
	resendInterval: 1000,
	resendTimeout: 10000,
};

Listener.init(gameInfo, config, event => {
	if (event.code === 0) {
		// 初始化成功
		// 继续在此添加代码
		// ...
	}
});
```

调用 Listener.init 时，需要传入游戏信息 gameInfo 和游戏配置 config 两个参数。
- gameInfo.gameId、gameInfo.secretKey 和 config.url 都需要根据控制台上的信息传入。
- gameInfo.openId 为玩家唯一 ID，例如，微信小游戏平台上的 OpenID。
- 其它字段由您自定义。

每个字段的具体含义您可参考 [Listener 对象](https://cloud.tencent.com/document/product/1038/33323)。

初始化成功后才能继续调用其他接口。因此，下文的 API 调用代码都应该在初始化回调函数内调用。

### 实例化 Room 对象

在开发游戏过程中的大部分业务接口都位于 Room 对象中。由于每个玩家只能加入一个房间，在游戏生命周期中可以实例化一个 Room 对象进行接口调用：

```
const room = new Room();
```

实例化 Room 后，可以调用 getMyRoom 接口来检查玩家是否已经加房，适用于应用重启后需要恢复玩家状态的场景。

```
// 查询玩家自己的房间
Room.getMyRoom(event => {
        if (event.code === 0) {
                // 设置房间信息到 room 实例
                room.initRoom(event.data.roomInfo);
                return console.log("玩家已在房间内：", event.data.roomInfo.name);
        }
        
        if (event.code === 20011) {
                return console.log("玩家不在房间内");
        }

        return console.log("调用失败");
});
```

后续的创建房间、加房、匹配等接口调用直接利用 room 实例即可。


<dx-alert infotype="notice" title="">
getMyRoom、getRoomList、getRoomByRoomId 接口是 Room 对象的静态方法，您需要使用 Room.getMyRoom、Room.getRoomList、Room.getRoomByRoomId 进行调用。Room 的实例无法直接访问 getMyRoom、getRoomList、getRoomByRoomId。
</dx-alert>



### Room 接收广播

一个房间对象会有很多广播事件与其相关，例如该房间有新成员加入、房间属性变化、房间开始对战等广播。Room 实例需要在 Listener 中注册广播监听，并且实现广播的回调函数。

#### 注册广播监听

```
// 监听
Listener.add(room);
```

#### 设置广播回调函数

```
// 广播：房间有新玩家加入
room.onJoinRoom = event => console.log("新玩家加入", event.data.joinPlayerId);
// 广播：房间有玩家退出
room.onLeaveRoom = event => console.log("玩家退出", event.data.leavePlayerId);
// 广播：房间被解散
room.onDismissRoom = event => console.log("房间被解散");
// 其他广播
// ...
```

其他广播接口您可参考 [Room 对象](https://cloud.tencent.com/document/product/1038/33325)。

#### 移除监听
如果不想再接收该 Room 实例的广播，可以从 Listener 中移除：

```
// 移除监听
Listener.remove(room);
```

### 游戏对战
如果玩家已经加入房间，可以通过帧同步功能进行游戏对战。游戏过程中用到的接口有发送帧消息、帧广播，您可以利用这两个接口进行帧同步。帧广播的开始、结束需要使用房间的 startFrameSync、stopFrameSync 接口。


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
room.onStartFrameSync = event => console.log("开始帧同步");
```

#### 发送帧消息
玩家收到帧同步开始广播后可以发送帧消息，后台会将每个玩家的帧消息组合后广播给每个玩家。

```
const frame = { x: 100, y: 100, dir: 30, id: "xxxxxxxx" };
room.sendFrame({ data: frame }, event => {
	if (event.code === ErrCode.EC_OK) {
		console.log("发送成功");
	}
});
```

#### 接收帧广播
您可设置 room.onRecvFrame 广播回调函数获得帧广播数据。

```
// 广播：收到帧消息
room.onRecvFrame = event => {
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
room.onStopFrameSync = event => console.log("停止帧同步");
```

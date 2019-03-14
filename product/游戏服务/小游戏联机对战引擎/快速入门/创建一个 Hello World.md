## 操作场景
本文档介绍如何使用小游戏联机对战引擎 SDK 在微信小游戏平台实现游戏帧同步服务，涉及到的小游戏联机对战引擎接口有房间匹配、退房、开始帧同步、停止帧同步、帧消息广播等。

## 前提条件
- 已在小游戏联机对战引擎控制台创建小游戏实例，并开通联机对战服务。
- 已获取游戏 gameID 和 secretKey。SDK 需要对这两个参数进行校验。

## 创建一个微信小游戏项目
1. 打开微信开发者工具，创建一个名为 HelloWorld 的小游戏项目。
2. 注意不要选择快速启动模板，直接创建空项目，从零开始完成项目。详细操作请参考 [小游戏开发文档](https://developers.weixin.qq.com/minigame/dev/index.html) 
![创建一个微信小游戏项目](https://main.qcloudimg.com/raw/f67503ffbcd3e0099ccf043bf9b97aa0.png)
3. 进入编辑界面后，在根目录创建 game.js 和 game.json 文件，并在 game.json 中添加如下代码：
```
{
  "deviceOrientation": "portrait"
}
```

![game.json 文件](https://main.qcloudimg.com/raw/c0046c611acf7eaf939bd6418d56b891.png)

 >!在开发过程中可以先跳过微信的域名检查。微信开发者工具上可以通过右侧【详情】设置，手机预览小程序/小游戏时可以打开调试功能跳过检查。

## 导入 MGOBE SDK
将 MGOBE.js 添加到项目根目录，在 game.js 中添加如下代码，完成导入 MGOBE SDK。
```
// 导入 MGOBE.js
import "./MGOBE.js";
// 获取 Room、Listener 对象
const { Room, Listener, ErrCode, ENUM } = MGOBE;
```

## 准备工作：工具类方法

在根目录创建一个 Util.js 文件，在里面添加以下工具类方法。

- 设置一个对象，用以保存一些常用属性和方法。
```
// 模拟全局对象
export const Global = {};
```

- 生成 openId，在实际项目中需要使用微信平台的接口获取 openId。
```
// 生成测试 openId
export const mockOpenId = () => `mock_openId_${Math.ceil(Math.random() * 100)}_${(new Date()).getMilliseconds()}`;
```

- 生成 userName，在实际项目中需要使用微信平台的接口获取玩家昵称。
```
// 生成测试 userName
export const mockName = () => `user_${Math.ceil(Math.random() * 100)}`;
```

- 获得 canvas 对象上下文，以及画布宽度、高度信息。
```
// 获得 canvas 上下文
export const canvas = wx.createCanvas();
export const ctx = canvas.getContext('2d');
export const width = canvas.width;
export const height = canvas.height;
```

- 最后还需要准备基本的点击事件管理方法，使用一个数组 clickHandlers 保存全部点击区域和点击回调，当监听到点击事件发生时，遍历该数组并执行点击回调。
```
	// 点击事件回调函数数组
	// Handler 结构： [id, [x1, y1, x2, y2], callback]
	let clickHandlers = [];

	// 开启点击事件监听
	wx.onTouchStart(function (e) {
		const {
			clientX,
			clientY
		} = e.touches[0];

		clickHandlers.forEach((handler) => {

			const x1 = handler[1][0];
			const y1 = handler[1][1];
			const x2 = handler[1][2];
			const y2 = handler[1][3];

			if (clientX > x1 && clientX < x2 && clientY > y1 && clientY < y2) {
				handler[2] && handler[2]();
			}
		});
	});

	// 添加监听
	export const onClick = (id, area, callback) => clickHandlers.push([id, area, callback]);

	// 移除监听
	export const offClick = (id) => clickHandlers = clickHandlers.filter(handler => handler[0] !== id);
```


## 准备工作：组件与页面
使用微信开发者工具直接开发原生小游戏，需要开发者自己实现组件与页面的管理。
在根目录新建两个文件夹，分别命名为 component 和 view，并在 component 中创建一个 BaseComponent.js 文件，在 view 中创建一个 BaseView.js 文件。示例代码如下所示：
![页面与组件文件夹](https://main.qcloudimg.com/raw/e30143528aa08e0497509ebc1cedafb3.png)

### 组件
组件是指页面上的按钮、文本框、输入框、下拉框等，每个组件需要维护组件 ID、点击事件、渲染、销毁等功能。
本项目将实现按钮 Button 和文本框 MsgBox 组件，BaseComponent.js 将作为这两个组件的基类。
在 BaseComponent.js 中添加以下代码：
```
// 组件基类
import * as Util from "../Util.js";

export default class BaseComponent {

  id;
  // 组件区域
  area = [0, 0, 0, 0];

  constructor() {
    // 为组件生成 ID
    this.id = Math.ceil(Math.random() * 10000) + "_" + Date.now();
  }

  // 子类实现具体绘制方法
  render() { }

  // 记录组件区域
  setArea(x, y, w, h) {
    this.area[0] = x;
    this.area[1] = y;
    this.area[2] = x + w;
    this.area[3] = y + h;
  }

  // 注册点击事件
  onClick(callback) {
    this.offClick();
    Util.onClick(this.id, this.area, callback);
  }

  // 取消点击事件
  offClick() {
    Util.offClick(this.id);
  }

  // 销毁
  onDestroy() {
    this.offClick();
  }
}
```

#### 实现按钮 Button
在 component 文件夹下新建一个 Button.js 文件，实现一个基于 BaseComponent 的 Button 类。Button 类包含 render、setText 两个方法。
示例代码如下所示：
```
import * as Util from "../Util.js";
import BaseComponent from "./BaseComponent.js";

export default class Button extends BaseComponent {
  x;
  y;
  text;

  constructor(x, y, text) {
    super();

    this.x = x;
    this.y = y;
    this.text = text;
  }

  // 绘制
  render() {
    // 清除原图像
    Util.ctx.lineWidth = 2;
    Util.ctx.fillStyle = "white";

    const x1 = this.area[0] - Util.ctx.lineWidth / 2;
    const y1 = this.area[1] - Util.ctx.lineWidth / 2;
    const x2 = this.area[2] + this.area[0] + Util.ctx.lineWidth / 2;
    const y2 = this.area[3] + this.area[1] + Util.ctx.lineWidth / 2;
    Util.ctx.fillRect(x1, y1, x2, y2);

    // 绘制图形
    Util.ctx.strokeStyle = "black";
    Util.ctx.fillStyle = "black";
    Util.ctx.font = "20px Arial";

    const padding = 5;
    const width = Util.ctx.measureText(this.text).width + padding * 2;
    const height = 20 + padding * 2;

    Util.ctx.strokeRect(this.x, this.y, width, height);
    Util.ctx.fillText(this.text, this.x + padding, this.y + height - padding - 3);

    // 记录按钮区域
    this.setArea(this.x, this.y, width, height);
  }

  // 设置文本内容
  setText(text) {
    this.text = text;
    this.render();
  }
}
```

#### 实现文本框 MsgBox
在 component 文件夹下新建一个 MsgBox.js 文件，实现一个基于 BaseComponent 的 MsgBox 类。MsgBox 类包含 render、setText 两个方法。
示例代码如下所示：
```
import * as Util from "../Util.js";
import BaseComponent from "./BaseComponent.js";

export default class MsgBox extends BaseComponent {
  x;
  y;
  text;

  constructor(x, y, text) {
    super();

    this.x = x;
    this.y = y;
    this.text = text;
  }

  // 绘制
  render() {
    const width = Util.width - 2 * this.x;
    const height = 300;
    const padding = 5;

    // 清除原图形
    Util.ctx.strokeStyle = "black";
    Util.ctx.fillStyle = "white";

    Util.ctx.fillRect(this.x, this.y, width, height);
    Util.ctx.strokeRect(this.x, this.y, width, height);

    // 绘制图形
    Util.ctx.strokeStyle = "black";
    Util.ctx.fillStyle = "black";
    Util.ctx.font = "15px Arial";

    const texts = this.text.split("\n");

    texts.forEach((t, i) => Util.ctx.fillText(t, this.x + padding, this.y + padding + (i + 1) * (15 + padding), width - padding * 2));

    // 记录文本框区域
    this.setArea(this.x, this.y, width, height);
  }

  // 设置文本内容
  setText(text) {
    this.text = text;
    this.render();
  }
}
```

最后，在 component 文件夹内创建一个 index.js 文件，导出 Button.js、MsgBox.js 两个文件。
```
import Button from "./Button.js";
import MsgBox from "./MsgBox.js";

export default {
  Button,
  MsgBox
};
```

![组件](https://main.qcloudimg.com/raw/145fc924e232a3ae43b50f9644b3d8bc.png)

### 页面

一般帧同步游戏都包含至少三个页面：主页、房间、游戏页。
本项目中也将对应实现三个页面：MainView、RoomView、GameView，而 view 文件夹下的 BaseView.js 将作为页面基类。一个页面从进入到切换离开一般包含初始化、更新、销毁这三阶段生命周期。因此，BaseView.js 中需要管理这三个生命周期的切换。此外，页面作为游戏表现层，也需要使用一个定时器驱动画面更新，这里介绍使用 requestAnimationFrame 方法。
示例代码如下所示：
```
// 页面基类
import * as Util from "../Util.js";
const Global = Util.Global;

export default class BaseView {

  // 页面内组件数组，如 Button、MsgBox
  components = [];

  constructor() {
    // 使用每个页面自己的 onUpdate 函数进行渲染
    AnimateUtil.callback = this.onUpdate.bind(this);

    // 初始化页面背景
    Util.ctx.fillStyle = 'white';
    Util.ctx.fillRect(0, 0, Util.width, Util.height);

    wx.hideLoading();
    this.onInit();
  }

  // 页面的生命周期
  // onInit: 进入页面前调用
  // onUpdate: 渲染层页面更新时调用
  // onDestroy: 离开页面后调用
  // 子类可以实现这三个方法
  onInit() { }
  onUpdate() { }
  onDestroy() { }

  // 跳转到其他页面
  open(ViewClass) {
    this.onDestroy();

    // 清除页面组件
    this.components.forEach(component => component.onDestroy());
    this.components = [];

    // 跳转
    setTimeout(() => new ViewClass());
  }

  // 添加组件
  addComponent(component) {
    this.components.push(component);
    component.render();
  }

  // 显示 toast
  toast(title) {
    wx.showToast({
      title,
      icon: 'none',
    });
  }

  // 显示 loading
  loading(title) {
    wx.showLoading({
      title,
    });
  }

  // 显示 Dialog
  dialog(content, confirm) {
    wx.showModal({
      title: '提示',
      content,
      success(res) {
        if (res.confirm) {
          confirm && confirm();
        }
      }
    })
  }
}

// 页面定时渲染
const AnimateUtil = {
  callback: () => { },
  run: () => {
    AnimateUtil.callback && AnimateUtil.callback();
    requestAnimationFrame(AnimateUtil.run);
  }
}

AnimateUtil.run();
```

### MainView 主页

在 view 文件夹下创建 MainView.js 文件，通过继承 BaseView 实现一个包含有一个按钮和文本框的页面。示例代码如下所示：
```
// 游戏主页
import * as Util from "../Util.js";
import BaseView from "./BaseView.js";
import Component from "../component/index.js";
const Global = Util.Global;

export default class MainView extends BaseView {
  constructor() {
    super();
  }

  onInit() {
    const button = new Component.Button(20, 20, "快速加房");
    const msgBox = new Component.MsgBox(20, 100, "");

    this.addComponent(button);
    this.addComponent(msgBox);
  }

  onUpdate() { }

  onDestroy() { }
}

Global.MainView = MainView;
```

然后在根目录的 game.js 中导入 Util.js 和 MainView.js，并实例化 MainView。编译后即可在左侧模拟器中看到效果。
```
// 导入 MGOBE.js
import "./MGOBE.js";
// 获取 Room、Listener 对象
const { Room, Listener, ErrCode, ENUM } = MGOBE;

import * as Util from "./Util.js";
const Global = Util.Global;

// 导入页面
import "./view/MainView.js";

// 启动页为 MainView
new Global.MainView();
```

![主页](https://main.qcloudimg.com/raw/0c72b95cedea39bf67d5992714c0ee7a.png)

### RoomView 房间页

在 view 文件夹下创建 RoomView.js 文件，实现一个包含有两个按钮和一个文本框的页面。示例代码如下所示：
```
// 房间页
import * as Util from "../Util.js";
import BaseView from "./BaseView.js";
import Component from "../component/index.js";
const Global = Util.Global;

export default class RoomView extends BaseView {

  button;
  msgBox;

  constructor() {
    super();
  }

  timer;

  onInit() {

    const button1 = new Component.Button(20, 20, "准备");
    this.button = button1;

    const button2 = new Component.Button(150, 20, "退出房间");

    const msgBox = new Component.MsgBox(20, 100, "");
    this.msgBox = msgBox;

    this.addComponent(button1);
    this.addComponent(button2);
    this.addComponent(msgBox);
  }

  onUpdate() { }

  onDestroy() { }
}

Global.RoomView = RoomView;
```

然后将 game.js 替换为以下代码，导入 RoomView.js，并将启动页换成 RoomView（也就是实例化 RoomView），编译后就能看到效果。
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

// 启动页为 RoomView
new Global.RoomView();
```

![房间页](https://main.qcloudimg.com/raw/130ad9dec82134842b8ac7212190fa50.png)

### GameView 游戏页

在 view 文件夹下创建 GameView.js 文件，实现一个包含有一个按钮和一个文本框的页面。示例代码如下所示：
```
// 帧同步游戏页面
import * as Util from "../Util.js";
import BaseView from "./BaseView.js";
import Component from "../component/index.js";
const Global = Util.Global;

export default class GameView extends BaseView {

  msgBox;

  constructor() {
    super();
  }

  onInit() {
    const button = new Component.Button(20, 20, "结束帧同步");

    const msgBox = new Component.MsgBox(20, 100, "");
    this.msgBox = msgBox;

    this.addComponent(button);
    this.addComponent(msgBox);
  }

  onUpdate() { }

  onDestroy() { }
}

Global.GameView = GameView;
```

将 game.js 替换为以下代码，导入 GameView.js，并将启动页换成 GameView，编译代码。
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

// 启动页为 GameView
new Global.GameView();
```

![房间页](https://main.qcloudimg.com/raw/1ccf1813ecab46f4f6aefe2e084e50c8.png)


到此，游戏基本页面全部完成，接下来主要完成 SDK 的调用，以及处理页面的更新、跳转逻辑。

## 初始化 SDK

在 game.js 中，将启动页改为 MainView，并完成 SDK 监听器初始化、实例化 Room 对象。玩家的 openId 使用 Util.js 中的 mockOpenId 方法生成。game.js 最终代码如下所示：
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
  version: 'v1.0',
  // 替换 为控制台上的“游戏ID”
  gameId: 91000000,
  // 随机生成 玩家 ID
  openId: Util.mockOpenId(),
  wxAppid: 'wx43c6c5xxxxxxxxx',
  // 替换 为控制台上的“密钥”
  secretKey: 'kJm9RZWL7xxxxxxxxxxxxxxxxxxx',
};

const config = {
  // 替换 为控制台上的“域名”
  url: 'access.wxlagame.com',
  reconnectMaxTimes: 5,
  reconnectInterval: 1000,
  resendInterval: 1000,
  resendTimeout: 10000,
  autoRequestFrame: true,
};

// 初始化 Listener
Listener.init(gameInfo, config);

// 实例化 Room 对象
const room = new Room();

// 接收广播
Listener.add(room);

// 保存常用对象的引用
Global.room = room;
Global.ErrCode = ErrCode;
Global.ENUM = ENUM;
Global.gameInfo = gameInfo;

// 启动页为 MainView
new Global.MainView();
```

## 实现快速加房

快速加房操作在 MainView 完成。交互逻辑是玩家点击【快速加房】后，SDK 发起房间匹配请求，请求成功后玩家将加入房间，此时要跳转到 RoomView。

因此，首先要在 MainView.js 的 onInit 方法中为 button 绑定点击事件：
```
  onInit() {
    const button = new Component.Button(20, 20, "快速加房");
    // 绑定点击事件
    button.onClick(() => this.matchRoom());

    const msgBox = new Component.MsgBox(20, 100, "");

    this.addComponent(button);
    this.addComponent(msgBox);
  }
```

然后为 MainView 类添加 matchRoom 方法：
```
  matchRoom() {

    this.loading('匹配中...');

    const userInfo = {
      userName: Util.mockName(),
    };

    Global.name = userInfo.userName;

    const matchRoomPara = {
      userInfo: userInfo,
      maxUsers: 2,
      roomType: "1",
    };

    // 调用房间匹配接口实现快速加房
    Global.room.matchRoom(matchRoomPara, event => {
      wx.hideLoading();
      if (event.code === Global.ErrCode.EC_OK) {
        // 接口调用成功，跳转到 RoomView
        return this.open(Global.RoomView);
      }

      return this.toast(`匹配失败[${event.code}]`);
    });
  }
```

编译代码后，点击【快速加房】，模拟器页面将跳转到 RoomView。

## 实现修改玩家状态

RoomView 有两个按钮，分别是【准备】、【退出房间】。交互逻辑是点击【准备】将修改玩家自定义状态，当房间内全部玩家都准备好后，可以开始帧同步进行游戏。点击【退出房间】，玩家将发起退房请求，成功后进入 MainView。

首先为【准备】绑定点击事件。在 RoomView.js 的 onInit 中为 button1 添加事件：
```
    const button1 = new Component.Button(20, 20, "准备");
    // 点击后切换状态
    button1.onClick(() => this.changeState(this.customStatus === 1 ? 0 : 1));
    this.button = button1;
```

这里只使用0和1表示玩家“未准备”、“已准备”两种状态。customStatus 为 RoomView 类的属性，用来保存玩家状态。
```
export default class RoomView extends BaseView {

  button;
  msgBox;
  
  customStatus;

  // ...
```

然后为 RoomView 类添加 changeState 方法：
```
  // 修改用户状态
  changeState(customStatus) {
    const changeUserStatePara = { customStatus };

    Global.room.changeUserState(changeUserStatePara, event => {
      if (event.code !== Global.ErrCode.EC_OK) {
        return this.toast(`操作失败[${event.code}]`);
      }

      return this.customStatus = customStatus;
    });
  }
```

## 检查房间属性
MGOBE SDK 中的 Room 对象会管理所有房间变化，任何玩家进行加房、退房、修改玩家状态等会改变房间信息的操作后，Room 对象会自动更新房间信息。
因此，玩家在 RoomView 修改状态后，只需要访问 Room 实例的 roomInfo 属性就能获得最新房间信息，页面也可以同步更新。可以直接使用定时器定时检查房间属性并更新页面。为 RoomView 类添加 checkRoom 方法定时检查房间属性，更新按钮和文本框，并当全部玩家处于【已准备】状态时跳转到 GameView 页面。
```
  checkRoom() {
    clearInterval(this.timer);

    // 定时检查房间状态，并更新页面信息
    // 满足条件就跳转到游戏页面
    this.timer = setInterval(() => {
      // 更新 按钮
      const user = Global.room.roomInfo.userList.find(user => user.openId === Global.gameInfo.openId);

      if (user) {
        this.customStatus = user.customStatus;

        // 更新 按钮 文字
        if (user.customStatus === 0) {
          this.button.setText("准备");
        } else {
          this.button.setText("取消准备");
        }
      }

      // 更新 MsgBox
      let msg = `房间ID:\n${Global.room.roomInfo.roomId}\n玩家列表:\n`;
      Global.room.roomInfo.userList.forEach((user, i) => msg += `${i}: ${user.openId} ${user.customStatus === 1 ? "已准备" : "未准备"}\n`);

      this.msgBox.setText(msg);

      if (!Global.room.roomInfo.userList.find(user => user.customStatus !== 1)) {
        // 全部玩家准备好就跳转
        clearInterval(this.timer);
        setTimeout(() => this.open(Global.GameView), 1500);
      }
    }, 500);
  }
```

这里使用 timer 属性保存计时器，当页面触发 onDestroy 事件时，需要清除定时器。checkRoom 方法可以在页面 onInit 时进行调用。

为 RoomView 类添加 timer 属性：
```
export default class RoomView extends BaseView {

  button;
  msgBox;
  
  customStatus;
  timer;

  // ...
```

在 onInit 追加代码：
```
onInit() {
    // ...

    this.checkRoom();
}
```

在 onDestroy 中清除定时器：
```
onDestroy() {
    // 离开页面时一定要清除定时器
    clearInterval(this.timer);
}
```

编译代码，玩家点击【快速加房】进入 RoomView 后，点击【准备】，按钮和文本框都将更新。如果房间内的玩家都是【已准备】状态，页面将跳转到 GameView。

![房间信息更新](https://main.qcloudimg.com/raw/d0f1ba9073e0f0cfe653db34cf387d5a.png)

## 处理其他玩家加房

当其他玩家进入房间时，SDK 会触发 joinRoomBroadcast 回调，因此可以在进入页面时为房间绑定 joinRoomBroadcast 广播回调函数。修改 RoomView.js 中的 onInit 方法。示例代码如下所示：
```
onInit() {
    // ...

    // 设置广播回调
    Global.room.joinRoomBroadcast = this.joinRoomBroadcast.bind(this);
}
```

然后添加 joinRoomBroadcast 方法，这里做一个 toast 提醒玩家即可。示例代码如下所示：
```
  // 加房广播
  joinRoomBroadcast(event) {
    this.toast("新玩家加入");
  }
```

需要注意的是，这里为 Global.room.joinRoomBroadcast 指定了一个回调函数，当页面跳转到其他页面时，这个回调函数引用还在。如果该函数依赖于页面脚本的上下文，有可能在触发广播时报错。因此好的习惯是在离开页面时置空 Global.room.joinRoomBroadcast。示例代码如下所示：
```
  onDestroy() {
    // 离开页面时一定要清除定时器
    clearInterval(this.timer);
    Global.room.joinRoomBroadcast = null;
  }
```

现在使用两个设备进行“快速加房”操作（如模拟器+手机预览），两个玩家有可能匹配在一起，这时页面上将弹出“新玩家加入”提示。

>!手机预览时打开调试，跳过域名检查。

模拟器界面效果图如下所示：
![模拟器界面效果](https://main.qcloudimg.com/raw/7ded0db58ca31868715ecc72897013e5.png)

手机预览效果图如下所示：
![手机预览效果](https://main.qcloudimg.com/raw/722cd1ac005a3ee9c4d8fc2e7e487d17.png)

## 实现退房功能

在 RoomView 中为 button2 绑定点击事件。示例代码如下所示：
```
  onInit() {

    // ...

    const button2 = new Component.Button(150, 20, "退出房间");
    button2.onClick(() => this.leaveRoom());

    // ...
  }
```

然后在 RoomView 类中实现 leaveRoom 方法。示例代码如下所示：
```
  // 退出房间
  leaveRoom() {
    Global.room.leaveRoom({}, event => {
      if (event.code !== Global.ErrCode.EC_OK && event.code !== Global.ErrCode.EC_ROOM_USER_NOT_IN_ROOM) {
        return this.toast(`操作失败[${event.code}]`);
      }
      return this.open(Global.MainView);
    });
  }
```

编译代码后，在模拟器中进行加房操作进入 RoomView 后，点击【退出房间】，即可跳转到 MainView。

## 实现开始帧同步

在 RoomView 中，全部玩家点击【准备】后，页面自动跳转到 GameView 页面。此时需要在 GameView 中检查房间状态，如果房间已开启帧同步，则激活该房间接收广播，否则调用开始帧同步接口。之后继续将玩家状态改为【未准备】，避免出现回到 RoomView 中又自动跳转 GameView 的情况。

修改 GameView.js 的 onInit 方法。示例代码如下所示：
```
  onInit() {
    const button = new Component.Button(20, 20, "结束帧同步");

    const msgBox = new Component.MsgBox(20, 100, "");
    this.msgBox = msgBox;

    this.addComponent(button);
    this.addComponent(msgBox);

    if (Global.room.roomInfo.status === Global.ENUM.RoomStatusType.START) {
      // 房间已开始帧同步，激活接收帧同步消息
      Global.room.activeFrame();
    } else {
      // 房间已未开始帧同步，调用 startFrameSync 接口
      this.startFrameSync();
    }

    // 修改玩家状态
    this.changeState(0);
  }
```

在 GameView 类中添加 startFrameSync 方法。示例代码如下所示：
```
  // 开始帧同步
  startFrameSync() {
    const func = () => Global.room.startFrameSync({}, event => {
      if (event.code !== Global.ErrCode.EC_OK) {
        return this.dialog("操作失败，是否重试？", () => func());
      }
    });

    func();
  }
```

继续在 GameView 类中添加 changeState 方法：
```
  // 修改用户状态
  changeState(customStatus) {
    const changeUserStatePara = { customStatus };

    const func = () => Global.room.changeUserState(changeUserStatePara, event => {
      if (event.code !== Global.ErrCode.EC_OK) {
        this.dialog("操作失败，是否重试？", () => func());
      }
    });

    func();
  }
```

## 实现发送帧消息
玩家在游戏过程中发送的帧消息都是由一些指令组成，比如“跳跃”、“发射子弹”等操作。这里实现一个简单的指令，每个玩家发送一个随机数出去。在 GameView 类中添加一个 sendFrame 方法。示例代码如下所示：
```
  // 玩家发送帧消息
  sendFrame() {
    const data = {
      name: Global.name,
      action: "random",
      number: Math.ceil(Math.random() * 100),
    }

    Global.room.sendFrame(data);
  }
```

## 实现接收帧广播
开始帧同步后，SDK 会收到服务器推送的帧广播消息。开发者需要绑定 frameBroadcast 回调函数，接收并处理每一帧消息。

在 GameView 类的 onInit 中为 room 对象绑定帧消息广播回调，并实现 frameBroadcast 方法。示例代码如下所示：
```
  onInit() {

    // ...

    // 设置广播回调
    Global.room.frameBroadcast = this.frameBroadcast.bind(this);
  }

  // ...

  frameBroadcast(event) {
    // 在这里处理帧广播
  }
```

继续在 frameBroadcast 中添加代码，实现记录帧广播消息，并定时发送帧消息。示例代码如下所示：
```
  frameId = 0;
  frameItems = [];

  frameBroadcast(event) {
    // 在这里处理帧广播

    const frameId = event.data.frameId;

    // 每隔 15 帧发送一次帧消息
    if (frameId > this.frameId + 15) {
      this.frameId = frameId;
      this.sendFrame();
    }

    // 记录帧广播消息
    if (event.data.frameItems) {
      this.frameItems = this.frameItems.concat(event.data.frameItems);
    }
  }
```

然后在 onUpdate 中将帧消息渲染到页面上：
```
  onUpdate() {
    // 渲染层不断更新页面
    this.drawFrameItems();
  }

  // ...

  // 将 frameItems 绘制在页面上
  drawFrameItems() {
    // 只显示5行
    const max = 5;

    if (this.frameItems.length > max) this.frameItems = this.frameItems.slice(this.frameItems.length - max);

    let msg = "";
    this.frameItems.forEach(item => {
      msg += item.data.name + " : " + item.data.number + "\n";
    });

    this.msgBox.setText(msg);
  }
```

编译项目，在模拟器上依次点击【快速加房】、【准备】后，进入 GameView，页面将自动更新 MsgBox，并显示玩家消息。

![手机预览效果](https://main.qcloudimg.com/raw/351dea43bfe7517bc022cbd248ca0682.png)

## 实现停止帧同步

最后一步，为 button 绑定点击事件监听，实现停止帧同步。

在 onInit 中添加代码：
```
  onInit() {
    const button = new Component.Button(20, 20, "结束帧同步");
    button.onClick(() => this.stopFrameSync());
    
    // ...
  }
```

stopFrameSync 方法实现。示例代码如下所示：

```
  // 停止帧同步
  stopFrameSync() {

    if (Global.room.status === Global.ENUM.RoomStatusType.STOP) { return; }

    const func = () => Global.room.stopFrameSync({}, event => {
      if (event.code !== Global.ErrCode.EC_OK) {
        this.dialog("操作失败，是否重试？", () => func());
      }
      return this.loading('停止中...');
    });

    func();
  }
```

帧同步停止后，页面需要跳转到 RoomView。检查房间帧同步状态有两种方法，一是监听 stopGameBroadcast 广播，二是使用定时器去不断检查 room.roomInfo.status 的值。这里使用后者，利用定时器同时检查房间状态和房间成员状态，如果房间停止帧同步并且房间成员状态全部为0 ，就跳转到 RoomView。示例代码如下所示：
```
  checkRoom() {
    clearInterval(this.timer);

    // 定时检查房间状态息
    // 满足条件就跳转到房间页面
    this.timer = setInterval(() => {
      if (Global.room.roomInfo.status === Global.ENUM.RoomStatusType.STOP &&
        !Global.room.roomInfo.userList.find(user => user.customStatus === 1)) {
        return this.open(Global.RoomView);
      }
    }, 1000);
  }
```

在 onInit 中调用 checkRoom。示例代码如下所示：
```
  onInit() {
    // ...

    this.checkRoom();
  }
```

在 onDestroy 中清除定时器，并置空 frameBroadcast 回调。示例代码如下所示：
```
  onDestroy() {
    // 离开页面时一定要清除定时器
    clearInterval(this.timer);
    Global.room.frameBroadcast = null;
  }
```

编译代码，在模拟器中进入 GameView 开始帧同步，然后点击【结束帧同步】，界面将跳转到 RoomView，并且玩家状态为【未准备】。

至此，这个 HelloWorld 示例结束，完成了从匹配加房到开始帧同步、结束帧同步的流程，示例代码可以从这里下载。更多 MGOBE API 可以参考 [API 文档](https://cloud.tencent.com/document/product/1038/33331)。

## 腾讯云云游戏 SDK 时序图

![](https://main.qcloudimg.com/raw/bd9d347d6b38a6587854119ac57d9799.png)

## SDK 概览

### 云游戏生命周期相关接口

| 接口名称                                                    | 接口描述               |
| ----------------------------------------------------------- | ---------------------- |
| [TCGSDK.init(params)](#tcgsdk.init(params))                 | 云游戏前端初始化       |
| [TCGSDK.getClientSession()](#tcgsdk.getclientsession())     | 获取 Client 端会话信息 |
| [TCGSDK.start(serverSession)](#tcgsdk.start(serversession)) | 启动云游戏             |
| [TCGSDK.destroy(msg)](#tcgsdk.destroy(msg))                 | 立即停止云游戏         |
| [TCGSDK.reconnect()](#tcgsdk.reconnect())                   | 重连接口               |



### 游戏进程相关接口

| 接口名称                                                     | 接口描述                   |
| ------------------------------------------------------------ | -------------------------- |
| [TCGSDK.gameRestart(callback, retry)](#tcgsdk.gamerestart(callback.2C-retry)) | 重启当前运行的游戏进程     |
| [TCGSDK.loginHelper(params, callback) ](#tcgsdk.loginhelper(params.2C-callback).3B) | 辅助登陆                   |
| [TCGSDK.getLoginWindowStat(gameid, callback)](#tcgsdk.getloginwindowstat(gameid.2C-callback)) | 获取当前窗口是否为登陆窗口 |

### 鼠标键盘控制相关接口

| 接口名称                                                     | 接口描述                       |
| ------------------------------------------------------------ | ------------------------------ |
| [TCGSDK.sendKeyboardEvent(event)](#tcgsdk.sendkeyboardevent(event)) | 发送鼠标及键盘事件             |
| [TCGSDK.sendRawEvent(event)   ](#tcgsdk.sendrawevent(event)) | 发送鼠标及键盘事件（底层实现） |
| [TCGSDK.setMoveSensitivity(value)](#tcgsdk.setmovesensitivity(value)) | 设置鼠标移动灵敏度             |
| [TCGSDK.sendSeqRawEvents(events)](#tcgsdk.sendseqrawevents(events)) | 发送按键序列（底层实现）       |
| [TCGSDK.getMoveSensitivity()](#tcgsdk.getmovesensitivity())  | 获取当前鼠标灵敏度值           |
| [TCGSDK.setMouseCanLock(true/false) ](#tcgsdk.setmousecanlock(true.2Ffalse)) | 设置是否允许锁定鼠标           |
| [TCGSDK.mouseMove(identifier, type, x, y, isLogic)](#tcgsdk.mousemove(identifier.2C-type.2C-x.2C-y.2C-islogic)) | 移动端向云端发送鼠标移动事件   |
| [TCGSDK.mouseTabletMode(enable)](#tcgsdk.mousetabletmode(enable)) | 开启或关闭滑屏鼠标移动模式     |
| [TCGSDK.setRemoteCursor(mode)](#tcgsdk.setremotecursor(mode)) | 设置鼠标样式                   |
| [TCGSDK.setCursorShowStat(show)](#tcgsdk.setcursorshowstat(show)) | 设置鼠标隐藏或显示             |
| [TCGSDK.getCursorShowStat()](#tcgsdk.getcursorshowstat())    | 获取鼠标隐藏状态               |
| [TCGSDK.setMobileCursorScale(val)](#tcgsdk.setmobilecursorscale(val)) | 移动端设置鼠标放大系数         |
| [TCGSDK.setRemoteCursorStyle(style)](#tcgsdk.setremotecursorstyle(style)) | 设置云端的系统鼠标样式         |
| [TCGSDK.clearRemoteKeys()](#tcgsdk.clearremotekeys())        | 重置云端按键状态               |
| [TCGSDK.resetRemoteCapsLock() ](#tcgsdk.resetremotecapslock()) | 重置云端大小写状态             |



### 调试及日志相关接口

| 接口名称                                                     | 接口描述           |
| ------------------------------------------------------------ | ------------------ |
| [TCGSDK.setDebugMode(enable, userid)](#tcgsdk.setdebugmode(enable.2C-userid)) | 打开或关闭调试模式 |
| [TCGSDK.reportLog() ](#tcgsdk.reportlog())                   | 上报问题           |
| [TCGSDK.setLogHandler(handler)](#tcgsdk.setloghandler(handler)) | 设置日志回调函数   |

### 音视频相关接口

| 接口名称                                                     | 接口描述           |
| ------------------------------------------------------------ | ------------------ |
| [TCGSDK.setStreamProfile(profile, callback, retry)](#tcgsdk.setstreamprofile(profile.2C-callback.2C-retry)) | 设置码流参数       |
| [TCGSDK.getDisplayRect()](#tcgsdk.getdisplayrect())          | 获取显示区域的参数 |
| [TCGSDK.setVolume(val) ](#tcgsdk.setvolume(val))             | 设置本地播放音量   |
| [TCGSDK.getVolume()](#tcgsdk.getvolume())                    | 获取当前音量值     |



## 云游戏生命周期相关接口

### TCGSDK.init(params) 

```
初始化云游戏SDK，params对象有效字段如下：
    {
        mount: 'mount-point',// 必填，页面挂载点的HTML元素id
        appid: 123456789,// 必填，用户的腾讯云appid，见https://console.cloud.tencent.com/developer
        debug: false,// 可选，默认为false, 如果为true，则自动显示webrtc状态信息，否则需要按“CTRL+~”快捷键显示
        standalone: false,// 可选，默认为false, 如果为true，则页面自行请求webrtc接口，仅用于云游戏体验，正式上线必须走云API，云API对接文档看后面的《后端与云API对接实例》
        isArmBoard: false,// 可选，默认为false，只针对远端设备是安卓板子的情况，如无特殊情况，禁止修改此项，否则触控坐标会有问题
        isArmServer: false,// 可选，默认false，只针对远端设备是armserver
        ordered: true, // 可选，默认为true，关闭此选项可以略微降低输入延迟，但是存在输入丢失风险
        showLogo: true,// 可选，默认为true，false则隐藏logo
        mask: true,// 可选，默认为true，false则隐藏click to start蒙层
        preloadTime: 3000,// 可选，游戏预加载时间，提前加载游戏的时间，单位为毫秒，默认为3000ms
        mic: false, // 可选，开启麦克风，默认为false
        nativeCursor: true, // 可选，默认为true，是否显示本地鼠标
        forceShowCursor: false, // 可选，默认为false, 强制显示鼠标，这时候忽略服务端下发的鼠标状态信息
        tabletMode: false, // 可选，默认为false，true则使用平板滑动鼠标模式，false为绝对映射模式，这个参数只针对移动端，PC端忽略该参数
        clickToFullscreen: true, // 可选，默认为true，是否启动点击全屏操作
        idleThreshold: true, // 可选，单位为秒，默认为300，空闲时间阈值，空闲超过这个时间将触发onNetworkChange事件，消息为{status: 'idle', times: 1}
        keepLastFrame: false,// 可选，断开的时候是否保留最后一帧画面，true-保留，false-不保留，默认false，如果需要保留最后一帧画面并重连，不能再次调用init函数，而是先调用destroy()接口，再调用start()接口
        reconnect: true, // 可选，默认为true，true-帧率掉0或者异常断开自动重连一次，false-不重连
        channel: 'product', // 可选，默认为'product', 'dev'-测试环境，'product'-正式环境
        loadingText: '加载中', // 可选，加载中的文字提示，默认为'正在启动云游戏'
        baseUrl: '',// 可选，webrtc请求的host部分，如http://cloud-gaming.myqcloud.com；但如果是本地html文件直接打开，则此参数必填；
        onGamepadConnectChange: function(){...},// 可选，手柄连接/断开事件回调
        onOrientationchange: function(res){...},// 可选，屏幕方向变化事件回调
        onConnectFail: function(res){...},// 可选，连接失败回调，调用start接口成功后才会触发
        onConnectSucc: function(res){...},// 可选，连接成功回调，调用start接口成功后才会触发
        onDisconnect: function(res){...},// 可选，断开/被踢触发此回调，调用start接口成功后才会触发
        onTouchEvent: function(event){...},// 可选，移动端触摸事件回调，调用start接口成功后才会触发, event结构如下：
        onWebrtcStat: function(ret){...},// 可选，webrtc状态回调，调用start接口成功后才会触发，设置这个回调后，如果webrtc请求返回错误，SDK不再自动弹出默认自带的错误提示框
        onInitSuccess: function(res){...},// 可选，初始化完毕的回调，触发此回调之后才能调用后面的API
        onNetworkChange: function(event){...},// 可选，网络状态变化，有以下状态，消息event分别对应如下：
        onInputStatusChanged: function(oldStatus, newStatus){...},// 可选，云端输入状态改变，有点击事件的时候都会触发，需要判断新旧状态
        onCursorShowStatChanged: function(oldStatus, newStatus){...},// 可选，云端鼠标显示/隐藏，只在变化的时候回调
        onLog: function(logText) {...}// 可选，日志回调函数，用于外部获取日志，作用与setLogHandler接口一致
    }    
```

#### onTouchEvent 事件字段描述

```
    {
        id: integer,// 触控事件的id
        type: string,// 事件类型，'touchstart','touchmove','touchend'三种之一
        cursorShow: boolean, // 云端鼠标是否隐藏
        x: integer,// 触控点在云端视频内的x坐标
        y: integer,// 触控点在云端视频内的y坐标
        pageX: integer,// 触控点在当前网页内的x坐标
        pageY: integer,// 触控点在当前网页内的y坐标
        movementX: integer,// 触控点相对上次坐标的x偏移值
        movementY: integer// 触控点相对上次坐标的y偏移值
    }
```

#### onNetworkChange 网络事件类型

| 描述                | event                                                        |
| ------------------- | ------------------------------------------------------------ |
| 物理网络已连接      | {"status": "online"}                                         |
| 物理网络已断开      | {"status": "offline"}                                        |
| 帧率低或卡顿        | {"status": "lag"}                                            |
| 空闲或无操作        | {"status": "idle"}                                           |
| 外网IP变化          | {"status": "ipchanged"}                                      |
| 连接loading时间过长 | {"status": "noflow"}                                         |
| 已连接但帧率掉0     | {"status": "noflowcenter"}                                   |
| 实时状态数据        | {"status": "stats", "stats": {...}}，stats字段的结构请参见  [stats 字段描述](#stats)。 |

####  <span id="stats ">stats 字段描述</span>

| 字段            | 类型   | 描述                                         |
| --------------- | ------ | -------------------------------------------- |
| bit_rate        | string | 客户端接收的码率，单位：Mbps。               |
| cpu             | string | 云端 CPU 占用率，单位：百分比。              |
| delay           | string | 客户端收到图像帧到解码显示的延时，单位：ms。 |
| fps             | string | 客户端显示帧率。                             |
| load_cost_time  | number | 云端加载时间。                               |
| nack            | string | 客户端重传次数。                             |
| packet_lost     | string | 客户端丢包次数。                             |
| packet_received | string | 客户端收到的包总数。                         |
| rtt             | number | 客户端到云端，网络端数据包往返耗时，。       |
| timestamp       | number | 此数据回调的时间戳，单位：ms。               |


#### <span id="onWebrtcStat_wrong">onWebrtcStat 错误码汇总</span>

| 错误码 | 说明                       |
| ------ | -------------------------- |
| code=0 | 请求正常                   |
| code=1 | 系统繁忙                   |
| code=2 | 票据不合法                 |
| code=3 | 用户带宽不足               |
| code=4 | 资源不足，没有可用机器     |
| code=5 | session 失效，需要重新登录 |
| code=6 | 媒体描述信息错误           |
| code=7 | 游戏拉起失败               |

#### onDisconnect 错误码汇总

| 错误码 | 说明     |
| ------ | -------- |
| code=0 | 被踢     |
| code=1 | 系统繁忙 |

### TCGSDK.getClientSession()

获取 client 端的会话信息，用于请求用户后端得到 serverSession，调用实例可以参照 demo.html 和本文档后面。

### TCGSDK.start(serverSession)

> 注意：这一段没看懂~~
> 前端先请求用户后端接口拿到 serverSession，并调用此接口开启游戏，serverSession 由用户后端请求云API生成，云API接口文档参见腾讯文档分享的《腾讯云云游戏》及本文档后面的《后端与云API对接实例》;

| 参数          | 参数类型 | 说明 |
| ------------- | -------- | ---- |
| serverSession |          |      |

### TCGSDK.destroy(msg)

立即停止云游戏，销毁数据连接和显示画面。

| 参数 | 参数类型 | 说明                                                         |
| ---- | -------- | ------------------------------------------------------------ |
| msg  |          | 默认错误弹窗的提示内容，结构为：`{"code": Number, "message": "your message"}`，msg 可以为 null。 |

> ! 如果 init 时设置了 onWebrtcState 回调，SDK 将不再自动弹出错误提示。

### TCGSDK.reconnect()

轻量级重连接口，需要之前的连接是成功的才有效，不可滥用。



## 游戏进程相关接口

### TCGSDK.gameRestart(callback, retry)

重启当前运行的游戏进程。

| 参数     | 参数类型 | 说明     |
| -------- | -------- | -------- |
| callback |          | 调用结果 |
| retry    |          | 重发次数 |

### TCGSDK.loginHelper(params, callback);

辅助登录。

| 参数     | 参数类型 | 说明                                                         |
| -------- | -------- | ------------------------------------------------------------ |
| params   |          | 辅助登录的参数，主要参数如下：<br>gameid：游戏 ID。<br>acc：帐号字符串。<br />pwd：密码字符串。 |
| callback |          | 执行结果回调。                                               |

**callback 的原型：**

```
function(res) {
  console.log(res)
}
```

**params js object 结构示例如下：**

```
{
  gameid: '12',
  acc: 'account',
  pwd: 'password',
}
```


### TCGSDK.getLoginWindowStat(gameid, callback)

获取当前窗口是否登录窗口。

| 参数     | 参数类型 | 说明           |
| -------- | -------- | -------------- |
| gameid   |          | 游戏 ID        |
| callback |          | 执行结果回调。 |

**callback 的原型如下：**

```
function(res) {
  console.log(res);
}
```

**返回的 res 结构：**

```
{code:0, data:{bottom: number, found: 1/0, left: number, name: 'xxxx', right: number, top: number, capslock: 0/1}}
```

  - found: 0表示当前不是登录窗口，1表示是登录窗口。
  - capslock: 0表示当前是小写，1表示是大写。



## **鼠标键盘控制相关接口**

### TCGSDK.sendKeyboardEvent(event)

对 [sendRawEvent(event)](#tcgsdk.sendrawevent(event)) 的包装，省掉 type 参数，可以用 html 元素定义一些虚拟按键，demo.html 有简单的例子。事件触发后调用 sendKeyboardEvent 发送按键消息，您可从 [键盘码查看网](https://keycode.info/) 中获取键盘的键位值。

| 参数  | 参数类型 | 说明                                          |
| ----- | -------- | --------------------------------------------- |
| event |          | 对象结构：`{key: Integer, down: true/false }` |


### TCGSDK.sendRawEvent(event)

更底层的发送函数，允许定义 event 的类型。event 对象结构如下：

   - 鼠标偏移（用于无边框限制的鼠标移动事件）：``{ type: "mousedeltamove", x: Number, y: Number }``，x、y坐标值均为整数。
   - 鼠标移动：``{ type: "mousemove", x: Number, y: Number }``，x、y坐标值均为整数
   - 鼠标左键点击：``{ type: "mouseleft", down: true/false }``
   - 鼠标右键点击：``{ type: "mouseright", down: true/false }``
   - 鼠标滚动：``{ type: "mousescroll", delta: Number }``
   - 键盘按键事件：``{ type: "keyboard", key: Integer, down: true/false }``
   - 手柄事件：
     1. 手柄连接事件：``{ type: "gamepadconnect" }``，发送操作按键前必须先发送这个事件
     2. 手柄断开事件：``{ type: "gamepaddisconnect" }``
     3. 手柄按键事件：``{ type: "gamepadkey", key: Number, down: true/false }``
        方向键：up->0x01, down->0x02, left->0x04, right->0x08
        按键：X->0x4000, Y->0x8000, A->0x1000, B->0x2000
        select：0x20
        start：0x10
     4. 手柄左摇杆事件：``{ type: "axisleft", x: [-32767~32767], y: [-32767~32767] }``，原浮点（-1~1）数值
     5. 手柄右摇杆事件：``{ type: "axisright", x: [-32767~32767], y: [-32767~32767] }``，原浮点（-1~1）数值
     6. 手柄左触发键（L1）事件：``{type: "gamepadkey", key: 0x100, down: true/false}``
     7. 手柄右触发键（R1）事件：``{type: "gamepadkey", key: 0x200, down: true/false}``
     8. 手柄左触发键（L2）事件：``{ type: "lt", x: [0-255], down: true/false }``，原浮点（0~1）数值：255
     9. 手柄右触发键（R2）事件：``{ type: "rt", x: [0-255], down: true/false }``，原浮点（0~1）数值：255
     10. 手柄左摇杆垂直按下（L3）事件：``{type: "gamepadkey", key: 0x80, down: true/false}``
     11. 手柄右摇杆垂直按下（R3）事件：``{type: "gamepadkey", key: 0x40, down: true/false}``

> ! 如果直接调用此接口发送鼠标移动/偏移事件，需额外处理显示区域偏移、灵敏度和坐标缩放，灵敏度设置 API 也无效，因此建议调用后面的 mouseMove 接口。

### TCGSDK.setMoveSensitivity(value)

设置鼠标或者触摸移动的敏感度，value为[0.01, 100.0]之间的的浮点数。

| 参数   | 参数类型 | 说明                                    |
| ------ | -------- | --------------------------------------- |
| events | float    | 取值范围：[0.01, 100.0]之间的的浮点数。 |


### TCGSDK.sendSeqRawEvents(events)

底层发送按键序列的函数。

| 参数   | 参数类型 | 说明                                                         |
| ------ | -------- | ------------------------------------------------------------ |
| events |          | 事件数组，如：如`` events = [{type: "mouseleft", down: true},{type: "mouseleft", down: true},...]``，数组最大限制10事件。 |

> ? event 的对象结构参考 [TCGSDK.sendRawEvent](#tcgsdk.sendrawevent(event)) 的描述。

### TCGSDK.getMoveSensitivity()

获取当前的鼠标灵敏度值。

### TCGSDK.setMouseCanLock(true/false)

设置是否允许锁定鼠标，用于用户操作网页控件，默认为 true。


### TCGSDK.mouseMove(identifier, type, x, y, isLogic)

移动端向云端（PC 端）发送鼠标移动事件。

| 参数       | 参数类型 | 说明                                                         |
| ---------- | -------- | ------------------------------------------------------------ |
| identifier | int      | 触控点的 ID，多点触控时每个触控点id不能相等，同个触控点的所有事件的触控点id必须一致。 |
| type       | string   | 触控事件类型，值为`touchstart`、`touchmove`、`touchend`、`touchcancel`中的一个，对于同一个触控点，touchstart 必须且只对应一个 `touchend` 或 `touchcancel`。 |
| x          | float    | 填写数字，触控点的 x 坐标，但是如果传浮点数，则按逻辑坐标处理。 |
| y          | float    | 填写数字，触控点的 y 坐标，但是如果传浮点数，则按逻辑坐标处理。 |
| isLogic    | boolean  | true 代表逻辑坐标，false或者不传则代表的是物理坐标（像素绝对坐标）。 |

>! 调用此接口无需额外处理显示区域偏移、灵敏度和坐标缩放。


### TCGSDK.mouseTabletMode(enable)

开启或关闭滑屏鼠标移动模式，可以随时切换，目前仅支持移动端。

| 参数   | 参数类型 | 说明                      |
| ------ | -------- | ------------------------- |
| enable | boolean  | true：打开，false：关闭。 |


### TCGSDK.setRemoteCursor(mode)

设置鼠标样式。

| 参数 | 参数类型 | 说明                                                         |
| ---- | -------- | ------------------------------------------------------------ |
| mode |          | 目前支持三种鼠标样式：<br>mode=0：页面渲染的固定鼠标图片。<br/>mode=1：云端下发鼠标图片，由浏览器页面渲染。<br/>mode=2：云端画面内渲染鼠标图片，此时会隐藏本地渲染的鼠标，兼容性最好，但是有延时。 |

### TCGSDK.setCursorShowStat(show)

设置鼠标隐藏或显示。

| 参数 | 类型    | 说明                    |
| ---- | ------- | ----------------------- |
| show | boolean | true：显示，false：隐藏 |

### TCGSDK.getCursorShowStat()

获取鼠标隐藏状态。

### TCGSDK.setMobileCursorScale(val)

移动端设置鼠标放大系数。

| 参数 | 参数类型 | 说明                                  |
| ---- | -------- | ------------------------------------- |
| val  |          | 放大系数，默认是1.0，与云端大小一致。 |

### TCGSDK.setRemoteCursorStyle(style)

设置云端的系统鼠标样式，[setRemoteCursor](r#tcgsdk.setremotecursor(mode)) 的 mode 为1和2时生效；

| 参数  | 参数类型 | 说明                                                         |
| ----- | -------- | ------------------------------------------------------------ |
| style |          | 样式字符串，值为以下的值之一：<ul syule="margin:0"><li>standard：系统默认鼠标样式，较小。</li><li>default_huge：系统超大鼠标样式，较大。</li></ul> |


### TCGSDK.clearRemoteKeys()

重置云端所有按键状态，用于卡键场景。

### TCGSDK.resetRemoteCapsLock()

重置云端大小写状态为小写。

## **调试及日志相关接口**

### TCGSDK.setDebugMode(enable, userid)

打开或关闭调试模式，打开的情况下将在控制台打印日志。

| 参数   | 参数类型 | 说明                            |
| ------ | -------- | ------------------------------- |
| enable |          | 打开日志和状态。                |
| userid |          | 用户的 ID，主要是用于过滤日志。 |

### TCGSDK.reportLog()

上报问题。

### TCGSDK.setLogHandler(handler)

设置日志回调函数，便于外部获取详细日志，作用与 init 时传的 onLog 回调一致。

| 参数    | 参数类型 | 说明                                     |
| ------- | -------- | ---------------------------------------- |
| handler |          | 日志回调函数，原型：function (logText)。 |



## 音视频相关接口

### TCGSDK.setStreamProfile(profile, callback, retry)

设置码流参数。

| 参数     | 参数类型 | 说明                                                         |
| -------- | -------- | ------------------------------------------------------------ |
| profile  | int      | 目前可用参数如下：<br>fps：帧率，范围[10,60]，单位帧。<br>max_bitrate：最大码率，范围[1,15]，单位：Mbps。<br>min_bitrate：最小码率，范围[1,15], 单位：Mbps。 |
| callback |          | 设置结果回调函数，可为 null。                                |
| retry    |          | 重试次数，可不填。                                           |

### TCGSDK.getDisplayRect()

获取显示区域的参数，边距，宽高等。

### TCGSDK.setVolume(val)

设置本地播放音量。

| 参数 | 参数类型 | 说明                          |
| ---- | -------- | ----------------------------- |
| val  | float    | 取值范围：[0,1]之间的浮点数。 |

### TCGSDK.getVolume()

获取当前音量值。

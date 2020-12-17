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
| [TCGSDK.loginHelper(params, callback) ](#tcgsdk.loginhelper(params.2C-callback).3B) | 辅助登录                   |
| [TCGSDK.getLoginWindowStat(gameid, callback)](#tcgsdk.getloginwindowstat(gameid.2C-callback)) | 获取当前窗口是否为登录窗口 |

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
| [TCGSDK.setDefaultCursorImage(url)](#tcgsdk.setdefaultcursorimage(url))  |设置云游戏页面中鼠标默认图片              |



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
| [TCGSDK.setPageBackground(url) ](#tcgsdk.setpagebackground(url))       | 设置云游戏页面的背景图     |




## 生命周期相关接口

### TCGSDK.init(params) 

params对象有效字段描述：

| 参数                    | 类型     | 是否可选 | 描述                                                         |
| ----------------------- | -------- | -------- | ------------------------------------------------------------ |
| mount                   | string   | 必填     | 页面挂载点的 HTML 元素 ID                                    |
| appid                   | number   | 必填     | 用户的腾讯云 [APPID](https://console.cloud.tencent.com/developer) |
| debug                   | boolean  | 可选     | true 为自动显示 webrtc 状态信息，否则需要按 `CTRL+~` 快捷键显示。默认值：false |
| showLogo                | boolean  | 可选     | 隐藏腾讯云 Logo，true 为隐藏，false 为不隐藏。默认值为 true  |
| mask                    | boolean  | 可选     | false 为隐藏 `click to start` 蒙层，默认值为 true            |
| mic                     | boolean  | 可选     | 开启本地麦克风，true 为开启，false 为关闭。默认值为 false     |
| nativeCursor            | boolean  | 可选     | 是否显示本地鼠标，true 为显示，false 为隐藏。默认值为 true   |
| tabletMode              | boolean  | 可选     | true 为使用平板滑动鼠标模式，false 为绝对映射模式。该参数只针对移动端，PC 端忽略该参数。默认值：false |
| clickToFullscreen       | boolean  | 可选     | 是否启动点击全屏操作，true 为启用，false为禁用。默认值为 true |
| idleThreshold           | number   | 可选     | 用户操作空闲时间阈值，单位为秒，默认值：300s<br />空闲超过这个时间将触发 `onNetworkChange` 事件，消息为 `{status: 'idle', times: 1}` |
| keepLastFrame           | boolean  | 可选     | 断开的时候是否保留最后一帧画面，如果需要保留最后一帧画面并重连，不能再次调用 init 函数，而是先调用 `destroy()` 接口，再调用 `start()` 接口。默认值：false |
| reconnect               | boolean  | 可选     | 默认值：true<br />true 为帧率掉0或者异常断开自动重连一次，false 为不重连 |
| channel                 | string   | 可选     | `'dev'`：测试环境，`'product'`：正式环境。默认值：`'product'` |
| loadingText             | string   | 可选     | 加载中的文字提示内容，默认值：`'正在启动云游戏' `              |
| baseUrl                 | string   | 可选     | webrtc 请求的 host 部分                                      |
| onGamepadConnectChange  | function | 可选     | 手柄连接/断开事件回调                                        |
| onOrientationchange     | function | 可选     | 屏幕方向变化事件回调                                         |
| onConnectFail           | function | 可选     | 连接失败回调，调用 start 接口成功后才会触发                  |
| onConnectSucc           | function | 可选     | 连接成功回调，调用 start 接口成功后才会触发                  |
| onDisconnect            | function | 可选     | 断开/被踢触发此回调，调用 start 接口成功后才会触发           |
| onTouchEvent            | function | 可选     | 移动端触摸事件回调，调用 start 接口成功后才会触发            |
| onWebrtcStat            | function | 可选     | webrtc 状态回调，调用 start 接口成功后才会触发，设置这个回调后，如果 webrtc 请求返回错误，SDK 不再自动弹出默认自带的错误提示框 |
| onInitSuccess           | function | 可选     | 初始化完毕的回调，触发此回调之后才能调用后面的 API           |
| onNetworkChange         | function | 可选     | 网络状态变化                                                 |
| onInputStatusChanged    | function | 可选     | 云端输入状态改变，有点击事件的时候都会触发，需要判断新旧状态 |
| onCursorShowStatChanged | function | 可选     | 云端鼠标显示/隐藏，只在变化的时候回调                        |
| onLog                   | function | 可选     | 日志回调函数，用于外部获取日志，作用与 [setLogHandler](#tcgsdk.setloghandler(handler)) 接口一致 |

#### onTouchEvent 事件字段描述

| 字段       | 类型    | 描述                                                         |
| ---------- | ------- | ------------------------------------------------------------ |
| id         | number  | 触控事件的 ID                                                |
| type       | string  | 事件类型，可选择 `'touchstart'`，`'touchmove'`，`'touchend'` 三种之一 |
| cursorShow | boolean | 云端鼠标是否隐藏，true 为显示，false 为隐藏                  |
| x          | number  | 触控点在视频区域内的 x 坐标                                  |
| y          | number  | 触控点在视频区域内的 y 坐标                                  |
| pageX      | number  | 触控点在当前网页内的 x 坐标                                  |
| pageY      | number  | 触控点在当前网页内的 y 坐标                                  |
| movementX  | number  | 触控点相对上次坐标的 x 偏移值                                |
| movementY  | number  | 触控点相对上次坐标的 y 偏移值                                |

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
| 实时状态数据        | {"status": "stats", "stats": {...}}，stats字段的结构请参见  [stats 字段描述](#stats_cpde) |

####  <span id="stats_cpde">stats 字段描述</span>

| 字段            | 类型   | 描述                                       |
| --------------- | ------ | ------------------------------------------ |
| bit_rate        | string | 客户端接收的码率，单位：Mbps               |
| cpu             | string | 云端 CPU 占用率，单位：百分比              |
| delay           | string | 客户端收到图像帧到解码显示的延时，单位：ms |
| fps             | string | 客户端显示帧率                             |
| load_cost_time  | number | 云端加载时长，单位：ms                     |
| nack            | string | 客户端重传次数                             |
| packet_lost     | string | 客户端丢包次数                             |
| packet_received | string | 客户端收到的包总数                         |
| rtt             | number | 客户端到云端，网络端数据包往返耗时         |
| timestamp       | number | 此数据回调的时间戳，单位：ms               |


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

客户端获取 Client 端的会话信息，后续供业务 Server 调用 [CreateSession(clientsession)](https://cloud.tencent.com/document/product/1162/40740) 使用。

### TCGSDK.start(serverSession)

 业务 Server 调用 [CreateSession](https://cloud.tencent.com/document/product/1162/40740) 获取到 serversession 后调用该接口启动云游戏。

### TCGSDK.destroy(msg)

立即停止云游戏，销毁数据连接和显示画面。

| 参数 | 参数类型 | 说明                                                         |
| ---- | -------- | ------------------------------------------------------------ |
| msg  | object   | 默认错误弹窗的提示内容，结构为：`{"code": Number, "message": "your message"}`，msg 可以为 null |

> ! 如果 init 时设置了 onWebrtcState 回调，SDK 将不再自动弹出错误提示。

### TCGSDK.reconnect()

轻量级重连接口，需要之前的连接是成功的才有效，不可滥用。



## 游戏进程相关接口

### TCGSDK.gameRestart(callback, retry)

重启当前运行的游戏进程。

| 参数     | 参数类型 | 说明     |
| -------- | -------- | -------- |
| callback | function | 调用结果 |
| retry    | number   | 重发次数 |

### TCGSDK.loginHelper(params, callback)

辅助登录。

| 参数     | 参数类型 | 说明                                                         |
| -------- | -------- | ------------------------------------------------------------ |
| params   | object   | 辅助登录的参数，主要参数如下：<li>gameid：游戏 ID</li><li>acc：帐号字符串</li><li>pwd：密码字符串</li> |
| callback | function | 执行结果回调                                                 |

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

| 参数     | 参数类型 | 说明         |
| -------- | -------- | ------------ |
| gameid   | string   | 游戏 ID      |
| callback | function | 执行结果回调 |

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

- found：0表示当前不是登录窗口，1表示是登录窗口。
- capslock：0表示当前是小写，1表示是大写。



## 鼠标键盘控制相关接口

### TCGSDK.sendKeyboardEvent(event)

对 [sendRawEvent(event)](#tcgsdk.sendrawevent(event)) 的包装，省掉 type 参数，可以用 html 元素定义一些虚拟按键，[demo.html](https://tcgsdk-1258344699.cos.ap-guangzhou.myqcloud.com/download/tcgsdk-latest.tar.gz) 有简单的例子。事件触发后调用 sendKeyboardEvent 发送按键消息，您可从 [键盘码查看网](https://keycode.info/) 中获取键盘的键位值。

| 参数  | 参数类型 | 说明                                          |
| ----- | -------- | --------------------------------------------- |
| event | object   | 对象结构：`{key: Integer, down: true/false }` |


### TCGSDK.sendRawEvent(event)

更底层的发送函数，允许定义 event 的类型。event 对象结构如下：

<table>
<thead><tr><th colspan=2>event 对象</th><th>结构说明</th>
</tr>
</thead>
<tbody><tr>
<td colspan=2>鼠标偏移（用于无边框限制的鼠标移动事件）</td>
<td><code>{ type: "mousedeltamove", x: Number, y: Number }</code>，x、y 坐标值均为整数</td>
</tr><tr>
<td colspan=2>鼠标移动</td>
<td><code>{ type: "mousemove", x: Number, y: Number }</code>，x、y 坐标值均为整数</td>
</tr><tr>
<td colspan=2>鼠标左键点击</td>
<td><code>{ type: "mouseleft", down: true/false }</code></td>
</tr><tr>
<td colspan=2>鼠标右键点击</td>
<td><code>{ type: "mouseright", down: true/false }</code></td>
</tr><tr>
<td colspan=2>鼠标滚动</td>
<td><code>{ type: "mousescroll", delta: Number }</code></td>
</tr><tr>
<td colspan=2>键盘按键事件</td>
<td><code>{ type: "keyboard", key: Integer, down: true/false }</code></td>
</tr><tr>
<td rowspan=12>手柄事件</td>
<td>手柄连接事件</td>
<td><code>{ type: "gamepadconnect" }</code>，发送操作按键前必须先发送这个事件</td>
</tr><tr>
<td>手柄断开事件</td>
<td><code>{ type: "gamepaddisconnect" }</code></td>
</tr><tr>
<td>手柄按键事件</td>
<td><code>{ type: "gamepadkey", key: Number, down: true/false }</code><ul style="margin:0"><li>方向键事件值：向上键值为<code>0x01</code>，向下键值为<code>0x02</code>，向左键值为<code>0x04</code>，向右键值为<code>0x08</code></li><li>按键事件值：X 键值为<code>0x4000</code>，Y 键值为<code>0x8000</code>，A 键值为<code>0x1000</code>，B 键值为<code>0x2000</code></li><li>select 事件值：键值为<code>0x20</code></li><li>start 事件值：键值为<code>0x10</code></li></ul></td>
</tr><tr>
<td>手柄左摇杆事件</td>
<td><code>{ type: "axisleft", x: [-32767~32767], y: [-32767~32767] }</code>，原浮点数值为（-1~1），实际返回原浮点数值 * 32767</td>
</tr><tr>
<td>手柄右摇杆事件</td>
<td><code>{ type: "axisright", x: [-32767~32767], y: [-32767~32767] }</code>，原浮点数值为（-1~1），实际返回原浮点数值 * 32767</td>
</tr><tr>
<td>手柄左触发键（L1）事件</td>
<td><code>{type: "gamepadkey", key: 0x100, down: true/false}</code></td>
</tr><tr>
<td>手柄右触发键（R1）事件</td>
<td><code>{type: "gamepadkey", key: 0x200, down: true/false}</code></td>
</tr><tr>
<td>手柄左触发键（L2）事件</td>
<td><code>{ type: "lt", x: [0-255], down: true/false }</code>，原浮点数值为（0~1），实际返回原浮点数值 * 255</td>
</tr><tr>
<td>手柄右触发键（R2）事件</td>
<td><code>{ type: "rt", x: [0-255], down: true/false }</code>，原浮点数值为（0~1），实际返回原浮点数值 * 255</td>
</tr><tr>
<td>手柄左摇杆垂直按下（L3）事件</td>
<td><code>{type: "gamepadkey", key: 0x80, down: true/false}</code></td>
</tr><tr>
<td>手柄右摇杆垂直按下（R3）事件</td>
<td><code>{type: "gamepadkey", key: 0x40, down: true/false}</code></td>
</tr>
</tbody></table>

> ! 如果直接调用此接口发送鼠标移动/偏移事件，需额外处理显示区域偏移、灵敏度和坐标缩放，灵敏度设置 API 也无效，因此建议调用后面的 [mouseMove](#tcgsdk.mousemove(identifier.2C-type.2C-x.2C-y.2C-islogic)) 接口。

### TCGSDK.setMoveSensitivity(value)

设置鼠标或者触摸移动的敏感度。

| 参数  | 参数类型 | 说明                                  |
| ----- | -------- | ------------------------------------- |
| value | number   | 取值范围：[0.01, 100.0]之间的浮点数 |


### TCGSDK.sendSeqRawEvents(events)

底层发送按键序列的函数。

| 参数   | 参数类型 | 说明                                                         |
| ------ | -------- | ------------------------------------------------------------ |
| events | object   | 事件数组，例如：`` events = [{type: "mouseleft", down: true},{type: "mouseleft", down: true},...]``，数组最大限制10个事件 |

> ? event 的对象结构参考 [TCGSDK.sendRawEvent](#tcgsdk.sendrawevent(event)) 的描述。

### TCGSDK.getMoveSensitivity()

获取当前的鼠标灵敏度值。

### TCGSDK.setMouseCanLock(true/false)

设置是否允许锁定鼠标，用于用户操作网页控件，其中 true 为允许，false 为禁止。默认为 true。


### TCGSDK.mouseMove(identifier, type, x, y, isLogic)

移动端向云端（PC 端）发送鼠标移动事件。

| 参数       | 参数类型 | 说明                                                         |
| ---------- | -------- | ------------------------------------------------------------ |
| identifier | number   | 触控点的 ID，多点触控时每个触控点 ID不能相等，同个触控点的所有事件的触控点 ID 必须一致 |
| type       | string   | 触控事件类型，值为`touchstart`、`touchmove`、`touchend`、`touchcancel`中的一个，对于同一个触控点，`touchstart` 必须且只对应一个 `touchend` 或 `touchcancel` |
| x          | number   | 填写数字，触控点的 x 坐标，但是如果传浮点数，则按逻辑坐标处理 |
| y          | number   | 填写数字，触控点的 y 坐标，但是如果传浮点数，则按逻辑坐标处理 |
| isLogic    | boolean  | true 代表逻辑坐标，false 或者不传则代表的是物理坐标（像素绝对坐标） |

>! 调用此接口无需额外处理显示区域偏移、灵敏度和坐标缩放。


### TCGSDK.mouseTabletMode(enable)

开启或关闭滑屏鼠标移动模式，可以随时切换，目前仅支持移动端。

| 参数   | 参数类型 | 说明                    |
| ------ | -------- | ----------------------- |
| enable | boolean  | true：打开，false：关闭 |


### TCGSDK.setRemoteCursor(mode)

设置鼠标样式。

| 参数 | 参数类型 | 说明                                                         |
| ---- | -------- | ------------------------------------------------------------ |
| mode | number   | 目前支持三种鼠标样式：<li>mode=0：页面渲染的固定鼠标图片</li><li>mode=1：云端下发鼠标图片，由浏览器页面渲染</li><li>mode=2：云端画面内渲染鼠标图片，此时会隐藏本地渲染的鼠标，兼容性最好，但是有延时</li> |

### TCGSDK.setCursorShowStat(show)

设置鼠标隐藏或显示。

| 参数 | 类型    | 说明                    |
| ---- | ------- | ----------------------- |
| show | boolean | true：显示，false：隐藏 |

### TCGSDK.getCursorShowStat()

获取鼠标隐藏状态。

### TCGSDK.setMobileCursorScale(val)

移动端设置鼠标放大系数。

| 参数 | 参数类型 | 说明                                                  |
| ---- | -------- | ----------------------------------------------------- |
| val  | number   | 放大系数，默认是1.0，与云端大小一致，取值范围[0.1,10] |

### TCGSDK.setRemoteCursorStyle(style)

设置云端的系统鼠标样式，[setRemoteCursor](#tcgsdk.setremotecursor(mode)) 的 mode 为1和2时生效；

| 参数  | 参数类型 | 说明                                                         |
| ----- | -------- | ------------------------------------------------------------ |
| style | string   | 样式字符串，值为以下的值之一：<li>standard：系统默认鼠标样式，较小</li><li>default_huge：系统超大鼠标样式，较大</li> |


### TCGSDK.clearRemoteKeys()

重置云端所有按键状态，用于云端按键卡住的场景。

### TCGSDK.resetRemoteCapsLock()

重置云端大小写状态为小写。

###  TCGSDK.setDefaultCursorImage(url)

设置云游戏页面中鼠标默认图片。

| 参数 | 参数类型 | 说明             |
| ---- | -------- | ---------------- |
| url  | Context  | 鼠标样式图片 URL |

## 调试及日志相关接口

### TCGSDK.setDebugMode(enable, userid)

打开或关闭调试模式，打开的情况下将在控制台打印日志。

| 参数   | 参数类型 | 说明                                      |
| ------ | -------- | ----------------------------------------- |
| enable | boolean  | 打开日志和状态，true 为打开，false 为隐藏 |
| userid | string   | 用户的 ID，主要是用于过滤日志             |

### TCGSDK.reportLog()

上报问题。

### TCGSDK.setLogHandler(handler)

设置日志回调函数，便于外部获取详细日志，作用与 init 时传的 onLog 回调一致。

| 参数    | 参数类型 | 说明                                     |
| ------- | -------- | ---------------------------------------- |
| handler | function | 日志回调函数，原型：`function (logText)` |



## 音视频相关接口

### TCGSDK.setStreamProfile(profile, callback, retry)

设置码流参数。

| 参数     | 参数类型 | 说明                                                         |
| -------- | -------- | ------------------------------------------------------------ |
| profile  | number   | 目前可用参数如下：<li>fps：帧率，范围[10,60]，单位：帧</li><li>max_bitrate：最大码率，范围[1,15]，单位：Mbps</li><li>min_bitrate：最小码率，范围[1,15]，单位：Mbps</li> |
| callback | function | 设置结果回调函数，可为 null                                  |
| retry    | number   | 重试次数，可不填                                             |

### TCGSDK.getDisplayRect()

获取显示区域的参数，边距，宽高等。

### TCGSDK.setVolume(val)

设置本地播放音量。

| 参数 | 参数类型 | 说明                        |
| ---- | -------- | --------------------------- |
| val  | number   | 取值范围：[0,1]之间的浮点数 |

### TCGSDK.getVolume()

获取当前音量值。

### TCGSDK.setPageBackground(url)

设置云游戏页面的背景图。

| 参数 | 参数类型 | 说明         |
| ---- | -------- | ------------ |
| url  | Context  | 背景图片 URL |



## Android SDK 时序图

腾讯云云游戏 SDK 时序图如下：

![](https://main.qcloudimg.com/raw/d7d82673b8e1ead4a31301ef2c7de3c9.png)
## Android SDK 接口概览

### 生命周期相关接口

| 接口名称       | 接口描述       |
| -------------------- | -------------------- |
| [ITcgSdk.start(ServerSession)](#ITcgSdk.start(ServerSession)) | 启动云游戏     |
| [ITcgSdk.stop()](#ITcgSdk.stop())         | 停止云游戏     |
| [ITcgSdk.reconnect()](#ITcgSdk.reconnect())                  | 重新连接       |
| [ITcgSdk.replace(pcSurfaceGameView)](#ITcgSdk.replace(pcSurfaceGameView))      | 替换 SDK 的游戏视图               |
| [ITcgSdk.registerTcgListener(listener)](#ITcgSdk.registerTcgListener(listener)) | 设置生命周期回调监听              |
| [ITcgSdk.unRegisterTcgListener(listener)](#ITcgSdk.unRegisterTcgListener(listener)) | 注销生命周期回调监听              |
| [ITcgListener](#ITcgListener)     | TcgSdk 生命周期回调，TcgSdk 在调用 start 接口之后进行初始化 |


### 鼠标键盘控制相关接口

| 接口名称       | 接口描述  |
| :------------------- | :--------------- |
| [ITcgSdk.sendShiftKey(down,callback)](#ITcgSdk.sendShiftKey(down,callback)) | 发送 shift 键     |
| [ITcgSdk.sendMouseLeft(down,callback)](#ITcgSdk.sendMouseLeft(down,callback)) | 鼠标左键控制      |
| [ITcgSdk.sendMouseMiddle(down,callback)](#ITcgSdk.sendMouseMiddle(down,callback)) | 鼠标中键控制      |
| [ITcgSdk.sendMouseRight(down,callback)](#ITcgSdk.sendMouseRight(down,callback)) | 鼠标右键控制      |
| [ITcgSdk.sendMouseScroll(delta,callback)](#ITcgSdk.sendMouseScroll(delta,callback)) | 鼠标滚轮控制      |
| [ITcgSdk.sendRawEvent(event,callback)](#ITcgSdk.sendRawEvent(event,callback)) | 发送按键事件      |
| [ITcgSdk.pasteInputBox(content,callback)](#ITcgSdk.pasteInputBox(content,callback)) | 发送文字到云端输入框                 |
| [ITcgSdk.sendKeyboardEvent(keycode,down,callback)](#ITcgSdk.sendKeyboardEvent(keycode,down,callback)) | 发送键盘事件      |
| [ITcgSdk.sendGamePadConnected(callback)](#ITcgSdk.sendGamePadConnected(callback)) | 告知远端设备已连接上手柄             |
| [ITcgSdk.sendGamePadDisconnected(callback)](#ITcgSdk.sendGamePadDisconnected(callback)) | 告知远端设备手柄已经断开             |
| [ITcgSdk.resetRemoteCapsLock(callback)](#ITcgSdk.resetRemoteCapsLock(callback)) | 重置云端大小写状态为小写             |
| [ITcgSdk.clearRemoteKeys(callback)](#ITcgSdk.clearRemoteKeys(callback)) | 重置云端按键状态                     |
| [ITcgSdk.registerIDleListener(listener)](#ITcgSdk.registerIDleListener(listener)) | 注册空闲状态监听器，监听用户空闲状态 |
| [ITcgSdk.unRegisterIDleListener(listener)](#ITcgSdk.unRegisterIDleListener(listener)) | 注销空闲状态监听器                   |
| [ITcgSdk.setCursorStyle(style,callback)](#ITcgSdk.setCursorStyle(style,callback)) | 设置云端鼠标样式          |


### 运行状态监控接口

| 接口名称       | 接口描述                 |
| :------------------- | :----------------------- |
| [ITcgSdk.registerJitterListener(listener)](#ITcgSdk.registerJitterListener(listener)) | 注册网络抖动状态回调监听 |
| [ITcgSdk.unRegisterJitterListener(listener)](#ITcgSdk.unRegisterJitterListener(listener)) | 注销网络抖动状态回调监听 |
| [ITcgSdk.registerLowFPSListener(listener)](#ITcgSdk.registerLowFPSListener(listener)) | 注册低帧率回调监听       |
| [ITcgSdk.unRegisterLowFPSListener(listener)](#ITcgSdk.unRegisterLowFPSListener(listener)) | 注销低帧率回调监听       |
| [ITcgSdk.registerReconnectListener(listener)](#ITcgSdk.registerReconnectListener(listener)) | 注册重连监听器           |
| [ITcgSdk.unRegisterReconnectListener(listener)](#ITcgSdk.unRegisterReconnectListener(listener)) | 注销重连监听器           |
| [ITcgSdk.registerStatsListener(listener)](#ITcgSdk.registerStatsListener(listener)) | 注册性能数据回调监听     |
| [ITcgSdk.unRegisterStatsListener(listener)](#ITcgSdk.unRegisterStatsListener(listener)) | 注销性能数据回调监听     |

### 音视频控制接口

| 接口名称       | 接口描述        |
| -------------------- | -------------- |
| [ITcgSdk.pause(callback)](#ITcgSdk.pause(callback))          | 暂停画面传输    |
| [ITcgSdk.resume(callback)](#ITcgSdk.resume(callback))        | 恢复画面传输    |
| [ITcgSdk.setStreamProfile(fps,minBitrate,maxBitrate,unit,callback)](#ITcgSdk.setStreamProfile(fps,minBitrate,maxBitrate,unit,callback)) | 设置建议的帧率和码率，云端会根据网络情况动态调整                   |
| [ITcgSdk.setVolume(volume)](#ITcgSdk.setVolume(volume))      | 设置游戏音频 PCM 增益大小，默认1.0 |
| [ITcgSdk.setVolume(userID,volume)](#ITcgSdk.setVolume(userID,volume)) | 设置游戏音频 PCM 增益大小，默认1.0 |
| [ITcgSdk.setMicVolume(volume)](#ITcgSdk.setMicVolume(volume)) | 设置本地麦克风音量（多人云游场景） |
| [ITcgSdk.getVolume()](#ITcgSdk.getVolume())                  | 获取当前音频 PCM 增益              |
| [ITcgSdk.registerResolutionChangeListener(listener)](#ITcgSdk.registerResolutionChangeListener(listener)) | 注册视频图像宽高变化监听           |
| [ITcgSdk.unRegisterResolutionChangeListener(listener)](#ITcgSdk.unRegisterResolutionChangeListener(listener)) | 注销视频图像宽高变化监听           |
| [IResolutionChangeListener.onResolutionChange()](#IResolutionChangeListener.onResolutionChange()) | 视频图像宽高发生变化               |


### 游戏进程相关接口

| 接口名称       | 接口描述     |
| -------------------- | ------------------- |
| [IRTCResult](#IRTCResult) | 远程调用结果 |
| [ITcgSdk.gameRestart(callback)](#ITcgSdk.gameRestart(callback))  | 重启当前运行的游戏进程                  |
| [ITcgSdk.getLoginWindowStat(callback)](#ITcgSdk.getLoginWindowStat(callback)) | 查询当前窗口是否支持自动登录功能        |
| [ITcgSdk.getInputMethodStat(callback)](#ITcgSdk.getInputMethodStat(callback)) | 查询云端输入法大小写状态                |
| [ITcgSdk.loginHelper(account,password,callback)](#ITcgSdk.loginHelper(account,password,callback)) | 辅助登录,到远端游戏登录窗口输入账号密码 |
| [ITcgSdk.registerGameProcessLaunchListener(listener)](#ITcgSdk.registerGameProcessLaunchListener(listener)) | 注册远端游戏进程启动回调监听            |
| [ITcgSdk.registerGameStatusListener(listener)](#ITcgSdk.registerGameStatusListener(listener)) | 注册游戏启动状态回调                    |
| [ITcgSdk.unRegisterGameStatusListener(listener)](#ITcgSdk.unRegisterGameStatusListener(listener)) | 注销游戏启动状态回调                    |
| [ITcgSdk.registerGameStatusListener(listener)](#ITcgSdk.registerGameStatusListener(listener)) | 注册游戏启动状态回调                    |
| [ITcgSdk.unRegisterGameProcessLaunchListener(listener)](#ITcgSdk.unRegisterGameProcessLaunchListener(listener)) | 注销远端游戏进程启动回调监听            |
| [ITcgSdk.registerRemoteLoginHelperListener(listener)](#ITcgSdk.registerRemoteLoginHelperListener(listener)) | 注册云 API 自动登录结果监听器           |
| [ITcgSdk.unRegisterRemoteLoginHelperListener(listener)](#ITcgSdk.unRegisterRemoteLoginHelperListener(listener)) | 注销云 API 自动登录结果监听器           |
| [ITcgSdk.registerGameArchiveListener(listener)](#ITcgSdk.registerGameArchiveListener(listener)) | 注册存档(加载及保存)监听器                    |
| [ITcgSdk.unRegisterGameArchiveListener(listener)](#ITcgSdk.unRegisterGameArchiveListener(listener)) | 注销存档(加载及保存)监听器    |

### 调试及日志相关接口

| 接口名称    | 接口描述    |
| --------- | ------------------ |
| ITcgSdk.setLogHandler(logger) | 设置日志回调函数，便于外部获取详细日志 |
| GameView.enableDebugView()    | 是否开启调试视图    |

### 云端桌面相关接口

| 接口名称       | 接口描述    |
| -------------------- | ---------- |
| [ITcgSdk.registerRemoteDesktopChangeListener(listener)](#ITcgSdk.registerRemoteDesktopChangeListener(listener))        | 注册远端桌面变化监听           |
| [ITcgSdk.unRegisterRemoteDesktopChangeListener(listener)](#ITcgSdk.unRegisterRemoteDesktopChangeListener(listener))      | 注销远端桌面变化监听           |
| [ITcgSdk.registerCursorVisibilityChangeListener(listener))](#ITcgSdk.registerCursorVisibilityChangeListener(listener))     | 注册远端设备光标可见性回调监听 |
| [ITcgSdk.unRegisterCursorVisibilityChangeListener(listener)](#ITcgSdk.unRegisterCursorVisibilityChangeListener(listener))   | 注销远端设备光标可见性回调监听 |
| ITcgSdk.checkCursorVisibility()   | 查询鼠标可见性                 |
| [ITcgSdk.checkCursorPos(listener)](#ITcgSdk.checkCursorPos(listener))  | 查询云端鼠标位置               |
| [ITcgSdk.unRegisterRemoteCursorPosListener(listener)](#ITcgSdk.unRegisterRemoteCursorPosListener(listener))          | 注销云端鼠标位置监听器         |
| [ITcgSdk.unRegisterRemoteInputStatusListener(listener)](#ITcgSdk.unRegisterRemoteInputStatusListener(listener))        | 注册云端输入可用性回调监听器   |
| [ITcgSdk.registerCursorBitmapListener(listener)](#ITcgSdk.registerCursorBitmapListener(listener))               | 监听获取鼠标图片               |
| [ITcgSdk.unRegisterCursorBitmapListener(listener)](#ITcgSdk.unRegisterCursorBitmapListener(listener))             | 注销获取鼠标图片监听           |
| [ITcgSdk.registerRemoteInputStatusListener(listener)](#ITcgSdk.registerRemoteInputStatusListener(listener))          | 注册云端输入可用性回调监听器   |
| [ITcgSdk.registerHitInputBoxListener(listener)](#ITcgSdk.registerHitInputBoxListener(listener)) | 注册远端设备输入框回调监听     |
| [ITcgSdk.unRegisterHitInputListener(listener)](#ITcgSdk.unRegisterHitInputListener(listener)) | 注销远端设备输入框回调监听     |
| [ITcgSdk.registerHitInputBoxListener2(listener)](#ITcgSdk.registerHitInputBoxListener2(listener)) | 注册远端设备输入框回调监听     |
| [ITcgSdk.unRegisterHitInputListener2(listener)](#ITcgSdk.unRegisterHitInputListener2(listener)) | 注销远端设备输入框回调监听     |

### 触控操作接口

| 接口名称       | 接口描述      |
| -------------------- | ------------------- |
| [CursorType.TouchClickKey](#CursorType.TouchClickKey)        | 当鼠标类型为 TOUCH 和 RELATIVE_TOUCH 时，触发点击的按键类型 |
| [GameView.setTouchClickKey(TouchClickKey)](#GameView.setTouchClickKey(TouchClickKey)) | 设置鼠标类型使用的按键           |
| [GameView.enableScaling(enable)](#GameView.enableScaling(enable)) | 是否允许双指缩放游戏画面         |
| [GameView.enableScaling(enable,min,max)](#GameView.enableScaling(enable,min,max)) | 是否允许双指缩放游戏画面         |
| GameView.resetScaling()           | 重置游戏画面缩放大小             |
| [GameView.setPinchOffset(rect)](#GameView.setPinchOffset(rect)) | 设置缩放时画面边框的偏移大小     |
| [GameView.handleMotion(enable)](#GameView.handleMotion(enable)) | 让游戏视图处理手势动作           |
| [GameView.setMoveSensitivity(value)](#GameView.setMoveSensitivity(value)) | 设置鼠标灵敏度                   |
| GameView.getMoveSensitivity()     | 返回已经设置的鼠标灵敏度         |
| GameView.getCurrentCursorType()   | 当前设置的鼠标模式               |
| [GameView.setCursorType(mode)](#GameView.setCursorType(mode)) | 设置鼠标模式                     |
| [GameView.setScaleType(mode)](#GameView.setScaleType(mode))  | 设置画面显示模式                 |
| [GameView.setOnPinchZoomListener(listener)](#GameView.setOnPinchZoomListener(listener)) | 监听双指缩放操作                 |


### 多人云游接口

| 接口名称       | 接口描述       |
| -------------------- | -------------------- |
| ITcgSdk.supportMultiPlayer()      | 返回多人云游操作实例              |
| [IMultiPlayer.apply(userID,role,seatIndex,result)](#IMultiPlayer.apply(userID,role,seatIndex,result)) | 观察者申请切换角色和席位                |
| [IMultiPlayer.change(userID,role,seatIndex,result)](#IMultiPlayer.change(userID,role,seatIndex,result)) | 房主切换观察者或玩家的角色和席位                |
| [IMultiPlayer.syncSeatInfo()](#IMultiPlayer.syncSeatInfo())  | 获取所有席位信息（玩家及观察者），结果会通过 onSeatChanged 通知 |
| [IMultiPlayer.registerSeatChangeListener(ISeatListener)](#IMultiPlayer.registerSeatChangeListener(ISeatListener)) | 注册席位信息监听器                |
| [IMultiPlayer.unRegisterSeatChangeListener(ISeatListener)](#IMultiPlayer.unRegisterSeatChangeListener(ISeatListener)) | 注销席位信息监听器                |

### 数据通道交互接口

| 接口名称       | 接口描述   |
| -------------------- | ----------------- |
| [ITcgSdk.createDataChannel(port,listener)](#ITcgSdk.createDataChannel(port,listener)) |创建一个可以和云端应用交互的数据通道     |
| [IDataChannel.send(data)](#IDataChannel.send(data)) |调用该接口给远端 UDP 端口发送数据     |
| [IDataChannel.close()](#IDataChannel.close())        | 关闭数据通道       |

### 其他说明

| 说明名称    | 描述                     |
| --------- | ------------------------ |
| [TcgErrorType](#TcgErrorType) | 错误码定义               |
| [GameView](#GameView)         | 该视图代理了远程设备视图 |
| [CursorType](#CursorType)     | 鼠标类型                 |

## 生命周期相关接口

[](id:ITcgSdk.start(ServerSession))
### ITcgSdk.start(ServerSession)

启动云游戏。

| 参数    | 类型          | 返回值 | 描述      |
| ------- | ------------- | ------ | --------------- |
| session | ServerSession | 无     | Server Session，从云 API 获取后需要做一次 Base64.decode |

[](id:ITcgSdk.stop())
### ITcgSdk.stop()

停止云游戏。

[](id:ITcgSdk.reconnect())
### ITcgSdk.reconnect()

重新连接。

[](id:ITcgSdk.replace(pcSurfaceGameView))
### ITcgSdk.replace(pcSurfaceGameView)

替换游戏视图，调用后原游戏视图不会释放，若不再使用需手动释放。 

> ! 如果传入的游戏视图已被释放, 该调用会抛 IllegalStateException 异常。

| 参数     | 类型           | 返回值 | 描述                    |
| -------- | -------------- | ------ | ----------------------- |
| pcSurfaceGameView | SimpleGameView | 无     | 游戏视图，可传 null |

[](id:ITcgSdk.registerTcgListener(listener))
### ITcgSdk.registerTcgListener(listener)  

设置生命周期回调监听。

| 参数     | 类型         | 返回值 | 描述          |
| -------- | ------------ | ------ | ------------------- |
| listener | ITcgListener | 无     | TcgSdk 生命周期回调，TcgSdk 在调用 start 接口之后进行初始化 |

[](id:ITcgSdk.unRegisterTcgListener(listener))
### ITcgSdk.unRegisterTcgListener(listener)

注销生命周期回调监听。

[](id:ITcgListener)
### ITcgListener

TcgSdk 生命周期回调，TcgSdk 在调用 start 接口之后进行初始化。

| 接口名称       | 接口描述           |
| -------------------- | ------------------ |
| [ITcgListener.onInitSuccess(clientSession)](#ITcgListener.onInitSuccess(clientSession)) | SDK 初始化成功回调 |
| [ITcgListener.onInitFailure(errorCode)](#ITcgListener.onInitFailure(errorCode)) | 初始化失败         |
| [ITcgListener.onConnectionFailure(errorCode,errorMsg)](#ITcgListener.onConnectionFailure(errorCode,errorMsg)) | 连接失败回调       |
| ITcgListener.onConnectionSuccess()        | 连接成功           |
| ITcgListener.onConnectionTimeout()        | 连接超时           |
| ITcgListener.onDrawFirstFrame()   | 首帧绘制时机       |

[](id:ITcgListener.onInitSuccess(clientSession))
#### ITcgListener.onInitSuccess(clientSession)

SDK 初始化成功回调。

| 参数          | 类型   | 描述                                                         |
| ------------- | ------ | ------------------------------------------------------------ |
| clientSession | String | ClientSession 客户端会话， 其内容较长, 可能会超出 logcat 输出限制 |


[](id:ITcgListener.onInitFailure(errorCode))
#### ITcgListener.onInitFailure(errorCode)

初始化失败回调。

| 参数      | 类型   | 描述   |
| --------- | ------------- | ------ |
| errorCode | [TcgErrorType](#TcgErrorType) int | 错误码 |

[](id:ITcgListener.onConnectionFailure(errorCode,errorMsg))
#### ITcgListener.onConnectionFailure(errorCode,errorMsg)

连接失败回调。

| 参数      | 类型   | 描述     |
| --------- | ------------- | -------- |
| errorCode | [TcgErrorType](#TcgErrorType) int | 错误码   |
| errorMsg  | String         | 错误消息 |

## 鼠标键盘控制相关接口
所有按键事件发送接口（包括 sendGamePadConnected）必须在 ITcgListener.onConnectionSuccess() 回调发生之后调用。
[](id:ITcgSdk.sendShiftKey(down,callback))

### ITcgSdk.sendShiftKey(down,callback)

初始化失败回调。

| 参数     | 类型       | 描述       |
| -------- | ---------- | --------- |
| down     | boolean    | true 表示按下，false 表示抬起 |
| callback | IRTCResult | callback 远端接口调用结果     |

[](id:ITcgSdk.sendMouseLeft(down,callback))
### ITcgSdk.sendMouseLeft(down,callback)

鼠标左键控制。

| 参数     | 类型       | 描述       |
| -------- | ---------- | --------- |
| down     | boolean    | true 表示按下，false 表示抬起 |
| callback | IRTCResult | callback 远端接口调用结果     |

[](id:ITcgSdk.sendMouseMiddle(down,callback))
### ITcgSdk.sendMouseMiddle(down,callback)

鼠标中键控制。

| 参数     | 类型       | 描述       |
| -------- | ---------- | --------- |
| down     | boolean    | true 表示按下，false 表示抬起 |
| callback | IRTCResult | callback 远端接口调用结果     |

[](id:ITcgSdk.sendMouseRight(down,callback))
### ITcgSdk.sendMouseRight(down,callback)

鼠标右键控制。

| 参数     | 类型       | 描述       |
| -------- | ---------- | --------- |
| down     | boolean    | true 表示按下，false 表示抬起 |
| callback | IRTCResult | callback 远端接口调用结果     |

[](id:ITcgSdk.sendMouseScroll(delta,callback))
### ITcgSdk.sendMouseScroll(delta,callback)

鼠标滚轮控制。

| 参数     | 类型       | 描述    |
| -------- | ---------- | -------- |
| delta    | int        | 偏移值                    |
| callback | IRTCResult | callback 远端接口调用结果 |

[](id:ITcgSdk.sendRawEvent(event,callback))
### ITcgSdk.sendRawEvent(event,callback)

发送底层事件。

<table id="event">
<thead><tr><th colspan=2>Parameters:event 对象</th><th>结构说明</th>
</tr>
</thead>
<tbody><tr>
<td colspan=2>鼠标偏移（用于无边框限制的鼠标移动事件）</td>
<td><code>{ type: "mousedeltamove",x: Number,y: Number }</code>，x、y 坐标值均为整数</td>
</tr><tr>
<td colspan=2>鼠标移动</td>
<td><code>{ type: "mousemove",x: Number,y: Number }</code>，x、y 坐标值均为整数</td>
</tr><tr>
<td colspan=2>鼠标左键点击</td>
<td><code>{ type: "mouseleft",down: true/false }</code></td>
</tr><tr>
<td colspan=2>鼠标右键点击</td>
<td><code>{ type: "mouseright",down: true/false }</code></td>
</tr><tr>
<td colspan=2>鼠标滚动</td>
<td><code>{ type: "mousescroll",delta: Number }</code></td>
</tr><tr>
<td colspan=2>鼠标滚轮单击</td>
<td><code>{ type: "mousemiddle",down: true/false }</code></td>
</tr><tr>
<td colspan=2>键盘按键事件</td>
<td><code>{ type: "keyboard",key: Integer,down: true/false }</code></td>
</tr><tr>
<td rowspan=12>手柄事件</td>
<td>手柄连接事件</td>
<td><code>{ type: "gamepadconnect" }</code>，发送操作按键前必须先发送这个事件</td>
</tr><tr>
<td>手柄断开事件</td>
<td><code>{ type: "gamepaddisconnect" }</code></td>
</tr><tr>
<td>手柄按键事件</td>
<td><code>{ type: "gamepadkey",key: Number,down: true/false }</code><ul style="margin:0">
    <li>方向键事件值：
        向上键值为<code>0x01</code>，
        向下键值为<code>0x02</code>，
        向左键值为<code>0x04</code>，
        向右键值为<code>0x08</code></li>
    <li>按键事件值：
        X 键值为<code>0x4000</code>，
        Y 键值为<code>0x8000</code>，
        A 键值为<code>0x1000</code>，
        B 键值为<code>0x2000</code></li>
    <li>select 事件值：
        键值为<code>0x20</code></li>
    <li>start 事件值：
        键值为<code>0x104</code></li></ul></td>
</tr><tr>
<td>手柄左摇杆事件</td>
<td><code>{ type: "axisleft",x: [-32767,32767],y: [-32767,32767] }</code>，原浮点数值为（-1,1），实际返回原浮点数值 * 32767</td>
</tr><tr>
<td>手柄右摇杆事件</td>
<td><code>{ type: "axisright",x: [-32767,32767],y: [-32767,32767] }</code>，原浮点数值为（-1,1），实际返回原浮点数值 * 32767</td>
</tr><tr>
<td>手柄左触发键（L1）事件</td>
<td><code>{type: "gamepadkey",key: 0x100,down: true/false}</code></td>
</tr><tr>
<td>手柄右触发键（R1）事件</td>
<td><code>{type: "gamepadkey",key: 0x200,down: true/false}</code></td>
</tr><tr>
<td>手柄左触发键（L2）事件</td>
<td><code>{ type: "lt",x: [0,255],down: true/false }</code>，原浮点数值为（0~1），实际返回原浮点数值 * 255</td>
</tr><tr>
<td>手柄右触发键（R2）事件</td>
<td><code>{ type: "rt",x: [0-255],down: true/false }</code>，原浮点数值为（0~1），实际返回原浮点数值 * 255</td>
</tr><tr>
<td>手柄左摇杆垂直按下（L3）事件</td>
<td><code>{type: "gamepadkey",key: 0x80,down: true/false}</code></td>
</tr><tr>
<td>手柄右摇杆垂直按下（R3）事件</td>
<td><code>{type: "gamepadkey",key: 0x40,down: true/false}</code></td>
</tr>
</tbody></table>




[](id:ITcgSdk.pasteInputBox(content,callback))
### ITcgSdk.pasteInputBox(content,callback)

发送文字到云端输入框。

> ! 这个接口需要云端游戏或程序支持剪贴板输入功能。

| 参数     | 类型       | 描述    |
| -------- | ---------- | -------- |
| content  | String     | 需要填入输入框的内容      |
| callback | IRTCResult | callback 远端接口调用结果 |

[](id:ITcgSdk.sendKeyboardEvent(keycode,down,callback))
### ITcgSdk.sendKeyboardEvent(keycode,down,callback)

发送键盘事件。

| 参数     | 类型       | 描述       |
| -------- | ---------- | --------- |
| keycode  | int        | 按键值     |
| down     | boolean    | true 表示按下，false 表示抬起 |
| callback | IRTCResult | callback 远端接口调用结果     |

[](id:ITcgSdk.sendGamePadConnected(callback))
### ITcgSdk.sendGamePadConnected(callback)
告知远端设备已连接上手柄。

| 参数     | 类型       | 描述       |
| -------- | ---------- | --------- |
| callback | IRTCResult | callback 远端接口调用结果     |

[](id:ITcgSdk.sendGamePadDisconnected(callback))
### ITcgSdk.sendGamePadDisconnected(callback)	
告知远端设备手柄已经断开。

| 参数     | 类型       | 描述       |
| -------- | ---------- | --------- |
| callback | IRTCResult | callback 远端接口调用结果     |

[](id:ITcgSdk.resetRemoteCapsLock(callback))
### ITcgSdk.resetRemoteCapsLock(callback)

重置云端大小写状态为小写。

| 参数     | 类型       | 描述    |
| -------- | ---------- | -------- |
| callback | IRTCResult | callback 远端接口调用结果 |

[](id:ITcgSdk.clearRemoteKeys(callback))
### ITcgSdk.clearRemoteKeys(callback)

重置云端按键状态。

| 参数     | 类型       | 描述    |
| -------- | ---------- | -------- |
| callback | IRTCResult | callback 远端接口调用结果 |


[](id:ITcgSdk.setCursorStyle(style,callback))
### ITcgSdk.setCursorStyle(style,callback)

设置云端鼠标样式

| 参数     | 类型       | 描述    |
| -------- | ---------- | -------- |
| style | CursorStyle | 需要的鼠标样式 |
| callback | IRTCResult | callback 远端接口调用结果 |

[](id:ITcgSdk.registerIDleListener(listener))
### ITcgSdk.registerIDleListener(listener)  

注册空闲状态监听器，监听用户空闲状态。

| 参数     | 类型          | 返回值 | 描述          |
| -------- | ------------- | ------ | ------------------- |
| listener | IIDleListener | 无     | TcgSdk 生命周期回调，TcgSdk 在调用 start 接口之后进行初始化 |

[](id:IIDleListener.onIdle())
#### IIDleListener.onIdle()

操作空闲回调，当用户在5分钟（默认）内无任何操作时回调该函数。无操作的触发时间可以通过 Builder 修改。

[](id:ITcgSdk.unRegisterIDleListener(listener))
### ITcgSdk.unRegisterIDleListener(listener)

注销空闲状态监听器。


## 运行状态监控接口

[](id:ITcgSdk.registerJitterListener(listener))
### ITcgSdk.registerJitterListener(listener)  

设置生命周期回调监听。

| 参数     | 类型            | 返回值 | 描述             |
| -------- | --------------- | ------ | ---------------- |
| listener | IJitterListener | 无     | 网络抖动状态监听 |

[](id:ITcgSdk.unRegisterJitterListener(listener))
### ITcgSdk.unRegisterJitterListener(listener)

注销生命周期回调监听。

####  IJitterListener.onJitter(rtt)

网络抖动状态监听。

| 参数 | 类型 | 描述          |
| ---- | ---- | -------------------- |
| rtt  | long | 客户端发起到收到远端响应的时间间隔（ms） |

[](id:ITcgSdk.registerLowFPSListener(listener))
### ITcgSdk.registerLowFPSListener(listener)  

设置生命周期回调监听。

| 参数     | 类型            | 返回值 | 描述             |
| -------- | --------------- | ------ | ---------------- |
| listener | ILowFPSListener | 无     | 出现低帧率时回调 |

[](id:ITcgSdk.unRegisterLowFPSListener(listener))
### ITcgSdk.unRegisterLowFPSListener(listener)

注销生命周期回调监听。

####  ILowFPSListener.onLowFps()

出现低帧率时回调，目前低帧率的判定标准是：连续5秒帧率都低于25帧/秒则认为是低帧率。

[](id:ITcgSdk.registerReconnectListener(listener))
### ITcgSdk.registerReconnectListener(listener)  

设置重连监听器。

| 参数     | 类型               | 返回值 | 描述       |
| -------- | ------------------ | ------ | ---------- |
| listener | IReconnectListener | 无     | 重连监听器 |

[](id:ITcgSdk.unRegisterReconnectListener(listener))
### ITcgSdk.unRegisterReconnectListener(listener)

注销重连监听器。

####  IReconnectListener.onReconnecting()

当出现重连时回调该函数。

| 参数  | 类型 | 描述                  |
| ----- | ---- | --------------------- |
| count | int  | SDK 启动后第 N 次重连 |

[](id:ITcgSdk.registerStatsListener(listener))
### ITcgSdk.registerStatsListener(listener)  

设置性能数据回调监听。

| 参数     | 类型           | 返回值 | 描述             |
| -------- | -------------- | ------ | ---------------- |
| listener | IStatsListener | 无     | 性能数据回调监听 |

[](id:ITcgSdk.unRegisterStatsListener(listener))
### ITcgSdk.unRegisterStatsListener(listener)

注销性能数据回调监听。

#### IStatsListener.onStats()

回调性能相同统计数据。

| 参数      | 类型                    | 描述       |
| --------- | ----------------------- | ---------- |
| perfValue | [PerfValue](#PerfValue) | 性能数据   |
| version   | String                  | 服务端版本 |
| region    | String                  | 服务器地区 |
| serverIp  | String                  | 服务器 IP   |

[](id:PerfValue)
#### PerfValue

| 参数           | 类型 | 描述               |
| -------------- | ---- | ------------------ |
| rtt            | long | 心跳往返延迟       |
| videoBitrate   | long | 视频码率           |
| packetsLost    | long | 丢弃的包个数       |
| averageBitRate | long | 视频平均码率 bit/s |

## 音视频控制接口

[](id:ITcgSdk.pause(callback))
### ITcgSdk.pause(callback)

暂停画面传输。

| 参数     | 类型       | 描述             |
| -------- | ---------- | ---------------- |
| callback | IRTCResult | 远端接口调用结果 |

[](id:ITcgSdk.resume(callback))
### ITcgSdk.resume(callback)

恢复画面传输。

| 参数     | 类型       | 描述             |
| -------- | ---------- | ---------------- |
| callback | IRTCResult | 远端接口调用结果 |

[](id:ITcgSdk.setStreamProfile(fps,minBitrate,maxBitrate,unit,callback))
### ITcgSdk.setStreamProfile(fps,minBitrate,maxBitrate,unit,callback)

设置建议的帧率和码率
注意: 该接口设置的仅是建议值, 云端会根据实际网络情况动态调整.

| 参数       | 类型    | 描述       |
| ---------- | ------ | ---------------- |
| fps        | int     | 建议帧率，范围[10，60]，默认60      |
| minBitrate | int     | 建议最小码率，范围[1Mbps,15Mbps]，默认1M，具体值取决与码率单位 |
| maxBitrate | int     | 建议最大码率，范围[1Mbps,15Mbps]，默认10M，具体值取决与码率单位  |
| unit       | [BitrateUnit](BitrateUnit) | callback 远端接口调用结果     |

[](id:BitrateUnit)
#### BitrateUnit

码率单位。

| 类型 | 描述          |
| ---- | ------------- |
| MB   | 码率单位 Mbps |
| KB   | 码率单位 Kbps |

[](id:ITcgSdk.setVolume(volume))
### ITcgSdk.setVolume(volume)

设置游戏音频 PCM 增益大小，默认1.0。

| 参数   | 类型  | 描述                |
| ------ | ----- | --------- |
| volume | float | [0,10]之间的浮点数，大于１时可能会导致声音失真 |

[](id:ITcgSdk.setVolume(userID,volume))
### ITcgSdk.setVolume(userID,volume)

针对特定用户（多人云游场景）设置音频 PCM 增益大小，默认1.0。

| 参数   | 类型   | 描述                |
| ------ | ------ | --------- |
| userID | String | 需要调整音频 PCM 增益的用户ID                    |
| volume | float  | [0,10]之间的浮点数，大于１时可能会导致声音失真 |

[](id:ITcgSdk.setMicVolume(volume))
### ITcgSdk.setMicVolume(volume)

设置本地麦克风音量（多人云游场景）。

| 参数   | 类型  | 描述                |
| ------ | ----- | --------- |
| volume | float | [0,10]之间的浮点数，大于１时可能会导致声音失真 |

[](id:ITcgSdk.getVolume())
### ITcgSdk.getVolume()

获取当前音频 PCM 增益。

[](id:ITcgSdk.registerResolutionChangeListener(listener))
### ITcgSdk.registerResolutionChangeListener(listener)  

注册视频图像宽高变化监听。

| 参数     | 类型    | 返回值 | 描述                 |
| -------- | -------- | ------ | -------------------- |
| listener | IResolutionChangeListener | 无     | 视频图像宽高变化监听 |

[](id:ITcgSdk.unRegisterResolutionChangeListener(listener))
### ITcgSdk.unRegisterResolutionChangeListener(listener)

注销视频图像宽高变化监听。

[](id:IResolutionChangeListener.onResolutionChange())
### IResolutionChangeListener.onResolutionChange()

视频图像宽高发生变化。

| 参数      | 类型 | 描述       |
| --------- | ---- | ----------------- |
| oldWidth  | int  | 变化前的视频图像宽度，首次渲染该值为0 |
| oldHeight | int  | 变化前的视频图像高度，首次渲染该值为0 |
| newWidth  | int  | 变化后的视频图像宽度                  |
| newHeight | int  | 变化后的视频图像高度                  |

## 游戏进程相关接口

[](id:IRTCResult)
### IRTCResult
远程调用结果。

| 接口名称 | 接口描述   |
| ------------------------ | ------------- |
| IRTCResult.onFailed(msg) | 远程调用失败            |
| IRTCResult.onTimeout()   | 调用超时                |
| IRTCResult.onSuccess()   | 仅表示接口调用本身执行成功（收到了远端设备的响应） |

[](id:ITcgSdk.gameRestart(callback))
### ITcgSdk.gameRestart(callback)

重启当前运行的游戏进程。

| 参数     | 类型    | 描述             |
| -------- | -------- | ---------------- |
| callback | [IRTCResult](#IRTCResult) | 远端接口调用结果 |

[](id:ITcgSdk.getLoginWindowStat(callback))
### ITcgSdk.getLoginWindowStat(callback)

查询当前窗口是否支持自动登录功能。

| 参数     | 类型 | 描述 |
| -------- | -------- | -------- |
| callback | [IAutoLoginWindowStatCallback](#IAutoLoginWindowStatCallback) | 是否支持自动登录功能回调 |

[](id:IAutoLoginWindowStatCallback)
#### IAutoLoginWindowStatCallback

| 接口名称  | 接口描述  |
| -------- | -------- |
| IRTCResult.onFailed(msg) | 远程调用失败 |
| IRTCResult.onTimeout() | 调用超时 |
| IRTCResult.onSuccess() | 仅表示接口调用本身执行成功（收到了远端设备的响应） |
| IRTCResult.onLoginWindowStat(supportAutoLogin) | 当前窗口是否支持自动登录功能 |

[](id:ITcgSdk.getInputMethodStat(callback))
### ITcgSdk.getInputMethodStat(callback)

查询云端输入法大小写状态。

| 参数     | 类型 | 描述                 |
| -------- | -------- | -------- |
| callback | [IInputMethodCallback](#IInputMethodCallback) | 输入法大小写状态回调 |

[](id:IInputMethodCallback)
#### IInputMethodCallback

| 接口名称  | 接口描述                |
| ---------------- | ------------- |
| IRTCResult.onFailed(msg)             | 远程调用失败            |
| IRTCResult.onTimeout()               | 调用超时                |
| IRTCResult.onSuccess()               | 仅表示接口调用本身执行成功（收到了远端设备的响应） |
| IRTCResult.onInputmethod(isCapsLock) | 云端输入法状态回调      |

[](id:ITcgSdk.loginHelper(account,password,callback))
### ITcgSdk.loginHelper(account,password,callback)

辅助登录，到远端游戏登录窗口输入账号密码。

> ? 该接口依赖于云端配置，若回调不生效需要和云游团队确认配置是否开启。

| 参数     | 类型       | 描述             |
| -------- | ---------- | ---------------- |
| account  | IRTCResult | 登录的账号       |
| password | IRTCResult | 登录的密码       |
| callback | IRTCResult | 远端接口调用结果 |

[](id:ITcgSdk.registerGameProcessLaunchListener(listener))
### ITcgSdk.registerGameProcessLaunchListener(listener)  

注册远端游戏进程启动回调监听。

> ? 该接口依赖于云端配置，若回调不生效需要和云游团队确认配置是否开启。

| 参数     | 类型    | 返回值 | 描述             |
| -------- | ------ | ------ | ---------------- |
| listener | IGameProcessLaunchListener | 无     | 游戏进程启动监听 |

[](id:ITcgSdk.unRegisterGameProcessLaunchListener(listener))
### ITcgSdk.unRegisterGameProcessLaunchListener(listener)

注销远端游戏进程启动回调监听。

[](id:IGameProcessLaunchListener.onGameProcessLaunched(launchStart,launchFinished))
#### IGameProcessLaunchListener.onGameProcessLaunched(launchStart,launchFinished)

| 参数           | 类型 | 描述                |
| -------------- | ---- | ------------------- |
| launchStart    | long | 游戏开始启动时间 ms |
| launchFinished | long | 游戏启动完成时间 ms |

[](id:ITcgSdk.registerGameStatusListener(listener))

### ITcgSdk.registerGameStatusListener(listener)  

注册游戏启动状态回调。

| 参数     | 类型                 | 返回值 | 描述                 |
| -------- | -------------------- | ------ | -------------------- |
| listener | IGameStatusListener2 | 无     | 视频图像宽高变化监听 |

[](id:ITcgSdk.unRegisterGameStatusListener(listener))
### ITcgSdk.unRegisterGameStatusListener(listener)

注销游戏启动状态回调。


#### IGameStatusListener2.onGameStatus(userID,gameID,requestID,status)

| 参数      | 类型   | 描述           |
| --------- | ------ | -------------------- |
| userID    | String | 调用云 API 的 userID              |
| gameID    | String | 启动的当前游戏 ID                 |
| requestID | String | 请求唯一标识    |
| status    | String | <li/>0：启动游戏成功<li/>1：启动游戏失败<li/>2：游戏状态从未运行变成运行<li/>3：游戏状态从运行变成未运行 |

[](id:ITcgSdk.registerRemoteLoginHelperListener(listener))
### ITcgSdk.registerRemoteLoginHelperListener(listener)  

注册云 API 自动登录结果监听器。

| 参数     | 类型    | 返回值 | 描述    |
| -------- | ------ | ------ | -------- |
| listener | IRemoteLoginHelperListener | 无     | 云 API 自动登录结果监听器 |

[](id:ITcgSdk.unRegisterRemoteLoginHelperListener(listener))
### ITcgSdk.unRegisterRemoteLoginHelperListener(listener)

注销云 API 自动登录结果监听器。

#### IRemoteLoginHelperListener.onAutoLogin(userID,gameID,result)

| 参数   | 类型   | 描述      |
| ------ | ------ | -------- |
| userID | String | 执行自动登录的用户 ID        |
| gameID | String | 游戏 ID  |
| result | int    | **0**表示登录成，**-1**表示登录失败 |

[](id:ITcgSdk.registerGameArchiveListener(listener))
### ITcgSdk.registerGameArchiveListener(listener)

注册加载游戏存档回调。

| 参数     | 类型       | 返回值 | 描述                 |
| -------- | --------- | ------ | -------------------- |
| listener | IGameArchive.IArchiveListener | 无     | 视频图像宽高变化监听 |

[](id:ITcgSdk.unRegisterGameArchiveListener(listener))
### ITcgSdk.unRegisterGameArchiveListener(listener)  

注销加载游戏存档回调。

#### IGameArchive.IArchiveListener.onLoadGameArchive(status,userID,gameID,name,url,saveType,categoryID,long archiveSize,long loadedSize)  

加载存档回调。

| 参数        | 类型                     | 描述        |
| ----------- | -------------- | ---------- |
| status      | [GameArchiveLoadStatus](#GameArchiveLoadStatus) int | 存档加载状态                   |
| userID      | String                   | 云 API 传入的 userID           |
| gameID      | String                   | 游戏 ID     |
| name        | String                   | 存档文件名                     |
| url         | String                   | 存档下载地址                   |
| saveType    | String                   | Auto 自动存档，Normal 手动存档 |
| categoryID  | String                   | 分类标识    |
| archiveSize | long                     | 存档大小    |
| loadedSize  | long                     | 已下载的存档大小               |

[](id:GameArchiveLoadStatus)
#### GameArchiveLoadStatus

 存档加载状态定义。

| 状态定义            | 说明                 |
| ------------------- | -------------------- |
| SUCCESS             | 存档保存成功         |
| DOWNLOAD_FAILED     | 存档保存失败         |
| VERIFICATION_FAILED | 存档校验失败         |
| UNZIP_FAILED        | 存档解压失败         |
| OTHER_FAILED        | 下载存档出现其他异常 |
| DOWNLOADING         | 文件下载中           |


#### IGameArchive.IArchiveListener.onSaveGameArchive(status,userID,gameID,name,url,saveType,categoryID,long archiveSize,long loadedSize)

保存存档回调。

| 参数        | 类型                     | 描述        |
| ----------- | -------------- | ---------- |
| status      | [GameArchiveSaveStatus](#GameArchiveSaveStatus) int | 存档保存状态                   |
| userID      | String                   | 云 API 传入的 userID           |
| gameID      | String                   | 游戏 ID     |
| name        | String                   | 存档文件名                     |
| url         | String                   | 存档下载地址                   |
| saveType    | String                   | Auto 自动存档，Normal 手动存档 |
| categoryID  | String                   | 分类标识    |
| archiveSize | long                     | 存档大小    |
| loadedSize  | long                     | 已下载的存档大小               |

[](id:GameArchiveSaveStatus)
#### GameArchiveSaveStatus

 存档保存状态定义。

| 状态定义              | 说明      |
| --------------------- | ---------------- |
| SUCCESS               | 存档保存成功      |
| SAVE_FAILED           | 保存存档失败      |
| ZIP_FAILED            | 压缩存档失败      |
| OTHER_FAILED          | 存档保存出现其他异常                 |
| UPLOADING             | 存档上传中        |
| ARCHIVE_NOT_FOUND     | 没找到存档        |
| OPERATION_IS_FREQUENT | 存档操作太频繁    |
| PLAY_TIME_TOO_SHORT   | 玩游戏时间不够    |
| ARCHIVE_DISABLE       | 当前游戏没有启用存档功能             |
| INVALID_PARAM         | 参数错误，例如 gameId 或 userId 匹配 |
| BUSY                  | 上一个请求正在处理中                 |
| SKIP_ARCHIVE          | 切换存档时跳过存档                   |

## 云端桌面相关接口

[](id:ITcgSdk.registerRemoteDesktopChangeListener(listener))
### ITcgSdk.registerRemoteDesktopChangeListener(listener)

注册远端桌面变化监听

| 参数     | 类型                  | 返回值 | 描述               |
| -------- | --------------------- | ------ | ------------------ |
| listener | IDesktopListener | 无     | 远程桌面信息回调 |

[](id:ITcgSdk.unRegisterRemoteDesktopChangeListener(listener))
### ITcgSdk.unRegisterRemoteDesktopChangeListener(listener)

注销远端桌面变化监听

| 参数     | 类型                  | 返回值 | 描述               |
| -------- | --------------------- | ------ | ------------------ |
| listener | IDesktopListener | 无     | 远程桌面信息回调 |


[](id:IDesktopListener.onDesktop(left,top,width,height,cursorShowing))
#### IDesktopListener.onDesktop(left,top,width,height,cursorShowing)

回调远程桌面信息

| 参数                 | 类型    | 描述                     |
| -------------------- | ------- | ------------------------ |
| left        | int | 游戏画面在远程桌面的横坐标偏移       |
| top        | int | 游戏画面在远程桌面的纵坐标偏移       |
| width        | int | 游戏画面分辨率宽度       |
| height        | int | 游戏画面分辨率高度       |
| cursorShowing | boolean | 远端鼠标是否展示 |

[](id:ITcgSdk.registerCursorVisibilityChangeListener(listener))
### ITcgSdk.registerCursorVisibilityChangeListener(listener)

注册远端设备光标可见性回调监听。

[](id:ITcgSdk.unRegisterCursorVisibilityChangeListener(listener))
### ITcgSdk.unRegisterCursorVisibilityChangeListener(listener)

注销远端设备光标可见性回调监听

| 参数     | 类型                  | 返回值 | 描述               |
| -------- | --------------------- | ------ | ------------------ |
| listener | IRemoteCursorVisibleListener | 无     | 光标可见性变化时候调用的回调 |

[](id:IRemoteCursorVisibleListener.onCursorVisibility(visible))
#### IRemoteCursorVisibleListener.onCursorVisibility(visible)

远端光标可见性改变时回调。

| 参数                 | 类型    | 描述                     |
| -------------------- | ------- | ------------------------ |
| visible | boolean | 远端设备光标当前是否可见 |

[](id:ITcgSdk.checkCursorPos(listener))
### ITcgSdk.checkCursorPos(listener)

查询云端鼠标位置。

| 参数     | 类型                  | 返回值 | 描述               |
| -------- | --------------------- | ------ | ------------------ |
| listener | IRemoteCursorPosListener | 无     | 云端鼠标位置监听器 |

[](id:ITcgSdk.unRegisterRemoteCursorPosListener(listener))
### ITcgSdk.unRegisterRemoteCursorPosListener(listener)

注销云端鼠标位置监听器。

| 参数     | 类型                  | 返回值 | 描述               |
| -------- | --------------------- | ------ | ------------------ |
| listener | IRemoteCursorPosListener | 无     | 云端鼠标位置监听器 |

[](id:IRemoteCursorPosListener.onCursorPos(x,y))
#### IRemoteCursorPosListener.onCursorPos(x,y)

云端鼠标位置更新。

| 参数                 | 类型    | 描述                     |
| -------------------- | ------- | ------------------------ |
| x        | int | 云端鼠标位置 x      |
| y        | int | 云端鼠标位置 y      |


[](id:ITcgSdk.registerRemoteInputStatusListener(listener))
### ITcgSdk.registerRemoteInputStatusListener(listener)

注册云端输入可用性回调监听器

| 参数     | 类型                  | 返回值 | 描述               |
| -------- | --------------------- | ------ | ------------------ |
| listener | IRemoteInputStatusListener | 无     | 云端输入可用性回调监听器 |

[](id:ITcgSdk.unRegisterRemoteInputStatusListener(listener))
### ITcgSdk.unRegisterRemoteInputStatusListener(listener)

注销云端输入可用性回调监听器。

| 参数     | 类型                  | 返回值 | 描述               |
| -------- | --------------------- | ------ | ------------------ |
| listener | IRemoteInputStatusListener | 无     | 云端输入可用性回调监听器 |

[](id:IRemoteInputStatusListener.onInputAbility(disable))
#### IRemoteInputStatusListener.onInputAbility(disable)

当云端屏蔽或开启客户端输入（鼠标点击以及按键事件）时这个函数会被回调。

| 参数                 | 类型    | 描述                     |
| -------------------- | ------- | ------------------------ |
| disable | boolean | true 表示云端屏蔽了输入支持，false 表示未屏蔽 |

[](id:ITcgSdk.registerCursorBitmapListener(listener))
### ITcgSdk.registerCursorBitmapListener(listener)

注册云端鼠标图片监听器。

| 参数     | 类型                  | 返回值 | 描述               |
| -------- | --------------------- | ------ | ------------------ |
| listener | ICursorBitmapListener | 无     | 云端鼠标图片监听器 |

[](id:ITcgSdk.unRegisterCursorBitmapListener(listener) )
### ITcgSdk.unRegisterCursorBitmapListener(listener)  

注销云端鼠标图片监听器。

| 参数     | 类型                  | 返回值 | 描述               |
| -------- | --------------------- | ------ | ------------------ |
| listener | ICursorBitmapListener | 无     | 云端鼠标图片监听器 |

[](id:ICursorBitmapListener.onGetCursor(bitmap,hotspotx,hotspoty))
#### ICursorBitmapListener.onGetCursor(bitmap,hotspotx,hotspoty)

输入框状态点击回调。

| 参数                 | 类型    | 描述                     |
| -------------------- | ------- | ------------------------ |
| bitmap        | Bitmap | 获取到的图片       |
| hotspotx | int | 鼠标在点击后坐标应该偏移的横轴位置 |
| hotspoty | int | 鼠标在点击后坐标应该偏移的纵轴位置 |

[](id:ITcgSdk.registerHitInputBoxListener(listener))
### ITcgSdk.registerHitInputBoxListener(listener)

注册远端设备输入框回调监听。

> ? 该接口依赖服务器针对游戏的配置。

| 参数     | 类型                 | 返回值 | 描述    |
| -------- | -------------------- | ------ | ------ |
| listener | IHitInputBoxListener | 无     | 远端设备输入框选中状态回调 |

[](id:ITcgSdk.unRegisterHitInputListener(listener))
### ITcgSdk.unRegisterHitInputListener(listener)  

注销远端设备输入框回调监听。

[](id:IHitInputBoxListener.onInputBox())
#### IHitInputBoxListener.onInputBox()

表示用户点中了输入框。

[](id:ITcgSdk.registerHitInputBoxListener2(listener))
### ITcgSdk.registerHitInputBoxListener2(listener)

注册远端设备输入框回调监听。

>? 该接口依赖服务器针对游戏的配置。

| 参数     | 类型                  | 返回值 | 描述               |
| -------- | --------------------- | ------ | ------------------ |
| listener | IHitInputBoxListener2 | 无     | 远端输入框回调监听 |

[](id:ITcgSdk.unRegisterHitInputListener2(listener) )
### ITcgSdk.unRegisterHitInputListener2(listener)  

注销远端设备输入框回调监听。

[](id:IHitInputBoxListener.onInputBox(isHitInputBox,isSupportLoginHelper))
#### IHitInputBoxListener.onInputBox(isHitInputBox,isSupportLoginHelper)

输入框状态点击回调。

| 参数                 | 类型    | 描述                     |
| -------------------- | ------- | ------------------------ |
| isHitInputBox        | boolean | 用户是否点中输入框       |
| isSupportLoginHelper | boolean | 当前窗口是否支持自动登录 |



## 触控操作接口

[](id:CursorType.TouchClickKey)
### CursorType.TouchClickKey

 当鼠标类型为 TOUCH 和 RELATIVE_TOUCH 时，触发点击的按键类型。

| 状态定义    | 说明     |
| ----------- | -------- |
| MOUSE_LEFT  | 鼠标左键 |
| MOUSE_RIGHT | 鼠标右键 |

[](id:GameView.setTouchClickKey(TouchClickKey))
### GameView.setTouchClickKey(TouchClickKey)

设置鼠标类型使用的按键。

| 参数          | 类型                     | 描述           |
| ------------- | ------------------------ | -------------------- |
| TouchClickKey | CursorType.TouchClickKey | 鼠标模式 TOUCH / RELATIVE_TOUCH 下，点击时的按键类型。默认是鼠标左键 |

[](id:GameView.enableScaling(enable))
### GameView.enableScaling(enable)

是否允许双指缩放游戏画面。

[](id:GameView.enableScaling(enable,min,max))
### GameView.enableScaling(enable,min,max)

是否允许双指缩放游戏画面。

| 参数   | 类型    | 描述        |
| ------ | ------- | ------------------ |
| enable | boolean | **true** 表示允许双指缩放画面，反之不允许 |
| min    | float   | 缩放的最小比例，需大于0                |
| max    | float   | 缩放的最大值，需大于１                 |

[](id:GameView.setPinchOffset(rect))
### GameView.setPinchOffset(rect)

设置缩放时画面边框的偏移大小，这能让游戏画面划出手机边框。

| 参数 | 类型 | 描述     |
| ---- | ---- | --------------- |
| rect | Rect | 边框四个边界可划出的大小，默认都是0 |


[](id:GameView.handleMotion(enable))
### GameView.handleMotion(enable)

让游戏视图处理手势动作。

[](id:GameView.setMoveSensitivity(value))
### GameView.setMoveSensitivity(value)

设置鼠标灵敏度。

| 参数 | 类型 | 描述     |
| ---- | ---- | --------------- |
| value | float | 鼠标灵敏度，value 为 [0.01, 10.0] 之间的的浮点数 |

[](id:GameView.setCursorType(mode))
### GameView.setCursorType(mode)

设置鼠标模式。

| 参数 | 类型    | 描述     |
| ---- | -------- | -------- |
| mode | [CursorType](#CursorType) | 鼠标模式 |


[](id:GameView.setScaleType(mode))
### GameView.setScaleType(mode)

设置画面缩放模式（画面类型）。

| 参数      | 类型    | 描述     |
| --------- | -------------- | -------- |
| scaleType | [CursorType](#GameView_CursorType) | 画面类型 |

[](id:GameView_CursorType)
#### CursorType

 画面缩放类型。

| 类型        | 说明           |
| ----------- | -------------------- |
| ASPECT_FIT  | 画面适应视频分辨率（默认）        |
| ASPECT_FILL | 拉伸：让画面和视图一样大，画面会被拉伸    |
| ASPECT_CROP | 平铺：画面等比例放大超过屏幕，画面短边和手机屏幕短边重合，另一边裁剪 |

[](id:GameView.setOnPinchZoomListener(listener))
### GameView.setOnPinchZoomListener(listener)

监听双指缩放操作。

| 参数     | 类型               | 描述               |
| -------- | ------------------ | ------------------ |
| listener | IPinchZoomListener | 设置双指缩放监听器 |

#### IPinchZoomListener.onPivot(float x,float y)

缩放时的缩放圆心回调。

| 参数 | 类型  | 描述       |
| ---- | ----- | ---------- |
| x    | float | 缩放横坐标 |
| y    | float | 缩放纵坐标 |

#### IPinchZoomListener.onScale(float x,float y)

缩放时的缩放值回调。

| 参数 | 类型  | 描述       |
| ---- | ----- | ---------- |
| x    | float | 缩放横坐标 |
| y    | float | 缩放纵坐标 |




## 多人云游接口

[](id:IMultiPlayer.apply(userID,role,seatIndex,result))
### IMultiPlayer.apply(userID,role,seatIndex,result)

观察者深切换角色和席位。

| 参数      | 类型       | 描述             |
| --------- | --------- | ---------------- |
| userID    | String     | 用户 ID          |
| role      | Role       | 目标角色         |
| seatIndex | int        | 目标席位         |
| result    | [IApplyResult](#IApplyResult) | 席位申请结果回调 |

[](id:IApplyResult)
#### IApplyResult

席位申请结果回调。

[](id:IApplyResult.status(code))
##### IApplyResult.status(code)

席位申请状态。

| 类型         | 说明                 |
| ----------- | -------------------- |
| STATUS_SUCCESS                  | 申请提交成功         |
| STATUS_INVALID_SEAT_INDEX       | 席位无效             |
| STATUS_NO_AUTHORIZED            | 鉴权失败             |
| STATUS_NO_SUCH_USER             | 用户不存在           |
| STATUS_ASSIGN_SEAT_FAILED       | 席位分配失败         |
| STATUS_SERVER_JSON_PARSE_FAILED | 服务端 JSON 解析失败 |
| STATUS_TIMEOUT                  | 申请提交超时         |

[](id:IMultiPlayer.change(userID,role,seatIndex,result))
### IMultiPlayer.change(userID,role,seatIndex,result)

房主切换观察者的角色和席位。

| 参数      | 类型         | 描述             |
| --------- | ----------- | ---------------- |
| userID    | String       | 用户 ID          |
| role      | Role         | 目标角色         |
| seatIndex | int  | 目标席位         |
| result    | [IChangeResult](#IChangeResult) | 席位修改结果回调 |

[](id:IChangeResult)
#### IChangeResult

席位修改结果回调。

[](id:IChangeResult.status(code))
##### IChangeResult.status(code)

席位申请状态。

| 类型         | 说明                 |
| ----------- | -------------------- |
| STATUS_SUCCESS                  | 申请提交成功         |
| STATUS_INVALID_SEAT_INDEX       | 席位无效             |
| STATUS_NO_AUTHORIZED            | 鉴权失败             |
| STATUS_NO_SUCH_USER             | 用户不存在           |
| STATUS_ASSIGN_SEAT_FAILED       | 席位分配失败         |
| STATUS_SERVER_JSON_PARSE_FAILED | 服务端 JSON 解析失败 |
| STATUS_TIMEOUT                  | 申请提交超时         |

[](id:IMultiPlayer.syncSeatInfo())
### IMultiPlayer.syncSeatInfo()

获取所有席位信息（玩家及观察者），结果会通过 onSeatChanged 通知。 

> ? 具体请参见 [IMultiPlayer.registerSeatChangeListener(ISeatListener)](#IMultiPlayer.registerSeatChangeListener(ISeatListener)) 和 [ISeatListener.onSeatChanged(userId,viewers,players)](#ISeatListener.onSeatChanged)。

[](id:IMultiPlayer.registerSeatChangeListener(ISeatListener))
### IMultiPlayer.registerSeatChangeListener(ISeatListener)

注册席位信息监听器。

| 参数     | 类型          | 描述           |
| -------- | ------------- | -------------------- |
| listener | ISeatListener | 席位信息变更的回调接口。**该接口既可以接收 syncSeatInfo 触发的回调信息，也可以接收云端主动推送的席位变更信息** |

[](id:ISeatListener)
#### ISeatListener

席位信息监听器。

[](id:ISeatListener.onSeatChanged)
##### ISeatListener.onSeatChanged(String userId,List&lt;String&gt; viewers,List&lt;String&gt;players)

当席位信息出现变更时，所有的用户会收到该回调。该接口既可以接收 syncSeatInfo 触发的回调信息，也可以接收云端主动推送的席位变更信息。

| 参数    | 类型         | 描述           |
| ------- | ------------ | -------------------- |
| userID  | String       | 该用户自己的用户 ID               |
| viewers | List&lt;String&gt; | 观察者的用户 ID 列表，列表可能为空，列表中的元素代表用户 ID，也可能会空 |
| players | List&lt;String&gt; | 玩家的用户 ID 列表，列表可能为空，列表中的元素代表用户 ID，也可能会空 |

[](id:ISeatListener.onRoleApplied(userId,role,seatIndex))
#### ISeatListener.onRoleApplied(userId,role,seatIndex)

当有用户申请席位变更时，房主会收到该回调。

| 参数      | 类型   | 描述                  |
| --------- | ------ | --------------------- |
| userID    | String | 申请变更席位的用户 ID |
| role      | Role   | 申请者申请的角色      |
| seatIndex | int    | 申请者申请的席位      |

[](id:IMultiPlayer.unRegisterSeatChangeListener(ISeatListener))
### IMultiPlayer.unRegisterSeatChangeListener(ISeatListener)

注销席位信息监听器。

## 数据通道交互接口

[](id:ITcgSdk.createDataChannel(port,listener))
### ITcgSdk.createDataChannel(port,listener)

创建一个可以和云端应用交互的数据通道，通过该通道可以将任意数据流送到云端应用监听的 port 端口。

| 参数     | 类型                 | 描述                |
| -------- | ---------- | ------------------- |
| port     | int                  | 云端应用监听的端口 |
| listener | [IDataChannelListener](#IDataChannelListener) | 数据通道监听器，用于回调数据通道的连接状态和数据  |

[](id:IDataChannelListener)
### IDataChannelListener

数据通道监听器。

| 接口名称       | 接口描述           |
| -------------------- | ------------------ |
| [IDataChannelListener.onMessage(port,buffer)](#IDataChannelListener.onMessage(port,buffer)) | 云端数据响应回调 |
| [IDataChannelListener.onConnectFailed(port,msg)](#IDataChannelListener.onConnectFailed(port,msg)) | 连接失败         |
| [IDataChannelListener.onConnectSuccess(port)](#IDataChannelListener.onConnectSuccess(port)) | 连接成功,可以通过数据通道给云端应用发送消息       |

[](id:IDataChannelListener.onMessage(port,buffer))
### IDataChannelListener.onMessage(port,buffer)  

云端数据响应回调。

| 参数     | 类型         | 描述          |
| -------- | ------------ | ------------------- |
| port | int | 目标端口 |
| buffer | ByteBuffer | 云端发送的数据内容 |

[](id:IDataChannelListener.onConnectFailed(port,msg))
### IDataChannelListener.onConnectFailed(port,msg)  

云端数据响应回调。

| 参数     | 类型         | 描述          |
| -------- | ------------ |------------------- |
| port | int | 连接失败的云端端口 |
| msg | String | 连接失败的提示信息 |

[](id:IDataChannelListener.onConnectSuccess(port))
### IDataChannelListener.onConnectSuccess(port)  

连接成功，可以通过数据通道给云端应用发送消息。

| 参数     | 类型         | 描述          |
| -------- | ------------ | ------------------- |
| port | int | 连接成功的云端端口 |

[](id:IDataChannel.send(data))
### IDataChannel.send(data)

调用该接口给远端 UDP 端口发送数据。

return：**0**表示发送成功，**-1**表示发送数据长度超过限制，**-2**表示连接关闭。

| 参数 | 类型   | 描述                |
| ---- | ------ | --------- |
| data | byte[] | 需要发送的数据内容, 单次发送大小限制在1200字节 |

[](id:IDataChannel.close())
### IDataChannel.close()

关闭数据通道。

## 其他说明

[](id:TcgErrorType)
### TcgErrorType

错误码定义。

| 错误码         | 说明                    |
| ------------- | ------------- |
| ERROR_UNKNOWN                     | 未知错误                |
| INIT_ERROR_SYS_BUSY               | 系统繁忙，请稍后重试    |
| INIT_ERROR_TICKET_ILLEGAL         | 票据不合法              |
| INIT_ERROR_INEFFICIENT_BANDWIDTH  | 建议您使用超过 10Mbps 的带宽以完美体验腾讯云云游戏 |
| INIT_ERROR_UNDER_RESOURCE         | 资源不足，请稍后重试    |
| INIT_ERROR_TICKET_EXPIRED         | 票据失效                |
| INIT_ERROR_INVALID_SPD            | SDP 信息错误            |
| INIT_ERROR_LAUNCH_GAME_ERROR      | 游戏拉起失败            |
| INIT_ERROR_GET_ARCHIVE_FAILED     | 下载用户游戏存档失败    |
| INIT_ERROR_TCG_SDK_STOPPED        | SDK 已终止，再使用需通过 Builder 重新创建          |
| CONN_ERROR_SET_REMOTE_SDP_FAILED  | 设置远端 SDP 异常       |
| CONN_ERROR_SET_LOCAL_SDP_FAILED   | 设置本地 SDP 异常       |
| CONN_ERROR_PEER_CONNECTION_FAILED | 节点连接异常            |
| CONN_ERROR_USER_LOGOUT            | 用户主动退出            |
| CONN_ERROR_DUPLICATE_CONNECTION   | 用户已在其他设备登录    |
| CONN_ERROR_TICKET_EXPIRED         | 本地获取的 token 失效（有效时间80s）               |
| CONN_ERROR_GET_TICKET_ERROR       | 获取重连 token 失败     |
| CONN_ERROR_GET_TICKET_TIMEOUT     | 获取重连 token 超时     |
| CONN_ERROR_CLOSE_BY_SERVER        | 服务端原因踢出节点      |
| CONN_ERROR_TIMEOUT                | 连接超时                |
| CONN_ERROR_NETWORK_DISCONNECTED   | 网络连接断开（WebRTC 内部会尝试重连）              |

[](id:GameView)
### GameView

**该视图代理了远程设备视图，支持：**

 - 本地按键和触摸事件的转换、封装，并将事件发送到远端设备。
 - 鼠标控制模式。
 - 调试视图（可以在界面上显示性能指标信息）。

**关于双指缩放**

- 如果您需要在使用 GameView 的同时使用自己添加的按键控件，请务必确保 GameView 和您的按键控件是兄弟关系，并且位于按键控件的最底层。
- 如果不能够让 GameView 位于控件最底层：
  - 请调用 `GameView.setOnTouchListener(null)`，屏蔽掉触摸监听。
  - 请在控件最底层添加一个代理视图，并且给代理视图设置 OnTouchListener，并在 onTouch 函数中调用 `GameView.handleMotion(MotionEvent event)` 并返回 true。
- 双指缩放功能默认开启，如果您不需要，请调用 `GameView.enableScaling(false)`。

[](id:CursorType)
### CursorType

 鼠标类型。

| 状态定义        | 说明          |
| --------------- | -------------------- |
| NO_CURSOR       | 禁用鼠标，触摸屏幕不触发任何事件  |
| NO_CURSOR_TOUCH | 无鼠触控，鼠标隐藏，点击可以单击按键（鼠标左键或右键）       |
| TOUCH           | 触控，鼠标跟随手指移动，点击可以单击按键（鼠标左键或右键）   |
| RELATIVE_TOUCH  | 滑鼠点击，轻触触发鼠标左键，长按触发按点击鼠标左键，可以拖动，滑动仅触发鼠标移动 |
| RELATIVE_MOVE   | 滑屏，鼠标在相对位置移动，不触发点击事件（可以发送其他按键事件） |


[](id:CursorStyle)
### CursorStyle

 鼠标样式。

| 状态定义        | 说明          |
| --------------- | -------------------- |
| NORMAL       | 默认鼠标样式         |
| HUGE | 大号鼠标       |

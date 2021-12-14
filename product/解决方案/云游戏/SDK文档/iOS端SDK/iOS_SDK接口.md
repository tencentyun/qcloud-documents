## 生命周期相关接口

[](id:initWithParams)
### [TCGGamePlayer initWithParams:andDelegate:]
SDK 初始化。接口立即返回，异步执行初始化通过回调通知结果。

| 参数     | 类型                 | 描述              |
| -------- | ----------- | ----------- |
| params   | NSDictionary           | 选填，预留暂未启用 |
| listener | TCGGamePlayerDelegate | 生命周期回调       |

[](id:startGameWithRemoteSession)
### [TCGGamePlayer startGameWithRemoteSession:error:]
启动云游戏。

| 参数           | 类型     | 描述             |
| ------------- | -------- | --------------- |
| remoteSession | NSString | Server Session，需从云 API 获取 |

[](id:stopGame)
### [TCGGamePlayer stopGame]
停止云游戏。

[](id:TCGGamePlayerDelegate)
### TCGGamePlayerDelegate
TCGGamePlayer 生命周期回调。

| 接口名称            | 接口描述            |
| ----------- | ----------- |
| [TCGGamePlayerDelegate onInitSuccess:]            | SDK 初始化成功回调 |
| [TCGGamePlayerDelegate onInitFailure:msg:]       | 初始化失败         |
| [TCGGamePlayerDelegate onConnectionFailure:msg:] | 连接失败回调       |
| [TCGGamePlayerDelegate onVideoShow]             | 首帧绘制时机       |

[](id:onInitSuccess)
#### [TCGGamePlayerDelegate onInitSuccess:]
SDK 初始化成功回调。

| 参数         | 类型     | 描述             |
| ------------ | -------- | ------------ |
| localSession | NSString | ClientSession 客户端会话， 其内容较长, 可能会超出 logcat 输出限制 |

[](id:onInitFailure)
#### [TCGGamePlayerDelegate onInitFailure:msg:]
初始化失败回调。

| 参数      | 类型         | 描述         |
| --------- | ------------ | ------------ |
| errorCode | TCGErrorType | 错误码       |
| errorMsg  | NSError      | 内部错误信息 |

[](id:onConnectionFailure)
#### [TCGGamePlayerDelegate onConnectionFailure:msg:]
连接失败回调。

| 参数      | 类型         | 描述         |
| --------- | ------------ | ------------ |
| errorCode | TCGErrorType | 错误码       |
| errorMsg  | NSError      | 内部错误信息 |

[](id:onVideoShow)
#### [TCGGamePlayerDelegate onVideoShow]
连接成功，画面开始显示。

## 音视频控制接口
[](id:pauseResumeGame)
### [TCGGamePlayer pauseResumeGame:]
暂停/恢复 画面传输。

| 参数    | 类型 | 描述               |
| ------- | ---- | -------------- |
| doPause | BOOL | YES 表示暂停画面传输，NO 表示恢复画面传输 |

[](id:setStreamBitrateMix)
### [TCGGamePlayer setStreamBitrateMix:max:fps:]
设置建议的帧率和码率
>! 该接口设置的仅是建议值，云端会根据实际网络情况动态调整。

| 参数       | 类型 | 描述             |
| ---------- | ---- | ----------- |
| fps        | int  | 建议帧率，范围[10，60]，默认45               |
| minBitrate | int  | 建议最小码率，范围[1000,15000]，默认1000kbps  |
| maxBitrate | int  | 建议最大码率，范围[1000,15000]，默认3000kbps |

[](id:setVolumeScale)
### [TCGGamePlayer setVolumeScale:]
设置游戏音频 PCM 增益大小，默认1.0。

| 参数  | 类型  | 描述              |
| ----- | ----- | ------------ |
| scale | float | [0,10]之间的浮点数，大于１时可能会导致声音失真 |

[](id:videoView)

### [TCGGamePlayer videoView]
获取游戏画面渲染的图层。

[](id:setVideoViewEnablePinch)
### [TCGGamePlayer setVideoViewEnablePinch:]
是否允许双指缩放/拖动游戏图层。

| 参数     | 类型 | 描述             |
| -------- | ---- | ------------ |
| isEnable | BOOL | YES 表示允许双指缩放画面，NO 表示不允许 |

[](id:setVideoViewEnablePinch)
### [TCGGamePlayer setVideoViewEnablePinch:]
设置缩放时画面边框的偏移大小，这能让游戏画面划出手机边框。

| 参数   | 类型         | 描述            |
| ------ | ------------ | --------- |
| insets | UIEdgeInsets | 指定边缘间距，默认(100, 50, 50, 100) |

[](id:onVideoSizeChanged)
### [TCGGamePlayerDelegate onVideoSizeChanged:]
视频图像宽高发生变化。

| 参数      | 类型   | 描述                |
| --------- | ------ | ---------- |
| videoSize | CGSize | 变化后的视频图像尺寸 |

[](id:onVideoOrientationChanged)
### [TCGGamePlayerDelegate onVideoOrientationChanged:]
（手游）视频画面的朝向发生改变，进入游戏前也会回调。
> ! 这里的朝向指画面里的内容是竖屏或横屏内容（可理解为云端手机的朝向），而视频画面的宽高是不会发生改变的。

| 参数        | 类型            | 描述            |
| ----------- | ------------ | -------------- |
| orientation | UIInterfaceOrientation | 视频画面的朝向 |

[](id:TCGGamePlayer)
## 游戏操控相关接口
> ! 所有按键相关接口必须在 [[TCGGamePlayerDelegate onVideoShow]](#onVideoShow) 回调发生之后调用才生效。


[](id:gameController)
### [TCGGamePlayer gameController]
获取游戏操控辅助类。

[](id:initWithFrame)
### [TCGVirtualMouseCursor initWithFrame:controller:]
创建鼠标视图（继承 UIView），支持将手指单击事件转换为 PC 上的鼠标操作。

> ? 视图为透明视图，使用时添加为 [videoView](#videoView) 的子视图，大小与 videoView 相同。

| 参数       | 类型            | 描述            |
| ---------- | --------- | ---------------- |
| frame      | CGRect                         | 视图的大小与位置 |
| controller | [TCGGameController](#gameController) | 游戏操控辅助类   |

[](id:setCursorTouchMode)
### [TCGVirtualMouseCursor setCursorTouchMode:]
设置鼠标的操控模式。

| 参数 | 类型            | 描述            |
| ---- | ----------- | -------------- |
| mode | [TCGMouseCursorTouchMode](#TCGMouseCursorTouchMode) | 鼠标的操控模式 |

[](id:setCursorIsShow)
### [TCGVirtualMouseCursor setCursorIsShow:]
设置鼠标的操控模式，配合 [onCursorVisibleChanged:](#onCursorVisibleChanged ) 回调一起使用。

| 参数   | 类型 | 描述             |
| ------ | ---- | ---------- |
| isShow | BOOL | YES 表示显示，NO 表示隐藏 |

[](id:setCursorImage)
### [TCGVirtualMouseCursor setCursorImage:andRemoteFrame:]
更新鼠标的图标，配合 [onCursorImageUpdated:frame:](#onCursorImageUpdated) 回调一起使用。

| 参数       | 类型    | 描述              |
| ---------- | ------- | ------------- |
| image      | UIImage | 鼠标指针图标                 |
| imageFrame | CGRect  | view 的大小位置，云端主动下发 |

[](id:setCursorSensitive)
### [TCGVirtualMouseCursor setCursorSensitive:]
设置鼠标相对移动时的灵敏度，[TCGMouseCursorTouchMode(RelativeTouch、RelativeOnly)](#TCGMouseCursorTouchMode) 下有效。

| 参数      | 类型    | 描述            |
| --------- | ------- | ----------- |
| sensitive | CGFloat | 默认1.0与手动滑动的幅度相同 |

[](id:setClickTypeIsLeft)
### [TCGVirtualMouseCursor setClickTypeIsLeft:]
设置鼠标触发单击的事件，[TCGMouseCursorTouchMode(AbsoluteTouch、RelativeTouch)](#TCGMouseCursorTouchMode) 下有效。

| 参数   | 类型 | 描述                |
| ------ | ---- | --------------- |
| isLeft | BOOL | YES 表示触发鼠标左键，NO 表示触发鼠标右键 |

[](id:moveCursorWithDiffX)
### [TCGVirtualMouseCursor moveCursorWithDiffX:diffY:]
以接口的方式移动鼠标指针。

| 参数  | 类型    | 描述             |
| ----- | ------- | ------------ |
| diffX | CGFloat | 在当前鼠标视图的 X 轴上，鼠标指针移动 diffX 个 point |
| diffY | CGFloat | 在当前鼠标视图的 Y 轴上，鼠标指针移动 diffY 个 point |

[](id:initWithFrame)
### [TCGVKeyGamepad initWithFrame:controller:]
创建一个虚拟按键视图（继承 UIView），支持将手指单击事件转换为键盘/手柄按键事件。

> ! 需要选用 **TCGVkey.framework** 库。

| 参数       | 类型            | 描述            |
| ---------- | --------- | ---------------- |
| frame      | CGRect  | 视图的大小与位置 |
| controller | [TCGGameController](#gameController) | 游戏操控辅助类   |

[](id:showKeyGamepad)
### [TCGVKeyGamepad showKeyGamepad:]
加载虚拟按键布局，生成按键，配置与 Android SDK、JS SDK 通用。

| 参数 | 类型     | 描述               |
| ---- | -------- | ------------ |
| cfg  | NSString | JSON 格式的配置内容 |

[](id:needConnected)
### [TCGVKeyGamepad needConnected]
查询当前的按键布局是否需要主动通知云端，返回 YES  表示时需调用 [enableVirtualGamepad](#enableVirtualGamepad) 通知云端启用虚拟手柄。

[](id:initWithFrame)
### [TCGRemoteTouchScreen initWithFrame:controller:]
（手游）创建云端触控视图（继承 UIView），支持将手指单击事件传递到云端手机上。

> ! 视图为透明视图，使用时添加为 [videoView](#videoView) 的子视图，大小与 videoView 相同。

| 参数       | 类型            | 描述            |
| ---------- | --------- | ---------------- |
| frame      | CGRect | 视图的大小与位置 |
| controller | [TCGGameController](#gameController) | 游戏操控辅助类   |


[](id:onCursorVisibleChanged )
### [TCGGameController onCursorVisibleChanged:]
云端鼠标显示状态变化。

| 参数     | 类型 | 描述            |
| -------- | ---- | ---------- |
| isVisble | BOOL | YES 表示云端鼠标可见，NO 表示云端鼠标不可见 |


[](id:onCursorImageUpdated)
### [TCGGameController onCursorImageUpdated:frame:]
云端鼠标显示状态变化。

| 参数       | 类型    | 描述             |
| ---------- | ------- | ------------ |
| image      | UIImage | 鼠标指针图标                |
| imageFrame | CGRect  | view的大小位置，云端主动下发 |

[](id:)
### [TCGGameController clickKeyboard:isDown:]
发送键盘事件，推荐使用 [TCGVKeyGamepad](#initWithFrame)。

| 参数    | 类型 | 描述              |
| ------- | ---- | ------------- |
| keycode | int  | 按键值            |
| isDown  | BOOL | true 表示按下，false 表示抬起 |

[](id:)
### [TCGGameController clickGamepadKey:isDown:]
发送游戏手柄按键事件，推荐使用 [TCGVKeyGamepad](#initWithFrame)。

| 参数    | 类型 | 描述                |
| ------- | ---- | --------------- |
| keycode | int  | 按键值              |
| isDown  | BOOL | YES 表示发送按下消息，NO 表示发送抬起消息 |

[](id:)
### [TCGGameController turnJoyStickX:y:isLeft:]
转动游戏手柄的（左/右）摇杆，推荐使用 [TCGVKeyGamepad](#initWithFrame)。

| 参数   | 类型    | 描述            |
| ------ | ------- | ----------- |
| deltaX | CGFloat | 范围[-1, 1]，最左端为-1 最右端为 1     |
| deltaY | CGFloat | 范围[-1, 1]，最左端为-1 最右端为 1     |
| isLeft | BOOL    | YES 表示转动左摇杆，NO 表示转动右摇杆 |

[](id:enableVirtualGamepad)
### [TCGGameController enableVirtualGamepad:]
通知云端启用虚拟游戏手柄。

| 参数   | 类型 | 描述              |
| ------ | ---- | ------------ |
| enable | BOOL | YES 表示发送启用的消息，NO 表示发送停用的消息 |

[](id:resetRemoteKeycode)
### [TCGGameController resetRemoteKeycode]
清空云端的按键，清除异常键盘卡键的状态。

[](id:remoteMobileBackClick)
### [TCGGameController remoteMobileBackClick]
 (手游) 触发云端的返回动作，触发云端系统的物理返回键。

## 数据通道交互接口
[](id:openCustomTransChannel)
### [TCGGamePlayer openCustomTransChannel:delegate:]
创建一条数据通道。
return：数据通道对象，与云端连接的结果通过代理异步回调通知。

| 参数             | 类型              | 描述             |
| --------------- | ------------- | ----------- |
| remotePort      | int | 云端应用监听的端口号 |
| channelDelegate | TCGCustomTransChannelDelegate | 数据通道的代理，用于回调数据通道的连接状态和数据 |

[](id:sendData)
### [TCGCustomTransChannel sendData:]
给云端 UDP 端口发送数据。

return：发送状态。**0**发送成功，**-1** 数据超过长度， **-2** 当前通道未连接成功。

| 参数 | 类型   | 描述              |
| ---- | ------ | ------------ |
| data | NSData | 需要发送的数据内容, 单次发送大小限制在1200字节 |

[](id:close)
### [TCGCustomTransChannel close]
关闭数据通道。

[](id:onConnSuccessAtRemotePort)
### [TCGCustomTransChannelDelegate onConnSuccessAtRemotePort:]
连接成功，可以通过数据通道给云端应用发送消息。

| 参数       | 类型 | 描述                |
| ---------- | ---- | ---------- |
| remotePort | int  | 云端应用监听的端口号 |

[](id:onConnFailed)
### [TCGCustomTransChannelDelegate onConnFailed:atRemotePort:]
连接失败。

| 参数       | 类型    | 描述              |
| ---------- | ------- | ------------ |
| remotePort | int     | 云端应用监听的端口号             |
| error      | NSError | 失败的原因，code：**-1**云端后台错误，**10009**连接超时 |

[](id:onClosedAtRemotePort)
### [TCGCustomTransChannel onClosedAtRemotePort:]
云端主动关闭了通道。

| 参数       | 类型 | 描述                |
| ---------- | ---- | ---------- |
| remotePort | int  | 云端应用监听的端口号 |

[](id:onReceiveData)
### [TCGCustomTransChannel onReceiveData:fromRemotePort:]
接收来自云端的数据。

| 参数       | 类型   | 描述                |
| ---------- | ------ | ---------- |
| data       | NSData | 数据内容            |
| remotePort | int    | 云端应用监听的端口号 |

## 调试及日志相关接口
[](id:)
### [TCGGamePlayer setLogger:withMinLevel:]
设置日志回调接收者及过滤等级。

| 参数     | 类型             | 描述                |
| -------- | --------------- | ---------- |
| logger   | [TCGLogDelegate](#logWithLevel) | 数据内容            |
| minLevel | [TCGLogLevel](#TCGLogLevel)     | 云端应用监听的端口号 |

[](id:logWithLevel)
### [TCGLogDelegate logWithLevel:log:]
日志打印回调接口。

| 参数     | 类型            | 描述       |
| -------- | ----------- | ---------- |
| logLevel | [TCGLogLevel](#TCGLogLevel) | 日志的等级 |
| log      | NSString             | 日志的内容 |

[](id:currentStatisReport)
### [TCGGamePlayer currentStatisReport]
返回获取当前的性能统计数据。

[](id:TCGMouseCursorTouchMode)
### TCGMouseCursorTouchMode
鼠标的操控模式。

| 状态定义      | 说明             |
| ------------- | ---------- |
| AbsoluteTouch | 鼠标跟随手指移动，单击可以单击按键               |
| RelativeTouch | 手指滑动控制鼠标相对移动，轻触触发鼠标左键，长按触发按单击鼠标左键, 滑动仅触发鼠标移动 |
| RelativeOnly  | 触控，鼠标跟随手指移动，单击可以单击按键（鼠标左键或右键）   |

[](id:TCGLogLevel)
### TCGLogLevel
日志等级。

| 等级              |说明|
| ------------- |------------- |
| TCGLogLevelDebug   |调试信息，主要用于开发过程中打印一些运行信息|
| TCGLogLevelInfo    |粗粒度信息，输出程序运行过程中的重要信息|
| TCGLogLevelWarning |警告，传递系统中的潜在错误信息|
| TCGLogLevelError   |错误，传递系统或应用程序中出现的各种级别的错误|
| TCGLogLevelNone    |不打印日志|

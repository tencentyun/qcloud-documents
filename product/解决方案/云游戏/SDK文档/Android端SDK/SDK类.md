## GameView


该视图代理了远程设备视图，支持功能如下：

- 本地按键和触摸事件的转换、封装，并将事件发送到远端设备。
- 鼠标控制模式。
- 调试视图（可以在界面上显示性能指标信息）。

### 方法概览

| 方法                                                      | 类型                                                         | 说明                       |
| --------------------------------------------------------- | ------------------------------------------------------------ | -------------------------- |
| [setSDK](#setsdk)                                         | void                                                         | 设置 SDK 接口              |
| [setOnGameViewTouchListener](#setongameviewtouchlistener) | void                                                         | 设置游戏画面触控事件监听器 |
| [enableDebugView](#enabledebugview)                       | void                                                         | 开启调试模式，展示性能数据 |
| [moveDelta](#movedelta)                                   | void                                                         | 移动光标                   |
| [movePosTo](#moveposto)                                   | void                                                         | 以绝对坐标方式移动光标位置 |
| [setMoveSensitivity](#setmovesensitivity)                 | void                                                         | 设置鼠标灵敏度             |
| [getMoveSensitivity](#getmovesensitivity)                 | float                                                        | 返回已经设置的鼠标灵敏度   |
| [setTouchClickKey](#settouchclickkey)                     | void                                                         | 设置鼠标类型使用的按键     |
| [setCursorType](#setcursortype)                           | void                                                         | 设置鼠标模式               |
| [getCurrentCursorType](#getcurrentcursortype)             | [CursorType](https://cloud.tencent.com/document/product/1162/52242) | 当前设置的鼠标模式         |
| [setScaleType](#setscaletype)                             | void                                                         | 设置画面显示模式           |

### setSDK

设置 SDK。

```java
public void setSDK(ITcgSdk sdk)
```

### setOnGameViewTouchListener

设置游戏画面触控事件监听器。

```java
public void setOnGameViewTouchListener(IOnGameViewTouchListener listener)
```

**参数：**

| 参数     | 类型                     | 说明           |
| -------- | ------------------------ | -------------- |
| listener | IOnGameViewTouchListener | 支持长按和单击 |

### enableDebugView

开启调试模式，展示性能数据。

```java
public void enableDebugView(boolean enable)
```

**参数：**

| 参数   | 类型    | 说明                                  |
| ------ | ------- | ------------------------------------- |
| enable | boolean | true 表示开启调试模式，false 表示关闭 |

### moveDelta

以相对坐标方式移动光标位置。

```java
public void moveDelta(float deltaX,
                      float deltaY)
```

**参数：**

| 参数   | 类型  | 说明                                     |
| ------ | ----- | ---------------------------------------- |
| deltaX | float | 横坐标移动的偏移量，该值受鼠标灵敏度影响 |
| deltaY | float | 纵坐标移动的偏移量，该值受鼠标灵敏度影响 |

> ? 更多详情请参见 [setMoveSensitivity(float)](#setmovesensitivity)。

### movePosTo

以绝对坐标方式移动光标位置。

```java
protected void movePosTo(float x,
                         float y)
```

**参数：**

| 参数 | 类型  | 说明              |
| ---- | ----- | ----------------- |
| x    | float | 本地设备的 x 坐标 |
| y    | float | 本地设备的 y 坐标 |

### setMoveSensitivity

设置鼠标灵敏度。

```java
public void setMoveSensitivity(float moveSensitivity)
```

**参数：**

| 参数            | 类型  | 说明                                             |
| --------------- | ----- | ------------------------------------------------ |
| moveSensitivity | float | 鼠标灵敏度，value 为 [0.01，10.0] 之间的的浮点数 |

### getMoveSensitivity

返回已经设置的鼠标灵敏度。

```java
public float getMoveSensitivity()
```

### setTouchClickKey

设置鼠标类型使用的按键。

```java
public void setTouchClickKey(com.tencent.tcgsdk.api.CursorType.TouchClickKey key)
```

**参数：**

| 参数 | 类型                                            | 说明                                                |
| ---- | ----------------------------------------------- | --------------------------------------------------- |
| key  | com.tencent.tcgsdk.api.CursorType.TouchClickKey | TOUCH / RELATIVE_TOUCH 单击时的按键，默认是鼠标左键 |

> ? 更多详情请参见 [CursorType.TOUCH](https://cloud.tencent.com/document/product/1162/52242#touch)、[CursorType.RELATIVE_TOUCH](https://cloud.tencent.com/document/product/1162/52242#relative_touch)。

### setCursorType

设置鼠标模式。

```java
public void setCursorType(CursorType mode)
```

**参数：**

| 参数 | 类型                                                         | 说明                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| mode | [CursorType](https://cloud.tencent.com/document/product/1162/52242#cursortype) | 鼠标类型，对于TOUCH / RELATIVE_TOUCH 两种类型可以指定单击时的按键 |

> ? 更多详情请参见 [setTouchClickKey(CursorType.TouchClickKey)](#settouchclickkey)。

### getCurrentCursorType

返回当前设置的鼠标模式。

```java
public CursorType getCurrentCursorType()
```

### setScaleType

设置画面显示模式，包括平铺、拉伸和自适应。

```java
public void setScaleType(ScaleType scaleType)
```

**参数：**

| 参数      | 类型      | 说明               |
| --------- | --------- | ------------------ |
| scaleType | ScaleType | 需要指定的显示模式 |



## TcgSdk2.Builder

TcgSdk 的构建器。

### 构造器概览

| 构造器              | 说明                      |
| ------------------- | ------------------------- |
| [Builder](#builder) | 构建一个TcgSdk 的 Builder |

### 方法概览

| 方法                                | 限定符和类型    | 说明                                                         |
| ----------------------------------- | --------------- | ------------------------------------------------------------ |
| [build](#build)                     | ITcgSdk         | 构建一个 TcgSdk 并初始化                                     |
| [autoReconnect](#autoreconnect)     | TcgSdk2.Builder | 帧率掉0或者异常断开是否触发自动重连                          |
| [dataChannel](#datachannel)         | TcgSdk2.Builder | 开启数据通道（必须开启）                                     |
| [localAudio](#localaudio)           | TcgSdk2.Builder | 开启本地音频上传能力，默认关闭                               |
| [localVideo](#localvideo)           | TcgSdk2.Builder | 开启本地视频上传能力，默认关闭                               |
| [timeout](#timeout)                 | TcgSdk2.Builder | 设置连接超时时间，超时则会触发超时回调                       |
| [logLevel](#loglevel)               | TcgSdk2.Builder | 指定日志级别                                                 |
| [enableHwCodec](#enablehwcodec)     | TcgSdk2.Builder | 是否优先使用硬解                                             |
| [lowFpsThreshold](#lowfpsthreshold) | TcgSdk2.Builder | 低帧率阈值，连续 lowFpsCountThreshold 秒帧率低 于lowFpsThreshold 会触发 ILowFPSListener 回调 |

### Builder

构建一个 TcgSdk 的 Builder。

```java
public Builder(Context context,
               long appID,
               ITcgListener listener,
               SurfaceViewRenderer surfaceRender)
```

**参数：**

| 参数          | 类型                | 说明                     |
| ------------- | ------------------- | ------------------------ |
| appID         | long                | 应用 ID                  |
| listener      | ITcgListener        | 生命周期回调             |
| surfaceRender | SurfaceViewRenderer | 用于展示游戏画面的绘制器 |

### build

构建一个 TcgSdk 并开始初始化，初始化成功会回调。

```java
public ITcgSdk build()
```

**返回：**返回 SDK 接口。

> ? 更多详情请参见 [ITcgListener.onInitSuccess(String)](https://cloud.tencent.com/document/product/1162/52326#oninitsuccess)。

### autoReconnect

帧率掉0或者异常断开是否触发自动重连。

```java
public TcgSdk2.Builder autoReconnect(boolean enable)
```

**参数：**

| 参数   | 类型    | 说明                                                         |
| ------ | ------- | ------------------------------------------------------------ |
| enable | boolean | 默认为 true。true 表示帧率连续掉0或者异常断开时自动重连，false 表示不重连 |

### dataChannel

开启数据通道（必须开启）。

```java
public TcgSdk2.Builder dataChannel(boolean enable)
```

**参数:**

| 参数   | 类型    | 说明                                                       |
| ------ | ------- | ---------------------------------------------------------- |
| enable | boolean | 默认为 true。true 表示开启数据通道，false 表示关闭数据通道 |

**返回：**被调用的 Builder 本身。

### localAudio

开启本地音频上传能力，默认关闭。

```java
public TcgSdk2.Builder localAudio(boolean enable)
```

**参数：**

| 参数   | 类型    | 说明                                                         |
| ------ | ------- | ------------------------------------------------------------ |
| enable | boolean | 默认为 false。true 表示开启本地音频上传，false 表示关闭本地音频上传 |

**返回：**被调用的 Builder 本身。

### localVideo

开启本地视频上传能力，默认关闭。

```java
public TcgSdk2.Builder localVideo(boolean enable)
```

**参数：**

| 参数   | 类型    | 说明                                                         |
| ------ | ------- | ------------------------------------------------------------ |
| enable | boolean | 默认为 false。true 表示开启本地视频上传，false 表示关闭本地视频上传 |

**返回：**被调用的 Builder 本身。

### timeout

连接超时时间，超时则会触发超时回调。

```java
public TcgSdk2.Builder timeout(long timeoutMs)
```

**参数：**

| 参数      | 类型 | 说明              |
| --------- | ---- | ----------------- |
| timeoutMs | long | 超时时间，默认60s |

**返回：**被调用的 Builder 本身。

> ? 更多详情请参见 [ITcgListener.onConnectionTimeout()](https://cloud.tencent.com/document/product/1162/52326#onconnectiontimeout)。

### logLevel

指定日志级别。

```java
public TcgSdk2.Builder logLevel(LogLevel level)
```

**参数：**

| 参数  | 类型     | 说明                 |
| ----- | -------- | -------------------- |
| level | LogLevel | 启动后指定的日志级别 |

**返回：**被调用的 Builder 本身。

### enableHwCodec

是否优先使用硬解。

```java
public TcgSdk2.Builder enableHwCodec(boolean enableHwCodec)
```

**参数：**

| 参数          | 类型    | 说明                              |
| ------------- | ------- | --------------------------------- |
| enableHwCodec | boolean | true 优先使用硬解，false 使用软解 |

### lowFpsThreshold

低帧率阈值，连续 lowFpsCountThreshold 秒码率低于 lowFpsThreshold 会触发 [ILowFPSListener](https://cloud.tencent.com/document/product/1162/52326#ilowfpslistener) 回调。

```java
public TcgSdk2.Builder lowFpsThreshold(int lowFpsThreshold,
                                       int lowFpsCountThreshold)
```

**参数：**

| 参数                 | 类型 | 说明           |
| -------------------- | ---- | -------------- |
| lowFpsThreshold      | int  | 最低帧率       |
| lowFpsCountThreshold | int  | 出现低帧的秒数 |

**返回：**被调用的 Builder 本身。

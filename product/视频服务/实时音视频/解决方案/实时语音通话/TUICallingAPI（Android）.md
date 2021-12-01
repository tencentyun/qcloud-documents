TUICalling 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持1v1和多人视频通话。TUICalling 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [实时语音通话（Android）](https://cloud.tencent.com/document/product/647/42047)。

- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时音视频通话组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 发送和处理信令消息。


## TUICalling API 概览
[](id:TUICalling)
 
#### SDK 基础函数

| API                                             | 描述                                             |
| ----------------------------------------------- | ------------------------------------------------ |
| [sharedInstance](#sharedinstance)               | 组件单例                                     |
| [call](#call) | C2C 邀请通话                                   |
| [receiveAPNSCalled](#receiveAPNSCalled)                     | 作为被邀请方接听来电                                   |
| [setCallingListener](#setCallingListener)               | 设置监听器。                                   |
| [setCallingBell](#setCallingBell)                             | 设置铃声（建议在30s以内）   |
| [enableMuteMode](#enableMuteMode)                                 | 开启静音模式 |
| [enableCustomViewRoute](#enableCustomViewRoute)                               | 开启自定义视图       |


## TUICallingListener API 概览
[](id:TUICallingListener)

#### 事件回调

| API                 | 描述       |
| ------------------- | ---------- |
| [shouldShowOnCallView](#shouldShowOnCallView) | 被叫时请求拉起接听页面 |
| [onCallStart](#onCallStart) | 呼叫开始回调。主叫、被叫均会触发 |
| [onCallEnd](#onCallEnd) | 通话回调。主叫、被叫均会触发 |
| [onCallEvent](#onCallEvent) | 通话事件回调 |

## Type API 概览
[](id:Type)

#### 通话类型
| enum                 | 描述       |
| ------------------- | ---------- |
| AUDIO | 音频通话 |
| VIDEO | 视频通话 |

## Role API 概览
[](id:Role)

#### 用户角色类型
| enum                 | 描述       |
| ------------------- | ---------- |
| CALL | 通话发起方（主叫） |
| CALLED | 通话接听方（被叫） |

## Event API 概览
[](id:Event)

#### 事件类型
| enum                 | 描述       |
| ------------------- | ---------- |
| CALL_START | 通话开始 |
| CALL_SUCCEED | 通话接通成功 |
| CALL_END | 通话结束 |
| CALL_FAILED | 通话失败 |

## SDK 基础函数

### sharedInstance
[](id:sharedInstance)

sharedInstance 是 TUICalling 的组件单例。

```java
public static TUICallingManager sharedInstance();
```

### call
[](id:call)

C2C 邀请通话。

```java
void call(String[] userIDs, Type type);
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| userIDs    | String[]  | 通话用户 ID 列表      |
| type | TUICalling.Type | 通话类型：音频/视频 |

### receiveAPNSCalled
[](id:receiveAPNSCalled)

作为被邀请方接听来电。

```java
void receiveAPNSCalled(String[] userIDs, Type type);
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| userIDs    | String[]  | 通话用户 ID 列表      |
| type | TUICalling.Type | 通话类型：音频/视频 |

### setCallingListener
[](id:setCallingListener)

设置监听器。

```java
void setCallingListener(TUICallingListener listener);
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| listener    | TUICallingListener  | TUIcalling 组件监听器   |

### setCallingBell
[](id:setCallingBell)

设置铃声(建议在30s以内)。

```java
void setCallingBell(String filePath);
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| filePath    | String  | 铃音资源路径   |

### enableMuteMode
[](id:enableMuteMode)

开启静音模式。

```java
void enableMuteMode(boolean enable);
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| enable    | boolean  | 是否开启静音模式   |

### enableCustomViewRoute
[](id:enableCustomViewRoute)

开启自定义视图。
开启后，会在呼叫/被叫开始回调中，接收到 CallingView 的实例，由开发者自行决定展示方式。
>! 必须全屏或者与屏幕等比例展示，否则会有展示异常。

```java
void enableCustomViewRoute(boolean enable);
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| enable    | boolean  | 是否开启自定义视图   |


## TUICallingListener 回调函数

### shouldShowOnCallView
[](id:shouldShowOnCallView)

是否同意被叫时请求拉起接听页面。

```java
boolean shouldShowOnCallView();
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| 返回值    | boolean  |  是否同意   |

### onCallStart
[](id:onCallStart)

呼叫开始回调。主叫、被叫均会触发。

```java
 void onCallStart(String[] userIDs, TUICalling.Type type, TUICalling.Role role, View tuiCallingView);
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| userIDs    | String[]  | 通话用户 ID 列表。      |
| type | TUICalling.Type | 通话类型：音频/视频 |
| role | TUICalling.Role | 用户角色类型：主叫/被叫 |
| tuiCallingView | View | 通话视图 View。enableCustomViewRoute 设置为 false 时，view 为 null |

### onCallEnd
[](id:onCallEnd)

通话结束回调。主叫、被叫均会触发。

```java
 void onCallEnd(String[] userIDs, TUICalling.Type type, TUICalling.Role role, long totalTime);
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| userIDs    | String[]  | 通话用户 ID 列表      |
| type | TUICalling.Type | 通话类型：音频/视频 |
| role | TUICalling.Role | 用户角色类型：主叫/被叫 |
| totalTime | long | 通话时长，单位：秒 |

### onCallEvent
[](id:onCallEvent)

通话事件回调。

```java
void onCallEvent(TUICalling.Event event, TUICalling.Type type, TUICalling.Role role, String message);
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| event    | TUICalling.Event  | 通话事件类型      |
| type | TUICalling.Type | 通话类型：音频/视频 |
| role | TUICalling.Role | 用户角色类型：主叫/被叫 |
| message | String | 事件的描述信息 |





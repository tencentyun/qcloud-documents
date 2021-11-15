TUICalling 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持1v1和多人视频通话。TUICalling 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [实时语音通话（iOS）](https://cloud.tencent.com/document/product/647/42046)。

- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时音视频通话组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 发送和处理信令消息。


## TUICalling API 概览
[](id:TUICalling)
 
#### SDK 基础函数

| API                                             | 描述                                             |
| ----------------------------------------------- | ------------------------------------------------ |
| [sharedInstance](#sharedinstance)               | 组件单例。                                       |
| [call](#call) | C2C 邀请通话。                                   |
| [receiveAPNSCalled](#receiveAPNSCalled)                     | 作为被邀请方接听来电。                                   |
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
| TUICallingTypeAudio | 音频通话 |
| TUICallingTypeVideo | 视频通话 |

## Role API 概览
[](id:Role)

#### 用户角色类型
| enum                 | 描述       |
| ------------------- | ---------- |
| TUICallingRoleCall | 通话发起方（主叫） |
| TTUICallingRoleCalled | 通话接听方（被叫） |

## Event API 概览
[](id:Event)

#### 事件类型
| enum                 | 描述       |
| ------------------- | ---------- |
| TUICallingEventCallStart | 通话开始 |
| TUICallingEventCallSucceed | 通话接通成功 |
| TUICallingEventCallEnd | 通话结束 |
| TUICallingEventCallFailed | 通话失败 |

## SDK 基础函数

### sharedInstance
[](id:sharedInstance)

sharedInstance 是 TUICallingManager 的组件单例。

```objc
+ (instancetype)shareInstance;
```

### call
[](id:call)

C2C 邀请通话。

```objc
- (void)call:(NSArray<NSString *> *)userIDs type:(TUICallingType)type;
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| userIDs    | NSArray  | 通话用户 ID 列表      |
| type | TUICallingType | 通话类型：音频/视频 |

### receiveAPNSCalled
[](id:receiveAPNSCalled)

作为被邀请方接听来电。

```objc
- (void)receiveAPNSCalled:(NSArray<NSString *> *)userIDs type:(TUICallingType)type;
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| userIDs    | NSArray  | 通话用户 ID 列表      |
| type | TUICallingType | 通话类型：音频/视频 |

### setCallingListener
[](id:setCallingListener)

设置监听器。

```objc
- (void)setCallingListener:(id<TUICallingListerner>)listener;
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| listener    | TUICallingListener  | TUIcalling 组件监听器   |

### setCallingBell
[](id:setCallingBell)

设置铃声（建议在30s以内）。

```objc
- (void)setCallingBell:(NSString *)filePath;
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| filePath    | NSString  | 铃音资源路径   |

### enableMuteMode
[](id:enableMuteMode)

开启静音模式。

```objc
- (void)enableMuteMode:(BOOL)enable;
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| enable    | BOOL  | 是否开启静音模式   |

### enableCustomViewRoute
[](id:enableCustomViewRoute)

开启自定义视图。
开启后，会在呼叫/被叫开始回调中，接收到 CallingViewController 的实例，由开发者自行决定展示方式。
>! 必须全屏展示，否则会有展示异常。

```objc
- (void)enableCustomViewRoute:(BOOL)enable;
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| enable    | BOOL  | 是否开启自定义视图   |


## TUICallingListener 回调函数

### shouldShowOnCallView
[](id:shouldShowOnCallView)

是否同意被叫时请求拉起接听页面。

```objc
- (BOOL)shouldShowOnCallView;
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| 返回值    | BOOL  |  是否同意   |

### onCallStart
[](id:onCallStart)

呼叫开始回调。主叫、被叫均会触发。

```objc
 - (void)callStart:(NSArray<NSString *> *)userIDs type:(TUICallingType)type role:(TUICallingRole)role viewController:(UIViewController * _Nullable)viewController;
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| userIDs    | NSArray  | 通话用户 ID 列表      |
| type | TUICallingType | 通话类型：音频/视频 |
| role | TUICallingRole | 用户角色类型：主叫/被叫 |
| viewController | UIViewController | 通话视图 ViewController  |

### onCallEnd
[](id:onCallEnd)

通话结束回调。主叫、被叫均会触发。enableCustomViewRoute 设置为 NO 时，此回调方法不会触发。

```objc
 - (void)callEnd:(NSArray<NSString *> *)userIDs type:(TUICallingType)type role:(TUICallingRole)role totalTime:(CGFloat)totalTime;
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| userIDs    | NSArray | 通话用户 ID 列表      |
| type | TUICallingType | 通话类型：音频/视频 |
| role | TUICallingRole | 用户角色类型：主叫/被叫 |
| totalTime | CGFloat | 通话时长，单位：秒  |

### onCallEvent
[](id:onCallEvent)

通话事件回调。enableCustomViewRoute 设置为 NO 时，此回调方法不会触发。

```objc
- (void)onCallEvent:(TUICallingEvent)event type:(TUICallingType)type role:(TUICallingRole)role message:(NSString *)message;
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| event    | TUICallingEvent  | 通话事件类型。      |
| type | TUICallingType | 通话类型：音频/视频 |
| role | TUICallingRole | 用户角色类型：主叫/被叫 |
| message | NSString | 事件的描述信息 |





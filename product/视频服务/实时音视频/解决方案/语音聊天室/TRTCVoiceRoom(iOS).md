TRTCVoiceRoom 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的组件，支持以下功能：

- 房主创建新的语音聊天室开播，听众进入语聊房间收听/互动。
- 房主可以邀请听众上麦、将座位上的麦上主播踢下麦。
- 房主还能对座位进行封禁，其他听众就不能再进行申请上麦了。
- 听众可以申请上麦，变成麦上主播，可以和其他人语音互动，也可以随时下麦成为普通的听众。
- 支持发送各种文本消息和自定义消息，自定义消息可用于实现弹幕、点赞和礼物等。

TRTCVoiceRoom 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [语音聊天室（iOS）](https://cloud.tencent.com/document/product/647/45753)。

- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时语音聊天组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 的 AVChatroom 实现聊天室的功能，同时，通过 IM 的属性接口来存储麦位表等房间信息，邀请信令可以用于上麦申请/抱麦申请。


<h2 id="TRTCVoiceRoom">TRTCVoiceRoom API 概览</h2>

### SDK 基础函数

| API                                             | 描述                     |
| ----------------------------------------------- | ------------------------ |
| [sharedInstance](#sharedinstance)               | 获取单例对象。           |
| [destroySharedInstance](#destroysharedinstance) | 销毁单例对象。           |
| [setDelegate](#setdelegate)                     | 设置事件回调。           |
| [setDelegateHandler](#setdelegatehandler)       | 设置事件回调所在的线程。 |
| [login](#login)                                 | 登录。                   |
| [logout](#logout)                               | 登出。                   |
| [setSelfProfile](#setselfprofile)               | 修改个人信息。           |

### 房间相关接口函数

| API                                 | 描述                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| [createRoom](#createroom)           | 创建房间（房主调用），若房间不存在，系统将自动创建一个新房间。 |
| [destroyRoom](#destroyroom)         | 销毁房间（房主调用）。                                       |
| [enterRoom](#enterroom)             | 进入房间（听众调用）。                                       |
| [exitRoom](#exitroom)               | 退出房间（听众调用）。                                       |
| [getRoomInfoList](#getroominfolist) | 获取房间列表的详细信息。                                     |
| [getUserInfoList](#getuserinfolist) | 获取指定 userId 的用户信息，如果为 nil，则获取房间内所有人的信息。 |

### 麦位管理接口

| API                     | 描述                                |
| ----------------------- | ----------------------------------- |
| [enterSeat](#enterseat) | 主动上麦（听众端和房主均可调用）。  |
| [moveSeat](#moveseat)   | 移动麦位 (麦上主播端可调用) 。 |
| [leaveSeat](#leaveseat) | 主动下麦（主播调用）。  |
| [pickSeat](#pickseat)   | 抱人上麦（房主调用）。              |
| [kickSeat](#kickseat)   | 踢人下麦（房主调用）。              |
| [muteSeat](#muteseat)   | 静音/解除静音某个麦位（房主调用）。 |
| [closeSeat](#closeseat) | 封禁/解禁某个麦位（房主调用）。     |

### 本地音频操作接口

| API                                             | 描述                 |
| ----------------------------------------------- | -------------------- |
| [startMicrophone](#startmicrophone)             | 开启麦克风采集。     |
| [stopMicrophone](#stopmicrophone)               | 停止麦克风采集。     |
| [setAudioQuality](#setaudioquality)             | 设置音质。           |
| [muteLocalAudio](#mutelocalaudio)               | 开启/关闭本地静音。  |
| [setSpeaker](#setspeaker)                       | 设置开启扬声器。     |
| [setAudioCaptureVolume](#setaudiocapturevolume) | 设置麦克风采集音量。 |
| [setAudioPlayoutVolume](#setaudioplayoutvolume) | 设置播放音量。       |
| [setVoiceEarMonitorEnable](#setvoiceearmonitorenable) | 开启/关闭 耳返。       |


### 远端用户音频操作接口

| API                                       | 描述                    |
| ----------------------------------------- | ----------------------- |
| [muteRemoteAudio](#muteremoteaudio)       | 静音/解除静音指定成员。 |
| [muteAllRemoteAudio](#muteallremoteaudio) | 静音/解除静音所有成员。 |

### 背景音乐音效相关接口

| API                                             | 描述                                                         |
| ----------------------------------------------- | ------------------------------------------------------------ |
| [getAudioEffectManager](#getaudioeffectmanager) | 获取背景音乐音效管理对象 [TXAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXAudioEffectManager__android.html#interfacecom_1_1tencent_1_1liteav_1_1audio_1_1TXAudioEffectManager)。 |

### 消息发送相关接口

| API                                     | 描述                                     |
| --------------------------------------- | ---------------------------------------- |
| [sendRoomTextMsg](#sendroomtextmsg)     | 在房间中广播文本消息，一般用于弹幕聊天。 |
| [sendRoomCustomMsg](#sendroomcustommsg) | 发送自定义文本消息。                     |

### 邀请信令相关接口

| API                                   | 描述             |
| ------------------------------------- | ---------------- |
| [sendInvitation](#sendinvitation)     | 向用户发送邀请。 |
| [acceptInvitation](#acceptinvitation) | 接受邀请。       |
| [rejectInvitation](#rejectinvitation) | 拒绝邀请。       |
| [cancelInvitation](#cancelinvitation) | 取消邀请。       |

<h2 id="TRTCVoiceRoomDelegate">TRTCVoiceRoomDelegate API 概览</h2>

### 通用事件回调

| API                       | 描述       |
| ------------------------- | ---------- |
| [onError](#onerror)       | 错误回调。 |
| [onWarning](#onwarning)   | 警告回调。 |
| [onDebugLog](#ondebuglog) | Log 回调。 |

### 房间事件回调

| API                                       | 描述                   |
| ----------------------------------------- | ---------------------- |
| [onRoomDestroy](#onroomdestroy)           | 房间被销毁的回调。     |
| [onRoomInfoChange](#onroominfochange)     | 语聊房间信息变更回调。 |
| [onUserVolumeUpdate](#onuservolumeupdate) | 用户通话音量回调。     |

### 麦位变更回调

| API                                     | 描述                                  |
| --------------------------------------- | ------------------------------------- |
| [onSeatListChange](#onseatlistchange)   | 全量的麦位列表变化。                  |
| [onAnchorEnterSeat](#onanchorenterseat) | 有成员上麦（主动上麦/房主抱人上麦）。 |
| [onAnchorLeaveSeat](#onanchorleaveseat) | 有成员下麦（主动下麦/房主踢人下麦）。 |
| [onSeatMute](#onseatmute)               | 房主禁麦。                            |
| [onUserMicrophoneMute](#onusermicrophonemute)               | 用户麦克风是否静音。                          |
| [onSeatClose](#onseatclose)             | 房主封麦。                            |

### 听众进出事件回调

| API                                 | 描述               |
| ----------------------------------- | ------------------ |
| [onAudienceEnter](#onaudienceenter) | 收到听众进房通知。 |
| [onAudienceExit](#onaudienceexit)   | 收到听众退房通知。 |

### 消息事件回调

| API                                         | 描述             |
| ------------------------------------------- | ---------------- |
| [onRecvRoomTextMsg](#onrecvroomtextmsg)     | 收到文本消息。   |
| [onRecvRoomCustomMsg](#onrecvroomcustommsg) | 收到自定义消息。 |

### 信令事件回调

| API                                               | 描述               |
| ------------------------------------------------- | ------------------ |
| [onReceiveNewInvitation](#onreceivenewinvitation) | 收到新的邀请请求。 |
| [onInviteeAccepted](#oninviteeaccepted)           | 被邀请人接受邀请。 |
| [onInviteeRejected](#oninviteerejected)           | 被邀请人拒绝邀请。 |
| [onInvitationCancelled](#oninvitationcancelled)   | 邀请人取消邀请。   |

## SDK 基础函数

[](id:sharedInstance)

### sharedInstance

获取 [TRTCVoiceRoom](https://cloud.tencent.com/document/product/647/45737) 单例对象。

```Objective-C
/**
* 获取 TRTCVoiceRoom 单例对象
*
* - returns: TRTCVoiceRoom 实例
* - note: 可以调用 {@link TRTCVoiceRoom#destroySharedInstance()} 销毁单例对象
*/
+ (instancetype)sharedInstance NS_SWIFT_NAME(shared());
```


### destroySharedInstance

销毁 [TRTCVoiceRoom](https://cloud.tencent.com/document/product/647/45753) 单例对象。

>?销毁实例后，外部缓存的 TRTCVoiceRoom 实例无法再使用，需要重新调用 [sharedInstance](#sharedInstance) 获取新实例。

```Objective-C
/**
* 销毁 TRTCVoiceRoom 单例对象
*
* - note: 销毁实例后，外部缓存的 TRTCVoiceRoom 实例不能再使用，需要重新调用 {@link TRTCVoiceRoom#sharedInstance()} 获取新实例
*/
+ (void)destroySharedInstance NS_SWIFT_NAME(destroyShared());
```

### setDelegate

[TRTCVoiceRoom](https://cloud.tencent.com/document/product/647/45753) 事件回调，您可以通过 TRTCVoiceRoomDelegate 获得 [TRTCVoiceRoom](https://cloud.tencent.com/document/product/647/45737) 的各种状态通知。

```Objective-C
/**
* 设置组件回调接口
* 
* 您可以通过 TRTCVoiceRoomDelegate 获得 TRTCVoiceRoom 的各种状态通知
*
* - parameter delegate 回调接口
* - note: TRTCVoiceRoom 中的回调事件，默认是在 Main Queue 中回调给您；如果您需要指定事件回调所在的队列，可使用 {@link TRTCVoiceRoom#setDelegateQueue(queue)}
*/
- (void)setDelegate:(id<TRTCVoiceRoomDelegate>)delegate NS_SWIFT_NAME(setDelegate(delegate:));
```

>?setDelegate 是 TRTCVoiceRoom 的代理回调。   

### setDelegateQueue

设置事件回调所在的线程队列，默认发送动主线程 MainQueue 中。

```Objective-C
/**
* 设置事件回调所在的队列
*
* - parameter queue 队列，TRTCVoiceRoom 中的各种状态通知回调，会派发到您指定的queue。
*/
- (void)setDelegateQueue:(dispatch_queue_t)queue NS_SWIFT_NAME(setDelegateQueue(queue:));

```

参数如下表所示：

| 参数  | 类型             | 含义                                                         |
| ----- | ---------------- | ------------------------------------------------------------ |
| queue | dispatch_queue_t | TRTCVoiceRoom 中的各种状态通知，会派发到您指定的线程队列里去。 |

   

### login

登录。

```Objective-C
- (void)login:(int)sdkAppID
       userId:(NSString *)userId
      userSig:(NSString *)userSig
     callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(login(sdkAppID:userId:userSig:callback:));

```

参数如下表所示：

| 参数     | 类型           | 含义                                                         |
| -------- | -------------- | ------------------------------------------------------------ |
| sdkAppId | int            | 您可以在**实时音视频控制台 >[应用管理](https://console.cloud.tencent.com/trtc/app)**> 应用信息中查看 SDKAppID。 |
| userId   | NSString       | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。 |
| userSig  | NSString       | 腾讯云设计的一种安全保护签名，获取方式请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |
| callback | ActionCallback | 登录回调，成功时 code 为0。                                  |

   

### logout

登出。

```Objective-C
- (void)logout:(ActionCallback _Nullable)callback NS_SWIFT_NAME(logout(callback:));
```

参数如下表所示：

| 参数     | 类型           | 含义                        |
| -------- | -------------- | --------------------------- |
| callback | ActionCallback | 登出回调，成功时 code 为0。 |

   

### setSelfProfile

修改个人信息。

```Objective-C
- (void)setSelfProfile:(NSString *)userName avatarURL:(NSString *)avatarURL callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(setSelfProfile(userName:avatarURL:callback:));
```

参数如下表所示：

| 参数      | 类型           | 含义                                |
| --------- | -------------- | ----------------------------------- |
| userName  | NSString       | 昵称。                              |
| avatarURL | NSString       | 头像地址。                          |
| callback  | ActionCallback | 个人信息设置回调，成功时 code 为0。 |

   


## 房间相关接口函数

### createRoom

创建房间（房主调用）。

```Objective-C
- (void)createRoom:(int)roomID roomParam:(VoiceRoomParam *)roomParam callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(createRoom(roomID:roomParam:callback:));
```

参数如下表所示：

| 参数      | 类型                | 含义                                                         |
| --------- | ------------------- | ------------------------------------------------------------ |
| roomId    | int                 | 房间标识，需要由您分配并进行统一管理。多个 roomID 可以汇总成一个语聊房间列表，腾讯云暂不提供语聊房间列表的管理服务，请自行管理您的语聊房间列表。 |
| roomParam | VoiceRoomParam | 房间信息，用于房间描述的信息。例如房间名称、麦位信息、封面信息等。如果需要麦位管理，必须要填入房间的麦位数。 |
| callback  | ActionCallback      | 创建房间的结果回调，成功时 code 为0。                        |

房主开播的正常调用流程如下： 
1. 房主调用 `createRoom` 创建新的语音聊天室，此时传入房间 ID、上麦是否需要房主确认、麦位数等房间属性信息。
2. 房主创建房间成功后，调用 `enterSeat` 进入座位。
3. 房主收到组件的 `onSeatListChange` 麦位表变化事件通知，此时可以将麦位表变化刷新到 UI 界面上。
4. 房主还会收到麦位表有成员进入的 `onAnchorEnterSeat` 的事件通知，此时会自动打开麦克风采集。

   

### destroyRoom

销毁房间（房主调用）。房主在创建房间后，可以调用这个函数来销毁房间。

```Objective-C
- (void)destroyRoom:(ActionCallback _Nullable)callback NS_SWIFT_NAME(destroyRoom(callback:));
```

参数如下表所示：

| 参数     | 类型           | 含义                                  |
| -------- | -------------- | ------------------------------------- |
| callback | ActionCallback | 销毁房间的结果回调，成功时 code 为0。 |


### enterRoom

进入房间（听众调用）。

```Objective-C
- (void)enterRoom:(NSInteger)roomID callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(enterRoom(roomID:callback:));
```

参数如下表所示：

| 参数     | 类型           | 含义                                  |
| -------- | -------------- | ------------------------------------- |
| roomId   | NSInteger            | 房间标识。                            |
| callback | ActionCallback | 进入房间的结果回调，成功时 code 为0。 |


听众进房收听的正常调用流程如下： 

1. 听众向您的服务端获取最新的语音聊天室列表，可能包含多个语聊房间的 roomId 和房间信息。
2. 听众选择一个语音聊天室，调用 `enterRoom` 并传入房间号即可进入该房间。
3. 进房后会收到组件的 `onRoomInfoChange` 房间属性变化事件通知，此时可以记录房间属性并做相应改变，例如 UI 展示房间名、记录上麦是否需要请求房主同意等。
4. 进房后会收到组件的 `onSeatListChange` 麦位表变化事件通知，此时可以将麦位表变化刷新到 UI 界面上。
5. 进房后还会收到麦位表有主播进入的 `onAnchorEnterSeat` 的事件通知。

### exitRoom

退出房间。

```Objective-C
- (void)exitRoom:(ActionCallback _Nullable)callback NS_SWIFT_NAME(exitRoom(callback:));
```

参数如下表所示：

| 参数     | 类型           | 含义                                  |
| -------- | -------------- | ------------------------------------- |
| callback | ActionCallback | 退出房间的结果回调，成功时 code 为0。 |

   

### getRoomInfoList

获取房间列表的详细信息，其中房间名称、房间封面是房主在创建 `createRoom()` 时通过 roomInfo 设置的。

>?如果房间列表和房间信息都由您自行管理，可忽略该函数。


```Objective-C
- (void)getRoomInfoList:(NSArray<NSNumber *> *)roomIdList callback:(VoiceRoomInfoCallback _Nullable)callback NS_SWIFT_NAME(getRoomInfoList(roomIdList:callback:));
```

参数如下表所示：

| 参数       | 类型                | 含义               |
| ---------- | ------------------- | ------------------ |
| roomIdList | NSArray&lt;NSNumber&gt; | 房间号列表。       |
| callback   | RoomInfoCallback    | 房间详细信息回调。 |


### getUserInfoList

获取指定 userId 的用户信息。

```Objective-C
- (void)getUserInfoList:(NSArray<NSString *> * _Nullable)userIDList callback:(VoiceRoomUserListCallback _Nullable)callback NS_SWIFT_NAME(getUserInfoList(userIDList:callback:));
```

参数如下表所示：

| 参数             | 类型               | 含义                                                         |
| ---------------- | ------------------ | ------------------------------------------------------------ |
| userIdList       | NSArray&lt;NSString&gt; | 需要获取的用户 ID 列表，如果为 null，则获取房间内所有人的信息。 |
| userlistcallback | UserListCallback   | 用户详细信息回调。                                           |


## 麦位管理接口

### enterSeat

主动上麦（听众端和房主均可调用）。

>?上麦成功后，房间内所有成员会收到 `onSeatListChange` 和 `onAnchorEnterSeat` 的事件通知。

```Objective-C
- (void)enterSeat:(NSInteger)seatIndex callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(enterSeat(seatIndex:callback:));
```

参数如下表所示：

| 参数      | 类型           | 含义                 |
| --------- | -------------- | -------------------- |
| seatIndex | NSInteger      | 需要上麦的麦位序号。 |
| callback  | ActionCallback | 操作回调。           |

调用该接口会立即修改麦位表。如果是听众申请上麦需要房主同意的场景，可以先调用 `sendInvitation` 向房主申请，收到 `onInvitationAccept ` 后再调用该函数。

### moveSeat
移动麦位 (麦上主播端可调用)。
>? 移动麦位成功后，房间内所有成员会收到 `onSeatListChange`、 `onAnchorLeaveSeat` 和 `onAnchorEnterSeat` 的事件通知。(主播调用后，只是修改麦位座位号信息，并不会切换该用户的主播身份。)

```Objective-C
- (NSInteger)moveSeat:(NSInteger)seatIndex callback:(ActionCallback _Nullable)callback
NS_SWIFT_NAME(moveSeat(seatIndex:callback:))
```
参数如下表所示：

| 参数      | 类型           | 含义                 |
| --------- | -------------- | -------------------- |
| seatIndex | NSInteger      | 需要移动到的麦位序号。 |
| callback  | ActionCallback | 操作回调。           |

返回值：

| 返回值   | 类型   | 含义                  |
| -------- | --------- | --------------------- |
| code     | NSInteger | 移动麦位操作结果（0为成功，其它为失败，10001为接口调用限频）。 |

调用该接口会立即修改麦位表。如果是听众申请上麦需要房主同意的场景，可以先调用 `sendInvitation` 向房主申请，收到 `onInvitationAccept` 后再调用该函数。

### leaveSeat

主动下麦（主播调用）。

>? 下麦成功后，房间内所有成员会收到 `onSeatListChange` 和 `onAnchorLeaveSeat` 的事件通知。

```Objective-C
- (void)leaveSeat:(ActionCallback _Nullable)callback NS_SWIFT_NAME(leaveSeat(callback:));
```

参数如下表所示：

| 参数     | 类型           | 含义       |
| -------- | -------------- | ---------- |
| callback | ActionCallback | 操作回调。 |

### pickSeat

抱人上麦（房主调用）。

>? 房主抱人上麦，房间内所有成员会收到 `onSeatListChange` 和 `onAnchorEnterSeat` 的事件通知。

```Objective-C
- (void)pickSeat:(NSInteger)seatIndex userId:(NSString *)userId callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(pickSeat(seatIndex:userId:callback:));
```

参数如下表所示：

| 参数      | 类型           | 含义                   |
| --------- | -------------- | ---------------------- |
| seatIndex | NSInteger      | 需要抱上麦的麦位序号。 |
| userId    | NSString       | 用户 ID。              |
| callback  | ActionCallback | 操作回调。             |

调用该接口会立即修改麦位表。如果是房主需要听众同意，听众才会上麦的场景，可以先调用 `sendInvitation` 向听众申请，收到 `onInvitationAccept `后再调用该函数。


### kickSeat

踢人下麦（房主调用）。

>? 房主踢人下麦，房间内所有成员会收到 `onSeatListChange` 和 `onAnchorLeaveSeat` 的事件通知。

```Objective-C
- (void)kickSeat:(NSInteger)seatIndex callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(kickSeat(seatIndex:callback:));
```

参数如下表所示：

| 参数      | 类型           | 含义                   |
| --------- | -------------- | ---------------------- |
| seatIndex | NSInteger      | 需要踢下麦的麦位序号。 |
| callback  | ActionCallback | 操作回调。             |

调用该接口会立即修改麦位表。

### muteSeat

静音/解除静音某个麦位（房主调用）。

>? 静音/解除静音某个麦位，房间内所有成员会收到 `onSeatListChange` 和 `onSeatMute` 的事件通知。

```Objective-C
- (void)muteSeat:(NSInteger)seatIndex isMute:(BOOL)isMute callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(muteSeat(seatIndex:isMute:callback:));
```

参数如下表所示：

| 参数      | 类型           | 含义                                          |
| --------- | -------------- | --------------------------------------------- |
| seatIndex | NSInteger      | 需要操作的麦位序号。                          |
| isMute    | BOOL           | YES：静音对应麦位；NO：解除静音对应麦位。 |
| callback  | ActionCallback | 操作回调。                                    |

调用该接口会立即修改麦位表。对应 seatIndex 座位上的主播，会自动调用 muteAudio 进行静音/解禁。

### closeSeat

封禁/解禁某个麦位（房主调用）。

>? 房主封禁/解禁对应麦位，房间内所有成员会收到 `onSeatListChange` 和 `onSeatClose` 的事件通知。

```Objective-C
- (void)closeSeat:(NSInteger)seatIndex isClose:(BOOL)isClose callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(closeSeat(seatIndex:isClose:callback:));
```

参数如下表所示：

| 参数      | 类型           | 含义                                       |
| --------- | -------------- | ------------------------------------------ |
| seatIndex | NSInteger      | 需要操作的麦位序号。                       |
| isClose   | BOOL           | YES：封禁对应麦位； NO：解封对应麦位。 |
| callback  | ActionCallback | 操作回调。                                 |

调用该接口会立即修改麦位表。封禁对应 seatIndex 座位上的主播，会自动下麦。


## 本地音频操作接口

### startMicrophone

开启麦克风采集。

```Objective-C
- (void)startMicrophone;
```

### stopMicrophone

停止麦克风采集。

```Objective-C
- (void)stopMicrophone;
```

### setAudioQuality

设置音质。

```Objective-C
- (void)setAuidoQuality:(NSInteger)quality NS_SWIFT_NAME(setAuidoQuality(quality:));
```

参数如下表所示：

| 参数    | 类型 | 含义                                                         |
| ------- | ---------- | ------------------------------------------------------------ |
| quality | NSInteger  | 音频质量，详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a955cccaddccb0c993351c656067bee55)。 |


### muteLocalAudio

静音/取消静音本地的音频。

```Objective-C
- (void)muteLocalAudio:(BOOL)mute NS_SWIFT_NAME(muteLocalAudio(mute:));
```

参数如下表所示：

| 参数 | 类型    | 含义                                                         |
| ---- | ------- | ------------------------------------------------------------ |
| mute | BOOL    | 静音/取消静音，详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a37f52481d24fa0f50842d3d8cc380d86)。 |



### setSpeaker

设置开启扬声器。

```Objective-C
- (void)setSpeaker:(BOOL)userSpeaker NS_SWIFT_NAME(setSpeaker(userSpeaker:));
```

参数如下表所示：

| 参数       | 类型    | 含义                        |
| ---------- | ------- | --------------------------- |
| useSpeaker | BOOL    | YES：扬声器；NO：听筒。 |



### setAudioCaptureVolume

设置麦克风采集音量。

```Objective-C
- (void)setAudioCaptureVolume:(NSInteger)voluem NS_SWIFT_NAME(setAudioCaptureVolume(volume:));
```

参数如下表所示：

| 参数   | 类型 | 含义                          |
| ------ | ---- | ----------------------------- |
| volume | NSInteger  | 采集音量，0 - 100， 默认100。 |


### setAudioPlayoutVolume

设置播放音量。

```Objective-C
- (void)setAudioPlayoutVolume:(NSInteger)volume NS_SWIFT_NAME(setAudioPlayoutVolume(volume:));
```

参数如下表所示：

| 参数   | 类型 | 含义                          |
| ------ | ---------- | ----------------------------- |
| volume | NSInteger  | 播放音量，0 - 100， 默认100。 |

### muteRemoteAudio

静音/解除静音指定成员。

```Objective-C
- (void)muteRemoteAudio:(NSString *)userId mute:(BOOL)mute NS_SWIFT_NAME(muteRemoteAudio(userId:mute:));
```

参数如下表所示：

| 参数   | 类型    | 含义                              |
| ------ | ------- | --------------------------------- |
| userId | NSString  | 指定的用户 ID。                   |
| mute   | BOOL      | YES：开启静音；NO：关闭静音。 |

### muteAllRemoteAudio

静音/解除静音所有成员。

```Objective-C
- (void)muteAllRemoteAudio:(BOOL)isMute NS_SWIFT_NAME(muteAllRemoteAudio(isMute:));
```

参数如下表所示：

| 参数 | 类型    | 含义                              |
| ---- | ------- | --------------------------------- |
| mute | BOOL | YES：开启静音；NO：关闭静音。 |

### setVoiceEarMonitorEnable

开启/关闭 耳返。

```Objective-C
- (void)setVoiceEarMonitorEnable:(BOOL)enable NS_SWIFT_NAME(setVoiceEarMonitor(enable:));
```
参数如下表所示：

| 参数 | 类型    | 含义                              |
| ---- | ------- | --------------------------------- |
| enable | BOOL | YES：开启耳返；NO：关闭耳返。 |


## 背景音乐音效相关接口函数

### getAudioEffectManager

获取背景音乐音效管理对象 [TXAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3646dad993287c3a1a38a5bc0e6e33aa)。

```Objective-C
- (TXAudioEffectManager * _Nullable)getAudioEffectManager;
```


## 消息发送相关接口函数

### sendRoomTextMsg

在房间中广播文本消息，一般用于弹幕聊天。

```Objective-C
- (void)sendRoomTextMsg:(NSString *)message callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(sendRoomTextMsg(message:callback:));
```

参数如下表所示：

| 参数     | 类型           | 含义           |
| -------- | -------------- | -------------- |
| message  | NSString       | 文本消息。     |
| callback | ActionCallback | 发送结果回调。 |

   

### sendRoomCustomMsg

发送自定义文本消息。

```Objective-C
- (void)sendRoomCustomMsg:(NSString *)cmd message:(NSString *)message callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(sendRoomCustomMsg(cmd:message:callback:));
```

参数如下表所示：

| 参数     | 类型           | 含义                                               |
| -------- | -------------- | -------------------------------------------------- |
| cmd      | NSString        | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message  | NSString        | 文本消息。                                         |
| callback | ActionCallback | 发送结果回调。                                     |

   

## 邀请信令相关接口

### sendInvitation

向用户发送邀请。

```Objective-C
- (NSString *)sendInvitation:(NSString *)cmd
                      userId:(NSString *)userId
                     content:(NSString *)content
                    callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(sendInvitation(cmd:userId:content:callback:));
```

参数如下表所示：

| 参数     | 类型           | 含义             |
| -------- | -------------- | ---------------- |
| cmd      | NSString       | 业务自定义指令。 |
| userId   | NSString       | 邀请的用户 ID。  |
| content  | NSString       | 邀请的内容。     |
| callback | ActionCallback | 发送结果回调。   |

返回值：

| 返回值   | 类型   | 含义                  |
| -------- | ------ | --------------------- |
| inviteId | NSString | 用于标识此次邀请 ID。 |

### acceptInvitation

接受邀请。

```Objective-C
- (void)acceptInvitation:(NSString *)identifier callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(acceptInvitation(id:callback:));
```

参数如下表所示：

| 参数     | 类型           | 含义           |
| -------- | -------------- | -------------- |
| id       | NSString       | 邀请 ID。      |
| callback | ActionCallback | 发送结果回调。 |

### rejectInvitation

拒绝邀请。

```Objective-C
- (void)rejectInvitation:(NSString *)identifier callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(rejectInvitation(id:callback:));
```

参数如下表所示：

| 参数     | 类型           | 含义           |
| -------- | -------------- | -------------- |
| id       | NSString       | 邀请 ID。      |
| callback | ActionCallback | 发送结果回调。 |


### cancelInvitation

取消邀请。

```Objective-C
- (void)cancelInvitation:(NSString *)identifier callback:(ActionCallback _Nullable)callback NS_SWIFT_NAME(cancelInvitation(id:callback:));
```

参数如下表所示：

| 参数     | 类型           | 含义           |
| -------- | -------------- | -------------- |
| id       | NSString       | 邀请 ID。      |
| callback | ActionCallback | 发送结果回调。 |

[](id:TRTCVoiceRoomDelegate)
## TRTCVoiceRoomDelegate 事件回调

## 通用事件回调

### onError

错误回调。

>? SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```Objective-C
- (void)onError:(int)code
                message:(NSString*)message
NS_SWIFT_NAME(onError(code:message:));
```

参数如下表所示：

| 参数    | 类型   | 含义       |
| ------- | ------ | ---------- |
| code    | int    | 错误码。   |
| message | NSString | 错误信息。 |


### onWarning

警告回调。

```Objective-C
- (void)onWarning:(int)code
                  message:(NSString *)message
NS_SWIFT_NAME(onWarning(code:message:));
```

参数如下表所示：

| 参数    | 类型   | 含义       |
| ------- | ------ | ---------- |
| code    | int    | 错误码。   |
| message | NSString | 警告信息。 |

   

### onDebugLog

Log 回调。

```Objective-C
- (void)onDebugLog:(NSString *)message
NS_SWIFT_NAME(onDebugLog(message:));
```

参数如下表所示：

| 参数    | 类型   | 含义       |
| ------- | ------ | ---------- |
| message | NSString | 日志信息。 |

   


## 房间事件回调

### onRoomDestroy

房间被销毁的回调。房主解散房间时，房间内的所有用户都会收到此通知。

```Objective-C
- (void)onRoomDestroy:(NSString *)roomId
NS_SWIFT_NAME(onRoomDestroy(roomId:));
```

参数如下表所示：

| 参数   | 类型   | 含义      |
| ------ | ------ | --------- |
| roomId | NSString | 房间 ID。 |


### onRoomInfoChange

进房成功后会回调该接口，roomInfo 中的信息在房主创建房间的时候传入。

```Objective-C
- (void)onRoomInfoChange:(VoiceRoomInfo *)roomInfo
NS_SWIFT_NAME(onRoomInfoChange(roomInfo:));
```

参数如下表所示：

| 参数     | 类型     | 含义       |
| -------- | -------- | ---------- |
| roomInfo | VoiceRoomInfo | 房间信息。 |


### onUserMicrophoneMute

用户麦克风是否静音回调，当用户调用muteLocalAudio，房间内的其他用户都会收到此通知。

```Objective-C
- (void)onUserMicrophoneMute:(NSString *)userId mute:(BOOL)mute
NS_SWIFT_NAME(onUserMicrophoneMute(userId:mute:));

```

参数如下表所示：

| 参数   | 类型   | 含义                      |
| ------ | ------ | ------------------------- |
| userId | NSString | 用户 ID。                 |
| mute | BOOL    | YES：静音麦位； NO：解除静音。 |


### onUserVolumeUpdate

启用音量大小提示，会通知每个成员的音量大小。

```Objective-C
- (void)onUserVolumeUpdate:(NSArray<TRTCVolumeInfo *> *)userVolumes totalVolume:(NSInteger)totalVolume
NS_SWIFT_NAME(onUserVolumeUpdate(userVolumes:totalVolume:));
```

参数如下表所示：

| 参数   | 类型   | 含义                      |
| ------ | ------ | ------------------------- |
| userVolumes | NSArray | 用户列表。                 |
| totalVolume | NSInteger    | 音量大小，取值：0 - 100。 |


## 麦位回调

### onSeatListChange

全量的麦位列表变化，包含了整个麦位表。

```Objective-C
- (void)onSeatInfoChange:(NSArray<VoiceRoomSeatInfo *> *)seatInfolist
NS_SWIFT_NAME(onSeatListChange(seatInfoList:));
```

参数如下表所示：

| 参数         | 类型                 | 含义             |
| ------------ | -------------------- | ---------------- |
| seatInfoList | NSArray&lt;VoiceRoomSeatInfo&gt; | 全量的麦位列表。 |

### onAnchorEnterSeat

有成员上麦(主动上麦/房主抱人上麦)。

```Objective-C
- (void)onAnchorEnterSeat:(NSInteger)index
                              user:(VoiceRoomUserInfo *)user
NS_SWIFT_NAME(onAnchorEnterSeat(index:user:));
```

参数如下表所示：

| 参数  | 类型     | 含义                 |
| ----- | -------- | -------------------- |
| index | NSInteger      | 成员上麦的麦位。     |
| user  | VoiceRoomUserInfo | 上麦用户的详细信息。 |

### onAnchorLeaveSeat

有成员下麦(主动下麦/房主踢人下麦)。

```Objective-C
- (void)onAnchorLeaveSeat:(NSInteger)index
                     user:(VoiceRoomUserInfo *)user
NS_SWIFT_NAME(onAnchorLeaveSeat(index:user:));
```

参数如下表所示：

| 参数  | 类型     | 含义                 |
| ----- | -------- | -------------------- |
| index | NSInteger      | 下麦的麦位。         |
| user  | VoiceRoomUserInfo | 上麦用户的详细信息。 |

### onSeatMute

房主禁麦。

```Objective-C
- (void)onSeatMute:(NSInteger)index
            isMute:(BOOL)isMute
NS_SWIFT_NAME(onSeatMute(index:isMute:));
```

参数如下表所示：

| 参数   | 类型    | 含义                               |
| ------ | ------- | ---------------------------------- |
| index  | NSInteger     | 操作的麦位。                       |
| isMute | BOOL | YES：静音麦位； NO：解除静音。 |

### onSeatClose

房主封麦。

```Objective-C
- (void)onSeatClose:(NSInteger)index
            isClose:(BOOL)isClose
NS_SWIFT_NAME(onSeatClose(index:isClose:));
```

参数如下表所示：

| 参数    | 类型    | 含义                                |
| ------- | ------- | ----------------------------------- |
| index   | NSInteger     | 操作的麦位。                        |
| isClose | BOOL | YES：封禁麦位； NO： 解禁麦位。 |

## 听众进出事件回调

### onAudienceEnter

收到听众进房通知。

```Objective-C
- (void)onAudienceEnter:(VoiceRoomUserInfo *)userInfo
NS_SWIFT_NAME(onAudienceEnter(userInfo:));
```

参数如下表所示：

| 参数     | 类型     | 含义           |
| -------- | -------- | -------------- |
| userInfo | VoiceRoomUserInfo | 进房听众信息。 |

### onAudienceExit

收到听众退房通知。

```Objective-C
- (void)onAudienceExit:(VoiceRoomUserInfo *)userInfo
NS_SWIFT_NAME(onAudienceExit(userInfo:));
```

参数如下表所示：

| 参数     | 类型     | 含义           |
| -------- | -------- | -------------- |
| userInfo | VoiceRoomUserInfo | 退房听众信息。 |

   

## 消息事件回调

### onRecvRoomTextMsg

收到文本消息。

```Objective-C
- (void)onRecvRoomTextMsg:(NSString *)message
                 userInfo:(VoiceRoomUserInfo *)userInfo
NS_SWIFT_NAME(onRecvRoomTextMsg(message:userInfo:));
```

参数如下表所示：

| 参数     | 类型     | 含义             |
| -------- | -------- | ---------------- |
| message  | NSString   | 文本消息。       |
| userInfo | VoiceRoomUserInfo | 发送者用户信息。 |

   

### onRecvRoomCustomMsg

收到自定义消息。

```Objective-C
- (void)onRecvRoomCustomMsg:(NSString *)command
                    message:(NSString *)message
                   userInfo:(VoiceRoomUserInfo *)userInfo
NS_SWIFT_NAME(onRecvRoomCustomMsg(command:message:userInfo:));
```

参数如下表所示：

| 参数     | 类型     | 含义                                               |
| -------- | -------- | -------------------------------------------------- |
| command  | NSString   | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message  | NSString   | 文本消息。                                         |
| userInfo | VoiceRoomUserInfo | 发送者用户信息。                                   |

## 邀请信令事件回调

### onReceiveNewInvitation

收到新的邀请请求。

```Objective-C
- (void)onReceiveNewInvitation:(NSString *)identifier
                       inviter:(NSString *)inviter
                           cmd:(NSString *)cmd
                       content:(NSString *)content
NS_SWIFT_NAME(onReceiveNewInvitation(id:inviter:cmd:content:));
```

参数如下表所示：

| 参数    | 类型     | 含义                               |
| ------- | -------- | ---------------------------------- |
| id      | NSString   | 邀请 ID。                          |
| inviter | NSString   | 邀请人的用户 ID。                  |
| cmd     | NSString   | 业务指定的命令字，由开发者自定义。 |
| content | NSString | 业务指定的内容。                   |

### onInviteeAccepted

被邀请者接受邀请。

```Objective-C
- (void)onInviteeAccepted:(NSString *)identifier
                  invitee:(NSString *)invitee
NS_SWIFT_NAME(onInviteeAccepted(id:invitee:));
```

参数如下表所示：

| 参数    | 类型   | 含义                |
| ------- | ------ | ------------------- |
| id      | NSString | 邀请 ID。           |
| invitee | NSString | 被邀请人的用户 ID。 |

### onInviteeRejected

被邀请者拒绝邀请。

```Objective-C
- (void)onInviteeRejected:(NSString *)identifier
                  invitee:(NSString *)invitee
NS_SWIFT_NAME(onInviteeRejected(id:invitee:));
```

参数如下表所示：

| 参数    | 类型   | 含义                |
| ------- | ------ | ------------------- |
| id      | NSString | 邀请 ID。           |
| invitee | NSString | 被邀请人的用户 ID。 |

### onInvitationCancelled

邀请人取消邀请。

```Objective-C
- (void)onInvitationCancelled:(NSString *)identifier
                      invitee:(NSString *)invitee NS_SWIFT_NAME(onInvitationCancelled(id:invitee:));
```

参数如下表所示：

| 参数    | 类型   | 含义              |
| ------- | ------ | ----------------- |
| id      | NSString | 邀请 ID。         |
| inviter | NSString | 邀请人的用户 ID。 |

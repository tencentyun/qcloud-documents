TRTCChatSalon 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的组件，支持以下功能：

- 房主创建新的语音沙龙开播，听众进入语音沙龙收听/互动。
- 房主可以邀请听众上麦、将座位上的麦上主播踢下麦。
- 听众可以申请上麦，变成麦上主播，可以和其他人语音互动，也可以随时下麦成为普通的听众。
- 支持发送各种文本消息和自定义消息，自定义消息可用于实现弹幕、点赞和礼物等。

TRTCChatSalon 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [语音沙龙（Android）](https://cloud.tencent.com/document/product/647/53537)。

- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时语音聊天组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 的 AVChatroom 实现聊天室的功能，同时，通过 IM 的属性接口来存储麦位表等房间信息，邀请信令可以用于上麦申请/抱麦申请。

[](id:TRTCChatSalon)

## TRTCChatSalon API 概览

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
| [getUserInfoList](#getuserinfolist) | 获取指定 userId 的用户信息，如果为 null，则获取房间内所有人的信息。 |

### 上下麦接口

| API                     | 描述                               |
| ----------------------- | ---------------------------------- |
| [enterSeat](#enterseat) | 主动上麦（听众端和房主均可调用）。 |
| [leaveSeat](#leaveseat) | 主动下麦（主播调用）。 |
| [pickSeat](#pickseat)   | 抱人上麦（房主调用）。             |
| [kickSeat](#kickseat)   | 踢人下麦（房主调用）。             |

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


### 远端用户音频操作接口

| API                                       | 描述                    |
| ----------------------------------------- | ----------------------- |
| [muteRemoteAudio](#muteremoteaudio)       | 静音/解除静音指定成员。 |
| [muteAllRemoteAudio](#muteallremoteaudio) | 静音/解除静音所有成员。 |

### 背景音乐音效相关接口

| API                                             | 描述                                                         |
| ----------------------------------------------- | ------------------------------------------------------------ |
| [getAudioEffectManager](#getaudioeffectmanager) | 获取背景音乐音效管理对象 [TXAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3646dad993287c3a1a38a5bc0e6e33aa)。 |

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

[](id:TRTCChatSalonDelegate)
## TRTCChatSalonDelegate API 概览

### 通用事件回调

| API                       | 描述       |
| ------------------------- | ---------- |
| [onError](#onerror)       | 错误回调。 |
| [onWarning](#onwarning)   | 警告回调。 |
| [onDebugLog](#ondebuglog) | Log 回调。 |

### 房间事件回调

| API                                       | 描述                       |
| ----------------------------------------- | -------------------------- |
| [onRoomDestroy](#onroomdestroy)           | 房间被销毁的回调。         |
| [onRoomInfoChange](#onroominfochange)     | 语音沙龙房间信息变更回调。 |
| [onUserVolumeUpdate](#onuservolumeupdate) | 用户通话音量回调。         |

### 麦位变更回调

| API                                            | 描述                                   |
| ---------------------------------------------- | -------------------------------------- |
| [onAnchorEnterSeat](#onanchorenterseat)        | 有成员上麦（主动上麦/房主抱人上麦）。  |
| [onAnchorLeaveSeat](#onanchorleaveseat)        | 有成员下麦（主动下麦/房主踢人下麦）。  |
| [onSeatMute](#onseatmute)                      | 房主禁麦。                             |

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

## 信令事件回调

| API                                               | 描述               |
| ------------------------------------------------- | ------------------ |
| [onReceiveNewInvitation](#onreceivenewinvitation) | 收到新的邀请请求。 |
| [onInviteeAccepted](#oninviteeaccepted)           | 被邀请人接受邀请。 |
| [onInviteeRejected](#oninviteerejected)           | 被邀请人拒绝邀请。 |
| [onInvitationCancelled](#oninvitationcancelled)   | 邀请人取消邀请。   |

## SDK 基础函数

### sharedInstance

获取 [TRTCChatSalon](https://cloud.tencent.com/document/product/647/53537) 单例对象。

```java
 public static synchronized TRTCChatSalon sharedInstance(Context context);
```

参数如下表所示：

| 参数    | 类型    | 含义                                                         |
| ------- | ------- | ------------------------------------------------------------ |
| context | Context | Android 上下文，内部会转为 ApplicationContext 用于系统 API 调用 |


### destroySharedInstance

销毁 [TRTCChatSalon](https://cloud.tencent.com/document/product/647/53537) 单例对象。

>?销毁实例后，外部缓存的 TRTCChatSalon 实例无法再使用，需要重新调用 [sharedInstance](#sharedinstance) 获取新实例。

```java
public static void destroySharedInstance();
```

### setDelegate
[TRTCChatSalon](https://cloud.tencent.com/document/product/647/53537) 事件回调，您可以通过 TRTCChatSalonDelegate 获得 [TRTCChatSalon](https://cloud.tencent.com/document/product/647/53537) 的各种状态通知。

```java
public abstract void setDelegate(TRTCChatSalonDelegate delegate);
```

>?setDelegate 是 TRTCChatSalon 的代理回调。   

### setDelegateHandler
设置事件回调所在的线程。

```java
public abstract void setDelegateHandler(Handler handler);
```

参数如下表所示：

| 参数    | 类型    | 含义                                                         |
| ------- | ------- | ------------------------------------------------------------ |
| handler | Handler | TRTCChatSalon 中的各种状态通知，会派发到您指定的 handler 线程。 |

   

### login

登录。

```java
public abstract void login(int sdkAppId,
 String userId, String userSig,
TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数     | 类型           | 含义                                                         |
| -------- | -------------- | ------------------------------------------------------------ |
| sdkAppId | int            | 您可以在实时音视频控制台 >【[应用管理](https://console.cloud.tencent.com/trtc/app)】> 应用信息中查看 SDKAppID。 |
| userId   | String         | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。 |
| userSig  | String         | 腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |
| callback | ActionCallback | 登录回调，成功时 code 为0。                                  |

   

### logout

登出。

```java
public abstract void logout(TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数     | 类型           | 含义                        |
| -------- | -------------- | --------------------------- |
| callback | ActionCallback | 登出回调，成功时 code 为0。 |

   

### setSelfProfile

修改个人信息。

```java
public abstract void setSelfProfile(String userName, String avatarURL, TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数      | 类型           | 含义                                |
| --------- | -------------- | ----------------------------------- |
| userName  | String         | 昵称。                              |
| avatarURL | String         | 头像地址。                          |
| callback  | ActionCallback | 个人信息设置回调，成功时 code 为0。 |

   


## 房间相关接口函数

### createRoom

创建房间（房主调用）。

```java
public abstract void createRoom(int roomId, TRTCChatSalonDef.RoomParam roomParam, TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数      | 类型           | 含义                                                         |
| --------- | -------------- | ------------------------------------------------------------ |
| roomId    | int            | 房间标识，需要由您分配并进行统一管理。多个 roomID 可以汇总成一个语音沙龙房间列表，腾讯云暂不提供语音沙龙房间列表的管理服务，请自行管理您的语音沙龙房间列表。 |
| roomParam | RoomParam      | 房间信息，用于房间描述的信息。例如房间名称、麦位信息、封面信息等。 |
| callback  | ActionCallback | 创建房间的结果回调，成功时 code 为0。                        |

房主开播的正常调用流程如下： 

1. 房主调用`createRoom`创建新的语音沙龙，此时传入房间 ID、上麦是否需要房主确认等房间属性信息。
2. 房主创建房间成功后，调用`enterSeat`进入座位。
3. 房主还会收到麦位表有成员进入的`onAnchorEnterSeat`的事件通知，此时会自动打开麦克风采集。

   

### destroyRoom

销毁房间（房主调用）。房主在创建房间后，可以调用这个函数来销毁房间。

```java
public abstract void destroyRoom(TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数     | 类型           | 含义                                  |
| -------- | -------------- | ------------------------------------- |
| callback | ActionCallback | 销毁房间的结果回调，成功时 code 为0。 |


### enterRoom

进入房间（听众调用）。

```java
public abstract void enterRoom(int roomId, TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数     | 类型           | 含义                                  |
| -------- | -------------- | ------------------------------------- |
| roomId   | int            | 房间标识。                            |
| callback | ActionCallback | 进入房间的结果回调，成功时 code 为0。 |


听众进房收听的正常调用流程如下： 

1. 听众向您的服务端获取最新的语音沙龙列表，可能包含多个语音沙龙房间的 roomId 和房间信息。
2. 听众选择一个语音沙龙，调用`enterRoom`并传入房间号即可进入该房间。
3. 进房后会收到组件的`onRoomInfoChange`房间属性变化事件通知，此时可以记录房间属性并做相应改变，例如 UI 展示房间名、记录上麦是否需要请求房主同意等。
4. 进房后还会收到麦位表有主播进入的`onAnchorEnterSeat`的事件通知。

### exitRoom

退出房间。

```java
public abstract void exitRoom(TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数     | 类型           | 含义                                  |
| -------- | -------------- | ------------------------------------- |
| callback | ActionCallback | 退出房间的结果回调，成功时 code 为0。 |

   

### getRoomInfoList

获取房间列表的详细信息，其中房间名称、房间封面是房主在创建 `createRoom()` 时通过 roomInfo 设置的。

>?如果房间列表和房间信息都由您自行管理，可忽略该函数。


```java
public abstract void getRoomInfoList(List<Integer> roomIdList, TRTCChatSalonCallback.RoomInfoCallback callback);
```

参数如下表所示：

| 参数       | 类型                | 含义               |
| ---------- | ------------------- | ------------------ |
| roomIdList | List&lt;Integer&gt; | 房间号列表。       |
| callback   | RoomInfoCallback    | 房间详细信息回调。 |


### getUserInfoList

获取指定userId的用户信息。

```java
public abstract void getUserInfoList(List<String> userIdList, TRTCChatSalonCallback.UserListCallback userlistcallback);
```

参数如下表所示：

| 参数             | 类型               | 含义                                                         |
| ---------------- | ------------------ | ------------------------------------------------------------ |
| userIdList       | List&lt;String&gt; | 需要获取的用户 ID 列表，如果为 null，则获取房间内所有人的信息。 |
| userlistcallback | UserListCallback   | 用户详细信息回调。                                           |


## 上下麦接口

### enterSeat

主动上麦（听众端和房主均可调用）。

>?上麦成功后，房间内所有成员会收到`onAnchorEnterSeat`的事件通知。

```java
public abstract void enterSeat(TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数     | 类型           | 含义       |
| -------- | -------------- | ---------- |
| callback | ActionCallback | 操作回调。 |

调用该接口会立即修改麦位表。如果是听众申请上麦需要房主同意的场景，可以先调用 `sendInvitation` 向房主申请，收到 `onInvitationAccept`后再调用该函数。

### leaveSeat

主动下麦（主播调用）。

>? 下麦成功后，房间内所有成员会收到`onAnchorLeaveSeat`的事件通知。

```java
public abstract void leaveSeat(TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数     | 类型           | 含义       |
| -------- | -------------- | ---------- |
| callback | ActionCallback | 操作回调。 |

### pickSeat

抱人上麦（房主调用）。

>? 房主抱人上麦，房间内所有成员会收到`onAnchorEnterSeat`的事件通知。

```java
public abstract void pickSeat(String userId, TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数     | 类型           | 含义       |
| -------- | -------------- | ---------- |
| userId   | String         | 用户 ID。  |
| callback | ActionCallback | 操作回调。 |

调用该接口会立即修改麦位表。如果是房主需要听众同意，听众才会上麦的场景，可以先调用 `sendInvitation` 向听众申请，收到 `onInvitationAccept`后再调用该函数。


### kickSeat

踢人下麦（房主调用）。

>? 房主踢人下麦，房间内所有成员会收到`onAnchorLeaveSeat`的事件通知。

```java
public abstract void kickSeat(String userId, TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数     | 类型           | 含义                 |
| -------- | -------------- | -------------------- |
| userId   | String         | 需要踢下麦的用户id。 |
| callback | ActionCallback | 操作回调。           |

调用该接口会立即修改麦位表。


## 本地音频操作接口

### startMicrophone

开启麦克风采集。

```java
public abstract void startMicrophone();
```

### stopMicrophone

停止麦克风采集。

```java
public abstract void stopMicrophone();
```

### setAudioQuality

设置音质。

```java
public abstract void setAudioQuality(int quality);
```

参数如下表所示：

| 参数    | 类型 | 含义                                                         |
| ------- | ---- | ------------------------------------------------------------ |
| quality | int  | 音频质量，详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a955cccaddccb0c993351c656067bee55)。 |


### muteLocalAudio

静音/取消静音本地的音频。

```java
public abstract void muteLocalAudio(boolean mute);
```

参数如下表所示：

| 参数 | 类型    | 含义                                                         |
| ---- | ------- | ------------------------------------------------------------ |
| mute | boolean | 静音/取消静音，详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a37f52481d24fa0f50842d3d8cc380d86)。 |



### setSpeaker

设置开启扬声器。

```java
public abstract void setSpeaker(boolean useSpeaker);
```

参数如下表所示：

| 参数       | 类型    | 含义                        |
| ---------- | ------- | --------------------------- |
| useSpeaker | boolean | true：扬声器；false：听筒。 |



### setAudioCaptureVolume

设置麦克风采集音量。

```java
public abstract void setAudioCaptureVolume(int volume);
```

参数如下表所示：

| 参数   | 类型 | 含义                          |
| ------ | ---- | ----------------------------- |
| volume | int  | 采集音量，0 - 100， 默认100。 |


### setAudioPlayoutVolume

设置播放音量。

```java
public abstract void setAudioPlayoutVolume(int volume);
```

参数如下表所示：

| 参数   | 类型 | 含义                          |
| ------ | ---- | ----------------------------- |
| volume | int  | 播放音量，0 - 100， 默认100。 |

### muteRemoteAudio

静音/解除静音指定成员。

```java
public abstract void muteRemoteAudio(String userId, boolean mute);
```

参数如下表所示：

| 参数   | 类型    | 含义                              |
| ------ | ------- | --------------------------------- |
| userId | String  | 指定的用户 ID。                   |
| mute   | boolean | true：开启静音；false：关闭静音。 |

### muteAllRemoteAudio

静音/解除静音所有成员。

```java
public abstract void muteAllRemoteAudio(boolean mute);
```

参数如下表所示：

| 参数 | 类型    | 含义                              |
| ---- | ------- | --------------------------------- |
| mute | boolean | true：开启静音；false：关闭静音。 |

   

## 背景音乐音效相关接口函数

### getAudioEffectManager

获取背景音乐音效管理对象 [TXAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3646dad993287c3a1a38a5bc0e6e33aa)。

```java
public abstract TXAudioEffectManager getAudioEffectManager();
```


## 消息发送相关接口函数

### sendRoomTextMsg

在房间中广播文本消息，一般用于弹幕聊天。

```java
public abstract void sendRoomTextMsg(String message, TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数     | 类型           | 含义           |
| -------- | -------------- | -------------- |
| message  | String         | 文本消息。     |
| callback | ActionCallback | 发送结果回调。 |

   

### sendRoomCustomMsg

发送自定义文本消息。

```java
public abstract void sendRoomCustomMsg(String cmd, String message, TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数     | 类型           | 含义                                               |
| -------- | -------------- | -------------------------------------------------- |
| cmd      | String         | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message  | String         | 文本消息。                                         |
| callback | ActionCallback | 发送结果回调。                                     |

   

## 邀请信令相关接口

### sendInvitation

向用户发送邀请。

```java
public abstract String sendInvitation(String cmd, String userId, String content, TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数     | 类型           | 含义             |
| -------- | -------------- | ---------------- |
| cmd      | String         | 业务自定义指令。 |
| userId   | String         | 邀请的用户 ID。  |
| content  | String         | 邀请的内容。     |
| callback | ActionCallback | 发送结果回调。   |

返回值：

| 返回值   | 类型   | 含义                  |
| -------- | ------ | --------------------- |
| inviteId | String | 用于标识此次邀请 ID。 |

### acceptInvitation

接受邀请。

```java
public abstract void acceptInvitation(String id, TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数     | 类型           | 含义           |
| -------- | -------------- | -------------- |
| id       | String         | 邀请 ID。      |
| callback | ActionCallback | 发送结果回调。 |

### rejectInvitation

拒绝邀请。

```java
public abstract void rejectInvitation(String id, TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数     | 类型           | 含义           |
| -------- | -------------- | -------------- |
| id       | String         | 邀请 ID。      |
| callback | ActionCallback | 发送结果回调。 |


### cancelInvitation

取消邀请。

```java
public abstract void cancelInvitation(String id, TRTCChatSalonCallback.ActionCallback callback);
```

参数如下表所示：

| 参数     | 类型           | 含义           |
| -------- | -------------- | -------------- |
| id       | String         | 邀请 ID。      |
| callback | ActionCallback | 发送结果回调。 |

[](id:TRTCChatSalonDelegate)
## TRTCChatSalonDelegate 事件回调

## 通用事件回调

### onError

错误回调。

>? SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```java
void onError(int code, String message);
```

参数如下表所示：

| 参数    | 类型   | 含义       |
| ------- | ------ | ---------- |
| code    | int    | 错误码。   |
| message | String | 错误信息。 |


### onWarning

警告回调。

```java
void onWarning(int code, String message);
```

参数如下表所示：

| 参数    | 类型   | 含义       |
| ------- | ------ | ---------- |
| code    | int    | 错误码。   |
| message | String | 警告信息。 |

   

### onDebugLog

Log 回调。

```java
void onDebugLog(String message);
```

参数如下表所示：

| 参数    | 类型   | 含义       |
| ------- | ------ | ---------- |
| message | String | 日志信息。 |

   


## 房间事件回调

### onRoomDestroy

房间被销毁的回调。房主解散房间时，房间内的所有用户都会收到此通知。

```java
void onRoomDestroy(String roomId);
```

参数如下表所示：

| 参数   | 类型   | 含义      |
| ------ | ------ | --------- |
| roomId | String | 房间 ID。 |


### onRoomInfoChange

进房成功后会回调该接口，roomInfo 中的信息在房主创建房间的时候传入。

```java
void onRoomInfoChange(TRTCChatSalonDef.RoomInfo roomInfo);
```

参数如下表所示：

| 参数     | 类型     | 含义       |
| -------- | -------- | ---------- |
| roomInfo | RoomInfo | 房间信息。 |

   

### onUserVolumeUpdate

启用音量大小提示，会通知每个成员的音量大小。

```java
void onUserVolumeUpdate(String userId, int volume);

```

参数如下表所示：

| 参数   | 类型   | 含义                      |
| ------ | ------ | ------------------------- |
| userId | String | 用户 ID。                 |
| volume | int    | 音量大小，取值：0 - 100。 |


## 麦位回调

### onAnchorEnterSeat

有成员上麦(主动上麦/房主抱人上麦)。

```java
void onAnchorEnterSeat(TRTCChatSalonDef.UserInfo user);
```

参数如下表所示：

| 参数 | 类型     | 含义                 |
| ---- | -------- | -------------------- |
| user | UserInfo | 上麦用户的详细信息。 |

### onAnchorLeaveSeat

有成员下麦(主动下麦/房主踢人下麦)。

```java
void onAnchorLeaveSeat(TRTCChatSalonDef.UserInfo user);
```

参数如下表所示：

| 参数 | 类型     | 含义                 |
| ---- | -------- | -------------------- |
| user | UserInfo | 上麦用户的详细信息。 |


### onSeatMute

房主禁麦。

```java
void onSeatMute(String userId, boolean isMute);
```

参数如下表所示：

| 参数   | 类型    | 含义                               |
| ------ | ------- | ---------------------------------- |
| userId  | String     | 麦位的用户 id。                       |
| isMute | boolean | true：静音麦位；false：解除静音。 |



## 听众进出事件回调

### onAudienceEnter

收到听众进房通知。

```java
void onAudienceEnter(TRTCChatSalonDef.UserInfo userInfo);
```

参数如下表所示：

| 参数     | 类型     | 含义           |
| -------- | -------- | -------------- |
| userInfo | UserInfo | 进房听众信息。 |

### onAudienceExit

收到听众退房通知。

```java
void onAudienceExit(TRTCChatSalonDef.UserInfo userInfo);
```

参数如下表所示：

| 参数     | 类型     | 含义           |
| -------- | -------- | -------------- |
| userInfo | UserInfo | 退房听众信息。 |

   

## 消息事件回调

### onRecvRoomTextMsg

收到文本消息。

```java
void onRecvRoomTextMsg(String message, TRTCChatSalonDef.UserInfo userInfo);
```

参数如下表所示：

| 参数     | 类型     | 含义             |
| -------- | -------- | ---------------- |
| message  | String   | 文本消息。       |
| userInfo | UserInfo | 发送者用户信息。 |

   

### onRecvRoomCustomMsg

收到自定义消息。

```java
void onRecvRoomCustomMsg(String cmd, String message, TRTCChatSalonDef.UserInfo userInfo);
```

参数如下表所示：

| 参数     | 类型     | 含义                                               |
| -------- | -------- | -------------------------------------------------- |
| cmd      | String   | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message  | String   | 文本消息。                                         |
| userInfo | UserInfo | 发送者用户信息。                                   |

## 邀请信令事件回调

### onReceiveNewInvitation

收到新的邀请请求。

```java
void onReceiveNewInvitation(String id, String inviter, String cmd, String content);
```

参数如下表所示：

| 参数    | 类型     | 含义                               |
| ------- | -------- | ---------------------------------- |
| id      | String   | 邀请 ID。                          |
| inviter | String   | 邀请人的用户 ID。                  |
| cmd     | String   | 业务指定的命令字，由开发者自定义。 |
| content | String   | 业务指定的内容。                   |

### onInviteeAccepted

被邀请者接受邀请。

```java
void onInviteeAccepted(String id, String invitee);
```

参数如下表所示：

| 参数    | 类型   | 含义                |
| ------- | ------ | ------------------- |
| id      | String | 邀请 ID。           |
| invitee | String | 被邀请人的用户 ID。 |

### onInviteeRejected

被邀请者拒绝邀请。

```java
void onInviteeRejected(String id, String invitee);
```

参数如下表所示：

| 参数    | 类型   | 含义                |
| ------- | ------ | ------------------- |
| id      | String | 邀请 ID。           |
| invitee | String | 被邀请人的用户 ID。 |

### onInvitationCancelled

邀请人取消邀请。

```java
void onInvitationCancelled(String id, String inviter);
```

参数如下表所示：

| 参数    | 类型   | 含义              |
| ------- | ------ | ----------------- |
| id      | String | 邀请 ID。         |
| inviter | String | 邀请人的用户 ID。 |

### onInvitationTimeout

邀请超时。

```java
void onInvitationTimeout(String id);
```

参数如下表所示：

| 参数    | 类型   | 含义              |
| ------- | ------ | ----------------- |
| id      | String | 邀请 ID。         |

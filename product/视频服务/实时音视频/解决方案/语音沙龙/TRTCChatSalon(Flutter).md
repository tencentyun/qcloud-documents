TRTCChatSalon 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的组件，支持以下功能：

- 房主创建新的语音沙龙开播，听众进入语音沙龙收听/互动。
- 房主可以同意听众上麦、将麦上主播踢下麦。
- 听众可以申请上麦，变成麦上主播，可以和其他人语音互动，也可以随时下麦成为普通的听众。
- 支持发送各种文本消息。

TRTCChatSalon 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [语音沙龙（Flutter）](https://cloud.tencent.com/document/product/647/53582)。

- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时语音聊天组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 的 AVChatroom 实现聊天室的功能，同时，通过 IM 的属性接口来存储麦位表等房间信息，邀请信令可以用于上麦申请/抱麦申请。

[](id:TRTCChatSalon)

## TRTCChatSalon API 概览

### SDK 基础函数

| API                                             | 描述           |
| ----------------------------------------------- | -------------- |
| [sharedInstance](#sharedinstance)               | 获取单例对象。 |
| [destroySharedInstance](#destroysharedinstance) | 销毁单例对象。 |
| [registerListener](#registerlistener)           | 设置事件监听。 |
| [unRegisterListener](#unregisterlistener)       | 销毁事件监听。 |
| [login](#login)                                 | 登录。         |
| [logout](#logout)                               | 登出。         |
| [setSelfProfile](#setselfprofile)               | 修改个人信息。 |

### 房间相关接口函数

| API                                     | 描述                                                         |
| --------------------------------------- | ------------------------------------------------------------ |
| [createRoom](#createroom)               | 创建房间（房主调用），若房间不存在，系统将自动创建一个新房间。 |
| [destroyRoom](#destroyroom)             | 销毁房间（房主调用）。                                       |
| [enterRoom](#enterroom)                 | 进入房间（听众调用）。                                       |
| [exitRoom](#exitroom)                   | 退出房间（听众调用）。                                       |
| [getRoomInfoList](#getroominfolist)     | 获取房间列表的详细信息。                                     |
| [getRoomMemberList](#getroommemberlist) | 获取房间内所有用户信息。                                     |
| [getArchorInfoList](#getarchorInfolist) | 获取房间主播列表。                                           |
| [getUserInfoList](#getuserinfolist)     | 获取指定 userId 的用户信息。                                 |

### 上下麦接口

| API                   | 描述                                |
| --------------------- | ----------------------------------- |
| [enterMic](#entermic) | 听众上麦。                          |
| [leaveMic](#leavemic) | 主播下麦。                          |
| [muteMic](#mutemic)   | 静音/解除静音某个麦位（房主调用）。 |
| [kickMic](#kickmic)   | 踢人下麦（房主调用）。              |

### 本地音频操作接口

| API                                             | 描述                 |
| ----------------------------------------------- | -------------------- |
| [startMicrophone](#startmicrophone)             | 开启麦克风采集。     |
| [stopMicrophone](#stopmicrophone)               | 停止麦克风采集。     |
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

| API                                 | 描述                                     |
| ----------------------------------- | ---------------------------------------- |
| [sendRoomTextMsg](#sendroomtextmsg) | 在房间中广播文本消息，一般用于弹幕聊天。 |

### 申请上麦信令相关接口

| API                             | 描述           |
| ------------------------------- | -------------- |
| [raiseHand](#raisehand)         | 听众申请上麦。 |
| [agreeToSpeak](#agreetospeak)   | 房主同意上麦。 |
| [refuseToSpeak](#refusetospeak) | 房主拒绝上麦。 |

[](id:TRTCChatSalonDelegate)
## TRTCChatSalonDelegate API 概览

### 通用事件回调

| API                                 | 描述       |
| ----------------------------------- | ---------- |
| [onError](#onerror)                 | 错误回调。 |
| [onWarning](#onwarning)             | 警告回调。 |
| [onKickedOffline](#onkickedoffline) | 被踢下线。 |

### 房间事件回调

| API                                       | 描述                     |
| ----------------------------------------- | ------------------------ |
| [onRoomDestroy](#onroomdestroy)           | 房间被销毁的回调。       |
| [onAnchorListChange](#onanchorlistchange) | 主播列表发生变化的回调。 |
| [onUserVolumeUpdate](#onuservolumeupdate) | 用户通话音量回调。       |

### 麦位变更回调

| API                                   | 描述                                  |
| ------------------------------------- | ------------------------------------- |
| [onAnchorEnterMic](#onanchorentermic) | 有成员上麦（主动上麦/房主抱人上麦）。 |
| [onAnchorLeaveMic](#onanchorleavemic) | 有成员下麦（主动下麦/房主踢人下麦）。 |
| [onMicMute](#onmicmute)               | 主播禁麦。                            |

### 听众进出事件回调

| API                                 | 描述               |
| ----------------------------------- | ------------------ |
| [onAudienceEnter](#onaudienceenter) | 收到听众进房通知。 |
| [onAudienceExit](#onaudienceexit)   | 收到听众退房通知。 |

### 消息事件回调

| API                                     | 描述           |
| --------------------------------------- | -------------- |
| [onRecvRoomTextMsg](#onrecvroomtextmsg) | 收到文本消息。 |

## 申请上麦信令事件回调

| API                                    | 描述                                     |
| -------------------------------------- | ---------------------------------------- |
| [onRaiseHand](#onraisehand) | 有听众举手，申请上麦。                   |
| [onAgreeToSpeak](#onagreetospeak)   | 听众申请举手后，收到房主同意举手的回调。 |
| [onRefuseToSpeak](#onrefusetospeak)    | 听众申请举手后，房主拒绝举手的回调。     |

## SDK 基础函数

### sharedInstance

获取 TRTCChatSalon 单例对象。

```dart
 static Future<TRTCChatSalon> sharedInstance()
```


### destroySharedInstance

销毁 TRTCChatSalon 单例对象。

>?销毁实例后，外部缓存的 TRTCChatSalon 实例无法再使用，需要重新调用 [sharedInstance](#sharedinstance) 获取新实例。

```dart
static void destroySharedInstance()
```

### registerListener

设置事件监听

```
void registerListener(VoiceListenerFunc func)
```

>?setDelegate 是 TRTCChatSalon 的代理回调。   

### unRegisterListener

移除组件事件监听接口。

```dart
void unRegisterListener(VoiceListenerFunc func)
```

参数如下表所示：

| 参数 | 类型              | 含义                                                      |
| ---- | ----------------- | --------------------------------------------------------- |
| func | VoiceListenerFunc | TRTCChatSalon 中的各种状态通知，会派发到您指定的 func函数 |


### login

登录。

```dart
Future<ActionCallback> login(int sdkAppId, String userId, String userSig)
```

参数如下表所示：

| 参数     | 类型   | 含义                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| sdkAppId | int    | 您可以在实时音视频控制台 >【[应用管理](https://console.cloud.tencent.com/trtc/app)】> 应用信息中查看 SDKAppID。 |
| userId   | String | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。 |
| userSig  | String | 腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |


### logout

登出。

```dart
Future<ActionCallback> logout()
```

### setSelfProfile

修改个人信息。

```dart
Future<ActionCallback> setSelfProfile(String userName, String avatarURL)
```

参数如下表所示：

| 参数      | 类型   | 含义       |
| --------- | ------ | ---------- |
| userName  | String | 昵称。     |
| avatarURL | String | 头像地址。 |

## 房间相关接口函数

### createRoom

创建房间（新建房间时调用）。

```
Future<ActionCallback> createRoom(int roomId, RoomParam roomParam)
```

参数如下表所示：

| 参数      | 类型      | 含义                                                         |
| --------- | --------- | ------------------------------------------------------------ |
| roomId    | int       | 房间标识，需要由您分配并进行统一管理。多个 roomID 可以汇总成一个语音沙龙房间列表，腾讯云暂不提供语音沙龙房间列表的管理服务，请自行管理您的语音沙龙房间列表。 |
| roomParam | RoomParam | 房间信息，用于房间描述的信息。例如房间名称、封面信息等。     |

房主开播的正常调用流程如下： 

1. 房主调用 `createRoom` 创建新的语音沙龙，此时传入房间 ID等房间属性信息。
2. 房主还会收到麦位表有成员进入的 `onAnchorEnterMic` 的事件通知，此时会自动打开麦克风采集。

### destroyRoom

销毁房间（房主调用）。房主在创建房间后，可以调用这个函数来销毁房间。

```dart
Future<ActionCallback> destroyRoom()
```


### enterRoom

进入房间（听众调用）。

```dart
Future<ActionCallback> enterRoom(int roomId)
```

参数如下表所示：

| 参数   | 类型 | 含义       |
| ------ | ---- | ---------- |
| roomId | int  | 房间标识。 |


听众进房收听的正常调用流程如下： 

1. 听众向您的服务端获取最新的语音沙龙列表，可能包含多个语音沙龙房间的 roomId 和房间信息。
2. 听众选择一个语音沙龙，调用 `enterRoom` 并传入房间号即可进入该房间。
3. 进房后会可查询 `getArchorInfoList` 获取主播列表，并根据 `getRoomMemberList` 获取房间所有用户列表，减去主播列表可以得到听众列表。
4. 进房后还会收到麦位表有主播进入的 `onAnchorEnterMic` 的事件通知。

### exitRoom

退出房间。

```dart
Future<ActionCallback> exitRoom()
```

### getRoomInfoList

获取房间列表的详细信息，其中房间名称、房间封面是房主在创建 `createRoom()` 时通过 roomInfo 设置的。

>?如果房间列表和房间信息都由您自行管理，可忽略该函数。


```dart
Future<RoomInfoCallback> getRoomInfoList(List<String> roomIdList)
```

参数如下表所示：

| 参数       | 类型                | 含义         |
| ---------- | ------------------- | ------------ |
| roomIdList | List&lt;String&gt; | 房间号列表。 |


### getRoomMemberList

获取房间内所有成员列表。

>?IM 直播聊天群默认只能拉取最近31个成员列表。


```dart
Future<MemberListCallback> getRoomMemberList(double nextSeq)
```

参数如下表所示：

| 参数    | 类型   | 含义                                                         |
| ------- | ------ | ------------------------------------------------------------ |
| nextSeq | double | 分页拉取标志，第一次拉取填0，回调成功如果 nextSeq 不为零，需要分页，传入再次拉取，直至为0。 |

### getArchorInfoList

获取房间内主播列表。

```dart
Future<UserListCallback> getArchorInfoList()
```


### getUserInfoList

获取指定 userId 的用户信息。

```dart
Future<UserListCallback> getUserInfoList(List<String> userIdList)
```

参数如下表所示：

| 参数       | 类型               | 含义                                                         |
| ---------- | ------------------ | ------------------------------------------------------------ |
| userIdList | List&lt;String&gt; | 需要获取的用户 ID 列表，如果为 null，则获取房间内所有人的信息。 |


## 上下麦接口

### enterMic

上麦（听众端和房主均可调用）。

>?上麦成功后，房间内所有成员会收到 `onAnchorEnterSeat` 的事件通知。

```
Future<ActionCallback> enterMic();
```

调用该接口会立即修改麦位表。听众需先调用 `raiseHand` 向房主申请，收到 `onAgreeToSpeak`后再调用该函数。

### leaveMic

主播下麦。

>? 下麦成功后，房间内所有成员会收到 `onAnchorLeaveMic` 的事件通知。

```dart
Future<ActionCallback> leaveMic()
```

### muteMic

静音/解除静音某个麦位（房主调用）。

>? 改变麦位的状态后，房间内所有成员会收到 `onAnchorListChange` 和 `onMicMute` 的事件通。

```dart
Future<ActionCallback> muteMic(bool mute)
```

### kickMic

踢人下麦（房主调用）。

>? 房主踢人下麦，房间内所有成员会收到 `onAnchorLeaveMic` 的事件通知。

```dart
Future<ActionCallback> kickMic(String userId)
```

参数如下表所示：

| 参数   | 类型   | 含义                 |
| ------ | ------ | -------------------- |
| userId | String | 需要踢下麦的用户 ID。 |

调用该接口会立即修改麦位表。


## 本地音频操作接口

### startMicrophone

开启麦克风采集。

```dart
void startMicrophone(int quality)
```

参数如下表所示：

| 参数    | 类型 | 含义                                                         |
| ------- | ---- | ------------------------------------------------------------ |
| quality | int  | 音频质量，详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a955cccaddccb0c993351c656067bee55)。 |

### stopMicrophone

停止麦克风采集。

```dart
void stopMicrophone()
```

### muteLocalAudio

静音/取消静音本地的音频。

```dart
void muteLocalAudio(bool mute)
```

参数如下表所示：

| 参数 | 类型    | 含义                                                         |
| ---- | ------- | ------------------------------------------------------------ |
| mute | bool | 静音/取消静音，详情请参见 [TRTC SDK](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a37f52481d24fa0f50842d3d8cc380d86)。 |


### setSpeaker

设置开启扬声器。

```dart
void setSpeaker(bool useSpeaker)
```

参数如下表所示：

| 参数       | 类型    | 含义                        |
| ---------- | ------- | --------------------------- |
| useSpeaker | bool | true：扬声器；false：听筒。 |



### setAudioCaptureVolume

设置麦克风采集音量。

```dart
void setAudioCaptureVolume(int volume)
```

参数如下表所示：

| 参数   | 类型 | 含义                          |
| ------ | ---- | ----------------------------- |
| volume | int  | 采集音量，0 - 100， 默认100。 |


### setAudioPlayoutVolume

设置播放音量。

```dart
void setAudioPlayoutVolume(int volume)
```

参数如下表所示：

| 参数   | 类型 | 含义                          |
| ------ | ---- | ----------------------------- |
| volume | int  | 播放音量，0 - 100， 默认100。 |

### muteRemoteAudio

静音/解除静音指定成员。

```dart
void muteRemoteAudio(String userId, bool mute)
```

参数如下表所示：

| 参数   | 类型    | 含义                              |
| ------ | ------- | --------------------------------- |
| userId | String  | 指定的用户 ID。                   |
| mute   | bool | true：开启静音；false：关闭静音。 |

### muteAllRemoteAudio

静音/解除静音所有成员。

```dart
void muteAllRemoteAudio(bool mute)
```

参数如下表所示：

| 参数 | 类型    | 含义                              |
| ---- | ------- | --------------------------------- |
| mute | bool | true：开启静音；false：关闭静音。 |


## 背景音乐音效相关接口函数

### getAudioEffectManager

获取背景音乐音效管理对象 [TXAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3646dad993287c3a1a38a5bc0e6e33aa)。

```dart
TXAudioEffectManager getAudioEffectManager()
```


## 消息发送相关接口函数

### sendRoomTextMsg

在房间中广播文本消息，一般用于弹幕聊天。

```dart
Future<ActionCallback> sendRoomTextMsg(String message)
```

参数如下表所示：

| 参数    | 类型   | 含义       |
| ------- | ------ | ---------- |
| message | String | 文本消息。 |

   

## 申请上麦信令相关接口

### raiseHand

听众申请上麦。

```dart
void raiseHand()
```

### agreeToSpeak

房主同意上麦。

```dart
Future<ActionCallback> agreeToSpeak(String userId)
```

参数如下表所示：

| 参数   | 类型   | 含义     |
| ------ | ------ | -------- |
| userId | String | 用户 ID。 |

### refuseToSpeak

房主拒绝用户上麦。

```dart
Future<ActionCallback> refuseToSpeak(String userId)
```

参数如下表所示：

| 参数   | 类型   | 含义     |
| ------ | ------ | -------- |
| userId | String | 用户 ID。 |

[](id:TRTCChatSalonDelegate)
## TRTCChatSalonDelegate 事件回调

## 通用事件回调

### onError

错误回调。

>? SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。


参数如下表所示：

| 参数      | 类型   | 含义                                                     |
| --------- | ------ | -------------------------------------------------------- |
| errCode   | int    | 错误码。                                                 |
| errMsg    | String | 错误信息。                                               |
| extraInfo | String | 扩展信息字段，个别错误码可能会带额外的信息帮助定位问题。 |

### onWarning

警告回调。

参数如下表所示：

| 参数        | 类型   | 含义                                                     |
| ----------- | ------ | -------------------------------------------------------- |
| warningCode | int    | 错误码。                                                 |
| warningMsg  | String | 警告信息。                                               |
| extraInfo   | String | 扩展信息字段，个别错误码可能会带额外的信息帮助定位问题。 |


### onKickedOffline

其他用户登录了同一账号，被踢下线。


## 房间事件回调

### onRoomDestroy

房间被销毁的回调。房主解散房间时，房间内的所有用户都会收到此通知。

### onAnchorListChange

主播列表发生变化的通知。

参数如下表所示：

| 参数   | 类型   | 含义       |
| ------ | ------ | ---------- |
| userId | String | 用户 ID。  |
| mute   | bool   | 静音状态。 |


### onUserVolumeUpdate

启用音量大小提示，会通知每个成员的音量大小。


参数如下表所示：

| 参数   | 类型   | 含义                      |
| ------ | ------ | ------------------------- |
| userId | String | 用户 ID。                 |
| volume | int    | 音量大小，取值：0 - 100。 |


## 麦位回调


### onAnchorEnterMic

有成员上麦。

参数如下表所示：

| 参数       | 类型   | 含义                 |
| ---------- | ------ | -------------------- |
| userId     | String | 进房的用户 ID。       |
| userName   | String | 用户昵称。           |
| userAvatar | String | 头像地址。           |
| mute       | bool   | 麦位状态，默认开麦。 |

### onAnchorLeaveMic

有成员下麦。

参数如下表所示：

| 参数   | 类型   | 含义           |
| ------ | ------ | -------------- |
| userId | String | 退房的用户 ID。 |

### onMicMute

房主是否禁麦。

参数如下表所示：

| 参数   | 类型   | 含义           |
| ------ | ------ | -------------- |
| userId | String | 下麦的用户 ID。 |
| mute   | bool   | 麦位状态。     |


## 听众进出事件回调

### onAudienceEnter

收到听众进房通知。


参数如下表所示：

| 参数       | 类型   | 含义           |
| ---------- | ------ | -------------- |
| userId     | String | 上麦的用户 ID。 |
| userName   | String | 用户昵称。     |
| userAvatar | String | 头像地址。     |

### onAudienceExit

收到听众退房通知。

参数如下表所示：

| 参数   | 类型   | 含义           |
| ------ | ------ | -------------- |
| userId | String | 下麦的用户 ID。 |


## 消息事件回调

### onRecvRoomTextMsg

收到文本消息。

参数如下表所示：

| 参数       | 类型   | 含义             |
| ---------- | ------ | ---------------- |
| message    | String | 文本消息。       |
| sendId     | String | 发送者用户 ID。   |
| userAvatar | String | 发送者用户头像。 |
| userName   | String | 发送者用户昵称。 |


## 申请举手信令事件回调

### onRaiseHand

收到新的上麦请求。


参数如下表所示：

| 参数   | 类型   | 含义               |
| ------ | ------ | ------------------ |
| userId | String | 申请举手的用户 ID。 |


### onAgreeToSpeak

房主同意上麦的回调。


参数如下表所示：

| 参数   | 类型   | 含义           |
| ------ | ------ | -------------- |
| userId | String | 房主的用户 ID。 |

### onRefuseToSpeak

房主拒绝上麦的回调。


参数如下表所示：

| 参数   | 类型   | 含义           |
| ------ | ------ | -------------- |
| userId | String | 房主的用户 ID。 |

TRTCLiveRoom 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持以下功能：

- 主播创建新的直播间开播，观众进入直播间观看。
- 主播和观众进行视频连麦互动。
- 两个不同房间的主播 PK 互动。
- 支持发送各种文本消息和自定义消息，自定义消息可用于实现弹幕、点赞和礼物。

TRTCLiveRoom 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [视频连麦直播（Flutter）](https://cloud.tencent.com/document/product/647/57388)。

- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647/32689) 作为低延时直播组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269/36887) 的 AVChatroom 实现直播聊天室的功能，同时，通过 IM 消息串联主播间的连麦流程。

[](id:TRTCLiveRoom)

## TRTCLiveRoom API 概览

### SDK 基础函数

| API                                             | 描述                     |
| ----------------------------------------------- | ------------------------ |
| [sharedInstance](#sharedinstance)               | 获取单例对象。           |
| [destroySharedInstance](#destroysharedinstance) | 销毁单例对象。           |
| [registerListener](#registerlistener)           | 设置事件回调。           |
| [unRegisterListener](#unregisterlistener)       | 设置事件回调所在的线程。 |
| [login](#login)                                 | 登录。                   |
| [logout](#logout)                               | 登出。                   |
| [setSelfProfile](#setselfprofile)               | 修改个人信息。           |

### 房间相关接口函数

| API                                     | 描述                                                         |
| --------------------------------------- | ------------------------------------------------------------ |
| [createRoom](#createroom)               | 创建房间（主播调用），若房间不存在，系统将自动创建一个新房间。 |
| [destroyRoom](#destroyroom)             | 销毁房间（主播调用）。                                       |
| [enterRoom](#enterroom)                 | 进入房间（观众调用）。                                       |
| [exitRoom](#exitroom)                   | 离开房间（观众调用）。                                       |
| [getRoomInfos](#getroominfos)           | 获取房间列表的详细信息。                                     |
| [getAnchorList](#getanchorlist)         | 获取房间内所有的主播列表，enterRoom() 成功后调用才有效。     |
| [getRoomMemberList](#getroommemberlist) | 获取房间内所有的成员信息，enterRoom() 成功后调用才有效。     |

### 推拉流相关接口函数

| API                                       | 描述                                               |
| ----------------------------------------- | -------------------------------------------------- |
| [startCameraPreview](#startcamerapreview) | 开启本地视频的预览画面。                           |
| [stopCameraPreview](#stopcamerapreview)   | 停止本地视频采集及预览。                           |
| [startPublish](#startpublish)             | 开始直播（推流）。                                 |
| [stopPublish](#stoppublish)               | 停止直播（推流）。                                 |
| [startPlay](#startplay)                   | 播放远端视频画面，可以在普通观看和连麦场景中调用。 |
| [stopPlay](#stopplay)                     | 停止渲染远端视频画面。                             |

### 主播和观众连麦

| API                                       | 描述               |
| ----------------------------------------- | ------------------ |
| [requestJoinAnchor](#requestjoinanchor)   | 观众请求连麦。     |
| [responseJoinAnchor](#responsejoinanchor) | 主播处理连麦请求。 |
| [kickoutJoinAnchor](#kickoutjoinanchor)   | 主播踢除连麦观众。 |

### 主播跨房间 PK

| API                               | 描述                   |
| --------------------------------- | ---------------------- |
| [requestRoomPK](#requestroompk)   | 主播请求跨房 PK。      |
| [responseRoomPK](#responseroompk) | 主播响应跨房 PK 请求。 |
| [quitRoomPK](#quitroompk)         | 退出跨房 PK。          |

### 音视频控制相关接口函数

| API                                       | 描述               |
| ----------------------------------------- | ------------------ |
| [switchCamera](#switchcamera)             | 切换前后摄像头。   |
| [setMirror](#setmirror)                   | 设置是否镜像展示。 |
| [muteLocalAudio](#mutelocalaudio)         | 静音本地音频。     |
| [muteRemoteAudio](#muteremoteaudio)       | 静音远端音频。     |
| [muteAllRemoteAudio](#muteallremoteaudio) | 静音所有远端音频。 |

### 背景音乐音效相关接口函数

| API                                             | 描述                                                         |
| ----------------------------------------------- | ------------------------------------------------------------ |
| [getAudioEffectManager](#getaudioeffectmanager) | 获取背景音乐音效管理对象 [TXAudioEffectManager](https://pub.dev/documentation/tencent_trtc_cloud/latest/tx_audio_effect_manager/TXAudioEffectManager-class.html)。 |

### 美颜滤镜相关接口函数

| API                                   | 描述                                                         |
| ------------------------------------- | ------------------------------------------------------------ |
| [getBeautyManager](#getbeautymanager) | 获取美颜管理对象 [TXBeautyManager](https://pub.dev/documentation/tencent_trtc_cloud/latest/tx_beauty_manager/TXBeautyManager-class.html)。 |

### 消息发送相关接口函数

| API                                     | 描述                                     |
| --------------------------------------- | ---------------------------------------- |
| [sendRoomTextMsg](#sendroomtextmsg)     | 在房间中广播文本消息，一般用于弹幕聊天。 |
| [sendRoomCustomMsg](#sendroomcustommsg) | 发送自定义文本消息。                     |

<h2 id="TRTCLiveRoomDelegate">TRTCLiveRoomDelegate API 概览</h2>

### 通用事件回调

| API                                 | 描述                               |
| ----------------------------------- | ---------------------------------- |
| [onError](#onerror)                 | 错误回调。                         |
| [onWarning](#onwarning)             | 警告回调。                         |
| [onKickedOffline](#onkickedoffline) | 其他用户登录了同一账号，被踢下线。 |

### 房间事件回调

| API                                           | 描述                                                 |
| --------------------------------------------- | ---------------------------------------------------- |
| [onEnterRoom](#onenterroom)                   | 本地进房回调。                                       |
| [onUserVideoAvailable](#onuservideoavailable) | 远端用户是否存在可播放的主路画面（一般用于摄像头）。 |
| [onRoomDestroy](#onroomdestroy)               | 房间被销毁的回调。                                   |

### 主播和观众进出事件回调

| API                                 | 描述                 |
| ----------------------------------- | -------------------- |
| [onAnchorEnter](#onanchorenter)     | 收到新主播进房通知。 |
| [onAnchorExit](#onanchorexit)       | 收到主播退房通知。   |
| [onAudienceEnter](#onaudienceenter) | 收到观众进房通知。   |
| [onAudienceExit](#onaudienceexit)   | 收到观众退房通知。   |

### 主播和观众连麦事件回调

| API                                         | 描述                           |
| ------------------------------------------- | ------------------------------ |
| [onRequestJoinAnchor](#onrequestjoinanchor) | 主播收到观众连麦请求时的回调。 |
| [onAnchorAccepted](#onanchoraccepted)       | 主播同意观众的连麦请求。       |
| [onAnchorRejected](#onanchorrejected)       | 主播拒绝观众的连麦请求。       |
| [onKickoutJoinAnchor](#onkickoutjoinanchor) | 连麦观众收到被踢出连麦的通知。 |

### 主播 PK 事件回调

| API                                   | 描述                   |
| ------------------------------------- | ---------------------- |
| [onRequestRoomPK](#onrequestroompk)   | 收到请求跨房 PK 通知。 |
| [onRoomPKAccepted](#onroompkaccepted) | 主播接受跨房 PK 请求。 |
| [onRoomPKRejected](#onroompkrejected) | 主播拒绝跨房 PK 请求。 |
| [onQuitRoomPK](#onquitroompk)         | 收到断开跨房 PK 通知。 |

### 消息事件回调

| API                                         | 描述             |
| ------------------------------------------- | ---------------- |
| [onRecvRoomTextMsg](#onrecvroomtextmsg)     | 收到文本消息。   |
| [onRecvRoomCustomMsg](#onrecvroomcustommsg) | 收到自定义消息。 |

## SDK 基础函数

### sharedInstance

获取 [TRTCLiveRoom](https://cloud.tencent.com/document/product/647/57388) 单例对象。

```java
 static Future<TRTCLiveRoom> sharedInstance()
```

### destroySharedInstance

销毁 [TRTCLiveRoom](https://cloud.tencent.com/document/product/647/57388) 单例对象。

>?销毁实例后，外部缓存的 TRTCLiveRoom 实例无法再使用，需要重新调用 [sharedInstance](#sharedinstance) 获取新实例。

```java
static void destroySharedInstance()
```

### registerListener

[TRTCLiveRoom](https://cloud.tencent.com/document/product/647/57388) 事件回调，您可以通过 TRTCLiveRoomDelegate 获得 [TRTCLiveRoom](https://cloud.tencent.com/document/product/647/57388) 的各种状态通知。

```java
void registerListener(VoiceListenerFunc func);
```

>?registerListener 是 TRTCLiveRoom 的代理回调。   


### unRegisterListener

移除组件事件监听接口。

```java
void unRegisterListener(VoiceListenerFunc func);
```


### login

登录。

```java
Future<ActionCallback> login(
      int sdkAppId, String userId, String userSig, TRTCLiveRoomConfig config);
```

参数如下表所示：

| 参数     | 类型               | 含义                                                         |
| -------- | ------------------ | ------------------------------------------------------------ |
| sdkAppId | int                | 您可以在实时音视频控制台 >【[应用管理](https://console.cloud.tencent.com/trtc/app)】> 应用信息中查看 SDKAppID。 |
| userId   | String             | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。 |
| userSig  | String             | 腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |
| config   | TRTCLiveRoomConfig | 全局配置信息，请在登录时初始化，登录之后不可变更。<ul style="margin:0;"><li>useCDNFirst 属性：用于设置观众观看方式。true 表示普通观众通过 CDN 观看，计费便宜但延时较高。false 表示普通观众通过低延时观看，计费价格介于 CDN 和连麦之间，但延迟可控制在1s以内。</li><li>CDNPlayDomain 属性：在 useCDNFirst 设置为 true 时才会生效，用于指定 CDN 观看的播放域名，您可以登录直播控制台 >【<a href="https://console.cloud.tencent.com/live/domainmanage">域名管理</a>】页面中进行设置。</li></ul> |

### logout

登出。

```java
Future<ActionCallback> logout();
```

### setSelfProfile

修改个人信息。

```java
Future<ActionCallback> setSelfProfile(String userName, String avatarURL);
```

参数如下表所示：

| 参数      | 类型   | 含义       |
| --------- | ------ | ---------- |
| userName  | String | 昵称。     |
| avatarURL | String | 头像地址。 |

## 房间相关接口函数

### createRoom

创建房间（主播调用）。

```java
Future<ActionCallback> createRoom(int roomId, TRTCCreateRoomParam roomParam);
```

参数如下表所示：

| 参数      | 类型      | 含义                                                         |
| --------- | --------- | ------------------------------------------------------------ |
| roomId    | int       | 房间标识，需要由您分配并进行统一管理。多个 roomID 可以汇总成一个直播间列表，腾讯云暂不提供直播间列表的管理服务，请自行管理您的直播间列表。 |
| roomParam | RoomParam | 房间信息，用于房间描述的信息，例如房间名称，封面信息等。如果房间列表和房间信息都由您的服务器自行管理，可忽略该参数。 |

主播开播的正常调用流程如下： 

1. 【主播】调用 `startCameraPreview()` 打开摄像头预览，此时可以调整美颜参数。 
2. 【主播】调用 `createRoom()` 创建直播间，房间创建成功与否会通过 ActionCallback 通知给主播。
3. 【主播】调用 `starPublish()` 开始推流。

### destroyRoom

销毁房间（主播调用）。主播在创建房间后，可以调用该函数来销毁房间。

```java
Future<ActionCallback> destroyRoom();
```


### enterRoom

进入房间（观众调用）。

```java
Future<ActionCallback> enterRoom(int roomId);
```

参数如下表所示：

| 参数   | 类型 | 含义       |
| ------ | ---- | ---------- |
| roomId | int  | 房间标识。 |

观众观看直播的正常调用流程如下： 

1. 【观众】向您的服务端获取最新的直播间列表，可能包含多个直播间的 roomID 和房间信息。
2. 【观众】观众选择一个直播间，并调用 `enterRoom()` 进入该房间。
3. 【观众】调用 `startPlay(userId)` 并传入主播的 userId 开始播放。
 - 若直播间列表已包含主播端的 userId 信息，观众端可直接调用 `startPlay(userId)` 即可开始播放。
 - 若在进房前暂未获取主播的 userId，观众端在进房后会收到 `TRTCLiveRoomDelegate` 中的 `onAnchorEnter(userId)` 的事件回调，该回调中携带主播的 userId 信息，再调用 `startPlay(userId)` 即可播放。 

### exitRoom

离开房间。

```java
Future<ActionCallback> exitRoom();
```


### getRoomInfos

获取房间列表的详细信息，房间信息是主播在创建 `createRoom()` 时通过 roomInfo 设置的。

>?如果房间列表和房间信息都由您自行管理，可忽略该函数。


```java
Future<RoomInfoCallback> getRoomInfos(List<String> roomIdList);
```

参数如下表所示：

| 参数       | 类型               | 含义         |
| ---------- | ------------------ | ------------ |
| roomIdList | List&lt;String&gt; | 房间号列表。 |

### getAnchorList

获取房间内所有的主播列表，`enterRoom()` 成功后调用才有效。

```java
Future<UserListCallback> getAnchorList();
```

### getRoomMemberList

获取房间内所有的观众信息，`enterRoom()` 成功后调用才有效。

```java
Future<UserListCallback> getRoomMemberList(int nextSeq)
```

参数如下表所示：

| 参数    | 类型 | 含义                                                         |
| ------- | ---- | ------------------------------------------------------------ |
| nextSeq | int  | 分页拉取标志，第一次拉取填0，回调成功如果 nextSeq 不为零，需要分页，传入再次拉取，直至为0。 |

   

## 推拉流相关接口函数

### startCameraPreview

开启本地视频的预览画面。

```java
Future<void> startCameraPreview(bool isFrontCamera, int viewId);
```

参数如下表所示：

| 参数          | 类型 | 含义                                  |
| ------------- | ---- | ------------------------------------- |
| isFrontCamera | bool | true：前置摄像头；false：后置摄像头。 |
| viewId        | int  | 视频 view 的回调 ID。                 |

### stopCameraPreview

停止本地视频采集及预览。

```java
  Future<void> stopCameraPreview();
```

   

### startPublish

开始直播（推流），适用于以下场景：
- 主播开播的时候调用。
- 观众开始连麦时调用。

```java
Future<void> startPublish(String streamId);
```

参数如下表所示：

| 参数     | 类型    | 含义                                                         |
| -------- | ------- | ------------------------------------------------------------ |
| streamId | String? | 用于绑定直播 CDN 的 streamId，如果您希望观众通过直播 CDN 进行观看，需要指定当前主播的直播 streamId。 |


### stopPublish

停止直播（推流），适用于以下场景：
- 主播结束直播时调用。
- 观众结束连麦时调用。


```java
Future<void> stopPublish();
```

### startPlay

播放远端视频画面，可以在普通观看和连麦场景中调用。

```java
Future<void> startPlay(String userId, int viewId);
```

参数如下表所示：

| 参数   | 类型   | 含义               |
| ------ | ------ | ------------------ |
| userId | String | 需要观看的用户id。 |
| viewId | int    | 视频view的回调id。 |

- **普通观看场景：**
    - 若直播间列表已包含主播端的 userId 信息，观众端可以直接在 `enterRoom()` 成功后调用 `startPlay(userId)` 播放主播的画面。
    - 若在进房前暂未获取主播的 userId，观众端在进房后会收到 `TRTCLiveRoomDelegate` 中的 `onAnchorEnter(userId)` 的事件回调，该回调中携带主播的 userId 信息，再调用 `startPlay(userId)` 即可播放主播的画面。

- **直播连麦场景：**
发起连麦后，主播会收到来自 `TRTCLiveRoomDelegate` 中的 `onAnchorEnter(userId)` 回调，此时使用回调中的 userId 调用 `startPlay(userId)` 即可播放连麦画面。

### stopPlay

停止渲染远端视频画面。需在 `onAnchorExit()` 回调时，调用该接口。

```java
Future<void> stopPlay(String userId);
```

参数如下表所示：

| 参数   | 类型   | 含义             |
| ------ | ------ | ---------------- |
| userId | String | 对方的用户信息。 |

## 主播和观众连麦

### requestJoinAnchor

观众请求连麦。

```java
Future<ActionCallback> requestJoinAnchor();
```

主播和观众的连麦流程如下：

1. 【观众】调用 `requestJoinAnchor()` 向主播发起连麦请求。
2. 【主播】会收到 `TRTCLiveRoomDelegate` 的 `onRequestJoinAnchor()` 回调通知。
3. 【主播】调用 `responseJoinAnchor()` 决定是否接受来自观众的连麦请求。
4. 【观众】会收到 responseCallback 回调通知，该通知会携带主播的处理结果。
5. 【观众】如果请求被同意，则调用 `startCameraPreview()` 开启本地摄像头。
6. 【观众】然后调用 `startPublish()` 正式进入推流状态。
7. 【主播】一旦观众进入连麦状态，主播会收到 `TRTCLiveRoomDelegate` 的 `onAnchorEnter()` 通知。
8. 【主播】主播调用 `startPlay()` 即可看到连麦观众的视频画面。
9. 【观众】如果直播间里已有其他观众正在跟主播连麦，新加入的连麦观众会收到 `onAnchorEnter()` 通知，调用 `startPlay()` 播放其他连麦者的视频画面。

   

### responseJoinAnchor

主播处理连麦请求。主播在收到 `TRTCLiveRoomDelegate` 的 `onRequestJoinAnchor()` 回调后需要调用此接口来处理观众的连麦请求。

```java
Future<ActionCallback> responseJoinAnchor(String userId, boolean agreee);
```

参数如下表所示：

| 参数   | 类型   | 含义                      |
| ------ | ------ | ------------------------- |
| userId | String | 观众 ID。                 |
| agree  | bool   | true：同意；false：拒绝。 |


### kickoutJoinAnchor

主播踢除连麦观众。主播调用此接口踢除连麦观众后，被踢连麦观众会收到 `TRTCLiveRoomDelegate` 的 `onKickoutJoinAnchor()` 回调通知。

```java
Future<ActionCallback> kickoutJoinAnchor(String userId);
```

参数如下表所示：

| 参数   | 类型   | 含义          |
| ------ | ------ | ------------- |
| userId | String | 连麦观众 ID。 |


## 主播跨房间 PK

### requestRoomPK

主播请求跨房 PK。

```java
Future<ActionCallback> requestRoomPK(int roomId, String userId);
```

参数如下表所示：

| 参数   | 类型   | 含义            |
| ------ | ------ | --------------- |
| roomId | int    | 被邀约房间 ID。 |
| userId | String | 被邀约主播 ID。 |

主播和主播之间可以跨房间 PK，两个正在直播中的主播 A 和 B 之间的跨房 PK 流程如下：

1. 【主播 A】调用 `requestRoomPK()` 向主播 B 发起连麦请求。
2. 【主播 B】会收到 `TRTCLiveRoomDelegate` 的 `onRequestRoomPK()` 回调通知。
3. 【主播 B】调用 `responseRoomPK()` 决定是否接受主播 A 的 PK 请求。
4. 【主播 B】如果接受主播 A 的要求，等待 `TRTCLiveRoomDelegate` 的 `onAnchorEnter()` 通知，然后调用 `startPlay()` 来显示主播 A 的视频画面。
5. 【主播 A】会收到 `onRoomPKAccepted` 或`onRoomPKRejected`回调通知。
6. 【主播 A】如果请求被同意，等待 `TRTCLiveRoomDelegate` 的 `onAnchorEnter()` 通知，然后调用 `startPlay()` 显示主播 B 的视频画面。

   

### responseRoomPK

主播响应跨房 PK 请求。主播响应后，对方主播会收到 `requestRoomPK` 传入的 `responseCallback` 回调。

```java
Future<ActionCallback> responseRoomPK(String userId, boolean agree);
```

参数如下表所示：

| 参数   | 类型   | 含义                      |
| ------ | ------ | ------------------------- |
| userId | String | 发起 PK 请求的主播 ID。   |
| agree  | bool   | true：同意；false：拒绝。 |


### quitRoomPK

退出跨房 PK。PK 中的任何一个主播退出跨房 PK 状态后，另一个主播会收到 `TRTCLiveRoomDelegate` 的 `onQuitRoomPk()` 回调通知。

```java
Future<ActionCallback> quitRoomPK();
```


## 音视频控制相关接口函数

### switchCamera

切换前后摄像头。

```java
Future<void> switchCamera(boolean isFrontCamera);
```

### setMirror

设置是否镜像展示。

```java
Future<void> setMirror(boolean isMirror);
```

参数如下表所示：

| 参数     | 类型 | 含义            |
| -------- | ---- | --------------- |
| isMirror | bool | 开启/关闭镜像。 |

   

### muteLocalAudio

静音本地音频。

```java
Future<void> muteLocalAudio(boolean mute);
```

参数如下表所示：

| 参数 | 类型 | 含义                              |
| ---- | ---- | --------------------------------- |
| mute | boolean | true：开启静音；false：关闭静音。 |

   

### muteRemoteAudio

静音远端音频。

```java
Future<void> muteRemoteAudio(String userId, boolean mute);
```

参数如下表所示：

| 参数   | 类型   | 含义                              |
| ------ | ------ | --------------------------------- |
| userId | String | 远端的用户 ID。                   |
| mute   | boolean   | true：开启静音；false：关闭静音。 |

   

### muteAllRemoteAudio

静音所有远端音频。

```java
Future<void> muteAllRemoteAudio(boolean mute);
```

参数如下表所示：

| 参数 | 类型 | 含义                              |
| ---- | ---- | --------------------------------- |
| mute | boolean | true：开启静音；false：关闭静音。 |

   

## 背景音乐音效相关接口函数

### getAudioEffectManager

获取背景音乐音效管理对象 [TXAudioEffectManager](https://pub.dev/documentation/tencent_trtc_cloud/latest/tx_audio_effect_manager/TXAudioEffectManager-class.html)。

```java
getAudioEffectManager();
```


## 美颜滤镜相关接口函数

### getBeautyManager

获取美颜管理对象 [TXBeautyManager](https://pub.dev/documentation/tencent_trtc_cloud/latest/tx_beauty_manager/TXBeautyManager-class.html)。

```java
getBeautyManager();
```

通过美颜管理，您可以使用以下功能：

- 设置“美颜风格”、“美白”、“红润”、“大眼”、“瘦脸”、“V脸”、“下巴”、“短脸”、“小鼻”、“亮眼”、“白牙”、“祛眼袋”、“祛皱纹”、“祛法令纹”等美容效果。
- 调整“发际线”、“眼间距”、“眼角”、“嘴形”、“鼻翼”、“鼻子位置”、“嘴唇厚度”、“脸型”。
- 设置人脸挂件（素材）等动态效果。
- 添加美妆。
- 进行手势识别。


## 消息发送相关接口函数

### sendRoomTextMsg

在房间中广播文本消息，一般用于弹幕聊天。

```java
Future<ActionCallback> sendRoomTextMsg(String message);
```

参数如下表所示：

| 参数    | 类型   | 含义       |
| ------- | ------ | ---------- |
| message | String | 文本消息。 |

### sendRoomCustomMsg

发送自定义文本消息。

```java
Future<ActionCallback> sendRoomCustomMsg(String cmd, String message);
```

参数如下表所示：

| 参数    | 类型   | 含义                                               |
| ------- | ------ | -------------------------------------------------- |
| cmd     | String | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message | String | 文本消息。                                         |


## TRTCLiveRoomDelegate事件回调

## 通用事件回调

### onError

错误回调。

>?SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

参数如下表所示：

| 参数    | 类型   | 含义       |
| ------- | ------ | ---------- |
| errCode | int    | 错误码。   |
| errMsg  | String | 错误信息。 |


### onWarning

警告回调。

参数如下表所示：

| 参数        | 类型   | 含义       |
| ----------- | ------ | ---------- |
| warningCode | int    | 错误码。   |
| warningMsg  | String | 警告信息。 |


### onKickedOffline

其他用户登录了同一账号，被踢下线。




## 房间事件回调

### onRoomDestroy

房间被销毁的回调。主播退房时，房间内的所有用户都会收到此通知。

### onEnterRoom

本地进房

参数如下表所示：

| 参数   | 类型 | 含义                                                     |
| ------ | ---- | -------------------------------------------------------- |
| result | int  | result &gt; 0 时为进房耗时（ms），result &lt; 0 时为进房错误码。 |

### onUserVideoAvailable

远端用户是否存在可播放的主路画面（一般用于摄像头）。

参数如下表所示：

| 参数      | 类型   | 含义           |
| --------- | ------ | -------------- |
| userId    | String | 用户标识。     |
| available | boolean   | 画面是否开启。 |

## 主播和观众进出事件回调

### onAnchorEnter

收到新主播进房通知。连麦观众和跨房 PK 主播进房后观众会收到新主播的进房事件，您可以调用 `TRTCLiveRoom` 的 `startPlay()` 显示该主播的视频画面。


参数如下表所示：

| 参数       | 类型   | 含义            |
| ---------- | ------ | --------------- |
| userId     | String | 新进房主播 ID。 |
| userName   | String | 用户昵称。        |
| userAvatar | String | 用户头像地址。    |

### onAnchorExit

收到主播退房通知。房间内的主播（和连麦中的观众）会收到新主播的退房事件，您可以调用 `TRTCLiveRoom` 的 `stopPlay()` 关闭该主播的视频画面。

参数如下表所示：

| 参数       | 类型   | 含义           |
| ---------- | ------ | -------------- |
| userId     | String | 退出主播 ID。  |
| userName   | String | 用户昵称。     |
| userAvatar | String | 用户头像地址。 |


### onAudienceEnter

收到观众进房通知。

```java
void onAudienceEnter(TRTCLiveRoomDef.TRTCLiveUserInfo userInfo);
```

参数如下表所示：

| 参数     | 类型                             | 含义                                |
| -------- | -------------------------------- | ----------------------------------- |
| userInfo | TRTCLiveRoomDef.TRTCLiveUserInfo | 进房观众用户 ID、昵称、头像等信息。 |


### onAudienceExit

收到观众退房通知。


参数如下表所示：

| 参数       | 类型   | 含义           |
| ---------- | ------ | -------------- |
| userId     | String | 退房观众信息。 |
| userName   | String | 用户昵称。     |
| userAvatar | String | 用户头像地址。 |

### onRequestJoinAnchor

主播收到观众连麦请求时的回调。


参数如下表所示：

| 参数       | 类型   | 含义              |
| ---------- | ------ | ----------------- |
| userId     | String | 请求连麦用户 ID。 |
| userName   | String | 用户昵称。        |
| userAvatar | String | 用户头像地址。    |

### onAnchorAccepted

主播同意观众的连麦请求。


参数如下表所示：

| 参数   | 类型   | 含义            |
| ------ | ------ | --------------- |
| userId | String | 主播的用户 ID。 |


### onAnchorRejected

主播拒绝观众的连麦请求。


参数如下表所示：

| 参数   | 类型   | 含义            |
| ------ | ------ | --------------- |
| userId | String | 主播的用户 ID。 |

### onKickoutJoinAnchor

连麦观众收到被踢出连麦的通知。连麦观众收到被主播踢除连麦的消息，您需要调用 `TRTCLiveRoom` 的 `stopPublish()` 退出连麦。


## 主播 PK 事件回调

### onRequestRoomPK

收到请求跨房 PK 通知。主播收到其他房间主播的 PK 请求，如果同意 PK ，您需要等待 `TRTCLiveRoomDelegate` 的 `onAnchorEnter()` 通知，然后调用 `startPlay()` 来播放邀约主播的流。

参数如下表所示：

| 参数       | 类型   | 含义              |
| ---------- | ------ | ----------------- |
| userId     | String | 请求跨房用户 ID。 |
| userName   | String | 用户昵称。        |
| userAvatar | String | 用户头像地址。    |

### onRoomPKAccepted

主播接受跨房 PK 请求。

参数如下表所示：

| 参数   | 类型   | 含义                    |
| ------ | ------ | ----------------------- |
| userId | String | 接收跨房 PK 的用户 ID。 |

### onRoomPKRejected

主播接受跨房 PK 请求。

参数如下表所示：

| 参数   | 类型   | 含义                    |
| ------ | ------ | ----------------------- |
| userId | String | 拒绝跨房 PK 的用户 ID。 |


### onQuitRoomPK

收到断开跨房 PK 通知。


## 消息事件回调

### onRecvRoomTextMsg

收到文本消息。


参数如下表所示：

| 参数    | 类型   | 含义       |
| ------- | ------ | ---------- |
| message | String | 文本消息。 |


### onRecvRoomCustomMsg

收到自定义消息。


参数如下表所示：

| 参数    | 类型   | 含义                                               |
| ------- | ------ | -------------------------------------------------- |
| command | String | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message | String | 文本消息。                                         |


TRTCLiveRoom 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持以下功能：
- 主播创建新的直播间开播，观众进入直播间观看。
- 主播和观众进行视频连麦互动。
- 两个不同房间的主播 PK 互动。
- 支持发送各种文本消息和自定义消息，自定义消息可用于实现弹幕、点赞和礼物。

TRTCLiveRoom 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [视频连麦直播（Android）](https://cloud.tencent.com/document/product/647/43182)。
- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647/32689) 作为低延时直播组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269/36887) 的 AVChatroom 实现直播聊天室的功能，同时，通过 IM 消息串联主播间的连麦流程。

[](id:TRTCLiveRoom)
## TRTCLiveRoom API 概览

### SDK 基础函数

| API | 描述 |
|-----|-----|
| [sharedInstance](#sharedinstance) | 获取单例对象。 |
| [destroySharedInstance](#destroysharedinstance) | 销毁单例对象。 |
| [setDelegate](#setdelegate) | 设置事件回调。|
| [setDelegateHandler](#setdelegatehandler) | 设置事件回调所在的线程。 |
| [login](#login) | 登录。|
| [logout](#logout) | 登出。|
| [setSelfProfile](#setselfprofile) | 修改个人信息。|

### 房间相关接口函数

| API | 描述 |
|-----|-----|
| [createRoom](#createroom) | 创建房间（主播调用），若房间不存在，系统将自动创建一个新房间。|
| [destroyRoom](#destroyroom) | 销毁房间（主播调用）。|
| [enterRoom](#enterroom) | 进入房间（观众调用）。|
| [exitRoom](#exitroom) | 离开房间（观众调用）。|
| [getRoomInfos](#getroominfos) | 获取房间列表的详细信息。|
| [getAnchorList](#getanchorlist) | 获取房间内所有的主播列表，enterRoom() 成功后调用才有效。|
| [getAudienceList](#getaudiencelist) | 获取房间内所有的观众信息，enterRoom() 成功后调用才有效。|

### 推拉流相关接口函数

| API | 描述 |
|-----|-----|
| [startCameraPreview](#startcamerapreview) | 开启本地视频的预览画面。|
| [stopCameraPreview](#stopcamerapreview) | 停止本地视频采集及预览。|
| [startPublish](#startpublish) | 开始直播（推流）。|
| [stopPublish](#stoppublish) | 停止直播（推流）。|
| [startPlay](#startplay) | 播放远端视频画面，可以在普通观看和连麦场景中调用。|
| [stopPlay](#stopplay) | 停止渲染远端视频画面。|

### 主播和观众连麦

| API | 描述 |
|-----|-----|
| [requestJoinAnchor](#requestjoinanchor) | 观众请求连麦。|
| [responseJoinAnchor](#responsejoinanchor) | 主播处理连麦请求。|
| [kickoutJoinAnchor](#kickoutjoinanchor) | 主播踢除连麦观众。|

### 主播跨房间 PK

| API | 描述 |
|-----|-----|
| [requestRoomPK](#requestroompk) | 主播请求跨房 PK。|
| [responseRoomPK](#responseroompk) | 主播响应跨房 PK 请求。|
| [quitRoomPK](#quitroompk) | 退出跨房 PK。|

### 音视频控制相关接口函数

| API | 描述 |
|-----|-----|
| [switchCamera](#switchcamera) | 切换前后摄像头。|
| [setMirror](#setmirror) | 设置是否镜像展示。|
| [muteLocalAudio](#mutelocalaudio) | 静音本地音频。|
| [muteRemoteAudio](#muteremoteaudio) | 静音远端音频。|
| [muteAllRemoteAudio](#muteallremoteaudio) | 静音所有远端音频。|

### 背景音乐音效相关接口函数

| API | 描述 |
|-----|-----|
| [getAudioEffectManager](#getaudioeffectmanager) | 获取背景音乐音效管理对象 [TXAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXAudioEffectManager__android.html#interfacecom_1_1tencent_1_1liteav_1_1audio_1_1TXAudioEffectManager)。|

### 美颜滤镜相关接口函数

| API | 描述 |
|-----|-----|
| [getBeautyManager](#getbeautymanager) | 获取美颜管理对象 [TXBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__android.html#classcom_1_1tencent_1_1liteav_1_1beauty_1_1TXBeautyManager)。|

### 消息发送相关接口函数

| API | 描述 |
|-----|-----|
| [sendRoomTextMsg](#sendroomtextmsg) | 在房间中广播文本消息，一般用于弹幕聊天。|
| [sendRoomCustomMsg](#sendroomcustommsg) | 发送自定义文本消息。|

### 调试相关接口函数

| API | 描述 |
|-----|-----|
| [showVideoDebugLog](#showvideodebuglog) | 是否在界面中展示 debug 信息。|

<h2 id="TRTCLiveRoomDelegate">TRTCLiveRoomDelegate API 概览</h2>

### 通用事件回调

| API | 描述 |
|-----|-----|
| [onError](#onerror) | 错误回调。|
| [onWarning](#onwarning) | 警告回调。|
| [onDebugLog](#ondebuglog) | Log 回调。|

### 房间事件回调

| API | 描述 |
|-----|-----|
| [onRoomDestroy](#onroomdestroy) | 房间被销毁的回调。|
| [onRoomInfoChange](#onroominfochange) | 直播房间信息变更回调。|

### 主播和观众进出事件回调

| API | 描述 |
|-----|-----|
| [onAnchorEnter](#onanchorenter) | 收到新主播进房通知。|
| [onAnchorExit](#onanchorexit) | 收到主播退房通知。|
| [onAudienceEnter](#onaudienceenter) | 收到观众进房通知。|
| [onAudienceExit](#onaudienceexit) | 收到观众退房通知。|

### 主播和观众连麦事件回调

| API | 描述 |
|-----|-----|
| [onRequestJoinAnchor](#onrequestjoinanchor) | 主播收到观众连麦请求时的回调。|
| [onKickoutJoinAnchor](#onkickoutjoinanchor) | 连麦观众收到被踢出连麦的通知。|

### 主播 PK 事件回调

| API | 描述 |
|-----|-----|
| [onRequestRoomPK](#onrequestroompk) | 收到请求跨房 PK 通知。|
| [onQuitRoomPK](#onquitroompk) | 收到断开跨房 PK 通知。|

### 消息事件回调

| API | 描述 |
|-----|-----|
| [onRecvRoomTextMsg](#onrecvroomtextmsg) | 收到文本消息。|
| [onRecvRoomCustomMsg](#onrecvroomcustommsg) | 收到自定义消息。|

## SDK 基础函数

[](id:sharedInstance)
### sharedInstance

获取 [TRTCLiveRoom](https://cloud.tencent.com/document/product/647/43182) 单例对象。
```java
 public static synchronized TRTCLiveRoom sharedInstance(Context context);
```
参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| context | Context | Android 上下文，内部会转为 ApplicationContext 用于系统 API 调用 |

   

### destroySharedInstance

销毁 [TRTCLiveRoom](https://cloud.tencent.com/document/product/647/43182) 单例对象。
>?销毁实例后，外部缓存的 TRTCLiveRoom 实例无法再使用，需要重新调用 [sharedInstance](#sharedInstance) 获取新实例。

```java
public static void destroySharedInstance();
```   

### setDelegate

[TRTCLiveRoom](https://cloud.tencent.com/document/product/647/43182) 事件回调，您可以通过 TRTCLiveRoomDelegate 获得 [TRTCLiveRoom](https://cloud.tencent.com/document/product/647/43182) 的各种状态通知。
```java
public abstract void setDelegate(TRTCLiveRoomDelegate delegate);
```

>?setDelegate 是 TRTCLiveRoom 的代理回调。   

### setDelegateHandler

设置事件回调所在的线程。
```java
public abstract void setDelegateHandler(Handler handler);
```
参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| handler | Handler | TRTCLiveRoom 中的各种状态通知回调会通过该 handler 通知给您，请勿与 setDelegate 混用。 |

   

### login

登录。

<dx-codeblock>
::: java java
public abstract void login(int sdkAppId,
 String userId, String userSig,
 TRTCLiveRoomDef.TRTCLiveRoomConfig config, 
 TRTCLiveRoomCallback.ActionCallback callback);
:::
</dx-codeblock>

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sdkAppId | int |  您可以在实时音视频控制台 >【[应用管理](https://console.cloud.tencent.com/trtc/app)】> 应用信息中查看 SDKAppID。 |
| userId | String | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。 |
| userSig | String | 腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |
| config | TRTCLiveRoomConfig | 全局配置信息，请在登录时初始化，登录之后不可变更。<ul style="margin:0;"><li>useCDNFirst 属性：用于设置观众观看方式。true 表示普通观众通过 CDN 观看，计费便宜但延时较高。false 表示普通观众通过低延时观看，计费价格介于 CDN 和连麦之间，但延迟可控制在1s以内。</li><li>CDNPlayDomain 属性：在 useCDNFirst 设置为 true 时才会生效，用于指定 CDN 观看的播放域名，您可以登录直播控制台 >【<a href="https://console.cloud.tencent.com/live/domainmanage">域名管理</a>】页面中进行设置。</li></ul> |
| callback | ActionCallback | 登录回调，成功时 code 为0。 |

   

### logout

登出。
```java
public abstract void logout(TRTCLiveRoomCallback.ActionCallback callback);
```
参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | ActionCallback | 登出回调，成功时 code 为0。 |

   

### setSelfProfile

修改个人信息。
```java
public abstract void setSelfProfile(String userName, String avatarURL, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userName | String | 昵称。 |
| avatarURL | String | 头像地址。 |
| callback | ActionCallback | 个人信息设置回调，成功时 code 为0。 |

   


## 房间相关接口函数
### createRoom

创建房间（主播调用）。
```java
public abstract void createRoom(int roomId, TRTCLiveRoomDef.TRTCCreateRoomParam roomParam, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | int | 房间标识，需要由您分配并进行统一管理。多个 roomID 可以汇总成一个直播间列表，腾讯云暂不提供直播间列表的管理服务，请自行管理您的直播间列表。 |
| roomParam | TRTCCreateRoomParam | 房间信息，用于房间描述的信息，例如房间名称，封面信息等。如果房间列表和房间信息都由您的服务器自行管理，可忽略该参数。 |
| callback | ActionCallback | 创建房间的结果回调，成功时 code 为0。 |

主播开播的正常调用流程如下： 
1. 【主播】调用 `startCameraPreview()` 打开摄像头预览，此时可以调整美颜参数。 
2. 【主播】调用 `createRoom()` 创建直播间，房间创建成功与否会通过 ActionCallback 通知给主播。
3. 【主播】调用 `starPublish()` 开始推流。

   

### destroyRoom

销毁房间（主播调用）。主播在创建房间后，可以调用该函数来销毁房间。
```java
public abstract void destroyRoom(TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | ActionCallback | 销毁房间的结果回调，成功时 code 为0。 |
   

### enterRoom

进入房间（观众调用）。
```java
public abstract void enterRoom(int roomId, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | int | 房间标识。 |
| callback | ActionCallback | 进入房间的结果回调，成功时 code 为0。 |


观众观看直播的正常调用流程如下： 
1. 【观众】向您的服务端获取最新的直播间列表，可能包含多个直播间的 roomID 和房间信息。
2. 【观众】观众选择一个直播间，并调用 `enterRoom()` 进入该房间。
3. 【观众】调用`startPlay(userId)`并传入主播的 userId 开始播放。
 - 若直播间列表已包含主播端的 userId 信息，观众端可直接调用 `startPlay(userId)` 即可开始播放。
 - 若在进房前暂未获取主播的 userId，观众端在进房后会收到 `TRTCLiveRoomDelegate` 中的 `onAnchorEnter(userId)` 的事件回调，该回调中携带主播的 userId 信息，再调用`startPlay(userId)`即可播放。 

   

### exitRoom

离开房间。
```java
public abstract void exitRoom(TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | ActionCallback | 退出房间的结果回调，成功时 code 为0。 |

   

### getRoomInfos

获取房间列表的详细信息，房间信息是主播在创建 `createRoom()` 时通过 roomInfo 设置的。
>?如果房间列表和房间信息都由您自行管理，可忽略该函数。


```java
public abstract void getRoomInfos(List<Integer> roomIdList, TRTCLiveRoomCallback.RoomInfoCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomIdList | List&lt;Integer&gt; | 房间号列表。 |
| callback | RoomInfoCallback | 房间详细信息回调。 |
   

### getAnchorList

获取房间内所有的主播列表，`enterRoom()` 成功后调用才有效。
```java
public abstract void getAnchorList(TRTCLiveRoomCallback.UserListCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | UserListCallback | 用户详细信息回调。 |

   

### getAudienceList

获取房间内所有的观众信息，`enterRoom()` 成功后调用才有效。
```java
public abstract void getAudienceList(TRTCLiveRoomCallback.UserListCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | UserListCallback | 用户详细信息回调。 |

   

## 推拉流相关接口函数
### startCameraPreview

开启本地视频的预览画面。
```java
public abstract void startCameraPreview(boolean isFront, TXCloudVideoView view, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isFront | boolean | true：前置摄像头；false：后置摄像头。 |
| view | TXCloudVideoView | 承载视频画面的控件。 |
| callback | ActionCallback | 操作回调。|

   

### stopCameraPreview

停止本地视频采集及预览。
```java
public abstract void stopCameraPreview();
```

   

### startPublish

开始直播（推流），适用于以下场景：
- 主播开播的时候调用
- 观众开始连麦时调用


```java
public abstract void startPublish(String streamId, TRTCLiveRoomCallback.ActionCallback callback);
```
参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| streamId | String | 用于绑定直播 CDN 的 streamId，如果您希望观众通过直播 CDN 进行观看，需要指定当前主播的直播 streamId。|
| callback | ActionCallback | 操作回调。|
   

### stopPublish

停止直播（推流），适用于以下场景：
- 主播结束直播时调用
- 观众结束连麦时调用


```java
public abstract void stopPublish(TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | ActionCallback | 操作回调。|



   

### startPlay

播放远端视频画面，可以在普通观看和连麦场景中调用。
```java
public abstract void startPlay(String userId, TXCloudVideoView view, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 需要观看的用户id。 |
| view | TXCloudVideoView | 承载视频画面的 view 控件。 |
| callback | ActionCallback | 操作回调。|

**普通观看场景**
- 若直播间列表已包含主播端的 userId 信息，观众端可以直接在 `enterRoom()` 成功后调用 `startPlay(userId)` 播放主播的画面。
- 若在进房前暂未获取主播的 userId，观众端在进房后会收到 `TRTCLiveRoomDelegate` 中的 `onAnchorEnter(userId)` 的事件回调，该回调中携带主播的 userId 信息，再调用`startPlay(userId)`即可播放主播的画面。

**直播连麦场景**
发起连麦后，主播会收到来自 `TRTCLiveRoomDelegate` 中的 `onAnchorEnter(userId)` 回调，此时使用回调中的 userId 调用 startPlay(userId) 即可播放连麦画面。

   

### stopPlay

停止渲染远端视频画面。需在 `onAnchorExit()` 回调时，调用该接口。
```java
public abstract void stopPlay(String userId, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 对方的用户信息。|
| callback | ActionCallback | 操作回调。|
   

## 主播和观众连麦
### requestJoinAnchor

观众请求连麦。
```java
public abstract void requestJoinAnchor(String reason, int timeout, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reason | String | 连麦原因。 |
| timeout | int | 超时时间。 |
| callback | ActionCallback | 主播响应回调。 |


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
public abstract void responseJoinAnchor(String userId, boolean agree, String reason);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 观众 ID。 |
| agree | boolean | true：同意；false：拒绝。 |
| reason | String | 同意/拒绝连麦的原因描述。 |
   

### kickoutJoinAnchor

主播踢除连麦观众。主播调用此接口踢除连麦观众后，被踢连麦观众会收到 `TRTCLiveRoomDelegate` 的 `onKickoutJoinAnchor()` 回调通知。

```java
public abstract void kickoutJoinAnchor(String userId, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 连麦观众 ID。 |
| callback | ActionCallback | 操作回调。|
  


## 主播跨房间 PK
### requestRoomPK

主播请求跨房 PK。
```java
public abstract void requestRoomPK(int roomId, String userId, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | int | 被邀约房间 ID。 |
| userId | String | 被邀约主播 ID。 |
| callback | ActionCallback | 请求跨房 PK 的结果回调。 |

主播和主播之间可以跨房间 PK，两个正在直播中的主播 A 和 B 之间的跨房 PK 流程如下：
1. 【主播 A】调用 `requestRoomPK()` 向主播 B 发起连麦请求。
2. 【主播 B】会收到 `TRTCLiveRoomDelegate` 的 `onRequestRoomPK()` 回调通知。
3. 【主播 B】调用 `responseRoomPK()` 决定是否接受主播 A 的 PK 请求。
4. 【主播 B】如果接受主播 A 的要求，等待 `TRTCLiveRoomDelegate` 的 `onAnchorEnter()` 通知，然后调用 `startPlay()` 来显示主播 A 的视频画面。
5. 【主播 A】会收到 `responseCallback` 回调通知，该通知会携带来自主播 B 的处理结果。
6. 【主播 A】如果请求被同意，等待 `TRTCLiveRoomDelegate` 的 `onAnchorEnter()` 通知，然后调用 `startPlay()` 显示主播 B 的视频画面。

   

### responseRoomPK

主播响应跨房 PK 请求。主播响应后，对方主播会收到 `requestRoomPK` 传入的 `responseCallback` 回调。
```java
public abstract void responseRoomPK(String userId, boolean agree, String reason);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 发起 PK 请求的主播 ID。 |
| agree | boolean | true：同意；false：拒绝。 |
| reason | String | 同意/拒绝 PK 的原因描述。 |
   

### quitRoomPK

退出跨房 PK。PK 中的任何一个主播退出跨房 PK 状态后，另一个主播会收到 `TRTCLiveRoomDelegate` 的 `onQuitRoomPk()` 回调通知。
```java
public abstract void quitRoomPK(TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | ActionCallback | 操作回调。|
   

## 音视频控制相关接口函数
### switchCamera

切换前后摄像头。
```java
public abstract void switchCamera();
```

   

### setMirror

设置是否镜像展示。
```java
public abstract void setMirror(boolean isMirror);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isMirror | boolean | 开启/关闭镜像。 |

   

### muteLocalAudio

静音本地音频。
```java
public abstract void muteLocalAudio(boolean mute);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | boolean | true：开启静音；false：关闭静音。|

   

### muteRemoteAudio

静音远端音频。
```java
public abstract void muteRemoteAudio(String userId, boolean mute);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 远端的用户 ID。 |
| mute | boolean | true：开启静音；false：关闭静音。|

   

### muteAllRemoteAudio

静音所有远端音频。
```java
public abstract void muteAllRemoteAudio(boolean mute);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | boolean | true：开启静音；false：关闭静音。|

   

## 背景音乐音效相关接口函数
### getAudioEffectManager

获取背景音乐音效管理对象 [TXAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3646dad993287c3a1a38a5bc0e6e33aa)。
```java
public abstract TXAudioEffectManager getAudioEffectManager();
```
   

## 美颜滤镜相关接口函数
### getBeautyManager

获取美颜管理对象 [TXBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__android.html#classcom_1_1tencent_1_1liteav_1_1beauty_1_1TXBeautyManager)。
```java
public abstract TXBeautyManager getBeautyManager();
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
public abstract void sendRoomTextMsg(String message, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| message | String | 文本消息。 |
| callback | ActionCallback | 发送结果回调。|

   

### sendRoomCustomMsg

发送自定义文本消息。
```java
public abstract void sendRoomCustomMsg(String cmd, String message, TRTCLiveRoomCallback.ActionCallback callback);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| cmd | String | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message | String | 文本消息。 |
| callback | ActionCallback | 发送结果回调。|

   

## 调试相关接口函数
### showVideoDebugLog

是否在界面中展示debug信息。
```java
public abstract void showVideoDebugLog(boolean isShow);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isShow | boolean | 开启/关闭 Debug 信息显示。 |

   

## TRTCLiveRoomDelegate事件回调

## 通用事件回调
### onError

错误回调。
>?SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```java
void onError(int code, String message);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | int | 错误码。 |
| message | String | 错误信息。 |
   

### onWarning

警告回调。
```java
void onWarning(int code, String message);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | int | 错误码。 |
| message | String | 警告信息。 |

   

### onDebugLog

Log 回调。
```java
void onDebugLog(String message);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| message | String | 日志信息。 |

   


## 房间事件回调
### onRoomDestroy

房间被销毁的回调。主播退房时，房间内的所有用户都会收到此通知。
```java
void onRoomDestroy(String roomId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomId | String | 房间 ID。 |



   

### onRoomInfoChange

直播房间信息变更回调。多用于直播连麦、PK下房间状态变化通知场景。
```java
void onRoomInfoChange(TRTCLiveRoomDef.TRTCLiveRoomInfo roomInfo);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| roomInfo | TRTCLiveRoomInfo | 房间信息。 |

   


## 主播和观众进出事件回调
### onAnchorEnter

收到新主播进房通知。连麦观众和跨房 PK 主播进房后观众会收到新主播的进房事件，您可以调用 `TRTCLiveRoom` 的 `startPlay()` 显示该主播的视频画面。
```java
void onAnchorEnter(String userId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 新进房主播 ID。 |
   

### onAnchorExit

收到主播退房通知。房间内的主播（和连麦中的观众）会收到新主播的退房事件，您可以调用 `TRTCLiveRoom` 的 `stopPlay()` 关闭该主播的视频画面。
```java
void onAnchorExit(String userId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 退房用户 ID。 |
   

### onAudienceEnter

收到观众进房通知。
```java
void onAudienceEnter(TRTCLiveRoomDef.TRTCLiveUserInfo userInfo);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userInfo | TRTCLiveUserInfo | 进房观众信息。 |

   

### onAudienceExit

收到观众退房通知。
```java
void onAudienceExit(TRTCLiveRoomDef.TRTCLiveUserInfo userInfo);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userInfo | TRTCLiveUserInfo | 退房观众信息。 |

   


## 主播和观众连麦事件回调
### onRequestJoinAnchor

主播收到观众连麦请求时的回调。
```java
void onRequestJoinAnchor(TRTCLiveRoomDef.TRTCLiveUserInfo userInfo, String reason, int timeOut);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userInfo | TRTCLiveUserInfo | 请求连麦观众信息。|
| reason | String | 连麦原因描述。|
| timeout | int | 处理请求的超时时间，如果上层超过该时间没有处理，则会自动将该次请求废弃。 |

   

### onKickoutJoinAnchor

连麦观众收到被踢出连麦的通知。连麦观众收到被主播踢除连麦的消息，您需要调用 `TRTCLiveRoom` 的 `stopPublish()` 退出连麦。
```java
void onKickoutJoinAnchor();
```
  


## 主播 PK 事件回调
### onRequestRoomPK

收到请求跨房 PK 通知。主播收到其他房间主播的 PK 请求，如果同意 PK ，您需要等待 `TRTCLiveRoomDelegate` 的 `onAnchorEnter()` 通知，然后调用 `startPlay()` 来播放邀约主播的流。
```java
void onRequestRoomPK(TRTCLiveRoomDef.TRTCLiveUserInfo userInfo, int timeout);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userInfo | TRTCLiveUserInfo | 发起跨房连麦的主播信息。|
| timeout | int | 处理请求的超时时间。 |
   

### onQuitRoomPK

收到断开跨房 PK 通知。
```java
void onQuitRoomPK();
```

   


## 消息事件回调
### onRecvRoomTextMsg

收到文本消息。
```java
void onRecvRoomTextMsg(String message, TRTCLiveRoomDef.TRTCLiveUserInfo userInfo);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| message | String | 文本消息。|
| userInfo | TRTCLiveUserInfo | 发送者用户信息。|

   

### onRecvRoomCustomMsg

收到自定义消息。
```java
void onRecvRoomCustomMsg(String cmd, String message, TRTCLiveRoomDef.TRTCLiveUserInfo userInfo);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| command | String | 命令字，由开发者自定义，主要用于区分不同消息类型。|
| message | String | 文本消息。|
| userInfo | TRTCLiveUserInfo | 发送者用户信息。 |

   
[](id:TRTCAudioEffectManager)
## TRTCAudioEffectManager
### playBGM

播放背景音乐。
```java
void playBGM(String url, int loopTimes, int bgmVol, int micVol, TRTCCloud.BGMNotify notify);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| url | String | 背景音乐文件路径。 |
| loopTimes | int | 循环次数 |
| bgmVol | int | BGM 音量 |
| micVol | int | 采集音量 |
| notify | TRTCCloud.BGMNotify | 播放通知 |

   

### stopBGM

停止播放背景音乐。
```java
void stopBGM();
```

   

### pauseBGM

暂停播放背景音乐。
```java
void pauseBGM();
```

   

### resumeBGM

继续播放背景音乐。
```java
void resumeBGM();
```

   

### setBGMVolume

设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音的音量大小。
```java
void setBGMVolume(int volume);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 音量大小，100表示正常音量，取值范围为0 - 100，默认值为100。 |

   

### setBGMPosition

设置背景音乐播放进度。
```java
int setBGMPosition(int position);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| position | int | 背景音乐播放进度，单位为毫秒（ms）。 |

__返回__

0：成功。

   

### setMicVolume

设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小。
```java
void setMicVolume(int volume);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | Int | 音量大小，取值0 - 100，默认值为100。 |

   

### setReverbType

设置混响效果。
```java
void setReverbType(int reverbType);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reverbType | int | 混响类型，详情请参见 `TRTCCloudDef` 中的 [TRTC_REVERB_TYPE](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#a60ecba31f49f70780e623d24bcfa1a7d) 定义。 |

   

### setVoiceChangerType

设置变声类型。
```java
void setVoiceChangerType(int type);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| type | int | 混响类型，详情请参见 `TRTCCloudDef` 中的 [TRTC_VOICE_CHANGER_TYPE](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#a899e72b3e4a16288e6c2edfd779e3beb) 定义。 |

   

### playAudioEffect

播放音效，每个音效都需要您指定具体的 ID，您可以通过该 ID 对音效的开始、停止、音量等进行设置。支持 aac、mp3 以及 m4a 格式。
```java
void playAudioEffect(int effectId, String path, int count, boolean publish, int volume);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| effectId | int | 音效 ID。 |
| path | String | 音效路径。 |
| count | int | 循环次数。 |
| publish | boolean | 是否推送 / true 推送给观众, false 本地预览。 |
| volume | int | 音量大小，取值范围为0 - 100，默认值为100。 |

   

### pauseAudioEffect

暂停音效播放。
```java
void pauseAudioEffect(int effectId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| effectId | int | 音效 ID。 |

   

### resumeAudioEffect

恢复音效播放。
```java
void resumeAudioEffect(int effectId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| effectId | int | 音效 ID。 |

   

### stopAudioEffect

停止音效播放。
```java
void stopAudioEffect(int effectId);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| effectId | int | 音效 ID。 |

   

### stopAllAudioEffects

停止全部音效播放。
```java
void stopAllAudioEffects();
```

   

### setAudioEffectVolume

设置音效音量。
```java
void setAudioEffectVolume(int effectId, int volume);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| effectId | int | 音效 ID。 |
| volume | int | 音量大小，取值范围为0 - 100，默认值为100。 |

   

### setAllAudioEffectsVolume

设置所有音效的音量。
```java
void setAllAudioEffectsVolume(int volume);
```

参数如下表所示：

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 音量大小，取值范围为0 - 100，默认值为100。 |

   

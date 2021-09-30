TRTCLiveRoom 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持以下功能：

- 主播创建新的直播间开播，观众进入直播间观看。
- 主播和观众进行视频连麦互动。
- 两个不同房间的主播 PK 互动。
- 支持发送各种文本消息和自定义消息，自定义消息可用于实现弹幕、点赞和礼物。

TRTCLiveRoom 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [视频连麦直播（iOS）](https://cloud.tencent.com/document/product/647/43181)。

- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647/32689) 作为低延时直播组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269/36887) 的 AVChatroom 实现直播聊天室的功能，同时，通过 IM 消息串联主播间的连麦流程。



<h2 id="TRTCLiveRoom">TRTCLiveRoom API 概览</h2>

### SDK 基础函数

| API                               | 描述           |
| --------------------------------- | -------------- |
| [delegate](#delegate)             | 设置事件回调。 |
| [login](#login)                   | 登录。         |
| [logout](#logout)                 | 登出。         |
| [setSelfProfile](#setselfprofile) | 修改个人信息。 |

### 房间相关接口函数

| API                                 | 描述                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| [createRoom](#createroom)           | 创建房间（主播调用），若房间不存在，系统将自动创建一个新房间。 |
| [destroyRoom](#destroyroom)         | 销毁房间（主播调用）。                                       |
| [enterRoom](#enterroom)             | 进入房间（观众调用）。                                       |
| [exitRoom](#exitroom)               | 离开房间（观众调用）。                                       |
| [getRoomInfos](#getroominfos)       | 获取房间列表的详细信息。                                     |
| [getAnchorList](#getanchorlist)     | 获取房间内所有的主播列表，enterRoom() 成功后调用才有效。     |
| [getAudienceList](#getaudiencelist) | 获取房间内所有的观众信息，enterRoom() 成功后调用才有效。     |

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
| [getAudioEffectManager](#getaudioeffectmanager) | 获取背景音乐音效管理对象 [TXAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXAudioEffectManager__ios.html#interfaceTXAudioEffectManager)。 |

### 美颜滤镜相关接口函数

| API                                   | 描述                                                         |
| ------------------------------------- | ------------------------------------------------------------ |
| [getBeautyManager](#getbeautymanager) | 获取美颜管理对象 [TXBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__ios.html#interfaceTXBeautyManager)。 |

### 消息发送相关接口函数

| API                                     | 描述                                     |
| --------------------------------------- | ---------------------------------------- |
| [sendRoomTextMsg](#sendroomtextmsg)     | 在房间中广播文本消息，一般用于弹幕聊天。 |
| [sendRoomCustomMsg](#sendroomcustommsg) | 发送自定义文本消息。                     |

### 调试相关接口函数

| API                                     | 描述                        |
| --------------------------------------- | --------------------------- |
| [showVideoDebugLog](#showvideodebuglog) | 是否在界面中展示debug信息。 |

<h2 id="TRTCLiveRoomDelegate">TRTCLiveRoomDelegate API 概览</h2>

### 通用事件回调

| API                       | 描述       |
| ------------------------- | ---------- |
| [onError](#onerror)       | 错误回调。 |
| [onWarning](#onwarning)   | 警告回调。 |
| [onDebugLog](#ondebuglog) | Log 回调。 |

### 房间事件回调

| API                                   | 描述                   |
| ------------------------------------- | ---------------------- |
| [onRoomDestroy](#onroomdestroy)       | 房间被销毁的回调。     |
| [onRoomInfoChange](#onroominfochange) | 直播房间信息变更回调。 |

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
| [onKickoutJoinAnchor](#onkickoutjoinanchor) | 连麦观众收到被踢出连麦的通知。 |

### 主播 PK 事件回调

| API                                 | 描述                   |
| ----------------------------------- | ---------------------- |
| [onRequestRoomPK](#onrequestroompk) | 收到请求跨房 PK 通知。 |
| [onQuitRoomPK](#onquitroompk)       | 收到断开跨房 PK 通知。 |

### 消息事件回调

| API                                         | 描述             |
| ------------------------------------------- | ---------------- |
| [onRecvRoomTextMsg](#onrecvroomtextmsg)     | 收到文本消息。   |
| [onRecvRoomCustomMsg](#onrecvroomcustommsg) | 收到自定义消息。 |



## SDK 基础函数

### delegate

[TRTCLiveRoom](https://cloud.tencent.com/document/product/647/43181) 事件回调，您可以通过 TRTCLiveRoomDelegate 获得 [TRTCLiveRoom](https://cloud.tencent.com/document/product/647/43181) 的各种状态通知。

```objc
@property(nonatomic, weak)id<TRTCLiveRoomDelegate> delegate;
```

>?delegate 是 TRTCLiveRoom 的代理回调。


### login

登录。

```objc
/// 登录到组件系统
/// - Parameters:
///   - sdkAppID: 您可以在实时音视频控制台 > 【[应用管理](https://console.cloud.tencent.com/trtc/app)】> 应用信息中查看 SDKAppID。
///   - userID: 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。
///   - userSig:  腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。
///   - config: 全局配置信息，请在登录时初始化，登录之后不可变更。 isAttachedTUIKit 项目中是否引入并使用TUIKit
///   - callback: 登录回调，成功时 code 为0。
/// - Note:
///   - userSig 建议设定 7 天，能够有效规避 usersign 过期导致的 IM 收发消息失败、TRTC 连麦失败等情况
- (void)loginWithSdkAppID:(int)sdkAppID
                  userID:(NSString *)userID
                 userSig:(NSString *)userSig
                  config:(TRTCLiveRoomConfig *)config
                callback:(Callback _Nullable)callback
NS_SWIFT_NAME(login(sdkAppID:userID:userSig:config:callback:));
```

参数如下表所示：

| 参数     | 类型                                      | 含义                                                         |
| -------- | ----------------------------------------- | ------------------------------------------------------------ |
| sdkAppID | Int                                       | 您可以在实时音视频控制台 >【[应用管理](https://console.cloud.tencent.com/trtc/app)】> 应用信息中查看 SDKAppID。 |
| userID   | String                                    | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。 |
| userSig  | String                                    | 腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |
| config   | TRTCLiveRoomConfig                        | 全局配置信息，请在登录时初始化，登录之后不可变更。<ul style="margin:0;"><li>useCDNFirst 属性：用于设置观众观看方式。true 表示普通观众通过 CDN 观看，计费便宜但延时较高。false 表示普通观众通过低延时观看，计费价格介于 CDN 和连麦之间，但延迟可控制在1s以内。</li><li>CDNPlayDomain 属性：在 useCDNFirst 设置为 true 时才会生效，用于指定 CDN 观看的播放域名，您可以登录直播控制台 >【<a href="https://console.cloud.tencent.com/live/domainmanage">域名管理</a>】页面中进行设置。</li></ul> |
| callback | (_ code: Int, _ message: String?) -> Void | 登录回调，成功时 code 为0。                                  |


### logout

登出。

```objc
// 退出登录
/// - Parameter callback:  登出回调，成功时 code 为0
- (void)logout:(Callback _Nullable)callback
NS_SWIFT_NAME(logout(_:));
```

参数如下表所示：

| 参数     | 类型                                      | 含义                        |
| -------- | ----------------------------------------- | --------------------------- |
| callback | (_ code: Int, _ message: String?) -> Void | 登出回调，成功时 code 为0。 |


### setSelfProfile

修改个人信息。

```objc
/// 设置用户信息，您设置的用户信息会被存储于腾讯云 IM 云服务中。
/// - Parameters:
///   - name: 用户昵称
///   - avatarURL: 用户头像地址
///   - callback: 个人信息设置回调，成功时 code 为0
- (void)setSelfProfileWithName:(NSString *)name
                     avatarURL:(NSString * _Nullable)avatarURL
                      callback:(Callback _Nullable)callback
NS_SWIFT_NAME(setSelfProfile(name:avatarURL:callback:));
```

参数如下表所示：

| 参数      | 类型                                      | 含义                                |
| --------- | ----------------------------------------- | ----------------------------------- |
| name      | String                                    | 昵称。                              |
| avatarURL | String                                    | 头像地址。                          |
| callback  | (_ code: Int, _ message: String?) -> Void | 个人信息设置回调，成功时 code 为0。 |


## 房间相关接口函数

### createRoom

创建房间（主播调用）。

```objc
/// 创建房间（主播调用），若房间不存在，系统将自动创建一个新房间。
/// 主播开播的正常调用流程是：
/// 1.【主播】调用 startCameraPreview() 打开摄像头预览，此时可以调整美颜参数。
/// 2.【主播】调用 createRoom() 创建直播间，房间创建成功与否会通过 callback 通知给主播。
/// 3.【主播】调用 startPublish() 开始推流。
/// - Parameters:
///   - roomID: 房间标识，需要由您分配并进行统一管理。多个 roomid 可以汇总成一个直播间列表，腾讯云暂不提供直播间列表的管理服务，请自行管理您的直播间列表。
///   - roomParam: TRTCCreateRoomParam | 房间信息，用于房间描述的信息，例如房间名称，封面信息等。如果房间列表和房间信息都由您自行管理，可忽略该参数。
///   - callback:  进入房间的结果回调，成功时 code 为0。
/// - Note:
///   - 主播开始直播的时候调用，可重复创建自己已创建过的房间。
- (void)createRoomWithRoomID:(UInt32)roomID
                   roomParam:(TRTCCreateRoomParam *)roomParam
                    callback:(Callback _Nullable)callback
NS_SWIFT_NAME(createRoom(roomID:roomParam:callback:));
```

参数如下表所示：

| 参数      | 类型                                      | 含义                                                         |
| --------- | ----------------------------------------- | ------------------------------------------------------------ |
| roomID    | UInt32                                    | 房间标识，需要由您分配并进行统一管理。多个 roomID 可以汇总成一个直播间列表，腾讯云暂不提供直播间列表的管理服务，请自行管理您的直播间列表。 |
| roomParam | TRTCCreateRoomParam                       | 房间信息，用于房间描述的信息，例如房间名称，封面信息等。如果房间列表和房间信息都由您自行管理，可忽略该参数。 |
| callback  | (_ code: Int, _ message: String?) -> Void | 创建房间的结果回调，成功时 code 为0。                        |

主播开播的正常调用流程如下： 

1. 【主播】调用 `startCameraPreview()` 打开摄像头预览，此时可以调整美颜参数。 
2. 【主播】调用 `createRoom()` 创建直播间，房间创建成功与否会通过 callback 通知给主播。
3. 【主播】调用 `starPublish()` 开始推流。

### destroyRoom

销毁房间（主播调用）。主播在创建房间后，可以调用该函数来销毁房间。

```objc
/// 销毁房间（主播调用）
/// 主播在创建房间后，可以调用这个函数来销毁房间。
/// - Parameter callback: 销毁房间的结果回调，成功时 code 为0。
/// - Note:
///   - 主播在创建房间后，可以调用该函数来销毁房间。
- (void)destroyRoom:(Callback _Nullable)callback
NS_SWIFT_NAME(destroyRoom(callback:));
```

参数如下表所示：

| 参数     | 类型                                      | 含义                                  |
| -------- | ----------------------------------------- | ------------------------------------- |
| callback | (_ code: Int, _ message: String?) -> Void | 销毁房间的结果回调，成功时 code 为0。 |



### enterRoom

进入房间（观众调用）。

```objc
/// 进入房间（观众调用）
/// 观众观看直播的正常调用流程是：
/// 1.【观众】向您的服务端获取最新的直播间列表，其中有多个直播间的 roomid 和房间信息。
/// 2.【观众】观众选择一个直播间以后，调用 enterRoom() 进入该房间。
/// 3.【观众】如果您的服务器所管理的房间列表中包含每一个房间的主播 userID，则可以直接在 enterRoom() 成功后调用 startPlay(userID) 即可播放主播的画面。
/// 如果您管理的房间列表只有 roomid 也没有关系，观众在 enterRoom() 成功后很快会收到来自 TRTCLiveRoomDelegate 中的 onAnchorEnter(userID) 回调。
/// 此时使用回调中的 userID 调用 startPlay(userID) 即可播放主播的画面。
/// - Parameters:
///   - roomID: 房间标识。
///   - useCDNFirst: 是否优先使用CDN播放
///   - cdnDomain: CDN域名
///   - callback: 进入房间的结果回调，成功时 code 为0。
/// - Note:
///   - 观众进入直播房间的时候调用
///   - 主播不可调用这个接口进入自己已创建的房间，而要用createRoom
- (void)enterRoomWithRoomID:(UInt32)roomID
                useCDNFirst:(BOOL)useCDNFirst
                  cdnDomain:(NSString * _Nullable)cdnDomain
                   callback:(Callback)callback
NS_SWIFT_NAME(enterRoom(roomID:useCDNFirst:cdnDomain:callback:));
```

参数如下表所示：

| 参数     | 类型                                      | 含义                                  |
| -------- | ----------------------------------------- | ------------------------------------- |
| roomID   | UInt32                                    | 房间标识。                            |
| callback | (_ code: Int, _ message: String?) -> Void | 进入房间的结果回调，成功时 code 为0。 |



观众观看直播的正常调用流程如下： 

1. 【观众】向您的服务端获取最新的直播间列表，可能包含多个直播间的 roomID 和房间信息。
2. 【观众】观众选择一个直播间，并调用 `enterRoom()` 进入该房间。
3. 【观众】调用`startPlay(userID)`并传入主播的 userID 开始播放。
 - 若直播间列表已包含主播端的 userID 信息，观众端可直接调用 `startPlay(userID)` 即可开始播放。
 - 若在进房前暂未获取主播的 userID，观众端在进房后会收到 `TRTCLiveRoomDelegate` 中的 `onAnchorEnter(userID)` 的事件回调，该回调中携带主播的 userID 信息，再调用`startPlay(userID)`即可播放。 



### exitRoom

离开房间。

```objc
/// 退出房间（观众调用）
/// - Parameter callback: 退出房间的结果回调，成功时 code 为0。
/// - Note:
///   - 观众离开直播房间的时候调用
///   - 主播不可调用这个接口离开房间

- (void)exitRoom:(Callback _Nullable)callback
NS_SWIFT_NAME(exitRoom(callback:));
```

参数如下表所示：

| 参数     | 类型                                      | 含义                                  |
| -------- | ----------------------------------------- | ------------------------------------- |
| callback | (_ code: Int, _ message: String?) -> Void | 退出房间的结果回调，成功时 code 为0。 |

### getRoomInfos

获取房间列表的详细信息，房间信息是主播在创建 `createRoom()` 时通过 roomInfo 设置的。
>?如果房间列表和房间信息都由您自行管理，可忽略该函数。

```objc
/// 获取房间列表的详细信息
/// 其中的信息是主播在创建 createRoom() 时通过 roomInfo 设置进来的，如果房间列表和房间信息都由您自行管理，可忽略该函数。
/// - Parameter roomIDs: 房间号列表
/// - Parameter callback: 房间详细信息回调
- (void)getRoomInfosWithRoomIDs:(NSArray<NSNumber *> *)roomIDs
                       callback:(RoomInfoCallback _Nullable)callback
NS_SWIFT_NAME(getRoomInfos(roomIDs:callback:));

```

参数如下表所示：

| 参数     | 类型                                                         | 含义               |
| -------- | ------------------------------------------------------------ | ------------------ |
| roomIDs  | [UInt32]                                                       | 房间号列表。       |
| callback | (_ code: Int, _ message: String?, _ roomList: [TRTCLiveRoomInfo]) -> Void | 房间详细信息回调。 |



### getAnchorList

获取房间内所有的主播列表，`enterRoom()` 成功后调用才有效。

```objc
/// 获取房间内所有的主播列表，enterRoom() 成功后调用才有效。
/// - Parameter callback: 用户详细信息回调
- (void)getAnchorList:(UserListCallback _Nullable)callback
NS_SWIFT_NAME(getAnchorList(callback:));

```

参数如下表所示：

| 参数     | 类型                                                         | 含义               |
| -------- | ------------------------------------------------------------ | ------------------ |
| callback | (_ code: Int, _ message: String, _ userList: [TRTCLiveUserInfo]) -> Void | 用户详细信息回调。 |


### getAudienceList

获取房间内所有的观众信息，`enterRoom()` 成功后调用才有效。

```objc
/// 获取房间内所有的观众信息，enterRoom() 成功后调用才有效。
/// - Parameter callback: 用户详细信息回调
- (void)getAudienceList:(UserListCallback _Nullable)callback
NS_SWIFT_NAME(getAudienceList(callback:));

```

参数如下表所示：

| 参数     | 类型                                                         | 含义               |
| -------- | ------------------------------------------------------------ | ------------------ |
| callback | (_ code: Int, _ message: String, _ userList: [TRTCLiveUserInfo]) -> Void | 用户详细信息回调。 |


## 推拉流相关接口函数

### startCameraPreview

开启本地视频的预览画面。

```objc
/// 开启本地视频的预览画面
/// - Parameters:
///   - frontCamera: true：前置摄像头；false：后置摄像头。
///   - view: 承载视频画面的控件。
///   - callback: 操作回调。
- (void)startCameraPreviewWithFrontCamera:(BOOL)frontCamera
                                     view:(UIView *)view
                                 callback:(Callback _Nullable)callback
NS_SWIFT_NAME(startCameraPreview(frontCamera:view:callback:));

```

参数如下表所示：

| 参数        | 类型                                      | 含义                                  |
| ----------- | ----------------------------------------- | ------------------------------------- |
| frontCamera | Bool                                      | true：前置摄像头；false：后置摄像头。 |
| view        | UIView                                    | 承载视频画面的控件。                  |
| callback    | (_ code: Int, _ message: String?) -> Void | 操作回调。                            |


### stopCameraPreview

停止本地视频采集及预览。

```objc
/// 停止本地视频采集及预览
- (void)stopCameraPreview;

```


### startPublish

开始直播（推流），适用于以下场景：

- 主播开播的时候调用
- 观众开始连麦时调用


```objc
/// 开始直播（推流），适用于如下两种场景：
/// 1. 主播开播的时候调用
/// 2. 观众开始连麦时调用
/// - Parameters:
///   - streamID: 用于绑定直播 CDN 的 streamId，如果您希望您的观众通过直播 CDN 进行观看，需要指定当前主播的直播 streamId。
///   - callback: 操作回调
- (void)startPublishWithStreamID:(NSString *)streamID
                        callback:(Callback _Nullable)callback
NS_SWIFT_NAME(startPublish(streamID:callback:));
```

参数如下表所示：

| 参数     | 类型                                      | 含义                                                         |
| -------- | ----------------------------------------- | ------------------------------------------------------------ |
| streamID | String                                    | 用于绑定直播 CDN 的 streamID，如果您希望观众通过直播 CDN 进行观看，需要指定当前主播的直播 streamID。 |
| callback | (_ code: Int, _ message: String?) -> Void | 操作回调。                                                   |


### stopPublish

停止直播（推流），适用于以下场景：

- 主播结束直播时调用。
- 观众结束连麦时调用。

```objc
/// 停止直播（推流），适用于如下两种场景：
/// 1. 主播结束直播时调用
/// 2. 观众结束连麦时调用
/// - Parameter callback: 操作回调。
- (void)stopPublish:(Callback _Nullable)callback
NS_SWIFT_NAME(stopPublish(callback:));
```

参数如下表所示：

| 参数     | 类型                                      | 含义       |
| -------- | ----------------------------------------- | ---------- |
| callback | (_ code: Int, _ message: String?) -> Void | 操作回调。 |



### startPlay

播放远端视频画面，可以在普通观看和连麦场景中调用。

```objc
/// 播放远端视频画面，可以在普通观看和连麦场景中调用
/// 【普通观看场景】
/// 1. 如果您的服务器所管理的房间列表中包含每一个房间的主播 userID，则可以直接在 enterRoom() 成功后调用 startPlay(userID) 即可播放主播的画面。
/// 2. 如果您管理的房间列表只有 roomid 也没有关系，观众在 enterRoom() 成功后很快会收到来自 TRTCLiveRoomDelegate 中的 onAnchorEnter(userID) 回调。
/// 此时使用回调中的 userID 调用 startPlay(userID) 即可播放主播的画面。
/// 【直播连麦场景】
/// 发起连麦后，主播会收到来自 TRTCLiveRoomDelegate 中的 onAnchorEnter(userID) 回调，此时使用回调中的 userID 调用 startPlay(userID) 即可播放连麦画面。
/// - Parameters:
///   - userID: 需要观看的用户 ID。
///   - view: 承载视频画面的 view 控件。
///   - callback: 操作回调。
- (void)startPlayWithUserID:(NSString *)userID
                       view:(UIView *)view
                   callback:(Callback _Nullable)callback
NS_SWIFT_NAME(startPlay(userID:view:callback:));
```

参数如下表所示：

| 参数     | 类型                                      | 含义                       |
| -------- | ----------------------------------------- | -------------------------- |
| userID   | String                                    | 需要观看的用户 ID。        |
| view     | UIView                                    | 承载视频画面的 view 控件。 |
| callback | (_ code: Int, _ message: String?) -> Void | 操作回调。                 |


**普通观看场景**

- 若直播间列表已包含主播端的 userID 信息，观众端可以直接在 `enterRoom()` 成功后调用 `startPlay(userID)` 播放主播的画面。
- 若在进房前暂未获取主播的 userID，观众端在进房后会收到 `TRTCLiveRoomDelegate` 中的 `onAnchorEnter(userID)` 的事件回调，该回调中携带主播的 userID 信息，再调用`startPlay(userID)`即可播放主播的画面。

**直播连麦场景**
发起连麦后，主播会收到来自 `TRTCLiveRoomDelegate` 中的 `onAnchorEnter(userID)` 回调，此时使用回调中的 userID 调用 `startPlay(userID)` 即可播放连麦画面。



### stopPlay

停止渲染远端视频画面。需在 `onAnchorExit()` 回调时，调用该接口。

```objc
/// 停止渲染远端视频画面
/// - Parameters:
///   - userID: 对方的用户信息。
///   - callback: 操作回调。
/// - Note:
///   - 在 onAnchorExit 回调时，调用这个接口
- (void)stopPlayWithUserID:(NSString *)userID
                  callback:(Callback _Nullable)callback
NS_SWIFT_NAME(stopPlay(userID:callback:));
```

参数如下表所示：

| 参数     | 类型                                      | 含义             |
| -------- | ----------------------------------------- | ---------------- |
| userID   | String                                    | 对方的用户信息。 |
| callback | (_ code: Int, _ message: String?) -> Void | 操作回调。       |




## 主播和观众连麦

### requestJoinAnchor

观众请求连麦。

```objc
/// 观众端请求连麦
/// - Parameters:
///   - reason: 连麦请求原因。
///   - responseCallback: 请求连麦的回调。
/// - Note: 观众发起请求后，主播端会收到`onRequestJoinAnchor`回调
- (void)requestJoinAnchor:(NSString *)reason
                  timeout:(double)timeout
         responseCallback:(ResponseCallback _Nullable)responseCallback
NS_SWIFT_NAME(requestJoinAnchor(reason:timeout:responseCallback:));
```

参数如下表所示：

| 参数             | 类型                                        | 含义           |
| ---------------- | ------------------------------------------- | -------------- |
| reason           | String                                      | 连麦原因。     |
| timeout | long | 主播响应回调。 |
| responseCallback | (_ agreed: Bool, _ reason: String?) -> Void | 主播响应回调。 |

主播和观众的连麦流程如下：

1. 【观众】调用 `requestJoinAnchor()` 向主播发起连麦请求。
2. 【主播】会收到 `TRTCLiveRoomDelegate` 的 `onRequestJoinAnchor()` 回调通知。
3. 【主播】调用 `responseJoinAnchor()` 决定是否接受来自观众的连麦请求。
4. 【观众】会收到 responseCallback  回调通知，该通知会携带主播的处理结果。
5. 【观众】如果请求被同意，则调用 `startCameraPreview()` 开启本地摄像头。
6. 【观众】调用 `startPublish()` 正式进入推流状态。
7. 【主播】一旦观众进入连麦状态，主播会收到 `TRTCLiveRoomDelegate` 的 `onAnchorEnter()` 通知。
8. 【主播】主播调用 `startPlay()` 即可看到连麦观众的视频画面。
9. 【观众】如果直播间里已有其他观众正在跟主播连麦，新加入的连麦观众会收到 `onAnchorEnter()` 通知，调用 `startPlay()` 播放其他连麦者的视频画面。


### responseJoinAnchor

主播处理连麦请求。主播在收到 `TRTCLiveRoomDelegate` 的 `onRequestJoinAnchor()` 回调后，需要调用该接口来处理观众的连麦请求。

```objc
/// 主播回复观众连麦请求
/// - Parameters:
///   - user: 观众 ID。
///   - agree: true：同意；false：拒绝。
///   - reason: 同意/拒绝连麦的原因描述。
/// - Note: 主播回复后，观众端会收到`requestJoinAnchor`传入的`responseCallback`回调
- (void)responseJoinAnchor:(NSString *)userID
                     agree:(BOOL)agree
                    reason:(NSString *)reason
NS_SWIFT_NAME(responseJoinAnchor(userID:agree:reason:));
```

参数如下表所示：

| 参数   | 类型    | 含义                      |
| ------ | ------- | ------------------------- |
| userID | String  | 观众 ID。                 |
| agree  | Bool    | true：同意；false：拒绝。 |
| reason | String? | 同意/拒绝连麦的原因描述。 |


### kickoutJoinAnchor

主播踢除连麦观众。主播调用此接口踢除连麦观众后，被踢连麦观众会收到 `TRTCLiveRoomDelegate` 的 `onKickoutJoinAnchor()` 回调通知。

```objc
/// 主播踢除连麦观众
/// - Parameters:
///   - userID: 连麦观众 ID。
///   - callback: 操作回调。
/// - Note: 主播调用此接口踢除连麦观众后，被踢连麦观众会收到 trtcLiveRoomOnKickoutJoinAnchor() 回调通知
- (void)kickoutJoinAnchor:(NSString *)userID
                 callback:(Callback _Nullable)callback
NS_SWIFT_NAME(kickoutJoinAnchor(userID:callback:));
```

参数如下表所示：

| 参数     | 类型                                      | 含义          |
| -------- | ----------------------------------------- | ------------- |
| userID   | String                                    | 连麦观众 ID。 |
| callback | (_ code: Int, _ message: String?) -> Void | 操作回调。    |



## 主播跨房间 PK

### requestRoomPK

主播请求跨房 PK。

```objc
/// 主播请求跨房 PK
/// - Parameters:
///   - roomID: 被邀约房间 ID。
///   - userID: 被邀约主播 ID。
///   - responseCallback: 请求跨房 PK 的结果回调。
/// - Note: 发起请求后，对方主播会收到 `onRequestRoomPK` 回调
- (void)requestRoomPKWithRoomID:(UInt32)roomID
                         userID:(NSString *)userID
               responseCallback:(ResponseCallback _Nullable)responseCallback
NS_SWIFT_NAME(requestRoomPK(roomID:userID:responseCallback:));
```

参数如下表所示：

| 参数             | 类型                                        | 含义                     |
| ---------------- | ------------------------------------------- | ------------------------ |
| roomID           | UInt32                                      | 被邀约房间 ID。          |
| userID           | String                                      | 被邀约主播 ID。          |
| responseCallback | (_ agreed: Bool, _ reason: String?) -> Void | 请求跨房 PK 的结果回调。 |

主播和主播之间可以跨房间 PK，两个正在直播中的主播 A 和 B 之间的跨房 PK 流程如下：

1. 【主播 A】调用 `requestRoomPK()` 向主播 B 发起连麦请求。
2. 【主播 B】会收到 `TRTCLiveRoomDelegate` 的 `onRequestRoomPK()` 回调通知。
3. 【主播 B】调用 `responseRoomPK()` 决定是否接受主播 A 的 PK 请求。
4. 【主播 B】如果接受主播 A 的请求，等待 `TRTCLiveRoomDelegate` 的 `onAnchorEnter()` 通知，然后调用 `startPlay()` 来显示主播 A 的视频画面。
5. 【主播 A】会收到 `responseCallback` 回调通知，该通知会携带来自主播 B 的处理结果。
6. 【主播 A】如果请求被同意，等待 `TRTCLiveRoomDelegate` 的 `onAnchorEnter()` 通知，然后调用 `startPlay()` 显示主播 B 的视频画面。


### responseRoomPK

主播响应跨房 PK 请求。主播响应后，对方主播会收到 `requestRoomPK` 传入的 `responseCallback` 回调。

```objc
/// 响应跨房 PK 请求
/// 主播响应其他房间主播的 PK 请求。
/// - Parameters:
///   - user: 发起 PK 请求的主播 ID
///   - agree: true：同意；false：拒绝
///   - reason: 同意/拒绝 PK 的原因描述
/// - Note: 主播回复后，对方主播会收到 `requestRoomPK` 传入的 `responseCallback` 回调
- (void)responseRoomPKWithUserID:(NSString *)userID
                           agree:(BOOL)agree
                          reason:(NSString *)reason
NS_SWIFT_NAME(responseRoomPK(userID:agree:reason:));
```

参数如下表所示：

| 参数   | 类型    | 含义                      |
| ------ | ------- | ------------------------- |
| userID | String  | 发起 PK 请求的主播 ID。   |
| agree  | Bool    | true：同意；false：拒绝。 |
| reason | String? | 同意/拒绝 PK 的原因描述。 |


### quitRoomPK

退出跨房 PK。PK 中的任何一个主播退出跨房 PK 状态后，另一个主播会收到 `TRTCLiveRoomDelegate` 的 `trtcLiveRoomOnQuitRoomPK()` 回调通知。

```objc
/// 主播退出跨房 PK
/// - Parameter callback: 退出跨房 PK 的结果回调
/// - Note: 当两个主播中的任何一个退出跨房 PK 状态后，另一个主播会收到 `trtcLiveRoomOnQuitRoomPK` 回调通知。
- (void)quitRoomPK:(Callback _Nullable)callback
NS_SWIFT_NAME(quitRoomPK(callback:));
```

参数如下表所示：

| 参数     | 类型                                      | 含义       |
| -------- | ----------------------------------------- | ---------- |
| callback | (_ code: Int, _ message: String?) -> Void | 操作回调。 |


## 音视频控制相关接口函数

### switchCamera

切换前后摄像头。

```objc
/// 切换前后摄像头
- (void)switchCamera;
```


### setMirror

设置是否镜像展示。

```objc
/// 设置是否镜像展示
/// - Parameter isMirror: 开启/关闭镜像。
- (void)setMirror:(BOOL)isMirror
NS_SWIFT_NAME(setMirror(isMirror:));
```

参数如下表所示：

| 参数     | 类型 | 含义            |
| -------- | ---- | --------------- |
| isMirror | Bool | 开启/关闭镜像。 |


### muteLocalAudio

静音本地音频。

```objc
/// 静音本地音频。
/// - Parameter isMuted: true：开启静音；false：关闭静音。
- (void)muteLocalAudio:(BOOL)isMuted
NS_SWIFT_NAME(muteLocalAudio(isMuted:));
```

参数如下表所示：

| 参数    | 类型 | 含义                              |
| ------- | ---- | --------------------------------- |
| isMuted | Bool | true：开启静音；false：关闭静音。 |

### muteRemoteAudio

静音远端音频。

```objc
/// 静音远端音频
/// - Parameters:
///   - userID: 远端的用户ID。
///   - isMuted: true：开启静音；false：关闭静音。
- (void)muteRemoteAudioWithUserID:(NSString *)userID isMuted:(BOOL)isMuted
NS_SWIFT_NAME(muteRemoteAudio(userID:isMuted:));
```

参数如下表所示：

| 参数    | 类型   | 含义                              |
| ------- | ------ | --------------------------------- |
| userID  | String | 远端的用户 ID。                   |
| isMuted | Bool   | true：开启静音；false：关闭静音。 |



### muteAllRemoteAudio

静音所有远端音频。

```objc
/// 静音所有远端音频
/// - Parameter isMuted: true：开启静音；false：关闭静音。
- (void)muteAllRemoteAudio:(BOOL)isMuted
NS_SWIFT_NAME(muteAllRemoteAudio(_:));
```

参数如下表所示：

| 参数    | 类型 | 含义                              |
| ------- | ---- | --------------------------------- |
| isMuted | Bool | true：开启静音；false：关闭静音。 |

### setAudioQuality

设置音频质量

```objc
/// 设置音频质量，支持的值为1 2 3，代表低中高
/// - Parameter quality 音频质量
- (void)setAudioQuality:(NSInteger)quality
NS_SWIFT_NAME(setAudioiQuality(quality:));
```

参数如下表所示：

| 参数    | 类型      | 含义                         |
| ------- | --------- | ---------------------------- |
| quality | NSInteger | 1：语音；2：标准； 3：音乐。 |

## 背景音乐音效相关接口函数

### getAudioEffectManager

获取背景音乐音效管理对象 [TXAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af962213fefe6988a08820ac9af00df66)。

```objc
/// 获取音效管理对象
- (TXAudioEffectManager *)getAudioEffectManager;
```

## 美颜滤镜相关接口函数

### getBeautyManager

获取美颜管理对象 [TXBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXBeautyManager__ios.html#interfaceTXBeautyManager)。

```objc
/* 获取美颜管理对象 TXBeautyManager
*
* 通过美颜管理，您可以使用以下功能：
* - 设置"美颜风格"、“美白”、“红润”、“大眼”、“瘦脸”、“V脸”、“下巴”、“短脸”、“小鼻”、“亮眼”、“白牙”、“祛眼袋”、“祛皱纹”、“祛法令纹”等美容效果。
* - 调整“发际线”、“眼间距”、“眼角”、“嘴形”、“鼻翼”、“鼻子位置”、“嘴唇厚度”、“脸型”
* - 设置人脸挂件（素材）等动态效果
* - 添加美妆
* - 进行手势识别
*/
- (TXBeautyManager *)getBeautyManager;
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

```objc
/// 发送文本消息，房间内所有成员都可见
/// - Parameters:
///   - message: 文本消息。
///   - callback: 发送回调。
- (void)sendRoomTextMsg:(NSString *)message callback:(Callback _Nullable)callback
NS_SWIFT_NAME(sendRoomTextMsg(message:callback:));
```

参数如下表所示：

| 参数     | 类型                                      | 含义           |
| -------- | ----------------------------------------- | -------------- |
| message  | String                                    | 文本消息。     |
| callback | (_ code: Int, _ message: String?) -> Void | 发送结果回调。 |


### sendRoomCustomMsg

发送自定义文本消息。

```objc
/// 发送自定义消息
/// - Parameters:
///   - command: 命令字，由开发者自定义，主要用于区分不同消息类型
///   - message: 本文消息。
///   - callback: 发送回调。
- (void)sendRoomCustomMsgWithCommand:(NSString *)command message:(NSString *)message callback:(Callback _Nullable)callback
NS_SWIFT_NAME(sendRoomCustomMsg(command:message:callback:));
```

参数如下表所示：

| 参数     | 类型                                      | 含义                                               |
| -------- | ----------------------------------------- | -------------------------------------------------- |
| command  | String                                    | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message  | String                                    | 文本消息。                                         |
| callback | (_ code: Int, _ message: String?) -> Void | 发送结果回调。                                     |


## 调试相关接口函数

### showVideoDebugLog

是否在界面中展示 debug 信息。

```objc
/// 是否在界面中展示debug信息
/// - Parameter isShow: 开启/关闭 Debug 信息显示。
- (void)showVideoDebugLog:(BOOL)isShow
NS_SWIFT_NAME(showVideoDebugLog(_:));
```

参数如下表所示：

| 参数   | 类型 | 含义                       |
| ------ | ---- | -------------------------- |
| isShow | Bool | 开启/关闭 Debug 信息显示。 |


## TRTCLiveRoomDelegate事件回调

## 通用事件回调

### onError

错误回调。

>?SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```objc
- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom
             onError:(NSInteger)code
             message:(NSString  *)message
NS_SWIFT_NAME(trtcLiveRoom(_:onError:message:));
```

参数如下表所示：

| 参数         | 类型             | 含义                         |
| ------------ | ---------------- | ---------------------------- |
| trtcLiveRoom | TRTCLiveRoomImpl | 当前 TRTCLiveRoom 组件实例。 |
| code         | Int              | 错误码。                     |
| message      | String?          | 错误信息。                   |


### onWarning

警告回调。

```objc
- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom
           onWarning:(NSInteger)code
             message:(NSString *)message
NS_SWIFT_NAME(trtcLiveRoom(_:onWarning:message:));
```

参数如下表所示：

| 参数         | 类型             | 含义                         |
| ------------ | ---------------- | ---------------------------- |
| trtcLiveRoom | TRTCLiveRoomImpl | 当前 TRTCLiveRoom 组件实例。 |
| code         | Int              | 错误码 TRTCWarningCode。     |
| message      | String?          | 警告信息。                   |



### onDebugLog

Log 回调。

```objc
- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom
          onDebugLog:(NSString *)log
NS_SWIFT_NAME(trtcLiveRoom(_:onDebugLog:));
```

参数如下表所示：

| 参数         | 类型             | 含义                         |
| ------------ | ---------------- | ---------------------------- |
| trtcLiveRoom | TRTCLiveRoomImpl | 当前 TRTCLiveRoom 组件实例。 |
| log          | String           | 日志信息。                   |


## 房间事件回调

### onRoomDestroy

房间被销毁的回调。主播退房时，房间内的所有用户都会收到此通知。

```objc
- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom
       onRoomDestroy:(NSString *)roomID
NS_SWIFT_NAME(trtcLiveRoom(_:onRoomDestroy:));
```

参数如下表所示：

| 参数         | 类型             | 含义                         |
| ------------ | ---------------- | ---------------------------- |
| trtcLiveRoom | TRTCLiveRoomImpl | 当前 TRTCLiveRoom 组件实例。 |
| roomID       | String           | 房间 ID。                    |


### onRoomInfoChange

直播房间信息变更回调。多用于直播连麦、PK下房间状态变化通知场景。

```objc
- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom
    onRoomInfoChange:(TRTCLiveRoomInfo *)info
NS_SWIFT_NAME(trtcLiveRoom(_:onRoomInfoChange:));
```

参数如下表所示：

| 参数         | 类型             | 含义                         |
| ------------ | ---------------- | ---------------------------- |
| trtcLiveRoom | TRTCLiveRoomImpl | 当前 TRTCLiveRoom 组件实例。 |
| info         | TRTCLiveRoomInfo | 房间信息。                   |




## 主播和观众进出事件回调

### onAnchorEnter

收到新主播进房通知。连麦观众和跨房 PK 主播进房后观众会收到新主播的进房事件，您可以调用 `TRTCLiveRoom` 的 `startPlay()` 显示该主播的视频画面。

```objc
- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom
       onAnchorEnter:(NSString *)userID
NS_SWIFT_NAME(trtcLiveRoom(_:onAnchorEnter:));
```

参数如下表所示：

| 参数         | 类型             | 含义                         |
| ------------ | ---------------- | ---------------------------- |
| trtcLiveRoom | TRTCLiveRoomImpl | 当前 TRTCLiveRoom 组件实例。 |
| userID       | String           | 新进房用户 ID。              |



### onAnchorExit

收到主播退房通知。房间内的主播（和连麦中的观众）会收到新主播的退房事件，您可以调用 `TRTCLiveRoom` 的 `stopPlay()` 关闭该主播的视频画面。

```objc
- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom
        onAnchorExit:(NSString *)userID
NS_SWIFT_NAME(trtcLiveRoom(_:onAnchorExit:));
```

参数如下表所示：

| 参数         | 类型             | 含义                         |
| ------------ | ---------------- | ---------------------------- |
| trtcLiveRoom | TRTCLiveRoomImpl | 当前 TRTCLiveRoom 组件实例。 |
| userID       | String           | 退房用户 ID。                |



### onAudienceEnter

收到观众进房通知。

```objc
- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom
     onAudienceEnter:(TRTCLiveUserInfo *)user
NS_SWIFT_NAME(trtcLiveRoom(_:onAudienceEnter:));
```

参数如下表所示：

| 参数         | 类型             | 含义                         |
| ------------ | ---------------- | ---------------------------- |
| trtcLiveRoom | TRTCLiveRoomImpl | 当前 TRTCLiveRoom 组件实例。 |
| user         | TRTCLiveUserInfo | 进房观众信息。               |


### onAudienceExit

收到观众退房通知。

```objc
- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom
      onAudienceExit:(TRTCLiveUserInfo *)user
NS_SWIFT_NAME(trtcLiveRoom(_:onAudienceExit:));
```

参数如下表所示：

| 参数         | 类型             | 含义                         |
| ------------ | ---------------- | ---------------------------- |
| trtcLiveRoom | TRTCLiveRoomImpl | 当前 TRTCLiveRoom 组件实例。 |
| user         | TRTCLiveUserInfo | 退房观众信息。               |


## 主播和观众连麦事件回调

### onRequestJoinAnchor

主播收到观众连麦请求时的回调。

```objc
- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom
 onRequestJoinAnchor:(TRTCLiveUserInfo *)user
             reason:(NSString * _Nullable)reason
             timeout:(double)timeout
NS_SWIFT_NAME(trtcLiveRoom(_:onRequestJoinAnchor:reason:timeout:));
```

参数如下表所示：

| 参数         | 类型             | 含义                         |
| ------------ | ---------------- | ---------------------------- |
| trtcLiveRoom | TRTCLiveRoomImpl | 当前 TRTCLiveRoom 组件实例。 |
| user         | TRTCLiveUserInfo | 请求连麦观众信息。           |
| reason       | String?          | 连麦原因描述。               |
| timeout      | Double           | 处理请求的超时时间。         |


### onKickoutJoinAnchor

连麦观众收到被踢出连麦的通知。连麦观众收到被主播踢除连麦的消息，您需要调用 `TRTCLiveRoom` 的 `stopPublish()` 退出连麦。

```objc
- (void)trtcLiveRoomOnKickoutJoinAnchor:(TRTCLiveRoom *)liveRoom
NS_SWIFT_NAME(trtcLiveRoomOnKickoutJoinAnchor(_:));
```

参数如下表所示：

| 参数         | 类型             | 含义                         |
| ------------ | ---------------- | ---------------------------- |
| trtcLiveRoom | TRTCLiveRoomImpl | 当前 TRTCLiveRoom 组件实例。 |



## 主播 PK 事件回调

### onRequestRoomPK

收到请求跨房 PK 通知。主播收到其他房间主播的 PK 请求，如果同意 PK ，您需要等待 `TRTCLiveRoomDelegate` 的 `onAnchorEnter()` 通知，然后调用 `startPlay()` 来播放邀约主播的流。

```objc
- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom
     onRequestRoomPK:(TRTCLiveUserInfo *)user
             timeout:(double)timeout
NS_SWIFT_NAME(trtcLiveRoom(_:onRequestRoomPK:timeout:));
```

参数如下表所示：

| 参数         | 类型             | 含义                         |
| ------------ | ---------------- | ---------------------------- |
| trtcLiveRoom | TRTCLiveRoomImpl | 当前 TRTCLiveRoom 组件实例。 |
| user         | TRTCLiveUserInfo | 发起跨房连麦的主播信息。     |
| timeout      | Double           | 处理请求的超时时间。         |


### onQuitRoomPK

收到断开跨房 PK 通知。

```objc
 - (void)trtcLiveRoomOnQuitRoomPK:(TRTCLiveRoom *)liveRoom
NS_SWIFT_NAME(trtcLiveRoomOnQuitRoomPK(_:));
```

参数如下表所示：

| 参数         | 类型             | 含义                         |
| ------------ | ---------------- | ---------------------------- |
| trtcLiveRoom | TRTCLiveRoomImpl | 当前 TRTCLiveRoom 组件实例。 |



## 消息事件回调

### onRecvRoomTextMsg

收到文本消息。

```objc
- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom
   onRecvRoomTextMsg:(NSString *)message
            fromUser:(TRTCLiveUserInfo *)user
NS_SWIFT_NAME(trtcLiveRoom(_:onRecvRoomTextMsg:fromUser:));
```

参数如下表所示：

| 参数         | 类型             | 含义                         |
| ------------ | ---------------- | ---------------------------- |
| trtcLiveRoom | TRTCLiveRoomImpl | 当前 TRTCLiveRoom 组件实例。 |
| message      | String           | 文本消息。                   |
| user         | TRTCLiveUserInfo | 发送者用户信息。             |



### onRecvRoomCustomMsg

收到自定义消息。

```objc
- (void)trtcLiveRoom:(TRTCLiveRoom *)trtcLiveRoom
onRecvRoomCustomMsgWithCommand:(NSString *)command
             message:(NSString *)message
            fromUser:(TRTCLiveUserInfo *)user
NS_SWIFT_NAME(trtcLiveRoom(_:onRecvRoomCustomMsg:message:fromUser:));
```

参数如下表所示：

| 参数         | 类型             | 含义                                               |
| ------------ | ---------------- | -------------------------------------------------- |
| trtcLiveRoom | TRTCLiveRoomImpl | 当前 TRTCLiveRoom 组件实例。                       |
| command      | String           | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message      | String           | 文本消息。                                         |
| user         | TRTCLiveUserInfo | 发送者用户信息。                                   |

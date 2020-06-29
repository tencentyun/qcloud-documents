**功能**

腾讯云移动直播 - 连麦直播间。

>! 后台接口限制并发为每秒100次请求，若您有高并发请求请提前 [联系我们](https://cloud.tencent.com/act/event/connect-service) 处理，避免影响服务调用。

**介绍**

基于腾讯云直播（LVB）、点播（VOD） 和即时通信（IM）三大 PAAS 服务组合而成，支持：

- 主播创建新的直播间开播，观众进入直播间观看。
- 主播和观众进行视频连麦互动。
- 两个不同房间的主播 PK 互动。
- 每一个直播间都有一个不限制房间人数的聊天室，支持发送各种文本消息和自定义消息，自定义消息可用于实现弹幕、点赞和礼物。

连麦直播间（MLVBLiveRoom）是一个开源的 Class，依赖两个腾讯云的闭源 SDK：

- LiteAVSDK：使用了其中的 [TXLivePusher]( https://cloud.tencent.com/document/product/454/34753?!editLang=zh&!preview#TXLivePusher) 和 [TXLivePlayer](https://cloud.tencent.com/document/product/454/34753?!editLang=zh&!preview#TXLivePlayer) 两个组件，前者用于推流，后者用于拉流。
- IM SDK：使用 IM SDK 的 AVChatroom 用于实现直播聊天室的功能，同时，主播间的连麦流程也是依靠 IM 消息串联起来的。

请参见 [直播连麦（LiveRoom）](https://cloud.tencent.com/document/product/454/14606)。

## MLVBLiveRoom  API 概览

### SDK 基础函数

| API                                             | 描述                        |
| ----------------------------------------------- | --------------------------- |
| [delegate](#delegate)                           | MLVBLiveRoom 事件回调       |
| [delegateQueue](#delegateQueue)                 | 设置驱动回调函数的 GCD 队列 |
| [sharedInstance](#sharedInstance)               | 获取 MLVBLiveRoom 单例对象  |
| [destorySharedInstance](#destorySharedInstance) | 销毁 MLVBLiveRoom 单例对象  |
| [loginWithInfo](#loginWithInfo)                 | 登录                        |
| [logout](#logout)                               | 登出                        |
| [setSelfProfile](#setSelfProfile)               | 修改个人信息                |

### 房间相关接口函数

| API                                 | 描述                       |
| ----------------------------------- | -------------------------- |
| [getRoomList](#getRoomList)         | 获取房间列表               |
| [getAudienceList](#getAudienceList) | 获取观众列表               |
| [createRoom](#createRoom)           | 创建房间（主播调用）       |
| [enterRoom](#enterRoom)             | 进入房间（观众调用）       |
| [exitRoom](#exitRoom)               | 离开房间                   |
| [setCustomInfo](#setCustomInfo)     | 设置当前房间的扩展信息字段 |
| [getCustomInfo](#getCustomInfo)     | 获取当前房间的扩展信息字段 |

### 主播和观众连麦

| API                                       | 描述             |
| ----------------------------------------- | ---------------- |
| [requestJoinAnchor](#requestJoinAnchor)   | 观众请求连麦     |
| [responseJoinAnchor](#responseJoinAnchor) | 主播处理连麦请求 |
| [joinAnchor](#joinAnchor)                 | 进入连麦状态     |
| [quitJoinAnchor](#quitJoinAnchor)         | 观众退出连麦     |
| [kickoutJoinAnchor](#kickoutJoinAnchor)   | 主播踢除连麦观众 |

### 主播跨房间 PK

| API                               | 描述             |
| --------------------------------- | ---------------- |
| [requestRoomPK](#requestRoomPK)   | 请求跨房 PK      |
| [responseRoomPK](#responseRoomPK) | 响应跨房 PK 请求 |
| [quitRoomPK](#quitRoomPK)         | 退出跨房 PK      |

### 视频相关接口函数

| API                                     | 描述                   |
| --------------------------------------- | ---------------------- |
| [startLocalPreview](#startLocalPreview) | 开启本地视频的预览画面 |
| [stopLocalPreview](#stopLocalPreview)   | 停止本地视频采集及预览 |
| [startRemoteView](#startRemoteView)     | 启动渲染远端视频画面   |
| [stopRemoteView](#stopRemoteView)       | 停止渲染远端视频画面   |
| [setMirror](#setMirror)                 | 设置观众端镜像效果     |

### 音频相关接口函数

| API                                       | 描述                     |
| ----------------------------------------- | ------------------------ |
| [muteLocalAudio](#muteLocalAudio)         | 是否屏蔽本地音频         |
| [muteRemoteAudio](#muteRemoteAudio)       | 设置指定用户是否静音     |
| [muteAllRemoteAudio](#muteAllRemoteAudio) | 设置所有远端用户是否静音 |

### 摄像头相关接口函数

| API                                       | 描述                                 |
| ----------------------------------------- | ------------------------------------ |
| [switchCamera](#switchCamera)             | 切换前后摄像头                       |
| [setCameraMuteImage](#setCameraMuteImage) | 主播屏蔽摄像头期间需要显示的等待图片 |
| [setZoom](#setZoom)                       | 调整焦距                             |
| [enableTorch](#enableTorch)               | 打开闪光灯                           |
| [setFocusPosition](#setFocusPosition)     | 设置手动对焦区域                     |

### 美颜滤镜相关接口函数

| API                                       | 描述                                                         |
| ----------------------------------------- | ------------------------------------------------------------ |
| [getBeautyManager](#getBeautyManager)     | 获取美颜管理对象 [TXBeautyManager](https://cloud.tencent.com/document/product/454/34753?!editLang=zh&!preview#TXBeautyManager) |
| [setBeautyStyle](#setBeautyStyle)         | 设置美颜、美白、红润效果级别                                 |
| [setFilter](#setFilter)                   | 设置指定素材滤镜特效                                         |
| [setSpecialRatio](#setSpecialRatio)       | 设置滤镜浓度                                                 |
| [setEyeScaleLevel](#setEyeScaleLevel)     | 设置大眼级别（仅企业版有效）                                 |
| [setFaceScaleLevel](#setFaceScaleLevel)   | 设置瘦脸级别（仅企业版有效）                                 |
| [setFaceVLevel](#setFaceVLevel)           | 设置 V 脸级别（仅企业版有效）                                |
| [setChinLevel](#setChinLevel)             | 设置下巴拉伸或收缩（仅企业版有效）                           |
| [setFaceShortLevel](#setFaceShortLevel)   | 设置短脸级别（仅企业版有效）                                 |
| [setNoseSlimLevel](#setNoseSlimLevel)     | 设置瘦鼻级别（仅企业版有效）                                 |
| [setGreenScreenFile](#setGreenScreenFile) | 设置绿幕背景视频（仅企业版有效）                             |
| [selectMotionTmpl](#selectMotionTmpl)     | 选择使用哪一款 AI 动效挂件（仅企业版有效）                   |

 ###  消息发送接口函数

| API                                     | 描述               |
| --------------------------------------- | ------------------ |
| [sendRoomTextMsg](#sendRoomTextMsg)     | 发送文本消息       |
| [sendRoomCustomMsg](#sendRoomCustomMsg) | 发送自定义文本消息 |

### 背景混音相关接口函数

| API                                         | 描述                   |
| ------------------------------------------- | ---------------------- |
| [playBGM](#playBGM)                         | 播放背景音乐           |
| [playBGM](#playBGM)                         | 播放背景音乐           |
| [stopBGM](#stopBGM)                         | 停止播放背景音乐       |
| [pauseBGM](#pauseBGM)                       | 暂停播放背景音乐       |
| [resumeBGM](#resumeBGM)                     | 继续播放背景音乐       |
| [getMusicDuration](#getMusicDuration)       | 获取音乐文件总时长     |
| [setMicVolume](#setMicVolume)               | 设置麦克风的音量大小   |
| [setBGMVolume](#setBGMVolume)               | 设置背景音乐的音量大小 |
| [setBGMPitch](#setBGMPitch)                 | 调整背景音乐的音调高低 |
| [setBGMPosition](#setBGMPosition)           | 调整背景音乐的音调高低 |
| [setReverbType](#setReverbType)             | 设置混响效果           |
| [setVoiceChangerType](#setVoiceChangerType) | 设置变声类型           |

### 背景混音相关接口函数

| API                                     | 描述                                               |
| --------------------------------------- | -------------------------------------------------- |
| [showVideoDebugLog](#showVideoDebugLog) | 在渲染 view 上显示播放或推流状态统计及事件消息浮层 |



## SDK 基础函数

<h3 id="delegate">delegate</h3>

MLVBLiveRoom 事件回调，您可以通过 [MLVBLiveRoomDelegate](https://cloud.tencent.com/document/product/454/34764?!editLang=zh&!preview) 获得 MLVBLiveRoom 的各种状态通知。

```
@property (nonatomic, weak) id< MLVBLiveRoomDelegate > delegate
```

>? 默认是在 Main Queue 中回调，如果需要自定义回调线程，可使用 delegateQueue。

------

<h3 id="delegateQueue">delegateQueue</h3>

设置驱动回调函数的 GCD 队列。

```
@property (nonatomic, copy) dispatch_queue_t delegateQueue
```

------

<h3 id="sharedInstance">sharedInstance</h3>

获取 MLVBLiveRoom 单例对象。

```
+ (instancetype)sharedInstance
```

**返回**

MLVBLiveRoom 实例。

>? 可以调用 [destroySharedInstance](#destorySharedInstance) 销毁单例对象。

------

<h3 id="destorySharedInstance">destorySharedInstance</h3>

销毁 MLVBLiveRoom 单例对象。

```
+ (void)destorySharedInstance
```

>? 销毁实例后，外部缓存的 MLVBLiveRoom 实例不能再使用，需要重新调用 [sharedInstance](#sharedInstance) 获取新实例。

------

<h3 id="loginWithInfo">loginWithInfo</h3>

登录。

```
- (void)loginWithInfo:(MLVBLoginInfo *)loginInfo completion:(void(^)(int errCode, NSString *errMsg))completion 
```

**参数**

| 参数       | 类型                                   | 含义           |
| :--------- | :------------------------------------- | :------------- |
| loginInfo  | MLVBLoginInfo *                        | 登录信息。     |
| completion | void(^)(int errCode, NSString *errMsg) | 登录结果回调。 |

------

<h3 id="logout">logout</h3>

登出。

```
- (void)logout
```

------

<h3 id="setSelfProfile">setSelfProfile</h3>

修改个人信息。

```
- (void)setSelfProfile:(NSString *)userName avatarURL:(NSString *)avatarURL completion:(void(^)(int code, NSString *msg))completion 
```

**参数**

| 参数      | 类型       | 含义       |
| :-------- | :--------- | :--------- |
| userName  | NSString * | 昵称。     |
| avatarURL | NSString * | 头像地址。 |

------

## 房间相关接口函数

<h3 id="getRoomList">getRoomList</h3>

获取房间列表。

```
- (void)getRoomList:(int)index count:(int)count completion:(void(^)(int errCode, NSString *errMsg, NSArray< MLVBRoomInfo * > *roomInfoArray))completion 
```

**参数**

| 参数       | 类型                                                         | 含义                        |
| :--------- | :----------------------------------------------------------- | :-------------------------- |
| index      | int                                                          | 房间开始索引，从0开始计算。 |
| count      | int                                                          | 希望后台返回的房间个数。    |
| completion | void(^)(int errCode, NSString *errMsg, NSArray< MLVBRoomInfo * > *roomInfoArray) | 获取房间列表的结果回调。    |

**介绍**

该接口支持分页获取房间列表，可以用 index 和 count 两个参数控制列表分页的逻辑，

- index = 0 & count = 10代表获取第一页的10个房间。
- index = 11 & count = 10代表获取第二页的10个房间。

------

<h3 id="getAudienceList">getAudienceList</h3>

获取观众列表。

```
- (void)getAudienceList:(NSString *)roomID completion:(void(^)(int errCode, NSString *errMsg, NSArray< MLVBAudienceInfo * > *audienceInfoArray))completion 

```

**参数**

| 参数       | 类型                                                         | 含义                     |
| :--------- | :----------------------------------------------------------- | :----------------------- |
| roomID     | NSString *                                                   | 房间标识。               |
| completion | void(^)(int errCode, NSString *errMsg, NSArray< MLVBAudienceInfo * > *audienceInfoArray) | 获取观众列表的结果回调。 |

**介绍**

当有观众进房时，后台会将其信息加入到指定房间的观众列表中，调入该函数即可返回指定房间的观众列表。

>? 观众列表最多只保存30人，因为对于常规的 UI 展示来说这已经足够，保存更多除了浪费存储空间，也会拖慢列表返回的速度。

------

<h3 id="createRoom">createRoom</h3>

创建房间（主播调用）。

```
- (void)createRoom:(NSString *)roomID roomInfo:(NSString *)roomInfo completion:(void(^)(int errCode, NSString *errMsg))completion 

```

**参数**

| 参数       | 类型                                   | 含义                                                         |
| :--------- | :------------------------------------- | :----------------------------------------------------------- |
| roomID     | NSString *                             | 房间标识，推荐做法是用主播的 userID 作为房间的 roomID，这样省去了后台映射的成本。room ID 可以填空，此时由后台生成。 |
| roomInfo   | NSString *                             | 房间信息（非必填），用于房间描述的信息，如房间名称，允许使用 JSON 格式作为房间信息。 |
| completion | void(^)(int errCode, NSString *errMsg) | 创建房间的结果回调。                                         |

**介绍**

主播开播的正常调用流程是：

1. 主播调用 [startLocalPreview](#startLocalPreview) 打开摄像头预览，此时可以调整美颜参数。
2. 主播调用 createRoom 创建直播间，房间创建成功与否会通过 completion 通知主播。

------

<h3 id="enterRoom">enterRoom</h3>

进入房间（观众调用）。

```
- (void)enterRoom:(NSString *)roomID view:(UIView *)view completion:(void(^)(int errCode, NSString *errMsg))completion 


```

**参数**

| 参数       | 类型                                   | 含义                 |
| :--------- | :------------------------------------- | :------------------- |
| roomID     | NSString *                             | 房间标识。           |
| view       | UIView *                               | 承载视频画面的控件。 |
| completion | void(^)(int errCode, NSString *errMsg) | 进入房间的结果回调。 |

**介绍**

观众观看直播的正常调用流程是：

1. 观众调用 [getRoomList](#getRoomList) 刷新最新的直播房间列表，并通过 completion 回调拿到房间列表。
2. 观众选择一个直播间以后，调用 enterRoom 进入该房间。

------

<h3 id="exitRoom">exitRoom</h3>

离开房间。

```
- (void)exitRoom:(void(^)(int errCode, NSString *errMsg))completion 


```

**参数**

| 参数       | 类型                                   | 含义                 |
| :--------- | :------------------------------------- | :------------------- |
| completion | void(^)(int errCode, NSString *errMsg) | 离开房间的结果回调。 |

------

<h3 id="setCustomInfo">setCustomInfo</h3>

设置当前房间的扩展信息字段。

```
- (void)setCustomInfo:(MLVBCustomFieldOp)op key:(NSString *)key value:(id)value completion:(void(^)(int errCode, NSString *custom))completion 


```

**参数**

| 参数       | 类型                                   | 含义                                |
| :--------- | :------------------------------------- | :---------------------------------- |
| op         | MLVBCustomFieldOp                      | 执行动作。                          |
| key        | NSString *                             | 自定义键。                          |
| value      | id                                     | 可选类型为 NSNumber 或者 NSString。 |
| completion | void(^)(int errCode, NSString *custom) | 操作完成的回调。                    |

**介绍**

有时候您需要为当前房间设置一些扩展字段，如“点赞人数”和“是否正在连麦”等，这些字段我们很难全都预先定义好，所以提供了如下三种操作接口：

- SET：设置，value 可以是数值或者字符串，例如“是否正在连麦”等。
- INC：增加，value 只能是整数，如“点赞人数”，“人气指数”等，都可以使用该操作接口。
- DEC：减少，value 只能是整数，如“点赞人数”，“人气指数”等，都可以使用该操作接口。

>? op 为 MLVBCustomFieldOpSet 或者 MLVBCustomFieldOpDec 时，value 需要是一个数字。

------

<h3 id="getCustomInfo">getCustomInfo</h3>

获取当前房间的扩展信息字段。

```
- (void)getCustomInfo:(void(^)(int errCode, NSString *errMsg, NSDictionary *customInfo))completion 

```

**参数**

| 参数       | 类型                                                         | 含义               |
| :--------- | :----------------------------------------------------------- | :----------------- |
| completion | void(^)(int errCode, NSString *errMsg, NSDictionary *customInfo) | 获取自定义值回调。 |

------

## 主播和观众连麦

<h3 id="requestJoinAnchor">requestJoinAnchor</h3>

观众请求连麦。

```
- (void)requestJoinAnchor:(NSString *)reason completion:(void(^)(int errCode, NSString *errMsg))completion 

```

**参数**

| 参数       | 类型                                   | 含义           |
| :--------- | :------------------------------------- | :------------- |
| reason     | NSString *                             | 连麦原因。     |
| completion | void(^)(int errCode, NSString *errMsg) | 主播响应回调。 |

**介绍**

主播和观众的连麦流程可以简单描述为如下几个步骤：

1. 观众调用 [requestJoinAnchor](#requestJoinAnchor ) 向主播发起连麦请求。
2. 主播会收到 [MLVBLiveRoomDelegate.onRequestJoinAnchor](https://cloud.tencent.com/document/product/454/34764?!editLang=zh&!preview#onRequestJoinAnchor) 的回调通知。
3. 主播调用 [responseJoinAnchor](#responseJoinAnchor ) 确定是否接受观众的连麦请求。
4. 观众会收到 requestJoinAnchor 传入的回调通知，可以得知请求是否被同意。
5. 观众如果请求被同意，则调用 [startLocalPreview](#startLocalPreview ) 开启本地摄像头，如果 App 还没有取得摄像头和麦克风权限，会触发 UI 提示。
6. 观众然后调用 [joinAnchor](#joinAnchor ) 正式进入连麦状态。
7. 主播一旦观众进入连麦状态，主播就会收到 [MLVBLiveRoomDelegate.onAnchorEnter](https://cloud.tencent.com/document/product/454/34764?!editLang=zh&!preview#onAnchorEnter) 通知。
8. 主播调用 [startRemoteView](#startRemoteView) 就可以看到连麦观众的视频画面。
9. 观众如果直播间里已经有其他观众正在跟主播进行连麦，那么新加入的这位连麦观众也会收到 [MLVBLiveRoomDelegate.onAnchorJoin](https://cloud.tencent.com/document/product/454/34764?!editLang=zh&!preview#onAnchorEnter) 通知，用于展示（startRemoteView）其他连麦者的视频画面。

------

<h3 id="responseJoinAnchor">responseJoinAnchor</h3>

主播处理连麦请求。

```
- (void)responseJoinAnchor:(NSString *)userID agree:(BOOL)agree reason:(NSString *)reason 

```

**参数**

| 参数   | 类型       | 含义                      |
| :----- | :--------- | :------------------------ |
| userID | NSString * | 观众 ID。                 |
| agree  | BOOL       | YES：同意；NO：拒绝。     |
| reason | NSString * | 同意/拒绝连麦的原因描述。 |

**介绍**

主播在收到 [MLVBLiveRoomDelegate.onRequestJoinAnchor](https://cloud.tencent.com/document/product/454/34764?!editLang=zh&!preview#onRequestJoinAnchor) 回调之后会需要调用此接口来处理观众的连麦请求。

------

<h3 id="joinAnchor">joinAnchor</h3>

进入连麦状态。

```
- (void)joinAnchor:(void(^)(int errCode, NSString *errMsg))completion 

```

**参数**

| 参数       | 类型                                   | 含义                 |
| :--------- | :------------------------------------- | :------------------- |
| completion | void(^)(int errCode, NSString *errMsg) | 进入连麦的结果回调。 |

**介绍**

进入连麦成功后，主播和其他连麦观众会收到 [MLVBLiveRoomDelegate.onAnchorEnter](https://cloud.tencent.com/document/product/454/34764?!editLang=zh&!preview#onAnchorEnter) 通知。

------

<h3 id="quitJoinAnchor">quitJoinAnchor</h3>

观众退出连麦。

```
- (void)quitJoinAnchor:(void(^)(int errCode, NSString *errMsg))completion 

```

**参数**

| 参数       | 类型                                   | 含义                 |
| :--------- | :------------------------------------- | :------------------- |
| completion | void(^)(int errCode, NSString *errMsg) | 退出连麦的结果回调。 |

**介绍**

退出连麦成功后，主播和其他连麦观众会收到 [MLVBLiveRoomDelegate.onAnchorExit](https://cloud.tencent.com/document/product/454/34764?!editLang=zh&!preview#onAnchorExit) 通知。

------

<h3 id="kickoutJoinAnchor">kickoutJoinAnchor</h3>

主播踢除连麦观众。

```
- (void)kickoutJoinAnchor:(NSString *)userID 

```

**参数**

| 参数   | 类型       | 含义            |
| :----- | :--------- | :-------------- |
| userID | NSString * | 连麦小主播 ID。 |

**介绍**

主播调用此接口踢除连麦观众后，被踢连麦观众会收到 [MLVBLiveRoomDelegate.onKickoutJoinAnchor](https://cloud.tencent.com/document/product/454/34764?!editLang=zh&!preview#onKickoutJoinAnchor) 回调通知。

## 主播跨房间 PK

<h3 id="requestRoomPK">requestRoomPK</h3>

请求跨房 PK。

```
- (void)requestRoomPK:(NSString *)userID completion:(void(^)(int errCode, NSString *errMsg, NSString *streamUrl))completion 

```

**参数**

| 参数       | 类型                                                        | 含义                     |
| :--------- | :---------------------------------------------------------- | :----------------------- |
| userID     | NSString *                                                  | 被邀约主播 ID。          |
| completion | void(^)(int errCode, NSString *errMsg, NSString *streamUrl) | 请求跨房 PK 的结果回调。 |

**介绍**

主播和主播之间可以跨房间 PK，两个正在直播中的主播 A 和 B，他们之间的跨房 PK 流程如下：

1. 主播 A 调用 [requestRoomPK](#responseRoomPK ) 向主播 B 发起连麦请求。
2. 主播 B 会收到 [MLVBLiveRoomDelegate.onRequestRoomPK](https://cloud.tencent.com/document/product/454/34764?!editLang=zh&!preview#onRequestRoomPK) 回调通知。
3. 主播 B 调用 responseRoomPK 确定是否接受主播 A 的 PK 请求。
4. 主播 B 如果接受了主播 A 的要求，可以直接调用 startRemoteView 来显示主播 A 的视频画面。
5. 主播 A 会通过传入的 completion 收到回调通知，可以得知请求是否被同意。
6. 主播 A 如果请求被同意，则可以调用 [startRemoteView](#startRemoteView ) 显示主播 B 的视频画面。

------

<h3 id="responseRoomPK">responseRoomPK</h3>

响应跨房 PK 请求。

```
- (void)responseRoomPK:(MLVBAnchorInfo *)anchor agree:(BOOL)agree reason:(NSString *)reason 

```

**参数**

| 参数   | 类型             | 含义                       |
| :----- | :--------------- | :------------------------- |
| anchor | MLVBAnchorInfo * | 发起 PK 请求的主播。       |
| agree  | BOOL             | YES：同意；NO：拒绝。      |
| reason | NSString *       | 同意或拒绝 PK 的原因描述。 |

**介绍**

主播响应其他房间主播的 PK 请求，发起 PK 请求的主播会收到 [MLVBLiveRoomDelegate.onRequestRoomPK](https://cloud.tencent.com/document/product/454/34764?!editLang=zh&!preview#onRequestRoomPK) 回调通知。

------

<h3 id="quitRoomPK">quitRoomPK</h3>

退出跨房 PK。

```
- (void)quitRoomPK:(void(^)(int errCode, NSString *errMsg))completion 

```

**参数**

| 参数       | 类型                                   | 含义                     |
| :--------- | :------------------------------------- | :----------------------- |
| completion | void(^)(int errCode, NSString *errMsg) | 退出跨房 PK 的结果回调。 |

**介绍**

当两个主播中的任何一个退出跨房 PK 状态后，另一个主播会收到 [MLVBLiveRoomDelegate.onQuitRoomPK]( https://cloud.tencent.com/document/product/454/34764?!editLang=zh&!preview#onQuitRoomPK) 回调通知。

## 视频相关接口函数

<h3 id="startLocalPreview">startLocalPreview</h3>

开启本地视频的预览画面。

```
- (void)startLocalPreview:(BOOL)frontCamera view:(UIView *)view 

```

**参数**

| 参数        | 类型     | 含义                              |
| :---------- | :------- | :-------------------------------- |
| frontCamera | BOOL     | YES：前置摄像头；NO：后置摄像头。 |
| view        | UIView * | 承载视频画面的控件。              |

------

<h3 id="stopLocalPreview">stopLocalPreview</h3>

停止本地视频采集及预览。

```
- (void)stopLocalPreview

```

------

<h3 id="startRemoteView">startRemoteView</h3>

启动渲染远端视频画面。

```
- (void)startRemoteView:(MLVBAnchorInfo *)anchorInfo view:(UIView *)view onPlayBegin:(IPlayBegin)onPlayBegin onPlayError:(IPlayError)onPlayError playEvent:(IPlayEventBlock)onPlayEvent 

```

**参数**

| 参数        | 类型             | 含义                 |
| :---------- | :--------------- | :------------------- |
| anchorInfo  | MLVBAnchorInfo * | 对方的用户信息。     |
| view        | UIView *         | 承载视频画面的控件。 |
| onPlayBegin | IPlayBegin       | 播放器开始回调。     |
| onPlayError | IPlayError       | 播放出错回调。       |
| onPlayEvent | IPlayEventBlock  | 其它播放事件回调。   |

>? 在 onUserVideoAvailable 回调时，调用这个接口。

------

<h3 id="stopRemoteView">stopRemoteView</h3>

停止渲染远端视频画面。

```
- (void)stopRemoteView:(MLVBAnchorInfo *)anchor 

```

**参数**

| 参数   | 类型             | 含义         |
| :----- | :--------------- | :----------- |
| anchor | MLVBAnchorInfo * | 对方的用户。 |

------

<h3 id="setMirror">setMirror</h3>

设置观众端镜像效果。

```
- (void)setMirror:(BOOL)isMirror 

```

**参数**

| 参数     | 类型 | 含义                                                        |
| :------- | :--- | :---------------------------------------------------------- |
| isMirror | BOOL | YES：播放端看到的是镜像画面；NO：播放端看到的是非镜像画面。 |

**介绍**

由于前置摄像头采集的画面是取自手机的观察视角，将采集到的画面直接展示给观众是没有问题的，但如果将采集到的画面也直接显示给主播，会让主播感受到和照镜子时完全相反的体验，主播会感到很奇怪。 因此，SDK 会默认开启本地摄像头预览画面的镜像效果，让主播直播时感受到和照镜子一样的体验效果。
setMirror 所影响的是观众端看到的视频效果，如果想要保持观众端看到的效果跟主播端保持一致，需要开启镜像； 如果想要让观众端看到正常的未经处理过的画面（如主播弹吉他的时候有类似需求），则可以关闭镜像。

>? 仅当前使用前置摄像头时，setMirror 接口才会生效，**在使用后置摄像头时此接口无效**。

## 音频相关接口函数

<h3 id="muteLocalAudio">muteLocalAudio</h3>

是否屏蔽本地音频。

```
- (void)muteLocalAudio:(BOOL)mute 

```

**参数**

| 参数 | 类型 | 含义                  |
| :--- | :--- | :-------------------- |
| mute | BOOL | YES：屏蔽；NO：开启。 |

------

<h3 id="muteRemoteAudio">muteRemoteAudio</h3>

设置指定用户是否静音。

```
- (void)muteRemoteAudio:(NSString *)userID mute:(BOOL)mute 

```

**参数**

| 参数   | 类型       | 含义                    |
| :----- | :--------- | :---------------------- |
| userID | NSString * | 对方的用户标识。        |
| mute   | BOOL       | YES：静音；NO：非静音。 |

------

<h3 id="muteAllRemoteAudio">muteAllRemoteAudio</h3>

设置所有远端用户是否静音。

```
- (void)muteAllRemoteAudio:(BOOL)mute 

```

**参数**

| 参数 | 类型 | 含义                    |
| :--- | :--- | :---------------------- |
| mute | BOOL | YES：静音；NO：非静音。 |

## 摄像头相关接口函数

<h3 id="switchCamera">switchCamera</h3>

切换前后摄像头。

```
- (void)switchCamera

```

------

<h3 id="setCameraMuteImage">setCameraMuteImage</h3>

主播屏蔽摄像头期间需要显示的等待图片。

```
- (void)setCameraMuteImage:(UIImage *)image 

```

**参数**

| 参数  | 类型      | 含义       |
| :---- | :-------- | :--------- |
| image | UIImage * | 等待图片。 |

**介绍**

当主播屏蔽摄像头，或者由于 App 切入后台无法使用摄像头的时候，我们需要使用一张等待图片来提示观众“主播暂时离开，请不要走开”。

------

<h3 id="setZoom">setZoom</h3>

调整焦距。

```
- (void)setZoom:(CGFloat)distance 

```

**参数**

| 参数     | 类型    | 含义                        |
| :------- | :------ | :-------------------------- |
| distance | CGFloat | 焦距大小，取值范围：1 - 5。 |

>? 当为1的时候为最远视角（正常镜头），当为5的时候为最近视角（放大镜头），这里最大值推荐为5，超过5后视频数据会变得模糊不清。

------

<h3 id="enableTorch">enableTorch</h3>

打开闪关灯。

```
- (BOOL)enableTorch:(BOOL)bEnable 

```

**参数**

| 参数    | 类型 | 含义                  |
| :------ | :--- | :-------------------- |
| bEnable | BOOL | YES：打开；NO：关闭。 |

**返回**

YES：打开成功；NO：打开失败。

------

<h3 id="setFocusPosition">setFocusPosition</h3>

设置手动对焦区域。

```
- (void)setFocusPosition:(CGPoint)touchPoint 

```

**介绍**

SDK 默认使用摄像头自动对焦功能，您也可以通过 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34753?!editLang=zh&!preview#TXLivePushConfig) 中的 touchFocus 选项关闭自动对焦，改用手动对焦。 改用手动对焦之后，需要由主播自己单击摄像头预览画面上的某个区域，来手动指导摄像头对焦。

## 美颜滤镜相关接口函数

<h3 id="getBeautyManager">getBeautyManager</h3>

获取美颜管理对象 [TXBeautyManager]( https://cloud.tencent.com/document/product/454/34753?!editLang=zh&!preview#TXBeautyManager)。

```
- (TXBeautyManager *)getBeautyManager 

```

**介绍**

通过美颜管理，您可以使用以下功能：

- 设置”美颜风格”、”美白”、“红润”、“大眼”、“瘦脸”、“V脸”、“下巴”、“短脸”、“小鼻”、“亮眼”、“白牙”、“祛眼袋”、“祛皱纹”、“祛法令纹”等美容效果。

- 调整“发际线”、“眼间距”、“眼角”、“嘴形”、“鼻翼”、“鼻子位置”、“嘴唇厚度”、“脸型”。

- 设置人脸挂件（素材）等动态效果。

- 添加美妆。

- 进行手势识别。

---

<h3 id="setBeautyStyle">setBeautyStyle</h3>

设置美颜、美白、红润效果级别。

```
- boolean setBeautyStyle(int beautyStyle , int beautyLevel, int whitenessLevel, int ruddinessLevel)

```

**参数**

| 参数           | 类型 | 含义                                                         |
| :------------- | :--- | :----------------------------------------------------------- |
| beautyStyle    | int  | 美颜风格，三种美颜风格：0 ：光滑；1：自然；2：天天 P 图版美颜（企业版有效，普通版本设置此选项无效）。 |
| beautyLevel    | int  | 美颜级别，取值范围 0 - 9； 0 表示关闭， 1 - 9值越大，效果越明显。 |
| whitenessLevel | int  | 美白级别，取值范围 0 - 9； 0 表示关闭， 1 - 9值越大，效果越明显。 |
| ruddinessLevel | int  | 红润级别，取值范围 0 - 9； 0 表示关闭， 1 - 9值越大，效果越明显。 |

------

<h3 id="setFilter">setFilter</h3>

设置指定素材滤镜特效。

```
- (void)setFilter:(UIImage *)image 

```

**参数**

| 参数  | 类型      | 含义                         |
| :---- | :-------- | :--------------------------- |
| image | UIImage * | 指定素材，即颜色查找表图片。 |

>? 滤镜素材请使用 png 格式，不能使用 jpg 格式。友情提示：Windows 里直接改文件的后缀名不能改变图片的格式，需要用 Photoshop 进行转换。

------

<h3 id="setSpecialRatio">setSpecialRatio</h3>

设置滤镜浓度。

```
- (void)setSpecialRatio:(float)specialValue 

```

**参数**

| 参数         | 类型  | 含义                                      |
| :----------- | :---- | :---------------------------------------- |
| specialValue | float | 从0到1，越大滤镜效果越明显，默认取值0.5。 |

------

<h3 id="setEyeScaleLevel">setEyeScaleLevel</h3>

设置大眼级别（企业版有效，普通版本设置此参数无效）。

```
- (void)setEyeScaleLevel:(float)eyeScaleLevel MLVB_DEPRECAETD_BEAUTY_API

```

**参数**

| 参数          | 类型  | 含义                                                         |
| :------------ | :---- | :----------------------------------------------------------- |
| eyeScaleLevel | float | 大眼等级取值为 0 - 9。取值为0时代表关闭美颜效果。默认值：0。 |

------

<h3 id="setFaceScaleLevel">setFaceScaleLevel</h3>

设置瘦脸级别（企业版有效，普通版本设置此参数无效）。

```
- (void)setFaceScaleLevel:(float)faceScaleLevel MLVB_DEPRECAETD_BEAUTY_API

```

**参数**

| 参数           | 类型  | 含义                                                         |
| :------------- | :---- | :----------------------------------------------------------- |
| faceScaleLevel | float | 瘦脸级别取值范围 0 - 9； 0 表示关闭 1 - 9值越大 效果越明显。 |

------

<h3 id="setFaceVLevel">setFaceVLevel</h3>

设置 V 脸级别（企业版有效，其它版本设置此参数无效）。

```
- (void)setFaceVLevel:(float)faceVLevel MLVB_DEPRECAETD_BEAUTY_API

```

**参数**

| 参数       | 类型  | 含义                                                         |
| :--------- | :---- | :----------------------------------------------------------- |
| faceVLevel | float | V 脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

------

<h3 id="setChinLevel">setChinLevel</h3>

设置下巴拉伸或收缩（企业版有效，其它版本设置此参数无效）。

```
- (void)setChinLevel:(float)chinLevel MLVB_DEPRECAETD_BEAUTY_API

```

**参数**

| 参数       | 类型      | 含义                                                         |
| :--------- | :-------- | :----------------------------------------------------------- |
| faceVLevel | chinLevel | 下巴拉伸或收缩级别，取值范围 -9 - 9；0 表示关闭，小于0表示收缩，大于0表示拉伸。 |

------

<h3 id="setFaceShortLevel">setFaceShortLevel</h3>

设置短脸级别（企业版有效，其它版本设置此参数无效）。

```
- (void)setFaceShortLevel:(float)faceShortlevel MLVB_DEPRECAETD_BEAUTY_API

```

**参数**

| 参数           | 类型      | 含义                                                         |
| :------------- | :-------- | :----------------------------------------------------------- |
| faceShortlevel | chinLevel | 短脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

------

<h3 id="setNoseSlimLevel">setNoseSlimLevel</h3>

设置瘦鼻级别（企业版有效，其它版本设置此参数无效）。

```
- (void)setNoseSlimLevel:(float)noseSlimLevel MLVB_DEPRECAETD_BEAUTY_API

```

**参数**

| 参数          | 类型      | 含义                                                         |
| :------------ | :-------- | :----------------------------------------------------------- |
| noseSlimLevel | chinLevel | 瘦鼻级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

------

<h3 id="setGreenScreenFile">setGreenScreenFile</h3>

设置绿幕背景视频（商业版有效，其它版本设置此参数无效）。

```
- (void)setGreenScreenFile:(NSURL *)file 

```

**参数**

| 参数 | 类型    | 含义                                       |
| :--- | :------ | :----------------------------------------- |
| file | NSURL * | 视频文件路径。支持 MP4；nil 表示关闭特效。 |

>? 此处的绿幕功能并非智能抠背，它需要被拍摄者的背后有一块绿色的幕布来辅助产生特效。

------

<h3 id="selectMotionTmpl">selectMotionTmpl</h3>

选择使用哪一款 AI 动效挂件（企业版有效，其它版本设置此参数无效）。

```
- (void)selectMotionTmpl:(NSString *)tmplName inDir:(NSString *)tmplDir MLVB_DEPRECAETD_BEAUTY_API

```

**参数**

| 参数     | 类型       | 含义           |
| :------- | :--------- | :------------- |
| tmplName | NSString * | 动效名称。     |
| tmplDir  | NSString * | 动效所在目录。 |

## 消息发送接口函数

<h3 id="sendRoomTextMsg">sendRoomTextMsg</h3>

发送文本消息。

```
- (void)sendRoomTextMsg:(NSString *)message completion:(void(^)(int errCode, NSString *errMsg))completion 

```

**参数**

| 参数       | 类型                                   | 含义           |
| :--------- | :------------------------------------- | :------------- |
| message    | NSString *                             | 文本消息。     |
| completion | void(^)(int errCode, NSString *errMsg) | 发送结果回调。 |

------

<h3 id="sendRoomCustomMsg">sendRoomCustomMsg</h3>

发送自定义文本消息。

```
- (void)sendRoomCustomMsg:(NSString *)cmd msg:(NSString *)message completion:(void(^)(int errCode, NSString *errMsg))completion 

```

**参数**

| 参数       | 类型                                   | 含义                                               |
| :--------- | :------------------------------------- | :------------------------------------------------- |
| cmd        | NSString *                             | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message    | NSString *                             | 文本消息。                                         |
| completion | void(^)(int errCode, NSString *errMsg) | 发送结果回调。                                     |

## 背景混音相关接口函数

<h3 id="playBGM">playBGM</h3>

播放背景音乐。

```
- (BOOL)playBGM:(NSString *)path 

```

**参数**

| 参数 | 类型       | 含义                                                         |
| :--- | :--------- | :----------------------------------------------------------- |
| path | NSString * | 音乐文件路径，一定要是 `app` 对应的 `document` 目录下面的路径，否则文件会读取失败。 |

**返回**

YES：成功；NO：失败。

------

<h3 id="playBGM">playBGM</h3>

播放背景音乐（高级版本）。

```
- (BOOL)playBGM:(NSString *)path withBeginNotify:(void(^)(NSInteger errCode))beginNotify withProgressNotify:(void(^)(NSInteger progressMS, NSInteger durationMS))progressNotify andCompleteNotify:(void(^)(NSInteger errCode))completeNotify 

```

**参数**

| 参数           | 类型                                                | 含义                                                         |
| :------------- | :-------------------------------------------------- | :----------------------------------------------------------- |
| path           | NSString *                                          | 音乐文件路径，一定要是 `app` 对应的 `document` 目录下面的路径，否则文件会读取失败。 |
| beginNotify    | void(^)(NSInteger errCode)                          | 音乐播放开始的回调通知。                                     |
| progressNotify | void(^)(NSInteger progressMS, NSInteger durationMS) | 音乐播放的进度通知，单位：毫秒。                             |
| completeNotify | void(^)(NSInteger errCode)                          | 音乐播放结束的回调通知。                                     |

**返回**

YES：成功；NO：失败。

------

<h3 id="stopBGM">stopBGM</h3>

停止播放背景音乐。

```
- (BOOL)stopBGM

```

------

<h3 id="pauseBGM">pauseBGM</h3>

暂停播放背景音乐。

```
- (BOOL)pauseBGM

```

------

<h3 id="resumeBGM">resumeBGM</h3>

继续播放背景音乐。

```
- (BOOL)resumeBGM

```

------

<h3 id="getMusicDuration">getMusicDuration</h3>

获取音乐文件总时长，单位毫秒。

```
- (int)getMusicDuration:(NSString *)path 

```

**参数**

| 参数 | 类型       | 含义                                                         |
| :--- | :--------- | :----------------------------------------------------------- |
| path | NSString * | 音乐文件路径，如果 path 为 nil，那么返回当前正在播放的背景音乐时长。 |

**返回**

成功返回时长，单位毫秒，失败返回-1。

------

<h3 id="setMicVolume">setMicVolume</h3>

设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小。

```
- (BOOL)setMicVolume:(float)volume 

```

**参数**

| 参数   | 类型  | 含义                                          |
| :----- | :---- | :-------------------------------------------- |
| volume | float | 音量大小，1.0 为正常音量，建议值为0.0 - 2.0。 |

------

<h3 id="setBGMVolume">setBGMVolume</h3>

设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小。

```
- (BOOL)setBGMVolume:(float)volume 

```

**参数**

| 参数   | 类型  | 含义                                         |
| :----- | :---- | :------------------------------------------- |
| volume | float | 音量大小，1.0为正常音量，建议值为0.0 - 2.0。 |

------

<h3 id="setBGMPitch">setBGMPitch</h3>

调整背景音乐的音调高低。

```
- (BOOL)setBGMPitch:(float)pitch 

```

**参数**

| 参数  | 类型  | 含义                                           |
| :---- | :---- | :--------------------------------------------- |
| pitch | float | 音调，默认值是0.0f，范围：-1 - 1之间的浮点数。 |

**返回**

YES：成功；NO：失败。

------

<h3 id="setBGMPosition">setBGMPosition</h3>

调整背景音乐的音调高低。

```
- (BOOL)setBGMPosition:(float)position

```

**参数**

| 参数     | 类型  | 含义                                |
| :------- | :---- | :---------------------------------- |
| position | float | 播放位置，默认值是0；范围是 0 - 1。 |

---

<h3 id="setReverbType">setReverbType</h3>

设置混响效果。

```
- (BOOL)setReverbType:(TXReverbType)reverbType 
```

**参数**

| 参数       | 类型         | 含义                                                       |
| :--------- | :----------- | :--------------------------------------------------------- |
| reverbType | TXReverbType | 混响类型，详见`TXLiveSDKTypeDef.h`中的 TXReverbType 定义。 |

**返回**

YES：成功；NO：失败。

------

<h3 id="setVoiceChangerType">setVoiceChangerType</h3>

设置变声类型。

```
- (BOOL)setVoiceChangerType:(TXVoiceChangerType)voiceChangerType 
```

**参数**

| 参数             | 类型               | 含义                                                         |
| :--------------- | :----------------- | :----------------------------------------------------------- |
| voiceChangerType | TXVoiceChangerType | 混响类型，详见`TXLiveSDKTypeDef.h`中的 voiceChangerType 定义。 |

**返回**

YES：成功；NO：失败。

## 调试相关接口函数

<h3 id="showVideoDebugLog">showVideoDebugLog</h3>

在渲染 view 上显示播放或推流状态统计及事件消息浮层。

```
- (void)showVideoDebugLog:(BOOL)isShow 
```

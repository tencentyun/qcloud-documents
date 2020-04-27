**功能**

腾讯云移动直播 - 连麦直播间。

>! 后台接口限制并发为每秒100次请求，若您有高并发请求请提前 [联系我们](https://cloud.tencent.com/act/event/connect-service) 处理，避免影响服务调用。

**介绍**

基于腾讯云直播（LVB）、云点播（VOD） 和即时通信（IM）三大 PAAS 服务组合而成，支持：

- 主播创建新的直播间开播，观众进入直播间观看。
- 主播和观众进行视频连麦互动。
- 两个不同房间的主播 PK 互动。
- 一个直播间都有一个不限制房间人数的聊天室，支持发送各种文本消息和自定义消息，自定义消息可用于实现弹幕、点赞和礼物。

连麦直播间（MLVBLiveRoom）是一个开源的 Class，依赖两个腾讯云的闭源 SDK：

- LiteAVSDK：使用了其中的 [TXLivePusher](https://cloud.tencent.com/document/product/454/34766?!preview&!editLang=zh#TXLivePusher) 和 [TXLivePlayer](https://cloud.tencent.com/document/product/454/34766?!preview&!editLang=zh#TXLivePlayer) 两个组件，前者用于推流，后者用于拉流。
- IM SDK：使用 IM SDK 的 AVChatroom 用于实现直播聊天室的功能，同时，主播间的连麦流程也是依靠 IM 消息串联起来的。

参考文档：[直播连麦](https://cloud.tencent.com/document/product/454/14606)。

## MLVBLiveRoom API 概览

### SDK 基础函数

| API 概览                                        | 描述                       |
| ----------------------------------------------- | -------------------------- |
| [sharedInstance](#sharedInstance)               | 获取 MLVBLiveRoom 单例对象 |
| [destroySharedInstance](#destroySharedInstance) | 销毁 MLVBLiveRoom 单例对象 |
| [setListener](#setListener)                     | 设置回调接口               |
| [setListenerHandler](#setListenerHandler)       | 设置驱动回调的线程         |
| [login](#login)                                 | 登录                       |
| [logout](#logout)                               | 退出登录                   |
| [setSelfProfile](#setSelfProfile)               | 修改个人信息               |

###  **房间相关接口函数** 

| API                                 | 描述                 |
| ----------------------------------- | -------------------- |
| [getRoomList](#getRoomList)         | 获取房间列表         |
| [getAudienceList](#getAudienceList) | 获取观众列表         |
| [createRoom](#createRoom)           | 创建房间（主播调用） |
| [enterRoom](#enterRoom)             | 进入房间（观众调用） |
| [exitRoom](#exitRoom)               | 离开房间             |
| [setCustomInfo](#setCustomInfo)     | 设置自定义信息       |
| [getCustomInfo](#getCustomInfo)     | 获取自定义信息       |

###  **主播和观众连麦** 

| API                                       | 描述             |
| ----------------------------------------- | ---------------- |
| [requestJoinAnchor](#requestJoinAnchor)   | 观众请求连麦     |
| [responseJoinAnchor](#responseJoinAnchor) | 主播处理连麦请求 |
| [joinAnchor](#joinAnchor)                 | 进入连麦状态     |
| [quitJoinAnchor](#quitJoinAnchor)         | 观众退出连麦     |
| [kickoutJoinAnchor](#kickoutJoinAnchor)   | 主播踢除连麦观众 |

###   **主播跨房间 PK**  

| API                               | 描述             |
| --------------------------------- | ---------------- |
| [requestRoomPK](#requestRoomPK)   | 请求跨房 PK      |
| [responseRoomPK](#responseRoomPK) | 响应跨房 PK 请求 |
| [quitRoomPK](#quitRoomPK)         | 退出跨房 PK      |

###   **视频相关接口函数**  

| API                                       | 描述                   |
| ----------------------------------------- | ---------------------- |
| [startLocalPreview](#startLocalPreview)   | 开启本地视频的预览画面 |
| [stopLocalPreview](#stopLocalPreview)     | 停止本地视频采集及预览 |
| [startRemoteView](#startRemoteView)       | 启动渲染远端视频画面   |
| [stopRemoteView](#stopRemoteView)         | 停止渲染远端视频画面   |
| [startScreenCapture](#startScreenCapture) | 启动录屏               |
| [stopScreenCapture](#stopScreenCapture)   | 结束录屏               |

###   **音频相关接口函数** 

| API                                       | 描述                     |
| ----------------------------------------- | ------------------------ |
| [muteLocalAudio](#muteLocalAudio)         | 是否屏蔽本地音频         |
| [muteRemoteAudio](#muteRemoteAudio)       | 设置指定用户是否静音     |
| [muteAllRemoteAudio](#muteAllRemoteAudio) | 设置所有远端用户是否静音 |

###   **摄像头相关接口函数** 

| API                                       | 描述                                 |
| ----------------------------------------- | ------------------------------------ |
| [switchCamera](#switchCamera)             | 切换摄像头                           |
| [setZoom](#setZoom)                       | 设置摄像头缩放因子（焦距）           |
| [enableTorch](#enableTorch)               | 开关闪光灯                           |
| [setCameraMuteImage](#setCameraMuteImage) | 主播屏蔽摄像头期间需要显示的等待图片 |
| [setCameraMuteImage](#setCameraMuteImage) | 主播屏蔽摄像头期间需要显示的等待图片 |

###   **美颜滤镜相关接口函数** 

| API                                                 | 描述                                                         |
| --------------------------------------------------- | ------------------------------------------------------------ |
| [getBeautyManager](#getBeautyManager)               | 获取美颜管理对象 TXBeautyManager，美颜的设置通过 TXBeautyManager 来设置 |
| [setWatermark](#setWatermark)                       | 添加水印，height 不用设置，SDK 内部会根据水印宽高比自动计算 height |
| [setExposureCompensation](#setExposureCompensation) | 调整曝光                                                     |

###   **消息发送接口函数** 

| API                                     | 描述               |
| --------------------------------------- | ------------------ |
| [sendRoomTextMsg](#sendRoomTextMsg)     | 发送文本消息       |
| [sendRoomCustomMsg](#sendRoomCustomMsg) | 发送自定义文本消息 |

###   **背景混音相关接口函数** 

| API                                           | 描述                                                         |
| --------------------------------------------- | ------------------------------------------------------------ |
| [playBGM](#playBGM)                           | 播放背景音乐                                                 |
| [setBGMNofify](#setBGMNofify)                 | 设置背景音乐的回调接口                                       |
| [stopBGM](#stopBGM)                           | 停止播放背景音乐                                             |
| [pauseBGM](#pauseBGM)                         | 暂停播放背景音乐                                             |
| [resumeBGM](#resumeBGM)                       | 继续播放背景音乐                                             |
| [getBGMDuration](#getBGMDuration)             | 获取音乐文件总时长                                           |
| [setMicVolumeOnMixing](#setMicVolumeOnMixing) | 设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小 |
| [setBGMVolume](#setBGMVolume)                 | 设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小 |
| [setReverbType](#setReverbType)               | 设置混响效果                                                 |
| [setVoiceChangerType](#setVoiceChangerType)   | 设置变声类型                                                 |
| [setBgmPitch](#setBgmPitch)                   | 设置背景音乐的音调                                           |
| [setBGMPosition](#setBGMPosition)             | 设置变声类型                                                 |

###   **废弃项** 

| API                                               | 描述                             |
| ------------------------------------------------- | -------------------------------- |
| [setBeautyStyle](#setBeautyStyle)                 | 设置美颜、美白、红润效果级别     |
| [setFilter](#setFilter)                           | 设置指定素材滤镜特效             |
| [setFilterConcentration](#setFilterConcentration) | 设置滤镜浓度                     |
| [setMotionTmpl](#setMotionTmpl)                   | 设置动效贴图                     |
| [setGreenScreenFile](#setGreenScreenFile)         | 设置绿幕文件                     |
| [setEyeScaleLevel](#setEyeScaleLevel)             | 设置大眼效果                     |
| [setFaceVLevel](#setFaceVLevel)                   | 设置 V 脸（企业版有效）          |
| [setFaceSlimLevel](#setFaceSlimLevel)             | 设置瘦脸效果                     |
| [setFaceShortLevel](#setFaceShortLevel)           | 设置短脸（企业版有效）           |
| [setChinLevel](#setChinLevel)                     | 设置下巴拉伸或收缩（企业版有效） |
| [setNoseSlimLevel](#setNoseSlimLevel)             | 设置瘦鼻（企业版有效）           |



## SDK 基础函数

<h3 id="sharedInstance">sharedInstance</h3>

获取 MLVBLiveRoom 单例对象。

```
MLVBLiveRoom sharedInstance(Context context)
```

**参数**

| 参数    | 类型    | 含义                                                         |
| :------ | :------ | :----------------------------------------------------------- |
| context | Context | Android 上下文，内部会转为 ApplicationContext 用于系统 API 调用。 |

**返回**

MLVBLiveRoom 实例。

>? 可以调用 destroySharedInstance() 销毁单例对象。

------

<h3 id="destroySharedInstance">destroySharedInstance</h3>

销毁 MLVBLiveRoom 单例对象。

```
void destroySharedInstance()
```

>? 销毁实例后，外部缓存的 MLVBLiveRoom 实例不能再使用，需要重新调用 sharedInstance(Context) 获取新实例。

------

<h3 id="setListener">setListener</h3>

设置回调接口。

```
- void setListener(IMLVBLiveRoomListener listener)
```

**参数**

| 参数     | 类型                  | 含义       |
| :------- | :-------------------- | :--------- |
| listener | IMLVBLiveRoomListener | 回调接口。 |

**介绍**

您可以通过 [IMLVBLiveRoomListener](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh) 获得 MLVBLiveRoom 的各种状态通知。

>? 默认是在 Main Thread 中回调，如果需要自定义回调线程，可使用 [setListenerHandler(Handler)](#setListenerHandler)。

------

<h3 id="setListenerHandler">setListenerHandler</h3>

设置驱动回调的线程。

```
- void setListenerHandler(Handler listenerHandler)
```

**参数**

| 参数            | 类型    | 含义   |
| :-------------- | :------ | :----- |
| listenerHandler | Handler | 线程。 |

------

<h3 id="login">login</h3>

登录。

```
- void login(final LoginInfo loginInfo, finalIMLVBLiveRoomListener.LoginCallback callback)
```

**参数**

| 参数      | 类型                                                         | 含义           |
| :-------- | :----------------------------------------------------------- | :------------- |
| loginInfo | final LoginInfo                                              | 登录信息。     |
| callback  | final [IMLVBLiveRoomListener.LoginCallback](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#LoginCallback) | 登录结果回调。 |

------

<h3 id="logout">logout</h3>

退出登录。

```
- void logout()
```

------

<h3 id="setSelfProfile">setSelfProfile</h3>

修改个人信息。

```
- void setSelfProfile(String userName, String avatarURL)
```

**参数**

| 参数      | 类型   | 含义       |
| :-------- | :----- | :--------- |
| userName  | String | 昵称。     |
| avatarURL | String | 头像地址。 |

------

## 房间相关接口函数

<h3 id="getRoomList">getRoomList</h3>

获取房间列表。

```
- void getRoomList(int index, int count, finalIMLVBLiveRoomListener.GetRoomListCallback callback)
```

**参数**

| 参数     | 类型                                                         | 含义                        |
| :------- | :----------------------------------------------------------- | :-------------------------- |
| index    | int                                                          | 房间开始索引，从0开始计算。 |
| count    | int                                                          | 希望后台返回的房间个数。    |
| callback | final [IMLVBLiveRoomListener.GetRoomListCallback](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#GetRoomListCallback) | 获取房间列表的结果回调。    |

**介绍**

该接口支持分页获取房间列表，可以用 index 和 count 两个参数控制列表分页的逻辑：

- index = 0 & count = 10 代表获取第一页的10个房间。
- index = 11 & count = 10 代表获取第二页的10个房间。

------

<h3 id="getAudienceList">getAudienceList</h3>

获取观众列表。

```
- void getAudienceList(IMLVBLiveRoomListener.GetAudienceListCallback callback)
```

**参数**

| 参数     | 类型                                                         | 含义                     |
| :------- | :----------------------------------------------------------- | :----------------------- |
| callback | [IMLVBLiveRoomListener.GetAudienceListCallback](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#GetAudienceListCallback) | 获取观众列表的结果回调。 |

**介绍**

当有观众进房时，后台会将其信息加入到指定房间的观众列表中，调入该函数即可返回指定房间的观众列表。

>? 观众列表最多只保存30人，因为对于常规的 UI 展示来说这已经足够，保存更多除了浪费存储空间，也会拖慢列表返回的速度。

------

<h3 id="createRoom">createRoom</h3>

创建房间（主播调用）。

```
- void createRoom(final String roomID, final String roomInfo, finalIMLVBLiveRoomListener.CreateRoomCallback callback)
```

**参数**

| 参数     | 类型                                                         | 含义                                                         |
| :------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| roomID   | final String                                                 | 房间标识，推荐做法是用主播的 userID 作为房间的 roomID，可省去后台映射的成本。roomID 可以填空，此时由后台生成。 |
| roomInfo | final String                                                 | 房间信息（非必填），用于房间描述的信息，如房间名称，允许使用 JSON 格式作为房间信息。 |
| callback | final [IMLVBLiveRoomListener.CreateRoomCallback](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#CreateRoomCallback) | 创建房间的结果回调。                                         |

**介绍**

主播开播的正常调用流程是：

1. 主播调用 startLocalPreview() 打开摄像头预览，此时可以调整美颜参数。
2. 主播调用 createRoom 创建直播间，房间创建成功与否会通过 IMLVBLiveRoomListener.CreateRoomCallback 通知给主播。

------

<h3 id="enterRoom">enterRoom</h3>

进入房间（观众调用）。

```
- void enterRoom(final String roomID, final TXCloudVideoView view, finalIMLVBLiveRoomListener.EnterRoomCallback callback)
```

**参数**

| 参数     | 类型                                         | 含义                 |
| :------- | :------------------------------------------- | :------------------- |
| roomID   | final String                                 | 房间标识。           |
| view     | final TXCloudVideoView                       | 承载视频画面的控件。 |
| callback | finalIMLVBLiveRoomListener.EnterRoomCallback | 进入房间的结果回调。 |

**介绍**

观众观看直播的正常调用流程是：

1. 观众调用 getRoomList() 刷新最新的直播房间列表，并通过 [IMLVBLiveRoomListener.GetRoomListCallback](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#GetRoomListCallback) 回调拿到房间列表。
2. 观众选择一个直播间以后，调用 enterRoom() 进入该房间。

------

<h3 id="exitRoom">exitRoom</h3>

离开房间。

```
- void exitRoom(IMLVBLiveRoomListener.ExitRoomCallback callback)
```

**参数**

| 参数     | 类型                                   | 含义                 |
| :------- | :------------------------------------- | :------------------- |
| callback | IMLVBLiveRoomListener.ExitRoomCallback | 离开房间的结果回调。 |

------

<h3 id="setCustomInfo">setCustomInfo</h3>

设置自定义信息。

```
- void setCustomInfo(final MLVBCommonDef.CustomFieldOp op, final String key, final Object value, finalIMLVBLiveRoomListener.SetCustomInfoCallback callback)
```

**参数**

| 参数     | 类型                                                         | 含义                                               |
| :------- | :----------------------------------------------------------- | :------------------------------------------------- |
| op       | final MLVBCommonDef.CustomFieldOp                            | 执行动作，定义请查看 MLVBCommonDef.CustomFieldOp。 |
| key      | final String                                                 | 自定义键。                                         |
| value    | final Object                                                 | 数值。                                             |
| callback | final [IMLVBLiveRoomListener.SetCustomInfoCallback](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#SetCustomInfoCallback) | 设置自定义信息完成的回调。                         |

**介绍**

有时候您可能需要为房间产生一些额外的信息，此接口可以将这些信息缓存到服务器。

>? 
>
>- op 为 MLVBCommonDef.CustomFieldOp#SET 时，value 可以是 String 或者 Integer 类型。
>- op 为 MLVBCommonDef.CustomFieldOp#INC 时，value 是 Integer 类型。
>- op 为 MLVBCommonDef.CustomFieldOp#DEC 时，value 是 Integer 类型。

------

<h3 id="getCustomInfo">getCustomInfo</h3>

获取自定义信息。

```
- void getCustomInfo(finalIMLVBLiveRoomListener.GetCustomInfoCallback callback)
```

**参数**

| 参数     | 类型                                                         | 含义                 |
| :------- | :----------------------------------------------------------- | :------------------- |
| callback | final [IMLVBLiveRoomListener.GetCustomInfoCallback](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#GetCustomInfoCallback) | 获取自定义信息回调。 |

------

## 主播和观众连麦

<h3 id="requestJoinAnchor">requestJoinAnchor</h3>

观众请求连麦。

```
- void requestJoinAnchor(String reason,IMLVBLiveRoomListener.RequestJoinAnchorCallback callback)
```

**参数**

| 参数     | 类型                                                         | 含义             |
| :------- | :----------------------------------------------------------- | :--------------- |
| reason   | String                                                       | 连麦原因。       |
| callback | [IMLVBLiveRoomListener.RequestJoinAnchorCallback](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#RequestJoinAnchorCallback) | 请求连麦的回调。 |

**介绍**

主播和观众的连麦流程可以简单描述为如下几个步骤：

1. 【观众】调用 requestJoinAnchor() 向主播发起连麦请求。
2. 【主播】会收到 [IMLVBLiveRoomListener.onRequestJoinAnchor(AnchorInfo, String)](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#onRequestJoinAnchor) 的回调通知。
3. 【主播】调用 responseJoinAnchor() 确定是否接受观众的连麦请求。
4. 【观众】会收到IMLVBLiveRoomListener.RequestJoinAnchorCallback 回调通知，可以得知请求是否被同意。
5. 【观众】如果请求被同意，则调用 startLocalPreview() 开启本地摄像头，如果 App 还没有取得摄像头和麦克风权限，会触发 UI 提示。
6. 【观众】然后调用 joinAnchor() 正式进入连麦状态。
7. 【主播】一旦观众进入连麦状态，主播就会收到 [IMLVBLiveRoomListener.onAnchorEnter(AnchorInfo)](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#onAnchorEnter) 通知。
8. 【主播】主播调用 startRemoteView() 就可以看到连麦观众的视频画面。
9. 【观众】如果直播间里已经有其他观众正在跟主播进行连麦，那么新加入的这位连麦观众也会收到 onAnchorJoin() 通知，用于展示（startRemoteView）其他连麦者的视频画面。

------

<h3 id="responseJoinAnchor">responseJoinAnchor</h3>

主播处理连麦请求。

```
- int responseJoinAnchor(String userID, boolean agree, String reason)
```

**参数**

| 参数   | 类型    | 含义                      |
| :----- | :------ | :------------------------ |
| userID | String  | 观众ID。                  |
| agree  | boolean | true：同意；false：拒绝。 |
| reason | String  | 同意/拒绝连麦的原因描述。 |

**返回**

0：响应成功；非0：响应失败。

**介绍**

主播在收到 [IMLVBLiveRoomListener.onRequestJoinAnchor(AnchorInfo， String)](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#onRequestJoinAnchor) 回调之后会需要调用此接口来处理观众的连麦请求。

------

<h3 id="joinAnchor">joinAnchor</h3>

进入连麦状态。

```
- void joinAnchor(finalIMLVBLiveRoomListener.JoinAnchorCallback callback)
```

**参数**

| 参数     | 类型                                                         | 含义                 |
| :------- | :----------------------------------------------------------- | :------------------- |
| callback | [IMLVBLiveRoomListener.JoinAnchorCallback](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#JoinAnchorCallback) | 进入连麦的结果回调。 |

**介绍**

进入连麦成功后，主播和其他连麦观众会收到 [IMLVBLiveRoomListener.onAnchorEnter(AnchorInfo)](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#onAnchorEnter) 通知。

------

<h3 id="quitJoinAnchor">quitJoinAnchor</h3>

观众退出连麦。

```
- void quitJoinAnchor(finalIMLVBLiveRoomListener.QuitAnchorCallback callback)
```

**参数**

| 参数     | 类型                                                         | 含义                 |
| :------- | :----------------------------------------------------------- | :------------------- |
| callback | final [IMLVBLiveRoomListener.QuitAnchorCallback](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#QuitAnchorCallback) | 退出连麦的结果回调。 |

**介绍**

退出连麦成功后，主播和其他连麦观众会收到 [IMLVBLiveRoomListener.onAnchorExit(AnchorInfo)](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#onAnchorExit) 通知。

------

<h3 id="kickoutJoinAnchor">kickoutJoinAnchor</h3>

主播踢除连麦观众。

```
- void kickoutJoinAnchor(String userID)
```

**参数**

| 参数   | 类型   | 含义          |
| :----- | :----- | :------------ |
| userID | String | 连麦观众 ID。 |

**介绍**

主播调用此接口踢除连麦观众后，被踢连麦观众会收到 [IMLVBLiveRoomListener.onKickoutJoinAnchor()](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#onKickoutJoinAnchor) 回调通知。

## 主播跨房间 PK

<h3 id="requestRoomPK">requestRoomPK</h3>

请求跨房 PK。

```
- void requestRoomPK(String userID, finalIMLVBLiveRoomListener.RequestRoomPKCallback callback)

```

**参数**

| 参数     | 类型                                                         | 含义                     |
| :------- | :----------------------------------------------------------- | :----------------------- |
| userID   | String                                                       | 被邀约主播 ID。          |
| callback | final [IMLVBLiveRoomListener.RequestRoomPKCallback](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#RequestRoomPKCallback) | 请求跨房 PK 的结果回调。 |

**介绍**

主播和主播之间可以跨房间 PK，两个正在直播中的主播 A 和 B，他们之间的跨房 PK 流程如下：

1. 主播 A 调用 requestRoomPK() 向主播 B 发起连麦请求。
2. 主播 B 会收到 [IMLVBLiveRoomListener.onRequestRoomPK(AnchorInfo)](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#onRequestRoomPK) 回调通知。
3. 主播 B 调用 responseRoomPK() 确定是否接受主播 A 的 PK 请求。
4. 主播 B 如果接受了主播 A 的要求，可以直接调用 [startRemoteView()](#startRemoteView) 来显示主播 A 的视频画面。
5. 主播 A 会收到 [IMLVBLiveRoomListener.RequestRoomPKCallback](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#RequestRoomPKCallback) 回调通知，可以得知请求是否被同意。
6. 主播 A 如果请求被同意，则可以调用 startRemoteView() 显示主播 B 的视频画面。

------

<h3 id="responseRoomPK">responseRoomPK</h3>

响应跨房 PK 请求。

```
- int responseRoomPK(String userID, boolean agree, String reason)

```

**参数**

| 参数   | 类型    | 含义                      |
| :----- | :------ | :------------------------ |
| userID | String  | 发起 PK 请求的主播 ID。   |
| agree  | boolean | true：同意；false：拒绝。 |
| reason | String  | 同意/拒绝 PK 的原因描述。 |

**返回**

0：响应成功；非0：响应失败。

**介绍**

主播响应其他房间主播的 PK 请求，发起 PK 请求的主播会收到 [IMLVBLiveRoomListener.RequestRoomPKCallback](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#RequestRoomPKCallback) 回调通知。

------

<h3 id="quitRoomPK">quitRoomPK</h3>

退出跨房 PK。

```
- void quitRoomPK(finalIMLVBLiveRoomListener.QuitRoomPKCallback callback)

```

**参数**

| 参数     | 类型                                          | 含义                     |
| :------- | :-------------------------------------------- | :----------------------- |
| callback | finalIMLVBLiveRoomListener.QuitRoomPKCallback | 退出跨房 PK 的结果回调。 |

**介绍**

当两个主播中的任何一个退出跨房 PK 状态后，另一个主播会收到 [IMLVBLiveRoomListener.onQuitRoomPK(AnchorInfo)](https://cloud.tencent.com/document/product/454/34777?!preview&!editLang=zh#onQuitRoomPK) 回调通知。

## 视频相关接口函数

<h3 id="startLocalPreview">startLocalPreview</h3>

开启本地视频的预览画面。

```
- void startLocalPreview(boolean frontCamera, TXCloudVideoView view)

```

**参数**

| 参数        | 类型             | 含义                              |
| :---------- | :--------------- | :-------------------------------- |
| frontCamera | boolean          | YES：前置摄像头；NO：后置摄像头。 |
| view        | TXCloudVideoView | 承载视频画面的控件。              |

------

<h3 id="stopLocalPreview">stopLocalPreview</h3>

停止本地视频采集及预览。

```
- void stopLocalPreview()

```

------

<h3 id="startRemoteView">startRemoteView</h3>

启动渲染远端视频画面。

```
- void startRemoteView(final AnchorInfo anchorInfo, final TXCloudVideoView view, finalIMLVBLiveRoomListener.PlayCallback callback)

```

**参数**

| 参数       | 类型                                    | 含义                 |
| :--------- | :-------------------------------------- | :------------------- |
| anchorInfo | final AnchorInfo                        | 对方的用户信息。     |
| view       | final TXCloudVideoView                  | 承载视频画面的控件。 |
| callback   | finalIMLVBLiveRoomListener.PlayCallback | 播放器监听器。       |

>? 在 onUserVideoAvailable 回调时，调用这个接口。

------

<h3 id="stopRemoteView">stopRemoteView</h3>

停止渲染远端视频画面。

```
- void stopRemoteView(final AnchorInfo anchorInfo)

```

**参数**

| 参数       | 类型             | 含义             |
| :--------- | :--------------- | :--------------- |
| anchorInfo | final AnchorInfo | 对方的用户信息。 |

------

### startScreenCapture<h3 id="startScreenCapture"></h3>

启动录屏。

```
- void startScreenCapture()



```

------

<h3 id="stopScreenCapture">stopScreenCapture</h3>

结束录屏。

```
- void stopScreenCapture()

```

------

## 音频相关接口函数

<h3 id="muteLocalAudio">muteLocalAudio</h3>

是否屏蔽本地音频。

```
- void muteLocalAudio(boolean mute)

```

**参数**

| 参数 | 类型    | 含义                      |
| :--- | :------ | :------------------------ |
| mute | boolean | true：屏蔽；false：开启。 |

------

<h3 id="muteRemoteAudio">muteRemoteAudio</h3>

设置指定用户是否静音。

```
- void muteRemoteAudio(String userID, boolean mute)

```

**参数**

| 参数   | 类型    | 含义                        |
| :----- | :------ | :-------------------------- |
| userID | String  | 对方的用户标识。            |
| mute   | boolean | true：静音；false：非静音。 |

------

<h3 id="muteAllRemoteAudio">muteAllRemoteAudio</h3>

设置所有远端用户是否静音。

```
- void muteAllRemoteAudio(boolean mute)

```

**参数**

| 参数 | 类型    | 含义                        |
| :--- | :------ | :-------------------------- |
| mute | boolean | true：静音；false：非静音。 |

------

## 摄像头相关接口函数

<h3 id="switchCamera">switchCamera</h3>

切换摄像头。

```
- void switchCamera()

```

------

<h3 id="setZoom">setZoom</h3>

设置摄像头缩放因子（焦距）。

```
- boolean setZoom(int distance)

```

**参数**

| 参数     | 类型 | 含义                                                         |
| :------- | :--- | :----------------------------------------------------------- |
| distance | int  | 取值范围：1 - 5 ，当为1的时候为最远视角（正常镜头），当为5的时候为最近视角（放大镜头），这里最大值推荐为5，超过5后视频数据会变得模糊不清。 |

------

<h3 id="enableTorch">enableTorch</h3>

开关闪光灯。

```
- boolean enableTorch(boolean enable)

```

**参数**

| 参数   | 类型    | 含义                      |
| :----- | :------ | :------------------------ |
| enable | boolean | true：开启；false：关闭。 |

------

<h3 id="setCameraMuteImage">setCameraMuteImage</h3>

主播屏蔽摄像头期间需要显示的等待图片。

```
- void setCameraMuteImage(Bitmap bitmap)

```

**参数**

| 参数   | 类型   | 含义   |
| :----- | :----- | :----- |
| bitmap | Bitmap | 位图。 |

**介绍**

当主播屏蔽摄像头，或者由于 App 切入后台无法使用摄像头的时候，我们需要使用一张等待图片来提示观众“主播暂时离开，请不要走开”。

------

<h3 id="setCameraMuteImage">setCameraMuteImage</h3>

主播屏蔽摄像头期间需要显示的等待图片。

```
- void setCameraMuteImage(final int id)

```

**参数**

| 参数 | 类型      | 含义                         |
| :--- | :-------- | :--------------------------- |
| id   | final int | 设置默认显示图片的资源文件。 |

**介绍**

当主播屏蔽摄像头，或者由于 App 切入后台无法使用摄像头的时候，我们需要使用一张等待图片来提示观众“主播暂时离开，请不要走开”。

## 美颜滤镜相关接口函数

<h3 id="getBeautyManager">getBeautyManager</h3>

获取美颜管理对象 TXBeautyManager。

```
public TXBeautyManager getBeautyManager()

```

**介绍**

通过美颜管理，您可以使用以下功能：

- 设置”美颜风格”、”美白”、“红润”、“大眼”、“瘦脸”、“V脸”、“下巴”、“短脸”、“小鼻”、“亮眼”、“白牙”、“祛眼袋”、“祛皱纹”、“祛法令纹”等美容效果。
- 调整“发际线”、“眼间距”、“眼角”、“嘴形”、“鼻翼”、“鼻子位置”、“嘴唇厚度”、“脸型”。
- 设置人脸挂件（素材）等动态效果。
- 添加美妆。
- 进行手势识别。

---

<h3 id="setWatermark">setWatermark</h3>

添加水印，height 不用设置，SDK 内部会根据水印宽高比自动计算 height。

```
- void setWatermark(Bitmap image, float x, float y, float width)

```

**参数**

| 参数  | 类型   | 含义                                    |
| :---- | :----- | :-------------------------------------- |
| image | Bitmap | 水印图片 null 表示清除水印。            |
| x     | float  | 归一化水印位置的 X 轴坐标，取值[0，1]。 |
| y     | float  | 归一化水印位置的 Y 轴坐标，取值[0，1]。 |
| width | float  | 归一化水印宽度，取值[0，1]。            |

------

----

<h3 id="setExposureCompensation">setExposureCompensation</h3>

调整曝光。

```
- void setExposureCompensation(float value)

```

**参数**

| 参数  | 类型  | 含义                                                         |
| :---- | :---- | :----------------------------------------------------------- |
| value | float | 曝光比例，表示该手机支持最大曝光调整值的比例，取值范围：-1 - 1。 负数表示调低曝光，-1是最小值；正数表示调高曝光，1是最大值；0表示不调整曝光。 |

------

## 消息发送接口函数

<h3 id="sendRoomTextMsg">sendRoomTextMsg</h3>

发送文本消息。

```
- void sendRoomTextMsg(String message, finalIMLVBLiveRoomListener.SendRoomTextMsgCallback callback)

```

**参数**

| 参数     | 类型                                               | 含义           |
| :------- | :------------------------------------------------- | :------------- |
| message  | String                                             | 文本消息。     |
| callback | finalIMLVBLiveRoomListener.SendRoomTextMsgCallback | 发送结果回调。 |

------

<h3 id="sendRoomCustomMsg">sendRoomCustomMsg</h3>

发送自定义文本消息。

```
- void sendRoomCustomMsg(String cmd, String message, finalIMLVBLiveRoomListener.SendRoomCustomMsgCallback callback)

```

**参数**

| 参数     | 类型                                                 | 含义                                               |
| :------- | :--------------------------------------------------- | :------------------------------------------------- |
| cmd      | String                                               | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message  | String                                               | 文本消息。                                         |
| callback | finalIMLVBLiveRoomListener.SendRoomCustomMsgCallback | 发送结果回调。                                     |

------

## 背景混音相关接口函数

<h3 id="playBGM">playBGM</h3>

播放背景音乐。

```
- boolean playBGM(String path)

```

**参数**

| 参数 | 类型   | 含义               |
| :--- | :----- | :----------------- |
| path | String | 背景音乐文件路径。 |

**返回**

true：播放成功；false：播放失败。

------

<h3 id="setBGMNofify">setBGMNofify</h3>

设置背景音乐的回调接口。

```
- void setBGMNofify(TXLivePusher.OnBGMNotify notify)

```

**参数**

| 参数   | 类型                     | 含义       |
| :----- | :----------------------- | :--------- |
| notify | TXLivePusher.OnBGMNotify | 回调接口。 |

---

<h3 id="stopBGM">stopBGM</h3>

停止播放背景音乐。

```
- void stopBGM()

```

------

<h3 id="pauseBGM">pauseBGM</h3>

暂停播放背景音乐。

```
- void pauseBGM()

```

------

<h3 id="resumeBGM">resumeBGM</h3>

继续播放背景音乐。

```
- void resumeBGM()

```

------

<h3 id="getBGMDuration">getBGMDuration</h3>

获取音乐文件总时长。

```
- int getBGMDuration(String path)

```

**参数**

| 参数 | 类型   | 含义                                                         |
| :--- | :----- | :----------------------------------------------------------- |
| path | String | 音乐文件路径，如果 path 为空，那么返回当前正在播放的 music 时长。 |

**返回**

成功返回时长，单位毫秒，失败返回-1。

------

<h3 id="setMicVolumeOnMixing">setMicVolumeOnMixing</h3>

设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小。

```
- void setMicVolumeOnMixing(int volume)

```

**参数**

| 参数   | 类型 | 含义                                       |
| :----- | :--- | :----------------------------------------- |
| volume | int  | 音量大小，100为正常音量，建议值为0 - 200。 |

------

<h3 id="setBGMVolume">setBGMVolume</h3>

设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小。

```
- void setBGMVolume(int volume)

```

**参数**

| 参数   | 类型 | 含义                                                         |
| :----- | :--- | :----------------------------------------------------------- |
| volume | int  | 音量大小，100为正常音量，建议值为0 - 200，如果需要调大背景音量可以设置更大的值。 |

------

<h3 id="setReverbType">setReverbType</h3>

设置混响效果。

```
- void setReverbType(int reverbType)

```

**参数**

| 参数       | 类型 | 含义                                                         |
| :--------- | :--- | :----------------------------------------------------------- |
| reverbType | int  | 混响类型，详见：<br> <li>TXLiveConstants#REVERB_TYPE_0（关闭混响）。<li>TXLiveConstants#REVERB_TYPE_1（KTV）。 <li>TXLiveConstants#REVERB_TYPE_2（小房间）。<li>TXLiveConstants#REVERB_TYPE_3（大会堂）。 <li>TXLiveConstants#REVERB_TYPE_4（低沉）。 <li>TXLiveConstants#REVERB_TYPE_5（洪亮）。 <li>TXLiveConstants#REVERB_TYPE_6（磁性）。 |

------

<h3 id="setVoiceChangerType">setVoiceChangerType</h3>

设置变声类型。

```
- void setVoiceChangerType(int voiceChangerType)

```

**参数**

| 参数             | 类型 | 含义                                                         |
| :--------------- | :--- | :----------------------------------------------------------- |
| voiceChangerType | int  | 变声类型，具体值请参考见 {@link TXLiveConstants} 中的 VOICECHANGER_TYPE_X 定义。 |

------

<h3 id="setBgmPitch">setBgmPitch</h3>

设置背景音乐的音调。

```
- void setBgmPitch(float pitch)

```

**参数**

| 参数  | 类型  | 含义                              |
| :---- | :---- | :-------------------------------- |
| pitch | float | 音调，0为正常音调，范围：-1 - 1。 |

**介绍**

该接口用于混音处理，例如将背景音乐与麦克风采集到的声音混合后播放。

---

<h3 id="setBGMPosition">setBGMPosition</h3>

设置变声类型。

```
- void setVoiceChangerType(int voiceChangerType)

```

**参数**

| 参数     | 类型 | 含义                           |
| :------- | :--- | :----------------------------- |
| position | int  | 背景音乐的播放位置，单位：ms。 |

**返回**

结果是否成功，true：成功；false：失败。



## 废弃项

<h3 id="setBeautyStyle">setBeautyStyle</h3>

设置美颜、美白、红润效果级别。

```
- boolean setBeautyStyle(int beautyStyle , int beautyLevel, int whitenessLevel, int ruddinessLevel)

```

**参数**

| 参数           | 类型 | 含义                                                         |
| :------------- | :--- | :----------------------------------------------------------- |
| beautyStyle    | int  | 美颜风格，三种美颜风格：0 ：光滑；1：自然；2：朦胧。         |
| beautyLevel    | int  | 美颜级别，取值范围 0 - 9； 0 表示关闭， 1 - 9值越大，效果越明显。 |
| whitenessLevel | int  | 美白级别，取值范围 0 - 9； 0 表示关闭， 1 - 9值越大，效果越明显。 |
| ruddinessLevel | int  | 红润级别，取值范围 0 - 9； 0 表示关闭， 1 - 9值越大，效果越明显。 |

----------

<h3 id="setFilter">setFilter</h3>

设置指定素材滤镜特效。

```
- void setFilter(Bitmap image)

```

**参数**

| 参数  | 类型   | 含义                                                      |
| :---- | :----- | :-------------------------------------------------------- |
| image | Bitmap | 指定素材，即颜色查找表图片。注意：**一定要用 png 格式**。 |

------

<h3 id="setFilterConcentration">setFilterConcentration</h3>

设置滤镜浓度。

```
- void setFilterConcentration(float concentration)

```

**参数**

| 参数          | 类型  | 含义                                      |
| :------------ | :---- | :---------------------------------------- |
| concentration | float | 从0到1，越大滤镜效果越明显，默认取值0.5。 |

------

<h3 id="setMotionTmpl">setMotionTmpl</h3>

设置动效贴图。

```
- void setMotionTmpl(String filePaht)

```

**参数**

| 参数     | 类型   | 含义               |
| :------- | :----- | :----------------- |
| filePaht | String | 动态贴图文件路径。 |

------

<h3 id="setGreenScreenFile">setGreenScreenFile</h3>

设置绿幕文件。

```
- boolean setGreenScreenFile(String file)

```

**参数**

| 参数 | 类型   | 含义                                                         |
| :--- | :----- | :----------------------------------------------------------- |
| file | String | 绿幕文件位置，支持两种方式： 1.资源文件放在 assets 目录，path 直接取文件名；2.path 取文件绝对路径。 |

**返回**

false：调用失败；true：调用成功。

**介绍**

目前图片支持 jpg/png，视频支持 mp4/3gp 等 Android 系统支持的格式。

>? API 要求18。

------

<h3 id="setEyeScaleLevel">setEyeScaleLevel</h3>

设置大眼效果。

```
- void setEyeScaleLevel(int level)

```

**参数**

| 参数  | 类型 | 含义                                                         |
| :---- | :--- | :----------------------------------------------------------- |
| level | int  | 大眼等级取值为 0 - 9。取值为0时代表关闭美颜效果。默认值：0。 |

---

<h3 id="setFaceVLevel">setFaceVLevel</h3>

设置 V 脸（特权版本有效，普通版本设置此参数无效）。

```
- void setEyeScaleLevel(int level)

```

**参数**

| 参数  | 类型 | 含义                                                      |
| :---- | :--- | :-------------------------------------------------------- |
| level | int  | V 脸级别取值范围 0 - 9。数值越大，效果越明显。默认值：0。 |

---

<h3 id="setFaceSlimLevel">setFaceSlimLevel</h3>

设置瘦脸效果。

```
- void setFaceSlimLevel(int level)
```

**参数**

| 参数  | 类型 | 含义                                                         |
| :---- | :--- | :----------------------------------------------------------- |
| level | int  | 瘦脸等级取值为 0 - 9。取值为0时代表关闭美颜效果。默认值：0。 |

---

<h3 id="setChinLevel">setChinLevel</h3>

设置下巴拉伸或收缩（特权版本有效，普通版本设置此参数无效）。

```
- void setChinLevel(int chinLevel)
```

**参数**

| 参数      | 类型 | 含义                                                         |
| :-------- | :--- | :----------------------------------------------------------- |
| chinLevel | int  | 下巴拉伸或收缩级别取值范围 -9 - 9。数值越大，拉伸越明显。默认值：0。 |

---

<h3 id="setNoseSlimLevel">setNoseSlimLevel</h3>

设置瘦鼻（特权版本有效，普通版本设置此参数无效）。

```
- void setNoseSlimLevel(int noseSlimLevel)
```

**参数**

| 参数          | 类型 | 含义                                                      |
| :------------ | :--- | :-------------------------------------------------------- |
| noseSlimLevel | int  | 瘦鼻级别取值范围 0 - 9。数值越大，效果越明显。默认值：0。 |

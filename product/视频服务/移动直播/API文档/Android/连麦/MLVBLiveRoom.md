__功能__

腾讯云视立方·移动直播 - 连麦直播间。

>! 后台接口限制并发为每秒100次请求，若您有高并发请求请提前 [联系我们](https://cloud.tencent.com/act/event/connect-service) 处理，避免影响服务调用。

__介绍__
    
基于腾讯云直播、云点播（VOD） 和即时通信（IM）三大 PAAS 服务组合而成，支持：

- 主播创建新的直播间开播，观众进入直播间观看。
- 主播和观众进行视频连麦互动。
- 两个不同房间的主播 PK 互动。
- 一个直播间都有一个不限制房间人数的聊天室，支持发送各种文本消息和自定义消息，自定义消息可用于实现弹幕、点赞和礼物。


连麦直播间（MLVBLiveRoom）是一个开源的 Class，依赖两个腾讯云的闭源 SDK：

- LiteAVSDK：使用了其中的 TXLivePusher 和 TXLivePlayer 两个组件，前者用于推流，后者用于拉流。
- IM SDK：使用 IM SDK 的 AVChatroom 用于实现直播聊天室的功能，同时，主播间的连麦流程也是依靠 IM 消息串联起来的。


参见文档：[直播连麦](https://cloud.tencent.com/document/product/454/14606)。



## SDK 基础函数

### sharedInstance

获取 [MLVBLiveRoom](https://cloud.tencent.com/document/product/454/34776) 单例对象。

```
MLVBLiveRoom sharedInstance(Context context)
```

__参数__

| 参数    | 类型    | 含义                                                         |
| ------- | ------- | ------------------------------------------------------------ |
| context | Context | Android 上下文，内部会转为 ApplicationContext 用于系统 API 调用。 |

__返回__

[MLVBLiveRoom](https://cloud.tencent.com/document/product/454/34776) 实例。

>?可以调用 [MLVBLiveRoom#destroySharedInstance()](https://cloud.tencent.com/document/product/454/34776#destroysharedinstance) 销毁单例对象。

***

### destroySharedInstance

销毁 [MLVBLiveRoom](https://cloud.tencent.com/document/product/454/34776) 单例对象。

```
void destroySharedInstance()
```

>?销毁实例后，外部缓存的 [MLVBLiveRoom](https://cloud.tencent.com/document/product/454/34776) 实例不能再使用，需要重新调用 [MLVBLiveRoom#sharedInstance(Context)](https://cloud.tencent.com/document/product/454/34776#sharedinstance) 获取新实例。

***

### setListener

设置回调接口。

```
abstract void setListener(IMLVBLiveRoomListener listener)
```

__参数__

| 参数     | 类型                                                         | 含义       |
| -------- | ------------------------------------------------------------ | ---------- |
| listener | [IMLVBLiveRoomListener](https://cloud.tencent.com/document/product/454/34777) | 回调接口。 |

__介绍__

您可以通过 [IMLVBLiveRoomListener](https://cloud.tencent.com/document/product/454/34777) 获得 [MLVBLiveRoom](https://cloud.tencent.com/document/product/454/34776) 的各种状态通知。

>?默认是在 Main Thread 中回调，如果需要自定义回调线程，可使用 [MLVBLiveRoom#setListenerHandler(Handler)](https://cloud.tencent.com/document/product/454/34776#setlistenerhandler)。

***

### setListenerHandler

设置驱动回调的线程。

```
abstract void setListenerHandler(Handler listenerHandler)
```

__参数__

| 参数            | 类型    | 含义   |
| --------------- | ------- | ------ |
| listenerHandler | Handler | 线程。 |

***

### login

登录。

```
abstract void login(final LoginInfo loginInfo, final IMLVBLiveRoomListener.LoginCallback callback)
```

__参数__

| 参数      | 类型                                                         | 含义           |
| --------- | ------------------------------------------------------------ | -------------- |
| loginInfo | final LoginInfo                                              | 登录信息。     |
| callback  | [final IMLVBLiveRoomListener.LoginCallback](https://cloud.tencent.com/document/product/454/34777#logincallback) | 登录结果回调。 |

***

### logout

退出登录。

```
abstract void logout()
```

***

### setSelfProfile

修改个人信息。

```
abstract void setSelfProfile(String userName, String avatarURL)
```

__参数__

| 参数      | 类型   | 含义       |
| --------- | ------ | ---------- |
| userName  | String | 昵称。     |
| avatarURL | String | 头像地址。 |

***


## 房间相关接口函数

### getRoomList

获取房间列表。

```
abstract void getRoomList(int index, int count, final IMLVBLiveRoomListener.GetRoomListCallback callback)
```

__参数__

| 参数     | 类型                                                         | 含义                        |
| -------- | ------------------------------------------------------------ | --------------------------- |
| index    | int                                                          | 房间开始索引，从0开始计算。 |
| count    | int                                                          | 希望后台返回的房间个数。    |
| callback | [final IMLVBLiveRoomListener.GetRoomListCallback](https://cloud.tencent.com/document/product/454/34777#getroomlistcallback) | 获取房间列表的结果回调。    |

__介绍__

该接口支持分页获取房间列表，可以用 index 和 count 两个参数控制列表分页的逻辑：

- index = 0 & count = 10 代表获取第一页的10个房间。
- index = 11 & count = 10 代表获取第二页的10个房间。

***

### getAudienceList

获取观众列表。

```
abstract void getAudienceList(IMLVBLiveRoomListener.GetAudienceListCallback callback)
```

__参数__

| 参数     | 类型                                                         | 含义                     |
| -------- | ------------------------------------------------------------ | ------------------------ |
| callback | [IMLVBLiveRoomListener.GetAudienceListCallback](https://cloud.tencent.com/document/product/454/34777#getaudiencelistcallback) | 获取观众列表的结果回调。 |

__介绍__

当有观众进房时，后台会将其信息加入到指定房间的观众列表中，调入该函数即可返回指定房间的观众列表。

>?观众列表最多只保存30人，因为对于常规的 UI 展示来说这已经足够，保存更多除了浪费存储空间，也会拖慢列表返回的速度。

***

### createRoom

创建房间（主播调用）。

```
abstract void createRoom(final String roomID, final String roomInfo, final IMLVBLiveRoomListener.CreateRoomCallback callback)
```

__参数__

| 参数     | 类型                                                         | 含义                                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| roomID   | final String                                                 | 房间标识，推荐做法是用主播的 userID 作为房间的 roomID，这样省去了后台映射的成本。roomID 可以填空，此时由后台生成。 |
| roomInfo | final String                                                 | 房间信息（非必填），用于房间描述的信息，如房间名称，允许使用 JSON 格式作为房间信息。 |
| callback | [final IMLVBLiveRoomListener.CreateRoomCallback](https://cloud.tencent.com/document/product/454/34777#createroomcallback) | 创建房间的结果回调。                                         |

__介绍__

主播开播的正常调用流程是： 

1. 主播调用 [startLocalPreview()](https://cloud.tencent.com/document/product/454/34776#startlocalpreview) 打开摄像头预览，此时可以调整美颜参数。 
2. 主播调用 createRoom 创建直播间，房间创建成功与否会通过 [IMLVBLiveRoomListener.CreateRoomCallback](https://cloud.tencent.com/document/product/454/34777#createroomcallback) 通知给主播。

***

### enterRoom

进入房间（观众调用）。

```
abstract void enterRoom(final String roomID, final TXCloudVideoView view, final IMLVBLiveRoomListener.EnterRoomCallback callback)
```

__参数__

| 参数     | 类型                                                         | 含义                 |
| -------- | ------------------------------------------------------------ | -------------------- |
| roomID   | final String                                                 | 房间标识。           |
| view     | final TXCloudVideoView                                       | 承载视频画面的控件。 |
| callback | [final IMLVBLiveRoomListener.EnterRoomCallback](https://cloud.tencent.com/document/product/454/34777#enterroomcallback) | 进入房间的结果回调。 |

__介绍__

观众观看直播的正常调用流程是： 

1. 观众调用 [getRoomList()](https://cloud.tencent.com/document/product/454/34776#getroomlist) 刷新最新的直播房间列表，并通过 [IMLVBLiveRoomListener.GetRoomListCallback](https://cloud.tencent.com/document/product/454/34777#getroomlistcallback) 回调拿到房间列表。 
2. 观众选择一个直播间以后，调用 [enterRoom()](https://cloud.tencent.com/document/product/454/34776#enterroom) 进入该房间。

***

### exitRoom

离开房间。

```
abstract void exitRoom(IMLVBLiveRoomListener.ExitRoomCallback callback)
```

__参数__

| 参数     | 类型                                                         | 含义                 |
| -------- | ------------------------------------------------------------ | -------------------- |
| callback | [IMLVBLiveRoomListener.ExitRoomCallback](https://cloud.tencent.com/document/product/454/34777#exitroomcallback) | 离开房间的结果回调。 |

***

### setCustomInfo

设置自定义信息。

```
abstract void setCustomInfo(final MLVBCommonDef.CustomFieldOp op, final String key, final Object value, final IMLVBLiveRoomListener.SetCustomInfoCallback callback)
```

__参数__

| 参数     | 类型                                                         | 含义                                               |
| -------- | ------------------------------------------------------------ | -------------------------------------------------- |
| op       | final MLVBCommonDef.CustomFieldOp                            | 执行动作，定义请查看 MLVBCommonDef.CustomFieldOp。 |
| key      | final String                                                 | 自定义键。                                         |
| value    | final Object                                                 | 数值。                                             |
| callback | [final IMLVBLiveRoomListener.SetCustomInfoCallback](https://cloud.tencent.com/document/product/454/34777#setcustominfocallback) | 设置自定义信息完成的回调。                         |

__介绍__

有时候您可能需要为房间产生一些额外的信息，此接口可以将这些信息缓存到服务器。

>?
>
>- op 为 MLVBCommonDef.CustomFieldOp#SET 时，value 可以是 String 或者 Integer 类型。
>- op 为 MLVBCommonDef.CustomFieldOp#INC 时，value 是 Integer 类型。
>- op 为 MLVBCommonDef.CustomFieldOp#DEC 时，value 是 Integer 类型。

***

### getCustomInfo

获取自定义信息。

```
abstract void getCustomInfo(final IMLVBLiveRoomListener.GetCustomInfoCallback callback)
```

__参数__

| 参数     | 类型                                                         | 含义                 |
| -------- | ------------------------------------------------------------ | -------------------- |
| callback | [final IMLVBLiveRoomListener.GetCustomInfoCallback](https://cloud.tencent.com/document/product/454/34777#getcustominfocallback) | 获取自定义信息回调。 |

***


## 主播和观众连麦

### requestJoinAnchor

观众请求连麦。

```
abstract void requestJoinAnchor(String reason, IMLVBLiveRoomListener.RequestJoinAnchorCallback callback)
```

__参数__

| 参数     | 类型                                                         | 含义             |
| -------- | ------------------------------------------------------------ | ---------------- |
| reason   | String                                                       | 连麦原因。       |
| callback | [IMLVBLiveRoomListener.RequestJoinAnchorCallback](https://cloud.tencent.com/document/product/454/34777#requestjoinanchorcallback) | 请求连麦的回调。 |

__介绍__

主播和观众的连麦流程可以简单描述为如下几个步骤：

1. 观众调用 [requestJoinAnchor()](https://cloud.tencent.com/document/product/454/34776#requestjoinanchor) 向主播发起连麦请求。
2. 主播会收到 [IMLVBLiveRoomListener#onRequestJoinAnchor(AnchorInfo， String)](https://cloud.tencent.com/document/product/454/34777#onrequestjoinanchor) 的回调通知。
3. 主播调用 [responseJoinAnchor()](https://cloud.tencent.com/document/product/454/34776#responsejoinanchor) 确定是否接受观众的连麦请求。
4. 观众会收到 [IMLVBLiveRoomListener.RequestJoinAnchorCallback](https://cloud.tencent.com/document/product/454/34777#requestjoinanchorcallback) 回调通知，可以得知请求是否被同意。
5. 观众如果请求被同意，则调用 [startLocalPreview()](https://cloud.tencent.com/document/product/454/34776#startlocalpreview) 开启本地摄像头，如果 App 还没有取得摄像头和麦克风权限，会触发 UI 提示。
6. 观众然后调用 [joinAnchor()](https://cloud.tencent.com/document/product/454/34776#joinanchor) 正式进入连麦状态。
7. 主播一旦观众进入连麦状态，主播就会收到 [IMLVBLiveRoomListener#onAnchorEnter(AnchorInfo)](https://cloud.tencent.com/document/product/454/34777#onanchorenter) 通知。
8. 主播调用 [startRemoteView()](https://cloud.tencent.com/document/product/454/34776#startremoteview) 就可以看到连麦观众的视频画面。
9. 观众如果直播间里已经有其他观众正在跟主播进行连麦，那么新加入的这位连麦观众也会收到 onAnchorJoin() 通知，用于展示（startRemoteView）其他连麦者的视频画面。

***

### responseJoinAnchor

主播处理连麦请求。

```
abstract int responseJoinAnchor(String userID, boolean agree, String reason)
```

__参数__

| 参数   | 类型    | 含义                      |
| ------ | ------- | ------------------------- |
| userID | String  | 观众ID。                  |
| agree  | boolean | true：同意；false：拒绝。 |
| reason | String  | 同意/拒绝连麦的原因描述。 |

__返回__

0：响应成功；非0：响应失败。

__介绍__

主播在收到 [IMLVBLiveRoomListener#onRequestJoinAnchor(AnchorInfo， String)](https://cloud.tencent.com/document/product/454/34777#onrequestjoinanchor) 回调之后会需要调用此接口来处理观众的连麦请求。

***

### joinAnchor

进入连麦状态。

```
abstract void joinAnchor(final IMLVBLiveRoomListener.JoinAnchorCallback callback)
```

__参数__

| 参数     | 类型                                                         | 含义                 |
| -------- | ------------------------------------------------------------ | -------------------- |
| callback | [final IMLVBLiveRoomListener.JoinAnchorCallback](https://cloud.tencent.com/document/product/454/34777#joinanchorcallback) | 进入连麦的结果回调。 |

__介绍__

进入连麦成功后，主播和其他连麦观众会收到 [IMLVBLiveRoomListener#onAnchorEnter(AnchorInfo)](https://cloud.tencent.com/document/product/454/34777#onanchorenter) 通知。

***

### quitJoinAnchor

观众退出连麦。

```
abstract void quitJoinAnchor(final IMLVBLiveRoomListener.QuitAnchorCallback callback)
```

__参数__

| 参数     | 类型                                                         | 含义                 |
| -------- | ------------------------------------------------------------ | -------------------- |
| callback | [final IMLVBLiveRoomListener.QuitAnchorCallback](https://cloud.tencent.com/document/product/454/34777#quitanchorcallback) | 退出连麦的结果回调。 |

__介绍__

退出连麦成功后，主播和其他连麦观众会收到 [IMLVBLiveRoomListener#onAnchorExit(AnchorInfo)](https://cloud.tencent.com/document/product/454/34777#onanchorexit) 通知。

***

### kickoutJoinAnchor

主播踢除连麦观众。

```
abstract void kickoutJoinAnchor(String userID)
```

__参数__

| 参数   | 类型   | 含义          |
| ------ | ------ | ------------- |
| userID | String | 连麦观众 ID。 |

__介绍__

主播调用此接口踢除连麦观众后，被踢连麦观众会收到 [IMLVBLiveRoomListener#onKickoutJoinAnchor()](https://cloud.tencent.com/document/product/454/34777#onkickoutjoinanchor) 回调通知。

***


## 主播跨房间 PK

### requestRoomPK

请求跨房 PK。

```
abstract void requestRoomPK(String userID, final IMLVBLiveRoomListener.RequestRoomPKCallback callback)
```

__参数__

| 参数     | 类型                                                         | 含义                     |
| -------- | ------------------------------------------------------------ | ------------------------ |
| userID   | String                                                       | 被邀约主播 ID。          |
| callback | [final IMLVBLiveRoomListener.RequestRoomPKCallback](https://cloud.tencent.com/document/product/454/34777#requestroompkcallback) | 请求跨房 PK 的结果回调。 |

__介绍__

主播和主播之间可以跨房间 PK，两个正在直播中的主播 A 和 B，他们之间的跨房 PK 流程如下：

1. 主播 A 调用 [requestRoomPK()](https://cloud.tencent.com/document/product/454/34776#requestroompk) 向主播 B 发起连麦请求。
2. 主播 B 会收到 [IMLVBLiveRoomListener#onRequestRoomPK(AnchorInfo)](https://cloud.tencent.com/document/product/454/34777#onrequestroompk) 回调通知。
3. 主播 B 调用 [responseRoomPK()](https://cloud.tencent.com/document/product/454/34776#responseroompk) 确定是否接受主播 A 的 PK 请求。
4. 主播 B 如果接受了主播 A 的要求，可以直接调用 [startRemoteView()](https://cloud.tencent.com/document/product/454/34776#startremoteview) 来显示主播 A 的视频画面。
5. 主播 A 会收到 [IMLVBLiveRoomListener.RequestRoomPKCallback](https://cloud.tencent.com/document/product/454/34777#requestroompkcallback) 回调通知，可以得知请求是否被同意。
6. 主播 A 如果请求被同意，则可以调用 [startRemoteView()](https://cloud.tencent.com/document/product/454/34776#startremoteview) 显示主播 B 的视频画面。

***

### responseRoomPK

响应跨房 PK 请求。

```
abstract int responseRoomPK(String userID, boolean agree, String reason)
```

__参数__

| 参数   | 类型    | 含义                      |
| ------ | ------- | ------------------------- |
| userID | String  | 发起 PK 请求的主播 ID。   |
| agree  | boolean | true：同意；false：拒绝。 |
| reason | String  | 同意/拒绝 PK 的原因描述。 |

__返回__

0：响应成功；非0：响应失败。

__介绍__

主播响应其他房间主播的 PK 请求，发起 PK 请求的主播会收到 [IMLVBLiveRoomListener.RequestRoomPKCallback](https://cloud.tencent.com/document/product/454/34777#requestroompkcallback) 回调通知。

***

### quitRoomPK

退出跨房 PK。

```
abstract void quitRoomPK(final IMLVBLiveRoomListener.QuitRoomPKCallback callback)
```

__参数__

| 参数     | 类型                                                         | 含义                     |
| -------- | ------------------------------------------------------------ | ------------------------ |
| callback | [final IMLVBLiveRoomListener.QuitRoomPKCallback](https://cloud.tencent.com/document/product/454/34777#quitroompkcallback) | 退出跨房 PK 的结果回调。 |

__介绍__

当两个主播中的任何一个退出跨房 PK 状态后，另一个主播会收到 [IMLVBLiveRoomListener#onQuitRoomPK(AnchorInfo)](https://cloud.tencent.com/document/product/454/34777#onquitroompk) 回调通知。

***


## 视频相关接口函数

### startLocalPreview

开启本地视频的预览画面。

```
abstract void startLocalPreview(boolean frontCamera, TXCloudVideoView view)
```

__参数__

| 参数        | 类型             | 含义                              |
| ----------- | ---------------- | --------------------------------- |
| frontCamera | boolean          | YES：前置摄像头；NO：后置摄像头。 |
| view        | TXCloudVideoView | 承载视频画面的控件。              |

***

### stopLocalPreview

停止本地视频采集及预览。

```
abstract void stopLocalPreview()
```

***

### startRemoteView

启动渲染远端视频画面。

```
abstract void startRemoteView(final AnchorInfo anchorInfo, final TXCloudVideoView view, final IMLVBLiveRoomListener.PlayCallback callback)
```

__参数__

| 参数       | 类型                                                         | 含义                 |
| ---------- | ------------------------------------------------------------ | -------------------- |
| anchorInfo | final AnchorInfo                                             | 对方的用户信息。     |
| view       | final TXCloudVideoView                                       | 承载视频画面的控件。 |
| callback   | [final IMLVBLiveRoomListener.PlayCallback](https://cloud.tencent.com/document/product/454/34777#playcallback) | 播放器监听器。       |

>?在 onUserVideoAvailable 回调时，调用这个接口。

***

### stopRemoteView

停止渲染远端视频画面。

```
abstract void stopRemoteView(final AnchorInfo anchorInfo)

```

__参数__

| 参数       | 类型             | 含义             |
| ---------- | ---------------- | ---------------- |
| anchorInfo | final AnchorInfo | 对方的用户信息。 |

***

### startScreenCapture

启动录屏。

```
abstract void startScreenCapture()

```

***

### stopScreenCapture

结束录屏。

```
abstract void stopScreenCapture()

```

***


## 音频相关接口函数

### muteLocalAudio

是否屏蔽本地音频。

```
abstract void muteLocalAudio(boolean mute)

```

__参数__

| 参数 | 类型    | 含义                      |
| ---- | ------- | ------------------------- |
| mute | boolean | true：屏蔽；false：开启。 |

***

### muteRemoteAudio

设置指定用户是否静音。

```
abstract void muteRemoteAudio(String userID, boolean mute)
```

__参数__

| 参数   | 类型    | 含义                        |
| ------ | ------- | --------------------------- |
| userID | String  | 对方的用户标识。            |
| mute   | boolean | true：静音；false：非静音。 |

***

### muteAllRemoteAudio

设置所有远端用户是否静音。

```
abstract void muteAllRemoteAudio(boolean mute)
```

__参数__

| 参数 | 类型    | 含义                        |
| ---- | ------- | --------------------------- |
| mute | boolean | true：静音；false：非静音。 |

***


## 摄像头相关接口函数

### switchCamera

切换摄像头。

```
abstract void switchCamera()
```

***

### setZoom

设置摄像头缩放因子（焦距）。

```
abstract boolean setZoom(int distance)
```

__参数__

| 参数     | 类型 | 含义                                                         |
| -------- | ---- | ------------------------------------------------------------ |
| distance | int  | 取值范围：1 - 5 ，当为1的时候为最远视角（正常镜头），当为5的时候为最近视角（放大镜头），这里最大值推荐为5，超过5后视频数据会变得模糊不清。 |

***

### enableTorch

开关闪光灯。

```
abstract boolean enableTorch(boolean enable)
```

__参数__

| 参数   | 类型    | 含义                      |
| ------ | ------- | ------------------------- |
| enable | boolean | true：开启；false：关闭。 |

***

### setCameraMuteImage

主播屏蔽摄像头期间需要显示的等待图片。

```
abstract void setCameraMuteImage(Bitmap bitmap)
```

__参数__

| 参数   | 类型   | 含义   |
| ------ | ------ | ------ |
| bitmap | Bitmap | 位图。 |

__介绍__

当主播屏蔽摄像头，或者由于 App 切入后台无法使用摄像头的时候，我们需要使用一张等待图片来提示观众“主播暂时离开，请不要走开”。

***

### setCameraMuteImage

主播屏蔽摄像头期间需要显示的等待图片。

```
abstract void setCameraMuteImage(final int id)
```

__参数__

| 参数 | 类型      | 含义                         |
| ---- | --------- | ---------------------------- |
| id   | final int | 设置默认显示图片的资源文件。 |

__介绍__

当主播屏蔽摄像头，或者由于 App 切入后台无法使用摄像头的时候，我们需要使用一张等待图片来提示观众“主播暂时离开，请不要走开”。

***


## 美颜滤镜相关接口函数

### getBeautyManager

获取美颜管理对象 [TXBeautyManager](https://cloud.tencent.com/document/product/454/39379)。

```
public TXBeautyManager getBeautyManager()
```

通过美颜管理，您可以使用以下功能：

- 设置”美颜风格”、”美白”、“红润”、“大眼”、“瘦脸”、“V脸”、“下巴”、“短脸”、“小鼻”、“亮眼”、“白牙”、“祛眼袋”、“祛皱纹”、“祛法令纹”等美容效果。
- 调整“发际线”、“眼间距”、“眼角”、“嘴形”、“鼻翼”、“鼻子位置”、“嘴唇厚度”、“脸型”。
- 设置人脸挂件（素材）等动态效果。
- 添加美妆。
- 进行手势识别。

***


### setFilter

设置指定素材滤镜特效。

```
abstract void setFilter(Bitmap image)
```

__参数__

| 参数  | 类型   | 含义                                                      |
| ----- | ------ | --------------------------------------------------------- |
| image | Bitmap | 指定素材，即颜色查找表图片。注意：**一定要用 png 格式**。 |

***

### setFilterConcentration

设置滤镜浓度。

```
abstract void setFilterConcentration(float concentration)
```

__参数__

| 参数          | 类型  | 含义                                      |
| ------------- | ----- | ----------------------------------------- |
| concentration | float | 从0到1，越大滤镜效果越明显，默认取值0.5。 |

***

### setWatermark

添加水印，height 不用设置，SDK 内部会根据水印宽高比自动计算 height。

```
abstract void setWatermark(Bitmap image, float x, float y, float width)
```

__参数__

| 参数  | 类型   | 含义                                    |
| ----- | ------ | --------------------------------------- |
| image | Bitmap | 水印图片 null 表示清除水印。            |
| x     | float  | 归一化水印位置的 X 轴坐标，取值[0，1]。 |
| y     | float  | 归一化水印位置的 Y 轴坐标，取值[0，1]。 |
| width | float  | 归一化水印宽度，取值[0，1]。            |

***

### setGreenScreenFile

设置绿幕文件。

```
abstract boolean setGreenScreenFile(String file)
```

__参数__

| 参数 | 类型   | 含义                                                         |
| ---- | ------ | ------------------------------------------------------------ |
| file | String | 绿幕文件位置，支持两种方式： 1.资源文件放在 assets 目录，path 直接取文件名；2.path 取文件绝对路径。 |

__返回__

false：调用失败；true：调用成功。

__介绍__

目前图片支持 jpg/png，视频支持 mp4/3gp 等 Android 系统支持的格式。

>?API 要求18。

***

### setExposureCompensation

调整曝光。

```
abstract void setExposureCompensation(float value)
```

__参数__

| 参数  | 类型  | 含义                                                         |
| ----- | ----- | ------------------------------------------------------------ |
| value | float | 曝光比例，表示该手机支持最大曝光调整值的比例，取值范围：-1 - 1。 负数表示调低曝光，-1是最小值；正数表示调高曝光，1是最大值；0表示不调整曝光。 |

***


## 消息发送接口函数

### sendRoomTextMsg

发送文本消息。

```
abstract void sendRoomTextMsg(String message, final IMLVBLiveRoomListener.SendRoomTextMsgCallback callback)
```

__参数__

| 参数     | 类型                                                         | 含义           |
| -------- | ------------------------------------------------------------ | -------------- |
| message  | String                                                       | 文本消息。     |
| callback | [final IMLVBLiveRoomListener.SendRoomTextMsgCallback](https://cloud.tencent.com/document/product/454/34777#sendroomtextmsgcallback) | 发送结果回调。 |

***

### sendRoomCustomMsg

发送自定义文本消息。

```
abstract void sendRoomCustomMsg(String cmd, String message, final IMLVBLiveRoomListener.SendRoomCustomMsgCallback callback)
```

__参数__

| 参数     | 类型                                                         | 含义                                               |
| -------- | ------------------------------------------------------------ | -------------------------------------------------- |
| cmd      | String                                                       | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message  | String                                                       | 文本消息。                                         |
| callback | [final IMLVBLiveRoomListener.SendRoomCustomMsgCallback](https://cloud.tencent.com/document/product/454/34777#sendroomcustommsgcallback) | 发送结果回调。                                     |

***


## 背景混音相关接口函数

### playBGM

播放背景音乐。

```
abstract boolean playBGM(String path)
```

__参数__

| 参数 | 类型   | 含义               |
| ---- | ------ | ------------------ |
| path | String | 背景音乐文件路径。 |

__返回__

true：播放成功；false：播放失败。

***

### stopBGM

停止播放背景音乐。

```
abstract void stopBGM()
```

***

### pauseBGM

暂停播放背景音乐。

```
abstract void pauseBGM()
```

***

### resumeBGM

继续播放背景音乐。

```
abstract void resumeBGM()
```

***

### getBGMDuration

获取音乐文件总时长。

```
abstract int getBGMDuration(String path)
```

__参数__

| 参数 | 类型   | 含义                                                         |
| ---- | ------ | ------------------------------------------------------------ |
| path | String | 音乐文件路径，如果 path 为空，那么返回当前正在播放的 music 时长。 |

__返回__

成功返回时长，单位毫秒，失败返回-1。

***

### setMicVolumeOnMixing

设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小。

```
abstract void setMicVolumeOnMixing(int volume)
```

__参数__

| 参数   | 类型 | 含义                                       |
| ------ | ---- | ------------------------------------------ |
| volume | int  | 音量大小，100为正常音量，建议值为0 - 200。 |

***

### setBGMVolume

设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小。

```
abstract void setBGMVolume(int volume)
```

__参数__

| 参数   | 类型 | 含义                                                         |
| ------ | ---- | ------------------------------------------------------------ |
| volume | int  | 音量大小，100为正常音量，建议值为0 - 200，如果需要调大背景音量可以设置更大的值。 |

***

### setReverbType

设置混响效果。

```
abstract void setReverbType(int reverbType)
```

__参数__

| 参数       | 类型 | 含义                                                         |
| ---------- | ---- | ------------------------------------------------------------ |
| reverbType | int  | 混响类型，详见： <br>TXLiveConstants#REVERB_TYPE_0（关闭混响）。<br> TXLiveConstants#REVERB_TYPE_1（KTV）。 <br>TXLiveConstants#REVERB_TYPE_2（小房间）。<br> TXLiveConstants#REVERB_TYPE_3（大会堂）。<br> TXLiveConstants#REVERB_TYPE_4（低沉）。<br> TXLiveConstants#REVERB_TYPE_5（洪亮）。<br>TXLiveConstants#REVERB_TYPE_6（磁性）。 |

***

### setVoiceChangerType

设置变声类型。

```
abstract void setVoiceChangerType(int voiceChangerType)
```

__参数__

| 参数             | 类型 | 含义                                |
| ---------------- | ---- | ----------------------------------- |
| voiceChangerType | int  | 变声类型，详见 TXVoiceChangerType。 |

***

### setBgmPitch

设置背景音乐的音调。

```
abstract void setBgmPitch(float pitch)
```

__参数__

| 参数  | 类型  | 含义                              |
| ----- | ----- | --------------------------------- |
| pitch | float | 音调，0为正常音调，范围：-1 - 1。 |

__介绍__

该接口用于混音处理，例如将背景音乐与麦克风采集到的声音混合后播放。

***

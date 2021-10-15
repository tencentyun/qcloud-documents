__功能__

腾讯云视立方·移动直播 - 连麦直播间。

>! 后台接口限制并发为每秒100次请求，若您有高并发请求请提前 [联系我们](https://cloud.tencent.com/act/event/connect-service) 处理，避免影响服务调用。

__介绍__

基于腾讯云直播、点播（VOD） 和即时通信（IM）三大 PAAS 服务组合而成，支持：

- 主播创建新的直播间开播，观众进入直播间观看。
- 主播和观众进行视频连麦互动。
- 两个不同房间的主播 PK 互动。
- 每一个直播间都有一个不限制房间人数的聊天室，支持发送各种文本消息和自定义消息，自定义消息可用于实现弹幕、点赞和礼物。


连麦直播间（MLVBLiveRoom）是一个开源的 Class，依赖两个腾讯云的闭源 SDK：

- LiteAVSDK：使用了其中的 TXLivePusher 和 [TXLivePlayer](https://cloud.tencent.com/document/product/454/34762) 两个组件，前者用于推流，后者用于拉流。
- IM SDK：使用 IM SDK 的 AVChatroom 用于实现直播聊天室的功能，同时，主播间的连麦流程也是依靠 IM 消息串联起来的。


请参见 [直播连麦（LiveRoom）](https://cloud.tencent.com/document/product/454/14606)。



## SDK 基础函数

### delegate

MLVBLiveRoom 事件回调，您可以通过 MLVBLiveRoomDelegate 获得 MLVBLiveRoom 的各种状态通知。

```
@property (nonatomic, weak) id< MLVBLiveRoomDelegate > delegate
```

>?默认是在 Main Queue 中回调，如果需要自定义回调线程，可使用 delegateQueue。

***

### delegateQueue

设置驱动回调函数的 GCD 队列。

```
@property (nonatomic, copy) dispatch_queue_t delegateQueue
```

***

### sharedInstance

获取 MLVBLiveRoom 单例对象。

```
+ (instancetype)sharedInstance
```

__返回__

MLVBLiveRoom 实例。

>?可以调用 MLVBLiveRoom destroySharedInstance 销毁单例对象。

***

### destorySharedInstance

销毁 MLVBLiveRoom 单例对象。

```
+ (void)destorySharedInstance
```

>?销毁实例后，外部缓存的 MLVBLiveRoom 实例不能再使用，需要重新调用 [sharedInstance](https://cloud.tencent.com/document/product/454/34763#sharedinstance) 获取新实例。

***

### loginWithInfo

登录。

```
- (void)loginWithInfo:(MLVBLoginInfo *)loginInfo completion:(void(^)(int errCode, NSString *errMsg))completion 
```

__参数__

| 参数       | 类型                                   | 含义           |
| ---------- | -------------------------------------- | -------------- |
| loginInfo  | MLVBLoginInfo *                        | 登录信息。     |
| completion | void(^)(int errCode, NSString *errMsg) | 登录结果回调。 |

***

### logout

登出。

```
- (void)logout
```

***

### setSelfProfile

修改个人信息。

```
- (void)setSelfProfile:(NSString *)userName avatarURL:(NSString *)avatarURL completion:(void(^)(int code, NSString *msg))completion 
```

__参数__

| 参数      | 类型       | 含义       |
| --------- | ---------- | ---------- |
| userName  | NSString * | 昵称。     |
| avatarURL | NSString * | 头像地址。 |
| completion | (void(^)(int code, NSString *msg)) | 修改结果回调。 |

***


## 房间相关接口函数

### getRoomList

获取房间列表。

```
- (void)getRoomList:(int)index count:(int)count completion:(void(^)(int errCode, NSString *errMsg, NSArray< MLVBRoomInfo * > *roomInfoArray))completion 
```

__参数__

| 参数       | 类型                                                         | 含义                        |
| ---------- | ------------------------------------------------------------ | --------------------------- |
| index      | int                                                          | 房间开始索引，从0开始计算。 |
| count      | int                                                          | 希望后台返回的房间个数。    |
| completion | void(^)(int errCode, NSString *errMsg, NSArray< MLVBRoomInfo * > *roomInfoArray) | 获取房间列表的结果回调。    |

__介绍__

该接口支持分页获取房间列表，可以用 index 和 count 两个参数控制列表分页的逻辑，

- index = 0 & count = 10代表获取第一页的10个房间。
- index = 11 & count = 10代表获取第二页的10个房间。

***

### getAudienceList

获取观众列表。

```
- (void)getAudienceList:(NSString *)roomID completion:(void(^)(int errCode, NSString *errMsg, NSArray< MLVBAudienceInfo * > *audienceInfoArray))completion 

```

__参数__

| 参数       | 类型                                                         | 含义                     |
| ---------- | ------------------------------------------------------------ | ------------------------ |
| roomID     | NSString *                                                   | 房间标识。               |
| completion | void(^)(int errCode, NSString *errMsg, NSArray< MLVBAudienceInfo * > *audienceInfoArray) | 获取观众列表的结果回调。 |

__介绍__

当有观众进房时，后台会将其信息加入到指定房间的观众列表中，调入该函数即可返回指定房间的观众列表。

>?观众列表最多只保存30人，因为对于常规的 UI 展示来说这已经足够，保存更多除了浪费存储空间，也会拖慢列表返回的速度。

***

### createRoom

创建房间（主播调用）。

```
- (void)createRoom:(NSString *)roomID roomInfo:(NSString *)roomInfo completion:(void(^)(int errCode, NSString *errMsg))completion 

```

__参数__

| 参数       | 类型                                   | 含义                                                         |
| ---------- | -------------------------------------- | ------------------------------------------------------------ |
| roomID     | NSString *                             | 房间标识，推荐做法是用主播的 userID 作为房间的 roomID，这样省去了后台映射的成本。room ID 可以填空，此时由后台生成。 |
| roomInfo   | NSString *                             | 房间信息（非必填），用于房间描述的信息，如房间名称，允许使用 JSON 格式作为房间信息。 |
| completion | void(^)(int errCode, NSString *errMsg) | 创建房间的结果回调。                                         |

__介绍__

主播开播的正常调用流程是： 

1. 主播调用 startLocalPreview 打开摄像头预览，此时可以调整美颜参数。 
2. 主播调用 createRoom 创建直播间，房间创建成功与否会通过 completion 通知主播。

***

### enterRoom

进入房间（观众调用）。

```
- (void)enterRoom:(NSString *)roomID view:(UIView *)view completion:(void(^)(int errCode, NSString *errMsg))completion 

```

__参数__

| 参数       | 类型                                   | 含义                 |
| ---------- | -------------------------------------- | -------------------- |
| roomID     | NSString *                             | 房间标识。           |
| view       | UIView *                               | 承载视频画面的控件。 |
| completion | void(^)(int errCode, NSString *errMsg) | 进入房间的结果回调。 |

__介绍__

观众观看直播的正常调用流程是： 

1. 观众调用 getRoomList  刷新最新的直播房间列表，并通过 completion 回调拿到房间列表。 
2. 观众选择一个直播间以后，调用 enterRoom  进入该房间。

***

### exitRoom

离开房间。

```
- (void)exitRoom:(void(^)(int errCode, NSString *errMsg))completion 

```

__参数__

| 参数       | 类型                                   | 含义                 |
| ---------- | -------------------------------------- | -------------------- |
| completion | void(^)(int errCode, NSString *errMsg) | 离开房间的结果回调。 |

***

### setCustomInfo

设置当前房间的扩展信息字段。

```
- (void)setCustomInfo:(MLVBCustomFieldOp)op key:(NSString *)key value:(id)value completion:(void(^)(int errCode, NSString *custom))completion 

```

__参数__

| 参数       | 类型                                   | 含义                                |
| ---------- | -------------------------------------- | ----------------------------------- |
| op         | MLVBCustomFieldOp                      | 执行动作。                          |
| key        | NSString *                             | 自定义键。                          |
| value      | id                                     | 可选类型为 NSNumber 或者 NSString。 |
| completion | void(^)(int errCode, NSString *custom) | 操作完成的回调。                    |

__介绍__

有时候您需要为当前房间设置一些扩展字段，如“点赞人数”和“是否正在连麦”等，这些字段我们很难全都预先定义好，所以提供了如下三种操作接口：

- SET：设置，value 可以是数值或者字符串，例如“是否正在连麦”等。
- INC：增加，value 只能是整数，如“点赞人数”，“人气指数”等，都可以使用该操作接口。
- DEC：减少，value 只能是整数，如“点赞人数”，“人气指数”等，都可以使用该操作接口。

>?op 为 MLVBCustomFieldOpSet 或者 MLVBCustomFieldOpDec 时，value 需要是一个数字。

***

### getCustomInfo

获取当前房间的扩展信息字段。

```
- (void)getCustomInfo:(void(^)(int errCode, NSString *errMsg, NSDictionary *customInfo))completion 

```

__参数__

| 参数       | 类型                                                         | 含义               |
| ---------- | ------------------------------------------------------------ | ------------------ |
| completion | void(^)(int errCode, NSString *errMsg, NSDictionary *customInfo) | 获取自定义值回调。 |

***


## 主播和观众连麦

### requestJoinAnchor

观众请求连麦。

```
- (void)requestJoinAnchor:(NSString *)reason completion:(void(^)(int errCode, NSString *errMsg))completion 

```

__参数__

| 参数       | 类型                                   | 含义           |
| ---------- | -------------------------------------- | -------------- |
| reason     | NSString *                             | 连麦原因。     |
| completion | void(^)(int errCode, NSString *errMsg) | 主播响应回调。 |

__介绍__

主播和观众的连麦流程可以简单描述为如下几个步骤：

1. 观众调用 requestJoinAnchor 向主播发起连麦请求。
2. 主播会收到 MLVBLiveRoomDelegate.onRequestJoinAnchor 的回调通知。
3. 主播调用 responseJoinAnchor 确定是否接受观众的连麦请求。
4. 观众会收到 requestJoinAnchor 传入的回调通知，可以得知请求是否被同意。
5. 观众如果请求被同意，则调用 startLocalPreview 开启本地摄像头，如果 App 还没有取得摄像头和麦克风权限，会触发 UI 提示。
6. 观众然后调用 joinAnchor 正式进入连麦状态。
7. 主播一旦观众进入连麦状态，主播就会收到 MLVBLiveRoomDelegate onAnchorEnter 通知。
8. 主播调用 startRemoteView 就可以看到连麦观众的视频画面。
9. 观众如果直播间里已经有其他观众正在跟主播进行连麦，那么新加入的这位连麦观众也会收到 MLVBLiveRoomDelegate onAnchorJoin 通知，用于展示（startRemoteView）其他连麦者的视频画面。

***

### responseJoinAnchor

主播处理连麦请求。

```
- (void)responseJoinAnchor:(NSString *)userID agree:(BOOL)agree reason:(NSString *)reason 

```

__参数__

| 参数   | 类型       | 含义                      |
| ------ | ---------- | ------------------------- |
| userID | NSString * | 观众 ID。                 |
| agree  | BOOL       | YES：同意；NO：拒绝。     |
| reason | NSString * | 同意/拒绝连麦的原因描述。 |

__介绍__

主播在收到 MLVBLiveRoomDelegate.onRequestJoinAnchor 回调之后会需要调用此接口来处理观众的连麦请求。

***

### joinAnchor

进入连麦状态。

```
- (void)joinAnchor:(void(^)(int errCode, NSString *errMsg))completion 

```

__参数__

| 参数       | 类型                                   | 含义                 |
| ---------- | -------------------------------------- | -------------------- |
| completion | void(^)(int errCode, NSString *errMsg) | 进入连麦的结果回调。 |

__介绍__

进入连麦成功后，主播和其他连麦观众会收到 MLVBLiveRoomDelegate.onAnchorEnter 通知。

***

### quitJoinAnchor

观众退出连麦。

```
- (void)quitJoinAnchor:(void(^)(int errCode, NSString *errMsg))completion 

```

__参数__

| 参数       | 类型                                   | 含义                 |
| ---------- | -------------------------------------- | -------------------- |
| completion | void(^)(int errCode, NSString *errMsg) | 退出连麦的结果回调。 |

__介绍__

退出连麦成功后，主播和其他连麦观众会收到 MLVBLiveRoomDelegate.onAnchorExit 通知。

***

### kickoutJoinAnchor

主播踢除连麦观众。

```
- (void)kickoutJoinAnchor:(NSString *)userID 

```

__参数__

| 参数   | 类型       | 含义            |
| ------ | ---------- | --------------- |
| userID | NSString * | 连麦小主播 ID。 |

__介绍__

主播调用此接口踢除连麦观众后，被踢连麦观众会收到 MLVBLiveRoomDelegate.onKickoutJoinAnchor 回调通知。

***


## 主播跨房间 PK

### requestRoomPK

请求跨房 PK。

```
- (void)requestRoomPK:(NSString *)userID completion:(void(^)(int errCode, NSString *errMsg, NSString *streamUrl))completion 

```

__参数__

| 参数       | 类型                                                        | 含义                     |
| ---------- | ----------------------------------------------------------- | ------------------------ |
| userID     | NSString *                                                  | 被邀约主播 ID。          |
| completion | void(^)(int errCode, NSString *errMsg, NSString *streamUrl) | 请求跨房 PK 的结果回调。 |

__介绍__

主播和主播之间可以跨房间 PK，两个正在直播中的主播 A 和 B，他们之间的跨房 PK 流程如下：

1. 主播 A 调用 requestRoomPK  向主播 B 发起连麦请求。
2. 主播 B 会收到 MLVBLiveRoomDelegate onRequestRoomPK 回调通知。
3. 主播 B 调用 responseRoomPK  确定是否接受主播 A 的 PK 请求。
4. 主播 B 如果接受了主播 A 的要求，可以直接调用 startRemoteView  来显示主播 A 的视频画面。
5. 主播 A 会通过传入的 completion 收到回调通知，可以得知请求是否被同意。
6. 主播 A 如果请求被同意，则可以调用 startRemoteView  显示主播 B 的视频画面。

***

### responseRoomPK

响应跨房 PK 请求。

```
- (void)responseRoomPK:(MLVBAnchorInfo *)anchor agree:(BOOL)agree reason:(NSString *)reason 

```

__参数__

| 参数   | 类型             | 含义                       |
| ------ | ---------------- | -------------------------- |
| anchor | MLVBAnchorInfo * | 发起 PK 请求的主播。       |
| agree  | BOOL             | YES：同意；NO：拒绝。      |
| reason | NSString *       | 同意或拒绝 PK 的原因描述。 |

__介绍__

主播响应其他房间主播的 PK 请求，发起 PK 请求的主播会收到 MLVBLiveRoomDelegate.onRequestRoomPK 回调通知。

***

### quitRoomPK

退出跨房 PK。

```
- (void)quitRoomPK:(void(^)(int errCode, NSString *errMsg))completion 

```

__参数__

| 参数       | 类型                                   | 含义                     |
| ---------- | -------------------------------------- | ------------------------ |
| completion | void(^)(int errCode, NSString *errMsg) | 退出跨房 PK 的结果回调。 |

__介绍__

当两个主播中的任何一个退出跨房 PK 状态后，另一个主播会收到 MLVBLiveRoomDelegate.onQuitRoomPK 回调通知。

***


## 视频相关接口函数

### startLocalPreview

开启本地视频的预览画面。

```
- (void)startLocalPreview:(BOOL)frontCamera view:(UIView *)view 

```

__参数__

| 参数        | 类型     | 含义                              |
| ----------- | -------- | --------------------------------- |
| frontCamera | BOOL     | YES：前置摄像头；NO：后置摄像头。 |
| view        | UIView * | 承载视频画面的控件。              |

***

### stopLocalPreview

停止本地视频采集及预览。

```
- (void)stopLocalPreview

```

***

### startRemoteView

启动渲染远端视频画面。

```
- (void)startRemoteView:(MLVBAnchorInfo *)anchorInfo view:(UIView *)view onPlayBegin:(IPlayBegin)onPlayBegin onPlayError:(IPlayError)onPlayError playEvent:(IPlayEventBlock)onPlayEvent 

```

__参数__

| 参数        | 类型             | 含义                 |
| ----------- | ---------------- | -------------------- |
| anchorInfo  | MLVBAnchorInfo * | 对方的用户信息。     |
| view        | UIView *         | 承载视频画面的控件。 |
| onPlayBegin | IPlayBegin       | 播放器开始回调。     |
| onPlayError | IPlayError       | 播放出错回调。       |
| onPlayEvent | IPlayEventBlock  | 其它播放事件回调。   |

>?在 onUserVideoAvailable 回调时，调用这个接口。

***

### stopRemoteView

停止渲染远端视频画面。

```
- (void)stopRemoteView:(MLVBAnchorInfo *)anchor 

```

__参数__

| 参数   | 类型             | 含义         |
| ------ | ---------------- | ------------ |
| anchor | MLVBAnchorInfo * | 对方的用户。 |

***

### setMirror

设置观众端镜像效果。

```
- (void)setMirror:(BOOL)isMirror 

```

__参数__

| 参数     | 类型 | 含义                                                        |
| -------- | ---- | ----------------------------------------------------------- |
| isMirror | BOOL | YES：播放端看到的是镜像画面；NO：播放端看到的是非镜像画面。 |

__介绍__

由于前置摄像头采集的画面是取自手机的观察视角，将采集到的画面直接展示给观众是没有问题的，但如果将采集到的画面也直接显示给主播，会让主播感受到和照镜子时完全相反的体验，主播会感到很奇怪。 因此，SDK 会默认开启本地摄像头预览画面的镜像效果，让主播直播时感受到和照镜子一样的体验效果。
setMirror 所影响的是观众端看到的视频效果，如果想要保持观众端看到的效果跟主播端保持一致，需要开启镜像； 如果想要让观众端看到正常的未经处理过的画面（如主播弹吉他的时候有类似需求），则可以关闭镜像。

>?仅当前使用前置摄像头时，setMirror 接口才会生效，**在使用后置摄像头时此接口无效**。

***


## 音频相关接口函数

### muteLocalAudio

是否屏蔽本地音频。

```
- (void)muteLocalAudio:(BOOL)mute 

```

__参数__

| 参数 | 类型 | 含义                  |
| ---- | ---- | --------------------- |
| mute | BOOL | YES：屏蔽；NO：开启。 |

***

### muteRemoteAudio

设置指定用户是否静音。

```
- (void)muteRemoteAudio:(NSString *)userID mute:(BOOL)mute 

```

__参数__

| 参数   | 类型       | 含义                    |
| ------ | ---------- | ----------------------- |
| userID | NSString * | 对方的用户标识。        |
| mute   | BOOL       | YES：静音；NO：非静音。 |

***

### muteAllRemoteAudio

设置所有远端用户是否静音。

```
- (void)muteAllRemoteAudio:(BOOL)mute 

```

__参数__

| 参数 | 类型 | 含义                    |
| ---- | ---- | ----------------------- |
| mute | BOOL | YES：静音；NO：非静音。 |

***


## 摄像头相关接口函数

### switchCamera

切换前后摄像头。

```
- (void)switchCamera

```

***

### setCameraMuteImage

主播屏蔽摄像头期间需要显示的等待图片。

```
- (void)setCameraMuteImage:(UIImage *)image 

```

__参数__

| 参数  | 类型      | 含义       |
| ----- | --------- | ---------- |
| image | UIImage * | 等待图片。 |

__介绍__

当主播屏蔽摄像头，或者由于 App 切入后台无法使用摄像头的时候，我们需要使用一张等待图片来提示观众“主播暂时离开，请不要走开”。

***

### setZoom

调整焦距。

```
- (void)setZoom:(CGFloat)distance 

```

__参数__

| 参数     | 类型    | 含义                        |
| -------- | ------- | --------------------------- |
| distance | CGFloat | 焦距大小，取值范围：1 - 5。 |

>?当为1的时候为最远视角（正常镜头），当为5的时候为最近视角（放大镜头），这里最大值推荐为5，超过5后视频数据会变得模糊不清。

***

### enableTorch

打开闪关灯。

```
- (BOOL)enableTorch:(BOOL)bEnable 

```

__参数__

| 参数    | 类型 | 含义                  |
| ------- | ---- | --------------------- |
| bEnable | BOOL | YES：打开；NO：关闭。 |

__返回__

YES：打开成功；NO：打开失败。

***

### setFocusPosition

设置手动对焦区域。

```
- (void)setFocusPosition:(CGPoint)touchPoint 

```

__介绍__

SDK 默认使用摄像头自动对焦功能，您也可以通过 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) 中的 touchFocus 选项关闭自动对焦，改用手动对焦。 改用手动对焦之后，需要由主播自己单击摄像头预览画面上的某个区域，来手动指导摄像头对焦。

***


## 美颜滤镜相关接口函数

### getBeautyManager

获取美颜管理对象 [TXBeautyManager](https://cloud.tencent.com/document/product/454/39382)。

```
- (TXBeautyManager *)getBeautyManager 

```

>? 通过美颜管理，您可以使用以下功能：
>- 设置”美颜风格”、”美白”、“红润”、“大眼”、“瘦脸”、“V脸”、“下巴”、“短脸”、“小鼻”、“亮眼”、“白牙”、“祛眼袋”、“祛皱纹”、“祛法令纹”等美容效果。
>- 调整“发际线”、“眼间距”、“眼角”、“嘴形”、“鼻翼”、“鼻子位置”、“嘴唇厚度”、“脸型”。
>- 设置人脸挂件（素材）等动态效果。
>- 添加美妆。
>- 进行手势识别。

***

### setFilter

设置指定素材滤镜特效。

```
- (void)setFilter:(UIImage *)image 

```

__参数__

| 参数  | 类型      | 含义                         |
| ----- | --------- | ---------------------------- |
| image | UIImage * | 指定素材，即颜色查找表图片。 |

>?滤镜素材请使用 png 格式，不能使用 jpg 格式。友情提示：Windows 里直接改文件的后缀名不能改变图片的格式，需要用 Photoshop 进行转换。

***

### setSpecialRatio

设置滤镜浓度。

```
- (void)setSpecialRatio:(float)specialValue 

```

__参数__

| 参数         | 类型  | 含义                                      |
| ------------ | ----- | ----------------------------------------- |
| specialValue | float | 从0到1，越大滤镜效果越明显，默认取值0.5。 |

***

### setGreenScreenFile

设置绿幕背景视频（商业版有效，其它版本设置此参数无效）。

```
- (void)setGreenScreenFile:(NSURL *)file 

```

__参数__

| 参数 | 类型    | 含义                                       |
| ---- | ------- | ------------------------------------------ |
| file | NSURL * | 视频文件路径。支持 MP4；nil 表示关闭特效。 |

>?此处的绿幕功能并非智能抠背，它需要被拍摄者的背后有一块绿色的幕布来辅助产生特效。

***

## 消息发送接口函数

### sendRoomTextMsg

发送文本消息。

```
- (void)sendRoomTextMsg:(NSString *)message completion:(void(^)(int errCode, NSString *errMsg))completion 

```

__参数__

| 参数       | 类型                                   | 含义           |
| ---------- | -------------------------------------- | -------------- |
| message    | NSString *                             | 文本消息。     |
| completion | void(^)(int errCode, NSString *errMsg) | 发送结果回调。 |

***

### sendRoomCustomMsg

发送自定义文本消息。

```
- (void)sendRoomCustomMsg:(NSString *)cmd msg:(NSString *)message completion:(void(^)(int errCode, NSString *errMsg))completion 

```

__参数__

| 参数       | 类型                                   | 含义                                               |
| ---------- | -------------------------------------- | -------------------------------------------------- |
| cmd        | NSString *                             | 命令字，由开发者自定义，主要用于区分不同消息类型。 |
| message    | NSString *                             | 文本消息。                                         |
| completion | void(^)(int errCode, NSString *errMsg) | 发送结果回调。                                     |

***


## 背景混音相关接口函数

### playBGM

播放背景音乐。

```
- (BOOL)playBGM:(NSString *)path 

```

__参数__

| 参数 | 类型       | 含义                                                         |
| ---- | ---------- | ------------------------------------------------------------ |
| path | NSString * | 音乐文件路径，一定要是 `app` 对应的 `document` 目录下面的路径，否则文件会读取失败。 |

__返回__

YES：成功；NO：失败。

***

### playBGM

播放背景音乐（高级版本）。

```
- (BOOL)playBGM:(NSString *)path withBeginNotify:(void(^)(NSInteger errCode))beginNotify withProgressNotify:(void(^)(NSInteger progressMS, NSInteger durationMS))progressNotify andCompleteNotify:(void(^)(NSInteger errCode))completeNotify 

```

__参数__

| 参数           | 类型                                                | 含义                                                         |
| -------------- | --------------------------------------------------- | ------------------------------------------------------------ |
| path           | NSString *                                          | 音乐文件路径，一定要是 `app` 对应的 `document` 目录下面的路径，否则文件会读取失败。 |
| beginNotify    | void(^)(NSInteger errCode)                          | 音乐播放开始的回调通知。                                     |
| progressNotify | void(^)(NSInteger progressMS, NSInteger durationMS) | 音乐播放的进度通知，单位：毫秒。                             |
| completeNotify | void(^)(NSInteger errCode)                          | 音乐播放结束的回调通知。                                     |

__返回__

YES：成功；NO：失败。

***

### stopBGM

停止播放背景音乐。

```
- (BOOL)stopBGM

```

***

### pauseBGM

暂停播放背景音乐。

```
- (BOOL)pauseBGM

```

***

### resumeBGM

继续播放背景音乐。

```
- (BOOL)resumeBGM

```

***

### getMusicDuration

获取音乐文件总时长，单位毫秒。

```
- (int)getMusicDuration:(NSString *)path 

```

__参数__

| 参数 | 类型       | 含义                                                         |
| ---- | ---------- | ------------------------------------------------------------ |
| path | NSString * | 音乐文件路径，如果 path 为 nil，那么返回当前正在播放的背景音乐时长。 |

__返回__

成功返回时长，单位毫秒，失败返回-1。

***

### setMicVolume

设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小。

```
- (BOOL)setMicVolume:(float)volume 

```

__参数__

| 参数   | 类型  | 含义                                          |
| ------ | ----- | --------------------------------------------- |
| volume | float | 音量大小，1.0 为正常音量，建议值为0.0 - 2.0。 |

***

### setBGMVolume

设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小。

```
- (BOOL)setBGMVolume:(float)volume 

```

__参数__

| 参数   | 类型  | 含义                                         |
| ------ | ----- | -------------------------------------------- |
| volume | float | 音量大小，1.0为正常音量，建议值为0.0 - 2.0。 |

***

### setBGMPitch

调整背景音乐的音调高低。

```
- (BOOL)setBGMPitch:(float)pitch 

```

__参数__

| 参数  | 类型  | 含义                                           |
| ----- | ----- | ---------------------------------------------- |
| pitch | float | 音调，默认值是0.0f，范围：-1 - 1之间的浮点数。 |

__返回__

YES：成功；NO：失败。

***

### setReverbType

设置混响效果。

```
- (BOOL)setReverbType:(TXReverbType)reverbType 

```

__参数__

| 参数       | 类型         | 含义                                                       |
| ---------- | ------------ | ---------------------------------------------------------- |
| reverbType | TXReverbType | 混响类型，详见`TXLiveSDKTypeDef.h`中的 TXReverbType 定义。 |

__返回__

YES：成功；NO：失败。

***

### setVoiceChangerType

设置变声类型。

```
- (BOOL)setVoiceChangerType:(TXVoiceChangerType)voiceChangerType 
```

__参数__

| 参数             | 类型               | 含义                                                         |
| ---------------- | ------------------ | ------------------------------------------------------------ |
| voiceChangerType | TXVoiceChangerType | 混响类型，详见`TXLiveSDKTypeDef.h`中的 voiceChangerType 定义。 |

__返回__

YES：成功；NO：失败。

***


## 调试相关接口函数

### showVideoDebugLog

在渲染 view 上显示播放或推流状态统计及事件消息浮层。

```
- (void)showVideoDebugLog:(BOOL)isShow 
```


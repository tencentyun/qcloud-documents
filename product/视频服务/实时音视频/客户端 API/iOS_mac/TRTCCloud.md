
TRTCCloud @ TXLiteAVSDK。

腾讯云视频通话功能的主要接口类。


## 创建与销毁
### delegate

设置回调接口 TRTCCloudDelegate。
```
@property (nonatomic, weak) id< TRTCCloudDelegate > delegate;
```

__介绍__

您可以通过 TRTCCloudDelegate 获得来自 SDK 的各种状态通知，详见 TRTCCloudDelegate.h 中的定义。

### delegateQueue

设置驱动 TRTCCloudDelegate 回调的队列。
```
@property (nonatomic, strong) dispatch_queue_t delegateQueue;
```

__介绍__

SDK 默认会采用 Main Queue 作为驱动 TRTCCloudDelegate。如果您不指定自己的 delegateQueue， SDK 的 TRTCCloudDelegate 回调都将由 Main Queue 来调用。此时您在 TRTCCloudDelegate 的回调函数里操作 UI 是线程安全的。

### sharedInstance

创建 TRTCCloud 单例。
```
+ (instancetype)sharedInstance
```


### destroySharedIntance

销毁 TRTCCloud 单例。
```
+ (void)destroySharedIntance
```



## 房间相关接口函数
### enterRoom

进入房间。
```
- (void)enterRoom:(TRTCParams *)param appScene:(TRTCAppScene)scene 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| param | [TRTCParams](https://cloud.tencent.com/document/product/647/32261#trtcparams) * | 进房参数，请参考 [TRTCParams](https://cloud.tencent.com/document/product/647/32261#trtcparams)。 |
| scene | [TRTCAppScene](https://cloud.tencent.com/document/product/647/32261#trtcappscene) | 应用场景，目前支持视频通话（VideoCall）和在线直播（Live）两种场景。 |

__介绍__

如果加入成功，您会收到来自 [TRTCCloudDelegate](https://cloud.tencent.com/document/product/647/32263) 中的 onEnterRoom(result) 回调:

- 如果加入成功，result 会是一个正数（result > 0），表示加入房间的时间消耗，单位是毫秒（ms）。
- 如果加入失败，result 会是一个负数（result < 0），表示进房失败的错误码。 进房失败的错误码含义请参见[错误码](https://cloud.tencent.com/document/product/647/32257)。



>?不管进房是否成功，enterRoom 都必须与 exitRoom 配对使用，在调用 exitRoom 前再次调用 enterRoom 函数会导致不可预期的错误问题。



### exitRoom

离开房间。
```
- (void)exitRoom
```

__介绍__

调用 [exitRoom](#exitroom) 接口会执行退出房间的相关逻辑，例如释放音视频设备资源和编解码器资源等。 待资源释放完毕，SDK 会通过 TRTCCloudDelegate 中的 onExitRoom() 回调通知到您。
如果您要再次调用 enterRoom() 或者切换到其他的音视频 SDK，请等待 onExitRoom() 回调到来之后再执行相关操作。 否则可能会遇到摄像头或麦克风（例如 iOS 里的 AudioSession）被占用等各种异常问题。


### switchRole

切换角色，仅适用于直播场景（TRTCAppSceneLIVE）。
```
- (void)switchRole:(TRTCRoleType)role 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| role | [TRTCRoleType](https://cloud.tencent.com/document/product/647/32261#trtcroletype) | 目标角色，默认为主播。 |

__介绍__

在直播场景下，一个用户可能需要在“观众”和“主播”之间来回切换。 您可以在进房前通过 [TRTCParams](https://cloud.tencent.com/document/product/647/32261#trtcparams) 中的 role 字段确定角色，也可以通过 switchRole 在进房后切换角色。


### connectOtherRoom

请求跨房通话（主播 PK）。
```
- (void)connectOtherRoom:(NSString *)param 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| param | NSString * | JSON 字符串连麦参数，roomId 代表目标房间号，userId 代表目标用户 ID。 |

__介绍__

TRTC 中两个不同音视频房间中的主播，可以通过“跨房通话”功能拉通连麦通话功能。使用此功能时，两个主播无需退出各自原来的直播间即可进行“连麦 PK”。
例如：当房间“001”中的主播 A 通过 connectOtherRoom() 跟房间“002”中的主播 B 拉通跨房通话后， 房间“001”中的用户都会收到主播 B 的 onUserEnter(B) 回调和 onUserVideoAvailable(B，YES) 回调。 房间“002”中的用户都会收到主播 A 的 onUserEnter(A) 回调和 onUserVideoAvailable(A，YES) 回调。
简言之，跨房通话的本质，就是把两个不同房间中的主播相互分享，让每个房间里的观众都能看到两个主播。


<pre>
               房间 001                    房间 002
            --------------              -------------
 跨房通话前：| 主播 A      |             | 主播 B     |
            | 观众 U V W  |             | 观众 X Y Z |
            --------------              -------------</pre>



<pre>              房间 001                     房间 002
            --------------              -------------
 跨房通话后：| 主播 A B    |             | 主播 B A   |
            | 观众 U V W  |             | 观众 X Y Z |
            --------------              -------------
</pre>

跨房通话的参数考虑到后续扩展字段的兼容性问题，暂时采用了 JSON 格式的参数，要求至少包含两个字段：
- roomId：房间“001”中的主播 A 要跟房间“002”中的主播 B 连麦，主播 A 调用 connectOtherRoom() 时 roomId 应指定为“002”。
- userId：房间“001”中的主播 A 要跟房间“002”中的主播 B 连麦，主播 A 调用 connectOtherRoom() 时 userId 应指定为 B 的 userId。


跨房通话的请求结果会通过 [TRTCCloudDelegate](https://cloud.tencent.com/document/product/647/32263) 中的 onConnectOtherRoom() 回调通知给您。


<pre>
  NSMutableDictionary * jsonDict = [[NSMutableDictionary alloc] init];
  [jsonDict setObject:@(002) forKey:"roomId"];
  [jsonDict setObject:@"userB" forKey:@"userId"];
  NSData* jsonData = [NSJSONSerialization dataWithJSONObject:jsonDict options:NSJSONWritingPrettyPrinted error:nil];
  NSString* jsonString = [[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding];
  [trtc connectOtherRoom:jsonString];
</pre>



### disconnectOtherRoom

退出跨房通话。
```
- (void)disconnectOtherRoom
```

__介绍__

跨房通话的退出结果会通过 [TRTCCloudDelegate](https://cloud.tencent.com/document/product/647/32263) 中的 onDisconnectOtherRoom() 回调通知给您。


### setDefaultStreamRecvMode

设置音视频数据接收模式（需要在进房前设置才能生效）。
```
- (void)setDefaultStreamRecvMode:(BOOL)autoRecvAudio video:(BOOL)autoRecvVideo
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| autoRecvAudio | BOOL | YES：自动接收音频数据；NO：需要调用 muteRemoteAudio 进行请求或取消。默认值：YES。 |
| autoRecvVideo | BOOL | YES：自动接收视频数据；NO：需要调用 startRemoteView/stopRemoteView 进行请求或取消。默认值：YES。 |

__介绍__

为实现进房秒开的绝佳体验，SDK 默认进房后自动接收音视频。即在您进房成功的同时，您将立刻收到远端所有用户的音视频数据。 若您没有调用 startRemoteView，视频数据将自动超时取消。 若您主要用于语音聊天等没有自动接收视频数据需求的场景，您可以根据实际需求选择接收模式。

>?需要在进房前设置才能生效。




## 视频相关接口函数
### startLocalPreview

开启本地视频的预览画面 (iOS 版本)。
```
- (void)startLocalPreview:(BOOL)frontCamera view:(TXView *)view 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| frontCamera | BOOL | YES：前置摄像头；NO：后置摄像头。 |
| view | TXView * | 承载视频画面的控件。 |

__介绍__

当开始渲染首帧摄像头画面时，您会收到 [TRTCCloudDelegate](https://cloud.tencent.com/document/product/647/32263) 中的 onFirstVideoFrame(nil) 回调。


### startLocalPreview

开启本地视频的预览画面 (Mac 版本)。
```
- (void)startLocalPreview:(TXView *)view 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| view | TXView * | 承载视频画面的控件。 |

__介绍__

在调用该方法前，可以先调用 setCurrentCameraDevice 选择使用 Mac 自带摄像头或外接摄像头。当开始渲染首帧摄像头画面时，您会收到 [TRTCCloudDelegate](https://cloud.tencent.com/document/product/647/32263) 中的 onFirstVideoFrame(nil) 回调。


### stopLocalPreview

停止本地视频采集及预览。
```
- (void)stopLocalPreview
```


### muteLocalVideo

是否屏蔽自己的视频画面。
```
- (void)muteLocalVideo:(BOOL)mute 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | BOOL | YES：屏蔽；NO：开启，默认值：NO。 |

__介绍__

当屏蔽本地视频后，房间里的其它成员将会收到 onUserVideoAvailable 回调通知。


### startRemoteView

开始显示远端视频画面。
```
- (void)startRemoteView:(NSString *)userId view:(TXView *)view 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 对方的用户标识。 |
| view | TXView * | 承载视频画面的控件。 |

__介绍__

在收到 SDK 的 onUserVideoAvailable(userid， YES) 通知时，可以获知该远程用户开启了视频，此后调用 startRemoteView(userid) 接口加载该用户的远程画面，可以用 loading 动画优化加载过程中的等待体验。待该用户的首帧画面开始显示时，您会收到 onFirstVideoFrame(userId) 事件回调。

### stopRemoteView

停止显示远端视频画面。
```
- (void)stopRemoteView:(NSString *)userId 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 对方的用户标识。 |

__介绍__

调用此接口后，SDK 会停止接收该用户的远程视频流，同时会清理相关的视频显示资源。


### stopAllRemoteView

停止显示所有远端视频画面。
```
- (void)stopAllRemoteView
```

>?如果有屏幕分享的画面在显示，则屏幕分享的画面也会一并被关闭。



### muteRemoteVideoStream

暂停接收指定的远端视频流。
```
- (void)muteRemoteVideoStream:(NSString *)userId mute:(BOOL)mute 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 对方的用户标识。 |
| mute | BOOL | 是否停止接收。 |

__介绍__

该接口仅停止接收远程用户的视频流，但并不释放显示资源，所以视频画面会冻屏在 mute 前的最后一帧。


### muteAllRemoteVideoStreams

停止接收所有远端视频流。
```
- (void)muteAllRemoteVideoStreams:(BOOL)mute 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | BOOL | 是否停止接收。 |


### setVideoEncoderParam

设置视频编码器相关参数。
```
- (void)setVideoEncoderParam:(TRTCVideoEncParam *)param 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| param | [TRTCVideoEncParam](https://cloud.tencent.com/document/product/647/32261#trtcvideoencparam) * | 视频编码参数，详情请参考 TRTCCloudDef.h 中的 [TRTCVideoEncParam](https://cloud.tencent.com/document/product/647/32261#trtcvideoencparam) 定义。 |

__介绍__

该设置决定了远端用户看到的画面质量（同时也是云端录制出的视频文件的画面质量）。


### setNetworkQosParam

设置网络流控相关参数。
```
- (void)setNetworkQosParam:(TRTCNetworkQosParam *)param 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| param | [TRTCNetworkQosParam](https://cloud.tencent.com/document/product/647/32261#trtcnetworkqosparam) * | 网络流控参数，详情请参考 TRTCCloudDef.h 中的 [TRTCNetworkQosParam](https://cloud.tencent.com/document/product/647/32261#trtcnetworkqosparam) 定义。 |

__介绍__

该设置决定 SDK 在各种网络环境下的调控策略（例如弱网下选择“保清晰”或“保流畅”）。


### setLocalViewFillMode

设置本地图像的渲染模式。
```
- (void)setLocalViewFillMode:(TRTCVideoFillMode)mode 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mode | [TRTCVideoFillMode](https://cloud.tencent.com/document/product/647/32261#trtcvideofillmode) | 填充（画面可能会被拉伸裁剪）或适应（画面可能会有黑边）。 |


### setRemoteViewFillMode

设置远端图像的渲染模式。
```
- (void)setRemoteViewFillMode:(NSString *)userId mode:(TRTCVideoFillMode)mode 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 用户 ID。 |
| mode | [TRTCVideoFillMode](https://cloud.tencent.com/document/product/647/32261#trtcvideofillmode) | 填充（画面可能会被拉伸裁剪）或适应（画面可能会有黑边）。 |


### setLocalViewRotation

设置本地图像的顺时针旋转角度。
```
- (void)setLocalViewRotation:(TRTCVideoRotation)rotation 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rotation | [TRTCVideoRotation](https://cloud.tencent.com/document/product/647/32261#trtcvideorotation) | 支持90、180以及270旋转角度，默认值：TRTCVideoRotation_0。 |


### setRemoteViewRotation

设置远端图像的顺时针旋转角度。
```
- (void)setRemoteViewRotation:(NSString *)userId rotation:(TRTCVideoRotation)rotation 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 用户 ID。 |
| rotation | [TRTCVideoRotation](https://cloud.tencent.com/document/product/647/32261#trtcvideorotation) | 支持90、180以及270旋转角度，默认值：TRTCVideoRotation_0。 |


### setVideoEncoderRotation

设置视频编码输出的（也就是远端用户观看到的，以及服务器录制下来的）画面方向。
```
- (void)setVideoEncoderRotation:(TRTCVideoRotation)rotation 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rotation | [TRTCVideoRotation](https://cloud.tencent.com/document/product/647/32261#trtcvideorotation) | 目前支持0和180两个旋转角度，默认值：TRTCVideoRotation_0。 |

__介绍__

在 iPad、iPhone 等设备180度旋转时，由于摄像头的采集方向没有变，所以对方看到的画面是上下颠倒的，在这种情况下，您可以通过该接口将 SDK 输出到对方的画面旋转180度，确保对方看到的画面依然正常。


### setLocalViewMirror

设置本地摄像头预览画面的镜像模式（iOS）。
```
- (void)setLocalViewMirror:(TRTCLocalVideoMirrorType)mirror 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mirror | [TRTCLocalVideoMirrorType](https://cloud.tencent.com/document/product/647/32261#trtclocalvideomirrortype) | 镜像模式，默认值为 TRTCLocalVideoMirrorType_Auto。 |


### setLocalViewMirror

设置本地摄像头预览画面的镜像模式（Mac）。
```
- (void)setLocalViewMirror:(BOOL)mirror 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mirror | BOOL | 镜像模式，默认值：YES。 |


### setVideoEncoderMirror

设置编码器输出的画面镜像模式。
```
- (void)setVideoEncoderMirror:(BOOL)mirror 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mirror | BOOL | 是否开启远端镜像，YES：开启远端画面镜像；NO：关闭远端画面镜像；默认值：NO。 |

__介绍__

该接口不改变本地摄像头的预览画面，但会改变另一端用户看到的（以及服务器录制的）画面效果。


### setGSensorMode

设置重力感应的适应模式。
```
- (void)setGSensorMode:(TRTCGSensorMode)mode 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mode | [TRTCGSensorMode](https://cloud.tencent.com/document/product/647/32261#trtcgsensormode) | 重力感应模式，详情请参考 TRTCGSensorMode 的定义，默认值：TRTCGSensorMode_UIAutoLayout。 |


### enableEncSmallVideoStream

开启大小画面双路编码模式。
```
- (int)enableEncSmallVideoStream:(BOOL)enable withQuality:(TRTCVideoEncParam *)smallVideoEncParam 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | BOOL | 是否开启小画面编码，默认值：NO。 |
| smallVideoEncParam | [TRTCVideoEncParam](https://cloud.tencent.com/document/product/647/32261#trtcvideoencparam) * | 小流的视频参数。 |

__返回__

0：成功；-1：大画面已经是最低画质。

__介绍__

如果当前用户是房间中的主要角色（例如主播、老师、主持人等），并且使用 PC 或者 Mac 环境，可以开启该模式。 开启该模式后，当前用户会同时输出【高清】和【低清】两路视频流（但只有一路音频流）。对于开启该模式的当前用户，会占用更多的网络带宽，并且会更加消耗 CPU 计算资源。
对于同一房间的远程观众而言：
- 如果下行网络很好，可以选择观看【高清】画面
- 如果下行网络较差，可以选择观看【低清】画面。

>?双路编码开启后，会消耗更多的 CPU 和网络带宽，所以对于 iMac、Windows 或者高性能 Pad 可以考虑开启，但请不要在手机端开启。


### setRemoteVideoStreamType

选定观看指定 uid 的大画面或小画面。
```
- (void)setRemoteVideoStreamType:(NSString *)userId type:(TRTCVideoStreamType)type 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 用户 ID。 |
| type | [TRTCVideoStreamType](https://cloud.tencent.com/document/product/647/32261#trtcvideostreamtype) | 视频流类型，即选择看大画面或小画面，默认为大画面。 |

__介绍__

此功能需要该 uid 通过 enableEncSmallVideoStream 提前开启双路编码模式。如果该 uid 没有开启双路编码模式，则此操作将无任何反应。


### setPriorRemoteVideoStreamType

设定观看方优先选择的视频质量。
```
- (void)setPriorRemoteVideoStreamType:(TRTCVideoStreamType)type 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| type | [TRTCVideoStreamType](https://cloud.tencent.com/document/product/647/32261#trtcvideostreamtype) | 默认观看大画面或小画面，默认为大画面。 |

__介绍__

低端设备推荐优先选择低清晰度的小画面。 如果对方没有开启双路视频模式，则此操作无效。



## 音频相关接口函数
### startLocalAudio

开启本地音频的采集和上行。
```
- (void)startLocalAudio
```

__介绍__

该函数会启动麦克风采集，并将音频数据传输给房间里的其他用户。
SDK 不会默认开启本地音频采集和上行，您需要调用该函数开启，否则房间里的其他用户将无法听到您的声音。

>?该函数会检查麦克风的使用权限，如果当前 App 没有麦克风权限，SDK 会向用户申请开启。



### stopLocalAudio

关闭本地音频的采集和上行。
```
- (void)stopLocalAudio
```

__介绍__

当关闭本地音频的采集和上行，房间里的其它成员会收到 onUserAudioAvailable(NO) 回调通知。


### muteLocalAudio

静音本地的音频。
```
- (void)muteLocalAudio:(BOOL)mute 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | BOOL | YES：屏蔽；NO：开启，默认值：NO。 |

__介绍__

当静音本地音频后，房间里的其它成员会收到 onUserAudioAvailable(NO) 回调通知。
与 stopLocalAudio 不同之处在于，muteLocalAudio 并不会停止发送音视频数据，而是继续发送码率极低的静音包。由于 MP4 等视频文件格式，对于音频的连续性是要求很高的，使用 stopLocalAudio 会导致录制出的 MP4 不易播放。因此在对录制质量要求很高的场景中，建议选择 muteLocalAudio，从而录制出兼容性更好的 MP4 文件。

### setAudioRoute

设置音频路由。
```
- (void)setAudioRoute:(TRTCAudioRoute)route 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| route | [TRTCAudioRoute](https://cloud.tencent.com/document/product/647/32261#trtcaudioroute) | 音频路由，即声音由哪里输出（扬声器、听筒），默认值：TRTCAudioModeSpeakerphone。 |

__介绍__

微信和手机 QQ 视频通话功能的免提模式就是基于音频路由实现的。 一般手机都有两个扬声器，一个是位于顶部的听筒扬声器，声音偏小；一个是位于底部的立体声扬声器，声音偏大。设置音频路由的作用就是决定声音使用哪个扬声器播放。


### muteRemoteAudio

静音某一个用户的声音。
```
- (void)muteRemoteAudio:(NSString *)userId mute:(BOOL)mute 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 对方的用户 ID。 |
| mute | BOOL | YES：静音；NO：非静音。 |


### muteAllRemoteAudio

静音所有用户的声音。
```
- (void)muteAllRemoteAudio:(BOOL)mute 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | BOOL | YES：静音；NO：非静音。 |


### enableAudioVolumeEvaluation

启用音量大小提示。
```
- (void)enableAudioVolumeEvaluation:(NSUInteger)interval 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| interval | NSUInteger | 设置 onUserVoiceVolume 回调的触发间隔，单位为ms，最小间隔为100ms，如果小于等于0则会关闭回调，建议设置为300ms。 |

__介绍__

开启此功能后，SDK 会在 onUserVoiceVolume() 中反馈对每一路声音音量大小值的评估。 如需打开此功能，请在 [startLocalAudio](#startlocalaudio) 之前调用。

>?Demo 中有一个音量大小的提示条，就是基于该接口实现的。

### startAudioRecording

开始录音。
```
- (int)startAudioRecording:(TRTCAudioRecordingParams *)param 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| param | TRTCAudioRecordingParams * | 录音参数，请参考 [TRTCAudioRecordingParams](https://cloud.tencent.com/document/product/647/32261#trtcaudiorecordingparams)。 |

__返回__

0：成功；-1：录音已开始；-2：文件或目录创建失败；-3：后缀指定的音频格式不支持。

__介绍__

该方法调用后， SDK 会将通话过程中的所有音频（包括本地音频，远端音频，BGM 等）录制到一个文件里。无论是否进房，调用该接口都生效。如果调用 exitRoom 时还在录音，录音会自动停止。


### stopAudioRecording

停止录音。
```
- (void)stopAudioRecording
```

__介绍__

如果调用 exitRoom 时还在录音，录音会自动停止。

### setSystemVolumeType

设置通话时使用的系统音量类型。
```
- (void)setSystemVolumeType:(TRTCSystemVolumeType)type 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| type | TRTCSystemVolumeType | 系统音量类型，请参考 [TRTCSystemVolumeType](https://cloud.tencent.com/document/product/647/32261#trtcsystemvolumetype)。 |

>?需要在调用 [startLocalAudio](#startlocalaudio) 之前调用该接口。



### enableAudioEarMonitoring

开启耳返。
```
- (void)enableAudioEarMonitoring:(BOOL)enable 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | BOOL | YES：开启；NO：关闭，默认值：NO。 |

__介绍__

开启后会在耳机里听到自己的声音。

>?仅在戴耳机时有效。



## 摄像头相关接口函数
### switchCamera

切换摄像头。
```
- (void)switchCamera
```


### isCameraZoomSupported

查询当前摄像头是否支持缩放。
```
- (BOOL)isCameraZoomSupported
```


### setZoom

设置摄像头缩放因子（焦距）。
```
- (void)setZoom:(CGFloat)distance 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| distance | CGFloat | 取值范围为1 - 5，数值越大，焦距越远。 |

__介绍__

取值范围1 - 5，取值为1表示最远视角（正常镜头），取值为5表示最近视角（放大镜头）。
最大值推荐为5，若超过5，视频数据会变得模糊不清。


### isCameraTorchSupported

查询是否支持开关闪光灯（手电筒模式）。
```
- (BOOL)isCameraTorchSupported
```


### enbaleTorch

开关闪光灯。
```
- (BOOL)enbaleTorch:(BOOL)enable 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | BOOL | YES：开启；NO：关闭，默认值：NO。 |


### isCameraFocusPositionInPreviewSupported

查询是否支持设置焦点。
```
- (BOOL)isCameraFocusPositionInPreviewSupported
```


### setFocusPosition

设置摄像头焦点。
```
- (void)setFocusPosition:(CGPoint)touchPoint 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| touchPoint | CGPoint | 对焦位置。 |


### isCameraAutoFocusFaceModeSupported

查询是否支持自动识别人脸位置。
```
- (BOOL)isCameraAutoFocusFaceModeSupported
```


### enableAutoFaceFoucs

自动识别人脸位置。
```
- (void)enableAutoFaceFoucs:(BOOL)enable 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | BOOL | YES：开启；NO：关闭，默认值：YES。 |


### getCameraDevicesList

获取摄像头设备列表。
```
- (NSArray< TRTCMediaDeviceInfo * > *)getCameraDevicesList
```

__返回__

摄像头设备列表，第一项为当前系统默认设备。

__介绍__

Mac 主机本身自带一个摄像头，也允许插入 USB 摄像头。如果您希望用户选择自己外接的摄像头，可以提供一个多摄像头选择的功能。

### getCurrentCameraDevice

获取当前使用的摄像头。
```
- (TRTCMediaDeviceInfo *)getCurrentCameraDevice
```


### setCurrentCameraDevice

设置要使用的摄像头。
```
- (int)setCurrentCameraDevice:(NSString *)deviceId 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| deviceId | NSString * | 从 getCameraDevicesList 中得到的设备 ID。 |

__返回__

0：成功；-1：失败。



## 音频设备相关接口函数
### getMicDevicesList

获取麦克风设备列表。
```
- (NSArray< TRTCMediaDeviceInfo * > *)getMicDevicesList
```

__返回__

麦克风设备列表，第一项为当前系统默认设备。

__介绍__

Mac 主机本身自带一个质量很好的麦克风，但它也允许用户外接其他的麦克风，而且很多 USB 摄像头上也自带麦克风。 如果您希望用户选择自己外接的麦克风，可以提供一个多麦克风选择的功能。


### getCurrentMicDevice

获取当前的麦克风设备。
```
- (TRTCMediaDeviceInfo *)getCurrentMicDevice
```

__返回__

当前麦克风设备信息。


### setCurrentMicDevice

设置要使用的麦克风。
```
- (int)setCurrentMicDevice:(NSString *)deviceId 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| deviceId | NSString * | 从 getMicDevicesList 中得到的设备 ID。 |

__返回__

0：成功；\<0：失败。


### getCurrentMicDeviceVolume

获取当前麦克风设备音量。
```
- (float)getCurrentMicDeviceVolume
```

__返回__

麦克风音量。


### setCurrentMicDeviceVolume

设置麦克风设备的音量。
```
- (void)setCurrentMicDeviceVolume:(NSInteger)volume 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | NSInteger | 麦克风音量值，范围0 - 100。 |


### getSpeakerDevicesList

获取扬声器设备列表。
```
- (NSArray< TRTCMediaDeviceInfo * > *)getSpeakerDevicesList
```

__返回__

扬声器设备列表，第一项为当前系统默认设备。


### getCurrentSpeakerDevice

获取当前的扬声器设备。
```
- (TRTCMediaDeviceInfo *)getCurrentSpeakerDevice
```

__返回__

当前扬声器设备信息。


### setCurrentSpeakerDevice

设置要使用的扬声器。
```
- (int)setCurrentSpeakerDevice:(NSString *)deviceId 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| deviceId | NSString * | 从 getSpeakerDevicesList 中得到的设备 ID。 |

__返回__

0：成功；\<0：失败。


### getCurrentSpeakerDeviceVolume

当前扬声器设备音量。
```
- (float)getCurrentSpeakerDeviceVolume
```

__返回__

扬声器音量。


### setCurrentSpeakerDeviceVolume

设置当前扬声器音量。
```
- (int)setCurrentSpeakerDeviceVolume:(NSInteger)volume 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | NSInteger | 设置的扬声器音量，范围0 - 100。 |

__返回__

0：成功；\<0：失败。



## 美颜滤镜相关接口函数
### getBeautyManager

获取美颜管理对象。
```
- (TXBeautyManager *)getBeautyManager
```

__介绍__

通过美颜管理，您可以使用以下功能：
- 设置“美颜风格”、“美白”、“红润”、“大眼”、“瘦脸”、“V脸”、“下巴”、“短脸”、“小鼻”、“亮眼”、“白牙”、“祛眼袋”、“祛皱纹”、“祛法令纹”等美容效果。
- 调整“发际线”、“眼间距”、“眼角”、“嘴形”、“鼻翼”、“鼻子位置”、“嘴唇厚度”、“脸型”
- 设置人脸挂件（素材）等动态效果
- 添加美妆
- 进行手势识别。


### setBeautyStyle

设置美颜、美白以及红润效果级别。
```
- (void)setBeautyStyle:(TRTCBeautyStyle)beautyStyle beautyLevel:(NSInteger)beautyLevel whitenessLevel:(NSInteger)whitenessLevel ruddinessLevel:(NSInteger)ruddinessLevel TRTC_DEPRECAETD_BEAUTY_API
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| beautyStyle | [TRTCBeautyStyle](https://cloud.tencent.com/document/product/647/32261#trtcbeautystyle) | 美颜风格，光滑或者自然，光滑风格磨皮更加明显，适合娱乐场景。 |
| beautyLevel | NSInteger | 美颜级别，取值范围0 - 9； 0表示关闭，1 - 9值越大，效果越明显。 |
| whitenessLevel | NSInteger | 美白级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |
| ruddinessLevel | NSInteger | 红润级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

__介绍__

SDK 内部集成两套风格不同的磨皮算法，一套我们取名叫“光滑”，适用于美女秀场，效果比较明显。 另一套我们取名“自然”，磨皮算法更多地保留了面部细节，主观感受上会更加自然。


### setFilter

设置指定素材滤镜特效。
```
- (void)setFilter:(TXImage *)image 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| image | TXImage * | 指定素材，即颜色查找表图片。**必须使用 png 格式**。 |


### setFilterConcentration

设置滤镜浓度。
```
- (void)setFilterConcentration:(float)concentration 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| concentration | float | 从0到1，越大滤镜效果越明显，默认值为0.5。 |

__介绍__

在美女秀场等应用场景里，滤镜浓度的要求会比较高，以便更加突显主播的差异。 我们默认的滤镜浓度是0.5，如果您觉得滤镜效果不明显，可以使用下面的接口进行调节。


### setWatermark

添加水印。
```
- (void)setWatermark:(TXImage *)image streamType:(TRTCVideoStreamType)streamType rect:(CGRect)rect 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| image | TXImage * | 水印图片，**必须使用透明底的 png 格式**。 |
| streamType | [TRTCVideoStreamType](https://cloud.tencent.com/document/product/647/32261#trtcvideostreamtype) | 如果要给屏幕分享的一路也设置水印，需要调用两次的 setWatermark。 |
| rect | CGRect | 水印相对于编码分辨率的归一化坐标，x，y，width，height 取值范围0 - 1。 |

__介绍__

水印的位置是通过 rect 来指定的，rect 的格式为 (x，y，width，height)
- x：水印的坐标，取值范围为0 - 1的浮点数。
- y：水印的坐标，取值范围为0 - 1的浮点数。
- width：水印的宽度，取值范围为0 - 1的浮点数。
- height：是不用设置的，SDK 内部会根据水印图片的宽高比自动计算一个合适的高度。


例如，如果当前编码分辨率是540 × 960，rect 设置为（0.1，0.1，0.2，0.0）。 那么水印的左上坐标点就是（540 × 0.1，960 × 0.1）即（54，96），水印的宽度是 540 × 0.2 = 108px，高度自动计算。


### setEyeScaleLevel

设置大眼级别（商用企业版有效，其它版本设置此参数无效）。
```
- (void)setEyeScaleLevel:(float)eyeScaleLevel TRTC_DEPRECAETD_BEAUTY_API
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| eyeScaleLevel | float | 大眼级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setFaceScaleLevel

设置瘦脸级别（商用企业版有效，其它版本设置此参数无效）。
```
- (void)setFaceScaleLevel:(float)faceScaleLevel TRTC_DEPRECAETD_BEAUTY_API
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| faceScaleLevel | float | 瘦脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setFaceVLevel

设置V脸级别（商用企业版有效，其它版本设置此参数无效）。
```
- (void)setFaceVLevel:(float)faceVLevel TRTC_DEPRECAETD_BEAUTY_API
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| faceVLevel | float | V脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setChinLevel

设置下巴拉伸或收缩（商用企业版有效，其它版本设置此参数无效）。
```
- (void)setChinLevel:(float)chinLevel TRTC_DEPRECAETD_BEAUTY_API
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| chinLevel | float | 下巴拉伸或收缩级别，取值范围 -9 - 9；0 表示关闭，小于0表示收缩，大于0表示拉伸。 |


### setFaceShortLevel

设置短脸级别（商用企业版有效，其它版本设置此参数无效）。
```
- (void)setFaceShortLevel:(float)faceShortlevel TRTC_DEPRECAETD_BEAUTY_API
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| faceShortlevel | float | 短脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setNoseSlimLevel

设置瘦鼻级别（商用企业版有效，其它版本设置此参数无效）。
```
- (void)setNoseSlimLevel:(float)noseSlimLevel TRTC_DEPRECAETD_BEAUTY_API
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| noseSlimLevel | float | 瘦鼻级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setGreenScreenFile

设置绿幕背景视频（商用企业版有效，其它版本设置此参数无效）。
```
- (void)setGreenScreenFile:(NSURL *)file 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| file | NSURL * | 视频文件路径。支持 MP4; nil 表示关闭特效。 |

__介绍__

此处的绿幕功能并非智能抠背，需要被拍摄者的背后有一块绿色的幕布来辅助产生特效。


### selectMotionTmpl

选择使用哪一款 AI 动效挂件（商用企业版有效，其它版本设置此参数无效）。
```
- (void)selectMotionTmpl:(NSString *)tmplPath TRTC_DEPRECAETD_BEAUTY_API
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| tmplPath | NSString * | 动效文件路径。 |


### setMotionMute

设置动效静音（商用企业版有效，其它版本设置此参数无效）。
```
- (void)setMotionMute:(BOOL)motionMute TRTC_DEPRECAETD_BEAUTY_API
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| motionMute | BOOL | YES：静音；NO：不静音。 |

__介绍__

部分挂件本身会有声音特效，通过此 API 可以关闭特效播放时所带的声音效果。



## 辅流相关接口函数（Mac）
### startRemoteSubStreamView

开始显示远端用户的屏幕分享画面。
```
- (void)startRemoteSubStreamView:(NSString *)userId view:(TXView *)view 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 对方的用户标识。 |
| view | TXView * | 渲染控件。 |

__介绍__

对应于 startRemoteView() 用于显示主画面，该接口只能用于显示辅路（屏幕分享、远程播片）画面。

>?请在 onUserSubStreamAvailable 回调后再调用这个接口。



### stopRemoteSubStreamView

停止显示远端用户的屏幕分享画面。
```
- (void)stopRemoteSubStreamView:(NSString *)userId 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 对方的用户标识。 |


### setRemoteSubStreamViewFillMode

设置屏幕分享画面的显示模式。
```
- (void)setRemoteSubStreamViewFillMode:(NSString *)userId mode:(TRTCVideoFillMode)mode 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 用户的 ID。 |
| mode | [TRTCVideoFillMode](https://cloud.tencent.com/document/product/647/32261#trtcvideofillmode) | 填充（画面可能会被拉伸裁剪）或适应（画面可能会有黑边），默认值：TRTCVideoFillMode_Fit。 |

__介绍__

对应于 setRemoteViewFillMode() 于设置主画面的显示模式，该接口用于设置远端的辅路（屏幕分享、远程播放视频）画面。


### getScreenCaptureSourcesWithThumbnailSize

枚举可分享的屏幕窗口。
```
- (NSArray< TRTCScreenCaptureSourceInfo * > *)getScreenCaptureSourcesWithThumbnailSize:(CGSize)thumbnailSize iconSize:(CGSize)iconSize 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| thumbnailSize | CGSize | 指定要获取的窗口缩略图大小，缩略图可用于绘制在窗口选择界面上。 |
| iconSize | CGSize | 指定要获取的窗口图标大小。 |

__返回__

窗口列表包括屏幕。

__介绍__

如果您要给您的 App 增加屏幕分享功能，一般需要先显示一个窗口选择界面，这样用户可以选择希望分享的窗口。通过下列函数，您可以获得可分享窗口的 ID、类型、窗口名称以及缩略图。获取上述信息后，您就可以实现一个窗口选择界面。您也可以使用 Demo 源码中已经实现好的窗口选择界面。

>?返回的列表中包括屏幕和应用窗口，屏幕会在列表的前面几个元素中。



### selectScreenCaptureTarget

设置屏幕共享参数，该方法在屏幕共享过程中也可以调用。
```
- (void)selectScreenCaptureTarget:(TRTCScreenCaptureSourceInfo *)screenSource rect:(CGRect)rect capturesCursor:(BOOL)capturesCursor highlight:(BOOL)highlight 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| screenSource | [TRTCScreenCaptureSourceInfo](https://cloud.tencent.com/document/product/647/32261#trtcscreencapturesourceinfo) * | 指定分享源。 |
| rect | CGRect | 指定捕获的区域（传 CGRectZero 则默认分享全屏）。 |
| capturesCursor | BOOL | 是否捕获鼠标光标。 |
| highlight | BOOL | 是否高亮正在分享的窗口。 |

__介绍__

如果您期望在屏幕分享的过程中，切换想要分享的窗口，可以再次调用这个函数，无需重新开启屏幕分享。


### startScreenCapture

启动屏幕分享。
```
- (void)startScreenCapture:(NSView *)view 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| view | NSView * | 渲染控件所在的父控件。 |


### stopScreenCapture

停止屏幕采集。
```
- (int)stopScreenCapture
```

__返回__

0：成功；\<0：失败。


### pauseScreenCapture

暂停屏幕分享。
```
- (int)pauseScreenCapture
```

__返回__

0：成功；\<0：失败。


### resumeScreenCapture

恢复屏幕分享。
```
- (int)resumeScreenCapture
```

__返回__

0：成功；\<0：失败。


### setSubStreamEncoderParam

设置屏幕分享的编码器参数。
```
- (void)setSubStreamEncoderParam:(TRTCVideoEncParam *)param 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| param | [TRTCVideoEncParam](https://cloud.tencent.com/document/product/647/32261#trtcvideoencparam) * | 辅流编码参数，详情请参考 TRTCCloudDef.h 中的 [TRTCVideoEncParam](https://cloud.tencent.com/document/product/647/32261#trtcvideoencparam) 定义。 |

__介绍__

对应于 setVideoEncoderParam() 设置主画面的编码参数，该函数仅用于设置辅路（屏幕分享、远程播放视频）的编码参数。 
该设置决定远端用户看到的画面质量，同时也是云端录制出的视频文件的画面质量。


### setSubStreamMixVolume

设置屏幕分享的混音音量大小。
```
- (void)setSubStreamMixVolume:(NSInteger)volume 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | NSInteger | 设置的音量大小，范围0 - 100。 |

__介绍__

数值越高，辅路音量的占比越高，麦克风音量占比越小。不推荐将该参数值设置过大，数值过大容易压制麦克风的声音。


## 自定义采集和渲染
### enableCustomVideoCapture

启用视频自定义采集模式。
```
- (void)enableCustomVideoCapture:(BOOL)enable 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | BOOL | 是否启用，默认值：NO。 |

__介绍__

开启该模式后，SDK 不在运行原有的视频采集流程，只保留编码和发送能力。 您需要用 sendCustomVideoData() 不断地向 SDK 塞入自己采集的视频画面。


### sendCustomVideoData

向 SDK 投送自己采集的视频数据。
```
- (void)sendCustomVideoData:(TRTCVideoFrame *)frame 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| frame | [TRTCVideoFrame](https://cloud.tencent.com/document/product/647/32261#trtcvideoframe) * | 视频数据，支持 PixelBuffer NV12，BGRA 以及 I420 格式数据。 |

__介绍__

[TRTCVideoFrame](https://cloud.tencent.com/document/product/647/32261#trtcvideoframe) 推荐下列填写方式（其他字段不需要填写）：
- pixelFormat：推荐选择 TRTCVideoPixelFormat_NV12。
- bufferType：推荐选择 TRTCVideoBufferType_PixelBuffer。
- pixelBuffer：iOS 平台上常用的视频数据格式。
- data：视频裸数据格式，bufferType 为 NSData 时使用。
- timestamp：如果 timestamp 间隔不均匀，会严重影响音画同步和录制出的 MP4 质量。
- width：视频图像长度，bufferType 为 NSData 时填写。
- height：视频图像宽度，bufferType 为 NSData 时填写。


参考文档：[自定义采集和渲染](https://cloud.tencent.com/document/product/647/34066)。

>?
>- SDK 内部有帧率控制逻辑，目标帧率以您在 setVideoEncoderParam 中设置的为准，太快会自动丢帧，太慢则会自动补帧。
>- 可以设置 frame 中的 timestamp 为 0，相当于让 SDK 自己设置时间戳，但请“均匀”地控制 sendCustomVideoData 的调用间隔，否则会导致视频帧率不稳定。


### setLocalVideoRenderDelegate

设置本地视频的自定义渲染回调。
```
- (int)setLocalVideoRenderDelegate:(id< TRTCVideoRenderDelegate >)delegate pixelFormat:(TRTCVideoPixelFormat)pixelFormat bufferType:(TRTCVideoBufferType)bufferType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| delegate | id< [TRTCVideoRenderDelegate](https://cloud.tencent.com/document/product/647/32263#trtcvideorenderdelegate) > | 自定义渲染回调。 |
| pixelFormat | [TRTCVideoPixelFormat](https://cloud.tencent.com/document/product/647/32261#trtcvideopixelformat) | 指定回调的像素格式。 |
| bufferType | [TRTCVideoBufferType](https://cloud.tencent.com/document/product/647/32261#trtcvideobuffertype) | PixelBuffer：可以直接使用 imageWithCVImageBuffer 转成 UIImage；NSData：经过内存整理的视频数据。 |

__返回__

0：成功；\<0：错误。

__介绍__

设置此方法后，SDK 内部会跳过原来的渲染流程，并把采集到的数据回调出来，您需要自己完成画面渲染。
- pixelFormat 指定回调的数据格式，例如 NV12、i420 以及 32BGRA。
- bufferType 指定 buffer 的类型，直接使用 PixelBuffer 效率最高；使用 NSData 相当于让 SDK 在内部做了一次内存转换，因此会有额外的性能损耗。




### setRemoteVideoRenderDelegate

设置远端视频的自定义渲染回调。
```
- (int)setRemoteVideoRenderDelegate:(NSString *)userId delegate:(id< TRTCVideoRenderDelegate >)delegate pixelFormat:(TRTCVideoPixelFormat)pixelFormat bufferType:(TRTCVideoBufferType)bufferType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 指定目标 userId。 |
| delegate | id< [TRTCVideoRenderDelegate](https://cloud.tencent.com/document/product/647/32263#trtcvideorenderdelegate) > | 自定义渲染的回调。 |
| pixelFormat | [TRTCVideoPixelFormat](https://cloud.tencent.com/document/product/647/32261#trtcvideopixelformat) | 指定回调的像素格式。 |
| bufferType | [TRTCVideoBufferType](https://cloud.tencent.com/document/product/647/32261#trtcvideobuffertype) | PixelBuffer：可以直接使用 imageWithCVImageBuffer 转成 UIImage；NSData：经过内存整理的视频数据。 |

__返回__

0：成功；\<0：错误。

__介绍__

此方法同 setLocalVideoRenderDelegate，区别在于一个是本地画面的渲染回调，一个是远程画面的渲染回调。

>?调用此函数之前，需要先调用 startRemoteView 来获取远端用户的视频流（view 设置为 nil 即可），否则不会有数据回调出来。



### enableCustomAudioCapture

启用音频自定义采集模式。
```
- (void)enableCustomAudioCapture:(BOOL)enable 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | BOOL | 是否启用, true：启用；false：关闭，默认值：NO。 |

__介绍__

开启该模式后，SDK 不在运行原有的音频采集流程，只保留编码和发送能力。您需要用 sendCustomAudioData() 不断地向 SDK 塞入自己采集的音频数据。

>?由于回声抵消（AEC）需要严格的控制声音采集和播放的时间，所以开启自定义音频采集后，AEC 能力可能会失效。



### sendCustomAudioData

向 SDK 投送自己采集的音频数据。
```
- (void)sendCustomAudioData:(TRTCAudioFrame *)frame 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| frame | [TRTCAudioFrame](https://cloud.tencent.com/document/product/647/32261#trtcaudioframe) * | 音频数据。 |

__介绍__

[TRTCAudioFrame](https://cloud.tencent.com/document/product/647/32261#trtcaudioframe) 推荐如下填写方式：

- data：音频帧 buffer。音频帧数据必须是 PCM 格式，推荐每帧20ms采样数。【48000采样率、单声道的帧长度：48000 × 0.02s × 1 × 16bit = 15360bit = 1920字节】。
- sampleRate：采样率，仅支持48000。
- channel：频道数量（如果是立体声，数据是交叉的），单声道：1； 双声道：2。
- timestamp：如果 timestamp 间隔不均匀，会严重影响音画同步和录制出的 MP4 质量。


参考文档：[自定义采集和渲染](https://cloud.tencent.com/document/product/647/34066)。

>?可以设置 frame 中的 timestamp 为0，相当于让 SDK 自己设置时间戳，但请“均匀”地控制 sendCustomAudioData 的调用间隔，否则会导致声音断断续续。



### setAudioFrameDelegate

设置音频数据回调。
```
- (void)setAudioFrameDelegate:(id< TRTCAudioFrameDelegate >)delegate 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| delegate | id< [TRTCAudioFrameDelegate](https://cloud.tencent.com/document/product/647/32263#trtcaudioframedelegate) > | 音频数据回调，delegate = nil 则停止回调数据。 |

__介绍__

设置此方法，SDK 内部会把音频数据（PCM 格式）回调出来，包括：
- onCapturedAudioFrame：本机麦克风采集到的音频数据
- onPlayAudioFrame：混音前的每一路远程用户的音频数据
- onMixedPlayAudioFrame：各路音频数据混合后送入扬声器播放的音频数据。



## 自定义消息发送
### sendCustomCmdMsg

发送自定义消息给房间内所有用户。
```
- (BOOL)sendCustomCmdMsg:(NSInteger)cmdID data:(NSData *)data reliable:(BOOL)reliable ordered:(BOOL)ordered 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| cmdID | NSInteger | 消息 ID，取值范围为1 - 10。 |
| data | NSData * | 待发送的消息，最大支持1KB（1000字节）的数据大小。 |
| reliable | BOOL | 是否可靠发送，可靠发送的代价是会引入一定的延时，因为接收端要暂存一段时间的数据来等待重传。 |
| ordered | BOOL | 是否要求有序，即是否要求接收端接收的数据顺序和发送端发送的顺序一致，这会带来一定的接收延时，因为在接收端需要暂存并排序这些消息。 |

__返回__

YES：消息已经发出；NO：消息发送失败。

__介绍__

该接口可以借助音视频数据通道向当前房间里的其他用户广播您自定义的数据，但因为复用了音视频数据通道， 请务必严格控制自定义消息的发送频率和消息体的大小，否则会影响音视频数据的质量控制逻辑，造成不确定性的问题。

>?本接口有以下限制：
>- 发送消息到房间内所有用户，每秒最多能发送30条消息。
>- 每个包最大为1KB，超过则很有可能会被中间路由器或者服务器丢弃。
>- 每个客户端每秒最多能发送总计8KB数据。
>- 将 reliable 和 ordered 同时设置为 YES 或 NO，暂不支持交叉设置。
>- 强烈建议不同类型的消息使用不同的 cmdID，这样可以在要求有序的情况下减小消息时延。


### sendSEIMsg

将小数据量的自定义数据嵌入视频帧中。
```
- (BOOL)sendSEIMsg:(NSData *)data repeatCount:(int)repeatCount 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| data | NSData * | 待发送的数据，最大支持1kb（1000字节）的数据大小。 |
| repeatCount | int | 发送数据次数。 |

__返回__

YES：消息已通过限制，等待后续视频帧发送；NO：消息被限制发送。

__介绍__

与 sendCustomCmdMsg 的原理不同，sendSEIMsg 是将数据直接塞入视频数据头中。因此，即使视频帧被旁路到了直播 CDN 上，这些数据也会一直存在。由于需要把数据嵌入视频帧中，建议尽量控制数据大小，推荐使用几个字节大小的数据。
最常见的用法是把自定义的时间戳（timstamp）用 sendSEIMsg 嵌入视频帧中，实现消息和画面的完美对齐。

>?本接口有以下限制：
>- 数据在接口调用完后不会被即时发送出去，而是从下一帧视频帧开始带在视频帧中发送。
>- 发送消息到房间内所有用户，每秒最多能发送30条消息（与 sendCustomCmdMsg 共享限制）。
>- 每个包最大为1KB，若发送大量数据，会导致视频码率增大，可能导致视频画质下降甚至卡顿（与 sendCustomCmdMsg 共享限制）。
>- 每个客户端每秒最多能发送总计8KB数据（与 sendCustomCmdMsg 共享限制）。
>- 若指定多次发送（repeatCount > 1），则数据会被带在后续的连续 repeatCount 个视频帧中发送出去，同样会导致视频码率增大。
>- 如果 repeatCount > 1，多次发送，接收消息 onRecvSEIMsg 回调也可能会收到多次相同的消息，需要去重。



## 背景混音相关接口函数
### playBGM

启动播放背景音乐。
```
- (void)playBGM:(NSString *)path withBeginNotify:(void(^)(NSInteger errCode))beginNotify withProgressNotify:(void(^)(NSInteger progressMS, NSInteger durationMS))progressNotify andCompleteNotify:(void(^)(NSInteger errCode))completeNotify 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | NSString * | 音乐文件路径。 |
| beginNotify | void(^)(NSInteger errCode) | 音乐播放开始的回调通知。 |
| progressNotify | void(^)(NSInteger progressMS, NSInteger durationMS) | 音乐播放的进度通知，单位毫秒。 |
| completeNotify | void(^)(NSInteger errCode) | 音乐播放结束的回调通知。 |


### stopBGM

停止播放背景音乐。
```
- (void)stopBGM
```


### pauseBGM

暂停播放背景音乐。
```
- (void)pauseBGM
```


### resumeBGM

继续播放背景音乐。
```
- (void)resumeBGM
```


### getBGMDuration

获取音乐文件总时长，单位毫秒。
```
- (NSInteger)getBGMDuration:(NSString *)path 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | NSString * | 音乐文件路径，如果 path 为空，那么返回当前正在播放的 music 时长。 |

__返回__

成功返回时长，失败返回-1。


### setBGMPosition

设置 BGM 播放进度。
```
- (int)setBGMPosition:(NSInteger)pos 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| pos | NSInteger | 单位毫秒。 |

__返回__

0：成功；-1：失败。


### setMicVolumeOnMixing

设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小。
```
- (void)setMicVolumeOnMixing:(NSInteger)volume 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | NSInteger | 音量大小，100为正常音量，取值范围为0 - 100。 |


### setBGMVolume

设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小。
```
- (void)setBGMVolume:(NSInteger)volume 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | NSInteger | 音量大小，100为正常音量，取值范围为0 - 100。 |


### setReverbType

设置混响效果 (目前仅支持 iOS)。
```
- (void)setReverbType:(TRTCReverbType)reverbType 
```

__参数__


| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reverbType | TXReverbType | 混响类型，详见 [TRTCReverbType](https://cloud.tencent.com/document/product/647/32261#trtcreverbtype)。 |


### setVoiceChangerType

设置变声类型 (目前仅支持 iOS)。
```
- (void)setVoiceChangerType:(TRTCVoiceChangerType)voiceChangerType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| voiceChangerType |TXVoiceChangerType | 变声类型，详情请参见  [TRTCVoiceChangerType](https://cloud.tencent.com/document/product/647/32261#trtcvoicechangertype)。 |

## 音效相关接口函数
### playAudioEffect

播放音效。
```
- (void)playAudioEffect:(TRTCAudioEffectParam *)effect 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| effect | [TRTCAudioEffectParam](https://cloud.tencent.com/document/product/647/32261#trtcaudioeffectparam) * | 音效。 |

__介绍__

每个音效都需要您指定具体的 ID，您可以通过该 ID 对音效的开始、停止、音量等进行设置。 若您想同时播放多个音效，请分配不同的 ID 进行播放。如果使用同一个 ID 播放不同音效，SDK 会先停止播放旧的音效，再播放新的音效。


### setAudioEffectVolume

设置单个音效音量。
```
- (void)setAudioEffectVolume:(int)effectId volume:(int)volume 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| effectId | int | 音效 ID。 |
| volume | int | 音量大小，取值范围为0 - 100；默认值：100。 |

>?该操作会覆盖通过 setAllAudioEffectsVolume 指定的整体音效音量。

### stopAudioEffect

停止音效。
```
- (void)stopAudioEffect:(int)effectId 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| effectId | int | 音效 ID。 |


### stopAllAudioEffects

停止所有音效。
```
- (void)stopAllAudioEffects
```


### setAllAudioEffectsVolume

设置所有音效音量。
```
- (void)setAllAudioEffectsVolume:(int)volume 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 音量大小，取值范围为0 - 100；默认值：100。 |

>?该操作会覆盖通过 setAudioEffectVolume 指定的单独音效音量。

## 设备和网络测试
### startSpeedTest

开始进行网络测速（视频通话期间请勿测试，以免影响通话质量）。
```
- (void)startSpeedTest:(uint32_t)sdkAppId userId:(NSString *)userId userSig:(NSString *)userSig completion:(void(^)(TRTCSpeedTestResult *result, NSInteger completedCount, NSInteger totalCount))completion 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sdkAppId | uint32_t | 应用标识。 |
| userId | NSString * | 用户标识。 |
| userSig | NSString * | 用户签名。 |
| completion | void(^)([TRTCSpeedTestResult](https://cloud.tencent.com/document/product/647/32261#trtcspeedtestresult) *result, NSInteger completedCount, NSInteger totalCount) | 测试回调，会分多次回调。 |

__介绍__

测速结果将会用于优化 SDK 接下来的服务器选择策略，因此推荐您在用户首次通话前先进行一次测速，这将有助于我们选择最佳的服务器。 同时，如果测试结果非常不理想，您可以通过醒目的 UI 提示用户选择更好的网络。

>?测速本身会消耗一定的流量，所以也会产生少量额外的流量费用。



### stopSpeedTest

停止服务器测速。
```
- (void)stopSpeedTest
```


### startCameraDeviceTestInView

开始进行摄像头测试。
```
- (void)startCameraDeviceTestInView:(NSView *)view 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| view | NSView * | 预览控件所在的父控件。 |

>?在测试过程中可以使用 setCurrentCameraDevice 接口切换摄像头。



### stopCameraDeviceTest

结束视频测试预览。
```
- (void)stopCameraDeviceTest
```


### startMicDeviceTest

开始进行麦克风测试。
```
- (void)startMicDeviceTest:(NSInteger)interval testEcho:(void(^)(NSInteger volume))testEcho 
```

__介绍__

该方法测试麦克风是否能正常工作，volume 的取值范围为0 - 100。


### stopMicDeviceTest

停止麦克风测试。
```
- (void)stopMicDeviceTest
```


### startSpeakerDeviceTest

开始扬声器测试。
```
- (void)startSpeakerDeviceTest:(NSString *)audioFilePath onVolumeChanged:(void(^)(NSInteger volume, BOOL isLastFrame))volumeBlock 
```

__介绍__

该方法播放指定的音频文件测试播放设备是否能正常工作。如果能听到声音，说明播放设备能正常工作。


### stopSpeakerDeviceTest

停止扬声器测试。
```
- (void)stopSpeakerDeviceTest
```



## 混流转码以及 CDN 旁路推流
### setMixTranscodingConfig

设置云端的混流转码参数。
```
- (void)setMixTranscodingConfig:(TRTCTranscodingConfig *)config 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| config | [TRTCTranscodingConfig](https://cloud.tencent.com/document/product/647/32261#trtctranscodingconfig) * | 请参考 TRTCCloudDef.h 中关于 [TRTCTranscodingConfig](https://cloud.tencent.com/document/product/647/32261#trtctranscodingconfig) 的介绍。如果传入 nil 则取消云端混流转码。 |

__介绍__

该接口会向腾讯云的转码服务器发送一条指令，目的是将房间里的多路画面叠加到一路画面上。
如果您在实时音视频 [控制台](https://console.cloud.tencent.com/rav/) 中的功能配置页开启了“启动自动旁路直播”功能， 房间里的每一路画面都会有一个对应的直播 [CDN 地址](https://cloud.tencent.com/document/product/647/16826)， 此时您可以通过云端混流，将多路直播地址的画面混合成一路，这样直播 CDN 上就可以看到混合后的画面。
您可以通过转码参数来调整每一路画面的位置以及最终输出的画面质量。
参考文档：[云端混流转码](https://cloud.tencent.com/document/product/647/16827)。 
示例代码：Demo 中增加了该功能的体验入口，您可以在“更多功能”面板中看到“云端画面混合”和“分享播放地址”体验到该功能。


<pre>
【画面1】=> 解码 => =>
                        \
【画面2】=> 解码 =>  画面混合 => 编码 => 【混合后的画面】
                        /
【画面3】=> 解码 => =>
</pre>


>?关于云端混流的注意事项：
>- 云端转码会引入一定的 CDN 观看延时，大概会增加1 - 2秒。
>- 调用该函数的用户，会将多路画面混合到自己这一路的 [CDN 地址](https://cloud.tencent.com/document/product/647/16826) 上。


### startPublishCDNStream

旁路转推到指定的推流地址。
```
- (void)startPublishCDNStream:(TRTCPublishCDNParam *)param 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| param | [TRTCPublishCDNParam](https://cloud.tencent.com/document/product/647/32261#trtcpublishcdnparam) * | 请参考 TRTCCloudDef.h 中关于 [TRTCPublishCDNParam](https://cloud.tencent.com/document/product/647/32261#trtcpublishcdnparam) 的介绍。 |

__介绍__

该接口会向腾讯云的转推服务器发送一条指令，腾讯云会将当前一路的音视频画面转推到您指定的 rtmp 推流地址上。
在实时音视频 [控制台](https://console.cloud.tencent.com/rav/) 中的功能配置页开启了“启动自动旁路直播”功能后， 房间里的每一路画面都有一路默认的腾讯云 CDN 地址，所以该功能并不常用，仅在您需要适配多家 CDN 服务商时才需要关注该功能。
由于仅转推单独的一路画面到直播 CDN 并没有什么太大的意义，所以该方案通常是跟云端转码混合使用的。 也就是先通过 setMixTranscodingConfig 将房间里的多路画面混合到一路上，再转推出去。

>?关于旁路转推的注意事项：
>- 默认只支持转推到腾讯云的 rtmp [推流地址](https://cloud.tencent.com/document/product/267/32720) 上，转推其他云的需求请通过工单联系我们。
>- 调用该函数的用户，默认只会转推自己这一路画面到指定的 rtmp 推流地址上，因此通常需要配合 setMixTranscodingConfig 同时使用。
>- 在实时音视频 [控制台](https://console.cloud.tencent.com/rav/) 中的功能配置页开启了“启动自动旁路直播”功能后，房间里的每一路画面都有一路默认的腾讯云 CDN 地址，因此仅当您需要适配多家 CDN 服务商时，才需要关注该功能。

### stopPublishCDNStream

停止旁路推流。
```
- (void)stopPublishCDNStream
```



## Log 相关接口函数
### getSDKVersion

获取 SDK 版本信息。
```
+ (NSString *)getSDKVersion
```


### setLogLevel

设置 Log 输出级别。
```
+ (void)setLogLevel:(TRTCLogLevel)level 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | [TRTCLogLevel](https://cloud.tencent.com/document/product/647/32261#trtcloglevel) | 参见 TRTCLogLevel，默认值：TRTC_LOG_LEVEL_NULL。 |


### setConsoleEnabled

启用或禁用控制台日志打印。
```
+ (void)setConsoleEnabled:(BOOL)enabled 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enabled | BOOL | 指定是否启用，默认为禁止状态。 |


### setLogCompressEnabled

启用或禁用 Log 的本地压缩。
```
+ (void)setLogCompressEnabled:(BOOL)enabled 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enabled | BOOL | 指定是否启用，默认为启动状态。 |

__介绍__

开启压缩后，Log 存储体积明显减小，但需要腾讯云提供的 Python 脚本解压后才能阅读。 禁用压缩后，Log 采用明文存储，可以直接用记事本打开阅读，但占用空间较大。


### setLogDirPath

修改日志保存路径。
```
+ (void)setLogDirPath:(NSString *)path 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | NSString * | 存储日志路径。 |

>?日志文件默认保存在 sandbox Documents/log 下，如需修改，必须在所有方法前调用。



### setLogDelegate

设置日志回调。
```
+ (void)setLogDelegate:(id< TRTCLogDelegate >)logDelegate 
```


### showDebugView

显示仪表盘。
```
- (void)showDebugView:(NSInteger)showType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| showType | NSInteger | 0：不显示；1：显示精简版；2：显示全量版。 |

__介绍__

仪表盘是状态统计和事件消息浮层 view，方便调试。 



### setDebugViewMargin

设置仪表盘的边距。
```
- (void)setDebugViewMargin:(NSString *)userId margin:(TXEdgeInsets)margin 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | NSString * | 用户 ID。 |
| margin | TXEdgeInsets | 仪表盘内边距，注意这里是基于 parentView 的百分比，margin 的取值范围是0 - 1。 |

__介绍__

必须在 showDebugView 调用前设置才会生效。


### callExperimentalAPI

调用实验性 API 接口。
```
- (void)callExperimentalAPI:(NSString *)jsonStr 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| jsonStr | NSString * | 接口及参数描述的 JSON 字符串。 |

>?该接口用于调用一些实验性功能。


TRTCCloud @ TXLiteAVSDK。

腾讯云视频通话功能的主要接口类。


## 基础方法
### sharedInstance

创建 [TRTCCloud](https://cloud.tencent.com/document/product/647/32264#trtccloud) 单例。
```
TRTCCloud sharedInstance(Context context)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| context | Context | Android 上下文，内部会转为 ApplicationContext 用于系统 API 调用。 |

__返回__

[TRTCCloud](https://cloud.tencent.com/document/product/647/32264#trtccloud) 实例。

>?可以调用 destroySharedInstance 销毁单例对象。


### destroySharedInstance

销毁 [TRTCCloud](https://cloud.tencent.com/document/product/647/32264#trtccloud) 单例。
```
void destroySharedInstance()
```


### setListener

设置回调接口 TRTCCloudListener，用户获得来自 [TRTCCloud](https://cloud.tencent.com/document/product/647/32264#trtccloud) 的各种状态通知。
```
abstract void setListener(TRTCCloudListener listener)
```

__介绍__

您可以通过 [TRTCCloudListener](https://cloud.tencent.com/document/product/647/32265#trtccloudlistener) 获得来自 SDK 的各种状态通知，详见 [TRTCCloudListener](https://cloud.tencent.com/document/product/647/32265#trtccloudlistener) 中的定义。


### setListenerHandler

设置驱动 [TRTCCloudListener](https://cloud.tencent.com/document/product/647/32265#trtccloudlistener) 回调的队列。
```
abstract void setListenerHandler(Handler listenerHandler)
```

__介绍__

SDK 默认会采用 Main Thread 作为驱动 TRTCCloudListener，也就是说，如果您不指定自己的 listenerHandler， SDK 的 [TRTCCloudListener](https://cloud.tencent.com/document/product/647/32265#trtccloudlistener) 回调都将由 Main Thread 来调用。此时您在 [TRTCCloudListener](https://cloud.tencent.com/document/product/647/32265#trtccloudlistener) 的回调函数里操作 UI 是线程安全的。



## 房间相关接口函数
### enterRoom

进入房间。
```
abstract void enterRoom(TRTCCloudDef.TRTCParams param, int scene)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| param | [TRTCCloudDef.TRTCParams](https://cloud.tencent.com/document/product/647/32266#trtcparams) | 进房参数，请参考 TRTCParams。 |
| scene | int | 应用场景，目前支持视频通话（VideoCall）和在线直播（Live）两种场景。 |

__介绍__

调用接口后，您会收到来自 [TRTCCloudListener](https://cloud.tencent.com/document/product/647/32265#trtccloudlistener) 中的 onEnterRoom(result) 回调: 如果加入成功，result 会是一个正数（result > 0），表示加入房间所消耗的时间，单位是毫秒（ms）。 如果加入失败，result 会是一个负数（result < 0），表示进房失败的错误码。 进房失败的错误码含义请参见 [错误码](https://cloud.tencent.com/document/product/647/32257)。

>?不管进房是否成功，enterRoom 都必须与 exitRoom 配对使用，在调用 exitRoom 前再次调用 enterRoom 函数会导致不可预期的错误问题。



### exitRoom

离开房间。
```
abstract void exitRoom()
```

__介绍__

调用 [exitRoom()](https://cloud.tencent.com/document/product/647/32264#exitroom) 接口会执行退出房间的相关逻辑，例如释放音视频设备资源和编解码器资源等。 待资源释放完毕，SDK 会通过 [TRTCCloudListener](https://cloud.tencent.com/document/product/647/32265#trtccloudlistener) 中的 onExitRoom() 回调通知到您。
如果您要再次调用 [enterRoom()](https://cloud.tencent.com/document/product/647/32264#enterroom) 或者切换到其他的音视频 SDK，请等待 onExitRoom() 回调到来之后再执行相关操作。 否则可能会遇到摄像头或麦克风被占用等各种异常问题，比如常见的 Android 媒体音量和通话音量切换问题等等。


### switchRole

切换角色，仅适用于直播场景（TRTCAppSceneLIVE）。
```
abstract void switchRole(int role)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| role | int | 目标角色。 |

__介绍__

在直播场景下，一个用户可能需要在“观众”和“主播”之间来回切换。 您可以在进房前通过 TRTCParams 中的 role 字段确定角色，也可以通过 switchRole 在进房后切换角色。


### ConnectOtherRoom

请求跨房通话（主播 PK）。
```
abstract void ConnectOtherRoom(String param)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| param | String | JSON 字符串连麦参数，roomId 代表目标房间号，userId 代表目标用户 ID。 |

__介绍__

TRTC 中两个不同音视频房间中的主播，可以通过“跨房通话”功能拉通连麦通话功能。使用此功能时，两个主播无需退出各自原来的直播间即可进行“连麦 PK”。
例如：当房间“001”中的主播 A 通过 connectOtherRoom() 跟房间“002”中的主播 B 拉通跨房通话后， 房间“001”中的用户都会收到主播 B 的 onUserEnter(B) 回调和 onUserVideoAvailable(B，true) 回调。 房间“002”中的用户都会收到主播 A 的 onUserEnter(A) 回调和 onUserVideoAvailable(A，true) 回调。
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
- roomId：房间“001”中的主播 A 要跟房间“002”中的主播 B 连麦，主播 A 调用 [ConnectOtherRoom()](https://cloud.tencent.com/document/product/647/32264#connectotherroom) 时 roomId 应指定为“002”。
- userId：房间“001”中的主播 A 要跟房间“002”中的主播 B 连麦，主播 A 调用 [ConnectOtherRoom()](https://cloud.tencent.com/document/product/647/32264#connectotherroom) 时 userId 应指定为 B 的 userId。


跨房通话的请求结果会通过 [TRTCCloudListener](https://cloud.tencent.com/document/product/647/32265#trtccloudlistener) 中的 onConnectOtherRoom() 回调通知给您。


<pre>
  JSONObject jsonObj = new JSONObject();
  jsonObj.put("roomId"， 002);
  jsonObj.put("userId"， "userB");
  trtc.ConnectOtherRoom(jsonObj.toString());
</pre>


### DisconnectOtherRoom

退出跨房通话。
```
abstract void DisconnectOtherRoom()
```

__介绍__

跨房通话的退出结果会通过 TRTCCloudListener.java 中的 onDisconnectOtherRoom 回调通知给您。



## 视频相关接口函数
### startLocalPreview

开启本地视频的预览画面。
```
abstract void startLocalPreview(boolean frontCamera, TXCloudVideoView view)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| frontCamera | boolean | true：前置摄像头；false：后置摄像头。 |
| view | TXCloudVideoView | 承载视频画面的控件。 |

__介绍__

当开始渲染首帧摄像头画面时，您会收到 [TRTCCloudListener](https://cloud.tencent.com/document/product/647/32265#trtccloudlistener) 中的 onFirstVideoFrame(null) 回调。


### stopLocalPreview

停止本地视频采集及预览。
```
abstract void stopLocalPreview()
```


### muteLocalVideo

是否屏蔽自己的视频画面。
```
abstract void muteLocalVideo(boolean mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | boolean | true：屏蔽；false：开启。 |

__介绍__

当屏蔽本地视频后，房间里的其它成员将会收到 onUserVideoAvailable 回调通知。


### startRemoteView

开始显示远端视频画面。
```
abstract void startRemoteView(String userId, TXCloudVideoView view)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 对方的用户标识。 |
| view | TXCloudVideoView | 承载视频画面的控件。 |

__介绍__

在收到 SDK 的 onUserVideoAvailable(userId， true) 通知时，可以获知该远程用户开启了视频，此后调用 startRemoteView(userId) 接口加载该用户的远程画面，可以用 loading 动画优化加载过程中的等待体验。 待该用户的首帧画面开始显示时，您会收到 onFirstVideoFrame(userId) 事件回调。


### stopRemoteView

停止显示远端视频画面。
```
abstract void stopRemoteView(String userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 对方的用户标识。 |

__介绍__

调用此接口后，SDK 会停止接收该用户的远程视频流，同时会清理相关的视频显示资源。


### stopAllRemoteView

停止显示所有远端视频画面。
```
abstract void stopAllRemoteView()
```

>?如果有屏幕分享的画面在显示，则屏幕分享的画面也会一并被关闭。



### muteRemoteVideoStream

暂停接收指定的远端视频流。
```
abstract void muteRemoteVideoStream(String userId, boolean mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 对方的用户标识。 |
| mute | boolean | 是否停止接收。 |

__介绍__

该接口仅停止接收远程用户的视频流，但并不释放显示资源，所以视频画面会冻屏在 mute 前的最后一帧。


### muteAllRemoteVideoStreams

停止接收所有远端视频流。
```
abstract void muteAllRemoteVideoStreams(boolean mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | boolean | 是否停止接收。 |


### setVideoEncoderParam

设置视频编码器相关参数。
```
abstract void setVideoEncoderParam(TRTCCloudDef.TRTCVideoEncParam param)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| param | [TRTCCloudDef.TRTCVideoEncParam](https://cloud.tencent.com/document/product/647/32266#trtcvideoencparam) | 视频编码参数，详情请参考 TRTCCloudDef.java 中的 TRTCVideoEncParam 定义。 |

__介绍__

该设置决定了远端用户看到的画面质量（同时也是云端录制出的视频文件的画面质量）。


### setNetworkQosParam

设置网络流控相关参数。
```
abstract void setNetworkQosParam(TRTCCloudDef.TRTCNetworkQosParam param)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| param | [TRTCCloudDef.TRTCNetworkQosParam](https://cloud.tencent.com/document/product/647/32266#trtcnetworkqosparam) | 网络流控参数，详情请参考 TRTCCloudDef.java 中的 TRTCNetworkQosParam 定义。 |

__介绍__

该设置决定了 SDK 在各种网络环境下的调控策略（例如弱网下是“保清晰”还是“保流畅”）。


### setLocalViewFillMode

设置本地图像的渲染模式。
```
abstract void setLocalViewFillMode(int mode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mode | int | 填充（画面可能会被拉伸裁剪）或适应（画面可能会有黑边）。 |


### setRemoteViewFillMode

设置远端图像的渲染模式。
```
abstract void setRemoteViewFillMode(String userId, int mode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。 |
| mode | int | 填充（画面可能会被拉伸裁剪）或适应（画面可能会有黑边）。 |


### setLocalViewRotation

设置本地图像的顺时针旋转角度。
```
abstract void setLocalViewRotation(int rotation)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rotation | int | rotation 支持 TRTC_VIDEO_ROTATION_90、TRTC_VIDEO_ROTATION_180、TRTC_VIDEO_ROTATION_270 旋转角度。 |


### setRemoteViewRotation

设置远端图像的顺时针旋转角度。
```
abstract void setRemoteViewRotation(String userId, int rotation)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。 |
| rotation | int | 支持 TRTC_VIDEO_ROTATION_90、TRTC_VIDEO_ROTATION_180、TRTC_VIDEO_ROTATION_270 旋转角度。 |


### setVideoEncoderRotation

设置视频编码输出的（也就是远端用户观看到的，以及服务器录制下来的）画面方向。
```
abstract void setVideoEncoderRotation(int rotation)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rotation | int | 目前支持 TRTC_VIDEO_ROTATION_0 和 TRTC_VIDEO_ROTATION_180 两个旋转角度。 |

__介绍__

当用户的手机或者 Android Pad 做了一个180度旋转时，由于摄像头的采集方向没有变，所以另一边的用户看到的画面是上下颠倒的， 在这种情况下，您可以通过该接口将 SDK 输出到对方的画面旋转180度，这样可以可以确保对方看到的画面依然正常。


### setLocalViewMirror

设置本地摄像头预览画面的镜像模式。
```
abstract void setLocalViewMirror(int mirrorType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mirrorType | int | mirrorType TRTC_VIDEO_MIRROR_TYPE_AUTO：SDK 决定镜像方式：前置摄像头镜像，后置摄像头不镜像。 TRTC_VIDEO_MIRROR_TYPE_ENABLE：前置摄像头和后置摄像头都镜像。 TRTC_VIDEO_MIRROR_TYPE_DISABLE：前置摄像头和后置摄像头都不镜像。 |


### setVideoEncoderMirror

设置编码器输出的画面镜像模式。
```
abstract void setVideoEncoderMirror(boolean mirror)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mirror | boolean | true：镜像；false：不镜像；默认是 false。 |

__介绍__

该接口不改变本地摄像头的预览画面，但会改变另一端用户看到的（以及服务器录制下来的）画面效果。


### setGSensorMode

设置重力感应的适应模式。
```
abstract void setGSensorMode(int mode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mode | int | 重力感应模式，详情请参考 TRTC_GSENSOR_MODE 的定义。 |


### enableEncSmallVideoStream

开启大小画面双路编码模式。
```
abstract int enableEncSmallVideoStream(boolean enable, TRTCCloudDef.TRTCVideoEncParam smallVideoEncParam)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | 是否开启小画面编码。 |
| smallVideoEncParam | [TRTCCloudDef.TRTCVideoEncParam](https://cloud.tencent.com/document/product/647/32266#trtcvideoencparam) | 小流的视频参数。 |

__返回__

0:成功；-1:大画面已经是最低画质。

__介绍__

如果当前用户是房间中的主要角色（例如主播、老师、主持人等），并且使用 PC 或者 Mac 环境，可以开启该模式。 开启该模式后，当前用户会同时输出【高清】和【低清】两路视频流（但只有一路音频流）。 对于开启该模式的当前用户，会占用更多的网络带宽，并且会更加消耗 CPU 计算资源。
对于同一房间的远程观众而言：
- 如果有些人的下行网络很好，可以选择观看【高清】画面
- 如果有些人的下行网络不好，可以选择观看【低清】画面。

>?双路编码开启后，会消耗更多的 CPU 和 网络带宽，所以对于 iMac、Windows 或者高性能 Pad 可以考虑开启，但请不要在手机端开启。



### setRemoteVideoStreamType

选定观看指定 uid 的大画面还是小画面。
```
abstract int setRemoteVideoStreamType(String userId, int streamType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。 |
| streamType | int | 视频流类型，即选择看大画面还是小画面。 |

__介绍__

此功能需要该 uid 通过 enableEncSmallVideoStream 提前开启双路编码模式。 如果该 uid 没有开启双路编码模式，则此操作将无任何反应。


### setPriorRemoteVideoStreamType

设定观看方优先选择的视频质量。
```
abstract int setPriorRemoteVideoStreamType(int streamType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| streamType | int | 默认观看大画面还是小画面。 |

__介绍__

低端设备推荐优先选择低清晰度的小画面。 如果对方没有开启双路视频模式，则此操作无效。



## 音频相关接口函数
### startLocalAudio

开启本地音频的采集和上行。
```
abstract void startLocalAudio()
```

__介绍__

该函数会启动麦克风采集，并将音频数据传输给房间里的其他用户。 SDK 并不会默认开启本地的音频上行，也就说，如果您不调用这个函数，房间里的其他用户就听不到您的声音。

>?该函数会检查麦克风的使用权限，如果当前 App 没有麦克风权限，SDK 会向用户申请开启。



### stopLocalAudio

关闭本地音频的采集和上行。
```
abstract void stopLocalAudio()
```

__介绍__

当关闭本地音频的采集和上行，房间里的其它成员会收到 onUserAudioAvailable(false) 回调通知。


### muteLocalAudio

静音本地的音频。
```
abstract void muteLocalAudio(boolean mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | boolean | true：屏蔽；false：开启。 |

__介绍__

当静音本地音频后，房间里的其它成员会收到 onUserAudioAvailable(false) 回调通知。
与 stopLocalAudio 不同之处在于，muteLocalAudio 并不会停止发送音视频数据，而是会继续发送码率极低的静音包。 在对录制质量要求很高的场景中，选择 muteLocalAudio 是更好的选择，能录制出兼容性更好的 MP4 文件。 这是由于 MP4 等视频文件格式，对于音频的连续性是要求很高的，简单粗暴地 stopLocalAudio 会导致录制出的 MP4 不易播放。


### setAudioRoute

设置音频路由。
```
abstract void setAudioRoute(int route)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| route | int | 音频路由，即声音由哪里输出（扬声器、听筒）。 |

__介绍__

微信和手机 QQ 里的视频通话功能，都有一个免提模式，开启后就不用把手机贴在耳朵上，这个功能就是基于音频路由实现的。 一般手机都有两个扬声器，一个是位于顶部的听筒扬声器，声音偏小；一个是位于底部的立体声扬声器，声音偏大。 设置音频路由的作用就是要决定声音从哪个扬声器播放出来。


### muteRemoteAudio

静音掉某一个用户的声音。
```
abstract void muteRemoteAudio(String userId, boolean mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 对方的用户 ID。 |
| mute | boolean | true：静音；false：非静音。 |


### muteAllRemoteAudio

静音掉所有用户的声音。
```
abstract void muteAllRemoteAudio(boolean mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | boolean | true：静音；false：非静音。 |


### enableAudioVolumeEvaluation

启用音量大小提示。
```
abstract void enableAudioVolumeEvaluation(int intervalMs)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| intervalMs | int | 决定了 onUserVoiceVolume 回调的触发间隔，单位为ms，最小间隔为100ms，如果小于等于0则会关闭回调，建议设置为300ms；详细的回调规则请参考 onUserVoiceVolume 的注释说明。 |

__介绍__

开启后会在 onUserVoiceVolume 中获取到 SDK 对音量大小值的评估。 我们在 Demo 中有一个音量大小的提示条，就是基于这个接口实现的。 如希望打开此功能，请在 [startLocalAudio()](https://cloud.tencent.com/document/product/647/32264#startlocalaudio) 之前调用。


### startAudioRecording

开始录音。
```
abstract int startAudioRecording(TRTCCloudDef.TRTCAudioRecordingParams TRTCAudioRecordingParams)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| TRTCAudioRecordingParams | [TRTCCloudDef.TRTCAudioRecordingParams](https://cloud.tencent.com/document/product/647/32266#trtcaudiorecordingparams) | 录音参数，请参考TRTCAudioRecordingParams。 |

__返回__

0：成功；-1：录音已开始；-2：文件或目录创建失败；-3：后缀指定的音频格式不支持。

__介绍__

该方法调用后， SDK 会将通话过程中的所有音频（包括本地音频，远端音频，BGM 等）录制到一个文件里。 无论是否进房，调用该接口都生效。如果调用 exitRoom 时还在录音，录音会自动停止。


### stopAudioRecording

停止录音。
```
abstract void stopAudioRecording()
```

__介绍__

如果调用 exitRoom 时还在录音，录音会自动停止。



## 摄像头相关接口函数
### switchCamera

切换摄像头。
```
abstract void switchCamera()
```


### isCameraZoomSupported

查询当前摄像头是否支持缩放。
```
abstract boolean isCameraZoomSupported()
```


### setZoom

设置摄像头缩放因子（焦距）。
```
abstract void setZoom(int distance)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| distance | int | 取值范围为1 - 5，数值越大，焦距越远。 |

__介绍__

取值范围1 - 5，当为1的时候为最远视角（正常镜头），当为5的时候为最近视角（放大镜头）。 这里最大值推荐为5，超过5后视频数据会变得模糊不清。


### isCameraTorchSupported

查询是否支持开关闪光灯（手电筒模式）。
```
abstract boolean isCameraTorchSupported()
```


### enableTorch

开关闪光灯。
```
abstract boolean enableTorch(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：开启；false：关闭。 |


### isCameraFocusPositionInPreviewSupported

查询是否支持设置焦点。
```
abstract boolean isCameraFocusPositionInPreviewSupported()
```


### setFocusPosition

设置摄像头焦点。
```
abstract void setFocusPosition(int x, int y)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| x | int | 对焦位置 x 坐标。 |
| y | int | 对焦位置 y 坐标。 |


### isCameraAutoFocusFaceModeSupported

查询是否支持自动识别人脸位置。
```
abstract boolean isCameraAutoFocusFaceModeSupported()
```



## 美颜滤镜相关接口函数
### setBeautyStyle

设置美颜、美白、红润效果级别。
```
abstract void setBeautyStyle(int beautyStyle, int beautyLevel, int whitenessLevel, int ruddinessLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| beautyStyle | int | 美颜风格，光滑或者自然，光滑风格磨皮更加明显，适合娱乐场景。 |
| beautyLevel | int | 美颜级别，取值范围0 - 9； 0表示关闭，1 - 9值越大，效果越明显。 |
| whitenessLevel | int | 美白级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |
| ruddinessLevel | int | 红润级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |

__介绍__

SDK 内部集成了两套风格不同的磨皮算法，一套我们取名叫“光滑”，适用于美女秀场，效果比较明显。 另一套我们取名“自然”，磨皮算法更多地保留了面部细节，主观感受上会更加自然。


### setFilter

设置指定素材滤镜特效。
```
abstract void setFilter(Bitmap image)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| image | Bitmap | 指定素材，即颜色查找表图片。**必须使用 png 格式**。 |


### setFilterConcentration

设置滤镜浓度。
```
abstract void setFilterConcentration(float concentration)
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
abstract void setWatermark(Bitmap image, int streamType, float x, float y, float width)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| image | Bitmap | 水印图片，**必须使用透明底的 png 格式**。 |
| streamType | int | 如果要给屏幕分享的一路也设置水印，需要调用两次的 setWatermark。 |
| x | float | 归一化水印位置的 X 轴坐标，取值[0,1]。 |
| y | float | 归一化水印位置的 Y 轴坐标，取值[0,1]。 |
| width | float | 归一化水印宽度，取值[0,1]。 |

__介绍__

水印的位置是通过 x， y， width 来指定的
- x：水印的坐标，取值范围为0 - 1的浮点数。
- y：水印的坐标，取值范围为0 - 1的浮点数。
- width：水印的宽度，取值范围为0 - 1的浮点数。


举例：如果当前编码分辨率是540 × 960，(x， y， width) 设置为（0.1， 0.1， 0.2） 那么：水印的左上坐标点就是 (540 × 0.1， 960 × 0.1)，也就是 (54， 96)，水印的宽度是 540 × 0.2 = 108px，高度自动计算。


### setEyeScaleLevel

setEyeScaleLevel 设置大眼级别（商用企业版有效，其它版本设置此参数无效）。
```
abstract void setEyeScaleLevel(int eyeScaleLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| eyeScaleLevel | int | 大眼级别取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setFaceSlimLevel

设置瘦脸级别（商用企业版有效，其它版本设置此参数无效）。
```
abstract void setFaceSlimLevel(int faceScaleLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| faceScaleLevel | int | 瘦脸级别取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setFaceVLevel

设置V脸级别（商用企业版有效，其它版本设置此参数无效）。
```
abstract void setFaceVLevel(int faceVLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| faceVLevel | int | V脸级别取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setFaceShortLevel

设置短脸级别（商用企业版有效，其它版本设置此参数无效）。
```
abstract void setFaceShortLevel(int faceShortlevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| faceShortlevel | int | 短脸级别取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setChinLevel

设置下巴拉伸或收缩（商用企业版有效，其它版本设置此参数无效）。
```
abstract void setChinLevel(int chinLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| chinLevel | int | 下巴拉伸或收缩级别取值范围0 - 9；0表示关闭，<0表示收缩，>0表示拉伸。 |


### setNoseSlimLevel

设置瘦鼻级别（商用企业版有效，其它版本设置此参数无效）。
```
abstract void setNoseSlimLevel(int noseSlimLevel)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| noseSlimLevel | int | 瘦鼻级别取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。 |


### setGreenScreenFile

设置绿幕背景视频（商用企业版有效，其它版本设置此参数无效）。
```
abstract boolean setGreenScreenFile(String file)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| file | String | 视频文件路径。支持 MP4；null：表示关闭特效。 |

__介绍__

此处的绿幕功能并非智能抠背，它需要被拍摄者的背后有一块绿色的幕布来辅助产生特效。


### selectMotionTmpl

选择使用哪一款 AI 动效挂件（商用企业版有效，其它版本设置此参数无效）。
```
abstract void selectMotionTmpl(String motionPath)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| motionPath | String | 动效完整路径。 |


### setMotionMute

设置动效静音（商用企业版有效，其它版本设置此参数无效）。
```
abstract void setMotionMute(boolean motionMute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| motionMute | boolean | true：静音；false：不静音。 |

__介绍__

有些挂件本身会有声音特效，通过此 API 可以关闭这些特效播放时所带的声音效果。



## 辅流相关接口函数
### startRemoteSubStreamView

开始显示远端用户的屏幕分享画面。
```
abstract void startRemoteSubStreamView(String userId, TXCloudVideoView view)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 对方的用户标识。 |
| view | TXCloudVideoView | 渲染控件。 |

__介绍__

对应于 [startRemoteView()](https://cloud.tencent.com/document/product/647/32264#startremoteview) 用于显示主画面，该接口只能用于显示辅路（屏幕分享、远程播片）画面。

>?请在 onUserSubStreamAvailable 回调后再调用这个接口。



### stopRemoteSubStreamView

停止显示远端用户的屏幕分享画面。
```
abstract void stopRemoteSubStreamView(String userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 对方的用户标识。 |


### setRemoteSubStreamViewFillMode

设置屏幕分享画面的显示模式。
```
abstract void setRemoteSubStreamViewFillMode(String userId, int mode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户的 ID。 |
| mode | int | 填充（画面可能会被拉伸裁剪）或适应（画面可能会有黑边）。 |

__介绍__

对应于 [setRemoteViewFillMode()](https://cloud.tencent.com/document/product/647/32264#setremoteviewfillmode) 于设置主画面的显示模式，该接口用于设置远端的辅路（屏幕分享、远程播片）画面。



## 自定义采集和渲染
### enableCustomVideoCapture

启用视频自定义采集模式。
```
abstract void enableCustomVideoCapture(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | 是否启用 true：启用；false：关闭。 |

__介绍__

开启该模式后，SDK 不在运行原有的视频采集流程，只保留编码和发送能力。 您需要用 [sendCustomVideoData()](https://cloud.tencent.com/document/product/647/32264#sendcustomvideodata) 不断地向 SDK 塞入自己采集的视频画面。


### sendCustomVideoData

向 SDK 投送自己采集的视频数据。
```
abstract void sendCustomVideoData(TRTCCloudDef.TRTCVideoFrame frame)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| frame | [TRTCCloudDef.TRTCVideoFrame](https://cloud.tencent.com/document/product/647/32266#trtcvideoframe) | 视频数据，如果是 buffer 方案，请设置 data 字段；如果是 texture 方案，请设置 TRTCTexture 对象。 |

__介绍__

Android 平台有两种的方案：buffer
- buffer 方案：对接起来比较简单，但是性能较差，不适合分辨率较高的场景。
- texture 方案：对接需要一定的 OpenGL 基础，但是性能较好，640 × 360 以上的分辨率请采用该方案。


参考文档：[自定义采集和渲染](https://cloud.tencent.com/document/product/647/34066)。

>?
>- SDK 内部有帧率控制逻辑，目标帧率以您在 setVideoEncoderParam 中设置的为准，太快会自动丢帧，太慢则会自动补帧。
>- 可以设置 frame 中的 timestamp 为 0，相当于让 SDK 自己设置时间戳，但请“均匀”地控制 sendCustomVideoData 的调用间隔，否则会导致视频帧率不稳定。


### setLocalVideoRenderListener

设置本地视频的自定义渲染回调。
```
abstract int setLocalVideoRenderListener(int pixelFormat, int bufferType, TRTCCloudListener.TRTCVideoRenderListener listener)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| pixelFormat | int | 指定视频帧的像素格式，如 TRTC_VIDEO_PIXEL_FORMAT_I420 或 TRTC_VIDEO_PIXEL_FORMAT_Texture_2D。 |
| bufferType | int | 指定视频帧的数据结构，TRTC_VIDEO_BUFFER_TYPE_BYTE_BUFFER 或 TRTC_VIDEO_BUFFER_TYPE_BYTE_ARRAY 对应 pixelFormat 为 TRTC_VIDEO_PIXEL_FORMAT_I420；TRTC_VIDEO_BUFFER_TYPE_TEXTURE 对应 pixelFormat 为 TRTC_VIDEO_PIXEL_FORMAT_Texture_2D。 |
| listener | [TRTCCloudListener.TRTCVideoRenderListener](https://cloud.tencent.com/document/product/647/32265#trtcvideorenderlistener) | 自定义视频渲染回调，每一帧视频数据回调一次。 |

__返回__

0：成功；<0：错误。

__介绍__

设置此方法后，SDK 内部会跳过自己原来的渲染流程，并把采集到的数据回调出来，您需要自己完成画面的渲染。
- pixelFormat 指定回调的数据格式，目前支持 Texture2D 和 I420 两种格式。
- bufferType 指定 buffer 的类型，BYTE_BUFFER 适合在 jni 层使用，BYTE_ARRAY 则可用于 Java 层的直接操作。


参考文档：[自定义采集和渲染](https://cloud.tencent.com/document/product/647/34066)。


### setRemoteVideoRenderListener

设置远端视频的自定义渲染回调。
```
abstract int setRemoteVideoRenderListener(String userId, int pixelFormat, int bufferType, TRTCCloudListener.TRTCVideoRenderListener listener)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 对方的用户标识。 |
| pixelFormat | int | 指定视频帧的像素格式，目前仅支持 TRTC_VIDEO_PIXEL_FORMAT_I420。 |
| bufferType | int | 指定视频帧的数据结构，如 TRTC_VIDEO_BUFFER_TYPE_BYTE_BUFFER， TRTC_VIDEO_BUFFER_TYPE_BYTE_ARRAY。 |
| listener | [TRTCCloudListener.TRTCVideoRenderListener](https://cloud.tencent.com/document/product/647/32265#trtcvideorenderlistener) | 自定义视频渲染回调，每一帧视频数据回调一次。 |

__返回__

0：成功；<0：错误。

__介绍__

此方法同 setLocalVideoRenderListener，区别在于一个是本地画面的渲染回调，一个是远程画面的渲染回调。 实际使用时，需要先调用 startRemoteView(userid， null) 启动远程视频流的拉取，并将 view 设置为 null， 否则SDK 不会启动自定义渲染流程，该 listener 的回调函数不会被触发。
参考文档：[自定义采集和渲染](https://cloud.tencent.com/document/product/647/34066)。


### enableCustomAudioCapture

启用音频自定义采集模式。
```
abstract void enableCustomAudioCapture(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | 是否启用 true：启用；false：关闭。 |

__介绍__

开启该模式后，SDK 不在运行原有的音频采集流程，只保留编码和发送能力。 您需要用 [sendCustomAudioData()](https://cloud.tencent.com/document/product/647/32264#sendcustomaudiodata) 不断地向 SDK 塞入自己采集的视频画面。


### sendCustomAudioData

向 SDK 投送自己采集的音频数据。
```
abstract void sendCustomAudioData(TRTCCloudDef.TRTCAudioFrame frame)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| frame | [TRTCCloudDef.TRTCAudioFrame](https://cloud.tencent.com/document/product/647/32266#trtcaudioframe) | 音频帧。目前只支持单声道，仅支持48K采样率。 |

__介绍__

TRTCAudioFrame 推荐如下填写方式：
- data：音频帧 buffer。音频帧数据必须是 PCM 格式，推荐每帧20ms采样数。【48000采样率、单声道的帧长度：48000 × 0.02s × 1 × 16bit = 15360bit = 1920字节】。
- sampleRate：采样率，仅支持48000。
- channel：频道数量（如果是立体声，数据是交叉的），单声道：1； 双声道：2。
- timestamp：如果 timestamp 间隔不均匀，会严重影响音画同步和录制出的 MP4 质量。


参考文档：[自定义采集和渲染](https://cloud.tencent.com/document/product/647/34066)。

>?可以设置 frame 中的 timestamp 为 0，相当于让 SDK 自己设置时间戳，但请“均匀”地控制 sendCustomAudioData 的调用间隔，否则会导致声音断断续续。



### setAudioFrameListener

设置音频数据回调。
```
abstract void setAudioFrameListener(TRTCCloudListener.TRTCAudioFrameListener listener)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| listener | [TRTCCloudListener.TRTCAudioFrameListener](https://cloud.tencent.com/document/product/647/32265#trtcaudioframelistener) | 音频数据回调，listener = null 则停止回调数据。 |

__介绍__

设置此方法，SDK 内部会把音频数据（PCM 格式）回调出来，包括：
- onCapturedAudioFrame：本机麦克风采集到的音频数据
- onPlayAudioFrame：混音前的每一路远程用户的音频数据
- onMixedPlayAudioFrame：各路音频数据混合后送入扬声器播放的音频数据。



## 自定义消息发送
### sendCustomCmdMsg

发送自定义消息给房间内所有用户。
```
abstract boolean sendCustomCmdMsg(int cmdID, byte [] data, boolean reliable, boolean ordered)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| cmdID | int | 消息 ID，取值范围为1 - 10。 |
| data | byte [] | 待发送的消息，最大支持1KB（1000字节）的数据大小。 |
| reliable | boolean | 是否可靠发送，可靠发送的代价是会引入一定的延时，因为接收端要暂存一段时间的数据来等待重传。 |
| ordered | boolean | 是否要求有序，即是否要求接收端接收的数据顺序和发送端发送的顺序一致，这会带来一定的接收延时，因为在接收端需要暂存并排序这些消息。 |

__返回__

true：消息已经发出；false：消息发送失败。

__介绍__

该接口可以借助音视频数据通道向当前房间里的其他用户广播您自定义的数据，但因为复用了音视频数据通道， 请务必严格控制自定义消息的发送频率和消息体的大小，否则会影响音视频数据的质量控制逻辑，造成不确定性的问题。

>?本接口有以下限制：
>- 发送消息到房间内所有用户，每秒最多能发送30条消息。
>- 每个包最大为1KB，超过则很有可能会被中间路由器或者服务器丢弃。
>- 每个客户端每秒最多能发送总计8KB数据。
>- 将 reliable 和 ordered 同时设置为 true 或 false，暂不支持交叉设置。
>- 强烈建议不同类型的消息使用不同的 cmdID，这样可以在要求有序的情况下减小消息时延。


### sendSEIMsg

将小数据量的自定义数据嵌入视频帧中。
```
abstract boolean sendSEIMsg(byte [] data, int repeatCount)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| data | byte [] | 待发送的数据，最大支持1kb（1000字节）的数据大小。 |
| repeatCount | int | 发送数据次数。 |

__返回__

true：消息已通过限制，等待后续视频帧发送；false：消息被限制发送。

__介绍__

跟 sendCustomCmdMsg 的原理不同，sendSEIMsg 是将数据直接塞入视频数据头中。因此，即使视频帧被旁路到了直播 CDN 上， 这些数据也会一直存在。但是由于要把数据嵌入视频帧中，所以数据本身不能太大，推荐几个字节就好。
最常见的用法是把自定义的时间戳（timstamp）用 sendSEIMsg 嵌入视频帧中，这种方案的最大好处就是可以实现消息和画面的完美对齐。

>?本接口有以下限制：
>- 数据在接口调用完后不会被即时发送出去，而是从下一帧视频帧开始带在视频帧中发送。
>- 发送消息到房间内所有用户，每秒最多能发送30条消息（与 sendCustomCmdMsg 共享限制）。
>- 每个包最大为1KB，若发送大量数据，会导致视频码率增大，可能导致视频画质下降甚至卡顿（与 sendCustomCmdMsg 共享限制）。
>- 每个客户端每秒最多能发送总计8KB数据（与 sendCustomCmdMsg 共享限制）。
>- 若指定多次发送（repeatCount>1），则数据会被带在后续的连续 repeatCount 个视频帧中发送出去，同样会导致视频码率增大。
>- 如果 repeatCount>1，多次发送，接收消息 onRecvSEIMsg 回调也可能会收到多次相同的消息，需要去重。



## 背景混音相关接口函数
### playBGM

启动播放背景音乐。
```
abstract void playBGM(String path, BGMNotify notify)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | String | 音乐文件路径。 |
| notify | [BGMNotify](https://cloud.tencent.com/document/product/647/32264#.E6.92.AD.E6.94.BE.E8.83.8C.E6.99.AF.E9.9F.B3.E4.B9.90.E7.9A.84.E5.9B.9E.E8.B0.83.E6.8E.A5.E5.8F.A3) | 播放背景音乐的回调。 |


### stopBGM

停止播放背景音乐。
```
abstract void stopBGM()
```


### pauseBGM

暂停播放背景音乐。
```
abstract void pauseBGM()
```


### resumeBGM

继续播放背景音乐。
```
abstract void resumeBGM()
```


### getBGMDuration

获取音乐文件总时长，单位毫秒。
```
abstract int getBGMDuration(String path)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | String | 音乐文件路径，如果 path 为空，那么返回当前正在播放的 music 时长。 |

__返回__

成功返回时长，失败返回-1。

### setBGMPosition

设置 BGM 播放进度。

```
abstract int setBGMPosition(int pos)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| pos | int | 单位毫秒。 |

__返回__

0：成功；-1：失败。


### setMicVolumeOnMixing

设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小。
```
abstract void setMicVolumeOnMixing(int volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 音量大小，100为正常音量，取值范围为0 - 200。 |


### setBGMVolume

设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小。
```
abstract void setBGMVolume(int volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 音量大小，100为正常音量，取值范围为0 - 200，如果需要调大背景音量可以设置更大的值。 |


### setReverbType

设置混响效果。
```
abstract void setReverbType(int reverbType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reverbType | int | 混响类型，详见 TRTC_REVERB_TYPE。 |


### setVoiceChangerType

设置变声类型。
```
abstract boolean setVoiceChangerType(int voiceChangerType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| voiceChangerType | int | 变声类型, 详见 TRTC_VOICE_CHANGER_TYPE。 |



## 网络测试
### startSpeedTest

开始进行网络测速（视频通话期间请勿测试，以免影响通话质量）。
```
abstract void startSpeedTest(int sdkAppId, String userId, String userSig)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sdkAppId | int | 应用标识。 |
| userId | String | 用户标识。 |
| userSig | String | 用户签名。 |

__介绍__

测速结果将会用于优化 SDK 接下来的服务器选择策略，因此推荐您在用户首次通话前先进行一次测速，这将有助于我们选择最佳的服务器。 同时，如果测试结果非常不理想，您可以通过醒目的 UI 提示用户选择更好的网络。 测试结果通过 [TRTCCloudListener.onSpeedTest](https://cloud.tencent.com/document/product/647/32265#onspeedtest) 回调出来。

>?测速本身会消耗一定的流量，所以也会产生少量额外的流量费用。



### stopSpeedTest

停止服务器测速。
```
abstract void stopSpeedTest()
```



## 混流转码并发布到 CDN
### setMixTranscodingConfig

设置云端的混流转码参数。
```
abstract void setMixTranscodingConfig(TRTCCloudDef.TRTCTranscodingConfig config)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| config | [TRTCCloudDef.TRTCTranscodingConfig](https://cloud.tencent.com/document/product/647/32266#trtctranscodingconfig) | 请参考 TRTCCloudDef.java 中关于 TRTCTranscodingConfig 的介绍。如果传入 null 则取消云端混流转码。 |

__介绍__

该接口会向腾讯云的转码服务器发送一条指令，目的是将房间里的多路画面叠加到一路画面上。
如果您在实时音视频 [控制台](https://console.cloud.tencent.com/rav/) 中的功能配置页开启了“启动自动旁路直播”功能， 房间里的每一路画面都会有一个对应的直播 [CDN 地址](https://cloud.tencent.com/document/product/647/16826)， 此时您可以通过云端混流，将多路直播地址的画面混合成一路，这样直播 CDN 上就可以看到混合后的画面。
您可以通过转码参数来调整每一路画面的位置以及最终输出的画面质量。
参考文档：[云端混流转码](https://cloud.tencent.com/document/product/647/16827)。 示例代码：我们在 Demo 中增加了该功能的体验入口，您可以在“更多功能”面板中看到“云端画面混合”和“分享播放地址”体验到该功能。


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
abstract void startPublishCDNStream(TRTCCloudDef.TRTCPublishCDNParam param)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| param | [TRTCCloudDef.TRTCPublishCDNParam](https://cloud.tencent.com/document/product/647/32266#trtcpublishcdnparam) | 请参考 TRTCCloudDef.java 中关于 TRTCPublishCDNParam 的介绍。 |

__介绍__

该接口会向腾讯云的转推服务器发送一条指令，腾讯云会将当前一路的音视频画面转推到您指定的 rtmp 推流地址上。
在实时音视频 [控制台](https://console.cloud.tencent.com/rav/) 中的功能配置页开启了“启动自动旁路直播”功能后， 房间里的每一路画面都有一路默认的腾讯云 CDN 地址，所以该功能并不常用，仅在您需要适配多家 CDN 服务商时才需要关注该功能。
由于仅转推单独的一路画面到直播 CDN 并没有什么太大的意义，所以该方案通常是跟云端转码混合使用的。 也就是先通过 setMixTranscodingConfig 将房间里的多路画面混合到一路上，再转推出去。

>?关于旁路转推的注意事项：
>- 默认只支持转推到腾讯云的 rtmp [推流地址](https://cloud.tencent.com/document/product/267/32720) 上，转推其他云的需求请通过工单联系我们。
>- 调用该函数的用户，只会转推自己这一路画面到指定的 rtmp 推流地址上，因此一般需要配合 setMixTranscodingConfig 一起使用。
>- TRTC 房间里的每一路画面都有一路默认的腾讯云 CDN 地址（需要开启），所以该功能并不常用，仅在您需要适配多家 CDN 服务商时才需要关注该功能。


### stopPublishCDNStream

停止旁路推流。
```
abstract void stopPublishCDNStream()
```



## Log 相关接口函数
### getSDKVersion

获取 SDK 版本信息。
```
String getSDKVersion()
```


### setLogLevel

设置 Log 输出级别。
```
void setLogLevel(int level)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | int | 参见 TRTC_LOG_LEVEL。 |


### setConsoleEnabled

启用或禁用控制台日志打印。
```
void setConsoleEnabled(boolean enabled)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enabled | boolean | 指定是否启用。 |


### setLogCompressEnabled

启用或禁用 Log 的本地压缩。
```
void setLogCompressEnabled(boolean enabled)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enabled | boolean | 指定是否启用。 |

__介绍__

开启压缩后，log　存储体积明显减小，但需要腾讯云提供的 Python 脚本解压后才能阅读。 禁用压缩后，log　采用明文存储，可以直接用记事本打开阅读，但占用空间较大。


### setLogDirPath

修改日志保存路径。
```
void setLogDirPath(String path)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | String | 存储日志路径。 |

>?日志文件默认保存在 /sdcard/log/tencent/liteav 下，如需修改， 必须在所有方法前调用，并且保证目录存在及应用有目录的读写权限。



### setLogListener

设置日志回调。
```
void setLogListener(final TRTCCloudListener.TRTCLogListener logListener)
```


### showDebugView

显示仪表。
```
abstract void showDebugView(int showType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| showType | int | 0：不显示；1：显示精简版；2：显示全量版。 |

__介绍__

仪表盘是状态统计和事件消息浮层　view，方便调试。


### setDebugViewMargin

设置仪表盘的边距。
```
abstract void setDebugViewMargin(String userId, TRTCViewMargin margin)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | String | 用户 ID。 |
| margin | [TRTCViewMargin](https://cloud.tencent.com/document/product/647/32264#.E6.92.AD.E6.94.BE.E8.83.8C.E6.99.AF.E9.9F.B3.E4.B9.90.E7.9A.84.E5.9B.9E.E8.B0.83.E6.8E.A5.E5.8F.A3) | 仪表盘内边距，注意这里是基于 parentView 的百分比，margin 的取值范围是0 - 1。 |

__介绍__

必须在 showDebugView 调用前设置才会生效。


### callExperimentalAPI

调用实验性 API 接口。
```
abstract void callExperimentalAPI(String jsonStr)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| jsonStr | String | 接口及参数描述的 JSON 字符串。 |

>?该接口用于调用一些实验性功能。



## 播放背景音乐的回调接口

__相关类__

`TRTCCloud.BGMNotify`



### onBGMStart

音乐播放开始的回调通知。
```
void onBGMStart(int errCode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| errCode | int | 0：播放成功；-1：播放失败。 |


### onBGMProgress

音乐播放进度的回调通知。
```
void onBGMProgress(long progress, long duration)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| progress | long | 当前 BGM 已播放时间(ms)。 |
| duration | long | 当前 BGM 总时间(ms)。 |


### onBGMComplete

音乐播放结束的回调通知。
```
void onBGMComplete(int err)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| err | int | 0：正常结束；-1：出错结束。 |



## 视图边距

__相关类__

`TRTCCloud.TRTCViewMargin`



### 属性列表

__属性列表__

| 属性 | 类型 | 字段含义 |
|-----|-----|-----|
| leftMargin | float | 距离左边的百分比，取值范围为0 - 1。 |
| topMargin | float | 距离顶部的百分比，取值范围为0 - 1。 |
| rightMargin | float | 距离右边的百分比，取值范围为0 - 1。 |
| bottomMargin | float | 距离底部的百分比，取值范围为0 - 1。 |





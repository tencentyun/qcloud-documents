
ITRTCCloud @ TXLiteAVSDK。

## 创建与销毁 ITRTCCloud 单例

### getTRTCShareInstance

用于动态加载 dll 时，获取 [ITRTCCloud](https://cloud.tencent.com/document/product/647/32269#itrtccloud) 对象指针。
```
LITEAV_API ITRTCCloud * getTRTCShareInstance()
```

__返回__

返回 [ITRTCCloud](https://cloud.tencent.com/document/product/647/32269#itrtccloud) 单例对象的指针，delete ITRTCCloud\*会编译错误，需要调用 destroyTRTCCloud 释放单例指针对象。


### destroyTRTCShareInstance

释放 [ITRTCCloud](https://cloud.tencent.com/document/product/647/32269#itrtccloud) 单例对象。
```
LITEAV_API void destroyTRTCShareInstance()
```



## 设置 TRTCCloudCallback 回调
### addCallback

设置回调接口 [ITRTCCloudCallback](https://cloud.tencent.com/document/product/647/32270#itrtccloudcallback)。
```
void addCallback(ITRTCCloudCallback * callback)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | [ITRTCCloudCallback](https://cloud.tencent.com/document/product/647/32270#itrtccloudcallback) * | 事件回调指针。 |

__介绍__

您可以通过 [ITRTCCloudCallback](https://cloud.tencent.com/document/product/647/32270#itrtccloudcallback) 获得来自 SDK 的各种状态通知，详见 ITRTCCloudCallback.h 中的定义。


### removeCallback

移除事件回调。
```
void removeCallback(ITRTCCloudCallback * callback)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | [ITRTCCloudCallback](https://cloud.tencent.com/document/product/647/32270#itrtccloudcallback) * | 事件回调指针。 |



## 房间相关接口函数
### enterRoom

进入房间。
```
void enterRoom(const TRTCParams & params, TRTCAppScene scene)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| params | const [TRTCParams](https://cloud.tencent.com/document/product/647/32271#trtcparams) & | 进房参数，请参考 [TRTCParams](https://cloud.tencent.com/document/product/647/32271#trtcparams)。 |
| scene | [TRTCAppScene](https://cloud.tencent.com/document/product/647/32271#trtcappscene) | 应用场景，目前支持视频通话（VideoCall）和在线直播（Live）两种场景。 |

__介绍__

如果加入成功，您会收到 onEnterRoom() 回调；如果失败，您会收到 onEnterRoom(result) 回调。 跟进房失败相关的错误码，请参见 [错误码](https://cloud.tencent.com/document/product/647/32257)。

>?不管进房是否成功，enterRoom 都必须与 exitRoom 配对使用，在调用 exitRoom 前再次调用 enterRoom 函数会导致不可预期的错误问题。



### exitRoom

离开房间。
```
void exitRoom()
```

__介绍__

调用 [exitRoom()](https://cloud.tencent.com/document/product/647/32269#exitroom) 接口会执行退出房间的相关逻辑，例如释放音视频设备资源和编解码器资源等。 待资源释放完毕，SDK 会通过 TRTCCloudCallback 中的 onExitRoom() 回调通知您。
如果您需要再次调用 [enterRoom()](https://cloud.tencent.com/document/product/647/32269#enterroom) 或者切换到其他的音视频 SDK，请等待 onExitRoom() 回调到来后再执行相关操作。 否则可能会遇到如摄像头、麦克风设备被强占等各种异常问题。


### switchRole

切换角色，仅适用于直播场景（TRTCAppSceneLIVE）。
```
void switchRole(TRTCRoleType role)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| role | [TRTCRoleType](https://cloud.tencent.com/document/product/647/32271#trtcroletype) | 目标角色。 |

__介绍__

在直播场景下，一个用户可能需要在“观众”和“主播”之间来回切换。 您可以在进房前通过 [TRTCParams](https://cloud.tencent.com/document/product/647/32271#trtcparams) 中的 role 字段确定角色，也可以通过 switchRole 在进房后切换角色。


### connectOtherRoom

请求跨房通话（主播 PK）。
```
void connectOtherRoom(const char * params)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| params | const char * | JSON 字符串连麦参数，roomId 代表目标房间号，userId 代表目标用户 ID。 |

__介绍__

TRTC 中两个不同音视频房间中的主播，可以通过“跨房通话”功能拉通连麦通话功能。使用此功能时，两个主播无需退出各自原来的直播间即可进行“连麦 PK”。
例如：当房间“001”中的主播 A 通过 [connectOtherRoom()](https://cloud.tencent.com/document/product/647/32269#connectotherroom) 跟房间“002”中的主播 B 拉通跨房通话后， 房间“001”中的用户都会收到主播 B 的 onUserEnter(B) 回调和 onUserVideoAvailable(B，true) 回调。 房间“002”中的用户都会收到主播 A 的 onUserEnter(A) 回调和 onUserVideoAvailable(A，true) 回调。
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
- roomId：房间“001”中的主播 A 要跟房间“002”中的主播 B 连麦，主播 A 调用 [connectOtherRoom()](https://cloud.tencent.com/document/product/647/32269#connectotherroom) 时 roomId 应指定为“002”。
- userId：房间“001”中的主播 A 要跟房间“002”中的主播 B 连麦，主播 A 调用 [connectOtherRoom()](https://cloud.tencent.com/document/product/647/32269#connectotherroom) 时 userId 应指定为 B 的 userId。


跨房通话的请求结果会通过 TRTCCloudCallback 中的 onConnectOtherRoom() 回调通知您。


<pre>
  //此处用到 jsoncpp 库来格式化 JSON 字符串
  Json::Value jsonObj;
  jsonObj["roomId"] = 002;
  jsonObj["userId"] = "userB";
  Json::FastWriter writer;
  std::string params = writer.write(jsonObj);
  trtc.ConnectOtherRoom(params.c_str());
</pre>


### disconnectOtherRoom

关闭跨房连麦。
```
void disconnectOtherRoom()
```

__介绍__

跨房通话的退出结果会通过 TRTCCloudCallback 中的 onDisconnectOtherRoom() 回调通知给您。



## 视频相关接口函数
### startLocalPreview

开启本地视频的预览画面。
```
void startLocalPreview(HWND rendHwnd)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rendHwnd | HWND | 承载预览画面的 HWND。 |

__介绍__

这个接口会启动默认的摄像头，可以通过 setCurrentCameraDevice 接口选用其他摄像头 当开始渲染首帧摄像头画面时，您会收到 TRTCCloudCallback 中的 onFirstVideoFrame(null) 回调。


### stopLocalPreview

停止本地视频采集及预览。
```
void stopLocalPreview()
```


### muteLocalVideo

是否屏蔽自己的视频画面。
```
void muteLocalVideo(bool mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | bool | true：屏蔽；false：开启。 |

__介绍__

当屏蔽本地视频后，房间里的其它成员将会收到 onUserVideoAvailable 回调通知。


### startRemoteView

开始显示远端视频画面。
```
void startRemoteView(const char * userId, HWND rendHwnd)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 对方的用户标识。 |
| rendHwnd | HWND | 承载预览画面的窗口句柄。 |

__介绍__

在收到 SDK 的 onUserVideoAvailable(userId， true) 通知时，可以获知该远程用户开启了视频，此后调用 startRemoteView(userId) 接口加载该用户的远程画面时，可以用 loading 动画优化加载过程中的等待体验。 待该用户的首帧画面开始显示时，您会收到 onFirstVideoFrame(userId) 事件回调。


### stopRemoteView

停止显示远端视频画面。
```
void stopRemoteView(const char * userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 对方的用户标识。 |

__介绍__

调用此接口后，SDK 会停止接收该用户的远程视频流，同时会清理相关的视频显示资源。


### stopAllRemoteView

停止显示所有远端视频画面。
```
void stopAllRemoteView()
```

>?如果有屏幕分享的画面在显示，则屏幕分享的画面也会一并被关闭。



### muteRemoteVideoStream

暂停接收指定的远端视频流。
```
void muteRemoteVideoStream(const char * userId, bool mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 对方的用户标识。 |
| mute | bool | 是否停止接收。 |

__介绍__

该接口仅停止接收远程用户的视频流，但并不释放显示资源，所以视频画面会冻屏在 mute 前的最后一帧。


### muteAllRemoteVideoStreams

停止接收所有远端视频流。
```
void muteAllRemoteVideoStreams(bool mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | bool | 是否停止接收。 |


### setVideoEncoderParam

设置视频编码器相关参数。
```
void setVideoEncoderParam(const TRTCVideoEncParam & params)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| params | const [TRTCVideoEncParam](https://cloud.tencent.com/document/product/647/32271#trtcvideoencparam) & | 视频编码参数，详情请参考 TRTCCloudDef.h 中的 [TRTCVideoEncParam](https://cloud.tencent.com/document/product/647/32271#trtcvideoencparam) 定义。 |

__介绍__

该设置决定了远端用户看到的画面质量（同时也是云端录制出的视频文件的画面质量）。


### setNetworkQosParam

设置网络流控相关参数。
```
void setNetworkQosParam(const TRTCNetworkQosParam & params)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| params | const [TRTCNetworkQosParam](https://cloud.tencent.com/document/product/647/32271#trtcnetworkqosparam) & | 网络流控参数，详情请参考 TRTCCloudDef.h 中的 [TRTCNetworkQosParam](https://cloud.tencent.com/document/product/647/32271#trtcnetworkqosparam) 定义。 |

__介绍__

该设置决定了 SDK 在各种网络环境下的调控策略（例如弱网下是“保清晰”还是“保流畅”）。


### setLocalViewFillMode

设置本地图像的渲染模式。
```
void setLocalViewFillMode(TRTCVideoFillMode mode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mode | [TRTCVideoFillMode](https://cloud.tencent.com/document/product/647/32271#trtcvideofillmode) | 填充（画面可能会被拉伸裁剪）或适应（画面可能会有黑边）。 |


### setRemoteViewFillMode

设置远端图像的渲染模式。
```
void setRemoteViewFillMode(const char * userId, TRTCVideoFillMode mode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 用户 ID。 |
| mode | [TRTCVideoFillMode](https://cloud.tencent.com/document/product/647/32271#trtcvideofillmode) | 填充（画面可能会被拉伸裁剪）或适应（画面可能会有黑边）。 |


### setLocalViewRotation

设置本地图像的顺时针旋转角度。
```
void setLocalViewRotation(TRTCVideoRotation rotation)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rotation | TRTCVideoRotation | 支持 TRTCVideoRotation90 、 TRTCVideoRotation180 以及 TRTCVideoRotation270 旋转角度。 |


### setRemoteViewRotation

设置远端图像的顺时针旋转角度。
```
void setRemoteViewRotation(const char * userId, TRTCVideoRotation rotation)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 用户 ID。 |
| rotation | TRTCVideoRotation | 支持 TRTCVideoRotation90 、 TRTCVideoRotation180 以及 TRTCVideoRotation270 旋转角度。 |


### setVideoEncoderRotation

设置视频编码输出的（也就是远端用户观看到的，以及服务器录制下来的）画面方向。
```
void setVideoEncoderRotation(TRTCVideoRotation rotation)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rotation | TRTCVideoRotation | 目前支持 TRTCVideoRotation0 和 TRTCVideoRotation180 旋转角度。 |


### setLocalViewMirror

设置本地摄像头预览画面的镜像模式。
```
void setLocalViewMirror(bool mirror)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mirror | bool | 镜像模式。 |


### setVideoEncoderMirror

设置编码器输出的画面镜像模式。
```
void setVideoEncoderMirror(bool mirror)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mirror | bool | 是否开启远端镜像, true：远端画面镜像；false：远端画面非镜像。默认值为 false。 |

__介绍__

该接口不改变本地摄像头的预览画面，但会改变另一端用户看到的（以及服务器录制的）画面效果。


### enableSmallVideoStream

开启大小画面双路编码模式。
```
void enableSmallVideoStream(bool enable, const TRTCVideoEncParam & smallVideoParam)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | bool | 是否开启小画面编码。 |
| smallVideoParam | const [TRTCVideoEncParam](https://cloud.tencent.com/document/product/647/32271#trtcvideoencparam) & | 小流的视频参数。 |

__介绍__

如果当前用户是房间中的主要角色（例如主播、老师、主持人等），并且使用 PC 或者 Mac 环境，可以开启该模式。 开启该模式后，当前用户会同时输出【高清】和【低清】两路视频流（但只有一路音频流）。 对于开启该模式的当前用户，会占用更多的网络带宽，并且会更加消耗 CPU 计算资源。
对于同一房间的远程观众而言：
- 如果用户的下行网络很好，可以选择观看【高清】画面
- 如果用户的下行网络不好，可以选择观看【低清】画面。


### setRemoteVideoStreamType

选定观看指定 userId 的大画面还是小画面。
```
void setRemoteVideoStreamType(const char * userId, TRTCVideoStreamType type)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 用户 ID。 |
| type | [TRTCVideoStreamType](https://cloud.tencent.com/document/product/647/32271#trtcvideostreamtype) | 视频流类型，即选择看大画面还是小画面。 |

__介绍__

此功能需要该 userId 通过 enableEncSmallVideoStream 提前开启双路编码模式。 如果该 userId 没有开启双路编码模式，则此操作无效。


### setPriorRemoteVideoStreamType

设定观看方优先选择的视频质量。
```
void setPriorRemoteVideoStreamType(TRTCVideoStreamType type)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| type | [TRTCVideoStreamType](https://cloud.tencent.com/document/product/647/32271#trtcvideostreamtype) | 默认观看大画面还是小画面。 |

__介绍__

低端设备推荐优先选择低清晰度的小画面。 如果对方没有开启双路视频模式，则此操作无效。



## 音频相关接口函数
### startLocalAudio

开启本地音频的采集和上行。
```
void startLocalAudio()
```

__介绍__

该函数会启动麦克风采集，并将音频数据传输给房间里的其他用户。 SDK 并不会默认开启本地的音频上行，也就说，如果您不调用这个函数，房间里的其他用户就听不到您的声音。

>?TRTC SDK 并不会默认打开本地的麦克风采集。



### stopLocalAudio

关闭本地音频的采集和上行。
```
void stopLocalAudio()
```

__介绍__

当关闭本地音频的采集和上行，房间里的其它成员会收到 onUserAudioAvailable(false) 回调通知。


### muteLocalAudio

静音本地的音频。
```
void muteLocalAudio(bool mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | bool | true：屏蔽；false：开启。 |

__介绍__

当静音本地音频后，房间里的其它成员会收到 onUserAudioAvailable(false) 回调通知。 与 stopLocalAudio 不同之处在于，muteLocalAudio 并不会停止发送音视频数据，而是会继续发送码率极低的静音包。 在对录制质量要求很高的场景中，选择 muteLocalAudio 是更好的选择，能录制出兼容性更好的 MP4 文件。 这是由于 MP4 等视频文件格式，对于音频的连续性是要求很高的，简单粗暴地 stopLocalAudio 会导致录制出的 MP4 不易播放。


### muteRemoteAudio

静音掉某一个用户的声音。
```
void muteRemoteAudio(const char * userId, bool mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 用户 ID。 |
| mute | bool | true：静音；false：非静音。 |


### muteAllRemoteAudio

静音掉所有用户的声音。
```
void muteAllRemoteAudio(bool mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | bool | true：静音；false：非静音。 |


### enableAudioVolumeEvaluation

启用或关闭音量大小提示。
```
void enableAudioVolumeEvaluation(uint32_t interval)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| interval | uint32_t | 设置 onUserVoiceVolume 回调的触发间隔，单位为ms，最小间隔为100ms，如果小于等于0则会关闭回调，建议设置为300ms。 |

__介绍__

开启此功能后，SDK 会在 onUserVoiceVolume() 中反馈对每一路声音音量大小值的评估。 我们在 Demo 中有一个音量大小的提示条，就是基于这个接口实现的。 如希望打开此功能，请在 [startLocalAudio()](https://cloud.tencent.com/document/product/647/32269#startlocalaudio) 之前调用。


### startAudioRecording

开始录音。
```
int startAudioRecording(const TRTCAudioRecordingParams & audioRecordingParams)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| audioRecordingParams | const [TRTCAudioRecordingParams](https://cloud.tencent.com/document/product/647/32271#trtcaudiorecordingparams) & | 录音参数，请参考TRTCAudioRecordingParams。 |

__返回__

0：成功；-1：录音已开始；-2：文件或目录创建失败；-3：后缀指定的音频格式不支持。

__介绍__

该方法调用后， SDK 会将通话过程中的所有音频(包括本地音频，远端音频，BGM等)录制到一个文件里。 无论是否进房，调用该接口都生效。 如果调用 exitRoom 时还在录音，录音会自动停止。


### stopAudioRecording

停止录音。
```
void stopAudioRecording()
```

__介绍__

如果调用 exitRoom 时还在录音，录音会自动停止。



## 摄像头相关接口函数
### getCameraDevicesList

获取摄像头设备列表。
```
ITRTCDeviceCollection * getCameraDevicesList()
```

__返回__

摄像头管理器对象指针 ITRTCDeviceCollection*。

__介绍__

示例代码： 

<pre>
 ITRTCDeviceCollection * pDevice = m_pCloud->getCameraDevicesList();
 for (int i = 0; i < pDevice->getCount(); i++)
 {
     std::wstring name = UTF82Wide(pDevice->getDeviceName(i));
 }
 pDevice->release();
 pDevice = null;
</pre>

>?如果 delete ITRTCDeviceCollection*指针会编译错误，SDK 维护 ITRTCDeviceCollection 对象的生命周期。



### setCurrentCameraDevice

设置要使用的摄像头。
```
void setCurrentCameraDevice(const char * deviceId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| deviceId | const char * | 从 getCameraDevicesList 中得到的设备 ID。 |


### getCurrentCameraDevice

获取当前使用的摄像头。
```
ITRTCDeviceInfo * getCurrentCameraDevice()
```

__返回__

ITRTCDeviceInfo 设备信息，能获取设备 ID 和设备名称。



## 音频设备相关接口函数
### getMicDevicesList

获取麦克风设备列表。
```
ITRTCDeviceCollection * getMicDevicesList()
```

__返回__

麦克风管理器对象指针 ITRTCDeviceCollection*。

__介绍__

示例代码： 

<pre>
 ITRTCDeviceCollection * pDevice = m_pCloud->getMicDevicesList();
 for (int i = 0; i < pDevice->getCount(); i++)
 {
     std::wstring name = UTF82Wide(pDevice->getDeviceName(i));
 }
 pDevice->release();
 pDevice = null;
</pre>

>?如果 delete ITRTCDeviceCollection* 指针会编译错误，SDK 维护 ITRTCDeviceCollection 对象的生命周期。



### getCurrentMicDevice

获取当前选择的麦克风。
```
ITRTCDeviceInfo * getCurrentMicDevice()
```

__返回__

ITRTCDeviceInfo 设备信息，能获取设备 ID 和设备名称。


### setCurrentMicDevice

设置要使用的麦克风。
```
void setCurrentMicDevice(const char * micId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| micId | const char * | 从 getMicDevicesList 中得到的设备 ID。 |

__介绍__

选择指定的麦克风作为录音设备，不调用该接口时，默认选择索引为0的麦克风。


### getCurrentMicDeviceVolume

获取当前麦克风设备音量。
```
uint32_t getCurrentMicDeviceVolume()
```

__返回__

音量值，范围是0 - 100。


### setCurrentMicDeviceVolume

设置麦克风设备的音量。
```
void setCurrentMicDeviceVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | uint32_t | 麦克风音量值，范围0 - 100。 |


### getSpeakerDevicesList

获取扬声器设备列表。
```
ITRTCDeviceCollection * getSpeakerDevicesList()
```

__返回__

扬声器管理器对象指针 ITRTCDeviceCollection*。

__介绍__

示例代码： 

<pre>
 ITRTCDeviceCollection * pDevice = m_pCloud->getSpeakerDevicesList();
 for (int i = 0; i < pDevice->getCount(); i++)
 {
     std::wstring name = UTF82Wide(pDevice->getDeviceName(i));
 }
 pDevice->release();
 pDevice = null;
</pre>

>?如果 delete ITRTCDeviceCollection* 指针会编译错误，SDK 维护 ITRTCDeviceCollection 对象的生命周期。



### getCurrentSpeakerDevice

获取当前的扬声器设备。
```
ITRTCDeviceInfo * getCurrentSpeakerDevice()
```

__返回__

ITRTCDeviceInfo 设备信息，能获取设备 ID 和设备名称。


### setCurrentSpeakerDevice

设置要使用的扬声器。
```
void setCurrentSpeakerDevice(const char * speakerId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| speakerId | const char * | 从 getSpeakerDevicesList 中得到的设备 ID。 |


### getCurrentSpeakerVolume

当前扬声器设备音量。
```
uint32_t getCurrentSpeakerVolume()
```

__返回__

扬声器音量，范围0 - 100。

>?查询的不是系统扬声器的音量大小。



### setCurrentSpeakerVolume

设置当前扬声器音量。
```
void setCurrentSpeakerVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | uint32_t | 设置的扬声器音量，范围0 - 100。 |

>?设置的不是系统扬声器的音量大小。



## 美颜相关接口函数
### setBeautyStyle

设置美颜、美白、红润效果级别。
```
void setBeautyStyle(TRTCBeautyStyle style, uint32_t beauty, uint32_t white, uint32_t ruddiness)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| style | [TRTCBeautyStyle](https://cloud.tencent.com/document/product/647/32271#trtcbeautystyle) | 美颜风格，光滑或者自然，光滑风格磨皮更加明显，适合娱乐场景。 |
| beauty | uint32_t | 美颜级别，取值范围0 - 9，0表示关闭，1 - 9值越大，效果越明显。 |
| white | uint32_t | 美白级别，取值范围0 - 9，0表示关闭，1 - 9值越大，效果越明显。 |
| ruddiness | uint32_t | 红润级别，取值范围0 - 9，0表示关闭，1 - 9值越大，效果越明显，该参数暂未生效。 |

__介绍__

SDK 内部集成了两套风格不同的磨皮算法，一套我们取名叫“光滑”，适用于美女秀场，效果比较明显。 另一套我们取名“自然”，磨皮算法更多地保留了面部细节，主观感受上会更加自然。


### setWaterMark

设置水印。
```
void setWaterMark(TRTCVideoStreamType streamType, const char * srcData, TRTCWaterMarkSrcType srcType, uint32_t nWidth, uint32_t nHeight, float xOffset, float yOffset, float fWidthRatio)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| streamType | [TRTCVideoStreamType](https://cloud.tencent.com/document/product/647/32271#trtcvideostreamtype) | 要设置水印的流类型(TRTCVideoStreamTypeBig、TRTCVideoStreamTypeSub)。 |
| srcData | const char * | 水印图片源数据（传 NULL 表示去掉水印）。 |
| srcType | [TRTCWaterMarkSrcType](https://cloud.tencent.com/document/product/647/32271#trtcwatermarksrctype) | 水印图片源数据类型（传 NULL 时忽略该参数）。 |
| nWidth | uint32_t | 水印图片像素宽度（源数据为文件路径时忽略该参数）。 |
| nHeight | uint32_t | 水印图片像素高度（源数据为文件路径时忽略该参数）。 |
| xOffset | float | 水印显示的左上角 x 轴偏移。 |
| yOffset | float | 水印显示的左上角 y 轴偏移。 |
| fWidthRatio | float | 水印显示的宽度占画面宽度比例（水印按该参数等比例缩放显示）。 |

__介绍__

水印的位置是通过 xOffset， yOffset， fWidthRatio 来指定的。
- xOffset：水印的坐标，取值范围为0 - 1的浮点数。
- yOffset：水印的坐标，取值范围为0 - 1的浮点数。
- fWidthRatio：水印的大小比例，取值范围为0 - 1的浮点数。

>?大小流暂未支持。



## 辅流相关接口函数
### startRemoteSubStreamView

开始渲染远端用户辅流画面。
```
void startRemoteSubStreamView(const char * userId, HWND rendHwnd)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 对方的用户标识。 |
| rendHwnd | HWND | 渲染画面的 HWND。 |

__介绍__

对应于 [startRemoteView()](https://cloud.tencent.com/document/product/647/32269#startremoteview) 用于显示主画面，该接口只能用于显示辅路（屏幕分享、远程播片）画面。

>?请在 onUserSubStreamAvailable 回调后再调用这个接口。



### stopRemoteSubStreamView

停止显示远端用户的屏幕分享画面。
```
void stopRemoteSubStreamView(const char * userId)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 对方的用户标识。 |


### setRemoteSubStreamViewFillMode

设置辅流画面的渲染模式。
```
void setRemoteSubStreamViewFillMode(const char * userId, TRTCVideoFillMode mode)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 用户的 ID。 |
| mode | [TRTCVideoFillMode](https://cloud.tencent.com/document/product/647/32271#trtcvideofillmode) | 填充（画面可能会被拉伸裁剪）或适应（画面可能会有黑边）。 |

__介绍__

对应于 [setRemoteViewFillMode()](https://cloud.tencent.com/document/product/647/32269#setremoteviewfillmode) 于设置远端的主路画面，该接口用于设置远端的辅路（屏幕分享、远程播片）画面。


### getScreenCaptureSources

枚举可共享的窗口列表，。
```
ITRTCScreenCaptureSourceList * getScreenCaptureSources(const SIZE & thumbSize, const SIZE & iconSize)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| thumbSize | const SIZE & | 指定要获取的窗口缩略图大小，缩略图可用于绘制在窗口选择界面上。 |
| iconSize | const SIZE & | 指定要获取的窗口图标大小。 |

__返回__

窗口列表包括屏幕。

__介绍__

如果您要给您的 App 增加屏幕分享功能，一般需要先显示一个窗口选择界面，这样用户可以选择希望分享的窗口。 通过如下函数，您可以获得可分享窗口的 ID、类型、窗口名称以及缩略图。 拿到这些信息后，您就可以实现一个窗口选择界面，当然，您也可以使用我们在 Demo 源码中已经实现好的一个界面。

>?返回的列表中包括屏幕和应用窗口，屏幕会在列表的前面几个元素中。
>如果 delete ITRTCScreenCaptureSourceList*指针会编译错误，SDK 维护 ITRTCScreenCaptureSourceList 对象的生命周期。


### selectScreenCaptureTarget

设置屏幕共享参数，该方法在屏幕共享过程中也可以调用。
```
void selectScreenCaptureTarget(const TRTCScreenCaptureSourceInfo & source, const RECT & captureRect, bool captureMouse, bool highlightWindow)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| source | const TRTCScreenCaptureSourceInfo & | 指定分享源。 |
| captureRect | const RECT & | 指定捕获的区域。 |
| captureMouse | bool | 指定是否捕获鼠标指针。 |
| highlightWindow | bool | 指定是否高亮正在共享的窗口，以及当捕获图像被遮挡时高亮遮挡窗口提示用户移走遮挡。 |

__介绍__

如果您期望在屏幕分享的过程中，切换想要分享的窗口，可以再次调用这个函数而不需要重新开启屏幕分享。
支持如下四种情况：
- 共享整个屏幕：sourceInfoList 中 type 为 Screen 的 source，captureRect 设为 { 0， 0， 0， 0 }
- 共享指定区域：sourceInfoList 中 type 为 Screen 的 source，captureRect 设为非 NULL，例如 { 100， 100， 300， 300 }
- 共享整个窗口：sourceInfoList 中 type 为 Window 的 source，captureRect 设为 { 0， 0， 0， 0 }
- 共享窗口区域：sourceInfoList 中 type 为 Window 的 source，captureRect 设为非 NULL，例如 { 100， 100， 300， 300 }。


### startScreenCapture

启动屏幕分享。
```
void startScreenCapture(HWND rendHwnd)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rendHwnd | HWND | 承载预览画面的 HWND。 |


### pauseScreenCapture

暂停屏幕分享。
```
void pauseScreenCapture()
```


### resumeScreenCapture

恢复屏幕分享。
```
void resumeScreenCapture()
```


### stopScreenCapture

停止屏幕采集。
```
void stopScreenCapture()
```


### setSubStreamEncoderParam

设置屏幕分享的编码器参数。
```
void setSubStreamEncoderParam(const TRTCVideoEncParam & params)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| params | const [TRTCVideoEncParam](https://cloud.tencent.com/document/product/647/32271#trtcvideoencparam) & | 辅流编码参数，详情请参考 TRTCCloudDef.h 中的 [TRTCVideoEncParam](https://cloud.tencent.com/document/product/647/32271#trtcvideoencparam) 定义。 |

__介绍__

对应于 [setVideoEncoderParam()](https://cloud.tencent.com/document/product/647/32269#setvideoencoderparam) 设置主路画面的编码质量，该函数仅用于设置辅路（屏幕分享、远程播片）的编码参数。 该设置决定了远端用户看到的画面质量，同时也是云端录制出的视频文件的画面质量。


### setSubStreamMixVolume

设置辅流的混音音量大小。
```
void setSubStreamMixVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | uint32_t | 设置的混音音量大小，范围0 - 100。 |

__介绍__

这个数值越高，辅路音量的占比就约高，麦克风音量占比就越小，所以不推荐设置得太大，否则麦克风的声音就被压制了。



## 自定义采集和渲染
### enableCustomVideoCapture

启用视频自定义采集模式。
```
void enableCustomVideoCapture(bool enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | bool | 是否启用。 |

__介绍__

开启该模式后，SDK 不在运行原有的视频采集流程，只保留编码和发送能力。 您需要用 [sendCustomVideoData()](https://cloud.tencent.com/document/product/647/32269#sendcustomvideodata) 不断地向 SDK 塞入自己采集的视频画面。


### sendCustomVideoData

向 SDK 投送自己采集的视频数据。
```
void sendCustomVideoData(TRTCVideoFrame * frame)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| frame | TRTCVideoFrame * | 视频数据，支持 I420 格式数据。 |

__介绍__

TRTCVideoFrame 推荐如下填写方式（其他字段不需要填写）：
- pixelFormat：仅支持 LiteAVVideoPixelFormat_I420。
- bufferType：仅支持 LiteAVVideoBufferType_Buffer。
- data：视频帧 buffer。
- length：视频帧数据长度，I420 格式下，其值等于：width × height × 3 / 2。
- width：视频图像长度。
- height：视频图像宽度。
- timestamp：如果 timestamp 间隔不均匀，会严重影响音画同步和录制出的 MP4 质量。


参考文档：[自定义采集和渲染](https://cloud.tencent.com/document/product/647/34066)。

>?
>- SDK 内部有帧率控制逻辑，目标帧率以您在 setVideoEncoderParam 中设置的为准，太快会自动丢帧，太慢则会自动补帧。
>- 可以设置 frame 中的 timestamp 为 0，相当于让 SDK 自己设置时间戳，但请“均匀”地控制 sendCustomVideoData 的调用间隔，否则会导致视频帧率不稳定。


### enableCustomAudioCapture

启用音频自定义采集模式 开启该模式后， SDK 停止运行原有的音频采集流程，只保留编码和发送能力。 您需要用 [sendCustomAudioData()](https://cloud.tencent.com/document/product/647/32269#sendcustomaudiodata) 不断地向 SDK 塞入自己采集的视频画面。
```
void enableCustomAudioCapture(bool enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | bool | 是否启用。 |


### sendCustomAudioData

向 SDK 投送自己采集的音频数据。
```
void sendCustomAudioData(TRTCAudioFrame * frame)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| frame | TRTCAudioFrame * | 音频帧，仅支持 LiteAVAudioFrameFormatPCM 格式。目前只支持单声道，仅支持48K采样率，LiteAVAudioFrameFormatPCM 格式。 |

__介绍__

TRTCAudioFrame 推荐如下填写方式（其他字段不需要填写）：
- audioFormat：仅支持 LiteAVAudioFrameFormatPCM。
- data：音频帧 buffer。
- length：音频帧数据长度，推荐每帧20ms采样数。【PCM格式、48000采样率、单声道的帧长度：48000 × 0.02s × 1 × 16bit = 15360bit = 1920字节】。
- sampleRate：采样率，仅支持48000。
- channel：频道数量（如果是立体声，数据是交叉的），单声道：1； 双声道：2。
- timestamp：如果 timestamp 间隔不均匀，会严重影响音画同步和录制出的 MP4 质量。


参考文档：[自定义采集和渲染](https://cloud.tencent.com/document/product/647/34066)。

>?可以设置 frame 中的 timestamp 为 0，相当于让 SDK 自己设置时间戳，但请“均匀”地控制 sendCustomAudioData 的调用间隔，否则会导致声音断断续续。



### setLocalVideoRenderCallback

设置本地视频自定义渲染。
```
int setLocalVideoRenderCallback(TRTCVideoPixelFormat pixelFormat, TRTCVideoBufferType bufferType, ITRTCVideoRenderCallback * callback)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| pixelFormat | TRTCVideoPixelFormat | 指定回调的像素格式。 |
| bufferType | TRTCVideoBufferType | 指定视频数据结构类型。 |
| callback | [ITRTCVideoRenderCallback](https://cloud.tencent.com/document/product/647/32270#itrtcvideorendercallback) * | 自定义渲染回调。 |

__返回__

0：成功；<0：错误。

>?设置此方法，SDK 内部会把采集到的数据回调出来，SDK 跳过 HWND 渲染逻辑 调用 setLocalVideoRenderCallback(TRTCVideoPixelFormat_Unknown， TRTCVideoBufferType_Unknown， nullptr) 停止回调。


### setRemoteVideoRenderCallback

设置远端视频自定义渲染。
```
int setRemoteVideoRenderCallback(const char * userId, TRTCVideoPixelFormat pixelFormat, TRTCVideoBufferType bufferType, ITRTCVideoRenderCallback * callback)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userId | const char * | 用户标识。 |
| pixelFormat | TRTCVideoPixelFormat | 指定回调的像素格式。 |
| bufferType | TRTCVideoBufferType | 指定视频数据结构类型。 |
| callback | [ITRTCVideoRenderCallback](https://cloud.tencent.com/document/product/647/32270#itrtcvideorendercallback) * | 自定义渲染回调。 |

__返回__

0：成功；<0：错误。

__介绍__

此方法同 setLocalVideoRenderDelegate，区别在于一个是本地画面的渲染回调， 一个是远程画面的渲染回调。

>?设置此方法，SDK 内部会把远端的数据解码后回调出来，SDK 跳过 HWND 渲染逻辑 调用 setRemoteVideoRenderCallback(userId， TRTCVideoPixelFormat_Unknown，  TRTCVideoBufferType_Unknown， nullptr) 停止回调。



### setAudioFrameCallback

设置音频数据回调。
```
int setAudioFrameCallback(ITRTCAudioFrameCallback * callback)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | [ITRTCAudioFrameCallback](https://cloud.tencent.com/document/product/647/32270#itrtcaudioframecallback) * | 声音帧数据（PCM 格式）的回调，callback = nullptr 则停止回调数据。 |

__返回__

0：成功；<0：错误。

__介绍__

设置此方法，SDK 内部会把声音模块的数据（PCM 格式）回调出来，包括：
- onCapturedAudioFrame：本机麦克风采集到的音频数据
- onPlayAudioFrame：混音前的每一路远程用户的音频数据
- onMixedPlayAudioFrame：各路音频数据混合后送入扬声器播放的音频数据。



## 自定义消息发送
### sendCustomCmdMsg

发送自定义消息给房间内所有用户。
```
bool sendCustomCmdMsg(uint32_t cmdId, const uint8_t * data, uint32_t dataSize, bool reliable, bool ordered)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| cmdId | uint32_t | 消息 ID，取值范围为1 - 10。 |
| data | const uint8_t * | 待发送的消息，最大支持1KB（1000字节）的数据大小。 |
| dataSize | uint32_t | 待发送的数据大小。 |
| reliable | bool | 是否可靠发送，可靠发送的代价是会引入一定的延时，因为接收端要暂存一段时间的数据来等待重传。 |
| ordered | bool | 是否要求有序，即是否要求接收端接收的数据顺序和发送端发送的顺序一致，这会带来一定的接收延时，因为在接收端需要暂存并排序这些消息。 |

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
bool sendSEIMsg(const uint8_t * data, uint32_t dataSize, int32_t repeatCount)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| data | const uint8_t * | 待发送的数据，最大支持1kb（1000字节）的数据大小。 |
| dataSize | uint32_t | 待发送的数据大小。 |
| repeatCount | int32_t | 发送数据次数。 |

__返回__

true：消息已通过限制，等待后续视频帧发送；false:消息被限制发送。

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
void playBGM(const char * path)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | const char * | 音乐文件路径。 |


### stopBGM

停止播放背景音乐。
```
void stopBGM()
```


### pauseBGM

暂停播放背景音乐。
```
void pauseBGM()
```


### resumeBGM

继续播放背景音乐。
```
void resumeBGM()
```


### getBGMDuration

获取音乐文件总时长，单位毫秒。
```
uint32_t getBGMDuration(const char * path)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | const char * | 音乐文件路径，如果 path 为空，那么返回当前正在播放的 music 时长。 |

__返回__

成功返回时长，失败返回-1。


### setBGMPosition

设置 BGM 播放进度。
```
void setBGMPosition(uint32_t pos)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| pos | uint32_t | 单位毫秒。 |


### setMicVolumeOnMixing

设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小。
```
void setMicVolumeOnMixing(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | uint32_t | 音量大小，100为正常音量，取值范围为0 - 200。 |


### setBGMVolume

设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小。
```
void setBGMVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | uint32_t | 音量大小，100为正常音量，取值范围为0 - 200。 |


### startSystemAudioLoopback

打开系统声音采集。
```
void startSystemAudioLoopback(const char * path)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | const char * | - path 为空，代表采集整个操作系统的声音。<br>- path 填写 exe 程序（如 QQ音乐）所在的路径，将会启动此程序并只采集此程序的声音。 |

__介绍__

开启后可以采集整个操作系统的播放声音（path 为空）或某一个播放器（path 不为空）的声音， 并将其混入到当前麦克风采集的声音中一起发送到云端。


### stopSystemAudioLoopback

关闭系统声音采集。
```
void stopSystemAudioLoopback()
```


### setSystemAudioLoopbackVolume

设置系统声音采集的音量。
```
void setSystemAudioLoopbackVolume(uint32_t volume)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | uint32_t | 音量大小，取值范围为0 - 100。 |



## 设备和网络测试
### startSpeedTest

开始进行网络测速（视频通话期间请勿测试，以免影响通话质量）。
```
void startSpeedTest(uint32_t sdkAppId, const char * userId, const char * userSig)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sdkAppId | uint32_t | 应用标识。 |
| userId | const char * | 用户标识。 |
| userSig | const char * | 用户签名。 |

__介绍__

测速结果将会用于优化 SDK 接下来的服务器选择策略，因此推荐您在用户首次通话前先进行一次测速，这将有助于我们选择最佳的服务器。 同时，如果测试结果非常不理想，您可以通过醒目的 UI 提示用户选择更好的网络。

>?测速本身会消耗一定的流量，所以也会产生少量额外的流量费用。



### stopSpeedTest

停止服务器测速。
```
void stopSpeedTest()
```


### startCameraDeviceTest

开始进行摄像头测试。
```
void startCameraDeviceTest(HWND rendHwnd)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rendHwnd | HWND | 承载预览画面的 HWND。 |

__介绍__

会触发 onLocalVideoFrameAfterProcess 回调接口。

>?在测试过程中可以使用 setCurrentCameraDevice 接口切换摄像头。



### stopCameraDeviceTest

停止摄像头测试。
```
void stopCameraDeviceTest()
```


### startMicDeviceTest

开启麦克风测试。
```
void startMicDeviceTest(uint32_t interval)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| interval | uint32_t | 反馈音量提示的时间间隔（ms），建议设置到大于 200 毫秒。 |

__介绍__

回调接口 onTestMicVolume 获取测试数据
该方法测试麦克风是否能正常工作，volume 的取值范围为0 - 100。


### stopMicDeviceTest

停止麦克风测试。
```
void stopMicDeviceTest()
```


### startSpeakerDeviceTest

开启扬声器测试。
```
void startSpeakerDeviceTest(const char * testAudioFilePath)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| testAudioFilePath | const char * | 音频文件的绝对路径，路径字符串使用 UTF-8 编码格式，支持文件格式：WAV、MP3。 |

__介绍__

回调接口 onTestSpeakerVolume 获取测试数据
该方法播放指定的音频文件测试播放设备是否能正常工作。如果能听到声音，说明播放设备能正常工作。


### stopSpeakerDeviceTest

停止扬声器测试。
```
void stopSpeakerDeviceTest()
```



## 混流转码以及 CDN 旁路推流
### setMixTranscodingConfig

启动(更新)云端的混流转码：通过腾讯云的转码服务，将房间里的多路画面叠加到一路画面上。
```
void setMixTranscodingConfig(TRTCTranscodingConfig * config)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| config | [TRTCTranscodingConfig](https://cloud.tencent.com/document/product/647/32271#trtctranscodingconfig) * | 请参考 TRTCCloudDef.h 中关于 [TRTCTranscodingConfig](https://cloud.tencent.com/document/product/647/32271#trtctranscodingconfig) 的介绍。如果传入 NULL 取消云端混流转码。 |

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
void startPublishCDNStream(const TRTCPublishCDNParam & param)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| param | const [TRTCPublishCDNParam](https://cloud.tencent.com/document/product/647/32271#trtcpublishcdnparam) & | 请参考 TRTCCloudDef.h 中关于 [TRTCPublishCDNParam](https://cloud.tencent.com/document/product/647/32271#trtcpublishcdnparam) 的介绍。 |

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
void stopPublishCDNStream()
```



## LOG 相关接口函数
### getSDKVersion

获取 SDK 版本信息。
```
const char * getSDKVersion()
```

__返回__

UTF-8 编码的版本号。


### setLogLevel

设置 Log 输出级别。
```
void setLogLevel(TRTCLogLevel level)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| level | [TRTCLogLevel](https://cloud.tencent.com/document/product/647/32271#trtcloglevel) | 参见 TRTCLogLevel。 |


### setConsoleEnabled

启用或禁用控制台日志打印。
```
void setConsoleEnabled(bool enabled)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enabled | bool | 指定是否启用。 |


### setLogCompressEnabled

启用或禁用 Log 的本地压缩。
```
void setLogCompressEnabled(bool enabled)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enabled | bool | 指定是否启用。 |

__介绍__

开启压缩后，Log 存储体积明显减小，但需要腾讯云提供的 Python 脚本解压后才能阅读。 禁用压缩后，Log 采用明文存储，可以直接用记事本打开阅读，但占用空间较大。


### setLogDirPath

设置日志保存路径。
```
void setLogDirPath(const char * path)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | const char * | 存储日志的文件夹，例如 "D:\\Log"，UTF-8 编码。 |

>?日志文件默认保存在 C:/Users/[系统用户名]/AppData/Roaming/Tencent/liteav/log，即 appdata%/Tencent/liteav/log 下，如需修改，必须在所有方法前调用。



### setLogCallback

设置日志回调。
```
void setLogCallback(ITRTCLogCallback * callback)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| callback | [ITRTCLogCallback](https://cloud.tencent.com/document/product/647/32270#itrtclogcallback) * | 日志回调。 |


### showDebugView

显示仪表盘。
```
void showDebugView(int showType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| showType | int | 0：不显示；1：显示精简版；2：显示全量版。 |

__介绍__

仪表盘是状态统计和事件消息浮层 view，方便调试。


### callExperimentalAPI

调用实验性 API 接口。
```
void callExperimentalAPI(const char * jsonStr)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| jsonStr | const char * | 接口及参数描述的 JSON 字符串。 |

>?该接口用于调用一些实验性功能。




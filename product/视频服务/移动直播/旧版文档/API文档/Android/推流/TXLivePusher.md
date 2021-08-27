

__功能__  

直播推流类。

__介绍__

主要负责将本地的音视频画面进行编码和 RTMP 推送，包含如下技术特点：

- 针对腾讯云的推流地址，会采用 QUIC 协议进行加速，配合改进后的 BBR2 带宽测算方案，可以最大限度的利用主播的上行带宽，降低直播卡顿率。
- 内嵌套的 Qos 流量控制技术具备上行网络自适应能力，可以根据主播端网络的具体情况实时调节音视频数据量。
- 内嵌多套美颜磨皮算法（自然&光滑）和多款色彩空间滤镜（支持自定义滤镜），可以根据需要自行选择。
- 企业版 SDK 包含了大眼、瘦脸以及隆鼻等功能，配合高级美颜动效素材，可快速地完成功能集成。
- 支持自定义的音视频采集和渲染，让您可以根据项目需要选择自己的音视频数据源。


 
## SDK 基础函数
### TXLivePusher

创建 [TXLivePusher](https://cloud.tencent.com/document/product/454/34772#txlivepusher) 实例。
```
 TXLivePusher(Context context)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| context | Context | 上下文。 |



### setConfig

设置 [TXLivePusher](https://cloud.tencent.com/document/product/454/34772#txlivepusher) 推流配置项。
```
void setConfig(TXLivePushConfig config)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| config | [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) | 推流配置项，请参见 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771)。 |



### getConfig

获取推流器配置信息。
```
TXLivePushConfig getConfig()
```

__返回__

推流器配置信息。



### setPushListener

设置推流回调接口。
```
void setPushListener(ITXLivePushListener listener)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| listener | [ITXLivePushListener](https://cloud.tencent.com/document/product/454/34770) | 播放器回调，请参考 [ITXLivePushListener](https://cloud.tencent.com/document/product/454/34770)。 |




## 推流基础接口
### startCameraPreview

启动摄像头预览。
```
void startCameraPreview(TXCloudVideoView view)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| view | TXCloudVideoView | 承载视频画面的控件。 |

__介绍__

启动预览后并不会立即开始 RTMP 推流，需要调用 [TXLivePusher#startPusher(String)](https://cloud.tencent.com/document/product/454/34772#startpusher) 才能真正开始推流。



### stopCameraPreview

停止摄像头预览。
```
void stopCameraPreview(boolean isNeedClearLastImg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isNeedClearLastImg | boolean | 是否需要清除最后一帧画面；true：清除最后一帧画面，false：保留最后一帧画面。 |

__返回__

是否成功停止播放，0：成功；非0：失败。



### startPusher

启动 RTMP 推流。
```
int startPusher(String rtmpURL)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rtmpURL | String | 推流地址，请参见 [获取推流地址](https://cloud.tencent.com/document/product/267/32720)。 |

__返回__

0：成功； -1：启动失败。

__介绍__

针对腾讯云的推流地址，会采用 QUIC 协议进行加速，配合改进后的 BBR2 带宽测算方案，可以最大限度的利用主播的上行带宽，降低直播卡顿率。



### stopPusher

停止 RTMP 推流。
```
void stopPusher()
```



### startScreenCapture

启动录屏推流（基于 MediaProjection 技术实现）。
```
void startScreenCapture()
```

__介绍__

如果要开启“隐私模式”，请调用 [pausePusher](https://cloud.tencent.com/document/product/454/34772#pausepusher) 接口推默认图及静音数据，取消隐私模式调用 [resumePusher](https://cloud.tencent.com/document/product/454/34772#resumepusher)。



### stopScreenCapture

结束录屏推流。
```
void stopScreenCapture()
```



### pausePusher

暂停摄像头或屏幕采集并进入垫片推流状态。
```
void pausePusher()
```

__介绍__

SDK 会暂时停止摄像头或屏幕采集，并使用 TXLivePushConfig.pauseImg 中指定的图片作为替代图像进行推流，也就是所谓的“垫片”。 这项功能常用于 App 被切到后台运行的场景，尤其是在 iOS 系统中，当 App 切到后台以后，操作系统不会再允许该 App 继续使用摄像头。 此时就可以通过调用 pausePush() 进入垫片状态。
对于绝大多数推流服务器而言，如果超过一定时间不推视频数据，服务器会断开当前的推流链接。
在 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 您可以指定：
- pauseImg 设置后台推流的默认图片，不设置该参数，则默认为黑色背景。
- pauseFps 设置后台推流帧率，最小值为5，最大值为20，默认10。
- pauseTime 设置后台推流持续时长，单位秒，默认300秒。

>?请注意调用顺序：startPush => ( pausePush => resumePush ) => stopPush()，错误的调用顺序会导致 SDK 表现异常。




### resumePusher

恢复摄像头采集并结束垫片推流状态。
```
void resumePusher()
```



### isPushing

查询是否正在推流。
```
boolean isPushing()
```

__返回__

true：正在推流，false：未推流。




## 视频相关接口
### setVideoQuality

设置视频编码质量。
```
void setVideoQuality(int quality, boolean adjustBitrate, boolean adjustResolution)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| quality | int | 画质类型（标清、高清、超高清）。 |
| adjustBitrate | boolean | 动态码率开关。 |
| adjustResolution | boolean | 动态切分辨率开关。 |

__介绍__

推荐设置：秀场直播 quality：HIGH_DEFINITION；adjustBitrate：false；adjustResolution：false。 请参见 [设定清晰度](https://cloud.tencent.com/document/product/454/7879#7.-.E8.AE.BE.E5.AE.9A.E7.94.BB.E9.9D.A2.E6.B8.85.E6.99.B0.E5.BA.A6)。

>?adjustResolution 早期被引入是为了让 [TXLivePusher](https://cloud.tencent.com/document/product/454/34772#txlivepusher) 能够满足视频通话这一封闭场景下的一些需求，现已不推荐使用。 如果您有视频通话的需求，可以使用我们专门为视频通话打造的 [TRTC](https://cloud.tencent.com/product/trtc) 服务。 由于目前很多 H5 播放器不支持分辨率动态变化，所以开启分辨率自适应以后，会导致 H5 播放端和录制文件的很多兼容问题。




### switchCamera

切换前后摄像头。
```
void switchCamera()
```

>?默认使用前置摄像头，该接口在启动预览 [startCameraPreview(TXCloudVideoView)](https://cloud.tencent.com/document/product/454/34772#startcamerapreview) 后调用才能生效，预览前调用无效。




### setMirror

设置视频镜像效果。
```
boolean setMirror(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：播放端看到的是镜像画面；false：播放端看到的是非镜像画面。 |

__介绍__

由于前置摄像头采集的画面是取自手机的观察视角，如果将采集到的画面直接展示给观众，是完全没有问题的。 但如果将采集到的画面也直接显示给主播，则会跟主播照镜子时的体验完全相反，会让主播感觉到很奇怪。 因此，SDK 会默认开启本地摄像头预览画面的镜像效果，让主播直播时跟照镜子时保持一个体验效果。
setMirror 所影响的则是观众端看到的视频效果，如果想要保持观众端看到的效果跟主播端保持一致，需要开启镜像； 如果想要让观众端看到正常的未经处理过的画面（例如主播弹吉他的时候有类似需求），则可以关闭镜像。





### setRenderRotation

设置本地摄像头预览画面的旋转方向。
```
void setRenderRotation(int rotation)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rotation | int | 取值为0 ，90，180，270（其他值无效），表示主播端摄像头预览视频的顺时针旋转角度。 |

__介绍__

该接口仅能够改变主播本地预览画面的方向，而不会改变观众端的画面效果。 如果希望改变观众端看到的视频画面的方向，例如原来是540x960，希望变成960x540，则可以通过设置 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中的 homeOrientation 来实现。


<pre>
// 竖屏推流（HOME 键在下）
_config.homeOrientation = TXLiveConstants.VIDEO_ANGLE_HOME_DOWN;
[_txLivePublisher setConfig:_config];
[_txLivePublisher setRenderRotation:0];</pre>

<pre>// 横屏推流（HOME 键在右）
_config.homeOrientation = TXLiveConstants.VIDEO_ANGLE_HOME_RIGHT;
[_txLivePublisher setConfig:_config];
[_txLivePublisher setRenderRotation:90];
</pre>



### turnOnFlashLight

打开后置摄像头旁边的闪光灯。
```
boolean turnOnFlashLight(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：打开闪光灯； false：关闭闪光灯。 |

__返回__

true：打开成功；false：打开失败。

__介绍__

此操作对于前置摄像头是无效的，因为绝大多数手机都没有给前置摄像头配置闪光灯。



### getMaxZoom

获取摄像头支持的焦距。
```
int getMaxZoom()
```

__返回__

0：不支持变焦；大于0：最大焦距。



### setZoom

调整摄像头的焦距。
```
boolean setZoom(int value)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| value | int | 焦距大小，取值范围：1 - [getMaxZoom()](https://cloud.tencent.com/document/product/454/34772#getmaxzoom)，默认值建议设置为1即可。 |

__返回__

true：成功； false：失败。

>?当 distance 为1的时候为最远视角（正常镜头），当为 [getMaxZoom()](https://cloud.tencent.com/document/product/454/34772#getmaxzoom) 的时候为最近视角（放大镜头），最大值不要超过，超过后画面会模糊不清。




### setExposureCompensation

调整曝光比例。
```
void setExposureCompensation(float value)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| value | float | 曝光比例，表示该手机支持最大曝光调整值的比例，取值范围从-1到1。 负数表示调低曝光，-1是最小值，对应 getMinExposureCompensation。 正数表示调高曝光，1是最大值，对应 getMaxExposureCompensation。 0表示不调整曝光，默认值为0。 |




## 美颜相关接口
### getBeautyManager
获取美颜管理对象 [TXBeautyManager](https://cloud.tencent.com/document/product/454/39379)。
通过美颜管理，您可以使用以下功能：
- 设置”美颜风格”、”美白”、“红润”、“大眼”、“瘦脸”、“V脸”、“下巴”、“短脸”、“小鼻”、“亮眼”、“白牙”、“祛眼袋”、“祛皱纹”、“祛法令纹”等美容效果。
- 调整“发际线”、“眼间距”、“眼角”、“嘴形”、“鼻翼”、“鼻子位置”、“嘴唇厚度”、“脸型”。
- 设置人脸挂件（素材）等动态效果。
- 添加美妆。
- 进行手势识别。

```
public TXBeautyManager getBeautyManager()
```



## 音频相关接口
### setMute

开启静音。
```
void setMute(boolean mute)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mute | boolean | true：静音；false：不静音。 |

__介绍__

开启静音后，SDK 并不会继续采集麦克风的声音，但是会用非常低（5kbps左右）的码率推送伪静音数据， 这样做的目的是为了兼容 H5 上的 video 标签，并让录制出来的 MP4 文件有更好的兼容性。



### setBGMNofify

设置背景音乐的回调接口。
```
void setBGMNofify(OnBGMNotify notify)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| notify | [OnBGMNotify](https://cloud.tencent.com/document/product/454/34772#onbgmnotify) | 回调接口。 |



### playBGM

播放背景音乐。
```
boolean playBGM(String path)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | String | 背景音乐文件路径。 |

__返回__

true：播放成功；false：播放失败。

__介绍__

SDK 会将背景音乐和麦克风采集的声音进行混合并一起推送到云端。



### stopBGM

停止播放背景音乐。
```
boolean stopBGM()
```

__返回__

true：停止播放成功； false：停止播放失败。



### pauseBGM

暂停播放背景音乐。
```
boolean pauseBGM()
```

__返回__

true：暂停播放成功； false：暂停播放失败。



### resumeBGM

继续播放背音乐。
```
boolean resumeBGM()
```

__返回__

true：恢复播放成功； false：恢复播放失败。



### getMusicDuration

获取背景音乐文件的总时长，单位是毫秒。
```
int getMusicDuration(String path)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | String | 音乐文件路径，如果 path 为空，那么返回当前正在播放的背景音乐的时长。 |



### setBGMVolume

设置混音时背景音乐的音量大小，仅在播放背景音乐混音时使用。
```
boolean setBGMVolume(float x)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| x | float | 音量大小，1为正常音量，范围是：[0 ~ 1] 之间的浮点数。 |

__返回__

true：成功；false：失败。



### setMicVolume

设置混音时麦克风音量大小，仅在播放背景音乐混音时使用。
```
boolean setMicVolume(float x)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| x | float | 音量大小，1为正常音量，范围是：[0 ~ 1] 之间的浮点数。 |

__返回__

true：成功；false：失败。



### setBgmPitch

调整背景音乐的音调高低。
```
void setBgmPitch(float pitch)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| pitch | float | 音调，默认值是0.0f，范围是：-1 - 1之间的浮点数。 |



### setReverb

设置混响效果。
```
void setReverb(int reverbType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reverbType | int | 混响类型，具体值请参见 TXLiveConstants 中的 REVERB_TYPE_X 定义。 |



### setVoiceChangerType

设置变声类型。
```
void setVoiceChangerType(int voiceChangerType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| voiceChangerType | int | 具体值请参见 TXLiveConstants 中的 VOICECHANGER_TYPE_X 定义。 |




## 本地录制接口
### setVideoRecordListener

设置录制回调接口。
```
void setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| listener | TXRecordCommon.ITXVideoRecordListener | 录制回调接口。 |



### startRecord

开始录制短视频。
```
int startRecord(final String videoFilePath)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| videoFilePath | final String | 视频录制后存储路径。 |

__返回__

0：成功；-1：videoPath 为空；-2：上次录制尚未结束，请先调用 stopRecord；-3：推流尚未开始。

>?
>- 只有启动推流后才能开始录制，非推流状态下启动录制无效。
>- 出于安装包体积的考虑，仅专业版和商业版两个版本的 LiteAVSDK 支持该功能，直播精简版仅定义了接口但并未实现。
>- 录制过程中请勿动态切换分辨率和软硬编，会有很大概率导致生成的视频异常。



### stopRecord

结束录制短视频，当停止推流后，如果视频还在录制中，SDK 内部会自动结束录制。
```
void stopRecord()
```

__返回__

0：成功； -1：不存在录制任务。



### snapshot

推流过程中本地截图。
```
void snapshot(final ITXSnapshotListener listener)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| listener | final [ITXSnapshotListener](https://cloud.tencent.com/document/product/454/34772#itxsnapshotlistener) | 截图完成回调。 |




## 自定义采集和处理
### sendCustomVideoTexture

自定义视频采集，向 SDK 发送自己采集的 texture 视频数据。
```
int sendCustomVideoTexture(int textureID, int w, int h)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| textureID | int | 视频纹理 ID。 |
| w | int | 视频图像的宽度，不能大于 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中的 videoResolution 属性设定的宽度，否则会失败，小于时 SDK 会自动裁剪。 |
| h | int | 视频图像的高度，不能大于 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中的 videoResolution 属性设定的宽度，否则会失败，小于时 SDK 会自动裁剪。 |

__返回__

返回视频数据的发送结果：
 - 0：发送成功；
 - 1：视频分辨率非法；
 - 3：视频格式非法；
 - 4：视频图像长宽不符合要求，画面比要求的小了；
 - 1000：SDK 内部错误。

__介绍__

在自定义视频采集模式下，SDK 不再继续从摄像头采集图像，只保留编码和发送能力，您需要定时地发送自己采集的视频数据。 要开启自定义视频采集，需要完成如下两个步骤：
- 开启自定义采集：给 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中的 customModeType 属性增加 CUSTOM_MODE_VIDEO_CAPTURE 选项，代表开启自定义视频采集。
- 设定视频分辨率：将 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中的 videoResolution 属性设置为您发送 YUV 数据的 width、height。

>?
>- 该接口目前仅支持在 OpenGL（EGL10）环境线程调用，SDK 内部会自动获取 EGL10 的上下文，然后维护一个 sharecontext。
>- 目前仅支持普通纹理，暂不支持外部纹理。
>- 开启自定义视频采集后，即无需再调用 startPreview 来开启摄像头采集。
>- SDK 内部不再做帧率控制，请务必保证调用该函数的频率和 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中设置的帧率一致，否则编码器输出的码率会不受控制。



### sendCustomVideoData

自定义视频采集，向 SDK 发送自己采集的 YUV 视频数据。
```
int sendCustomVideoData(byte [] buffer, int bufferType, int w, int h)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| buffer | byte [] | 视频数据。 |
| bufferType | int | 视频格式 目前仅支持 YUV_420P 、RGB_RGBA 两种数据格式。 |
| w | int | 视频图像的宽度；不能大于 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中的 videoResolution 属性设定的宽度，否则会失败，小于时 SDK 会自动裁剪。 |
| h | int | 视频图像的高度；不能大于 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中的 videoResolution 属性设定的宽度，否则会失败，小于时 SDK 会自动裁剪。 |

__返回__

如果返回值大于0，代表发送成功，但发送的帧率过高，超过了 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中设置的帧率， 帧率过高会导致最终编出的码率超过 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中设置的码率，返回值表示当前视频帧比预期提前的毫秒数。
 -  0：发送成功；
 - 1：视频分辨率非法；
 - 2：YUV 数据长度与设置的视频分辨率所要求的长度不一致；
 - 3：视频格式非法；
 - 4：视频图像长宽不符合要求，画面比要求的小了；
 - 1000：SDK 内部错误。

__介绍__

在自定义视频采集模式下，SDK 不再继续从摄像头采集图像，只保留编码和发送能力，您需要定时地发送自己采集的视频数据。 要开启自定义视频采集，需要完成如下两个步骤：
- 开启自定义采集：给 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中的 customModeType 属性增加 CUSTOM_MODE_VIDEO_CAPTURE 选项，代表开启自定义视频采集。
- 设定视频分辨率：将 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中的 videoResolution 属性设置为您发送 YUV 数据的 width、height。

>?
>- 开启自定义视频采集后，即无需再调用 startPreview 来开启摄像头采集。
>- buffer 方式的处理性能要比 texture 方式的处理性能差很多。
>- SDK 内部不再做帧率控制，请务必保证调用该函数的频率和 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中设置的帧率一致，否则编码器输出的码率会不受控制。



### sendCustomPCMData

自定义音频采集，向 SDK 发送自己采集的音频 PCM 数据。
```
void sendCustomPCMData(byte [] pcmBuffer)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| pcmBuffer | byte [] | pcm 音频数据。 |

__介绍__

在自定义音频采集模式下，SDK 不再继续从麦克风采集声音，只保留编码和发送能力，您需要定时地发送自己采集的声音数据（PCM 格式）
要开启自定义音频采集，需要完成如下两个步骤：
- 开启自定义采集：给 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中的 customModeType 属性增加 CUSTOM_MODE_AUDIO_CAPTURE 选项，代表开启自定义音频采集。
- 设定音频采样率：将 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中的 audioSampleRate 属性设置为您期望的音频采样率，audioChannels 设置为期望的声道数，默认值：1（单声道）。

>?SDK 对每次传入的 PCM buffer 大小有严格要求，每一个采样点要求是16位宽。 如果是单声道，请保证传入的 PCM 长度为2048；如果是双声道，请保证传入的 PCM 长度为4096。




### setVideoProcessListener

自定义视频处理回调。
```
void setVideoProcessListener(VideoCustomProcessListener listener)
```

__介绍__

自定义视频采集和自定义视频处理不能同时开启，与自定义视频采集不同，自定义视频处理依然是由 SDK 采集摄像头的画面， 但 SDK 会通过 [VideoCustomProcessListener](https://cloud.tencent.com/document/product/454/34772#videocustomprocesslistener) 回调将数据回调给您的 App 进行二次加工。
如果要开启自定义视频处理，需要给 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中的 customModeType 属性增加 CUSTOM_MODE_VIDEO_PREPROCESS 选项。

>?出于性能和稳定性考虑，一般不建议开启此特性。




### setAudioProcessListener

自定义音频处理回调。
```
void setAudioProcessListener(AudioCustomProcessListener listener)
```

__介绍__

自定义音频采集和自定义音频处理不能同时开启，与自定义音频采集不同，自定义音频处理依然是由 SDK 采集麦克风的声音， 但 SDK 会通过 [AudioCustomProcessListener](https://cloud.tencent.com/document/product/454/34772#audiocustomprocesslistener) 回调将数据回调给您的 App 进行二次加工。
如果要开启自定义音频处理，需要给 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 中的 customModeType 属性增加 CUSTOM_MODE_AUDIO_PREPROCESS 选项。

>?出于性能和稳定性考虑，一般不建议开启此特性。




### setSurface

指定 SDK 渲染所使用的 Surface（仅供微信 App 使用）。
```
void setSurface(Surface surface)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| surface | Surface | 渲染 surface，Nonnull：开始渲染；null：停止渲染。 |

__介绍__

该接口是为了支持微信小程序最新版本中的同层渲染能力而增加的，目的是让微信小程序通知设置渲染用的 Surface， 我们推荐您不要使用此接口，建议直接使用 TXCloudVideoView。

>?
>- 使用该接口需要 [startCameraPreview(TXCloudVideoView)](https://cloud.tencent.com/document/product/454/34772#startcamerapreview) 传入 null。
>- 此功能为高级特性，除非您非常明确需要使用该特性，否则建议您使用 [startCameraPreview(TXCloudVideoView)](https://cloud.tencent.com/document/product/454/34772#startcamerapreview)。



### setSurfaceSize

设置渲染 Surface 的大小（仅供微信 App 使用）。
```
void setSurfaceSize(int width, int height)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| width | int | surface 宽度。 |
| height | int | surface 高度。 |

__介绍__

该接口是为了支持微信小程序最新版本中的同层渲染能力而增加的，目的是让微信小程序通知设置渲染用的 Surface， 我们推荐您不要使用此接口，建议直接使用 TXCloudVideoView。

>?
>- Surface 大小变化后，需要重新设定。
>- 此功能为高级特性，除非您非常明确需要使用该特性，否则建议您使用 [startCameraPreview(TXCloudVideoView)](https://cloud.tencent.com/document/product/454/34772#startcamerapreview)。



### setFocusPosition

在 Surface 模式下，设置摄像机的对焦位置。
```
void setFocusPosition(float x, float y)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| x | float | 聚焦点位置 x 值。 |
| y | float | 聚焦点位置 y 值。 |

>?
>- Surface 模式下，需要您自行监听点击事件，通知 SDK 进行对焦；详细实现方式，可参考 Demo 实现。
>- 此功能为高级特性，除非您非常明确需要使用该特性，否则建议您使用 [startCameraPreview(TXCloudVideoView)](https://cloud.tencent.com/document/product/454/34772#startcamerapreview)。




## 更多实用接口
### sendMessageEx

发送 SEI 消息，播放端 [TXLivePlayer](https://cloud.tencent.com/document/product/454/34775#txliveplayer) 通过 onPlayEvent(PLAY_EVT_GET_MESSAGE) 来接收该消息。
```
boolean sendMessageEx(byte [] msg)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| msg | byte [] | - |

__返回__

true：消息发送成功；false：消息发送失败。

>?
>- sendMessage 已经不推荐使用，会导致 H5 播放器产生兼容性问题，请使用 sendMessageEx。
>- 若您使用过 sendMessage，不推荐立刻升级到 sendMessageEx。
>- sendMessageEx 发送消息给旧版本5.0及以前的 SDK 版本时，消息会无法正确解析，但播放不受影响。



### sendMessage
```
void sendMessage(byte [] msg)
```



### onLogRecord

输出自己的 log，保存到 SDK 内部的 xlog 文件中。
```
void onLogRecord(String str)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| str | String | 存入本地文件的 log。 |

>?此功能一般仅用在协助调试的情况下。






## VideoCustomProcessListener

__功能__

自定义视频处理回调类。



### onTextureCustomProcess

在 OpenGL 线程中回调，在这里可以进行采集图像的二次处理。
```
int onTextureCustomProcess(int textureId, int width, int height)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| textureId | int | 纹理 ID。 |
| width | int | 纹理的宽度。 |
| height | int | 纹理的高度。 |

__返回__

返回给 SDK 的纹理 ID，如果不做任何处理，返回传入的纹理 ID 即可。



### onDetectFacePoints

企业版回调人脸坐标。
```
void onDetectFacePoints(float [] points)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| points | float [] | 归一化人脸坐标，每两个值表示某点 P 的 X，Y 值。值域[0.f，1.f]。 |



### onTextureDestoryed

在 OpenGL 线程中回调，可以在这里释放创建的 OpenGL 资源。
```
void onTextureDestoryed()
```




## AudioCustomProcessListener

__功能__

自定义音频处理回调类。



### onRecordRawPcmData

回调未经过任何处理的 SDK 录制音频 PCM 数据。
```
void onRecordRawPcmData(byte [] data, long ts, int sampleRate, int channels, int bits, boolean withBgm)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| data | byte [] | pcm 数据。 |
| ts | long | pcm 对应时间戳。 |
| sampleRate | int | 音频采样率。 |
| channels | int | 音频通道。 |
| bits | int | 音频 bits。 |
| withBgm | boolean | 回调的数据是否包含 BGM，当不开启回声消除时，回调的 raw pcm 会包含 bgm。 |



### onRecordPcmData

回调 SDK 录制音频 PCM 数据。
```
void onRecordPcmData(byte [] data, long ts, int sampleRate, int channels, int bits)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| data | byte [] | pcm 数据。 |
| ts | long | pcm 对应时间戳。 |
| sampleRate | int | 音频采样率。 |
| channels | int | 音频通道。 |
| bits | int | 音频 bits。 |




## OnBGMNotify

__功能__

背景音乐回调类。



### onBGMStart

音乐播放开始的回调通知。
```
void onBGMStart()
```



### onBGMProgress

音乐播放进度的回调通知。
```
void onBGMProgress(long progress, long duration)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| progress | long | 当前 BGM 已播放时间（ms）。 |
| duration | long | 当前 BGM 总时间（ms）。 |



### onBGMComplete

音乐播放结束的回调通知。
```
void onBGMComplete(int err)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| err | int | 0：正常结束；-1：出错结束。 |




## ITXSnapshotListener

__功能__

截图回调类。



### onSnapshot
```
void onSnapshot(Bitmap bmp)
```




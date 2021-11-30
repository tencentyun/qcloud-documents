
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
### config

设置 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) 推流配置项，见`TXLivePushConfig.h`文件中的详细定义。
```
@property (nonatomic, copy) TXLivePushConfig * config
```

### delegate

设置推流回调接口，见`TXLivePushListener.h`文件中的详细定义。
```
@property (nonatomic, weak) id< TXLivePushListener > delegate
```

### initWithConfig

创建 TXLivePusher 示例。
```
- (id)initWithConfig:(TXLivePushConfig *)config 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| config | [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) * | [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) 推流配置项，见`TXLivePushConfig.h`文件中的详细定义。 |




## 推流基础接口
### rtmpURL

获取当前推流的 RTMP 地址。
```
@property (nonatomic, readonly, assign) NSString * rtmpURL
```

### startPreview

启动摄像头预览。
```
- (int)startPreview:(TXView *)view 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| view | TXView * | 承载视频画面的控件。 |

__介绍__

启动预览后并不会立刻开始 RTMP 推流，需要调用 startPush 才能真正开始推流。



### stopPreview

停止摄像头预览。
```
- (void)stopPreview
```



### startPush

启动 RTMP 推流。
```
- (int)startPush:(NSString *)rtmpURL 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rtmpURL | NSString * | 推流地址，请参见 [获取推流地址](https://cloud.tencent.com/document/product/267/32720)。 |

__返回__

0：启动成功；-1：启动失败；-5：license 校验失败。

__介绍__

针对腾讯云的推流地址，会采用 QUIC 协议进行加速，配合改进后的 BBR2 带宽测算方案，可以最大限度的利用主播的上行带宽，降低直播卡顿率。

>?-5返回码代表 license 校验失败，TXLivePusher 需要 [License](https://cloud.tencent.com/document/product/454/34750) 校验通过才能工作。




### stopPush

停止 RTMP 推流。
```
- (void)stopPush
```



### pausePush

暂停摄像头采集并进入垫片推流状态。
```
- (void)pausePush
```

__介绍__

SDK 会暂时停止摄像头采集，并使用 [TXLivePushConfig.pauseImg](https://cloud.tencent.com/document/product/454/34756) 中指定的图片作为替代图像进行推流，也就是所谓的“垫片”。 这项功能常用于 App 被切到后台运行的场景，尤其是在 iOS 系统中，当 App 切到后台以后，操作系统不会再允许该 App 继续使用摄像头。 此时就可以通过调用 [pausePush](https://cloud.tencent.com/document/product/454/34755#pausepush) 进入垫片状态。
对于绝大多数推流服务器而言，如果超过一定时间不推视频数据，服务器会断开当前的推流链接。
在 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) 您可以指定：
- pauseImg 设置后台推流的默认图片，默认为黑色背景。
- pauseFps 设置后台推流帧率，最小值为5，最大值为20，默认为10。
- pauseTime 设置后台推流持续时长，单位秒，默认300秒。

>?请注意调用顺序：startPush => ( pausePush => resumePush ) => [stopPush](https://cloud.tencent.com/document/product/454/34755#stoppush)，错误的调用顺序会导致 SDK 表现异常。




### resumePush

恢复摄像头采集并结束垫片推流状态。
```
- (void)resumePush
```



### isPublishing

查询是否正在推流。
```
- (bool)isPublishing
```

__返回__

YES：推流中；NO：没有在推流。




## 视频相关接口
### frontCamera

查询当前是否为前置摄像头。
```
@property (nonatomic, readonly, assign) BOOL frontCamera
```

### setVideoQuality

设置视频编码质量。
```
- (void)setVideoQuality:(TX_Enum_Type_VideoQuality)quality adjustBitrate:(BOOL)adjustBitrate adjustResolution:(BOOL)adjustResolution 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| quality | TX_Enum_Type_VideoQuality | 画质类型（标清，高清，超高清）。 |
| adjustBitrate | BOOL | 动态码率开关。 |
| adjustResolution | BOOL | 动态切分辨率开关。 |

__介绍__

推荐设置：秀场直播 quality：HIGH_DEFINITION；adjustBitrate：NO；adjustResolution：NO。请参见 [设定清晰度](https://cloud.tencent.com/document/product/454/7879#7.-.E8.AE.BE.E5.AE.9A.E7.94.BB.E9.9D.A2.E6.B8.85.E6.99.B0.E5.BA.A6)。

>?adjustResolution 早期被引入是为了让 TXLivePusher 能够满足视频通话这一封闭场景下的一些需求，现已不推荐使用。 如果您有视频通话的需求，可以使用我们专门为视频通话打造的 [TRTC](https://cloud.tencent.com/product/trtc) 服务。 由于目前很多 H5 播放器不支持分辨率动态变化，所以开启分辨率自适应以后，会导致 H5 播放端和录制文件的很多兼容问题。




### switchCamera

切换前后摄像头（iOS）。
```
- (int)switchCamera
```



### selectCamera

选择摄像头（macOS）。
```
- (void)selectCamera:(AVCaptureDevice *)camera 
```



### setMirror

设置视频镜像效果。
```
- (void)setMirror:(BOOL)isMirror 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isMirror | BOOL | YES：播放端看到的是镜像画面；NO：播放端看到的是非镜像画面。 |

__介绍__

由于前置摄像头采集的画面是取自手机的观察视角，如果将采集到的画面直接展示给观众，是完全没有问题的。 但如果将采集到的画面也直接显示给主播，则会跟主播照镜子时的体验完全相反，会让主播感觉到很奇怪。 因此，SDK 会默认开启本地摄像头预览画面的镜像效果，让主播直播时跟照镜子时保持一个体验效果。
setMirror 所影响的则是观众端看到的视频效果，如果想要保持观众端看到的效果跟主播端保持一致，需要开启镜像； 如果想要让观众端看到正常的未经处理过的画面（如主播弹吉他的时候有类似需求），则可以关闭镜像。





### setRenderRotation

设置本地摄像头预览画面的旋转方向。
```
- (void)setRenderRotation:(int)rotation 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rotation | int | 取值为0、90、180和270（其他值无效），表示主播端摄像头预览视频的顺时针旋转角度。 |

__介绍__

该接口仅能够改变主播本地预览画面的方向，而不会改变观众端的画面效果。 如果希望改变观众端看到的视频画面的方向，例如原来是540 × 960，希望变成960 × 540，则可以通过设置 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) 中的 homeOrientation 来实现。


```
// 竖屏推流（HOME 键在下）
_config.homeOrientation = HOME_ORIENTATION_DOWN;
[_txLivePublisher setConfig:_config];
[_txLivePublisher setRenderRotation:0];
// 横屏推流（HOME 键在右）
_config.homeOrientation = HOME_ORIENTATION_RIGHT;
[_txLivePublisher setConfig:_config];
[_txLivePublisher setRenderRotation:90];
```



### toggleTorch

打开后置摄像头旁边的闪光灯。
```
- (BOOL)toggleTorch:(BOOL)bEnable 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| bEnable | BOOL | YES：打开；NO：关闭。 |

__返回__

YES：打开成功；NO：打开失败。

__介绍__

此操作对于前置摄像头是无效的，因为绝大多数手机都没有给前置摄像头配置闪光灯。



### setZoom

调整摄像头的焦距。
```
- (void)setZoom:(CGFloat)distance 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| distance | CGFloat | 焦距大小，取值范围：1 - 5，默认值建议设置为1即可。 |

>?当 distance 为1的时候为最远视角（正常镜头），当为5的时候为最近视角（放大镜头），最大值不要超过5，超过5后画面会模糊不清。




### setFocusPosition

设置手动对焦区域。
```
- (void)setFocusPosition:(CGPoint)touchPoint 
```

__介绍__

SDK 默认使用摄像头自动对焦功能，您也可以通过 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) 中的 touchFocus 选项关闭自动对焦，改用手动对焦。 改用手动对焦之后，需要由主播自己单击摄像头预览画面上的某个区域，来手动指导摄像头对焦。

>?早期 SDK 版本仅仅提供了手动和自动对焦的选择开关，并不支持设置对焦位置，3.0版本以后，手动对焦的接口才开放出来。





## 美颜相关接口
### getBeautyManager

获取美颜管理对象 [TXBeautyManager](https://cloud.tencent.com/document/product/454/39382)。
```
- (TXBeautyManager *)getBeautyManager 
```

通过美颜管理，您可以使用以下功能：
- 设置”美颜风格”、”美白”、“红润”、“大眼”、“瘦脸”、“V脸”、“下巴”、“短脸”、“小鼻”、“亮眼”、“白牙”、“祛眼袋”、“祛皱纹”、“祛法令纹”等美容效果。
- 调整“发际线”、“眼间距”、“眼角”、“嘴形”、“鼻翼”、“鼻子位置”、“嘴唇厚度”、“脸型”。
- 设置人脸挂件（素材）等动态效果。
- 添加美妆。
- 进行手势识别。



## 音频相关接口
### setMute

开启静音。
```
- (void)setMute:(BOOL)bEnable 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| bEnable | BOOL | 是否开启静音。 |

__介绍__

开启静音后，SDK 并不会继续采集麦克风的声音，但是会用非常低（5kbps左右）的码率推送伪静音数据， 这样做的目的是为了兼容 H5 上的 video 标签，并让录制出来的 MP4 文件有更好的兼容性。



### playBGM

播放背景音乐。
```
- (BOOL)playBGM:(NSString *)path 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | NSString * | 本地音乐文件路径。 |

__返回__

YES：成功；NO：失败。

__介绍__

SDK 会将背景音乐和麦克风采集的声音进行混合并一起推送到云端。



### playBGM

播放背景音乐（高级版本）。
```
- (BOOL)playBGM:(NSString *)path withBeginNotify:(void(^)(NSInteger errCode))beginNotify withProgressNotify:(void(^)(NSInteger progressMS, NSInteger durationMS))progressNotify andCompleteNotify:(void(^)(NSInteger errCode))completeNotify 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | NSString * | 本地音乐文件路径。 |
| beginNotify | void(^)(NSInteger errCode) | 播放开始的回调。 |
| progressNotify | void(^)(NSInteger progressMS, NSInteger durationMS) | 播放进度回调。 |
| completeNotify | void(^)(NSInteger errCode) | 播放完毕回调。 |

__返回__

YES：成功；NO：失败。



### stopBGM

停止播放背景音乐。
```
- (BOOL)stopBGM
```



### pauseBGM

暂停播放背景音乐。
```
- (BOOL)pauseBGM
```



### resumeBGM

继续播放背景音乐。
```
- (BOOL)resumeBGM
```



### getMusicDuration

获取背景音乐文件的总时长，单位是毫秒。
```
- (int)getMusicDuration:(NSString *)path 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| path | NSString * | 音乐文件路径，如果 path 为空，那么返回当前正在播放的背景音乐的时长。 |



### setBGMVolume

设置混音时背景音乐的音量大小，仅在播放背景音乐混音时使用。
```
- (BOOL)setBGMVolume:(float)volume 
```


__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | float | 音量大小，1为正常音量，范围是0 - 1之间的浮点数。 |

__返回__

YES：成功；NO：失败。



### setMicVolume

设置混音时麦克风音量大小，仅在播放背景音乐混音时使用。
```
- (BOOL)setMicVolume:(float)volume 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | float | 音量大小，1为正常音量，范围是0 - 1之间的浮点数。 |

__返回__

YES：成功；NO：失败。



### setBgmPitch

调整背景音乐的音调高低。
```
- (BOOL)setBgmPitch:(float)pitch 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| pitch | float | 音调，默认值是0.0f，范围是-1 - 1之间的浮点数。 |

__返回__

YES：成功；NO：失败。



### setReverbType

设置混响效果。
```
- (BOOL)setReverbType:(TXReverbType)reverbType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| reverbType | TXReverbType | 混响类型，详见`TXLiveSDKTypeDef.h`中的 TXReverbType 定义。 |

__返回__

YES：成功；NO：失败。



### setVoiceChangerType

设置变声类型。
```
- (BOOL)setVoiceChangerType:(TXVoiceChangerType)voiceChangerType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| voiceChangerType | TXVoiceChangerType | 混响类型，详见`TXLiveSDKTypeDef.h`中的 voiceChangerType 定义。 |

__返回__

YES：成功；NO：失败。




## 本地录制接口
### recordDelegate

录制回调接口，详见`TXLiveRecordTypeDef.h`中的 TXLiveRecordListener 定义。
```
@property (nonatomic, weak) id< TXLiveRecordListener > recordDelegate
```

### startRecord

开始录制短视频。
```
- (int)startRecord:(NSString *)videoPath 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| videoPath | NSString * | 视频录制后存储路径。 |

__返回__

0：成功；-1：videoPath 为空；-2：上次录制尚未结束，请先调用 stopRecord；-3：推流尚未开始。

>?
>1. &nbsp;只有启动推流后才能开始录制，非推流状态下启动录制无效。
>2. &nbsp;出于安装包体积的考虑，仅专业版和商业版两个版本的 LiteAVSDK 支持该功能，直播精简版仅定义了接口但并未实现。
>3. &nbsp;录制过程中请勿动态切换分辨率和软硬编，会有很大概率导致生成的视频异常。



### stopRecord
```
- (int)stopRecord
```

__返回__

0：成功；-1：不存在录制任务。



### snapshot

推流过程中本地截图。
```
- (void)snapshot:(void(^)(TXImage *))snapshotCompletionBlock 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| snapshotCompletionBlock | void(^)(TXImage *) | 截图完成的回调函数。 |




## 自定义采集和处理
### videoProcessDelegate

自定义视频处理回调。
```
@property (nonatomic, weak) id< TXVideoCustomProcessDelegate > videoProcessDelegate
```

__介绍__

自定义视频采集和自定义视频处理不能同时开启，与自定义视频采集不同，自定义视频处理依然是由 SDK 采集摄像头的画面， 但 SDK 会通过 TXVideoCustomProcessDelegate（见`TXVideoCustomProcessDelegate.h`）回调将数据回调给您的 App 进行二次加工。
如果要开启自定义视频处理，需要给 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) 中的 customModeType 属性增加 CUSTOM_MODE_VIDEO_PREPROCESS 选项。

>?出于性能和稳定性考虑，一般不建议开启此特性。


### audioProcessDelegate

自定义音频处理回调。
```
@property (nonatomic, weak) id< TXAudioCustomProcessDelegate > audioProcessDelegate
```

__介绍__

自定义音频采集和自定义音频处理不能同时开启，与自定义音频采集不同，自定义音频处理依然是由 SDK 采集麦克风的声音， 但 SDK 会通过 TXAudioCustomProcessDelegate（见`TXAudioCustomProcessDelegate.h`）回调将数据回调给您的 App 进行二次加工。
如果要开启自定义音频处理，需要给 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) 中的 customModeType 属性增加 CUSTOM_MODE_AUDIO_PREPROCESS 选项。

>?出于性能和稳定性考虑，一般不建议开启此特性。


### sendVideoSampleBuffer

自定义视频采集，向 SDK 发送自己采集的视频数据。
```
- (void)sendVideoSampleBuffer:(CMSampleBufferRef)sampleBuffer 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sampleBuffer | CMSampleBufferRef | 向 SDK 发送的 SampleBuffer。 |

__介绍__

在自定义视频采集模式下，SDK 不再继续从摄像头采集图像，只保留编码和发送能力，您需要定时地发送自己采集的 SampleBuffer。 要开启自定义视频采集，需要完成如下两个步骤：

1. 开启自定义采集：给 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) 中的 customModeType 属性增加 CUSTOM_MODE_VIDEO_CAPTURE 选项，代表开启自定义视频采集。
2. 设定视频分辨率：将 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) 中的 sampleBufferSize 属性设置为您期望的分辨率。 如果期望编码分辨率跟采集分辨率一致，可以不设置 sampleBufferSize 属性，而是将 autoSampleBufferSize 设置为 YES。

>?
>1. 开启自定义视频采集后，即无需再调用 startPreview 来开启摄像头采集。
>2. SDK 内部有简单的帧率控制，如果发送太快时 SDK 会自动丢弃多余的帧率；如果超时不发送，SDK 会不断地重复发送最后一帧。



### sendCustomPCMData

自定义音频采集，向 SDK 发送自己采集的音频 PCM 数据。
```
- (void)sendCustomPCMData:(unsigned char *)data len:(unsigned int)len 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| data | unsigned char * | 要发送的 PCM buffer。 |
| len | unsigned int | 数据长度。 |

__介绍__

在自定义音频采集模式下，SDK 不再继续从麦克风采集声音，只保留编码和发送能力，您需要定时地发送自己采集的声音数据（PCM 格式） 要开启自定义音频采集，需要完成如下两个步骤：

1. 开启自定义采集：给 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) 中的 customModeType 属性增加 CUSTOM_MODE_AUDIO_CAPTURE 选项，代表开启自定义音频采集。
2. 设定音频采样率：将 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) 中的 audioSampleRate 属性设置为您期望的音频采样率，audioChannels 设置为期望的声道数，默认值：1（单声道）。

>?SDK 对每次传入的 PCM buffer 大小有严格要求，每一个采样点要求是16位宽。 如果是单声道，请保证传入的 PCM 长度为2048；如果是双声道，请保证传入的 PCM 长度为4096。




### sendAudioSampleBuffer

自定义音频采集，向 SDK 发送自己采集的音频数据。
```
- (void)sendAudioSampleBuffer:(CMSampleBufferRef)sampleBuffer withType:(RPSampleBufferType)sampleBufferType 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sampleBuffer | CMSampleBufferRef | 采集到的声音 sampleBuffer。 |
| sampleBufferType | RPSampleBufferType | RPSampleBufferTypeAudioApp：ReplayKit 采集到的 App 声音。RPSampleBufferTypeAudioMic：ReplayKit 采集到的麦克风声音。 |

__介绍__

相比于 sendCustomPCMData，sendAudioSampleBuffer 主要用于 ReplayKit 录屏推流的场景。 要开启自定义音频采集，需要完成如下两个步骤：

1. 开启自定义采集：给 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) 中的 customModeType 属性增加 CUSTOM_MODE_AUDIO_CAPTURE 选项，代表开启自定义音频采集。
2. 设定音频采样率：将 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34756) 中的 audioSampleRate 属性设置为您期望的音频采样率，audioChannels 设置为期望的声道数，默认值：1（单声道）。


当使用 ReplayKit 做录屏推流时，iOS 的 ReplayKit 接口会回调两种类型的声音数据：
- RPSampleBufferTypeAudioApp，也就是要录制的 App 的声音数据。
- RPSampleBufferTypeAudioMic，也就是要录制的麦克风的声音数据。


当您通过 sendAudioSampleBuffer 向 SDK 调用各种类型的声音数据时，SDK 内部会进行混流，否则只会发送一路的声音数据。



### setSendAudioSampleBufferMuted

要求 SDK 发送静音数据。
```
- (void)setSendAudioSampleBufferMuted:(BOOL)muted 
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| muted | BOOL | YES；静音；NO；关闭静音。 |

__介绍__

该函数配合 sendAudioSampleBuffer 使用，在 InApp 类型录制切后台场合时需要调用，系统屏幕录制不需要。




## 更多实用接口
### sendMessageEx

发送 SEI 消息，播放端（TXLivePlayer）通过 onPlayEvent（EVT_PLAY_GET_MESSAGE）来接收该消息。
```
- (BOOL)sendMessageEx:(NSData *)data 
```

__介绍__

本接口是将数据直接塞入视频数据头中，因此不能太大（几个字节比较合适），一般常用于塞入自定义时间戳等信息。

>?
>- sendMessage 已经不推荐使用，会导致 H5 播放器产生兼容性问题，请使用 sendMessageEx。
>- 若您使用过 sendMessage，不推荐立刻升级到 sendMessageEx。
>- sendMessageEx 发送消息给旧版本5.0及以前的 SDK 版本时，消息会无法正确解析，但播放不受影响。



### sendMessage
```
- (void)sendMessage:(NSData *)data 
```



### showVideoDebugLog

打开包含视频状态信息的调试浮层，该浮层一般用于 SDK 调试期间，外发版本请不要打开。
```
- (void)showVideoDebugLog:(BOOL)isShow 
```



### setLogViewMargin

设置调试浮层在视频 view 上的位置。
```
- (void)setLogViewMargin:(TXEdgeInsets)margin 
```



### setEnableClockOverlay

设置推流是否覆盖时钟。
```
- (void)setEnableClockOverlay:(BOOL)enabled 
```

>?需要双方的时间相同才能获取准确的延迟时间。



### enableClockOverlay

获取当前推流画面是否有覆盖时钟。
```
- (BOOL)enableClockOverlay
```





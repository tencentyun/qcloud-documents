

__功能__

腾讯云直播推流用 RTMP SDK 的参数配置模块。

__介绍__ 

主要负责 [TXLivePusher](https://cloud.tencent.com/document/product/454/34772#txlivepusher) 对应的参数设置，**其中绝大多数设置项在推流开始之后再设置是无效的**。



## 常用设置项
### setHomeOrientation

设置采集的视频的旋转角度。
```
void setHomeOrientation(int homeOrientation)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| homeOrientation | int | 采集的视频的旋转角度。 |

__介绍__

接口说明：
- 默认值：TXLiveConstants.VIDEO_ANGLE_HOME_DOWN（竖屏推流）。
- 其他取值：TXLiveConstants.VIDEO_ANGLE_HOME_RIGHT 和 TXLiveConstants.VIDEO_ANGLE_HOME_LEFT (横屏推流)。
- 改变该字段的设置以后，本地摄像头的预览画面方向也会发生改变，请调用 TXLivePusher 的 [setRenderRotation](https://cloud.tencent.com/document/product/454/34772#setrenderrotation) 进行矫正。



### setTouchFocus

设置是否开启手动对焦。
```
void setTouchFocus(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：开启手动对焦；false：不开启手动对焦。 |

__介绍__

接口说明：
- 默认值：true。
- 因为硬件的限制，API 14以上的版本以及后置摄像头才会支持。



### setEnableZoom

设置是否允许双指手势放大预览画面。
```
void setEnableZoom(boolean enableZoom)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enableZoom | boolean | - |

__介绍__

接口说明：
- 默认值：false。



### setWatermark

设置水印图片及水印图片位置。
```
void setWatermark(Bitmap watermark, int x, int y)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| watermark | Bitmap | 水印图片。 |
| x | int | 水印位置的 X 轴坐标。 |
| y | int | 水印位置的 Y 轴坐标。 |

__介绍__

接口说明：
- 水印位置坐标系与系统保持一致。
- 设置为 null 关闭水印。



### setWatermark

设置水印图片及水印图片位置。
```
void setWatermark(Bitmap watermark, float x, float y, float width)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| watermark | Bitmap | 水印图片。 |
| x | float | 归一化水印位置的 X 轴坐标，取值[0，1]。 |
| y | float | 归一化水印位置的 Y 轴坐标，取值[0，1]。 |
| width | float | 归一化水印宽度，取值[0，1]。 |

__介绍__

接口说明：
- 使用归一化坐标。
- 假设推流分辨率为：540 × 960，x，y，width 分别设置为：（0.1， 0.1， 0.1），那么水印的实际像素坐标为：（540 * 0.1， 960 * 0.1， 水印宽度 * 0.1， 水印高度会被自动计算）。



### setLocalVideoMirrorType

设置本地预览画面的镜像类型。
```
void setLocalVideoMirrorType(int mirrorType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mirrorType | int | 镜像类型。 |

__介绍__

接口说明：
- 默认值：TXLiveConstants#LOCAL_VIDEO_MIRROR_TYPE_AUTO。
- TXLiveConstants#LOCAL_VIDEO_MIRROR_TYPE_AUTO 表示由 SDK 决定镜像方式：前置摄像头镜像，后置摄像头不镜像。
- TXLiveConstants#LOCAL_VIDEO_MIRROR_TYPE_ENABLE 表示前置摄像头和后置摄像头都镜像。
- TXLiveConstants#LOCAL_VIDEO_MIRROR_TYPE_DISABLE 表示前置摄像头和后置摄像头都不镜像。



## 垫片推流
### setPauseImg

设置垫片推流的图片素材。
```
void setPauseImg(Bitmap img)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| img | Bitmap | bitmap 图片。 |

__介绍__

接口说明：
- 图片最大尺寸不能超过1920 × 1920。



### setPauseImg

设置垫片的帧率与最长持续时间。
```
void setPauseImg(int time, int fps)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| time | int | 时间。 |
| fps | int | 帧率。 |

__介绍__

接口说明：
- 默认值：最大持续时间为300秒，帧率为10。
- 调用 [TXLivePusher](https://cloud.tencent.com/document/product/454/34772#txlivepusher) 的 pausePush() 接口，会暂停摄像头采集并进入垫片推流状态，如果该状态一直保持， 可能会消耗主播过多的手机流量，本字段用于指定垫片推流的最大持续时间，超过后不会断开云服务器的链接，但会进入纯音频推流。
>? 若您的移动直播服务是在2018年09月之前开通的，指定垫片推流持续时间超过后即会断开云服务器的连接。



### setPauseFlag

设置后台推流的选项。
```
void setPauseFlag(int flag)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| flag | int | 选项。 |

__介绍__

接口说明：
- 默认值：TXLiveConstants#PAUSE_FLAG_PAUSE_VIDEO。
- TXLiveConstants#PAUSE_FLAG_PAUSE_VIDEO 表示暂停推流时，采用 [TXLivePushConfig#setPauseImg(Bitmap)](https://cloud.tencent.com/document/product/454/34771#setpauseimg) 传入的图片作为画面推流，声音不做暂停，继续录制麦克风或 custom 音频发送。
- TXLiveConstants#PAUSE_FLAG_PAUSE_AUDIO 表示暂停推流时，推静音数据，画面数据不做暂停，继续发送摄像头、录屏或 custom 视频数据。
- TXLiveConstants#PAUSE_FLAG_PAUSE_VIDEO|TXLiveConstants#PAUSE_FLAG_PAUSE_AUDIO 表示暂停推流时，推送暂停图片和静音数据。




## 音视频编码参数
### setVideoResolution

设置采集的视频的分辨率。
```
void setVideoResolution(int resolution)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| resolution | int | 分辨率。 |

__介绍__

接口说明：
- 默认值：TXLiveConstants#VIDEO_RESOLUTION_TYPE_540_960 。
- 其他值可参见 TXLiveConstants VIDEO_RESOLUTION_TYPE_XXX 。



### setVideoFPS

设置视频帧率。
```
void setVideoFPS(int fps)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| fps | int | 帧率。 |

__介绍__

接口说明：
- 默认值：20。



### setVideoEncodeGop

设置视频编码 GOP。
```
void setVideoEncodeGop(int gop)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| gop | int | 视频 GOP。 |

__介绍__

接口说明：
- 默认值：3，单位为秒。



### setVideoBitrate

设置视频编码码率。
```
void setVideoBitrate(int bitrate)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| bitrate | int | 视频编码码率，单位：kbps。 |

__介绍__

接口说明：
- 默认值：1200。
- 不开启码率自适应时，视频以此码率编码。



### setMaxVideoBitrate

设置最大视频码率。
```
void setMaxVideoBitrate(int maxBitrate)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| maxBitrate | int | 最大视频码率。 |

__介绍__

接口说明：
- 默认值：1000。
- 只有开启码率自适应， 该设置项才能启作用：[setAutoAdjustBitrate(boolean)](https://cloud.tencent.com/document/product/454/34771#setautoadjustbitrate)。



### setMinVideoBitrate

设置最小视频码率。
```
void setMinVideoBitrate(int minBitrate)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| minBitrate | int | 最小视频码率。 |

__介绍__

接口说明：
- 默认值：400。
- 只有开启码率自适应， 该设置项才能启作用：[setAutoAdjustBitrate(boolean)](https://cloud.tencent.com/document/product/454/34771#setautoadjustbitrate)。



### setAutoAdjustBitrate

设置是否开启码率自适应。
```
void setAutoAdjustBitrate(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：开启码率自适应，false：禁用码率自适应。 |

__介绍__

接口说明：
- 默认值：false。
- 开启后，SDK会根据网络情况自动调节视频码率，调节范围在（[videoBitrateMin](https://cloud.tencent.com/document/product/454/34774#setminautoadjustcachetime) - [videoBitrateMax](https://cloud.tencent.com/document/product/454/34774#setmaxautoadjustcachetime)）。



### setAutoAdjustStrategy

设置动态调整码率的策略。
```
void setAutoAdjustStrategy(int strategy)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| strategy | int | - |

__介绍__

接口说明：
- 默认值： TXLiveConstants#AUTO_ADJUST_BITRATE_STRATEGY_1。
- 其他值： 请参见 TXLiveConstants 类中 AUTO_ADJUST_XXX 。



### setAudioSampleRate

设置声音采样率。
```
void setAudioSampleRate(int sample)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| sample | int | 音频采样率。 |

__介绍__

接口说明：
- 默认值：48000。
- 其他值：8000、16000、32000、44100、48000。



### setAudioChannels

设置声道数。
```
void setAudioChannels(int channels)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| channels | int | 声道数。 |

__介绍__

接口说明：
- 默认值：1。
- 其他值：1、2。



### enablePureAudioPush

开启纯音频推流。
```
void enablePureAudioPush(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：启动纯音频推流；false：关闭纯音频推流。 |

__介绍__

接口说明：
- 默认值：false。
- 只有在推流启动前设置才会生效，推流过程中设置不会生效。



### enableScreenCaptureAutoRotate

设置录屏推流时是否要根据情况自适应旋转（仅用于录屏推流）。
```
void enableScreenCaptureAutoRotate(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：视频内容为屏幕旋转后最大化显示；false：视频内容为屏幕内容缩放居中显示。 |

__介绍__

接口说明：
- 默认值：false。



### enableHighResolutionCaptureMode

是否固定摄像头的采集分辨率为720p。
```
void enableHighResolutionCaptureMode(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：开启； false：关闭。 |

__介绍__

接口说明：
- 默认值：true，采用1280 × 720的采集分辨率。



### setVideoEncoderXMirror

设置观众端水平镜像。
```
void setVideoEncoderXMirror(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：镜像；false：不镜像。 |

__介绍__

接口说明：
- 默认值：false。




## 网络相关参数
### setConnectRetryCount

设置推流端重连次数。
```
void setConnectRetryCount(int count)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| count | int | 重连次数。 |

__介绍__

当 SDK 与服务器异常断开连接时，SDK 会尝试与服务器重连，通过此函数设置 SDK 重连次数。
接口说明：
- 默认值：3。
- 取值范围：1 - 10。



### setConnectRetryInterval

设置推流端重连间隔。
```
void setConnectRetryInterval(int interval)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| interval | int | SDK 重连间隔，单位秒。 |

__介绍__

当 SDK 与服务器异常断开连接时，SDK 会尝试与服务器重连，通过此函数来设置两次重连间隔时间。
接口说明：
- 默认值：3秒。
- 取值范围：3秒 - 30秒。




## 自定义采集和处理
### setCustomModeType

自定义采集和自定义处理开关。
```
void setCustomModeType(int modeType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| modeType | int | 模式类型。 |

__介绍__

接口说明：
- 该字段需要使用与运算符进行级联操作（自定义采集和自定义处理不能同时开启）： 开启自定义视频采集：　\_config.customModeType |= CUSTOM_MODE_VIDEO_CAPTURE；开启自定义音频采集：\_config.customModeType |= CUSTOM_MODE_AUDIO_CAPTURE。
- 其他值：请参见 TXLiveConstants 中 CUSTOM_MODE_XXX 。




## 专业设置项
### enableAEC

设置回声消除。
```
void enableAEC(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：开启回声消除； false：不开启。 |

__介绍__

接口说明：
- 默认值：false。
- 连麦时必须开启，非连麦时不要开启。



### enableAGC

设置自动增益。
```
void enableAGC(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：开启自动增益； false：不开启。 |

__介绍__

接口说明：
- 默认值：false。



### enableANS

设置噪声抑制。
```
void enableANS(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：开启噪声抑制； false：不开启。 |

__介绍__

接口说明：
- 默认值：false。



### setVolumeType

设置系统音量类型。
```
void setVolumeType(int volumeType)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volumeType | int | 系统音量类型 |

__介绍__

接口说明：
- 默认值：TXLiveConstants#AUDIO_VOLUME_TYPE_AUTO。
- 
- 默认值：TXLiveConstants#AUDIO_VOLUME_TYPE_AUTO。
- TXLiveConstants#AUDIO_VOLUME_TYPE_VOIP 表示通话音量类型。
- TXLiveConstants#AUDIO_VOLUME_TYPE_MEDIA 表示媒体音量类型。




### setHardwareAcceleration

设置硬件加速选项。
```
void setHardwareAcceleration(int encodeOpt)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| encodeOpt | int | 硬件加速选项。 |

__介绍__

接口说明：
- 默认值：TXLiveConstants#ENCODE_VIDEO_AUTO，自动选择是否启用硬件加速。
- 其他值：TXLiveConstants#ENCODE_VIDEO_HARDWARE，开启硬件加速，TXLiveConstants#ENCODE_VIDEO_SOFTWARE，禁用硬件加速，默认禁用硬件加速。



### enableVideoHardEncoderMainProfile

是否开启 MainProfile 硬编码模式。
```
void enableVideoHardEncoderMainProfile(boolean enable)
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | boolean | true：开启；false：关闭。 |

__介绍__

接口说明：
- 默认值：true，此参数仅在开启硬件编码加速时有效。



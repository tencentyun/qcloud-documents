__功能__

腾讯云直播推流器。

__介绍__

主要负责将本地的音频和视频画面进行编码，并推送到指定的推流地址，支持任意的推流服务端。
推流器包含如下能力：

- 自定义的视频采集，让您可以根据项目需要定制自己的音视频数据源。
- 美颜、滤镜、贴纸，包含多套美颜磨皮算法（自然&光滑）和多款色彩空间滤镜（支持自定义滤镜）。
- Qos 流量控制技术，具备上行网络自适应能力，可以根据主播端网络的具体情况实时调节音视频数据量。
- 脸形调整、动效挂件，支持基于优图 AI 人脸识别技术的大眼、瘦脸、隆鼻等脸形微调以及动效挂件效果，只需要购买 **优图 License** 就可以轻松实现丰富的直播效果。

## SDK 基础函数
### initWithLiveMode
初始化直播推流器。

```dart
  V2TXLivePusher(V2TXLiveMode liveMode)
```

#### 参数 

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| liveMode | V2TXLiveMode | 推流协议类型：RTMP/ROOM 协议，默认值：RTMP。 |

***

### addListener

设置推流器回调。通过设置回调，可以监听 V2TXLivePusher 推流器的一些回调事件，包括推流器状态、音量回调、统计数据、警告和错误信息等。

```dart
  void addListener(V2TXLivePusherObserver func)
```

#### 参数 

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| observer | V2TXLivePusherObserver | 推流器的回调目标对象，更多信息请参见 [V2TXLivePusherObserver](https://pub.dev/documentation/live_flutter_plugin/latest/v2_tx_live_pusher_observer/v2_tx_live_pusher_observer-library.html)。 |

***

## 推流基础接口
### setRenderViewID

设置本地摄像头预览 View，本地摄像头采集到的画面，经过美颜、脸形调整、滤镜等多种效果叠加之后，最终会显示到传入的 View 上。
```dart
  Future<V2TXLiveCode> setRenderViewID(int viewID) 
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| viewID | int | 本地摄像头预览视图 V2TXLiveVideoWidget.onViewCreated(int viewID)。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### startPush

开始音视频数据推流。
```dart
  Future<V2TXLiveCode> startPush(String url)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| url |  String | 推流的目标地址，支持任意推流服务端。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。
- V2TXLIVE_ERROR_INVALID_PARAMETER：操作失败，URL 不合法。
- V2TXLIVE_ERROR_REFUSED：RTC 不支持同一设备上同时推拉同一个 StreamId。

***

### stopPush

停止推送音视频数据。
```dart
  Future<V2TXLiveCode> stopPush()
```

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### isPushing

当前推流器是否正在推流中。
```dart
  Future<V2TXLiveCode> isPushing()
```

#### 返回

是否正在播放。
- 1：正在推流中。
- 0：已经停止推流。

***


## 视频相关接口
### setVideoQuality
设置推流视频编码参数。
```dart
  Future<V2TXLiveCode> setVideoQuality(V2TXLiveVideoEncoderParam param)
```
#### 参数

| 参数  | 类型    |含义           |
| ---- | ----  | ----  |
| param | [V2TXLiveVideoEncoderParam](https://pub.dev/documentation/live_flutter_plugin/latest/v2_tx_live_def/V2TXLiveVideoEncoderParam-class.html) | 视频编码参数。 |


***

### setRenderRotation

设置本地摄像头预览画面的旋转角度。
```dart
  Future<V2TXLiveCode> setRenderRotation(V2TXLiveRotation rotation)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rotation | [V2TXLiveRotation](#V2TXLiveRotation) | 旋转角度，默认值：v2TXLiveRotation0。 |

#### 返回
返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

[](id:V2TXLiveRotation)
#### V2TXLiveRotation 枚举值

| 取值 | 含义 |
|---------|---------|
| v2TXLiveRotation0 | 不旋转。 |
| v2TXLiveRotation90 | 顺时针旋转90度。 |
| v2TXLiveRotation180 | 顺时针旋转180度。 |
| v2TXLiveRotation270 | 顺时针旋转270度。 |

***

### setRenderMirror

设置本地摄像头预览镜像。
```dart
  Future<V2TXLiveCode> setRenderMirror(V2TXLiveMirrorType mirrorType)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mirrorType | [V2TXLiveMirrorType](#V2TXLiveMirrorType) | 摄像头镜像类型，默认值：v2TXLiveMirrorTypeAuto。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

[](id:V2TXLiveMirrorType)

#### V2TXLiveMirrorType枚举值

| 取值 | 含义 |
|---------|---------|
| v2TXLiveMirrorTypeAuto | 默认镜像类型. 在这种情况下，前置摄像头的画面是镜像的，后置摄像头的画面不是镜像的。 |
| v2TXLiveMirrorTypeEnable | 前置摄像头和后置摄像头都切换为镜像模式。 |
| v2TXLiveMirrorTypeDisable | 前置摄像头和后置摄像头都切换为非镜像模式。 |

***

### startCamera

打开本地摄像头。

>? startVirtualCamera、startCamera 和 startScreenCapture 同一 Pusher 实例下，仅有一个能上行，三者为覆盖关系。例如先调用 startCamera，后调用 startVirtualCamera。此时表现为暂停摄像头推流，开启图片推流。

```dart
  Future<V2TXLiveCode> startCamera(bool frontCamera)
```

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### stopCamera

关闭本地摄像头。
```dart
  Future<void> stopCamera() 
```

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***
### startVirtualCamera

开启图片推流。

>? startVirtualCamera、startCamera 和 startScreenCapture 同一 Pusher 实例下，仅有一个能上行，三者为覆盖关系。例如先调用 startCamera，后调用 startVirtualCamera。此时表现为暂停摄像头推流，开启图片推流。

```dart
  Future<V2TXLiveCode> startVirtualCamera(String type, String imageUrl)
```

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| type | String | network(网络资源), file(本地资源) |
| imageUrl | String | 资源地址 |

***

### stopVirtualCamera

关闭图片推流。

```dart
  Future<V2TXLiveCode> stopVirtualCamera()
```

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### startScreenCapture
开启屏幕采集。
>? 
>- iOS 端暂不支持通过此接口开启屏幕采集。
>- startVirtualCamera、startCamera 和 startScreenCapture 同一 Pusher 实例下，仅有一个能上行，三者为覆盖关系。例如先调用 startCamera，后调用 startVirtualCamera。此时表现为暂停摄像头推流，开启图片推流。

1. 需要通过 iOS Broadcast Upload Extension 来开启屏幕采集。
2. 然后设置 enableCustomVideoCapture 开启自定义采集支持。 
3. 最后通过 sendCustomVideoFrame 把 Broadcast Upload Extension 中采集到的屏幕画面送出去。

```dart
  Future<V2TXLiveCode> startScreenCapture(String appGroup)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| appGroup |  String | 主 App 与 Broadcast 共享的 Application Group Identifier，可以指定为 nil，但按照文档设置会使功能更加可靠。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### stopScreenCapture
关闭屏幕采集。
```dart
  Future<V2TXLiveCode> stopScreenCapture()
```
#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### snapshot

截取推流过程中的本地画面。

>? 返回值成功后可以在 `V2TXLivePusherObserver.onSnapshotComplete` 回调中获取截图图片。

```dart
  Future<V2TXLiveCode> snapshot()
```

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。
- V2TXLIVE_ERROR_REFUSED：已经停止推流，不允许调用截图操作。

***

### setWatermark
设置推流器水印。默认情况下，水印不开启。
```dart
  Future<V2TXLiveCode> setWatermark(String type, String image, double x,
      double y, double scale)
```
#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| type | String | network(网络资源), file(本地资源) |
| image | String | 资源地址 |
| x | double | 水印的坐标。 |
| y | double | 水印的坐标。 |
| scale | double | 水印的缩放比例。 |

***

### setEncoderMirror
设置视频编码镜像。
```dart
  Future<V2TXLiveCode> setEncoderMirror(bool mirror)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mirror | bool | 是否镜像。默认值：false。 |

***

### enableCustomVideoCapture

开启/关闭自定义视频采集。在自定义视频采集模式下，SDK 不再从摄像头采集图像，只保留编码和发送能力。
```dart
  Future<V2TXLiveCode> enableCustomVideoCapture(bool enable)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | bool | 是否开启自定义采集。默认值：false。 |

***

### sendCustomVideoFrame
在自定义视频采集模式下，将采集的视频数据发送到 SDK。
```dart
  Future<V2TXLiveCode> sendCustomVideoFrame(V2TXLiveVideoFrame videoFrame)
```
#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| videoFrame | V2TXLiveVideoFrame | 向 SDK 发送的 视频帧数据。 |

#### 返回
返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。
- V2TXLIVE_ERROR_INVALID_PARAMETER：发送失败，视频帧数据不合法。
- V2TXLIVE_ERROR_REFUSED：发送失败，您必须先调用 enableCustomVideoCapture 开启自定义视频采集。

***

### enableCustomVideoProcess
开启/关闭自定义视频处理。
```dart
  Future<V2TXLiveCode> enableCustomVideoProcess(bool enable,
      V2TXLivePixelFormat pixelFormat, V2TXLiveBufferType bufferType)
```
#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | bool | 是否开启自定义视频处理。默认值：false。 |
| pixelFormat | V2TXLivePixelFormat | 视频帧的像素格式。 |
| bufferType | V2TXLiveBufferType | 视频数据包装格式。 |

[](id:V2TXLivePixelFormat)
#### V2TXLivePixelFormat 枚举值
| 取值 | 说明 |
|---------|---------|
|  v2TXLivePixelFormatUnknown | 未知。 |
|  v2TXLivePixelFormatI420|  YUV420P I420。 |
|  v2TXLivePixelFormatTexture2D | OpenGL 2D 纹理。 |

[](id:V2TXLiveBufferType)
#### V2TXLiveBufferType 枚举值
| 取值 | 说明 |
|---------|---------|
| v2TXLiveBufferTypeUnknown | 未知。 |
| v2TXLiveBufferTypeByteBuffer|  DirectBuffer，装载 I420 等 buffer，在 native 层使用。 |
|  v2TXLiveBufferTypeByteArray|  byte[]，装载 I420 等 buffer，在 Java 层使用。 |
|  v2TXLiveBufferTypeTexture| 直接操作纹理 ID，性能最好，画质损失最少。 |

***

### sendSeiMessage
发送 SEI 消息。播放端 [V2TXLivePlayer](https://pub.dev/documentation/live_flutter_plugin/latest/v2_tx_live_player/V2TXLivePlayer-class.html) 通过 [V2TXLivePlayerObserver](https://pub.dev/documentation/live_flutter_plugin/latest/v2_tx_live_player_observer/v2_tx_live_player_observer-library.html) 中的 `onReceiveSeiMessage` 回调来接收该消息。
```dart
  Future<V2TXLiveCode> sendSeiMessage(int payloadType, Uint8List data)
```
#### 参数
| 参数 | 类型 | 含义 |
|-----|-----|-----|
| payloadType | int | 数据类型，支持 5、242。推荐填：242 |
| data | Uint8List | 待发送的数据 | 

 #### 返回
 返回值 V2TXLiveCode：
 - V2TXLIVE_OK：成功。

***

## 美颜相关接口
### getBeautyManager
获取美颜管理对象 [TXBeautyManager](https://pub.dev/documentation/live_flutter_plugin/latest/manager_tx_beauty_manager/manager_tx_beauty_manager-library.html)。
通过美颜管理，您可以使用以下功能：

- 设置”美颜风格”、”美白”、“红润”、“大眼”、“瘦脸”、“V脸”、“下巴”、“短脸”、“小鼻”、“亮眼”、“白牙”、“祛眼袋”、“祛皱纹”、“祛法令纹”等美容效果。
- 调整“发际线”、“眼间距”、“眼角”、“嘴形”、“鼻翼”、“鼻子位置”、“嘴唇厚度”、“脸型”。
- 设置人脸挂件（素材）等动态效果。
- 添加美妆。
- 进行手势识别。

```dart
  TXBeautyManager getBeautyManager()
```

***

## 音频相关接口
### startMicrophone

打开麦克风。
```dart
  Future<V2TXLiveCode> startMicrophone()
```
#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***
### stopMicrophone

关闭麦克风。
```dart
  Future<V2TXLiveCode> stopMicrophone()
```
#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### setAudioQuality

设置推流音频质量。
```dart
  Future<V2TXLiveCode> setAudioQuality(V2TXLiveAudioQuality quality)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| quality | V2TXLiveAudioQuality | 音频质量。 |

#### V2TXLiveAudioQuality 枚举值
| 取值 | 说明 |
|---------|---------|
|  v2TXLiveAudioQualitySpeech | 语音音质。采样率：16k、单声道、音频码率：16kbps。<br>适合语音通话为主的场景，例如在线会议，语音通话。 |
|  v2TXLiveAudioQualityDefault|  默认音质。采样率：48k、单声道、音频码率：50kbps。<br>SDK 默认的音频质量，如无特殊需求推荐选择之。 |
|  v2TXLiveAudioQualityMusic | 音乐音质。采样率：48k、双声道 + 全频带、音频码率：128kbps。<br>适合需要高保真传输音乐的场景，例如 K 歌、音乐直播等。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。
- V2TXLIVE_ERROR_REFUSED：推流过程中，不允许调整音质。
***

### enableVolumeEvaluation

启用采集音量大小提示。
>? 开启后可以在 `V2TXLivePusherObserver.onMicrophoneVolumeUpdate` 回调中获取到 SDK 对音量大小值的评估。

```dart
  Future<V2TXLiveCode> enableVolumeEvaluation(int intervalMs)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| intervalMs | int | 决定了 onMicrophoneVolumeUpdate 音量大小回调的触发间隔，单位为 ms，最小间隔为 100ms，如果小于等于0则会关闭回调，建议设置为 300ms。默认值：0，不开启。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

## 音效相关接口
### getAudioEffectManager


获取音效管理对象 [TXAudioEffectManager](https://pub.dev/documentation/live_flutter_plugin/latest/manager_tx_audio_effect_manager/manager_tx_audio_effect_manager-library.html)。
通过音效管理，您可以使用以下功能：

- 调整麦克风收集的人声音量。
- 设置混响和变声效果。
- 开启耳返，并设置耳返的音量。
- 添加背景音乐，调整背景音乐的播放效果。

```dart
  TXAudioEffectManager getAudioEffectManager()
```

***

## 设备管理相关接口
### getDeviceManager

获取设备管理对象 [TXDeviceManager](https://pub.dev/documentation/live_flutter_plugin/latest/manager_tx_device_manager/manager_tx_device_manager-library.html)。
通过设备管理，您可以使用以下功能：

- 切换前后摄像头。
- 设置自动聚焦。
- 设置摄像头缩放倍数。
- 打开或关闭闪光灯。

```dart
  TXDeviceManager getDeviceManager()
```

***
## 更多实用接口
### setProperty

调用 V2TXLivePusher 的高级 API 接口。
```dart
  Future<V2TXLiveCode> setProperty(String key, String value)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| key | String | 高级 API 对应的 key。 |
| value | String | 调用 key 所对应的高级 API 时，需要的参数。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。
- V2TXLIVE_ERROR_INVALID_PARAMETER：操作失败，key 不允许为空。

***

### setMixTranscodingConfig
设置云端的混流转码参数。如果您在 [实时音视频控制台](https://console.cloud.tencent.com/trtc/) 中的功能配置页开启了“启用旁路推流”功能，每一路画面都会有一个默认的直播 [CDN 地址](https://cloud.tencent.com/document/product/647/16826)。一个直播间中可能有不止一位主播，而且每个主播都有自己的画面和声音，但对于 CDN 观众来说，他们只需要一路直播流，所以您需要将多路音视频流混成一路标准的直播流，这就需要混流转码。
```dart
  Future<V2TXLiveCode> setMixTranscodingConfig(V2TXLiveTranscodingConfig? config)
```
#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| config | V2TXLiveTranscodingConfig | 云端混流（转码）配置。 |

#### V2TXLiveTranscodingConfig 
| 取值 | 说明 |
|---------|---------|
| v2TXLiveBufferTypeUnknown | 未知。 |
| v2TXLiveBufferTypeByteBuffer|  DirectBuffer，装载 I420 等 buffer，在 native 层使用。 |
| v2TXLiveBufferTypeByteArray|  byte[]，装载 I420 等 buffer，在 Java 层使用。 |
| v2TXLiveBufferTypeTexture| 直接操作纹理 ID，性能最好，画质损失最少。 |

***

### showDebugView

显示仪表盘。
```dart
  Future<V2TXLiveCode> showDebugView(bool isShow)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isShow | bool | 是否显示，默认值：fasle。 |

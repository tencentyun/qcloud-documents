__功能__

腾讯云直播的推流的回调通知。

**介绍**

可以接收 [V2TXLivePusher](https://pub.dev/documentation/live_flutter_plugin/latest/v2_tx_live_pusher/v2_tx_live_pusher-library.html) 推流器的一些推流通知，包括推流器连接状态、音视频首帧回调、统计数据、警告和错误信息等。


## SDK 基础回调
### onError

直播推流器错误通知，推流出现错误时，会回调该通知。
```dart
V2TXLivePusherListenerType.onError
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code      | V2TXLiveCode    | 错误码。   |
| msg       | String | 错误信息。 |
| extraInfo | Map | 扩展信息。 |

***

### onWarning

直播推流器警告通知。
```dart
V2TXLivePusherListenerType.onWarning
```
 
#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code      | V2TXLiveCode    | 警告码。   |
| msg       | String | 警告信息。 |
| extraInfo | Map | 扩展信息。 |

***

## 视频相关回调
### onPushStatusUpdate

直播推流器连接状态回调通知。
```dart
V2TXLivePusherListenerType.onPushStatusUpdate
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| status    | V2TXLivePushStatus | 状态码。       |
| msg       | String         | 连接状态信息。 |
| extraInfo | Map     | 扩展信息。     |

[](id:V2TXLivePushStatus)

#### V2TXLivePushStatus 枚举值

| 取值 | 含义 |
|---------|---------|
| V2TXLivePushStatusDisconnected: 0 | 与服务器断开连接。 |
| V2TXLivePushStatusConnecting: 1 | 正在连接服务器。 |
| V2TXLivePushStatusConnectSuccess: 2 | 连接服务器成功。 |
| V2TXLivePushStatusReconnecting:  3| 重连服务器中。 |

***

### onSnapshotComplete

截图回调。
```dart
V2TXLivePusherListenerType.onSnapshotComplete
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| image | Uint8List | 已截取的视频画面。 |

***

### onProcessVideoFrame

自定义视频处理回调。
>? 调用 `V2TXLivePusher.enableCustomVideoProcess(bool enable, V2TXLivePixelFormat pixelFormat, V2TXLiveBufferType bufferType)` 开启自定义视频处理后，会收到这个回调通知。

```dart
V2TXLivePusherListenerType.onProcessVideoFrame
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| srcFrame | Map | 用于承载未处理的视频画面。 |
| dstFrame | Map | 用于承载处理过的视频画面。 |

***

### onGLContextDestroyed
自定义视频处理 GL 环境销毁回调。
```dart
V2TXLivePusherListenerType.onGLContextDestroyed
```
***

### onCaptureFirstVideoFrame
首帧视频采集完成的回调通知。
```dart
V2TXLivePusherListenerType.onCaptureFirstVideoFrame
```

***
## 音频相关回调
### onCaptureFirstAudioFrame
首帧音频采集完成的回调通知。
```dart
V2TXLivePusherListenerType.onCaptureFirstAudioFrame
```

***

### onMicrophoneVolumeUpdate
麦克风采集音量值回调。
```dart
V2TXLivePusherListenerType.onMicrophoneVolumeUpdate
```

***

## 统计回调
### onStatisticsUpdate
直播推流器统计数据回调。
```dart
V2TXLivePusherListenerType.onStatisticsUpdate
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| statistics | Map | 推流器统计数据。 |

***

## 混流回调
### onSetMixTranscodingConfig
设置云端的混流转码参数的回调。

> ? 调用 `V2TXLivePusher.setMixTranscodingConfig(V2TXLiveTranscodingConfig config)` 设置云端混流转码参数后，会收到这个回调通知。

```dart
V2TXLivePusherListenerType.onSetMixTranscodingConfig
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | V2TXLiveCode | 0 表示成功，其余值表示失败。 |
| msg | String | 具体错误原因。 |


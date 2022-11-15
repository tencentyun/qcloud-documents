
__功能__

腾讯云直播的播放器回调通知。


__介绍__

可以接收 [V2TXLivePlayer](https://pub.dev/documentation/live_flutter_plugin/latest/v2_tx_live_player/v2_tx_live_player-library.html) 播放器的一些回调通知，包括播放器状态、播放音量回调、音视频首帧回调、统计数据、警告和错误信息等。


## SDK 基础回调
### onError

直播播放器错误通知，播放器出现错误时，会回调该通知。
```dart
V2TXLivePlayerListenerType.onError
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | V2TXLiveCode |  错误码。 |
| msg | String |  错误信息。 |
| extraInfo | Map |  扩展信息。 |

***

### onWarning

直播播放器警告通知。
```dart
V2TXLivePlayerListenerType.onWarning
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | V2TXLiveCode |  警告码。 |
| msg | String |  警告码信息。 |
| extraInfo | Map |  扩展信息。 |

***

### onConnected

已经成功连接到服务器通知。
```dart
V2TXLivePlayerListenerType.onConnected
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| extraInfo | Map |  扩展信息。 |

***

## 视频相关回调
### onVideoPlaying

视频播放事件通知。
```dart
V2TXLivePlayerListenerType.onVideoPlaying
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| firstPlay | bool |  第一次播放标志。 |
| extraInfo | Map |  扩展信息。 |

***

### onVideoLoading

视频加载事件通知。
```dart
V2TXLivePlayerListenerType.onVideoLoading
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| extraInfo | Map |  扩展信息。 |

***

### onVideoResolutionChanged

直播播放器分辨率变化通知。
```dart
V2TXLivePlayerListenerType.onVideoResolutionChanged
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| width | int | 视频宽 |
| height | int | 视频高 |

***

### onSnapshotComplete

截图回调。
```dart
V2TXLivePlayerListenerType.onSnapshotComplete
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| image | Uint8List | 已截取的视频画面。 |

***

### onRenderVideoFrame

自定义视频渲染回调。
> ? 调用 `V2TXLivePlayer.enableCustomRendering(pixelFormat:bufferType:)` 开启自定义渲染之后，会收到这个回调通知。

```dart
V2TXLivePlayerListenerType.onRenderVideoFrame
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| videoFrame | Map | 视频帧数据。 |

***


## 音频相关回调

### onAudioPlaying

音频播放事件通知。
```dart
V2TXLivePlayerListenerType.onAudioPlaying
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| firstPlay | bool |  第一次播放标志。 |
| extraInfo | Map |  扩展信息。 |

***

### onAudioLoading

音频加载事件通知。
```dart
V2TXLivePlayerListenerType.onAudioLoading
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| extraInfo | Map |  扩展信息。 |

***


### onPlayoutVolumeUpdate

播放器音量大小回调。
```dart
V2TXLivePlayerListenerType.onPlayoutVolumeUpdate
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 音量大小，取值范围：0 - 100。 |

***

## 统计回调

### onStatisticsUpdate

直播播放器统计数据回调。
```dart
V2TXLivePlayerListenerType.onStatisticsUpdate
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| statistics | Map | 播放器统计数据。 |

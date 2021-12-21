**功能**

腾讯云直播的播放器回调通知。


**介绍**

可以接收 [V2TXLivePlayer](https://cloud.tencent.com/document/product/454/56045) 播放器的一些回调通知，包括播放器状态、播放音量回调、音视频首帧回调、统计数据、警告和错误信息等。


## SDK 基础回调
### onError

直播播放器错误通知，播放器出现错误时，会回调该通知。
```
public void onError(V2TXLivePlayer player, int code, String msg, Bundle extraInfo)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| code | int |  错误码。 |
| msg |  String |  错误信息。 |
| extraInfo | Bundle|  扩展信息。 |

***

### onWarning

直播播放器警告通知。
```
public void onWarning(V2TXLivePlayer player, int code, String msg, Bundle extraInfo)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| code | int |  警告码。 |
| msg | String |  警告码信息。 |
| extraInfo | Bundle |  扩展信息。 |

***

## 视频相关回调
### onVideoResolutionChanged

直播播放器分辨率变化通知

```
public void onVideoResolutionChanged(V2TXLivePlayer player, int width, int height) 
```
#### 参数
| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| width | int |  视频宽。 |
| width | int |  视频高。 |

### onVideoLoading

视频加载事件。

```
public void onVideoLoading(V2TXLivePlayer player, Bundle extraInfo)
```
#### 参数
| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| extraInfo | Bundle |  扩展信息。 |

### onVideoPlaying

视频播放事件。

```
public void onVideoPlaying(V2TXLivePlayer player, boolean firstPlay, Bundle extraInfo)
```
#### 参数
| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| firstPlay | boolean | 第一次播放标志 |
| extraInfo | Bundle |  扩展信息。 |

### onSnapshotComplete

截图回调。
```
public void onSnapshotComplete(V2TXLivePlayer player, Bitmap image)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| image | Bitmap * | 已截取的视频画面。 |

***

### onRenderVideoFrame

自定义视频渲染回调。
> 调用 `[V2TXLivePlayer enableCustomRendering:pixelFormat:bufferType:]` 开启自定义渲染之后，会收到这个回调通知。
```
public void onRenderVideoFrame(V2TXLivePlayer player, V2TXLiveVideoFrame videoFrame)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| videoFrame | V2TXLiveVideoFrame | 视频帧数据。 |

***


## 音频相关回调
### onAudioLoading

音频加载事件。

```
public void onAudioLoading(V2TXLivePlayer player, Bundle extraInfo)
```
#### 参数
| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| extraInfo | Bundle |  扩展信息。 |

### onAudioPlaying

音频播放事件。

```
public void onAudioPlaying(V2TXLivePlayer player, boolean firstPlay, Bundle extraInfo)
```
#### 参数
| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| firstPlay | boolean | 第一次播放标志 |
| extraInfo | Bundle |  扩展信息。 |

### onPlayoutVolumeUpdate

播放器音量大小回调。
```
public void onPlayoutVolumeUpdate(V2TXLivePlayer player, int volume)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| volume | int | 音量大小，取值范围：0 - 100。 |

***

## 统计回调
### onStatisticsUpdate
直播播放器统计数据回调。
```
public void onStatisticsUpdate(V2TXLivePlayer player, V2TXLivePlayerStatistics statistics)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| statistics | V2TXLivePlayerStatistics | 播放器统计数据。 |



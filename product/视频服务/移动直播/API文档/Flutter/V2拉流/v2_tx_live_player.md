
__功能__

腾讯云直播播放器。
主要负责从指定的直播流地址拉取音视频数据，并进行解码和本地渲染播放。

__介绍__

播放器包含如下能力：

- 支持 RTMP、HTTP-FLV、TRTC、WebRTC 协议。
- 屏幕截图，可以截取当前直播流的视频画面。
- 延时调节，可以设置播放器缓存自动调整的最小和最大时间。
- 自定义的视频数据处理，您可以根据项目需要处理直播流中的视频数据后，再进行渲染以及播放。


## SDK 基础函数
### addListener

设置播放器回调。通过设置回调，可以监听 V2TXLivePlayer 播放器的一些回调事件，包括播放器状态、播放音量回调、音视频首帧回调、统计数据、警告和错误信息等。

```dart
  void addListener(V2TXLivePlayerObserver func)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| observer | V2TXLivePlayerObserver | 播放器的回调目标对象，详情请参见 [V2TXLivePlayerObserver](https://cloud.tencent.com/document/product/454/56047)。 |

***

## 播放基础接口
### setRenderViewID

设置播放器渲染 View，该控件负责显示视频内容。
```dart
  Future<V2TXLiveCode> setRenderViewID(int viewID)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| viewID | int | 播放器渲染 V2TXLiveVideoWidget.onViewCreated viewId。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### startPlay

开始播放音视频流。
```dart
  Future<V2TXLiveCode> startPlay(String url)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| url | String | 音视频流的播放地址，支持 RTMP、HTTP-FLV、TRTC、WebRTC 协议。|

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。
- V2TXLIVE_ERROR_INVALID_PARAMETER：操作失败，URL不合法。
- V2TXLIVE_ERROR_REFUSED：RTC 不支持同一设备上同时推拉同一个 StreamId。

***

### stopPlay

停止播放音视频流。
```dart
  Future<V2TXLiveCode> stopPlay()
```

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### isPlaying

播放器是否正在播放中。
```dart
  Future<int> isPlaying()
```

#### 返回

是否正在播放。
- 1：正在播放中。
- 0：已经停止播放。

***

## 视频相关接口
### setRenderRotation

设置播放器画面的旋转角度。
```dart
  Future<V2TXLiveCode> setRenderRotation(V2TXLiveRotation rotation)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rotation | [V2TXLiveRotation](#V2TXLiveRotation ) | 旋转角度，默认值：0。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

[](id:V2TXLiveRotation )

#### V2TXLiveRotation 枚举值

| 取值                | 含义            |
| ------------------- | --------------- |
| v2TXLiveRotation0   | 不旋转。          |
| v2TXLiveRotation90  | 顺时针旋转90度。  |
| v2TXLiveRotation180 | 顺时针旋转180度。 |
| v2TXLiveRotation270 | 顺时针旋转270度。 |

***

### setRenderFillMode

设置画面的填充模式。
```dart
  Future<V2TXLiveCode> setRenderFillMode(V2TXLiveFillMode mode) 
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mode | [V2TXLiveFillMode](#V2TXLiveFillMode) | 画面填充模式，默认值：v2TXLiveFillModeFit。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

[](id:V2TXLiveFillMode )

#### V2TXLiveFillMode 枚举值

| 取值                 | 含义                                                         |
| -------------------- | ------------------------------------------------------------ |
| v2TXLiveFillModeFit  | 图像适应屏幕，保持画面完整，但如果图像宽高比不同于屏幕宽高比，会有黑边的存在。 |
| v2TXLiveFillModeFill | 图像铺满屏幕，不留黑边，如果图像宽高比不同于屏幕宽高比，部分画面内容会被裁剪掉。 |

***

### pauseVideo

暂停播放器的视频流。
```dart
  Future<V2TXLiveCode> pauseVideo()
```

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***


### resumeVideo

恢复播放器的视频流。
```dart
  Future<V2TXLiveCode> resumeVideo()
```

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### snapshot

截取播放过程中的视频画面。

> ? 返回值成功后可以在 `V2TXLivePlayerObserver.onSnapshotComplete` 回调中获取截图图片。

```dart
  Future<V2TXLiveCode> snapshot()
```

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。
- V2TXLIVE_ERROR_REFUSED：播放器处于停止状态，不允许调用截图操作。

***

## 音频相关接口
### pauseAudio

 暂停播放器的音频流。
```dart
  Future<V2TXLiveCode> pauseAudio()
```
#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***
### resumeAudio

 恢复播放器的音频流。
```dart
  Future<V2TXLiveCode> resumeAudio()
```
#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### setPlayoutVolume

设置音量。
```dart
  Future<V2TXLiveCode> setPlayoutVolume(int volume) 
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| volume | int | 音量大小，取值范围0 - 100，默认值：100。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### enableVolumeEvaluation

启用播放音量大小提示。
> ? 开启后可以在 `V2TXLivePlayerObserver.onPlayoutVolumeUpdate` 回调中获取到 SDK 对音量大小值的评估。
```dart
  Future<V2TXLiveCode> enableVolumeEvaluation(int intervalMs)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| intervalMs | int | onPlayoutVolumeUpdate 音量大小回调的触发间隔，单位为 ms，最小间隔为 100ms。如果小于等于0则会关闭回调，建议设置为 300ms。默认值：0，不开启。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***


## 更多实用接口
### setCacheParams

设置播放器缓存自动调整的最小和最大时间（ 单位：秒）。
```dart
  Future<V2TXLiveCode> setCacheParams(double minTime, double maxTime)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| minTime | double | 缓存自动调整的最小时间，取值需要大于0。默认值：1。 |
| maxTime | double | 缓存自动调整的最大时间，取值需要大于0。默认值：5。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。
- V2TXLIVE_ERROR_INVALID_PARAMETER：操作失败，minTime 和 maxTime 需要大于0。
- V2TXLIVE_ERROR_REFUSED：播放器处于播放状态，不支持修改缓存策略。

***

### showDebugView

是否显示播放器状态信息的调试浮层。
```dart
  Future<void> showDebugView(bool isShow)
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isShow | bool | 是否显示，默认值：false。 |

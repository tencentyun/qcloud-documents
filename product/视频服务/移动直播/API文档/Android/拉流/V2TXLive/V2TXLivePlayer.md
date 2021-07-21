
__功能__

腾讯云直播播放器。
主要负责从指定的直播流地址拉取音视频数据，并进行解码和本地渲染播放。

__介绍__

播放器包含如下能力:

- 支持RTMP、HTTP-FLV、TRTC、WebRTC。
- 屏幕截图，可以截取当前直播流的视频画面。
- 延时调节，可以设置播放器缓存自动调整的最小和最大时间。
- 自定义的视频数据处理，您可以根据项目需要处理直播流中的视频数据后，再进行渲染以及播放。


## SDK 基础函数
### setObserver

设置播放器回调。通过设置回调，可以监听 V2TXLivePlayer 播放器的一些回调事件，包括播放器状态、播放音量回调、音视频首帧回调、统计数据、警告和错误信息等。

```
public abstract void setObserver(V2TXLivePlayerObserver observer);
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| observer | V2TXLivePlayerObserver | 播放器的回调目标对象，更多详情请参见 [V2TXLivePlayerObserver](https://cloud.tencent.com/document/product/454/56049)。 |

***

## 播放基础接口
### setRenderView

设置播放器渲染 View，该控件负责显示视频内容。
```
public abstract int setRenderView(TXCloudVideoView view);
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| view | TXCloudVideoView| 播放器渲染 View。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### setRenderView

设置播放器渲染 View，该控件负责显示视频内容。
```
public abstract int setRenderView(SurfaceView view);
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| view | SurfaceView | 播放器渲染 View。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### setRenderView

设置播放器渲染 View，该控件负责显示视频内容。
```
public abstract int setRenderView(TextureView view);
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| view | TextureView | 播放器渲染 View。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### startPlay

开始播放音视频流。
```
public abstract int startPlay(String url);
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| url |  String | 音视频流的播放地址，支持 RTMP、HTTP-FLV、TRTC、WebRTC 协议。|

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。
- V2TXLIVE_ERROR_INVALID_PARAMETER：操作失败，URL 不合法。
- V2TXLIVE_ERROR_REFUSED：RTC 不支持同一设备上同时推拉同一个 StreamId。

***

### stopPlay

停止播放音视频流。
```
public abstract int stopPlay();
```

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### isPlaying

播放器是否正在播放中。
```
public abstract int isPlaying();
```

#### 返回

是否正在播放。
- 1：正在播放中。
- 0：已经停止播放。

***

## 视频相关接口
### setRenderRotation

设置播放器画面的旋转角度。
```
public abstract int setRenderRotation(V2TXLiveRotation rotation);
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| rotation | [V2TXLiveRotation](#V2TXLiveRotation) | 旋转角度，默认值：V2TXLiveRotation0。 |

#### 返回
返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

[](id:V2TXLiveRotation)
#### V2TXLiveRotation 枚举值

| 取值 | 含义 | 
|---------|---------|
| V2TXLiveRotation0 | 不旋转。 | 
| V2TXLiveRotation90 | 顺时针旋转90度。 | 
| V2TXLiveRotation180 | 顺时针旋转180度。 | 
| V2TXLiveRotation270 | 顺时针旋转270度。 | 

***

### setRenderFillMode

设置画面的填充模式。
```
public abstract int setRenderFillMode(V2TXLiveFillMode mode);
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| mode | [V2TXLiveFillMode](#V2TXLiveFillMode)   | 画面填充模式，默认值：V2TXLiveFillModeFit。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

[](id:V2TXLiveFillMode)
#### V2TXLiveFillMode 枚举值

| 取值 | 含义 |
|---------|---------|
| V2TXLiveFillModeFit | 图像适应屏幕，保持画面完整，但如果图像宽高比不同于屏幕宽高比，会有黑边的存在。 | 
| V2TXLiveFillModeFill | 图像铺满屏幕，不留黑边，如果图像宽高比不同于屏幕宽高比，部分画面内容会被裁剪掉。 | 

***

### pauseVideo

暂停播放器的视频流。
```
public abstract int pauseVideo();
```

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***


### resumeVideo

恢复播放器的视频流。
```
public abstract int resumeVideo();
```

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### snapshot

截取播放过程中的视频画面。

>? 返回值成功后可以在 `V2TXLivePlayerObserver.onSnapshotComplete` 回调中获取截图图片。

```
public abstract int snapshot();
```

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。
- V2TXLIVE_ERROR_REFUSED：播放器处于停止状态，不允许调用截图操作。

***

### enableCustomRendering

设置视频自定义渲染回调。通过该方法，可以获取解码后的每一帧视频画面，进行自定义渲染处理，添加自定义显示效果。
>? 开启成功后可在 `V2TXLivePlayerObserver.onRenderVideoFrame` 回调中获取视频帧数据。
```
public abstract int enableCustomRendering(
        boolean enable,
        V2TXLivePixelFormat pixelFormat, 
        V2TXLiveBufferType bufferType);
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| enable | Boolean | 是否开启自定义渲染。默认值：false。 |
| pixelFormat | [V2TXLivePixelFormat](#V2TXLivePixelFormat) | 自定义渲染回调的视频像素格式。 |
| bufferType | [V2TXLiveBufferType](#V2TXLiveBufferType) | 自定义渲染回调的视频数据格式。 |

#### 返回
返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。
- V2TXLIVE_ERROR_NOT_SUPPORTED：像素格式或者数据格式不支持。

[](id:V2TXLivePixelFormat)
#### V2TXLivePixelFormat 枚举值
| 取值 | 说明 | 
|---------|---------|
|  V2TXLivePixelFormatUnknown | 未知。 | 
|  V2TXLivePixelFormatI420|  YUV420P I420。 | 
|  V2TXLivePixelFormatTexture2D | OpenGL 2D 纹理。 | 

[](id:V2TXLiveBufferType)
#### V2TXLiveBufferType 枚举值
| 取值 | 说明 | 
|---------|---------|
| V2TXLiveBufferTypeUnknown | 未知。 | 
| V2TXLiveBufferTypeByteBuffer|  DirectBuffer，装载 I420 等 buffer，在 native 层使用。 | 
|  V2TXLiveBufferTypeByteArray|  byte[]，装载 I420 等 buffer，在 Java 层使用。 | 
|  V2TXLiveBufferTypeTexture| 直接操作纹理 ID，性能最好，画质损失最少。 |




***

## 音频相关接口
### pauseAudio

 暂停播放器的音频流。
```
public abstract int pauseAudio();
```
#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***
### resumeAudio

 恢复播放器的音频流。
```
public abstract int resumeAudio();
```
#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***

### setPlayoutVolume

设置音量。
```
public abstract int setPlayoutVolume(int volume);
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
>? 开启后可以在 `V2TXLivePlayerObserver.onPlayoutVolumeUpdate` 回调中获取到 SDK 对音量大小值的评估。
```
public abstract int enableVolumeEvaluation(int intervalMs);
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| intervalMs | int | onPlayoutVolumeUpdate 音量大小回调的触发间隔，单位为 ms，最小间隔为 100ms，如果小于等于0则会关闭回调，建议设置为 300ms。默认值：0，不开启。 |

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。

***


## 更多实用接口
### setCacheParams

设置播放器缓存自动调整的最小和最大时间 ( 单位：秒 )。
```
public abstract int setCacheParams(float minTime, float maxTime);
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| minTime | float | 缓存自动调整的最小时间，取值需要大于0。默认值：1。|
| maxTime | float | 缓存自动调整的最大时间，取值需要大于0。默认值：5。|

#### 返回

返回值 V2TXLiveCode：
- V2TXLIVE_OK：成功。
- V2TXLIVE_ERROR_INVALID_PARAMETER：操作失败，minTime 和 maxTime 需要大于0。
- V2TXLIVE_ERROR_REFUSED：播放器处于播放状态，不支持修改缓存策略。

***

### showDebugView

是否显示播放器状态信息的调试浮层。
```
public abstract void showDebugView(boolean isShow);
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| isShow | boolean | 是否显示，默认值：NO。 |



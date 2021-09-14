**功能**

腾讯云直播的推流的回调通知。

**介绍**

可以接收 [V2TXLivePusher](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__android.html) 推流器的一些推流通知，包括推流器连接状态、音视频首帧回调、统计数据、警告和错误信息等。


## SDK 基础回调
### onError

直播推流器错误通知，推流出现错误时，会回调该通知。
```
public void onError(int code, String msg, Bundle extraInfo)
```

#### 参数

| 参数      | 类型   | 含义       |
| --------- | ------ | ---------- |
| code      | int    | 错误码。   |
| msg       | String | 错误信息。 |
| extraInfo | Bundle | 扩展信息。 |

***

### onWarning

直播推流器警告通知。
```
public void onWarning(int code, String msg, Bundle extraInfo)
```

#### 参数

| 参数      | 类型   | 含义         |
| --------- | ------ | ------------ |
| code      | int    | 警告码。     |
| msg       | String | 警告码信息。 |
| extraInfo | Bundle | 扩展信息。   |

***

## 视频相关回调
### onPushStatusUpdate

直播推流器连接状态回调通知。
```
public void onPushStatusUpdate(V2TXLivePushStatus status, String msg, Bundle extraInfo)
```

#### 参数

| 参数      | 类型               | 含义           |
| --------- | ------------------ | -------------- |
| status    | V2TXLivePushStatus | 状态码。       |
| msg       | String             | 连接状态信息。 |
| extraInfo | Bundle             | 扩展信息。     |

#### V2TXLivePushStatus 枚举值

| 取值                             | 含义               |
| -------------------------------- | ------------------ |
| V2TXLivePushStatusDisconnected   | 与服务器断开连接。 |
| V2TXLivePushStatusConnecting     | 正在连接服务器。   |
| V2TXLivePushStatusConnectSuccess | 连接服务器成功。   |
| V2TXLivePushStatusReconnecting   | 重连服务器中。     |

***

### onSnapshotComplete

截图回调。
```
public void onSnapshotComplete(Bitmap image)
```

#### 参数

| 参数  | 类型     | 含义               |
| ----- | -------- | ------------------ |
| image | Bitmap * | 已截取的视频画面。 |

***

### onProcessVideoFrame

自定义视频处理回调。
>? 调用 `V2TXLivePusher#enableCustomVideoProcess(boolean, V2TXLiveDef.V2TXLivePixelFormat, V2TXLiveDef.V2TXLiveBufferType)` 开启自定义视频处理后，会收到这个回调通知。

```
public void onProcessVideoFrame(V2TXLiveVideoFrame srcFrame, V2TXLiveVideoFrame dstFrame)
```

#### 参数

| 参数     | 类型               | 含义                       |
| -------- | ------------------ | -------------------------- |
| srcFrame | V2TXLiveVideoFrame | 用于承载未处理的视频画面。 |
| dstFrame | V2TXLiveVideoFrame | 用于承载处理过的视频画面。 |

***
### onGLContextCreated
自定义视频处理 GL 环境创建回调。
```
public void onGLContextCreated()
```
***

### onGLContextDestroyed
自定义视频处理GL环境销毁回调。
```
public void onGLContextDestroyed()
```

***

### onCaptureFirstVideoFrame
首帧视频采集完成的回调通知。
```
public void onCaptureFirstVideoFrame()
```

***

## 音频相关回调
### onCaptureFirstAudioFrame
首帧音频采集完成的回调通知。
```
public void onCaptureFirstAudioFrame()
```

***

### onMicrophoneVolumeUpdate
麦克风采集音量值回调。
```
public void onMicrophoneVolumeUpdate(int volume)
```

***

## 统计回调
### onStatisticsUpdate
直播推流器统计数据回调。
```
public void onStatisticsUpdate(V2TXLivePusherStatistics statistics)
```

#### 参数

| 参数       | 类型                     | 含义             |
| ---------- | ------------------------ | ---------------- |
| statistics | V2TXLivePusherStatistics | 推流器统计数据。 |

***

## 混流回调
### onSetMixTranscodingConfig
设置云端的混流转码参数的回调。

> ? 调用 `V2TXLivePusher#setMixTranscodingConfig(V2TXLiveDef.V2TXLiveTranscodingConfig)` 设置云端混流转码参数后，会收到这个回调通知。

```
public void onSetMixTranscodingConfig(int code, String msg)
```
| 参数 | 类型   | 含义                         |
| ---- | ------ | ---------------------------- |
| code | int    | 0 表示成功，其余值表示失败。 |
| msg  | String | 具体错误原因。               |

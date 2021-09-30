__功能__

腾讯云直播的推流的回调通知。

**介绍**

可以接收 [V2TXLivePusher](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html) 推流器的一些推流通知，包括推流器连接状态、音视频首帧回调、统计数据、警告和错误信息等。


## SDK 基础回调
### onError

直播推流器错误通知，推流出现错误时，会回调该通知。
```
- (void)onError:(V2TXLiveCode)code message:(NSString *)msg extraInfo:(NSDictionary *)extraInfo
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code      | V2TXLiveCode    | 错误码。   |
| msg       | NSString * | 错误信息。 |
| extraInfo | NSDictionary * | 扩展信息。 |

***

### onWarning

直播推流器警告通知。
```
- (void)onWarning:(V2TXLiveCode)code message:(NSString *)msg extraInfo:(NSDictionary *)extraInfo
```
 
#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code      | V2TXLiveCode    | 警告码。   |
| msg       | NSString * | 警告信息。 |
| extraInfo | NSDictionary * | 扩展信息。 |

***

## 视频相关回调
### onPushStatusUpdate

直播推流器连接状态回调通知。
```
- (void)onPushStatusUpdate:(V2TXLivePushStatus)status
                   message:(NSString *)msg
                 extraInfo:(NSDictionary *)extraInfo
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| status    | V2TXLivePushStatus | 状态码。       |
| msg       | NSString *         | 连接状态信息。 |
| extraInfo | NSDictionary *     | 扩展信息。     |

[](id:V2TXLivePushStatus)

#### V2TXLivePushStatus 枚举值

| 取值 | 含义 |
|---------|---------|
| V2TXLivePushStatusDisconnected | 与服务器断开连接。 |
| V2TXLivePushStatusConnecting | 正在连接服务器。 |
| V2TXLivePushStatusConnectSuccess | 连接服务器成功。 |
| V2TXLivePushStatusReconnecting | 重连服务器中。 |

***

### onSnapshotComplete

截图回调。
```
- (void)onSnapshotComplete:(TXImage *)image
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| image | TXImage * | 已截取的视频画面。 |

***

### onProcessVideoFrame

自定义视频处理回调。
>? 调用 `V2TXLivePusher#enableCustomVideoProcess:(BOOL)enable pixelFormat:(V2TXLivePixelFormat)pixelFormat bufferType:(V2TXLiveBufferType)bufferType` 开启自定义视频处理后，会收到这个回调通知。

```
- (void)onProcessVideoFrame:(V2TXLiveVideoFrame * _Nonnull)srcFrame dstFrame:(V2TXLiveVideoFrame * _Nonnull)dstFrame
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| srcFrame | V2TXLiveVideoFrame * | 用于承载未处理的视频画面。 |
| dstFrame | V2TXLiveVideoFrame * | 用于承载处理过的视频画面。 |

***

### onGLContextDestroyed
自定义视频处理 GL 环境销毁回调。
```
- (void)onGLContextDestroyed
```
***

### onCaptureFirstVideoFrame
首帧视频采集完成的回调通知。
```
- (void)onCaptureFirstVideoFrame
```

***
## 音频相关回调
### onCaptureFirstAudioFrame
首帧音频采集完成的回调通知。
```
- (void)onCaptureFirstAudioFrame
```

***

### onMicrophoneVolumeUpdate
麦克风采集音量值回调。
```
- (void)onMicrophoneVolumeUpdate:(NSInteger)volume
```

***

## 统计回调
### onStatisticsUpdate
直播推流器统计数据回调。
```
- (void)onStatisticsUpdate:(V2TXLivePusherStatistics *)statistics
```

#### 参数

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| statistics | V2TXLivePusherStatistics * | 推流器统计数据。 |

***

## 混流回调
### onSetMixTranscodingConfig
设置云端的混流转码参数的回调。

> ? 调用 `V2TXLivePusher#setMixTranscodingConfig:(V2TXLiveTranscodingConfig *)config` 设置云端混流转码参数后，会收到这个回调通知。

```
- (void)onSetMixTranscodingConfig:(V2TXLiveCode)code message:(NSString *)msg
```
| 参数 | 类型 | 含义 |
|-----|-----|-----|
| code | V2TXLiveCode | 0 表示成功，其余值表示失败。 |
| msg | NSString * | 具体错误原因。 |



__功能__

腾讯云直播的播放器回调通知。


__介绍__

可以接收 [V2TXLivePlayer](https://cloud.tencent.com/document/product/454/56044) 播放器的一些回调通知，包括播放器状态、播放音量回调、音视频首帧回调、统计数据、警告和错误信息等。


## SDK 基础回调
### onError

直播播放器错误通知，播放器出现错误时，会回调该通知。
```
- (void)onError:(id<V2TXLivePlayer>)player
            code:(V2TXLiveCode)code
         message:(NSString *)msg
       extraInfo:(NSDictionary *)extraInfo
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| code | V2TXLiveCode |  错误码。 |
| msg | NSString * |  错误信息。 |
| extraInfo | NSDictionary * |  扩展信息。 |

***

### onWarning

直播播放器警告通知。
```
- (void)onWarning:(id<V2TXLivePlayer>)player
              code:(V2TXLiveCode)code
           message:(NSString *)msg
         extraInfo:(NSDictionary *)extraInfo
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| code | V2TXLiveCode |  警告码。 |
| msg | NSString * |  警告码信息。 |
| extraInfo | NSDictionary * |  扩展信息。 |

***

## 视频相关回调
### onVideoPlayStatusUpdate

直播播放器视频状态变化通知。
```
- (void)onVideoPlayStatusUpdate:(id<V2TXLivePlayer>)player
                          status:(V2TXLivePlayStatus)status
                          reason:(V2TXLiveStatusChangeReason)reason
                       extraInfo:(NSDictionary *)extraInfo
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| status | [V2TXLivePlayStatus](#V2TXLivePlayStatus) | 状态码。 |
| reason | V2TXLiveStatusChangeReason |  状态对应的原因。 |
| extraInfo | NSDictionary * |  扩展信息。 |

[](id:V2TXLivePlayStatus)

#### V2TXLivePlayStatus 枚举类

| 取值                      | 含义                                        |
| ------------------------- | ------------------------------------------- |
| V2TXLivePlayStatusStopped | 播放停止。                                  |
| V2TXLivePlayStatusPlaying | 正在播放。                                  |
| V2TXLivePlayStatusLoading | 正在缓冲（首次加载不会抛出 Loading 事件）。 |

***

### onSnapshotComplete

截图回调。
```
- (void)onSnapshotComplete:(id<V2TXLivePlayer>)player image:(TXImage *)image
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| image | TXImage * | 已截取的视频画面。 |

***

### onRenderVideoFrame

自定义视频渲染回调。
> ? 调用 `[V2TXLivePlayer enableCustomRendering:pixelFormat:bufferType:]` 开启自定义渲染之后，会收到这个回调通知。
```
- (void)onRenderVideoFrame:(id<V2TXLivePlayer>)player
                      frame:(V2TXLiveVideoFrame *)videoFrame
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| videoFrame | V2TXLiveVideoFrame * | 视频帧数据。 |

***


## 音频相关回调
### onAudioPlayStatusUpdate

直播播放器音频状态变化通知。
```
- (void)onAudioPlayStatusUpdate:(id<V2TXLivePlayer>)player
                          status:(V2TXLivePlayStatus)status
                          reason:(V2TXLiveStatusChangeReason)reason
                       extraInfo:(NSDictionary *)extraInfo
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| status | [V2TXLivePlayStatus](#V2TXLivePlayStatus) | 状态码。 |
| reason | V2TXLiveStatusChangeReason |  状态对应的原因。 |
| extraInfo | NSDictionary * |  扩展信息。 |

***

### onPlayoutVolumeUpdate

播放器音量大小回调。
```
- (void)onPlayoutVolumeUpdate:(id<V2TXLivePlayer>)player volume:(NSInteger)volume
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| volume | NSInteger | 音量大小，取值范围：0 - 100。 |

***

## 统计回调

### onStatisticsUpdate

直播播放器统计数据回调。
```
- (void)onStatisticsUpdate:(id<V2TXLivePlayer>)player
                 statistics:(V2TXLivePlayerStatistics *)statistics
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| statistics | V2TXLivePlayerStatistics | 播放器统计数据。 |

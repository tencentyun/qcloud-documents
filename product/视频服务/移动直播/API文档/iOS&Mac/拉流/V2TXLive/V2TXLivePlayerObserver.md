
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

### onConnected

已经成功连接到服务器通知。
```
- (void)onConnected:(id<V2TXLivePlayer>)player 
			extraInfo:(NSDictionary *)extraInfo
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| extraInfo | NSDictionary * |  扩展信息。 |

***

## 视频相关回调
### onVideoPlaying

视频播放事件通知。
```
- (void)onVideoPlaying:(id<V2TXLivePlayer>)player
			   firstPlay:(BOOL)firstPlay 
			   extraInfo:(NSDictionary *)extraInfo
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| firstPlay | BOOL |  第一次播放标志。 |
| extraInfo | NSDictionary * |  扩展信息。 |

***

### onVideoLoading

视频加载事件通知。
```
- (void)onVideoLoading:(id<V2TXLivePlayer>)player
			   extraInfo:(NSDictionary *)extraInfo;
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| extraInfo | NSDictionary * |  扩展信息。 |

***

### onVideoResolutionChanged

直播播放器分辨率变化通知。
```
- (void)onVideoResolutionChanged:(id<V2TXLivePlayer>)player 
								width:(NSInteger)width 
							  height:(NSInteger)height;
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| width | NSInteger | 视频宽 |
| height | NSInteger | 视频高 |

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

### onAudioPlaying

音频播放事件通知。
```
- (void)onAudioPlaying:(id<V2TXLivePlayer>)player 
			   firstPlay:(BOOL)firstPlay 
			   extraInfo:(NSDictionary *)extraInfo;
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
| firstPlay | BOOL |  第一次播放标志。 |
| extraInfo | NSDictionary * |  扩展信息。 |

***

### onAudioLoading

音频加载事件通知。
```
- (void)onAudioLoading:(id<V2TXLivePlayer>)player 
			   extraInfo:(NSDictionary *)extraInfo;
```

__参数__

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| player | V2TXLivePlayer |  回调该通知的播放器对象。 |
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

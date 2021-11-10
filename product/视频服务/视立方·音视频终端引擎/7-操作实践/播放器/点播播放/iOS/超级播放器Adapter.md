腾讯云视立方 iOS 超级播放器 Adapter 为云点播提供给客户希望使用第三方播放器或自研播放器开发的对接云 PaaS 资源的播放器插件，常用于有自定义播放器功能需求的用户。

## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | -  | -  | &#10003;  | - |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## SDK下载
腾讯云视立方 iOS 超级播放器 Adapter SDK 和 Demo 项目，请参见 [TXCPlayerAdapterSDK_iOS](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TXCPlayerAdapter/Release/1.0.0/TXCPlayerAdapterSDK_1.0.0_iOS.zip)。 

## 集成指引

### 环境要求

配置支持 HTTP 请求，需要在项目的 info.plist 文件中添加 `App Transport Security Settings->Allow Arbitrary Loads` 设置为 YES。

###  组件依赖

添加 `GCDWebServer` 组件依赖。   

```objective-c
pod "GCDWebServer", "~> 3.0"
```

GCDWebServer 是一个轻量的 HTTP server，它基于 GCD 并可用于 OS X & iOS，该库还实现了基于 Web 的文件上传以及 WebDAV server 等扩展功能。

### 使用播放器

变量声明，播放器主类为 `TXCPlayerAdapter`，创建后即可播放视频。

fileId 一般是在视频上传后，由服务器返回：

1. 客户端视频发布后，服务器会返回 fileId 到客户端。
2. 服务端视频上传，在 [确认上传](https://cloud.tencent.com/document/product/266/9757) 的通知中包含对应的 fileId。


如果文件已存在腾讯云，则可以进入 [媒资管理](https://console.cloud.tencent.com/vod/media) ，找到对应的文件。点开后在右侧视频详情中，可以看到相关参数。

```objective-c
NSInteger appId; ////appid 在腾讯云点播申请
NSString *fileId;
//psign 即超级播放器签名，签名介绍和生成方式参见链接：https://cloud.tencent.com/document/product/266/42436
NSString *pSign = self.pSignTextView.text;
    
TXCPlayerAdapter *adapter = [TXCPlayerAdapter shareAdapterWithAppId:appId];
```

请求视频信息和播放：

```objective-c
id<ITXCPlayerAssistorProtocol> assistor = [TXCPlayerAdapter createPlayerAssistorWithFileId:fileId pSign:pSign];
[assistor requestVideoInfo:^(id<ITXCPlayerAssistorProtocol> response, NSError *error) {
    if (error) {
        NSLog(@"create player assistor error : %@",error);
        [self.view makeToast:error.description duration:5.0 position:CSToastPositionBottom];
        return;
    }
    [weakSelf avplayerPlay:response]; //播放视频
}];



- (void)avplayerPlay:(id<ITXCPlayerAssistorProtocol>)response
{
    AVPlayerViewController *playerVC = [[AVPlayerViewController alloc] init];
    self.playerVC = playerVC;
    TXCStreamingInfo *info = response.getStreamingInfo;
    AVPlayer *player = [[AVPlayer alloc] initWithURL:[NSURL URLWithString:info.playUrl]];
    playerVC.player = player;
    playerVC.title = response.getVideoBasicInfo.name;
    [self.navigationController pushViewController:playerVC animated:YES];
    
    [player addObserver:self forKeyPath:@"status" options:NSKeyValueObservingOptionNew context:nil];
}
```

使用完后销毁 Player：

```objective-c
[TXCPlayerAdapter destroy];
```



## SDK 接口说明

### 初始化 Adatper
初始化 Adapter，单例。

**接口**

```
+ (instancetype)shareAdapterWithAppId:(NSUInteger)appId;
```

**参数说明**

appId：填写 appid（如果使用了子应用，则填 subappid）。

### 销毁 Adatper
销毁 Adapter，当程序退出后调用。

**接口**

```
+ (void)destroy;
```

### 创建播放器辅助类

通过播放器辅助类可以获取播放 fileId 相关信息以及处理 DRM 加密接口等。

**接口**

```
+ (id<ITXCPlayerAssistorProtocol>)createPlayerAssistorWithFileId:(NSString *)fileId
                                                           pSign:(NSString *)pSign;
```

**参数说明**

| 参数名 | 类型   | 描述               |
| :----- | :----- | :----------------- |
| fileId | String | 要播放的视频 fileId |
| pSign  | String | 超级播放器签名     |

### 请求视频播放信息

本接口会请求腾讯云点播服务器，获取播放视频的流信息等。

**接口**

```objective-c
- (void)requestVideoInfo:(ITXCRequestVideoInfoCallback)completion;
```

**参数说明**

| 参数名         | 类型                         | 描述         |
| :------------- | :--------------------------- | :----------- |
| completion | ITXCRequestVideoInfoCallback | 异步回调函数 |



### 销毁播放器辅助类

销毁辅助类，在退出播放器或者切换了下一个视频播放的时候调用。

**接口**

```
+ (void)destroyPlayerAssistor:(id<ITXCPlayerAssistorProtocol>)assistor;
```



### 获取视频的基本信息

获取视频信息， 必须是在 `id<ITXCPlayerAssistorProtocol>.requestVideoInfo` 回调之后才生效。

**接口**

```
- (TXCVideoBasicInfo *)getVideoBasicInfo;
```

**参数说明**

TXCVideoBasicInfo 参数如下：

| 参数名      | 类型   | 描述                 |
| :---------- | :----- | :------------------- |
| name        | String | 视频名称             |
| size        | Int    | 视频大小，单位：字节 |
| duration    | Float  | 视频时长，单位：秒   |
| description | String | 视频描述             |
| coverUrl    | String | 视频封面             |



### 获取视频流信息

获取视频流信息列表，必须是在 `id<ITXCPlayerAssistorProtocol>.requestVideoInfo` 回调之后才生效。

**接口**

```
- (TXCStreamingInfo *)getStreamingInfo;
```

**参数说明**

TXCStreamingInfo 参数如下：

| 参数名     | 类型   | 描述                                                         |
| :--------- | :----- | :----------------------------------------------------------- |
| playUrl    | String | 播放 URL                                                     |
| subStreams | List   | 自适应码流子流信息，类型为 [TXCSubStreamInfo](#TXCSubStreamInfo) |

TXCSubStreamInfo 参数如下：[](id:TXCSubStreamInfo)

| 参数名         | 类型   | 描述                                 |
| :------------- | :----- | :----------------------------------- |
| type           | String | 子流的类型，目前可能的取值仅有 video |
| width          | Int    | 子流视频的宽，单位：px               |
| height         | Int    | 子流视频的高，单位：px               |
| resolutionName | String | 子流视频在播放器中展示的规格名       |

### 获取关键帧打点信息

获取视频关键帧打点信息，必须是在 `id<ITXCPlayerAssistorProtocol>.requestVideoInfo` 回调之后才生效。

**接口**

```
- (NSArray<TXCKeyFrameDescInfo *> *)getKeyFrameDescInfos;
```

**参数说明**

TXCKeyFrameDescInfo 参数如下：

| 参数名     | 类型   | 描述          |
| :--------- | :----- | :------------ |
| timeOffset | Float  | 1.1           |
| content    | String | "片头开始..." |



### 获取缩略图信息

获取缩略图信息，必须是在 `id<ITXCPlayerAssistorProtocol>.requestVideoInfo` 回调之后才生效。

**接口**

```
- (TXCImageSpriteInfo *)getImageSpriteInfo;
```

**参数说明**

TCXImageSpriteInfo 参数如下：

| 参数名    | 类型   | 描述                               |
| :-------- | :----- | :--------------------------------- |
| imageUrls | List   | 缩略图下载 URL 数组，类型为 String |
| webVttUrl | String | 缩略图 VTT 文件下载 URL            |


## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | &#10003;  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。


## 对接流程
短视频发布是将 MP4 文件上传到腾讯视频云，并获得在线观看 URL， 腾讯视频云支持视频观看的就近调度、秒开播放、动态加速 以及海外接入等要求，从而确保优质的观看体验。
![](//mc.qcloudimg.com/static/img/283c8d7fe0a5a316097ae687a2bf6c5a/image.png)

1. 使用 TXUGCRecord 接口录制一段小视频，录制结束后会生成一个小视频文件（MP4）回调给客户。
2. 您的 App 向您的业务服务器申请上传签名。上传签名是 App 将 MP4 文件上传到腾讯云视频分发平台的“许可证”，为了确保安全性，这些上传签名都要求由您的业务 Server 进行签发，而不能由终端 App 生成。
3. 使用 TXUGCPublish 接口发布视频，发布成功后 SDK 会将观看地址的 URL 回调给您。

## 注意事项

- App 千万不要把计算上传签名的 SecretID 和 SecretKey 写在客户端的代码里，这两个关键信息泄露将导致安全隐患，如恶意攻击者一旦破解 App 获取该信息，就可以免费使用您的流量和存储服务。
- 正确的做法是在您的服务器上用  SecretID 和 SecretKey 生成一次性的上传签名然后将签名交给 App。因为服务器一般很难被攻陷，所以安全性是可以保证的。
- 发布短视频时，请务必保证正确传递 Signature 字段，否则会发布失败。

## 对接攻略
![](https://main.qcloudimg.com/raw/34cf62c826be3fe846b71091a35c0522.png)

[](id:step1)

### 1. 选择视频

可以接着上篇文档中的录制或者编辑，把生成的视频进行上传，或者可以选择手机本地的视频进行上传。

[](id:step2)

### 2. 压缩视频

对选择的视频进行压缩，使用 [TXVideoEditer.generateVideo(int videoCompressed, String videoOutputPath)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVideoEditer__ios.html#a053ca6ab4eb193f29872300636ce9d05) 接口，支持4种分辨率的压缩，后续会增加自定义码率的压缩。

[](id:step3)

### 3. 发布视频
把刚才生成的 MP4 文件发布到腾讯云上，App 需要拿到上传文件用的短期有效上传签名，这部分有独立的文档介绍，详情请参件 [签名派发](https://cloud.tencent.com/document/product/1449/59084)。
TXUGCPublish（位于 TXUGCPublish.h）负责将 MP4 文件发布到腾讯云视频分发平台上，以确保视频观看的就近调度、秒开播放、动态加速以及海外接入等需求。

```ObjectiveC
TXPublishParam * param = [[TXPublishParam alloc] init];

param.signature = _signature;                                // 需要填写第四步中计算的上传签名

// 录制生成的视频文件路径 TXVideoRecordListener 的 onRecordComplete 回调中可以获取
param.videoPath = _videoPath;  
// 录制生成的视频首帧预览图路径。值为通过调用 startRecord 指定的封面路径，或者指定一个路径，然后将TXVideoRecordListener 的 onRecordComplete 回调中获取到的 UIImage 保存到指定路径下，可以置为 nil。
param.coverPath = _coverPath; 

TXUGCPublish *_ugcPublish = [[TXUGCPublish alloc] init];
// 文件发布默认是采用断点续传
_ugcPublish.delegate = self;                                 // 设置 TXVideoPublishListener 回调
[_ugcPublish publishVideo:param];
```

发布的过程和结果是通过 TXVideoPublishListener（位于 TXUGCPublishListener.h 头文件中定义）接口反馈出来的：

- onPublishProgress 用于反馈文件发布的进度，参数 uploadBytes 表示已经上传的字节数，参数 totalBytes 表示需要上传的总字节数。
```ObjectiveC 
@optional
-(void) onPublishProgress:(NSInteger)uploadBytes totalBytes: (NSInteger)totalBytes;
```
- onPublishComplete 用于反馈发布结果，TXPublishResult 的字段 errCode 和 descMsg 分别表示错误码和错误描述信息，videoURL 表示短视频的点播地址，coverURL 表示视频封面的云存储地址，videoId 表示视频文件云存储 ID，您可以通过此 ID 调用点播 [服务端 API 接口](https://cloud.tencent.com/document/product/266/7788)。
``` C 
@optional
-(void) onPublishComplete:(TXPublishResult*)result;
```
- 通过 [编辑错误码表](https://cloud.tencent.com/document/product/1449/57179#error) 和 [录制错误码表](https://cloud.tencent.com/document/product/1449/59155#error) 确认短视频的发布结果。


### 4. 播放视频

[第3步](#step3) 上传成功后，会返回视频的 fileId，播放地址 URL，封面 URL。用 [点播播放器](https://cloud.tencent.com/document/product/584/9372) 可以直接传入 fileId 播放，或者 URL 播放。


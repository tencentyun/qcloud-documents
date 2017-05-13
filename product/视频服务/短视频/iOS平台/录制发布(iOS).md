## 对接流程

- **短视频录制**：
即采集摄像头画面和麦克风声音，经过图像和声音处理后，进行编码压缩最终生成期望清晰度的 MP4 文件。

- **短视频发布**：
即将 MP4 文件上传到腾讯视频云，并获得在线观看 URL， 腾讯视频云支持视频观看的就近调度、秒开播放、动态加速 以及海外接入等要求，从而确保优质的观看体验。

![](//mc.qcloudimg.com/static/img/283c8d7fe0a5a316097ae687a2bf6c5a/image.png)

* 第一步：使用 TXUGCRecord 接口录制一段小视频，录制结束后会生成一个小视频文件（MP4）回调给客户；

* 第二步：您的 APP 向您的业务服务器申请上传签名。上传签名是 APP 将 MP4 文件上传到腾讯云视频分发平台的 “许可证”，为了确保安全性，这些上传签名都要求由您的业务 Server 进行签发，而不能由终端 App 生成。

* 第三步：使用 TXUGCPublish 接口发布视频，发布成功后 SDK 会将观看地址的 URL 回调给您。

## 特别注意

- APP 千万不要把计算上传签名的 SecretID 和 SecretKey 写在客户端的代码里，这两个关键信息泄露将导致安全隐患，比如恶意攻击者一旦破解 APP 获取该信息，就可以免费使用您的流量和存储服务。

- 正确的做法是在您的服务器上用  SecretID 和 SecretKey 生成一次性的上传签名然后将签名交给 APP。因为服务器一般很难被攻陷，所以安全性是可以保证的。

- 发布短视频时，请务必保证正确传递 SecretID 和 Signature 字段，否则会发布失败；

- 对短视频录制接口 startRecord 和 stopRecord 的调用必须保证配对；

- 视频录制时长由客户您的代码来控制，基于性能考虑，为了保证良好的用户体验，建议录制时长最长不超过60秒。


## 接口介绍 
腾讯云 UGC SDK 提供了相关接口用来实现短视频的录制与发布，其详细定义如下：

|  接口文件 |  功能 |
| ------| --------|
| `TXUGCRecord.h` |实现小视频的录制功能|
| `TXUGCPublish.h` | 实现小视频的上传发布 |
| `TXUGCRecordListener.h` | 小视频录制回调及发布回调 |
| `TXUGCRecordTypeDef.h` | 基本参数定义 |

## 对接攻略

![](//mc.qcloudimg.com/static/img/6b21b033259c1b5124648b73e88fb243/image.png)


### 1. 画面预览
TXUGCRecord（位于 TXUGCRecord.h） 负责小视频的录制功能，我们的第一个工作是先把预览功能实现。startCamera 函数用于启动预览。由于启动预览要打开摄像头和麦克风，所以这里可能会有权限申请的提示窗。

```ObjectiveC
UIView *    preViewContainer;                    //准备一个预览摄像头画面的 view
TXUGCSimpleConfig *config = [[TXUGCSimpleConfig alloc] init];
//config.videoQuality = VIDEO_QUALITY_LOW;       // 360p, 10秒钟视频大约0.75M
config.videoQuality   = VIDEO_QUALITY_MEDIUM;    // 540p, 10秒钟视频大约 1.5M （编码参数同微信iOS版小视频）
//config.videoQuality = VIDEO_QUALITY_HIGH;      // 720p, 10秒钟视频大约   3M
config.watermark      = image;                   // 水印图片(要用背景透明的 PNG 图片)
config.watermarkPos   = pos;                     // 水印图片的位置
config.frontCamera    = YES;                     //是否前置摄像头，使用 switchCamera 可以切换
[TXUGCRecord shareInstance].delegate = self;     //self 实现了 TXVideoPublishListener 接口
[[TXUGCRecord shareInstance] startCamera:param preview:preViewContainer];
```

### 2. 画面特效
不管是录制前，还是录制中，您都可以使用 TXUGCRecord 里的特效开关来为视频画面添加一些特效，或者是对摄像头本身进行控制。

```ObjectiveC
//////////////////////////////////////////////////////////////////////////
//                      以下为 1.9.1 版本后均支持的特效
//////////////////////////////////////////////////////////////////////////
//
// 切换前后摄像头 参数 isFront 代表是否前置摄像头 默认前置
[[TXUGCRecord shareInstance] switchCamera YES];

// 设置美颜 和 美白 效果级别
// beautyDepth     : 美颜级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
// whiteningDepth  : 美白级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
[[TXUGCRecord shareInstance] setBeautyDepth: 7 WhiteningDepth: 1];

// 设置颜色滤镜：浪漫、清新、唯美、粉嫩、怀旧...
// image     : 指定滤镜用的颜色查找表。注意：一定要用png格式！！！
// demo用到的滤镜查找表图片位于 RTMPiOSDemo/RTMPiOSDemo/resource／FilterResource.bundle 中
// setSpecialRatio : 用于设置滤镜的效果程度，从0到1，越大滤镜效果越明显，默认取值0.5
[[TXUGCRecord shareInstance] setFilter: filterImage];
[[TXUGCRecord shareInstance] setSpecialRatio: 0.5];

// 是否打开闪光灯
[[TXUGCRecord shareInstance] toggleTorch: YES];

//////////////////////////////////////////////////////////////////////////
//                       以下为仅特权版才支持的特效
// （由于采用优图团队的知识产权，我们无法对外免费提供，需要使用特权版 SDK 才能支持）
//////////////////////////////////////////////////////////////////////////

// 设置大眼级别 0 ~ 9； ----- 推荐让主播自己选择特效程度，不同人的喜好不一样
[[TXUGCRecord shareInstance] setEyeScaleLevel: 0];

// 设置瘦脸级别 0 ~ 9； ----- 推荐让主播自己选择特效程度，不同人的喜好不一样
[[TXUGCRecord shareInstance] setFaceScaleLevel: 0];

// 设置动效贴纸 tmplName - 素材的名字   tmplDir - 素材包的路径
[[TXUGCRecord shareInstance] selectMotionTmpl: tmplName inDir：tmplDir];

// 设置绿幕效果 绿幕素材为宽高比 9:16 （比如 368*640、540*960、720 * 1280）的 MP4 文件
[[TXUGCRecord shareInstance] setGreenScreenFile: file]; 
```


### 3. 文件录制
调用 TXUGCRecord 的 startRecord 函数即可开始录制，调用 stopRecord 函数即可结束录制，startRecord 和 stopRecord 的调用一定要配对。
```ObjectiveC
[[TXUGCRecord shareInstance] startRecord];
[[TXUGCRecord shareInstance] stopRecord];
``` 

录制的过程和结果是通过 TXVideoRecordListener（位于 TXUGCRecordListener.h 头文件中定义）接口反馈出来的：

- onRecordProgress 用于反馈录制的进度，参数millisecond表示录制时长，单位毫秒:
```ObjectiveC
@optional
-(void) onRecordProgress:(NSInteger)milliSecond;
``` 

- onRecordComplete 反馈录制的结果，TXRecordResult 的 retCode 和 descMsg 字段分别表示错误码和错误描述信息，videoPath 表示录制完成的小视频文件路径，coverImage 为自动截取的小视频第一帧画面，便于在视频发布阶段使用。
```ObjectiveC   
@optional
-(void) onRecordComplete:(TXRecordResult*)result;
```     

### 4. 文件预览
使用 [播放SDK](https://www.qcloud.com/document/product/454/7880) 即可预览刚才生成的 MP4 文件，需要在调用 startPlay 时指定播放类型为 [PLAY_TYPE_LOCAL_VIDEO](https://www.qcloud.com/document/product/454/7880#step-3.3A-.E5.90.AF.E5.8A.A8.E6.92.AD.E6.94.BE6) 。

### 5. 获取签名
要把刚才生成的 MP4 文件发布到腾讯云上，App 需要拿到上传文件用的短期有效上传签名，这部分有独立的文档介绍，详情请参考 [Server端集成 - 签名派发](https://www.qcloud.com/document/product/584/9371)。

### 6. 文件发布
TXUGCPublish（位于 TXUGCPublish.h）负责将 MP4 文件发布到腾讯云视频分发平台上，以确保视频观看的就近调度、秒开播放、动态加速 以及海外接入等需求。

```ObjectiveC
TXPublishParam * param = [[TXPublishParam alloc] init];

param.secretId  = @"AKIDeqtlGihED4oqjRP2324seJn1313MLnaa";   // 需要填写您的 SecretId
param.signature = _signature;                                // 需要填写第四步中计算的上传签名

// 录制生成的视频文件路径 TXVideoRecordListener 的 onRecordComplete 回调中可以获取
param.videoPath = _videoPath;  
// 录制生成的视频首帧预览图， TXVideoRecordListener 的 onRecordComplete 回调中可以获取，可以置为 nil
param.coverPath = _coverImage; 

TXUGCPublish *_ugcPublish = [[TXUGCPublish alloc] init];
_ugcPublish.delegate = self;                                 // 设置 TXVideoPublishListener 回调
[_ugcPublish publishVideo:param];
``` 

发布的过程和结果是通过 TXVideoPublishListener（位于 TXUGCRecordListener.h 头文件中定义）接口反馈出来的：

- onPublishProgress 用于反馈文件发布的进度，参数 uploadBytes 表示已经上传的字节数，参数 totalBytes 表示需要上传的总字节数。
```ObjectiveC 
@optional
-(void) onPublishProgress:(NSInteger)uploadBytes totalBytes: (NSInteger)totalBytes;
```

- onPublishComplete 用于反馈发布结果，TXPublishResult 的字段 errCode 和 descMsg 分别表示错误码和错误描述信息，videoURL表示短视频的点播地址，coverURL表示视频封面的云存储地址，videoId表示视频文件云存储Id，您可以通过这个Id调用点播 [服务端API接口](https://www.qcloud.com/document/product/266/1965)。
``` C 
@optional
-(void) onPublishComplete:(TXPublishResult*)result;
```
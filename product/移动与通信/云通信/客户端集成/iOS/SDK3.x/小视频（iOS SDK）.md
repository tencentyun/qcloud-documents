## 1. 集成小视频扩展包

从 [官网](https://www.qcloud.com/product/im.html#sdk) 下载ImSDK开发包，小视频扩展包：IMUGCExt.framework、TXRTMPSDK.framework。各个包的说明如下：

* IMUGCExt.framework		IM小视频UGC消息能力扩展包
  * 发送小视频消息 TIMUGCElem 功能
  * 上传小视频功能
* TXRTMPSDK.framework   小视频录制、编辑能力扩展包
  * 包含小视频录制功能
  * 包含小视频编辑功能
  * 其他能力请参见[移动直播SDK文档](https://www.qcloud.com/document/product/454/7876)
  
在工程中添加`TXRTMPSDK.framework`，同时还要添加以下系统依赖库

> 1. VideoToolbox.framework
> 2. SystemConfiguration.framework
> 3. CoreTelephony.framework
> 4. AVFoundation.framework
> 5. CoreMedia.framework
> 6. CoreGraphics.framework
> 7. libstdc++.tbd
> 8. libz.tbd
> 9. libiconv.tbd
> 10. libresolv.tbd

如果不需要使用小视频功能，可以在集成时移除 IMUGCExt.framework 和 TXRTMPSDK.framework 。

## 2. 录制小视频

录制小视频的步骤包括：画面预览、画面特效、文件录制和文件预览。

### 2.1 画面预览
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

### 2.2 画面特效
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


### 2.3 文件录制
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

### 2.4 文件预览
使用 [播放SDK](https://www.qcloud.com/document/product/454/7880) 即可预览刚才生成的 MP4 文件，需要在调用 startPlay 时指定播放类型为 [PLAY_TYPE_LOCAL_VIDEO](https://www.qcloud.com/document/product/454/7880#step-3.3A-.E5.90.AF.E5.8A.A8.E6.92.AD.E6.94.BE6) 。

## 3. 发送小视频消息

小视频消息由 TIMUGCElem 定义。它是TIMElem的一个子类，也就是说小视频也是消息的一种内容。 发送小视频的过程，就是将TIMUGCElem加入到TIMMessage中，然后随消息一起发送出去。详细如下：

**TIMUGCElem原型：**

```
/**
 *  UGC视频（加载UGC扩展包有效）
 */
@interface TIMUGCVideo : NSObject
/**
 *  视频url，不用设置
 */
@property(nonatomic,strong) NSString * url;
/**
 *  视频文件类型，发送消息时设置
 */
@property(nonatomic,strong) NSString * type;
/**
 *  视频时长，发送消息时设置
 */
@property(nonatomic,assign) int duration;
/**
 *  视频大小，不用设置
 */
@property(nonatomic,assign) int size;

/**
 *  获取视频
 *
 *  @param path 视频保存路径
 *  @param succ 成功回调
 *  @param fail 失败回调，返回错误码和错误描述
 */
- (void)getVideo:(NSString*)path succ:(TIMSucc)succ fail:(TIMFail)fail;

@end

/**
 *  UGC封面（加载UGC扩展包有效）
 */
@interface TIMUGCCover : NSObject
/**
 *  视频url，不用设置
 */
@property(nonatomic,strong) NSString * url;
/**
 *  封面图片类型，发送消息时设置
 */
@property(nonatomic,strong) NSString * type;
/**
 *  图片宽度，发送消息时设置
 */
@property(nonatomic,assign) int width;
/**
 *  图片高度，发送消息时设置
 */
@property(nonatomic,assign) int height;
/**
 *  视频大小，不用设置
 */
@property(nonatomic,assign) int size;

/**
 *  获取图片
 *
 *  @param path 图片保存路径
 *  @param succ 成功回调，返回图片数据
 *  @param fail 失败回调，返回错误码和错误描述
 */
- (void)getImage:(NSString*)path succ:(TIMSucc)succ fail:(TIMFail)fail;

@end

/**
 *  UGC消息（加载UGC扩展包有效）
 */
@interface TIMUGCElem : TIMElem

/**
 *  UGC视频id
 */
@property(nonatomic,strong) NSString * videoId;

/**
 *  UGC视频文件地址，发送消息时设置
 */
@property(nonatomic,strong) NSString * videoPath;

/**
 *  视频信息，发送消息时设置
 */
@property(nonatomic,strong) TIMUGCVideo * video;

/**
 *  UGC封面图片，发送消息时设置
 */
@property(nonatomic,strong) NSString * coverPath;

/**
 *  封面信息，发送消息时设置
 */
@property(nonatomic,strong) TIMUGCCover * cover;

@end
```

**参数说明：**

参数 | 说明
---|---
videoId | 小视频的ID
videoPath | 录制小视频成功后，本地视频文件的路径 
video | 发送时需要设置type、duration属性
coverPath | 录制小视频成功后，本地封面图片文件的路径
cover | 发送时需要设置type、width、height属性

可以通过 TIMUploadProcessListener 监听器得到当前上传进度。

**图片发送示例： **

```
/**
*  获取聊天会话, 以同用户iOS-001的单聊为例，群聊可参见4.1节a部分
*/
TIMConversation * c2c_conversation = [[TIMManager sharedInstance] getConversation:TIM_C2C receiver:@"iOS-001"];

/**
*  构造一条消息
*/
TIMMessage * msg = [[TIMMessage alloc] init];

/**
*  构造小视频内容
*/
TIMUGCElem * ugc_elem = [[TIMImageElem alloc] init];
ugc_elem.videoPath = @"/xxx/videoPath.mp4";
ugc_elem.video = [[TIMUGCVideo alloc] init];
ugc_elem.video.type = @"mp4";
ugc_elem.video.duration = 10;
ugc_elem.coverPath = @"/xxx/coverPath.jpg";
ugc_elem.cover = [[TIMUGCCover alloc] init];
ugc_elem.cover.type = @"jpg";
ugc_elem.cover.width = 88;
ugc_elem.cover.height = 88;

/**
*  将图片内容添加到消息容器中
*/
[msg addElem:image_elem];

/**
*  发送消息
*/
[conversation sendMessage:msg succ:^(){  //成功
       NSLog(@"SendMsg Succ");
}fail:^(int code, NSString * err) {  //失败
       NSLog(@"SendMsg Failed:%d->%@", code, err);
}];
```

示例中发送了一个小视频消息。


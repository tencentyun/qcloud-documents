## 集成小视频扩展包

从 [官网](https://cloud.tencent.com/product/im.html#sdk) 下载 IM SDK 开发包，小视频扩展包：`IMUGCExt.framework`、`TXRTMPSDK.framework`。

> **注意：**
>- 如果不需要使用小视频功能，可以在集成时移除 `IMUGCExt.framework` 和 `TXRTMPSDK.framework` 。
>- Demo 中美颜和 P 图效果需要额外添加 `beauty_libs` 中的 framework 和资源。

**功能介绍**

| 对象 | 介绍 | 功能 |
| --- | --- | --- |
| IMUGCExt.framework | 云通信 IM 小视频 UGC 消息能力扩展包 | 发送小视频消息 TIMUGCElem 功能，上传小视频功能 |
| TXRTMPSDK.framework | 小视频录制、编辑能力扩展包 | 包含小视频录制功能、小视频编辑功能，其他能力请参见 [移动直播 SDK 文档](https://cloud.tencent.com/document/product/454/7876) |
  
在工程中添加 `TXRTMPSDK.framework`，同时还要添加以下系统依赖库。

```
VideoToolbox.framework
SystemConfiguration.framework
CoreTelephony.framework
AVFoundation.framework
CoreMedia.framework
CoreGraphics.framework
libstdc++.tbd
libz.tbd
libiconv.tbd
libresolv.tbd
```

云通信 IM 的短视频默认仅存储7天，如需长期存储，需要在控制台开通短视频点播服务。**短视频点播服务开通方式如下：**

![](https://mc.qcloudimg.com/static/img/7830ff8639567e4a9d60923349bf5a58/image.png)

## 录制小视频

录制小视频的步骤包括：画面预览、画面特效、文件录制和文件预览。

### 画面预览

`TXUGCRecord`（位于 `TXUGCRecord.h`） 负责小视频的录制功能，我们的第一个工作是先把预览功能实现。`startCamera` 函数用于启动预览。由于启动预览要打开摄像头和麦克风，所以这里可能会有权限申请的提示窗。

```ObjectiveC
UIView *    preViewContainer;                    //准备一个预览摄像头画面的 view
TXUGCSimpleConfig *config = [[TXUGCSimpleConfig alloc] init];
//config.videoQuality = VIDEO_QUALITY_LOW;       // 360p, 10 秒钟视频大约 0.75M
config.videoQuality   = VIDEO_QUALITY_MEDIUM;    // 540p, 10 秒钟视频大约 1.5M （编码参数同微信 iOS 版小视频）
//config.videoQuality = VIDEO_QUALITY_HIGH;      // 720p, 10 秒钟视频大约 3M
config.watermark      = image;                   // 水印图片(要用背景透明的 PNG 图片)
config.watermarkPos   = pos;                     // 水印图片的位置
config.frontCamera    = YES;                     //是否前置摄像头，使用 switchCamera 可以切换
[TXUGCRecord shareInstance].delegate = self;     //self 实现了 TXVideoPublishListener 接口
[[TXUGCRecord shareInstance] startCamera:param preview:preViewContainer];
```

### 画面特效

不管是录制前，还是录制中，您都可以使用 `TXUGCRecord` 里的特效开关来为视频画面添加一些特效，或者是对摄像头本身进行控制。

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
// image     : 指定滤镜用的颜色查找表。注意：一定要用 png 格式！！！
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

### 文件录制

调用 `TXUGCRecord` 的 `startRecord` 函数即可开始录制，调用 `stopRecord` 函数即可结束录制，`startRecord` 和 `stopRecord` 的调用一定要配对。

```ObjectiveC
[[TXUGCRecord shareInstance] startRecord];
[[TXUGCRecord shareInstance] stopRecord];
``` 

录制的过程和结果是通过 `TXVideoRecordListener`（位于 `TXUGCRecordListener.h` 头文件中定义）接口反馈出来的。

- `onRecordProgress` 用于反馈录制的进度，参数 `millisecond` 表示录制时长，单位毫秒。
- `onRecordComplete` 反馈录制的结果，`TXRecordResult` 的 `retCode` 和`descMsg` 字段分别表示错误码和错误描述信息，`videoPath` 表示录制完成的小视频文件路径，`coverImage` 为自动截取的小视频第一帧画面，便于在视频发布阶段使用。

```ObjectiveC
@optional
-(void) onRecordProgress:(NSInteger)milliSecond;

@optional
-(void) onRecordComplete:(TXRecordResult*)result;
```     

### 文件预览

使用 [播放 SDK](https://cloud.tencent.com/document/product/454/7880) 即可预览刚才生成的 MP4 文件，需要在调用 `startPlay` 时指定播放类型为 [PLAY_TYPE_LOCAL_VIDEO](https://cloud.tencent.com/document/product/454/7880#step-3.3A-.E5.90.AF.E5.8A.A8.E6.92.AD.E6.94.BE6) 。

## 小视频消息

### 发送小视频消息

小视频消息由 `TIMUGCElem` 定义。它是 `TIMElem` 的一个子类，也就是说小视频也是消息的一种内容。 发送小视频的过程，就是将 `TIMUGCElem` 加入到 `TIMMessage` 中，然后随消息一起发送出去。可以通过 `TIMUploadProcessListener` 监听器得到当前上传进度。

**`TIMUGCElem`原型：**

```
/**
 *  UGC 视频（加载 UGC 扩展包有效）
 */
@interface TIMUGCVideo : NSObject
/**
 *  视频文件类型，发送消息时设置
 */
@property(nonatomic,strong) NSString * type;
/**
 *  视频时长，发送消息时设置
 */
@property(nonatomic,assign) int duration;
@end
/**
 *  UGC 封面（加载 UGC 扩展包有效）
 */
@interface TIMUGCCover : NSObject
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
@end
/**
 *  UGC 消息（加载 UGC 扩展包有效）
 */
@interface TIMUGCElem : TIMElem
/**
 *  UGC 视频 ID
 */
@property(nonatomic,strong) NSString * videoId;
/**
 *  UGC 视频文件地址，发送消息时设置
 */
@property(nonatomic,strong) NSString * videoPath;
/**
 *  视频信息，发送消息时设置
 */
@property(nonatomic,strong) TIMUGCVideo * video;
/**
 *  UGC 封面图片，发送消息时设置
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
videoId | 小视频的 ID
videoPath | 录制小视频成功后，本地视频文件的路径 
video | 发送时需要设置 type、duration 属性
coverPath | 录制小视频成功后，本地封面图片文件的路径
cover | 发送时需要设置 type、width、height 属性

**小视频消息发送示例：**

```
/**
*  获取聊天会话, 以同用户 iOS-001 的单聊为例
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

### 接收小视频消息

接收方收到消息后，可通过 `getElem` 从 `TIMMessage` 中获取所有的 `Elem` 节点，其中类型为 `TIMUGCElem` 的是小视频消息节点。然后通过 `video` 和 `cover` 对象获取该小视频的视频和封面图片文件。

**`TIMUGCElem`原型：**

```
/**
 *  UGC 视频（加载 UGC 扩展包有效）
 */
@interface TIMUGCVideo : NSObject
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
 *  UGC 封面（加载UGC扩展包有效）
 */
@interface TIMUGCCover : NSObject
/**
 *  获取图片
 *
 *  @param path 图片保存路径
 *  @param succ 成功回调，返回图片数据
 *  @param fail 失败回调，返回错误码和错误描述
 */
- (void)getImage:(NSString*)path succ:(TIMSucc)succ fail:(TIMFail)fail;
@end
```

以下示例从会话中取出10条消息，获取小视频消息并下载相应数据。**示例：**

```
//以收到新消息回调为例，介绍下图片消息的解析过程
//接收到的图片保存的路径
NSString * video_path = @"/xxx/videoPath.pm4";
NSString * cover_path = @"/xxx/coverPath.jpg";
[conversation getMessage:10 last:nil succ:^(NSArray * msgList) {  //获取消息成功
	//遍历所有的消息
	for (TIMMessage * msg in msgList) {
		//遍历一条消息的所有元素
		for (TIMUGCElem * elem in TIMUGCElem) {
		   //图片元素
			if ([elem isKindOfClass:[TIMUGCElem class]]) {
				TIMUGCElem * ugc_elem = (TIMImageElem * )elem;
				[ugc_elem.video getVideo:vieo_path succ^{
					NSLog(@"SUCC: video store to %@", video_path);
				} fail:^(int code, NSString *err)｛
					NSLog(@"ERR: code=%d, err=%@", code, err);
				｝];
				[ugc_elem.cover getImage:cover_path succ^{
					NSLog(@"SUCC: cover store to %@", cover_path);
				} fail:^:(int code, NSString *err){
					NSLog(@"ERR: code=%d, err=%@", code, err);
				}];
			}
		}
	}
} fail:^(int code, NSString * err) {  //获取消息失败
	NSLog(@"Get Message Failed:%d->%@", code, err);
}];
```

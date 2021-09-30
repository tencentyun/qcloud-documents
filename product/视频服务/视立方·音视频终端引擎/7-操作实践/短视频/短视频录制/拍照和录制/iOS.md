视频录制包括视频变速录制、美颜、滤镜、声音特效、背景音乐设置等功能。 

## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | &#10003;  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。


## 使用类介绍
腾讯云视立方短视频 UGSV SDK 提供了相关接口用来实现短视频的录制，其详细定义如下：

| 接口文件                | 功能                                       |
| ----------------------- | ------------------------------------------ |
| TXUGCRecord.h         | 小视频录制功能                             |
| TXUGCRecordListener.h | 小视频录制回调                             |
| TXUGCRecordEventDef.h | 小视频录制事件回调                         |
| TXUGCRecordTypeDef.h  | 基本参数定义                               |
| TXUGCPartsManager.h   | 视频片段管理类，用于视频的多段录制，回删等 |

## 使用说明

### 使用流程

视频录制的基本使用流程如下：
1. 配置录制参数。
2. 启动画面预览。
3. 设置录制效果。
4. 完成录制。

### 示例代码
<dx-codeblock>
::: ios objcect-c
@interface VideoRecordViewController <TXUGCRecordListener> {
   UIView *_videoRecordView;
}

@implementation VideoRecordViewController
- (void)viewDidLoad {
   [super viewDidLoad];

   // 创建一个视图用于显示相机预览图片
   _videoRecordView = [[UIView alloc] initWithFrame:self.view.bounds];
   [self.view addSubview:_videoRecordView];

   // 1. 配置录制参数
   TXUGCSimpleConfig * param = [[TXUGCSimpleConfig alloc] init];
   param.videoQuality = VIDEO_QUALITY_MEDIUM;

   // 2. 启动预览, 设置参数与在哪个View上进行预览
   [[TXUGCRecord shareInstance] startCameraSimple:param preview:_videoRecordView];

   // 3. 设置录制效果，这里以添加水印为例
   UIImage *watermarke = [UIImage imageNamed:@"watermarke"];
   [[TXUGCRecord shareInstance] setWaterMark:watermarke normalizationFrame:CGRectMake(0.01, 0.01, 0.1, 0)];
   }

// 4. 开始录制
- （IBAction)onStartRecord:(id)sender {
   [TXUGCRecord shareInstance].recordDelegate = self;
   int result = [[TXUGCRecord shareInstance] startRecord];
   if(0 != result) {
        if(-3 == result) [self alert:@"启动录制失败" msg:@"请检查摄像头权限是否打开"];
        else if(-4 == result) [self alert:@"启动录制失败" msg:@"请检查麦克风权限是否打开"];
        else if(-5 == result) [self alert:@"启动录制失败" msg:@"licence 验证失败"];
   } else {
      // 启动成功
   }
   }

// 结束录制
- （IBAction)onStopRecord:(id)sender {
   [[TXUGCRecord shareInstance] stopRecord];
   }

// 录制完成回调
-(void) onRecordComplete:(TXUGCRecordResult*)result
{
   if (result.retCode == UGC_RECORD_RESULT_OK) {
      // 录制成功， 视频文件在result.videoPath中
   } else {
      // 错误处理，错误码定义请参见 TXUGCRecordTypeDef.h 中 TXUGCRecordResultCode 的定义
   }
}

-(void)alert:(NSString *)title msg:(NSString *)msg
{
    UIAlertView *alert = [[UIAlertView alloc] initWithTitle:title message:msg delegate:self cancelButtonTitle:@"确定" otherButtonTitles:nil, nil];
    [alert show];
}
@end
:::
</dx-codeblock>

## 画面预览
TXUGCRecord（位于 TXUGCRecord.h）负责小视频的录制功能，我们的第一个工作是先把预览功能实现。startCameraSimplePreview 函数用于启动预览。由于启动预览要打开摄像头和麦克风，所以这里可能会有权限申请的提示窗。
### 1. 启动预览
<dx-codeblock>
::: ios objcect-c
TXUGCRecord *record = [TXUGCRecord sharedInstance];
record.recordDelegate = self; //设置录制回调, 回调方法见 TXUGCRecordListener

//配置相机及启动预览
TXUGCSimpleConfig * param = [[TXUGCSimpleConfig alloc] init];
//param.videoQuality = TXRecordCommon.VIDEO_QUALITY_LOW;		// 360p
//param.videoQuality = TXRecordCommon.VIDEO_QUALITY_MEDIUM;		// 540p
param.videoQuality = TXRecordCommon.VIDEO_QUALITY_HIGH;		  // 720p
param.frontCamera = YES;    //使用前置摄像头
param.minDuration = 5;	//视频录制的最小时长5s
param.maxDuration = 60;	//视频录制的最大时长60s
param.enableBFrame = YES; // 开启B帧，相同码率下能获得更好的画面质量

//在self.previewView中显示照相机预览画面
[recorder startCameraSimple:param preview:self.previewView];

//结束画面预览
[[TXUGCRecord shareInstance] stopCameraPreview];
:::
</dx-codeblock>

### 2. 调整预览参数

如果在相机启动后，可以通过以下方法修改：

<dx-codeblock>
::: ios objcect-c
// 切换视频录制分辨率到540p
[recorder setVideoResolution: VIDEO_RESOLUTION_540_960];

// 切换视频录制码率到6500Kbps
[recorder setVideoBitrate: 6500];

// 设置焦距为3, 当为1的时候为最远视角（正常镜头），当为5的时候为最近视角（放大镜头）
[recorder setZoom: 3];

// 切换到后置摄像头 YES 切换到前置摄像头 NO 切换到后置摄像头
[recorder switchCamera: NO];

// 打开闪光灯 YES为打开， NO为关闭.
[recorder toggleTorch: YES];

// 设置自定义图像处理回调
recorder.videoProcessDelegate = delegate;
:::
</dx-codeblock>

## 录制过程控制
### 录制的开始、暂停与恢复
<dx-codeblock>
::: ios objcect-c
// 开始录制
[recorder startRecord];

// 开始录制，可以指定输出视频文件地址和封面地址
[recorder startRecord:videoFilePath coverPath:coverPath];

// 开始录制,可以指定输出视频文件地址、视频分片存储地址和封面地址
[recorder startRecord:videoFilePath videoPartsFolder:videoPartFolder coverPath:coverPath];

// 暂停录制
[recorder pauseRecord];

// 继续录制
[recorder resumeRecord];

// 结束录制
[recorder stopRecord];
:::
</dx-codeblock>

录制的过程和结果是通过 TXUGCRecordListener（位于 TXUGCRecordListener.h 中定义）协议进行回调：
- onRecordProgress 用于反馈录制的进度，参数 millisecond 表示录制时长，单位毫秒。
```
  @optional
   (void)onRecordProgress:(NSInteger)milliSecond;
```
- onRecordComplete 反馈录制的结果，TXRecordResult 的 retCode 和 descMsg 字段分别表示错误码和错误描述信息，videoPath 表示录制完成的小视频文件路径，coverImage 为自动截取的小视频第一帧画面，便于在视频发布阶段使用。
```
  @optional
   (void)onRecordComplete:(TXUGCRecordResult*)result;
```
- onRecordEvent 录制事件回调预留的接口，暂未使用。
```
  @optional
   (void)onRecordEvent:(NSDictionary*)evt;
```

## 录制属性设置
### 画面设置
```objc
// 设置横竖屏录制
[recorder setHomeOrientation:VIDOE_HOME_ORIENTATION_RIGHT];

// 设置视频预览方向
// rotation : 取值为 0 , 90, 180, 270（其他值无效） 表示视频预览向右旋转的角度
// 注意：需要在startRecord 之前设置，录制过程中设置无效
[recorder setRenderRotation:rotation];

// 设置录制的宽高比
// VIDEO_ASPECT_RATIO_9_16 宽高比为9:16
// VIDEO_ASPECT_RATIO_3_4  宽高比为3:4
// VIDEO_ASPECT_RATIO_1_1  宽高比为1:1
// 注意：需要在startRecord 之前设置，录制过程中设置无效
[recorder setAspectRatio:VIDEO_ASPECT_RATIO_9_16];
```
### 速度设置
```
// 设置视频录制速率
//    VIDEO_RECORD_SPEED_SLOWEST,       极慢速
//   VIDEO_RECORD_SPEED_SLOW,           慢速
//    VIDEO_RECORD_SPEED_NOMAL,         正常速
//    VIDEO_RECORD_SPEED_FAST,          快速
//    VIDEO_RECORD_SPEED_FASTEST,       极快速
[recorder setRecordSpeed:VIDEO_RECORD_SPEED_NOMAL];
```

### 声音设置
<dx-codeblock>
::: ios objcect-c
// 设置麦克风的音量大小，播放背景音混音时使用，用来控制麦克风音量大小
// 音量大小,1为正常音量,建议值为0-2,如果需要调大音量可以设置更大的值.
[recorder setMicVolume:volume];

// 设置录制是否静音 参数 isMute 代表是否静音，默认不静音
[recorder setMute:isMute];
:::
</dx-codeblock>

## 拍照

```objc
// 截图/拍照，startCameraSimplePreview 或者 startCameraCustomPreview 之后调用有效
[recorder snapshot:^(UIImage *image) {
    // image 为截图结果
}];
```

## 设置效果

在视频录制的过程中，您可以给录制视频的画面设置各种特效。
### 水印效果
```objc
// 设置全局水印
// normalizationFrame : 水印相对于视频图像的归一化值，sdk 内部会根据水印宽高比自动计算 height
// 例如视频图像大小为（540，960）  frame 设置为（0.1，0.1，0.1, 0）
// 水印的实际像素坐标为
// (540*0.1, 960*0.1, 540*0.1, 540*0.1*waterMarkImage.size.height / waterMarkImage.size.width）
[recorder setWaterMark:waterMarkImage normalizationFrame:frame)
```

### 滤镜效果

<dx-codeblock>
::: ios objcect-c
//设置风格滤镜
// 设置颜色滤镜：浪漫、清新、唯美、粉嫩、怀旧...
// filterImage : 指定滤镜用的颜色查找表。注意：一定要用 png 格式
// demo 用到的滤镜查找表图片位于 FilterResource.bundle 中
[recorder setFilter:filterImage];

 // 用于设置滤镜的效果程度，从0到1，越大滤镜效果越明显，默认取值0.5
[recorder setSpecialRatio:ratio];

// 设置组合滤镜特效
// mLeftBitmap      左侧滤镜
// leftIntensity   左侧滤镜强度
// mRightBitmap     右侧滤镜
// rightIntensity  右侧滤镜强度
// leftRadio       左侧图片占的比例大小
// 可以此接口实现滑动切换滤镜的效果，详见 demo。
[recorder setFilter:leftFilterImgage leftIntensity:leftIntensity rightFilter:rightFilterImgage rightIntensity:rightIntensity leftRatio:leftRatio];
:::
</dx-codeblock>

### 美颜效果
```
// 设置美颜风格、级别、美白及红润的级别
// beautyStyle的定义如下:
// typedef NS_ENUM(NSInteger, TXVideoBeautyStyle) {
//    VIDOE_BEAUTY_STYLE_SMOOTH     = 0,    // 光滑
//    VIDOE_BEAUTY_STYLE_NATURE     = 1,    // 自然
//    VIDOE_BEAUTY_STYLE_PITU       = 2,    // pitu 美颜, 需要购买企业版
// };
// 级别的范围为0-9 0为关闭， 1-9值越大，效果越明显
[recorder setBeautyStyle:beautyStyle beautyLevel:beautyLevel whitenessLevel:whitenessLevel ruddinessLevel:ruddinessLevel];
```

## 高级功能
- [多段录制](https://cloud.tencent.com/document/product/1449/57028)
- [录制草稿箱](https://cloud.tencent.com/document/product/1449/57030)
- [添加背景音乐](https://cloud.tencent.com/document/product/1449/57036)
- [变声和混响](https://cloud.tencent.com/document/product/1449/57038)
- [定制视频数据](https://cloud.tencent.com/document/product/1449/57060)


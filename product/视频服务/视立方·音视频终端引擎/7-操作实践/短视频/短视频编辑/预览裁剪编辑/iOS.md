视频编辑包括视频裁剪、时间特效（慢动作、倒放、重复）、滤镜特效（动感光波、暗黑幻影、灵魂出窍、画面分裂）、滤镜风格（唯美、粉嫩、蓝调等）、音乐混音、动态贴纸、静态贴纸、气泡字幕等功能。

## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | &#10003;  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 相关类介绍 

| 类名           | 功能  |
| ------------- | --------- |
| TXVideoInfoReader.h| 媒体信息获取 |
| TXVideoEditer.h | 视频编辑 |

## 使用说明
视频编辑的基本使用流程如下：

1. 设置视频路径。
2. 添加效果。
3. 生成视频到指定文件。
4. 监听生成事件。

## 代码示例

<dx-codeblock>
::: ios objective-c
// 这以使用了 Demo 中的 Common/UGC/VideoPreview 来做预览的视图
#import "VideoPreview.h"

@implementation EditViewController
{
   TXVideoEditer *editor;
   VideoPreview *_videoPreview;
}

- (void)viewDidLoad {
   [super viewDidLoad];
   _videoPreview = [[VideoPreview alloc] initWithFrame:self.view.bounds];
   [self.view addSubview:_videoPreview];
   // 编辑预览参数
   TXPreviewParam *param = [[TXPreviewParam alloc] init];
   param.videoView = _videoPreview.renderView;
   param.renderMode = PREVIEW_RENDER_MODE_FILL_EDGE;

   // 1. 初始化编辑器, 如无需预览，可以传 nil 或直接调用 init 方法
   TXVideoEditer *editor = [[TXVideoEditer alloc] initWithPreview:param];

   // 设置源视频路径
   NSString *path = [[NSBundle mainBundle] pathForResource:@"demo" ofType:@"mp4"]
   [editor setVideoPath: path];

   // 配置代理
   editor.generateDelegate = self;      // 设置生成事件的回调委托对象，可以获取生成进度与结果

   // 2. 对视频进行处理，这里以添加水印为例
   [editor setWaterMark:[UIImage imageNamed:@"water_mark"]
         normalizationFrame:CGRectMake(0,0,0.1,0)];
   }

// 3. 生成视频, 以响应用户点击为例
- (IBAction)onGenerate:(id)sender {
   NSString *output = [NSTemporaryDirectory() stringByAppendingPathComponent:@"temp.mp4"];
   [editor generateVideo:VIDEO_COMPRESSED_720P videoOutputPath:output];                                                              
   }

// 4. 获取生成进度
-(void) onGenerateProgress:(float)progress
{
}

// 获取生成结果
-(void) onGenerateComplete:(TXGenerateResult *)result
{
   if (result.retCode == 0) {
      // 生成成功
   } else {
      // 生成失败，原因可以查看 result.descMsg
   }
}
@end
:::
</dx-codeblock>

## 视频信息获取
TXVideoInfoReader 的 getVideoInfo 方法可以获取指定视频文件的一些基本信息, 相关接口如下：
<dx-codeblock>
::: ios objective-c
// 获取视频文件的信息
+ (TXVideoInfo *)getVideoInfo:(NSString *)videoPath;

/** 获取视频文件信息
 * @param videoAsset 视频文件属性
 * @return 视频信息
 */
+ (TXVideoInfo *)getVideoInfoWithAsset:(AVAsset *)videoAsset;
:::
</dx-codeblock>
返回的 TXVideoInfo 定义如下：
<dx-codeblock>
::: ios objective-c
/// 视频信息
@interface TXVideoInfo : NSObject
/// 视频首帧图片
@property (nonatomic, strong) UIImage*              coverImage;
/// 视频时长(s)
@property (nonatomic, assign) CGFloat               duration;
/// 视频大小(byte)
@property (nonatomic, assign) unsigned long long    fileSize;
/// 视频fps
@property (nonatomic, assign) float                 fps;      
/// 视频码率 (kbps)
@property (nonatomic, assign) int                   bitrate;
/// 音频采样率
@property (nonatomic, assign) int                   audioSampleRate;
/// 视频宽度
@property (nonatomic, assign) int                   width;
/// 视频高度
@property (nonatomic, assign) int                   height;
/// 视频旋转角度
@property (nonatomic, assign) int                   angle;
@end
:::
</dx-codeblock>

## 缩略图获取
缩略图的接口主要用于生成视频编辑界面的预览缩略图，或获取视频封面等。
### 按个数平分时间获取缩略图

TXVideoInfoReader 的 getSampleImages 可以获取按指定数量，时间间隔相同的预览图：
```objective-c
/** 获取视频的采样图列表
 * @param count        获取的采样图数量（均匀采样）
 * @param maxSize      缩略图的最大大小，生成的缩略图大小不会超出这个宽高
 * @param videoAsset   视频文件属性
 * @param sampleProcess 采样进度
 */
+ (void)getSampleImages:(int)count
                maxSize:(CGSize)maxSize
             videoAsset:(AVAsset *)videoAsset
               progress:(sampleProcess)sampleProcess;
```
开发包中的 VideoRangeSlider 即使用了 getSampleImages 获取了10张缩略图来构建一个由视频预览图组成的进度条。

### 根据时间列表获取缩略图
```objective-c
 /**
 * 根据时间列表获取缩略图列表
 * @param asset   视频文件对象
 * @param times   获取的时间列表
 * @param maxSize 缩略图大小
 */
+ (UIImage *)getSampleImagesFromAsset:(AVAsset *)asset
                                times:(NSArray<NSNumber*> *)times
                              maxSize:(CGSize)maxSize
                             progress:(sampleProcess)sampleProcess;
```

## 编辑预览
视频编辑提供了**定点预览**（将视频画面定格在某一时间点）与**区间预览**（循环播放某一时间段 A<=>B 内的视频片段）两种效果预览方式，使用时需要给 SDK 绑定一个 UIView 用于显示视频画面。

### 1. 绑定 UIView
TXVideoEditer 的 initWithPreview 函数用于绑定一个 UIView 给 SDK 来渲染视频画面，通过控制 TXPreviewParam 的 renderMode 来设置**自适应**与**填充**两种模式。

```   
   PREVIEW_RENDER_MODE_FILL_SCREEN - 填充模式，尽可能充满屏幕不留黑边，所以可能会裁剪掉一部分画面。     
   PREVIEW_RENDER_MODE_FILL_EDGE   - 适应模式，尽可能保持画面完整，但当宽高比不合适时会有黑边出现。   
```

### 2. 定点预览
TXVideoEditer 的 previewAtTime 函数用于定格显示某一个时间点的视频画面。
```
/** 渲染某一时刻的视频画面
 *  @param time      预览帧时间(s)
 */
- (void)previewAtTime:(CGFloat)time;
```

### 3. 区间预览
TXVideoEditer 的 startPlayFromTime 函数用于循环播放某一时间段 A<=>B 内的视频片段。
```
/** 播放某一时间段的视频
 * @param startTime     播放起始时间(s)
 * @param endTime       播放结束时间(s)
 */
- (void)startPlayFromTime:(CGFloat)startTime
                   toTime:(CGFloat)endTime;
```
### 4. 预览的暂停与恢复

```
/// 暂停播放
- (void)pausePlay;

/// 继续播放
- (void)resumePlay;

/// 停止播放
- (void)stopPlay;
```

### 5. 美颜滤镜
您可以给视频添加滤镜效果，例如美白、浪漫、清新等滤镜，Demo 提供了多种滤镜选择，对应的滤镜资源在 `Common/Resource/Filter/FilterResource.bundle` 中，同时也可以设置自定义的滤镜。  
#### 设置滤镜的方法：

```
- (void) setFilter:(UIImage *)image;
```
其中 image 为滤镜映射图，image 设置为 nil，会清除滤镜效果。

#### Demo 示例：
```
TXVideoEditer     *_ugcEdit;
NSString * path = [[NSBundle mainBundle] pathForResource:@"FilterResource" ofType:@"bundle"];
path = [path stringByAppendingPathComponent:@"langman.png"];
UIImage* image = [UIImage imageWithContentsOfFile:path];
[_ugcEdit setFilter:image];
```
### 6. 设置水印
<dx-tabs>
::: 设置全局水印
您可以为视频设置水印图片，并且可以指定图片的位置。
**设置水印的方法：** 
```
- (void) setWaterMark:(UIImage *)waterMark  normalizationFrame:(CGRect)normalizationFrame;
```

其中 waterMark 表示水印图片，normalizationFrame 是相对于视频图像的归一化 frame，frame 的 x、y、width、height 的取值范围都为0 - 1。

**Demo 示例：**
```
UIImage *image = [UIImage imageNamed:@"watermark"];  
[_ugcEdit setWaterMark:image normalizationFrame:CGRectMake(0, 0, 0.3 , 0.3 * image.size.height / image.size.width)];//水印大小占视频宽度的30%，高度根据宽度自适应
```
:::
::: 设置片尾水印
您可以为视频设置片尾水印，并且可以指定片尾水印的位置。

**设置片尾水印的方法：** 
```
- (void) setTailWaterMark:(UIImage *)tailWaterMark normalizationFrame:(CGRect)normalizationFrame 
                          duration:(CGFloat)duration;
```

其中 tailWaterMark 表示片尾水印图片，normalizationFrame 是相对于视频图像的归一化 frame，frame 的 x、y、width、height 的取值范围都为0 - 1，duration 为水印的持续时长。

**Demo 示例：**
设置水印在片尾中间，持续时间1s。

```
UIImage *tailWaterimage = [UIImage imageNamed:@"tcloud_logo"];
float w = 0.15;
float x = (1.0 - w) / 2.0;
float width = w * videoMsg.width;
float height = width * tailWaterimage.size.height / tailWaterimage.size.width;
float y = (videoMsg.height - height) / 2 / videoMsg.height;
[_ugcEdit setTailWaterMark:tailWaterimage normalizationFrame:CGRectMake(x,y,w,0) duration:1];   

```
:::
</dx-tabs>

## 压缩裁剪
### 视频码率设置
```
/**
 * 设置视频码率
 * @param bitrate  视频码率 单位:kbps
 *                 如果设置了码率，SDK 生成视频会优先使用这个码率，注意码率不要太大或则太小，码率太小视频会模糊不清，码率太大，生成视频体积会很大
 *                 这里建议设置范围为：600-12000，如果没有调用这个接口，SDK内部会根据压缩质量自动计算码率
 */
- (void) setVideoBitrate:(int)bitrate;
```

### 视频裁剪
视频编辑类操作都符合同一个操作原则：即先设定操作指定，最后用 generateVideo 将所有指令顺序执行，这种方式可以避免多次重复压缩视频引入的不必要的质量损失。

```objective-c
TXVideoEditer* _ugcEdit = [[TXVideoEditer alloc] initWithPreview:param];
// 设置裁剪的起始时间和结束时间
[_ugcEdit setCutFromTime:_videoRangeSlider.leftPos toTime:_videoRangeSlider.rightPos];
// ...
// 生成最终的视频文件
_ugcEdit.generateDelegate = self;
[_ugcEdit generateVideo:VIDEO_COMPRESSED_540P videoOutputPath:_videoOutputPath];
```
输出时指定文件压缩质量和输出路径，输出的进度和结果会通过 `generateDelegate` 以回调的形式通知用户。

## 高级功能

- [类抖音特效](https://cloud.tencent.com/document/product/1449/57050)
- [设置背景音乐](https://cloud.tencent.com/document/product/1449/57036)
- [贴纸字幕](https://cloud.tencent.com/document/product/1449/57052)
- [图片转场特效](https://cloud.tencent.com/document/product/1449/57056)








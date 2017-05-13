
## 接口介绍

| 类名                   | 功能       |
| -------------------- | -------- |
| TXUGCVideoInfoReader | 视频文件信息读取 |
| TXUGCEditer          | 视频编辑     |
| TXUGCJoiner          | 视频合并     |
| TXOperationParam     | 操作类型对象   |

## 接入步骤

### 1. 信息读取
#### 1.1 读取视频基本信息
TXUGCVideoInfoReader提供了方法，一次性读出所有相关信息，这些信息将在后续的视频编辑过程中使用。

```objective-c
/*
 * 视频信息
 */
@interface TXVideoInfo : NSObject
@property (nonatomic, strong) UIImage*              coverImage;     //视频首帧图片
@property (nonatomic, assign) CGFloat               duration;       //视频时长(s)
@property (nonatomic, assign) unsigned long long    fileSize;       //视频大小(byte)
@property (nonatomic, assign) int                   fps;            //视频fps
@property (nonatomic, assign) int                   bitrate;        //视频码率 (kbps)
@property (nonatomic, assign) int                   audioSampleRate;//音频采样率
@property (nonatomic, assign) int                   width;          //视频宽度
@property (nonatomic, assign) int                   height;         //视频高度
@end

+ (TXVideoInfo *)getVideoInfo:(NSString *)videoPath;
```

#### 1.2 生成预览缩略图
视频编辑通常要提供一个缩略图列表，以便用户快速预览和定位视频文件。获取视频缩略图的方法如下：

```objective-c
[TXUGCVideoInfoReader getSampleImages:10 videoPath:_videoPath progress:^(int number, UIImage *image) {
        // UI显示 iamge
    }];
```

参数传入视频文件路径和期望的缩略图数量如此处的10，使用者可以根据App界面设计的预览区域大小计算出所需要的缩略图数量，SDK根据视频文件的时长，均匀读取指定数量的视频截图。

### 2. 视频编辑
#### 2.1 视频预览
视频编辑提供了即时预览与播放预览两种方式，预览需要上层提供一个UIView用于显示视频画面。

调用`- (instancetype)initWithPreview:(TXPreviewParam *)param`创建TXUGCEditer对象，编辑过程中的即时预览和播放都将渲染到这个UIView上。

预览单帧画面，在缩略图上移动可以根据当前时间戳预览某一帧画面，直接调用`- (void)previewAtTime:(CGFloat)time;`此函数即可，当前视频帧会自动显示在传入的预览view上，通过指定预览view的渲染模式可以设置自适应与填充两种模式。

*  `PREVIEW_RENDER_MODE_FILL_SCREEN`表示填充模式
*  `PREVIEW_RENDER_MODE_FILL_EDGE`表示自适应模式

预览播放视频，直接调用`- (void)startPlayFromTime:(CGFloat)startTime toTime:(CGFloat)endTime`实现，表示预览播放某个时间区间的视频，视频预览的进度可以通过`previewDelegate`获取。


#### 2.2 裁剪生成视频 

对一个视频编辑有很多种操作，裁剪只是其中一种。因此，我们将这些操作定义为`TXOperationParam`对象，

```objective-c
/*
 * 视频操作
 */
@interface TXOperationParam : NSObject
@property (nonatomic, assign) TXOperationType       type;           //操作类型
@property (nonatomic, assign) CGFloat               startTime;      //操作开始时间(s)
@property (nonatomic, assign) CGFloat               endTime;        //操作结束时间(s)
@end
```

TXOperationType目前只支持OPERATION_TYPE_CUT（剪裁视频），startTime表示裁剪的开始时间，endTime表示裁剪的结束时间。

当对视频操作满意后，通过调用`- (int)setOperationList:(NSArray<TXOperationParam *> *)operationList`设置编辑操作，接下来就是把前面操作应用在每一帧上，最终输出为一个文件。

```objective-c
TXUGCEditer* _ugcEdit = [[TXUGCEditer alloc] initWithPreview:param];
TXOperationParam *param = [[TXOperationParam alloc] init];
param.type      = OPERATION_TYPE_CUT;
param.startTime = _videoRangeSlider.leftPos;
param.endTime   = _videoRangeSlider.rightPos;
[_ugcEdit setOperationList:@[param]];
[_ugcEdit generateVideo:VIDEO_COMPRESSED_540P videoOutputPath:_videoOutputPath];
```
输出时指定文件压缩质量和输出路径，输出的进度和结果会通过`generateDelegate`以回调的形式通知用户。

### 3. 视频合成

视频合成需要创建TXUGCJoiner对象，同TXUGCEditer类似，合成也需要上层提供预览UIView，eg：
```objective-c
TXPreviewParam *param = [[TXPreviewParam alloc] init];
param.videoView = _videoPreview.renderView;
TXUGCJoiner* _ugcJoin = [[TXUGCJoiner alloc] initWithPreview:param];
[_ugcJoin setVideoPathList:_composeArray];//需要合并的文件数组
_ugcJoin.previewDelegate = _videoPreview;
```
设置好预览view同时传入待合成的视频文件数组后，可以开始播放预览，合成模块提供了一组接口来做视频的播放预览，eg：

*  `startPlay`表示视频播放开始
*  `pausePlay`表示视频播放暂停
*  `resumePlay`表示视频播放恢复

预览效果满意后调用生成接口即可生成合成后的文件，eg：
```objective-c
_ugcJoin.composeDelegate = self;
[_ugcJoin composeVideo:VIDEO_COMPRESSED_540P videoOutputPath:_outFilePath];
```

合成时指定文件压缩质量和输出路径，输出的进度和结果会通过`composeDelegate`以回调的形式通知用户。

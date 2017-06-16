## 功能概览
视频编辑包括视频裁剪加速、美颜滤镜、音乐混音及添加字幕等功能，我们在SDK开发包的Demo中实现了一套UI源码供使用参考及体验，各功能的界面如下:

![](//mc.qcloudimg.com/static/img/c89588c66500984f5ed790a1a25696cc/IOSVideoEditIOS.jpg)

![](//mc.qcloudimg.com/static/img/304285e91495e5fa463e8512411b6185/IOSVideoEditsubtitle.jpg)
其中图1是视频裁剪加速操作界面，图2是添加滤镜操作界面，图3是添加音乐伴奏操作界面，图4-6是添加字幕操作的界面。

编译运行Demo体验，从资源下载处下载[SDK开发包](https://www.qcloud.com/document/product/584/9366)，解压出来运行Demo工程RTMPiOSDemo.xcodeproj，在运行起来后的主界面中点选视频编辑即可选择视频进入进行编辑功能体验。

## 复用现有UI
视频编辑具有比较复杂的交互逻辑，这也决定了其 UI 复杂度很高，所以我们比较推荐复用 SDK 开发包中的 UI 源码，使用时从Demo中拷贝以下文件夹到自己的工程: 
1. VideoEditor(代码)
2. Resource下的VideoEditor与FilterResource.bundle(资源)
3. Common与Third(整个Demo依赖的公共代码，根据自己的需要再进行删改)

UI源码说明
源码中各个界面组件比较独立，您可根据自己产品需求再对界面进行修改加工。
主要界面组件说明：
1. VideoCutView: 视频裁剪界面，包含了视频裁剪与加速功能，如需定制裁剪界面可对此类进行修改或替换。
2. FilterSettingView: 视频添加滤镜界面，目前包含9种滤镜，如果修改滤镜操作的界面可对此类进行修改或替换。
3. MusicMixView: 视频添加混音界面，包含音乐文件选择，音乐信息展示，音乐长度裁剪，原音与伴音音量调整等功能，如需修改混音界面可对此类进行修改或替换。
4. TextAddView: 视频添加字幕界面，此界面只包含跳转到VideoTextViewController的按钮，实际添加字幕的界面及操作在VideoTextViewController中进行，可根据需要进行修改或去除此界面。
5. VideoTextField: 字幕输入组件，包含字幕文字输入、字幕拖动、放大、旋转、删除、添加字幕背景样式等功能，VideoTextViewController中主要利用此组件完成字幕的添加删除。

VideoEditViewController只负责将这几个界面与预览界面VideoPreview组合起来，并结合SDK去处理界面间的交互及响应，如需对界面进行整体结构的调整可在此类中进行。


## 自己实现UI
如果您不考虑复用我们开发包中的 UI 代码，决心自己实现 UI 部分，则可以参考如下的攻略进行对接：

### 1. 预览图片组

TXVideoInfoReader 的 getVideoInfo 方法可以获取指定视频文件的一些基本信息，getSampleImages 则可以获取指定数量的预览图：

```objective-c
// 获取视频文件的信息
+ (TXVideoInfo *)getVideoInfo:(NSString *)videoPath;

// 对视频文件进行预读，均匀得生成 count 张预览图片组
+ (void)getSampleImages:(int)count
              videoPath:(NSString *)videoPath
               progress:(sampleProcess)sampleProcess;
```

开发包中的 VideoRangeSlider 即使用了 getSampleImages 获取了 10 张缩略图来构建一个由视频预览图组成的进度条。

### 2 效果预览
视频编辑提供了 **定点预览**（将视频画面定格在某一时间点）与**区间预览**（循环播放某一时间段A<=>B内的视频片段）两种效果预览方式，使用时需要给 SDK 绑定一个 UIView 用于显示视频画面。

- **绑定 UIView**
TXVideoEditer 的 initWithPreview 函数用于绑定一个 UIView 给 SDK 来渲染视频画面，绑定时需要制定**自适应**与**填充**两种模式。
```
   PREVIEW_RENDER_MODE_FILL_SCREEN - 填充模式，尽可能充满屏幕不留黑边，所以可能会裁剪掉一部分画面。
   PREVIEW_RENDER_MODE_FILL_EDGE   - 适应模式，尽可能保持画面完整，但当宽高比不合适时会有黑边出现。
```

- **定点预览**
TXVideoEditer 的 previewAtTime 函数用于定格显示某一个时间点的视频画面。

- **区间预览**
TXVideoEditer 的 startPlayFromTime 函数用于循环播放某一时间段A<=>B内的视频片段。

### 3 视频裁剪
视频编辑类操作都符合同一个操作原则：即先设定操作指定，最后用 generateVideo 将所有指令顺序执行，这种方式可以避免多次重复压缩视频引入的不必要的质量损失。

```objective-c
TXUGCEditer* _ugcEdit = [[TXUGCEditer alloc] initWithPreview:param];
// 设置裁剪的 起始时间 和 结束时间
[_ugcEdit setCutFromTime:_videoRangeSlider.leftPos toTime:_videoRangeSlider.rightPos];
// ...
// 生成最终的视频文件
_ugcEdit.generateDelegate = self;
[_ugcEdit generateVideo:VIDEO_COMPRESSED_540P videoOutputPath:_videoOutputPath];
```
输出时指定文件压缩质量和输出路径，输出的进度和结果会通过`generateDelegate`以回调的形式通知用户。

### 4. 滤镜特效
您可以给视频添加滤镜效果，例如美白、浪漫、清新等滤镜，demo提供了9种滤镜选择，同时也可以设置自定义的滤镜。  
设置滤镜的方法为：

```
- (void) setFilter:(UIImage *)image;
```
其中 image 为滤镜映射图，image 设置为nil，会清除滤镜效果。

Demo示例：
```
TXVideoEditer     *_ugcEdit;
NSString * path = [[NSBundle mainBundle] pathForResource:@"FilterResource" ofType:@"bundle"];
path = [path stringByAppendingPathComponent:@"langman.png"];
UIImage* image = [UIImage imageWithContentsOfFile:path];
[_ugcEdit setFilter:image];
```
### 5. 音轨处理
您可以为视频添加自己喜欢的背景音乐，并且可以选择音乐播放的起始时间和结束时间，如果音乐的播放时间段小于视频的时间段，音乐会循环播放至视频结束。除此之外，您也可以设置视频声音和背景声音的大小，来达到自己想要声音合成效果。

设置背景音乐的方法为：

```
- (void) setBGM:(NSString *)path startTime:(float)startTime endTime:(float)endTime;
```
其中 path 为音乐文件路径，startTime 为音乐的起始时间，endTime 为音乐的结束时间。

设置视频和背景声音大小的方法为： 
 
```
- (void) setVideoVolume:(float)volume;  
- (void) setBGMVolume:(float)volume;
```   
其中 volume 表示声音的大小，取值范围 0 ~ 1 ，0 表示静音，1 表示原声大小。

Demo示例：
```
NSString * path = [[NSBundle mainBundle] pathForResource:@"FilterResource" ofType:@"bundle"];
path = [path stringByAppendingPathComponent:@"defalut.mp3"];
[_ugcEdit setBGM:path startTime:1 endTime:10];
[_ugcEdit setVideoVolume:0.5];
[_ugcEdit setBGMVolume:0.5];
```
### 6. 视频加速
您可以设置视频加速播放，实现快播的效果。

设置视频加速播放的方法为：  

```
- (void) setSpeedLevel:(float)level;
```  
其中 level 表示加速等级，取值范围 1 ~ 4 ，1 表示原速度，4 表示4倍速度。

Demo示例：
```
[_ugcEdit setSpeedLevel:2];//两倍加速
```
### 7. 设置水印
您可以为视频设置水印图片，并且可以指定图片的位置

设置水印的方法为：  

```
- (void) setWaterMark:(UIImage *)waterMark  normalizationFrame:(CGRect)normalizationFrame;
```  
其中 waterMark 表示水印图片，normalizationFrame 是相对于视频图像的归一化frame，frame 的 x，y，width，height 的取值范围都为 0~1。

Demo示例：
```
UIImage *image = [UIImage imageNamed:@"watermark"];
[_ugcEdit setWaterMark:image normalizationFrame:CGRectMake(0, 0, 0.3 , 0.3 * image.size.height / image.size.width)];//水印大小占视频宽度的30%，高度根据宽度自适应
```
### 8. 字幕叠加
您可以为视频添加字幕，我们支持对每一帧视频添加字幕，每个字幕你也可以设置视频作用的起始时间和结束时间。所有的字幕组成了一个字幕列表， 你可以把字幕列表传给SDK内部，SDK会自动在合适的时间对视频和字幕做叠加。

设置字幕的方法为：  

```
- (void) setSubtitleList:(NSArray<TXSubtitle *> *)subtitleList;

TXSubtitle 的参数如下：
@interface TXSubtitle: NSObject
@property (nonatomic, strong) UIImage*              titleImage;     //字幕图片   （这里需要客户把承载文字的控件转成image图片）
@property (nonatomic, assign) CGRect                frame;          //字幕的frame（注意这里的frame坐标是相对于渲染view的坐标）
@property (nonatomic, assign) CGFloat               startTime;      //字幕起始时间(s)
@property (nonatomic, assign) CGFloat               endTime;        //字幕结束时间(s)
@end
```  
其中：  
titleImage ： 表示字幕图片，如果上层使用的是 UILabel 之类的控件，请先把控件转成 UIImage ，具体方法可以参照 demo 的示例代码。  
frame ： 表示字幕的 frame ，注意这个frame是相对于渲染 view（initWithPreview时候传入的view）的frame ，具体可以参照 demo 的示例代码。  
startTime ： 字幕作用的起始时间。  
endTime ： 字幕作用的结束时间。  

因为字幕这一块的UI逻辑比较复杂，我们已经在 demo 层有一整套的实现方法，推荐客户直接参考 demo 实现， 可以大大降低您的接入成本。

Demo示例：
```
@interface VideoTextInfo : NSObject
@property (nonatomic, strong) VideoTextFiled* textField;
@property (nonatomic, assign) CGFloat startTime; //in seconds
@property (nonatomic, assign) CGFloat endTime;
@end

videoTextInfos = @[VideoTextInfo1, VideoTextInfo2 ...];

 for (VideoTextInfo* textInfo in videoTextInfos) {
        TXSubtitle* subtitle = [TXSubtitle new];
        subtitle.titleImage = textInfo.textField.textImage;  //UILabel（UIView） -> UIImage
        subtitle.frame = [textInfo.textField textFrameOnView:_videoPreview]; //计算相对于渲染view的坐标
        subtitle.startTime = textInfo.startTime;  //字幕起始时间
        subtitle.endTime = textInfo.endTime;      //字幕结束时间
        [subtitles addObject:subtitle];           //添加字幕列表
  }    
    
 [_ugcEditer setSubtitleList:subtitles];          //设置字幕列表
```

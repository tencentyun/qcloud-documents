
## 复用现有UI
视频编辑器具有比较复杂的交互逻辑，这也决定了其 UI 复杂度很高，而且随着 SDK 的编辑功能不断强化，这里的复杂性会越来越高，所以我们比较推荐复用 SDK 开发包中的 UI 源码（ VideoEditor 目录包含短视频的编辑器代码）。


### 1. 视频裁剪
![](//mc.qcloudimg.com/static/img/a3242d1e0abb14e332011205a384100d/image.jpg)

- VideoPreview 用于实现上图中的视频预览区
- VideoRangeSlider 用于实现上图中的滑动条和裁剪工具
- VideoEditViewController 用于将 VideoPreview 和 VideoRangeSlider 整合起来。

### 2. 滤镜特效
2.0.4 版本支持，敬请期待

### 3. 音轨处理
2.0.4 版本支持，敬请期待

### 4. 视频加速
2.0.4 版本支持，敬请期待

### 5. 字幕叠加
2.0.4 版本支持，敬请期待


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
```objective-c
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
2.0.4 版本支持，敬请期待

### 5. 音轨处理
2.0.4 版本支持，敬请期待

### 6. 视频加速
2.0.4 版本支持，敬请期待

### 7. 字幕叠加
2.0.4 版本支持，敬请期待


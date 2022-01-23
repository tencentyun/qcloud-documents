## 复用现有 UI
视频拼接器具有比较复杂的交互逻辑，这也决定了其 UI 复杂度很高，所以我们比较推荐复用 SDK 开发包中的 UI 源码。VideoJoiner 目录包含短视频拼接器的 UI 源码。 
![](https://main.qcloudimg.com/raw/bf53388286f715539974dec32f458d98.png)

- **VideoJoinerController**：用于实现上图中的视频拼接列表，支持上下拖拽调整顺序。
- **VideoJoinerCell**：用于实现拼接列表中的每一个视频片段。
- **VideoEditPrevController**：用于预览拼接后的视频观看效果。

## 自己实现 UI
如果您不考虑复用我们开发包中的 UI 代码，想自己实现 UI 部分，则可以参考如下的攻略进行对接。
 
### 1. 选择视频文件
Demo 中使用了 QBImagePicker 这样一个开源库实现了多个文件的选择功能，相关代码在 Demo 的 MainViewController 里有所体现。

### 2. 设置预览 View
视频合成需要创建 TXVideoJoiner 对象，同 TXUGCEditer 类似，预览功能也需要上层提供预览 UIView：
```objectivec
//准备预览 View
TXPreviewParam *param = [[TXPreviewParam alloc] init];
param.videoView = _videoPreview.renderView;
param.renderMode = PREVIEW_RENDER_MODE_FILL_EDGE;

// 创建 TXVideoJoiner 对象并设置预览 view
TXVideoJoiner* _videoJoin = [[TXVideoJoiner alloc] initWithPreview:param];
_videoJoin.previewDelegate = _videoPreview;

// 设置待拼接的视频文件组 _composeArray，也就是第一步中选择的若干个文件
[_videoJoin setVideoPathList:_composeArray];
```

设置好预览 view 同时传入待合成的视频文件数组后，可以开始播放预览，合成模块提供了一组接口来做视频的播放预览：

*  `startPlay`：表示视频播放开始。
*  `pausePlay`：表示视频播放暂停。
*  `resumePlay`：表示视频播放恢复。

### 3. 生成最终文件
预览效果满意后调用生成接口即可生成合成后的文件：
```objectivec
_videoJoin.joinerDelegate = self;
[_videoJoin joinVideo:VIDEO_COMPRESSED_540P videoOutputPath:_outFilePath];
```

合成时指定文件压缩质量和输出路径，输出的进度和结果会通过`joinerDelegate`以回调的形式通知用户。

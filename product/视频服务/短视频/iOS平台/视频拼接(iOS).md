
## 复用现有UI
视频编辑器由于逻辑本身的复杂性决定了其 UI 复杂度很高，此文档适用于您要自己编写 UI 界面的场景；相比之下，我们更推荐您使用我们在 SDK 开发包中附赠的 UI 控件源代码，您可以通过代码复用 + 风格修改，节省掉大量 UI 细节的处理时间。

## 自己实现UI
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
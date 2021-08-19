## 复用现有 UI 
视频拼接器具有比较复杂的交互逻辑，这也决定了其 UI 复杂度很高，所以我们比较推荐复用 SDK 开发包中的 UI 源码。 videojoiner 目录包含短视频拼接器的 UI 源码。
![](https://main.qcloudimg.com/raw/128e4f3be2ca2312f697e9e2aa202ff1.png)

- TCVideoJoinerActivity 用于实现上图中的视频拼接列表，支持上下拖拽调整顺序。
- TCVideoJoinerPreviewActivity 用于预览拼接后的视频观看效果。

## 自己实现 UI
如果您不考虑复用我们开发包中的 UI 代码，决心自己实现 UI 部分，则可以参考如下的攻略进行对接：

### 1. 选择视频文件  
自己实现多选文件功能。

### 2. 设置预览 View  
视频合成需要创建 TXVideoJoiner 对象，同 TXVideoEditer 类似，预览功能也需要上层提供预览 FrameLayout：


<dx-codeblock>
::: android java
//准备预览 View        
TXVideoEditConstants.TXPreviewParam param = new TXVideoEditConstants.TXPreviewParam();
param.videoView = mVideoView;
param.renderMode = TXVideoEditConstants.PREVIEW_RENDER_MODE_FILL_EDGE;

// 创建 TXUGCJoiner 对象并设置预览 view
TXVideoJoiner mTXVideoJoiner = new TXVideoJoiner(this);
mTXVideoJoiner.setTXVideoPreviewListener(this);
mTXVideoJoiner.initWithPreview(param);
// 设置待拼接的视频文件组 mVideoSourceList，也就是第一步中选择的若干个文件
mTXVideoJoiner.setVideoPathList(mVideoSourceList);
:::
</dx-codeblock>

设置好预览 view 同时传入待合成的视频文件数组后，可以开始播放预览，合成模块提供了一组接口来做视频的播放预览：

- startPlay：表示视频播放开始。
- pausePlay：表示视频播放暂停。
- resumePlay：表示视频播放恢复。

### 3. 生成最终文件
预览效果满意后调用生成接口即可生成合成后的文件：
```
mTXVideoJoiner.setVideoJoinerListener(this);
mTXVideoJoiner.joinVideo(TXVideoEditConstants.VIDEO_COMPRESSED_540P, mVideoOutputPath);
```
合成时指定文件压缩质量和输出路径，输出的进度和结果会通过 TXVideoJoiner.TXVideoJoinerListener 以回调的形式通知用户。

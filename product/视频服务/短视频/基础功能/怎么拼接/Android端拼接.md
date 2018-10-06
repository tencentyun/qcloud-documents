## 功能概览
视频拼接功能可以前两段视频前后拼接，也可以将两段视频以制定的位置合并到一起。

##相关类介绍

| 类名           | 功能  |
| ------------- | --------- |
| `TXVideoJoiner`| 视频合成类 |

## 使用说明
视频拼接的基本使用流程如下
1. 实例化拼接对象
2. 传入被合并或者拼接的多段视频
3. 开始拼接
4. 监听拼接合成事件获取进度及完成情况

## 从相册选取多个视频文件
Demo中使用了实现从相册选取多视频的功能, 可以参考工具包Demo中TCVideoJoinChooseActivity中的示例代码。

### 1. 选择视频文件  
自己实现多选文件功能
### 2. 设置视频合成源

1、创建视频合成对象

2、设置视频合成的视频源路径列表List<String> pathList。
```
/**
 * 设置合成的视频列表
 * @param videoPathList 视频列表路径
 */
public int setVideoPathList(List<String> videoPathList) ;
```
完整示例如下：
```
TXVideoJoiner mTXVideoJoiner = new TXVideoJoiner(this);
// 设置待拼接的视频文件组 mVideoSourceList，也就是第一步中选择的若干个文件
mTXVideoJoiner.setVideoPathList(mVideoSourceList);
```
### 3. 视频合成预览 
视频合成预览步骤及调用接口如下：
 
1、预览功能也需要上层提供预览 FrameLayout。
 
```
/**
  * 初始化预览View
  * @param param
  */
public void initWithPreview(TXVideoEditConstants.TXPreviewParam param);
```
2、设置视频合成预览进度的回调
```
/**
  * 设置视频合成预览进度回调
  * @param listener
  */
public void setTXVideoPreviewListener(TXVideoJoiner.TXVideoPreviewListener listener);
```
完整示例如下：

1、xml中配置
```
<FrameLayout
    android:id="@+id/video_view"
    android:layout_width="match_parent"
    android:layout_height="225dp" />
```
2、java代码设置
```
//准备预览 View        
FrameLayout videoView = (FrameLayout) findViewById(R.id.video_view);
TXVideoEditConstants.TXPreviewParam param = new TXVideoEditConstants.TXPreviewParam();
param.videoView = videoView;
param.renderMode = TXVideoEditConstants.PREVIEW_RENDER_MODE_FILL_EDGE;

// 创建 TXUGCJoiner 对象并设置预览 view
mTXVideoJoiner.setTXVideoPreviewListener(this);
mTXVideoJoiner.initWithPreview(param);
```
### 4. 播放状态控制
设置好预览view同时传入待合成的视频文件数组后，可以开始播放预览，合成模块提供了一组接口来做视频的播放预览：
```
// 开始播放视频
public void startPlay();
// 暂停播放视频
public void pausePlay();
// 继续播放视频
public void resumePlay();
// 停止播放视频
public void stopPlay();
```
### 5. 生成最终文件
预览效果满意后调用生成接口即可生成合成后的文件，视频合成步骤及调用接口如下：

1、设置视频合成进度回调
```
/**
  * 设置合成回调
  * @param listener
  */
public void setVideoJoinerListener(TXVideoJoiner.TXVideoJoinerListener listener);
```
2、视频合成
```
/**
  * 合成
  * @param videoCompressed
  * @param videoOutputPath
  */
public void joinVideo(int videoCompressed, String videoOutputPath);
```
完整示例如下：
```
String outputPath = Environment.getExternalStorageDirectory() + File.separator + "temp.mp4";
//使用前面创建好的TXVideoJoiner对象
mTXVideoJoiner.setVideoJoinerListener(this);
mTXVideoJoiner.joinVideo(TXVideoEditConstants.VIDEO_COMPRESSED_540P, outputPath);
```
合成时指定文件压缩质量和输出路径，输出的进度和结果会通过 TXVideoJoiner.TXVideoJoinerListener 以回调的形式通知用户。

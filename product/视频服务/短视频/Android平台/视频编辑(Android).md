# 短视频编辑功能概览
视频编辑包括视频裁剪加速、美颜滤镜、音乐混音及添加字幕等功能，我们在SDK开发包的Demo中实现了一套UI源码供使用参考及体验，各功能的界面如下:

![](https://mc.qcloudimg.com/static/img/6887670916605956d6a624db942ac8eb/short_video_editer.png)

- 图1是视频裁剪加速操作界面
- 图2是添加滤镜操作界面
- 图3是添加音乐伴奏操作界面
- 图4-6是添加字幕操作的界面

编译运行Demo体验，从资源下载处下载[Android完整版开发包](https://www.qcloud.com/document/product/454/7873)，解压出来运行RTMPAndroidDemoSrc工程，在运行起来后的主界面中点选视频编辑即可选择视频进入进行编辑功能体验。

## 1 复用现有UI
视频编辑具有比较复杂的交互逻辑，这也决定了其 UI 复杂度很高，所以我们比较推荐复用 SDK 开发包中的 UI 源码，使用时从Demo中拷贝以下文件夹到自己的工程: 

1. videoeditor/下的代码
2. res/下的VideoEditor资源
3. jniLibs/下的jar和so
4.在AndroidManifest.xml中声明这几个Activity，并声明权限

```
<uses-permission android:name="android.permission.READ_CONTACTS" />
```

```
<activity
    android:name=".videoeditor.TCVideoEditerActivity"
    android:screenOrientation="portrait"
    /> 
<activity
    android:name=".common.activity.videochoose.TCVideoChooseActivity"
    android:screenOrientation="portrait">
</activity>
```

## 2 自己实现UI
如果您不考虑复用我们开发包中的 UI 代码，决心自己实现 UI 部分，则可以参考如下的攻略进行对接：
### 1. 预览图片组
**TXVideoInfoReader** 的 **getVideoFileInfo** 方法可以获取指定视频文件的一些基本信息，**getSampleImages** 则可以获取指定数量的预览图：

```objective-c
// 获取视频文件的信息
getVideoFileInfo(String videoPath){...}

// 对视频文件进行预读，均匀得生成 count 张预览图片组
getSampleImages(int count, String videoPath, TXVideoInfoReader.OnSampleProgrocess listener)
```
开发包中的 TCVideoEditerActivity 即使用了 getSampleImages 获取了 10 张缩略图来构建一个由视频预览图组成的进度条。

### 2 效果预览
视频编辑提供了**区间预览**（循环播放某一时间段A<=>B内的视频片段）预览方式，使用时需要给 SDK 绑定一个 FrameLayout 用于显示视频画面。

- **绑定 FrameLayout**  
TXVideoEditer 的 initWithPreview 函数用于绑定一个 FrameLayout 给 SDK 来渲染视频画面，绑定时需要制定**自适应**与**填充**两种模式。
```
PREVIEW_RENDER_MODE_FILL_SCREEN - 填充模式，尽可能充满屏幕不留黑边，所以可能会裁剪掉一部分画面。
PREVIEW_RENDER_MODE_FILL_EDGE   - 适应模式，尽可能保持画面完整，但当宽高比不合适时会有黑边出现。
```

- **区间预览**
TXVideoEditer 的 startPlayFromTime 函数用于循环播放某一时间段A<=>B内的视频片段。

### 3 视频裁剪
视频编辑类操作都符合同一个操作原则：即先设定操作指定，最后用 generateVideo 将所有指令顺序执行，这种方式可以避免多次重复压缩视频引入的不必要的质量损失。

```objective-c
mTXVideoEditer.initWithPreview(param);
// 设置裁剪的 起始时间 和 结束时间
 mTXVideoEditer.setCutFromTime(mEditPannel.getSegmentFrom(), mEditPannel.getSegmentTo());
// ...
// 生成最终的视频文件
mTXVideoEditer.setVideoGenerateListener(this);
mTXVideoEditer.generateVideo(TXVideoEditConstants.VIDEO_COMPRESSED_540P, mVideoOutputPath);
```
输出时指定文件压缩质量和输出路径，输出的进度和结果会通过`TXVideoEditer.TXVideoGenerateListener`以回调的形式通知用户。

### 4. 滤镜特效
您可以给视频添加滤镜效果，例如美白、浪漫、清新等滤镜，demo提供了9种滤镜选择，同时也可以设置自定义的滤镜。  
设置滤镜调用 **TXVideoEditer** 的 **setFilter** 方法：

```
void setFilter(Bitmap bmp) 
```
其中 image 为滤镜映射图，image 设置为nil，会清除滤镜效果。
 
### 5. 音轨处理
准备中...
 
### 6. 视频加速
准备中...
### 7. 设置水印
准备中...
### 8. 字幕叠加
准备中...

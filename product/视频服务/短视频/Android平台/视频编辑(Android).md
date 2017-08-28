# 短视频编辑功能概览
视频编辑包括视频裁剪加速、美颜滤镜、音乐混音及添加字幕等功能，我们在SDK开发包的Demo中实现了一套UI源码供使用参考及体验，各功能的界面如下:

![](https://mc.qcloudimg.com/static/img/fe456c2f70519ec31eefc008f6e14791/androidedit1.png)

![](https://mc.qcloudimg.com/static/img/edc4f6add127d240259fc310bf40ddd6/androidedit2.png)
- 图1是视频裁剪加速操作界面
- 图2是添加滤镜操作界面
- 图3是添加音乐伴奏操作界面
- 图4-6是添加字幕操作的界面

编译运行Demo体验，从资源下载处下载[Android完整版开发包](https://www.qcloud.com/document/product/454/7873)，解压出来运行RTMPAndroidDemoSrc工程，在运行起来后的主界面中点选视频编辑即可选择视频进入进行编辑功能体验。

## 1 复用现有UI
视频编辑具有比较复杂的交互逻辑，这也决定了其 UI 复杂度很高，所以我们比较推荐复用 SDK 开发包中的 UI 源码，使用时从Demo中拷贝以下文件夹到自己的工程:

1. shortview/editor下的代码
2. res/下的VideoEditor资源
3. jniLibs/下的jar和so
4. 在AndroidManifest.xml中声明这几个Activity，并声明权限

```
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
```

```
<activity
    android:name=".shortvideo.choose.TCVideoChooseActivity"
    android:screenOrientation="portrait"
    />
<activity
    android:name=".shortvideo.editor.TCVideoEditerActivity"
    android:screenOrientation="portrait">
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
您可以为视频添加自己喜欢的背景音乐，并且可以选择音乐播放的起始时间和结束时间，如果音乐的播放时间段小于视频的时间段，音乐会循环播放至视频结束。除此之外，您也可以设置视频声音和背景声音的大小，来达到自己想要声音合成效果。

设置背景音乐的方法为：
```
public int setBGM(String path);
```
其中 mBGMPath 为音乐文件路径，返回值为 0 表示设置成功； 其他表示失败，如：不支持的音频格式。
设置BGM起止时间的方法为：
```
public void setBGMStartTime(long startTime, long endTime);
```
其中起止时间的单位均为毫秒。

设置视频和背景声音大小的方法为：
```
public void setVideoVolume(float volume);
public void setBGMVolume(float volume);
```
其中 volume 表示声音的大小， 取值范围 0 ~ 1 ， 0 表示静音， 1 表示原声大小。

Demo示例：
```
mTXVideoEditer.setBGM(mBGMPath);
mTXVideoEditer.setBGMStartTime(startTime, endTime);
mTXVideoEditer.setBGMVolume(0.5f);
mTXVideoEditer.setVideoVolume(0.5f);
```
### 6. 视频加速
您可以设置视频加速播放，实现快播的效果。

设置视频加速播放的方法为：

```
public void setSpeedLevel(float speed);
```
其中 level 表示加速等级，取值范围 1 ~ 4 ，1 表示原速度，4 表示4倍速度。

Demo示例：
```
mTXVideoEditer.setSpeedLevel(2.0f);
```
### 7. 设置水印
您可以为视频设置水印图片，并且可以指定图片的位置

设置水印的方法为：

```
public void setWaterMark(Bitmap waterMark, TXVideoEditConstants.TXRect rect);
```
其中 waterMark 表示水印图片，rect 是相对于视频图像的归一化frame，frame 的 x，y，width，height 的取值范围都为 0 ~ 1。

Demo示例：
```
TXVideoEditConstants.TXRect rect = new TXVideoEditConstants.TXRect();
rect.x = 0.5f;
rect.y = 0.5f;
rect.width = 0.5f;
mTXVideoEditer.setWaterMark(mWaterMarkLogo, rect);
```
### 8. 字幕叠加
您可以为视频添加字幕，我们支持对每一帧视频添加字幕，每个字幕你也可以设置视频作用的起始时间和结束时间。所有的字幕组成了一个字幕列表， 你可以把字幕列表传给SDK内部，SDK会自动在合适的时间对视频和字幕做叠加。

设置字幕的方法为：

```
public void setSubtitleList(List<TXVideoEditConstants.TXSubtitle> subtitleList);

//TXSubtitle 的参数如下：
public final static class TXSubtitle {
		public Bitmap titleImage;                                 // 字幕图片
		public TXRect frame;                                      // 字幕的frame
		public long startTime;                                    // 字幕起始时间(ms)
		public long endTime;                                      // 字幕结束时间(ms)
}

public final static class TXRect {
		public float x;
		public float y;
		public float width;
}
```
其中：
titleImage ： 表示字幕图片，如果上层使用的是 TextView 之类的控件，请先把控件转成 Bitmap ，具体方法可以参照 demo 的示例代码。
frame ： 表示字幕的 frame ，注意这个frame是相对于渲染 view（initWithPreview时候传入的view）的frame ，具体可以参照 demo 的示例代码。
startTime ： 字幕作用的起始时间。
endTime ： 字幕作用的结束时间。

因为字幕这一块的UI逻辑比较复杂，我们已经在 demo 层有一整套的实现方法，推荐客户直接参考 demo 实现， 可以大大降低您的接入成本。

Demo示例：
```
mSubtitleList.clear();
for (int i = 0; i < mWordInfoList.size(); i++) {
    TCWordOperationView view = mOperationViewGroup.getOperationView(i);
    TXVideoEditConstants.TXSubtitle subTitle = new TXVideoEditConstants.TXSubtitle();
    subTitle.titleImage = view.getRotateBitmap(); //获取Bitmap
    TXVideoEditConstants.TXRect rect = new TXVideoEditConstants.TXRect();
    rect.x = view.getImageX(); // 获取相对parent view的x坐标
    rect.y = view.getImageY(); // 获取相对parent view的y坐标
    rect.width = view.getImageWidth(); // 图片宽度
    subTitle.frame = rect;
    subTitle.startTime = mWordInfoList.get(i).getStartTime(); // 设置开始时间
    subTitle.endTime = mWordInfoList.get(i).getEndTime();	// 设置结束时间
    mSubtitleList.add(subTitle);
}
mTXVideoEditer.setSubtitleList(mSubtitleList); // 设置字幕列表
```

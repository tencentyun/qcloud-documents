视频编辑包括视频裁剪、时间特效（慢动作、倒放、重复）、滤镜特效（动感光波，暗黑幻影，灵魂出窍，画面分裂）、滤镜风格（唯美，粉嫩，蓝调等）、音乐混音、动态贴纸、静态贴纸、气泡字幕等功能。

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
| TXVideoInfoReader| 媒体信息获取 |
| TXVideoEditer | 视频编辑 |

## 使用说明
视频编辑的基本使用流程如下：

1. 设置视频路径。
2. 视频导入。
3. 添加效果。
4. 生成视频到指定文件。
5. 监听生成事件。
6. 资源释放。


## 视频信息获取
**TXVideoInfoReader** 的 **getVideoFileInfo** 方法可以获取指定视频文件的一些基本信息, 相关接口如下：
```
/**
  * 获取视频信息
  * @param videoPath 视频文件路径
  * @return
  */
public TXVideoEditConstants.TXVideoInfo getVideoFileInfo(String videoPath);
```
返回的 TXVideoInfo 定义如下：

```
public final static class TXVideoInfo {
        public Bitmap coverImage;                                // 视频首帧图片
        public long duration;                                         // 视频时长(ms)
        public long fileSize;                                          // 视频大小(byte)
        public float fps;                                                // 视频 fps
        public int bitrate;                                              // 视频码率 (kbps)
        public int width;                                               // 视频宽度
        public int height;                                               // 视频高度
        public int audioSampleRate;                              // 音频码率
 }
```
完整示例如下：
```
//sourcePath 为视频源路径
String sourcePath = Environment.getExternalStorageDirectory() + File.separator + "temp.mp4";
TXVideoEditConstants.TXVideoInfo info = TXVideoInfoReader.getInstance().getVideoFileInfo(sourcePath);
```
## 缩略图获取
缩略图的接口主要用于生成视频编辑界面的预览缩略图，或获取视频封面等。
### 按个数平分时间获取缩略图

<dx-tabs>
::: 快速导入生成精准缩略图
**调用接口：**

```
/**
  * 获取缩略图列表
  * @param count    缩略图张数
  * @param width    缩略图宽度
  * @param height   缩略图高度
  * @param fast       缩略图是否关键帧的图片
  * @param listener 缩略图的回调函数
*/
public void getThumbnail(int count, int width, int height, boolean fast, TXThumbnailListener listener)
```

参数 @param fast 可以使用两种模式：
- 快速出图：输出的缩略图速度比较快，但是与视频对应不精准，传入参数 true。
- 精准出图：输出的缩略图与视频时间点精准对应，但是在高分辨率上速度慢一些，传入参数 false。

**完整示例：**

```
mTXVideoEditer.getThumbnail(TCVideoEditerWrapper.mThumbnailCount, 100, 100, false, mThumbnailListener);

private TXVideoEditer.TXThumbnailListener mThumbnailListener = new TXVideoEditer.TXThumbnailListener() {
    @Override
        public void onThumbnail(int index, long timeMs, final Bitmap bitmap) {
            Log.i(TAG, "onThumbnail: index = " + index + ",timeMs:" + timeMs);
        //将缩略图放入图片控件上
        }
    };
```
:::
:::  全功能导入获取缩略图
请参见 [视频导入](#video_import)。
:::
</dx-tabs>

### 根据时间列表获取缩略图
```
List<Long> list = new ArrayList<>();
list.add(10000L);
list.add(12000L);
list.add(13000L);
list.add(14000L);
list.add(15000L);

TXVideoEditer txVideoEditer = new TXVideoEditer(TCVideoPreviewActivity.this);
txVideoEditer.setVideoPath(mVideoPath);
txVideoEditer.setThumbnailListener(new TXVideoEditer.TXThumbnailListener() {
       @Override
       public void onThumbnail(int index, long timeMs, Bitmap bitmap) {
           Log.i(TAG, "bitmap:" + bitmap + ",timeMs:" + timeMs);
           saveBitmap(bitmap, timeMs);
       }
});
txVideoEditer.getThumbnailList(list, 200, 200);
```
>!
>- List 中时间点不能超出视频总时长，对于超出总时长的返回最后一张图片。
>- 设置的时间点单位是毫秒（ms）。

[](id:video_import)
## 视频导入

### 快速导入
快速导入视频，可以直接观看到视频编辑的预览效果，支持视频裁剪、时间特效（慢动作）、滤镜特效、滤镜风格、音乐混音、动态贴纸、静态贴纸、气泡字幕等功能，不支持的功能有时间特效（重复、倒放）。

[](id:p1)
### 全功能导入
全功能导入，支持所有的功能，包括时间特效（重复、倒放）。需要为视频先预处理操作。
经过全功能导入后的视频可以精确的 seek 到每个时间点，看到对应的画面，预处理操作同时还可以精确的生成当前时间点视频缩略图。

全功能导入步骤及调用接口如下：
1. 设置精确输出缩略图。
```
/**
  * 设置预处理输出的缩略图
  */
public void setThumbnail(TXVideoEditConstants.TXThumbnail thumbnail)
```
2. 设置输出缩略图的回调。
```
/**
  * 设置预处理输出缩略图回调
  * @param listener
  */
public void setThumbnailListener(TXThumbnailListener listener)
```
>!缩略图的宽高最好不要设置视频宽高，SDK 内部缩放效率更高。
3. 设置视频预处理回调接口。
```
/**
  * 设置视频预处理回调
  * @param listener
  */
public void setVideoProcessListener(TXVideoProcessListener listener)
```
4. 进行视频预处理。
```
public void processVideo();
```

#### 完整示例如下：

```
int thumbnailCount = 10;  //可以根据视频时长生成缩略图个数
TXVideoEditConstants.TXThumbnail thumbnail = new TXVideoEditConstants.TXThumbnail();
thumbnail.count = thumbnailCount;
thumbnail.width = 100;   // 输出缩略图宽
thumbnail.height = 100;  // 输出缩略图高
mTXVideoEditer.setThumbnail(thumbnail);                               // 设置预处理生成的缩略图
mTXVideoEditer.setThumbnailListener(mThumbnailListener); //  设置缩略图回调

mTXVideoEditer.setVideoProcessListener(this);                       // 视频预处理进度回调
mTXVideoEditer.processVideo();                                               // 进行预处理
```

## 编辑预览
视频编辑提供了 定点预览（将视频画面定格在某一时间点）与区间预览（循环播放某一时间段 A<=>B 内的视频片段）两种效果预览方式，使用时需要给 SDK 绑定一个 UIView 用于显示视频画面。

### 1. 设置预览播放的 Layout
```
public void initWithPreview(TXVideoEditConstants.TXPreviewParam param)
```
设置预览 Layout 时，可以设置两种视频画面渲染模式，在 TXVideoEditConstants 常量中定义了这两种渲染模式
```
public final static int PREVIEW_RENDER_MODE_FILL_SCREEN = 1;   // 填充模式，尽可能充满屏幕不留黑边，所以可能会裁剪掉一部分画面
public final static int PREVIEW_RENDER_MODE_FILL_EDGE = 2;        // 适应模式，尽可能保持画面完整，但当宽高比不合适时会有黑边出现
```
### 2. 定点预览
经过 [全功能导入](#p1) 的视频可以精确预览到某一个时间点的视频画面。
```
public void previewAtTime(long timeMs);
```
### 3. 区间预览
TXVideoEditer 的 startPlayFromTime 函数用于循环播放某一时间段 A<=>B 内的视频片段。
```
// 播放某一时间段的视频，从 startTime 到 endTime 的视频片段
public void startPlayFromTime(long startTime, long endTime);
```
### 4. 预览的暂停与恢复
```
// 暂停播放视频
public void pausePlay();


// 继续播放视频
public void resumePlay();


// 停止播放视频
public void stopPlay();
```

### 5. 美颜滤镜
您可以给视频添加滤镜效果，例如美白、浪漫、清新等滤镜，Demo 提供了16种滤镜选择，同时也可以设置自定义的滤镜。

#### 设置滤镜的方法：

```
void setFilter(Bitmap bmp)
```
其中 Bitmap 为滤镜映射图，bmp 设置为 null，会清除滤镜效果。

```
void setSpecialRatio(float specialRatio)
```
该接口可以调整滤镜程度值，一般为0.0 - 1.0。

```
void setFilter(Bitmap leftBitmap, float leftIntensity, Bitmap rightBitmap, float rightIntensity, float leftRatio)
```
该接口能够实现组合滤镜，即左右可以添加不同的滤镜。leftBitmap 为左侧滤镜、leftIntensity 为左侧滤镜程度值；rightBitmap 为右侧滤镜、rightIntensity 为右侧滤镜程度值；leftRatio 为左侧滤镜所占的比例，一般为0.0 - 1.0。当 leftBitmap 或 rightBitmap 为 null，则该侧清除滤镜效果。

### 6. 水印
<dx-tabs>
::: 设置全局水印
您可以为视频设置水印图片，并且可以指定图片的位置。

#### 设置水印方法：
```
public void setWaterMark(Bitmap waterMark, TXVideoEditConstants.TXRect rect);
```

其中 waterMark 表示水印图片，rect 是相对于视频图像的归一化 frame，frame 的 x、y、width、height 的取值范围都为 0 - 1。

#### Demo 示例：
```
TXVideoEditConstants.TXRect rect = new TXVideoEditConstants.TXRect();
rect.x = 0.5f;
rect.y = 0.5f;
rect.width = 0.5f;
mTXVideoEditer.setWaterMark(mWaterMarkLogo, rect);
```
:::
::: 设置片尾水印
您可以为视频设置片尾水印，并且可以指定片尾水印的位置。

#### 设置片尾水印的方法：
```
setTailWaterMark(Bitmap tailWaterMark, TXVideoEditConstants.TXRect txRect, int duration);
```

其中 tailWaterMark 表示片尾水印图片，txRect 是相对于视频图像的归一化 txRect，txRect 的 x、y、width 取值范围都为0 - 1，duration 为水印的持续时长，单位：秒。

#### Demo 实例：
设置水印在片尾中间，持续3秒。
```
Bitmap tailWaterMarkBitmap = BitmapFactory.decodeResource(getResources(), R.drawable.tcloud_logo);
TXVideoEditConstants.TXRect txRect = new TXVideoEditConstants.TXRect();
txRect.x = (mTXVideoInfo.width - tailWaterMarkBitmap.getWidth()) / (2f * mTXVideoInfo.width);
txRect.y = (mTXVideoInfo.height - tailWaterMarkBitmap.getHeight()) / (2f * mTXVideoInfo.height);
txRect.width = tailWaterMarkBitmap.getWidth() / (float) mTXVideoInfo.width;
mTXVideoEditer.setTailWaterMark(tailWaterMarkBitmap, txRect, 3);
```
:::
</dx-tabs>

## 压缩裁剪
### 视频码率设置
目前支持自定义视频的码率，这里建议设置的范围600 - 12000kbps，如果设置了这个码率，SDK 最终压缩视频时会优先选取这个码率，注意码率不要太大或太小，码率太大，视频的体积会很大，码率太小，视频会模糊不清。
```
public void setVideoBitrate(int videoBitrate);
```

### 视频裁剪
设置视频裁剪的开始时间和结束时间。
```
/**
  * 设置视频剪切范围
  * @param startTime 视频剪切的开始时间(ms)
  * @param endTime   视频剪切的结束时间(ms)
  */
public void setCutFromTime(long startTime, long endTime)


// ...
// 生成最终的视频文件
public void generateVideo(int videoCompressed, String videoOutputPath)
```

参数 videoCompressed 在 TXVideoEditConstants 中可选常量。
```
VIDEO_COMPRESSED_360P ——压缩至360P分辨率（360*640）
VIDEO_COMPRESSED_480P ——压缩至480P分辨率（640*480）
VIDEO_COMPRESSED_540P ——压缩至540P分辨率 (960*540)
VIDEO_COMPRESSED_720P ——压缩至720P分辨率 (1280*720)
```
如果源视频的分辨率小于设置的常量对应的分辨率，按照原视频的分辨率。
如果源视频的分辨率大于设置的常量对象的分辨率，进行视频压缩至相应分辨率。

## 资源释放
当您不再使用 mTXVideoEditer 对象时，一定要记得调用 **release()** 释放它。

## 高级功能
- [类抖音特效](https://cloud.tencent.com/document/product/1449/57051)
- [设置背景音乐](https://cloud.tencent.com/document/product/1449/57037)
- [贴纸字幕](https://cloud.tencent.com/document/product/1449/57053)
- [图片转场特效](https://cloud.tencent.com/document/product/1449/57057)


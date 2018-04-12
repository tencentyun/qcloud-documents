
## 对接攻略
短视频录制即采集摄像头画面和麦克风声音，经过图像和声音处理后，进行编码压缩最终生成期望清晰度的 MP4 文件。
可以通过开发包中的DEMO工程体验录制的功能
![](https://main.qcloudimg.com/raw/4f8195d62fdb7e78ccd11609aad0c87d.png )
Android录制功能的代码位置：com.tencent.liteav.demo.videorecord包名下面，其中TCVideoSettingActivity是录制设置界面，TCVideoRecordActivity是录制界面，另外需要拷贝界面中所需的资源文件，就可以实现录制的界面效果和功能了。
## 接口介绍 
腾讯云 UGC SDK 提供了相关接口用来实现短视频的录制与发布，其详细定义如下：

| 接口文件                     | 功能                       |
| ------------------------ | ------------------------ |
| `TXUGCRecord.java`       | 实现小视频的录制功能               |
| `TXRecordCommon.java`    | 基本参数定义，包括了小视频录制回调及发布回调接口 |
| `TXUGCPartsManager.java` | 视频片段管理类，用于视频的多段录制，回删等    |
| `ITXVideoRecordListener.java` | 小视频录制回调                  |

### 1. 画面预览
TXUGCRecord（位于 TXUGCRecord.java） 负责小视频的录制功能，我们的第一个工作是先把预览功能实现。startCameraSimplePreview函数用于启动预览。由于启动预览要打开摄像头和麦克风，所以这里可能会有权限申请的提示窗。

```java
mTXCameraRecord = TXUGCRecord.getInstance(this.getApplicationContext());
mTXCameraRecord.setVideoRecordListener(this);					//设置录制回调
mVideoView = (TXCloudVideoView) findViewById(R.id.video_view);	//准备一个预览摄像头画面的
mVideoView.enableHardwareDecode(true);
TXRecordCommon.TXUGCSimpleConfig param = new TXRecordCommon.TXUGCSimpleConfig();
//param.videoQuality = TXRecordCommon.VIDEO_QUALITY_LOW;		// 360p
param.videoQuality = TXRecordCommon.VIDEO_QUALITY_MEDIUM;		// 540p
//param.videoQuality = TXRecordCommon.VIDEO_QUALITY_HIGH;		// 720p
param.isFront = true;           //是否前置摄像头，使用
param.minDuratioin = 5000;	//视频录制的最小时长ms
param.maxDuration = 60000;	//视频录制的最大时长ms
mTXCameraRecord.startCameraSimplePreview(param,mVideoView);
```

### 2. 画面特效
不管是录制前，还是录制中，您都可以使用 TXUGCRecord 里的特效开关来为视频画面添加一些特效，或者是对摄像头本身进行控制。

```java
//////////////////////////////////////////////////////////////////////////
//                      以下为 1.9.1 版本后均支持的特效
//////////////////////////////////////////////////////////////////////////
//
// 切换前后摄像头 参数 mFront 代表是否前置摄像头 默认前置
mTXCameraRecord.switchCamera(mFront);

// 设置美颜 和 美白 效果级别
// beautyDepth     : 美颜级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
// whiteningDepth  : 美白级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
mTXCameraRecord.setBeautyDepth(beautyDepth, whiteningDepth);

// 设置颜色滤镜：浪漫、清新、唯美、粉嫩、怀旧...
// Bitmap     : 指定滤镜用的颜色查找表。注意：一定要用png格式！！！
// demo用到的滤镜查找表图片位于RTMPAndroidDemo/app/src/main/res/drawable-xxhdpi/目录下。
// setSpecialRatio : 用于设置滤镜的效果程度，从0到1，越大滤镜效果越明显，默认取值0.5
mTXCameraRecord.setFilter(filterBitmap);
mTXCameraRecord.setSpecialRatio(0.5);
// 设置全局水印TXRect-水印相对于视频图像的归一化值，sdk内部会根据水印宽高比自动计算height
// 比如视频图像大小为（540，960） TXRect三个参数设置为0.1，0.1，0.1,
// 水印的实际像素坐标为（540 * 0.1，960 * 0.1，540 * 0.1 ，
// 540 * 0.1 * watermarkBitmap.height / watermarkBitmap.width）
setWatermark(watermarkBitmap, txRect)
// 设置绿幕文件:目前图片支持jpg/png，视频支持mp4/3gp等Android系统支持的格式
setGreenScreenFile(path, isLoop);
// 设置美颜风格：光滑，自然，朦胧
setBeautyStyle(style);

// 是否打开闪光灯 参数 mFlashOn 代表是否打开闪关灯 默认关闭
mTXCameraRecord.toggleTorch(mFlashOn);
// 获取摄像头支持的最大焦距
mTXCameraRecord.mTXCameraRecord();
// 设置焦距
mTXCameraRecord.setZoom(value);

//////////////////////////////////////////////////////////////////////////
//                      背景音相关
//////////////////////////////////////////////////////////////////////////
// 设置背景音乐播放回调接口.TXRecordCommon.ITXBGMNotify
setBGMNofify(notify);
// 播放背景音
mTXCameraRecord.playBGM(path);
// 停止播放背景音
mTXCameraRecord.stopBGM();
// 暂停播放背景音
mTXCameraRecord.pauseBGM();
// 继续播放背景音
mTXCameraRecord.resumeBGM();
// 设置麦克风的音量大小，播放背景音混音时使用，用来控制麦克风音量大小
// 音量大小,1为正常音量,建议值为0~2,如果需要调大音量可以设置更大的值.
mTXCameraRecord.setMicVolume(x);
// 设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小
// 音量大小,1为正常音量,建议值为0~2,如果需要调大背景音量可以设置更大的值.
setBGMVolume(x);

//////////////////////////////////////////////////////////////////////////
//                       以下为仅特权版才支持的特效
// （由于采用优图团队的知识产权，我们无法对外免费提供，需要使用特权版 SDK 才能支持）
//////////////////////////////////////////////////////////////////////////

// 设置动效贴纸 motionTmplPath 动效文件路径： 空String "" 则取消动效
mTXCameraRecord.setMotionTmp(motionTmplPath);
// 设置绿幕文件:目前图片支持jpg/png，视频支持mp4/3gp等Android系统支持的格式
mTXCameraRecord.setGreenScreenFile();
// 设置大眼效果 0~9
mTXCameraRecord.setEyeScaleLevel(eyeScaleLevel);
// 设置瘦脸效果 0~9
mTXCameraRecord.setFaceScaleLevel(faceScaleLevel);
// 设置V脸效果 0~9
mTXCameraRecord.setFaceVLevel(level)
// 设置下巴拉伸或收缩效果 0~9
mTXCameraRecord.setChinLevel(scale)
// 设置缩脸效果 0~9
mTXCameraRecord.setFaceShortLevel(level)
// 设置小鼻效果 0~9
mTXCameraRecord.setNoseSlimLevel(scale)

```


### 3. 文件录制
调用 TXUGCRecord 的 startRecord 函数即可开始录制，调用 stopRecord 函数即可结束录制，startRecord 和 stopRecord 的调用一定要配对。
```java
mTXCameraRecord.startRecord();
mTXCameraRecord.stopRecord();
```

录制的过程和结果是通过 TXRecordCommon.ITXVideoRecordListener（位于 TXRecordCommon.java 中定义）接口反馈出来的：

- onRecordProgress 用于反馈录制的进度，参数millisecond表示录制时长，单位毫秒:
```java
@optional
void onRecordProgress(long milliSecond);
```

- onRecordComplete 反馈录制的结果，TXRecordResult 的 retCode 和 descMsg 字段分别表示错误码和错误描述信息，videoPath 表示录制完成的小视频文件路径，coverImage 为自动截取的小视频第一帧画面，便于在视频发布阶段使用。
```java   
@optional
void onRecordComplete(TXRecordResult result);
```

- onRecordEvent 录制事件回调，包含事件id和事件相关的参数(key,value)格式

```java   
@optional
void onRecordEvent(final int event, final Bundle param);
```



### 4.多段录制与回删

```java
// pauseRecord 后会生成一段视频，视频可以在 TXUGCPartsManager 里面获取 
mTXCameraRecord.pauseRecord();
// 继续录制视频
mTXCameraRecord.resumeRecord();
// 获取片段管理对象
mTXCameraRecord.getPartsManager();
// 获取当前所有视频片段的总时长
mTXUGCPartsManager.getDuration();
// 获取所有视频片段路径
mTXUGCPartsManager.getPartsPathList();
// 删除最后一段视频
mTXUGCPartsManager.deleteLastPart();
// 删除指定片段视频
mTXUGCPartsManager.deletePart(index);
// 删除所有片段视频
mTXUGCPartsManager.deleteAllParts();
```

### 5. 文件预览

使用 [视频播放](https://cloud.tencent.com/document/product/584/9373) 即可预览刚才生成的 MP4 文件，需要在调用 startPlay 时指定播放类型为 [PLAY_TYPE_LOCAL_VIDEO](https://cloud.tencent.com/document/product/584/9373#step-3.3A-.E5.90.AF.E5.8A.A8.E6.92.AD.E6.94.BE.E5.99.A86) 。

### 6. 获取 licence 信息
新版本的SDK增加了短视频licence的校验，如果校验没通过，您可以通过该接口来查询licence中具体信息

``` 
mTXCameraRecord.getLicenceInfo();
``` 
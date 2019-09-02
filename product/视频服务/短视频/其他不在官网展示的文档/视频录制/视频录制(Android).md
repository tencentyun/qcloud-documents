## 对接攻略
短视频录制即采集摄像头画面和麦克风声音，经过图像和声音处理后，进行编码压缩最终生成期望清晰度的 MP4 文件。
可以通过开发包中的DEMO工程体验录制的功能
![](https://main.qcloudimg.com/raw/333c7a07d6a37308152391c73ee99b7a.png )
Android录制功能的代码位置：com.tencent.liteav.demo.videorecord 包名下面，其中 TCVideoSettingActivity 是录制设置界面，TCVideoRecordActivity 是录制界面，另外需要拷贝界面中所需的资源文件，就可以实现录制的界面效果和功能了。
## 接口介绍 
腾讯云 UGC SDK 提供了相关接口用来实现短视频的录制，其详细定义如下：

| 接口文件                     | 功能                       |
| ------------------------ | ------------------------ |
| `TXUGCRecord.java`       | 实现小视频的录制功能               |
| `TXRecordCommon.java`    | 基本参数定义，包括了小视频录制回调及发布回调接口 |
| `TXUGCPartsManager.java` | 视频片段管理类，用于视频的多段录制，回删等    |
| `ITXVideoRecordListener.java` | 小视频录制回调                  |

### 1. 画面预览相关
TXUGCRecord（位于 TXUGCRecord.java） 负责小视频的录制功能，我们的第一个工作是先把预览功能实现。startCameraSimplePreview函数用于启动预览。由于启动预览要打开摄像头和麦克风，所以这里可能会有权限申请的提示窗。

```java
mTXCameraRecord = TXUGCRecord.getInstance(this.getApplicationContext());
mTXCameraRecord.setVideoRecordListener(this);					//设置录制回调
mVideoView = (TXCloudVideoView) findViewById(R.id.video_view);	//准备一个预览摄像头画面的 view
mVideoView.enableHardwareDecode(true);
TXRecordCommon.TXUGCSimpleConfig param = new TXRecordCommon.TXUGCSimpleConfig();
//param.videoQuality = TXRecordCommon.VIDEO_QUALITY_LOW;		// 360p
param.videoQuality = TXRecordCommon.VIDEO_QUALITY_MEDIUM;		// 540p
//param.videoQuality = TXRecordCommon.VIDEO_QUALITY_HIGH;		// 720p
param.isFront = true;           //是否前置摄像头，使用
param.minDuration = 5000;	//视频录制的最小时长ms
param.maxDuration = 60000;	//视频录制的最大时长ms
param.needEdit = false; // 录制完是否直接进入编辑界面编辑视频。false:生成指定参数的视频；true:生成高码率的视频，可快速进入编辑界面使用全部编辑功能
mTXCameraRecord.startCameraSimplePreview(param,mVideoView);

// 停止摄像头预览
stopCameraPreview();

// 切换视频录制分辨率
mTXCameraRecord.setVideoResolution(TXRecordCommon.VIDEO_RESOLUTION_540_960);

// 切换视频录制码率
mTXCameraRecord.setVideoBitrate(6500);

// 获取摄像头支持的最大焦距
mTXCameraRecord.getMaxZoom();

// 设置焦距
mTXCameraRecord.setZoom(value);

// 切换前后摄像头 参数 mFront 代表是否前置摄像头 默认前置
mTXCameraRecord.switchCamera(mFront);

// 是否打开闪光灯 参数 mFlashOn 代表是否打开闪关灯 默认关闭
mTXCameraRecord.toggleTorch(mFlashOn);

// 设置自定义图像处理回调
mTXCameraRecord.setVideoProcessListener(customProcessListener);
```

```java
VideoCustomProcessListener回调接口：
/**
  在OpenGL线程中回调，在这里可以进行采集图像的二次处理
  Parameters:
  textureId - 纹理ID
  width - 纹理的宽度
  height - 纹理的高度
  Returns:
  返回给SDK的纹理ID，如果不做任何处理，返回传入的纹理ID即可
  说明：SDK回调出来的纹理类型是GLES20.GL_TEXTURE_2D，接口返回给SDK的纹理类型也必须是GLES20.GL_TEXTURE_2D
*/
int onTextureCustomProcess(int textureId, int width, int height);

/**
  商业版回调人脸坐标
  Parameters:
  points - 归一化人脸坐标，每两个值表示某点P的X,Y值。值域[0.f,1.f]
*/
void onDetectFacePoints(float[] points);

/**
  在OpenGL线程中回调，可以在这里释放创建的OpenGL资源
*/
void onTextureDestroyed();
```

### 2. 画面截图

```java
// 截图/拍照，startCameraSimplePreview或者startCameraCustomPreview 之后调用有效
mTXCameraRecord.snapshot(new TXRecordCommon.ITXSnapshotListener() {
                @Override
                public void onSnapshot(Bitmap bmp) {
                    // 保存或者显示截图
                }
            });
```

### 3. 录制相关

```java
// 设置横竖屏录制
mTXCameraRecord.setHomeOrientation(TXLiveConstants.VIDEO_ANGLE_HOME_DOWN);

// 设置视频预览方向
mTXCameraRecord.setRenderRotation(TXLiveConstants.RENDER_ROTATION_PORTRAIT);

// 设置录制的宽高比
// TXRecordCommon.VIDEO_ASPECT_RATIO_9_16 宽高比为9:16
// TXRecordCommon.VIDEO_ASPECT_RATIO_3_4  宽高比为3:4
// TXRecordCommon.VIDEO_ASPECT_RATIO_1_1  宽高比为1:1
mTXCameraRecord.setAspectRatio(TXRecordCommon.VIDEO_ASPECT_RATIO_9_16);

// 设置视频录制速率
mTXCameraRecord.setRecordSpeed(TXRecordCommon.RECORD_SPEED_NORMAL);

// 设置麦克风的音量大小，播放背景音混音时使用，用来控制麦克风音量大小
// 音量大小,1为正常音量,建议值为0~2,如果需要调大音量可以设置更大的值.
mTXCameraRecord.setMicVolume(x);

// 设置录制是否静音 参数isMute代表是否静音，默认不静音
mTXCameraRecord.setMute(isMute);

// 开始录制
mTXCameraRecord.startRecord();

// 开始录制，可以指定输出视频文件地址和封面地址
mTXCameraRecord.startRecord(videoFilePath, coverPath)

// 开始录制,可以指定输出视频文件地址、封面地址、视频分片存储地址
mTXCameraRecord.startRecord(videoFilePath, videoPartFolder, coverPath);

// 暂停录制
mTXCameraRecord.pauseRecord();

// 继续录制
mTXCameraRecord.resumeRecord();

// 结束录制
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

### 4. 录制效果相关
在视频录制的过程中，您可以给录制视频的画面设置各种特效

```java
// 设置全局水印
//TXRect-水印相对于视频图像的归一化值，sdk内部会根据水印宽高比自动计算height
// 比如视频图像大小为（540，960） TXRect三个参数设置为0.1，0.1，0.1,
// 水印的实际像素坐标为（540 * 0.1，960 * 0.1，540 * 0.1 ，
// 540 * 0.1 * watermarkBitmap.height / watermarkBitmap.width）
mTXCameraRecord.setWatermark(watermarkBitmap, txRect)

// 设置美颜类型
mTXCameraRecord.setBeautyStyle(style);

// 设置美颜、美白、红润效果程度
mTXCameraRecord.setBeautyDepth(int style, int beautyDepth, int whiteningDepth, int ruddyDepth);

// 设置颜色滤镜：浪漫、清新、唯美、粉嫩、怀旧...
// filterBitmap     : 指定滤镜用的颜色查找表。注意：一定要用png格式！！！
// demo用到的滤镜查找表图片位于RTMPAndroidDemo/app/src/main/res/drawable-xxhdpi/目录下。
mTXCameraRecord.setFilter(filterBitmap);

// 设置组合滤镜特效
// mLeftBitmap      左侧滤镜
// leftIntensity   左侧滤镜程度
// mRightBitmap     右侧滤镜
// rightIntensity  右侧滤镜程度
// leftRadio       左侧图片占的比例大小
// 可以此接口实现滑动切换滤镜的效果，详见demo。
mTXCameraRecord.setFilter(mLeftBitmap, leftIntensity, mRightBitmap, rightIntensity, leftRatio);

// 用于设置滤镜的效果程度，从0到1，越大滤镜效果越明显，默认取值0.5
mTXCameraRecord.setSpecialRatio(0.5);

// 设置大眼效果 建议0~9，如果需要更明显可以设置更大值
mTXCameraRecord.setEyeScaleLevel(eyeScaleLevel);

// 设置瘦脸效果 建议0~9，如果需要更明显可以设置更大值
mTXCameraRecord.setFaceScaleLevel(faceScaleLevel);

// 设置V脸效果 建议0~9，如果需要更明显可以设置更大值
mTXCameraRecord.setFaceVLevel(level);

// 设置下巴拉伸或收缩效果 建议0~9，如果需要更明显可以设置更大值
mTXCameraRecord.setChinLevel(scale);

// 设置缩脸效果 建议0~9，如果需要更明显可以设置更大值
mTXCameraRecord.setFaceShortLevel(level);

// 设置小鼻效果 建议0~9，如果需要更明显可以设置更大值
mTXCameraRecord.setNoseSlimLevel(scale);

// 设置绿幕文件:目前图片支持jpg/png，视频支持mp4/3gp等Android系统支持的格式并支持循环播放
mTXCameraRecord.setGreenScreenFile(path, isLoop);

// 设置动效贴纸 motionTmplPath 动效文件路径： 空String "" 则取消动效
mTXCameraRecord.setMotionTmp(motionTmplPath);

// 设置动效贴纸是否静音: true: 动效贴纸静音；false：动效贴纸不静音
mTXCameraRecord.setMotionMute(true);
```

### 5. 录制BGM相关
在视频录制的过程中，您可以给视频的添加喜欢的BGM
```java
// 设置BGM路径
mTXCameraRecord.setBGM(path);

// 设置BGM播放回调 TXRecordCommon.ITXBGMNotify
mTXCameraRecord.setBGMNofify(notify);

// 播放BGM
mTXCameraRecord.playBGMFromTime(startTime, endTime)

// 停止播放BGM
mTXCameraRecord.stopBGM();

// 暂停播放BGM
mTXCameraRecord.pauseBGM();

// 继续播放BGM
mTXCameraRecord.resumeBGM();

// 设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小
// 音量大小,1为正常音量,建议值为0~2,如果需要调大背景音量可以设置更大的值.
mTXCameraRecord.setBGMVolume(x);

// 设置背景音乐播放的开始位置和结束位置
mTXCameraRecord.seekBGM(startTime, endTime);
```

### 6. 录制声音特效相关

```java
// 设置混响
// TXRecordCommon.VIDOE_REVERB_TYPE_0 关闭混响
// TXRecordCommon.VIDOE_REVERB_TYPE_1 KTV
// TXRecordCommon.VIDOE_REVERB_TYPE_2 小房间
// TXRecordCommon.VIDOE_REVERB_TYPE_3 大会堂
// TXRecordCommon.VIDOE_REVERB_TYPE_4 低沉
// TXRecordCommon.VIDOE_REVERB_TYPE_5 洪亮
// TXRecordCommon.VIDOE_REVERB_TYPE_6 金属声
// TXRecordCommon.VIDOE_REVERB_TYPE_7 磁性
mTXCameraRecord.setReverb(TXRecordCommon.VIDOE_REVERB_TYPE_1);

// 设置变声
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_0  关闭变声
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_1  熊孩子
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_2  萝莉
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_3  大叔
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_4  重金属
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_6  外国人
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_7  困兽
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_8  死肥仔
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_9  强电流
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_10 重机械
// TXRecordCommon.VIDOE_VOICECHANGER_TYPE_11 空灵
mTXCameraRecord.setVoiceChangerType(TXRecordCommon.VIDOE_VOICECHANGER_TYPE_1);

```
### 7. 多段录制及回删

```java
// 开始录制
mTXCameraRecord.startRecord();

// pauseRecord 后会生成一段视频，视频可以在 TXUGCPartsManager 里面获取 
mTXCameraRecord.pauseRecord();

// 继续录制视频
mTXCameraRecord.resumeRecord();

// 停止录制，将多段视频合成为一个视频输出
mTXCameraRecord.startRecord();

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

### 8. 文件预览

使用 [视频播放](https://cloud.tencent.com/document/product/584/9373) 即可预览刚才生成的 MP4 文件，需要在调用 startPlay 时指定播放类型为 [PLAY_TYPE_LOCAL_VIDEO](https://cloud.tencent.com/document/product/584/9373#step-3.3A-.E5.90.AF.E5.8A.A8.E6.92.AD.E6.94.BE.E5.99.A86) 。

### 9. 获取 license 信息
参考 [短视频license集成](https://cloud.tencent.com/document/product/584/11638)

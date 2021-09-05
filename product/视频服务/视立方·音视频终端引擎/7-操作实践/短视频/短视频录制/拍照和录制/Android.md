视频录制包括视频变速录制、美颜、滤镜、声音特效、背景音乐设置等功能。 

## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | &#10003;  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。


## 相关类介绍
| 类                     | 功能                                           |
| ---------------------- | ---------------------------------------------- |
| TXUGCRecord            | 实现视频的录制功能                             |
| TXUGCPartsManager      | 视频片段管理类，用于视频的多段录制，回删等     |
| ITXVideoRecordListener | 录制回调                                       |
| TXRecordCommon         | 基本参数定义，包括了视频录制回调及发布回调接口 |

## 使用说明

### 使用流程

视频录制的基本使用流程如下：
1. 配置录制参数。
2. 启动画面预览。
3. 设置录制效果。
4. 完成录制。

### 代码示例
```
// 创建一个用户相机预览的 TXCloudVideoView
mVideoView = (TXCloudVideoView) findViewById(R.id.video_view);
// 1、配置录制参数，已推荐配置 TXUGCSimpleConfig 为例
TXRecordCommon.TXUGCSimpleConfig param = new TXRecordCommon.TXUGCSimpleConfig();
param.videoQuality = TXRecordCommon.VIDEO_QUALITY_MEDIUM;
// 2、启动画面预览
mTXCameraRecord.startCameraSimplePreview(param, mVideoView);
// 3、设置录制效果，这里以添加水印为例
TXVideoEditConstants.TXRect rect = new TXVideoEditConstants.TXRect();
rect.x = 0.5f;
rect.y = 0.5f;
rect.width = 0.5f;
mTXCameraRecord.setWatermark(BitmapFactory.decodeResource(getResources(), R.drawable.watermark), rect);
// 4、开始录制
int result = mTXCameraRecord.startRecord();
if (result != TXRecordCommon.START_RECORD_OK) {
            if (result == -4) {画面还没出来} 
            else if (result == -3) {//版本太低}
	    else if (result == -5) {// licence 验证失败] }
            }
else{// 启动成功}
// 结束录制
mTXCameraRecord.stopRecord();
// 录制完成回调
public void onRecordComplete(TXRecordCommon.TXRecordResult result) {
	if (result.retCode >= 0 ) {
		// 录制成功， 视频文件在 result.videoPath 中
	}else{
		// 错误处理，错误码定义请参见 TXRecordCommon 中“录制结果回调错误码定义”
	}
}
```

## 画面预览
TXUGCRecord（位于 TXUGCRecord.java）负责小视频的录制功能，我们的第一个工作是先把预览功能实现。startCameraSimplePreview 函数用于启动预览。由于启动预览要打开摄像头和麦克风，所以这里可能会有权限申请的提示窗。

### 1. 启动预览
```
TXUGCRecord mTXCameraRecord = TXUGCRecord.getInstance(this.getApplicationContext());
mTXCameraRecord.setVideoRecordListener(this);					// 设置录制回调
mVideoView = (TXCloudVideoView) findViewById(R.id.video_view);	// 准备一个预览摄像头画面的
TXRecordCommon.TXUGCSimpleConfig param = new TXRecordCommon.TXUGCSimpleConfig();
//param.videoQuality = TXRecordCommon.VIDEO_QUALITY_LOW;		// 360p
//param.videoQuality = TXRecordCommon.VIDEO_QUALITY_MEDIUM;		// 540p
param.videoQuality = TXRecordCommon.VIDEO_QUALITY_HIGH;		// 720p
param.isFront = true;           // 是否使用前置摄像头
param.minDuration = 5000;	// 视频录制的最小时长 ms
param.maxDuration = 60000;	// 视频录制的最大时长 ms
param.touchFocus = false; // false 为自动聚焦；true 为手动聚焦
mTXCameraRecord.startCameraSimplePreview(param,mVideoView);

// 结束画面预览
mTXCameraRecord.stopCameraPreview();
```
### 2. 调整预览参数
在相机启动后，可以通过以下方法调整预览参数：
``` 
// 切换视频录制分辨率到540p
mTXCameraRecord.setVideoResolution(TXRecordCommon.VIDEO_RESOLUTION_540_960);

// 切换视频录制码率到6500Kbps
mTXCameraRecord.setVideoBitrate(6500);

// 获取摄像头支持的最大焦距
mTXCameraRecord.getMaxZoom();

// 设置焦距为3, 当为1的时候为最远视角（正常镜头），当为5的时候为最近视角（放大镜头）
mTXCameraRecord.setZoom(3);

// 切换到后置摄像头 true 切换到前置摄像头；false 切换到后置摄像头
mTXCameraRecord.switchCamera(false);

// 打开闪光灯 true 为打开， false 为关闭.
mTXCameraRecord.toggleTorch(false);

// param.touchFocus 为 true 时为手动聚焦，可以通过下面接口设置聚焦位置
mTXCameraRecord.setFocusPosition(eventX, eventY);

// 设置自定义图像处理回调
mTXCameraRecord.setVideoProcessListener(this);
```

## 拍照
在相机开启预览后，即可使用拍照的功能。

``` 
// 截图/拍照，startCameraSimplePreview 或者 startCameraCustomPreview 之后调用有效
mTXCameraRecord.snapshot(new TXRecordCommon.ITXSnapshotListener() {
                @Override
                public void onSnapshot(Bitmap bmp) {
                    // 保存或者显示截图
                }
            });
```

## 录制过程控制
录制的开始、暂停与恢复。
``` 
// 开始录制
mTXCameraRecord.startRecord();

// 开始录制，可以指定输出视频文件地址和封面地址
mTXCameraRecord.startRecord(videoFilePath, coverPath);

// 开始录制,可以指定输出视频文件地址、视频分片存储地址、封面地址
mTXCameraRecord.startRecord(videoFilePath, videoPartFolder, coverPath);

// 暂停录制
mTXCameraRecord.pauseRecord();

// 继续录制
mTXCameraRecord.resumeRecord();

// 结束录制
mTXCameraRecord.stopRecord();
```
录制的过程和结果是通过 TXRecordCommon.ITXVideoRecordListener（位于 TXRecordCommon.java 中定义）接口反馈：

- onRecordProgress 用于反馈录制的进度，参数 millisecond 表示录制时长，单位：毫秒。
``` 
@optional
void onRecordProgress(long milliSecond);
```

- onRecordComplete 反馈录制的结果，TXRecordResult 的 retCode 和 descMsg 字段分别表示错误码和错误描述信息，videoPath 表示录制完成的小视频文件路径，coverImage 为自动截取的小视频第一帧画面，便于在视频发布阶段使用。
```    
@optional
void onRecordComplete(TXRecordResult result);
```

- onRecordEvent 录制事件回调，包含事件id和事件相关的参数 `(key,value)` 格式。
```    
@optional
void onRecordEvent(final int event, final Bundle param);
```

## 录制属性设置
### 画面设置

``` 
// 设置横竖屏录制
mTXCameraRecord.setHomeOrientation(TXLiveConstants.VIDEO_ANGLE_HOME_RIGHT);

// 设置视频预览方向
// TXLiveConstants.RENDER_ROTATION_0(常规竖屏) 
// TXLiveConstants.RENDER_ROTATION_90(左旋90度) 
// TXLiveConstants.RENDER_ROTATION_180(左旋180度) 
// TXLiveConstants.RENDER_ROTATION_270(左旋270度) 
// 注意：需要在 startRecord 之前设置，录制过程中设置无效
mTXCameraRecord.setRenderRotation(TXLiveConstants.RENDER_ROTATION_PORTRAIT);

// 设置录制的宽高比
// TXRecordCommon.VIDEO_ASPECT_RATIO_9_16 宽高比为9:16
// TXRecordCommon.VIDEO_ASPECT_RATIO_3_4  宽高比为3:4
// TXRecordCommon.VIDEO_ASPECT_RATIO_1_1  宽高比为1:1
// 注意：需要在 startRecord 之前设置，录制过程中设置无效
mTXCameraRecord.setAspectRatio(TXRecordCommon.VIDEO_ASPECT_RATIO_9_16);
```

### 速度设置
``` 
// 设置视频录制速率
// TXRecordCommon.RECORD_SPEED_SLOWEST(极慢速) 
// TXRecordCommon.RECORD_SPEED_SLOW(慢速) 
// TXRecordCommon.RECORD_SPEED_NORMAL(标准) 
// TXRecordCommon.RECORD_SPEED_FAST(快速) 
// TXRecordCommon.RECORD_SPEED_FASTEST(极快速) 
mTXCameraRecord.setRecordSpeed(TXRecordCommon.VIDEO_RECORD_SPEED_NORMAL);
```
### 声音设置

``` 
// 设置麦克风的音量大小，播放背景音混音时使用，用来控制麦克风音量大小
// 音量大小,1为正常音量,建议值为0-2,如果需要调大音量可以设置更大的值.
mTXCameraRecord.setMicVolume(volume);
// 设置录制是否静音 参数 isMute 代表是否静音，默认不静音
mTXCameraRecord.setMute(isMute);
```

## 设置效果
在视频录制的过程中，您可以给录制视频的画面设置各种特效。
### 水印
``` 
// 设置全局水印
// TXRect-水印相对于视频图像的归一化值，sdk 内部会根据水印宽高比自动计算 height
// 例如视频图像大小为（540，960） TXRect 三个参数设置为0.1，0.1，0.1
// 水印的实际像素坐标为（540 * 0.1，960 * 0.1，540 * 0.1 ，
// 540 * 0.1 * watermarkBitmap.height / watermarkBitmap.width）
mTXCameraRecord.setWatermark(watermarkBitmap, txRect)
```
### 滤镜
``` 
// 设置颜色滤镜：浪漫、清新、唯美、粉嫩、怀旧...
// filterBitmap     : 指定滤镜用的颜色查找表。注意：一定要用 png 格式。
// demo 用到的滤镜查找表图片位于 RTMPAndroidDemo/app/src/main/res/drawable-xxhdpi/ 目录下。
mTXCameraRecord.setFilter(filterBitmap);

// 设置组合滤镜特效
// mLeftBitmap      左侧滤镜
// leftIntensity   左侧滤镜程度
// mRightBitmap     右侧滤镜
// rightIntensity  右侧滤镜程度
// leftRadio       左侧图片占的比例大小
// 可以此接口实现滑动切换滤镜的效果，详见 demo。
mTXCameraRecord.setFilter(mLeftBitmap, leftIntensity, mRightBitmap, rightIntensity, leftRatio);

// 用于设置滤镜的效果程度，从0到1，越大滤镜效果越明显，默认取值0.5
mTXCameraRecord.setSpecialRatio(0.5);
```

### 美颜

``` 
// 设置美颜类型
mTXCameraRecord.setBeautyStyle(style);

// 设置大眼效果 建议0-9，如果需要更明显可以设置更大值
mTXCameraRecord.setEyeScaleLevel(eyeScaleLevel);

// 设置瘦脸效果 建议0-9，如果需要更明显可以设置更大值
mTXCameraRecord.setFaceScaleLevel(faceScaleLevel);

// 设置V脸效果 建议0-9，如果需要更明显可以设置更大值
mTXCameraRecord.setFaceVLevel(level);

// 设置下巴拉伸或收缩效果 建议0-9，如果需要更明显可以设置更大值
mTXCameraRecord.setChinLevel(scale);

// 设置缩脸效果 建议0-9，如果需要更明显可以设置更大值
mTXCameraRecord.setFaceShortLevel(level);

// 设置小鼻效果 建议0-9，如果需要更明显可以设置更大值
mTXCameraRecord.setNoseSlimLevel(scale);

// 设置绿幕文件:目前图片支持 jpg/png，视频支持 mp4/3gp 等 Android 系统支持的格式并支持循环播放
mTXCameraRecord.setGreenScreenFile(path, isLoop);

// 设置动效贴纸 motionTmplPath 动效文件路径： 空 String "" 则取消动效
mTXCameraRecord.setMotionTmp(motionTmplPath);

// 设置动效贴纸是否静音: true: 动效贴纸静音；false：动效贴纸不静音
mTXCameraRecord.setMotionMute(true);
```

## 获取 License 信息
腾讯云视立方短视频 UGSV SDK 具备了短视频 License 的校验，如果校验没通过，您可以通过该接口来查询 License 中具体信息：

``` 
TXUGCBase.getInstance().getLicenceInfo(Context context);
```

## 高级功能

- [多段录制](https://cloud.tencent.com/document/product/1449/57029)
- [录制草稿箱](https://cloud.tencent.com/document/product/1449/57031)
- [添加背景音乐](https://cloud.tencent.com/document/product/1449/57037)
- [变声和混响](https://cloud.tencent.com/document/product/1449/57039)
- [定制视频数据](https://cloud.tencent.com/document/product/1449/57061)


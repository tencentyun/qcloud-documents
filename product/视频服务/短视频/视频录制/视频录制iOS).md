## 对接攻略
短视频录制即采集摄像头画面和麦克风声音，经过图像和声音处理后，进行编码压缩最终生成期望清晰度的 MP4 文件。
可以通过开发包中的 DEMO 工程体验录制的功能
![](https://main.qcloudimg.com/raw/4f8195d62fdb7e78ccd11609aad0c87d.png )
## 接口介绍 
腾讯云 UGC SDK 提供了相关接口用来实现短视频的录制，其详细定义如下：

|  接口文件 |  功能 |
| ------| --------|
| `TXUGCRecord.h` |小视频录制功能|
| `TXUGCRecordListener.h` | 小视频录制回调 |
| `TXUGCRecordEventDef.h` | 小视频录制事件回调 |
| `TXUGCRecordTypeDef.h` | 基本参数定义 |
| `TXUGCPartsManager.h` | 视频片段管理类，用于视频的多段录制，回删等 |

### 1. 画面预览相关
TXUGCRecord（位于 TXUGCRecord.h） 负责小视频的录制功能。startCamera 函数用于启动预览。由于启动预览要打开摄像头和麦克风，所以这里可能会有权限申请的提示窗。

```ObjectiveC
//开始画面预览
UIView *    preViewContainer;                    //准备一个预览摄像头画面的 view
TXUGCSimpleConfig *config = [[TXUGCSimpleConfig alloc] init];
//config.videoQuality = VIDEO_QUALITY_LOW;       // 360p, 10秒钟视频大约0.75M
config.videoQuality   = VIDEO_QUALITY_MEDIUM;    // 540p, 10秒钟视频大约 1.5M （编码参数同微信iOS版小视频）
//config.videoQuality = VIDEO_QUALITY_HIGH;      // 720p, 10秒钟视频大约   3M
config.frontCamera    = YES;                     //是否前置摄像头，使用 switchCamera 可以切换
config.minDuration    = 5;                       //视频录制的最小时长
config.maxDuration    = 60;                      //视频录制的最大时长
[TXUGCRecord shareInstance].recordDelegate = self; 
[[TXUGCRecord shareInstance] startCamera:param preview:preViewContainer];

//切换视频录制分辨率
[[TXUGCRecord shareInstance] setVideoResolution:VIDEO_RESOLUTION_540_960];

//切换视频录制码率
[[TXUGCRecord shareInstance] setVideoBitrate：2400];

//调整焦距
[[TXUGCRecord shareInstance] setZoom：distance];

//切换前后摄像头
[[TXUGCRecord shareInstance] switchCamera：YES];

//打开闪关灯
[[TXUGCRecord shareInstance] toggleTorch:YES];

//结束画面预览
[[TXUGCRecord shareInstance] stopCameraPreview];
```

### 2. 画面截图相关
```ObjectiveC
 //截图/拍照,startCamera 之后调用有效
 [[TXUGCRecord shareInstance] snapshot:^(UIImage *) {
        
 }];
```

### 3. 录制相关
短视频提供了丰富的录制自定义接口，您可以根据需求来进行设置。

```ObjectiveC
//设置横竖屏录制
[[TXUGCRecord shareInstance] setHomeOrientation:VIDOE_HOME_ORIENTATION_RIGHT];

//设置视频预览方向
[[TXUGCRecord shareInstance] setRenderRotation:rotation];

//设置视频录制比例：3：4  9：16  1：1
[[TXUGCRecord shareInstance] setAspectRatio:VIDEO_ASPECT_RATIO_9_16];

//设置视频录制速率
[[TXUGCRecord shareInstance] setRecordSpeed:VIDEO_RECORD_SPEED_NOMAL];

//设置录制是否静音
[[TXUGCRecord shareInstance] setMute:YES];

//开始录制
[[TXUGCRecord shareInstance] startRecord];

//开始录制,可以指定输出视频文件地址和封面地址
[[TXUGCRecord shareInstance] startRecord:videopath coverPath:coverPath];

//开始录制,可以指定输出视频文件地址、封面地址、视频分片存储地址
[[TXUGCRecord shareInstance] startRecord:videopath videoPartsFolder:videoPartsFolder coverPath:coverPath];

//暂停录制
[[TXUGCRecord shareInstance] pauseRecord];

//继续录制
[[TXUGCRecord shareInstance] resumeRecord];

//结束录制
[[TXUGCRecord shareInstance] stopRecord];
```

### 4. 录制效果相关
在视频录制的过程中，您可以给录制视频的画面设置各种特效

```ObjectiveC  
//设置全局水印
[[TXUGCRecord shareInstance] setWaterMark:watermark normalizationFrame:watermarkFrame];

//设置美颜和美白
[[TXUGCRecord shareInstance] setBeautyStyle:beautyStyle beautyLevel:beautyLevel whitenessLevel:whitenessLevel ruddinessLevel:ruddinessLevel];

//设置风格滤镜
[[TXUGCRecord shareInstance] setFilter:filterImage];

//设置风格滤镜效果程度
[[TXUGCRecord shareInstance] setSpecialRatio:0.5];

//设置大眼级别
[[TXUGCRecord shareInstance] setEyeScaleLevel:5];

//设置瘦脸级别
[[TXUGCRecord shareInstance] setFaceScaleLevel:5];

//设置V脸级别
[[TXUGCRecord shareInstance] setFaceVLevel:5];

//设置下巴拉伸或收缩
[[TXUGCRecord shareInstance] setChinLevel:5];

//设置短脸
[[TXUGCRecord shareInstance] setFaceShortLevel:5];

//设置瘦鼻
[[TXUGCRecord shareInstance] setNoseSlimLevel:5];

//设置绿幕文件
[[TXUGCRecord shareInstance] setGreenScreenFile:file];

//设置动效
[[TXUGCRecord shareInstance] selectMotionTmpl:tmplName inDir:tmplDir];

//设置动效静音
[[TXUGCRecord shareInstance] setMotionMute:YES];
```

### 4. 录制BGM相关
在视频录制的过程中，您可以给视频的添加喜欢的BGM  

```ObjectiveC 
// 设置BGM
[[TXUGCRecord shareInstance] setBGMAsset:_BGMPath];

// 设置BGM，从系统媒体库loading出来的音乐，可以直接传入对应的音乐属性，会极大的降低音乐从系统媒体库loading的时间
[[TXUGCRecord shareInstance] setBGMAsset:_BGMAsset];

// 播放BGM
- (BOOL)playBGMFromTime:(float)startTime
                 toTime:(float)endTime
        withBeginNotify:(void (^)(NSInteger errCode))beginNotify
     withProgressNotify:(void (^)(NSInteger progressMS, NSInteger durationMS))progressNotify
      andCompleteNotify:(void (^)(NSInteger errCode))completeNotify;

// 停止播放背景音乐
[[TXUGCRecord shareInstance] stopBGM];

// 暂停播放背景音乐
[[TXUGCRecord shareInstance] pauseBGM];

// 继续播放背景音乐
[[TXUGCRecord shareInstance] resumeBGM];

// 设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小
// volume: 音量大小，1为正常音量，建议值为0~2，如果需要调大音量可以设置更大的值
[[TXUGCRecord shareInstance] setMicVolume:1.0];

// setBGMVolume 设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小
// volume: 音量大小，1为正常音量，建议值为0~2，如果需要调大背景音量可以设置更大的值
[[TXUGCRecord shareInstance]setBGMVolume:1.0];
```
### 5. 录制声音特效相关
在视频录制的过程中，您可以给录制的声音设置各种特效 

```ObjectiveC 
// 设置混响效果
[[TXUGCRecord shareInstance] setReverbType:VIDOE_REVERB_TYPE_1];

// 设置变声类型
[[TXUGCRecord shareInstance] setVoiceChangerType:VIDOE_VOICECHANGER_TYPE_1];

```
    
### 6. 多段录制及回删  
在视频录制的过程中，您可以录制多段视频，并且管理这些视频，最终合成一个完整的视频

```ObjectiveC
// 开始录制
[[TXUGCRecord shareInstance] startRecord];

// 调用 pauseRecord 后会生成一段视频，视频可以在 TXUGCPartsManager 里面获取管理
[[TXUGCRecord shareInstance] pauseRecord];

// 继续录制视频
[[TXUGCRecord shareInstance] resumeRecord];

// 停止录制，将多段视频合成为一个视频输出
[[TXUGCRecord shareInstance] stopRecord];

//获取视频分片管理对象
@property (nonatomic, strong, readonly) TXUGCPartsManager *partsManager; 

//获取当前所有视频片段的总时长
[_partsManager getDuration];

//获取所有视频片段路径
[_partsManager getVideoPathList];

// 删除最后一段视频
[_partsManager deleteLastPart];

// 删除指定片段视频
[_partsManager deletePart:1];

// 删除所有片段视频
[_partsManager deleteAllParts];  

//合成所有片段视频
[_partsManager joinAllParts: videoOutputPath];
```

### 7. 文件预览
使用 [视频播放](https://cloud.tencent.com/document/product/584/9372) 即可预览刚才生成的 MP4 文件，需要在调用 startPlay 时指定播放类型为 [PLAY_TYPE_LOCAL_VIDEO](https://cloud.tencent.com/document/product/584/9372#step-3.3A-.E5.90.AF.E5.8A.A8.E6.92.AD.E6.94.BE6) 。

### 8. 获取 licence 信息
参考 [短视频licence集成](https://cloud.tencent.com/document/product/584/11638)

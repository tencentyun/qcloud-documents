## 对接攻略
短视频录制即采集摄像头画面和麦克风声音，经过图像和声音处理后，进行编码压缩最终生成期望清晰度的 MP4 文件。
可以通过开发包中的DEMO工程体验录制的功能
![](https://main.qcloudimg.com/raw/4f8195d62fdb7e78ccd11609aad0c87d.png )
## 接口介绍 
腾讯云 UGC SDK 提供了相关接口用来实现短视频的录制与发布，其详细定义如下：

|  接口文件 |  功能 |
| ------| --------|
| `TXUGCRecord.h` |实现小视频的录制功能|
| `TXUGCRecordListener.h` | 小视频录制回调及发布回调 |
| `TXUGCRecordEventDef.h` | 小视频录制事件回调 |
| `TXUGCRecordTypeDef.h` | 基本参数定义 |
| `TXUGCPartsManager.h` | 视频片段管理类，用于视频的多段录制，回删等 |

### 1. 画面预览
TXUGCRecord（位于 TXUGCRecord.h） 负责小视频的录制功能，我们的第一个工作是先把预览功能实现。startCamera 函数用于启动预览。由于启动预览要打开摄像头和麦克风，所以这里可能会有权限申请的提示窗。

```ObjectiveC
UIView *    preViewContainer;                    //准备一个预览摄像头画面的 view
TXUGCSimpleConfig *config = [[TXUGCSimpleConfig alloc] init];
//config.videoQuality = VIDEO_QUALITY_LOW;       // 360p, 10秒钟视频大约0.75M
config.videoQuality   = VIDEO_QUALITY_MEDIUM;    // 540p, 10秒钟视频大约 1.5M （编码参数同微信iOS版小视频）
//config.videoQuality = VIDEO_QUALITY_HIGH;      // 720p, 10秒钟视频大约   3M
config.frontCamera    = YES;                     //是否前置摄像头，使用 switchCamera 可以切换
config.minDuration    = 5;                       //视频录制的最小时长
config.maxDuration    = 60;                      //视频录制的最大时长
[TXUGCRecord shareInstance].delegate = self;     //self 实现了 TXVideoPublishListener 接口
[[TXUGCRecord shareInstance] startCamera:param preview:preViewContainer];
```

### 2. 画面特效
不管是录制前，还是录制中，您都可以使用 TXUGCRecord 里的特效开关来为视频画面添加一些特效，或者是对摄像头本身进行控制。

```ObjectiveC
//////////////////////////////////////////////////////////////////////////
                        以下为 1.9.1 版本后均支持的特效
//////////////////////////////////////////////////////////////////////////

// 设置视频录制比例：3：4  9：16  1：1
[[TXUGCRecord shareInstance] setAspectRatio:videoRatio];

// 设置全局水印
// waterMark            全局水印图片
// normalizationFrame   水印相对于视频图像的归一化frame
[[TXUGCRecord shareInstance] setWaterMark:waterMark  normalizationFrame:normalizationFrame];

// 切换前后摄像头 isFront:是否前置摄像头(默认前置)
[[TXUGCRecord shareInstance] switchCamera:YES];

// 设置美颜 和 美白 效果级别
// beautyDepth     : 美颜级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
// whiteningDepth  : 美白级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
[[TXUGCRecord shareInstance] setBeautyDepth: 7 WhiteningDepth: 1];

// 设置颜色滤镜:浪漫、清新、唯美、粉嫩、怀旧...
// image: 指定滤镜用的颜色查找表。注意：一定要用png格式！！！
// demo用到的滤镜查找表图片位于 RTMPiOSDemo/RTMPiOSDemo/resource/FilterResource.bundle中
   setSpecialRatio : 用于设置滤镜的效果程度，从0到1，越大滤镜效果越明显，默认取值0.5
[[TXUGCRecord shareInstance] setFilter: filterImage];
[[TXUGCRecord shareInstance] setSpecialRatio: 0.5];

// 是否打开闪光灯
[[TXUGCRecord shareInstance] toggleTorch: YES];

// 调整焦距 distance 1~5 ，当为1的时候为最远视角（正常镜头），当为5的时候为最近视角（放大镜头），这里最大值推荐为5，超过5后视频数据会变得模糊不清
[[TXUGCRecord shareInstance]setZoom:1.0];

//////////////////////////////////////////////////////////////////////////
//                             背景音相关
//////////////////////////////////////////////////////////////////////////
// 播放背景音
[[TXUGCRecord shareInstance] playBGM:path
    withBeginNotify:beginNotify
 withProgressNotify:progressNotify
  andCompleteNotify:completeNotify];

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

//////////////////////////////////////////////////////////////////////////
//                       以下为仅特权版才支持的特效
// （由于采用优图团队的知识产权，我们无法对外免费提供，需要使用特权版 SDK 才能支持）
//////////////////////////////////////////////////////////////////////////

// 设置大眼级别 0 ~ 9
[[TXUGCRecord shareInstance] setEyeScaleLevel: 0];

// 设置瘦脸级别 0 ~ 9
[[TXUGCRecord shareInstance] setFaceScaleLevel: 0];

// 设置V脸级别 0 ~ 9
[[TXUGCRecord shareInstance] setFaceVLevel:0];

// 设置下巴拉伸或收缩 -9 ~ 9 
[[TXUGCRecord shareInstance] setChinLevel:0];

// 设置短脸 0 ~ 9
[[TXUGCRecord shareInstance] setFaceShortLevel:0];

// 设置瘦鼻 0 ~ 9
[[TXUGCRecord shareInstance] setNoseSlimLevel:0];

// 设置动效贴纸 tmplName - 素材的名字   tmplDir - 素材包的路径
[[TXUGCRecord shareInstance] selectMotionTmpl: tmplName inDir：tmplDir];

// 设置绿幕效果 绿幕素材为宽高比 9:16 （比如 368*640、540*960、720 * 1280）的 MP4 文件
[[TXUGCRecord shareInstance] setGreenScreenFile: file]; 
```


### 3. 视频录制
调用 TXUGCRecord 的 startRecord 函数即可开始录制，调用 stopRecord 函数即可结束录制，startRecord 和 stopRecord 的调用一定要配对。

```ObjectiveC
[[TXUGCRecord shareInstance] startRecord];
[[TXUGCRecord shareInstance] stopRecord];
``` 

录制的过程和结果是通过 TXVideoRecordListener（位于 TXUGCRecordListener.h 头文件中定义）接口反馈出来的：

- onRecordProgress 用于反馈录制的进度，参数millisecond表示录制时长，单位毫秒:

```ObjectiveC
@optional
-(void) onRecordProgress:(NSInteger)milliSecond;
``` 

- onRecordComplete 反馈录制的结果，TXRecordResult 的 retCode 和 descMsg 字段分别表示错误码和错误描述信息，videoPath 表示录制完成的小视频文件路径，coverImage 为自动截取的小视频第一帧画面，便于在视频发布阶段使用。

```ObjectiveC   
@optional
-(void) onRecordComplete:(TXRecordResult*)result;
``` 
    
### 4. 多段视频录制及回删  
```ObjectiveC
 // pauseRecord 后会生成一段视频，视频可以在 TXUGCPartsManager 里面获取 
[[TXUGCRecord shareInstance] pauseRecord];

 // resumeRecord 会继续录制视频
[[TXUGCRecord shareInstance] resumeRecord];

//获取片段管理对象
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

### 5. 文件预览
使用 [视频播放](https://cloud.tencent.com/document/product/584/9372) 即可预览刚才生成的 MP4 文件，需要在调用 startPlay 时指定播放类型为 [PLAY_TYPE_LOCAL_VIDEO](https://cloud.tencent.com/document/product/584/9372#step-3.3A-.E5.90.AF.E5.8A.A8.E6.92.AD.E6.94.BE6) 。

### 6. 获取 licence 信息
新版本的SDK增加了短视频licence的校验，如果校验没通过，您可以通过该接口来查询licence中具体信息

``` 
NSString *licenceInfo = [[TXUGCRecord shareInstance] getLicenceInfo];
``` 
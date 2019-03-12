下面是腾讯视频云iOS SDK的主要接口列表，分为TXLivePush和TXLivePlayer两个类及相应的回调接口，详细接口请查看[API 接口文档](http://imgcache.qq.com/open/qcloud/video/act/liteav_ios_doc/index.html)。

## 接口概览

### TXLivePush

| 名称                                                 | 描述                         |
| ---------------------------------------------------- | --------------------------- |
| (id)initWithConfig:(TXLivePushConfig *)config;       | 设置推流配置信息              |
| (int)startPush:(NSString *)rtmpURL;                  | 启动到指定URL推流             |
| (void)stopPush;                                      | 停止推流                     |
| (void)pausePush;                                     | 暂停推流                     |
| (void)resumePush;                                    | 恢复推流                     |
| (bool)isPublishing;                                  | 是否正在推流中                |
| (int) startRecord:(NSString *)videoPath;             | 开始录制短视频                |
| (int) stopRecord                                     | 结束录制短视频                |
| (int)startPreview:(UIView *)view;                    | 开始推流画面的预览            |
| (void)stopPreview;                                   | 停止预览                     |
| (int)switchCamera;                                   | 切换前后摄像头                |
| (void)setMirror:(BOOL)isMirror                       | 设置是否为镜像画面            |
| (void)setBeautyStyle                                 | 设置美颜 和 美白 效果级别      |
| (void)setEyeScaleLevel:(float)eyeScaleLevel;         | 设置大眼级别                  |
| (void)setFaceScaleLevel:(float)faceScaleLevel;       | 设置瘦脸级别                  |
| (void)setFilter:(UIImage *)image;                    | 设置滤镜                      |
| (void)setSpecialRatio:(float)specialValue            |  设置滤镜效果程度             |
| (void)setFaceVLevel:(float)faceVLevel;               | 设置V脸                      |
| (void)setChinLevel:(float)chinLevel;                 | 设置下巴拉伸或收缩            |
| (void)setFaceShortLevel:(float)faceShortlevel;       | 设置瘦脸                     |
| (void)setNoseSlimLevel:(float)noseSlimLevel;         | 设置瘦鼻                     |
| (BOOL)toggleTorch:(BOOL)bEnable;                     | 打开或关闭闪光灯              |
| (void)setRenderRotation:(int)rotation;               | 设置本地视频方向              |
| (void)setMute:(BOOL)bEnable;                         | 设置静音                     |
| (void)sendCustomPCMData                              | 发送客户自定义的音频PCM数据    |
| (void)sendVideoSampleBuffer                          | 发送自定义的SampleBuffer      |
| (void)sendAudioSampleBuffer                          | 发送自定义音频包              |
| (void)setSendAudioSampleBufferMuted:(BOOL)muted;     | Replaykit发送静音包           |
| (void)setFocusPosition:(CGPoint)touchPoint;          |  调用手动对焦功能              |
| (void)setZoom:(CGFloat)distance;                     | 推送自定义视频数据             |
| (BOOL)playBGM:(NSString *)path;                      | 播放背景音乐                  |
| (BOOL)stopBGM;                                       | 停止播放背景音乐               |
| (BOOL)resumeBGM;                                     | 继续播放背景音乐               |
| (int)getMusicDuration:(NSString *)path;              | 获取音乐文件总时长，单位毫秒    |
| (BOOL)setMicVolume:(float)volume;                    | 设置麦克风的音量大小            |
| (BOOL)setBGMVolume:(float)volume;                    | 设置背景音乐的音量大小          |
| (BOOL)setBgmPitch:(float)pitch;                      | 设置背景音的变声类型            |
| (BOOL)setReverbType:(TXReverbType)reverbType;        | 设置混响效果, 详见 TXReverbType |
| (BOOL)setVoiceChangerType                            | 设置变声类型                   |
| (void)setGreenScreenFile:(NSURL *)file;              | 设置绿幕文件。仅增值版有效      |
| (void)selectMotionTmpl                               | 选择动效                       |
| (void)setLogViewMargin                               | 设置状态浮层view在渲染view上的边距 |
| (void)showVideoDebugLog                              | 是否显示播放状态统计及事件消息浮层view|
| (void)snapshot                                       | 推流截图.仅对硬编起效           |
| (BOOL)sendMessageEx                                  | 发送消息                       |

### TXLivePlayer

| 名称                                       | 描述                  |
| ---------------------------------------- | ---------------------- |
| setupVideoWidget                         | 创建Video渲染Widget     |
| removeVideoWidget                        | 移除Video渲染Widget     |
| setPlayListener                          | 设置TXLivePlayer 的回调 |
| startPlay                                | 开始播放                |
| stopPlay                                 | 停止播放                |
| pause                                    | 暂停播放                |
| resume                                   | 恢复播放                |
| prepareLiveSeek                          | 直播时移准备，拉取该直播流的起始播放时间    |
| resumeLive                               | 是否正在播放            |
| seek                                     | 跳转到音视频流某个时间   |
| width                                    | 视频宽度                |
| height                                   | 视频高度                |
| setRenderRotation                        | 设置画面的方向           |
| setRenderMode                            | 设置画面的裁剪模式       |
| setMute                                  | 设置静音                |
| startRecord                              | 开始录制短视频           |
| stopRecord                               | 结束录制短视频           |
| snapshot                                 | 通过回调返回当前图像     |
| setRate                                  | 设置播放速率。点播有效    |
| setLogViewMargin                         | 设置状态浮层view在渲染view上的边距    |
| showVideoDebugLog                        | 是否显示播放状态统计及事件消息浮层view |
| setAudioRoute                            | 设置声音播放模式(切换扬声器，听筒)     |
| switchStream                             | flv直播无缝切换           |

### TXLivePushConfig

| 属性名              | 类型                      | 说明                                           |
| --------           | ------------------------- | ---------------------------------------------  |
| customModeType          | int                     | 客户自定义模式 |
| beautyFilterDepth | float                    | 美颜强度 0 ~ 9, 默认值为0 |
| whiteningFilterDepth | float                 | 播美白强度:0 ~ 9, 默认值为0 |
| enableHWAcceleration | BOOL                  | 开启硬件加速, iOS系统版本>8.0 默认开启 |
| homeOrientation      | int                      |  home键所在方向，用来切换横竖屏推流（tips：此参数的设置可能会改变推流端本地视频流方向，此参数设置后，请调用TXLivePush 里的setRenderRotation 来修正推流端本地视频流方向，具体请参考demo设置 ）,默认值为HOME_ORIENTATION_DOWN |
| videoFPS             | int                        | 视频采集帧率, 默认值为 15 |
| enableAEC        | BOOL                        | 是否开启回声消除， 默认值为 NO                   |
| videoResolution    | int                        | 视频分辨率, 默认值为VIDEO_RESOLUTION_TYPE_360_640  |
| videoBitratePIN | int                          | 视频固定码率，默认值为700 |
| videoEncodeGop | int                          | 视频编码 GOP，单位 second 秒， 默认值为3 |
| audioSampleRate | int                          | 音频采样率 , 取值设置为 枚举值 TX_Enum_Type_AudioSampleRate，也可直接设置为对应的采样率 ，比如 audioSampleRate = AUDIO_SAMPLE_RATE_48000 或  audioSampleRate = 48000, 默认值为AUDIO_SAMPLE_RATE_48000 |
| audioChannels | int                          | 音频声道数, 默认值为1 |
| enableAutoBitrate | BOOL                          | 码率自适应: SDK会根据网络情况自动调节视频码率, 调节范围在 (videoBitrateMin - videoBitrateMax)， 默认值为NO |
| autoAdjustStrategy | int                          | 码率自适应: SDK会根据网络情况自动调节视频码率，同时自动调整分辨率, 默认值为AUTO_ADJUST_BITRATE_STRATEGY_1 |
| videoBitrateMax | int                          | 视频最大码率，仅当enableAutoBitrate = YES 时有效， 默认值为 1000 |
| videoBitrateMin | int                          | 视频最小码率，仅当enableAutoBitrate = YES时有效， 默认值为 400 |
| enableNAS | BOOL                          | 噪音抑制, 默认值为 YES |
| frontCamera | BOOL                          | 是否前置 camera, 默认值为 YES |
| touchFocus | BOOL                          | 是否允许点击曝光聚焦, 默认为 YES |
| enableZoom | BOOL                          | 是否允许双指手势放大预览画面，默认为 NO |
| connectRetryCount | int                          | 推流器连接重试次数 : 最小值为 1， 最大值为 10, 默认值为 3 |
| connectRetryInterval | int                          | 推流器连接重试间隔 : 单位秒，最小值为 3, 最大值为 30， 默认值为 3 |
| watermark     | UIImage *                          | 设置水印图片. 设为nil等同于关闭水印 |
| watermarkPos | CGPoint                          | 设置水印图片位置，水印大小为图片实际大小 |
| watermarkNormalization | CGRect                          | 水印相对于推流分辨率的归一化坐标，x,y,width,height 取值范围 0~1；height不用设置，sdk内部会根据水印宽高比自动计算height |
| pVideoFuncPtr | PVideoProcessHookFunc        | 视频预处理Hook       |
| pAudioFuncPtr | PAudioProcessHookFunc        | 音频预处理Hook       |
| sampleBufferSize | CGSize                    | 发送自定义 CMSampleBuffer 的输出分辨率。当设置此属性时，videoResolution 自动失效。此值设置需与源 SampleBuffer 的画面比例一致，否则会引起画面变形。调用 sendVideoSampleBuffer 必须设置此值，或者设置autoSampleBufferSize=YES |
| autoSampleBufferSize | BOOL                  | 设置 YES 时，调用 sendVideoSampleBuffer 输出分辨率等于输入分辨率, 默认值为 NO |
| enableAudioAcceleration | BOOL               | 开启音频硬件加速， 默认值为 YES |
| pauseTime               | int                | 后台推流时长，单位秒，默认 300 秒 |
| pauseFps | UIImage *                         | 后台推流图片, 图片最大尺寸不能超过 1920*1920 |
| enableAEC | BOOL                            |  是否开启回声消除, 默认值为 YES |
| enableAudioPreview | BOOL                   | 是否开启耳返, 默认值为 NO |
| enablePureAudioPush | BOOL                  | 是否纯音频推流, 默认值为 NO |
| enableNearestIP | BOOL                      | 是否就近选路， 默认值为 YES |
| rtmpChannelType | int                       | RTMP 传输通道的类型，取值为枚举值：TX_Enum_Type_RTMPChannel， 默认值为 RTMP_CHANNEL_TYPE_AUTO |

### TXLivePlayConfig

| 属性名              | 类型                      | 说明                                           |
| --------           | ------------------------- | ---------------------------------------------  |
| cacheTime          | float                     | 播放器缓存时间 : 单位秒，取值需要大于0, 默认值为5 |
| bAutoAdjustCacheTime | BOOL                    | 播放器缓存时间 : 单位秒，取值需要大于0, 默认值为5 |
| maxAutoAdjustCacheTime | float                 | 播放器缓存自动调整的最大时间 : 单位秒，取值需要大于0, 默认值为5 |
| minAutoAdjustCacheTime | float                 | 播放器缓存自动调整的最小时间 : 单位秒，取值需要大于0, 默认值为5 |
| videoBlockThreshold | int                      | 播放器视频卡顿报警阈值，只有渲染间隔超过这个阈值的卡顿才会有PLAY_WARNING_VIDEO_PLAY_LAG通知 |
| connectRetryCount | int                        | 播放器连接重试次数 : 最小值为 1， 最大值为 10, 默认值为 3 |
| enableAEC        | BOOL                        | 是否开启回声消除， 默认值为 NO                   |
| enableMessage    | BOOL                        | 是否开启消息通道， 默认值为 NO                   |
| playerPixelFormatType | OSType                 | 视频渲染对象回调的视频格式. 仅支持 kCVPixelFormatType_420YpCbCr8Planar和kCVPixelFormatType_420YpCbCr8BiPlanarFullRange, 默认值为kCVPixelFormatType_420YpCbCr8Planar |
| enableNearestIP | BOOL                         | 只对加速拉流生效，用于指定加速拉流是否开启就近选路 (当前版本不启用) |
| rtmpChannelType | int                          | RTMP传输通道的类型，取值为枚举值：TX_Enum_Type_RTMPChannel, 默认值为RTMP_CHANNEL_TYPE_AUTO |

## 接口详情

### TXLivePush

#### 1.initWithConfig

接口详情：`(id)initWithConfig:(TXLivePushConfig *)config`

init 时候初始化 config.

- **参数说明**

| 参数   | 类型                | 说明          |
| ------ | ------------------ | ------------ |
| config | TXLivePushConfig * | 推流器配置信息 |



#### 2.startPush

接口详情：`(int)startPush:(NSString *)rtmpURL`

启动到指定URL推流（rtmpURL 腾讯云的推流地址）

- **参数说明**

| 参数   | 类型                | 说明          |
| ------ | ------------------ | ------------ |
| url    | NSString *         | RTMP完整的URL |


- **返回值**
0 为 OK

#### 3.stopPush

接口详情：`(void)stopPush`

停止推流

#### 4.pausePush

接口详情：`(void)pausePush`

暂停推流，后台视频发送 TXLivePushConfig 里面设置的图像，音频会继续录制声音发送, 如果不需要录制声音，需要再调下 `setMute` 接口。

 * 当从前台切到后台的时候，调用 pausePush 会推配置里设置的图片(TXLivePushConfig.pauseImg)
 * 当从后台回到前台的时候，调用 resumePush 恢复推送 camera 采集的数据
 * 相关属性设置请参考 TXLivePushConfig：
 * pauseImg  设置后台推流的默认图片，不设置为默认黑色背景
 * pauseFps  设置后台推流帧率，最小值为 5，最大值为 20 ，默认 10
 * pauseTime 设置后台推流持续时长，单位秒，默认 300 秒

#### 5. isPublishing 

接口详情：`(bool)isPublishing`

是否正在推流中。YES 推流中，NO 没有推流

#### 6. startRecord                   

接口详情：`(int) startRecord:(NSString *)videoPath`

开始录制短视频，开始推流后才能启动录制
注意：
1. 录制过程中请勿动态切换分辨率和软硬编，可能导致生成的视频异常
2. 目前仅支持 Enterprise 和 Professional SDK版本，其他版本调用无效

注意：关闭摄像头是同步操作，正常会耗时100~200ms，在某些手机上耗时会多一些，如果觉得耗时有影响可以抛到异步线程调用该接口

- **参数说明**

| 参数                 | 类型      | 说明                                       |
| ------------------ | ---------- | ---------------------------------------- |
| videoPath          | NSString * | 视频录制后存储路径                          |

- **返回值**
*  0 成功；
* -1 videoPath 为nil；
* -2 上次录制未结束，请先stopRecord
* -3 推流未开始

#### 7. stopRecord

接口详情：`(int) stopRecord`

结束录制短视频，停止推流后，如果视频还在录制中，SDK内部会自动结束录制

- **返回值**
*  0 成功；
* -1 不存在录制任务；

#### 8.stopPreview

接口详情：`(void)stopPreview`

停止预览

#### 9.switchCamera

接口详情：`(int)switchCamera`

切换前后摄像头

#### 10.setMirror

接口详情：`(void)setMirror:(BOOL)isMirror`

isMirror YES：播放端看到的是镜像画面   NO：播放端看到的是非镜像画面

tips：推流端前置摄像头默认看到的是镜像画面，后置摄像头默认看到的是非镜像画面


#### 11.setBeautyStyle

接口详情：`(void)setBeautyStyle:(TX_Enum_Type_BeautyStyle)beautyStyle beautyLevel:(float)beautyLevel whitenessLevel:(float)whitenessLevel ruddinessLevel:(float)ruddinessLevel`

设置美颜和美白效果级别。

| 参数                 | 类型      | 说明                                      |
| ------------------ | ---------- | ----------------------------------------  |
| beautyStyle        |TX_Enum_Type_BeautyStyle |                              |
| beautyLevel        | float |美颜级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。|
| whitenessLevel     | float |美白级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。|
| ruddinessLevel     | float |红润级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。|

其中，TX_Enum_Type_BeautyStyle 如下

|  名称             |  值      |   说明    |
| ----------------- | ------- | --------  |
|BEAUTY_STYLE_SMOOTH | 0       |  光滑     |
|BEAUTY_STYLE_NATURE | 1       |  自然     |
|BEAUTY_STYLE_PITU   | 2       |  P 图美颜 |

#### 12.setEyeScaleLevel

接口详情：`(void)setEyeScaleLevel:(float)eyeScaleLevel`

设置大眼级别（特权版本有效，普通版本设置此参数无效）

| 参数              | 类型     | 说明                                     |
| ----------------- | ------- | ---------------------------------------- |
| eyeScaleLevel     | float | 大眼级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。|



#### 13.setFaceScaleLevel

接口详情：`(void)setFaceScaleLevel:(float)eyeScaleLevel`

设置瘦脸级别（特权版本有效，普通版本设置此参数无效）

| 参数              | 类型     | 说明                                     |
| ----------------- | ------- | ---------------------------------------- |
| faceScaleLevel    | float | 瘦脸级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。|




#### 14. setFilter

接口详情：`(void)setFilter:(UIImage *)image`

设置指定素材滤镜特效。


| 参数            | 类型     | 说明                                           |
| --------------- | -------- | --------------------------------------------- |
| image          | UIImage * | 指定素材，即颜色查找表图片。注意：一定要用png格式 |


#### 15.setSpecialRatio

接口详情：`(void)setSpecialRatio:(float)specialValue`

设置滤镜效果程度

| 参数            | 类型     | 说明                                           |
| --------------- | -------- | --------------------------------------------- |
| specialValue    | float    | 从 0 到 1，越大滤镜效果越明显，默认取值 0.5      |


#### 16.setFaceVLevel

接口详情：`(void)setFaceVLevel:(float)faceVLevel`

设置V脸（特权版本有效，普通版本设置此参数无效）

| 参数            | 类型     | 说明                                               |
| --------------- | -------- | ------------------------------------------------- |
| faceVLevel      | float    | 取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显   |


#### 17.setFaceShortLevel

接口详情：`(void)setChinLevel:(float)chinLevel`

设置下巴拉伸或收缩（特权版本有效，普通版本设置此参数无效）

| 参数      | 类型   | 说明                                                      |
| --------- | ----- | --------------------------------------------------------- |
| chinLevel | float | 下巴拉伸或收缩级别取值范围 -9 ~ 9； 0 表示关闭 -9收缩 ~ 9拉伸 |

#### 18.setFaceShortLevel

接口详情：`(void)setFaceShortLevel:(float)faceShortlevel`

设置短脸（特权版本有效，普通版本设置此参数无效）

| 参数      | 类型   | 说明                                                      |
| --------- | ----- | --------------------------------------------------------- |
| faceShortlevel | float | 短脸级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。  |



#### 19.setNoseSlimLevel

接口详情：`(void)setNoseSlimLevel:(float)noseSlimLevel`

设置瘦鼻（特权版本有效，普通版本设置此参数无效）

| 参数      | 类型   | 说明                                                      |
| --------- | ----- | --------------------------------------------------------- |
| noseSlimLevel | float | 瘦鼻级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。  |

#### 20.toggleTorch

接口详情：`(BOOL)toggleTorch:(BOOL)bEnable`

打开闪光灯

| 参数      | 类型   | 说明                                                      |
| --------- | ----- | --------------------------------------------------------- |
| bEnable  | BOOL  | YES 打开，NO 关闭                                           |

返回值

 * YES，打开成功。
 * NO，打开失败。

#### 21.setRenderRotation

接口详情：`(void)setRenderRotation:(int)rotation`

设置本地视频方向。

| 参数      | 类型   | 说明                                                      |
| --------- | ----- | --------------------------------------------------------- |
| rotation | int    | 取值为 0 , 90, 180, 270（其他值无效）表示推流端本地视频向右旋转的角度  |

#### 22.setMute

接口详情：`(void)setMute:(BOOL)bEnable`

设置静音。

#### 23.sendCustomPCMData

接口详情：`(void)sendCustomPCMData:(unsigned char *)data len:(unsigned int)len`

发送客户自定义的音频PCM数据。

说明：目前SDK只支持16位采样的PCM编码；如果是单声道，请保证传入的PCM长度为2048；如果是双声道，请保证传入的PCM长度为4096。

| 参数      | 类型   | 说明                                                      |
| --------- | ----- | --------------------------------------------------------- |
| data  | unsigned char *  | PCM 数据                                           |
| len   | unsigned int     | 数据的长度                                          |

#### 24.sendVideoSampleBuffer

接口详情：`(void)sendVideoSampleBuffer:(CMSampleBufferRef)sampleBuffer`

发送自定义的SampleBuffer，代替sendCustomVideoData。内部有简单的帧率控制，发太快会自动丢帧；超时则会重发最后一帧。

相关属性设置请参考TXLivePushConfig，autoSampleBufferSize优先级高于sampleBufferSize。

#### 25.sendAudioSampleBuffer

接口详情：`(void)sendAudioSampleBuffer:(CMSampleBufferRef)sampleBuffer withType:(RPSampleBufferType)sampleBufferType`

Replaykit发送自定义音频包。

- **参数说明**

| 参数           | 类型               | 说明                                         |
| ------------- | ------------------ | ---------------------------------------------- |
| sampleBuffer  | CMSampleBufferRef  | 声音                                           |
| sampleBufferType | RPSampleBufferType | RPSampleBufferTypeAudioApp or RPSampleBufferTypeAudioMic, 当两种声音都发送时，内部做混音；否则只发送一路声音 |


#### 26.setSendAudioSampleBufferMuted

接口详情： `(void)setSendAudioSampleBufferMuted:(BOOL)muted`

Replaykit发送静音包。


#### 27.setFocusPosition

接口详情： `(void)setFocusPosition:(CGPoint)touchPoint`

调用手动对焦功能。

说明: 早期SDK版本手动对焦功能是由SDK内部触发，现在把手动对焦的接口开放出来，客户可以根据自己需求触发, 如果客户调用这个接口，SDK内部触发对焦的逻辑将会停止，避免重复触发对焦逻辑。

| 参数       | 类型     | 说明           |
| --------- | -------  | ---------       |
| touchPoint | CGPoint | 传入的对焦点位置 |

#### 28.setZoom

接口详情：`(void)setZoom:(CGFloat)distance`

调整焦距。

- **参数说明**

| 参数       | 类型   | 说明                                                      |
| -------- | -----   | -------------------------------------------------------   |
| distance | CGFloat | distance取值范围 1~5 ，当为1的时候为最远视角（正常镜头），当为5的时候为最近视角（放大镜头），这里最大值推荐为5，超过5后视频数据会变得模糊不清 |



#### 29.playBGM

接口详情：`(BOOL)playBGM:(NSString *)path`

以下接口用于混音处理，背景音与 Mic 采集到的人声混合。

播放背景音乐。

- **参数说明**

| 参数       | 类型                  | 说明       |
| -------- | ---------------------- | ---------- |
| path     | NSString *             | 音乐文件路径，一定要是 app 对应的 document 目录下面的路径，否则文件会读取失败 |


#### 30. playBGM

接口详情：
```
(BOOL) playBGM:(NSString *)path
   withBeginNotify:(void (^)(NSInteger errCode))beginNotify
withProgressNotify:(void (^)(NSInteger progressMS, NSInteger durationMS))progressNotify
 andCompleteNotify:(void (^)(NSInteger errCode))completeNotify;
```
播放背景音乐。

| 参数        | 类型                    | 说明       |
| --------    | ---------------------- | ---------- |
| path        | NSString *             | 音乐文件路径，一定要是 app 对应的 document 目录下面的路径，否则文件会读取失败 |
| beginNotify | void (^)(NSInteger errCode))beginNotify | 音乐播放开始的回调通知 |
| withProgressNotify |  void (^)(NSInteger progressMS, NSInteger durationMS))progressNotify   | 音乐播放的进度通知，单位毫秒 |
| completeNotify | (void (^)(NSInteger errCode))completeNotify | 音乐播放结束的回调通知 |


#### 31.stopBGM

接口详情： `(BOOL)stopBGM`

停止播放背景音乐。

#### 32.pauseBGM

接口详情：`(BOOL)pauseBGM`

暂停播放背景音乐。

#### 33.resumeBGM

接口详情：`(BOOL)resumeBGM`

继续播放背景音乐。

#### 34.getMusicDuration

接口详情：`(int)getMusicDuration:(NSString *)path`

获取音乐文件总时长，单位毫秒。


| 参数       | 类型      | 说明                                                     |
| --------- | --------- | ----------------------------------------------------    |
| path      | NSString * | 音乐文件路径，如果path为空，那么返回当前正在播放的music时长 |

返回值：音乐文件总时长，单位为毫秒。

#### 35.setMicVolume

接口详情：`(BOOL)setMicVolume:(float)volume`

设置麦克风的音量大小，播放背景音乐混音时使用，用来控制麦克风音量大小。


| 参数       | 类型      | 说明                                                     |
| --------- | --------- | ----------------------------------------------------    |
| volume      | float    |  音量大小，1为正常音量，建议值为0~2，如果需要调大音量可以设置更大的值 |


#### 36.setBGMVolume

接口详情：`(BOOL)setBGMVolume:(float)volume`

设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小


| 参数       | 类型      | 说明                                                     |
| --------- | --------- | ----------------------------------------------------    |
| volume     | float   | 音量大小，1为正常音量，建议值为0~2，如果需要调大背景音量可以设置更大的值 |


#### 37.setBGMPitch

接口详情：`(BOOL)setBgmPitch:(float)pitch`

设置背景音的变声类型


| 参数       | 类型      | 说明                                                     |
| --------- | --------- | ----------------------------------------------------    |
| pitch     | float     | 默认值是0.f;范围是 [-1,1]                                 |


#### 38.setVideoQuality

接口详情：
```
(void)setVideoQuality:(TX_Enum_Type_VideoQuality)quality
          adjustBitrate:(BOOL) adjustBitrate
       adjustResolution:(BOOL) adjustResolution;

```

设置视频质量。


| 参数       | 类型      | 说明                                                     |
| --------- | --------- | ----------------------------------------------------     |
| quality   | TX_Enum_Type_VideoQuality  | 画质类型(标清，高清，超高清)              |
| adjustBitrate   | BOOL                 | 动态码率开关                             |
| adjustResolution | BOOL                | 动态切分辨率开关                         |


#### 39.setReverbType

接口详情：`(BOOL)setReverbType:(TXReverbType)reverbType`

设置混响效果。


| 参数       | 类型      | 说明                                                     |
| --------- | --------- | ----------------------------------------------------     |
| reverbType   | TXReverbType  | 混响类型 ，详见 TXReverbType                       |

TXRevbType:
```
typedef NS_ENUM(NSInteger, TXReverbType) {
    REVERB_TYPE_0         = 0,    //关闭混响
    REVERB_TYPE_1         = 1,    //KTV
    REVERB_TYPE_2         = 2,    //小房间
    REVERB_TYPE_3         = 3,    //大会堂
    REVERB_TYPE_4         = 4,    //低沉
    REVERB_TYPE_5         = 5,    //洪亮
    REVERB_TYPE_6         = 6,    //金属声
    REVERB_TYPE_7         = 7,    //磁性
};
```
#### 40.setVoiceChangerType

接口详情：`(BOOL)setVoiceChangerType:(TXVoiceChangerType)voiceChangerType`

设置变声类型。


| 参数       | 类型      | 说明                                                     |
| --------- | --------- | ----------------------------------------------------     |
| voiceChangerType   | TXVoiceChangerType  | 变声类型, 详见 TXVoiceChangerType      |

其中，TXVoiceChangerType定义如下：
```
typedef NS_ENUM(NSInteger, TXVoiceChangerType) {
    VOICECHANGER_TYPE_0   = 0,    //关闭变声
    VOICECHANGER_TYPE_1   = 1,    //熊孩子
    VOICECHANGER_TYPE_2   = 2,    //萝莉
    VOICECHANGER_TYPE_3   = 3,    //大叔
    VOICECHANGER_TYPE_4   = 4,    //重金属
    VOICECHANGER_TYPE_5   = 5,    //感冒
    VOICECHANGER_TYPE_6   = 6,    //外国人
    VOICECHANGER_TYPE_7   = 7,    //困兽
    VOICECHANGER_TYPE_8   = 8,    //死肥仔
    VOICECHANGER_TYPE_9   = 9,    //强电流
    VOICECHANGER_TYPE_10  = 10,   //重机械
    VOICECHANGER_TYPE_11  = 11,   //空灵
};
```

#### 41.setGreenScreenFile

接口详情：`(void)setGreenScreenFile:(NSURL *)file`

设置绿幕文件。仅增值版有效


| 参数       | 类型      | 说明                                                     |
| --------- | --------- | ----------------------------------------------------     |
| file      | NSURL *   |  绿幕文件路径。支持mp4; nil 关闭绿幕                        |



#### 42.selectMotionTmpl

接口详情：`(void)selectMotionTmpl:(NSString *)tmplName inDir:(NSString *)tmplDir`

选择动效。仅增值版有效


| 参数       | 类型      | 说明                                                     |
| --------- | --------- | ----------------------------------------------------     |
| tmplName  | NSString *  |  动效名称                                               |
| tmplDir   | NSString *  |  动效目录                                               |

#### 43.setLogViewMargin

接口详情：`(void)setLogViewMargin:(UIEdgeInsets)margin`

设置状态浮层view在渲染view上的边距


| 参数       | 类型      | 说明                                                     |
| --------- | --------- | ----------------------------------------------------     |
| margin  | UIEdgeInsets  |  状态浮层view在渲染view上的边距                          |

#### 44.showVideoDebugLog

接口详情：`(void)showVideoDebugLog:(BOOL)isShow`

是否显示播放状态统计及事件消息浮层view。


#### 45.snapshot

接口详情：`(void)snapshot:(void (^)(UIImage *))snapshotCompletionBlock`

推流截图，仅对硬编起效。

| 参数       | 类型      | 说明                                                     |
| --------- | --------- | ----------------------------------------------------     |
| snapshotCompletionBlock  | void (^)(UIImage *)  |  截图完成回调                   |


#### 46.sendMessageEx

接口详情：`(void)sendMessageEx:(NSData *) data`

发送消息(消息大小不允许超过2K），播放端通过 onPlayEvent(PLAY_EVT_GET_MESSAGE)接收。

该接口发送消息，能够解决旧的sendMessage接口会导致在iOS上无法播放对应的HLS流的问题。

| 参数       | 类型      | 说明                                                     |
| --------- | --------- | ----------------------------------------------------     |
| data      | NSData *  |  要发送的内容                                             |


### TXLivePlayer

#### 1. setupVideoWidget

接口详情：`(void)setupVideoWidget:(CGRect)frame containView:(UIView *)view insertIndex:(unsigned int)idx`

创建Video渲染Widget,该控件承载着视频内容的展示。

- **参数说明**

| 参数     | 类型             | 说明                |
| ------  | ---------------- | -------------       |
| frame   | CGRect           | Widget在父view中的rc |
| view    | UIView *         | 父view              |
| idx     | unsigned int     | Widget在父view上的层级位置 |


#### 2. removeVideoWidget

接口详情：`(void)removeVideoWidget`

移除Video渲染Widget。

#### 3. startPlay

接口详情：`(int)startPlay:(NSString *)url type:(TX_Enum_PlayType)playType`

启动从指定 URL 播放 RTMP 音视频流。

| 参数     | 类型             | 说明                |
| ------  | ---------------- | -------------       |
| url         | NSString *       | 完整的URL(如果播放的是本地视频文件，这里传本地视频文件的完整路径) |
| playType    | TX_Enum_PlayType | 播放类型   |

返回值：0 = OK



#### 4.stopPlay

接口详情：`(int)stopPlay`

停止播放音视频流。

返回：0 = OK

#### 5.isPlaying

接口详情：`(bool)isPlaying`

是否正在播放。

返回值：YES 为正在播放。


#### 6.pause

接口详情：`(void)pause`

点播场景是暂停播放。直播场景是没有暂停播放这说法，调用该方法意味这停止拉流。


#### 7.resume

接口详情：`(void)resume`

点播场景是从 pause 位置恢复播放。直播场景则是重新拉流。


#### 8.prepareLiveSeek

接口详情：`(int)prepareLiveSeek`

直播时移准备，拉取该直播流的起始播放时间。

使用时移功能需在播放开始后调用此方法，否则时移失败。时移的使用请参考文档 https://cloud.tencent.com/document/product/266/9237

非腾讯云直播地址不能时移。

* 返回值

| 返回值 | 含义        |
| ------ | ----------- |
|   0   |  ok         |
|  -1   | appID 未配置 |
|  -2   | 流 ID 格式错误 |


#### 9.resumeLive

接口详情：`(int)resumeLive`

停止时移播放，返回直播

返回 0 代表 ok。


#### 10.seek

接口详情： `(int)seek:(float)time`

点播流播放跳转到音视频流某个时间；直播流则时移到该位置。

- **参数说明**

| 参数   | 类型   | 说明                                       |
| ----  | ----   | ----------------------------------------   |
| time | float   | 时间，单位为秒                               |


#### 11.setRenderRotation

接口详情：`(void)setRenderRotation:(TX_Enum_Type_HomeOrientation)rotation`

设置画面的方向。

其中，TX_Enum_Type_HomeOrientation 的定义如下：
```
typedef NS_ENUM(NSInteger, TX_Enum_Type_HomeOrientation) {
    HOME_ORIENTATION_RIGHT  = 0,        // home在右边
    HOME_ORIENTATION_DOWN,              // home在下面
    HOME_ORIENTATION_LEFT,              // home在左边
    HOME_ORIENTATION_UP,                // home在上面
};
```

#### 12.setRenderMode

接口详情：`(void)setRenderMode:(TX_Enum_Type_RenderMode)renderMode`

- **参数说明**

| 参数         | 类型                    | 说明                                |
| ---------- | ------------------------- | ---------------------------------  |
| renderMode | TX_Enum_Type_RenderMode  |  详见 TX_Enum_Type_RenderMode 的定义 |

```
typedef NS_ENUM(NSInteger, TX_Enum_Type_RenderMode) {
    RENDER_MODE_FILL_SCREEN  = 0,    // 图像铺满屏幕
    RENDER_MODE_FILL_EDGE            // 图像长边填满屏幕
};
```

#### 13.setMute

接口详情：`(void)setMute:(BOOL)bEnable`

设置静音


#### 14.startRecord

接口详情：`(int) startRecord:(TXRecordType)recordType`

开始录制短视频。

- **参数说明**

| 参数       | 类型                                | 说明                 |
| -------- | ------------------------------------- | ------------------- |
| recordType | TXRecordType                        | 参见TXRecordType定义 |

TXRecordType 定义如下
```
typedef NS_ENUM(NSInteger, TXRecordType)
{
    RECORD_TYPE_STREAM_SOURCE = 1,            //视频源为正在播放的视频流
};
```

* 返回值

| 返回值 | 含义        |
| ------ | ----------- |
|   0   |  ok         |
|  -1   | 正在录制短视频 |
|  -2   | videoRecorder初始化失败 |

#### 15.stopRecord

接口详情：`(int) stopRecord`

结束录制短视频。

| 返回值 | 含义        |
| ------ | ----------- |
|   0   |  ok         |
|  -1   | 不存在录制任务 |
|  -2   | videoRecorder 没有初始化 |



#### 16. snapshot

接口详情：`(void)snapshot:(void (^)(UIImage *))snapshotCompletionBlock`

截屏。snapshotCompletionBlock 通过回调返回当前图像。



#### 17. setRate

接口详情：`(void)setRate:(float)rate`

设置播放速率。点播有效。

| 参数       | 类型                                | 说明                |
| --------  | ----------------------------------- | ------------------- |
| rate      | float                               | 1.0                 |



#### 18. setLogViewMargin

接口详情：`(void)setLogViewMargin:(UIEdgeInsets)margin`

设置状态浮层view在渲染view上的边距。



#### 19. showVideoDebugLog

接口详情：`(void)showVideoDebugLog:(BOOL)isShow`

是否显示播放状态统计及事件消息浮层view。


#### 20. setAudioRoute

接口详情：`(void)setAudioRoute:(TXAudioRouteType)audioRoute`

设置声音播放模式(切换扬声器，听筒)。

其中，TXAudioRouteType 定义如下：
```
typedef NS_ENUM(NSInteger, TXAudioRouteType) {
    AUDIO_ROUTE_SPEAKER    = 0,   //扬声器
    AUDIO_ROUTE_RECEIVER   = 1,   //听筒
};
```

#### 21. switchStream

接口详情：`(int)switchStream:(NSString *)playUrl`

flv 直播无缝切换。

| 参数       | 类型                                | 说明                |
| --------  | ----------------------------------- | ------------------- |
| playUrl   | NSString *                          | 播放地址             |

返回值：0 为 ok

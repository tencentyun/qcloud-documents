下面是腾讯视频云Android SDK的主要接口列表，分为TXLivePusher和TXLivePlayer两个类及相应的回调接口，详细接口请查看[API 接口文档](http://imgcache.qq.com/open/qcloud/video/act/liteav_android_doc/index.html)。


## TXLivePusher

##### API列表

| 名称                                       | 描述                                |
| ---------------------------------------- | --------------------------------- |
| setConfig(TXLivePushConfig config)       | 设置推流配置信息                          |
| getConfig()                              | 获取推流配置信息                          |
| setPushListener(ITXLivePushListener listener) | 设置推流事件状态回调                  |
| setVideoProcessListener(VideoCustomProcessListener listener) | 设置自定义视频处理回调 |
| startCameraPreview(TXCloudVideoView view) | 启动摄像头预览                           |
| stopCameraPreview(isNeedClearLastImg)    | 关闭摄像头预览                           |
| startPusher(String url)                  | 启动推流                              |
| stopPusher()                             | 停止推流                              |
| pausePusher()                            | 暂停推流                              |
| resumePusher()                           | 恢复推流                              |
| startScreenCapture()                     | 启动录屏                              |
| stopScreenCapture()                      | 结束录屏                              |
| setVideoQuality(quality, adjustBitrate, adjustResolution) | 设置推流视频质量，是否开启 Qos 流量控制， 是否允许动态分辨率 |
| setBeautyFilter(style, beautyLevel, whiteningLevel, ruddyLevel) | 设置美颜风格、磨皮程度、美白级别和红润级别             |
| setExposureCompensation()                | 调整曝光                            |
| setFilter()                              | 设置指定素材滤镜特效                |
| setChinLevel()                           | 设置下巴拉伸或收缩，企业版本有效    |
| setEyeScaleLevel()                       | 设置大眼级别，企业版本有效          |
| setFaceShortLevel()                      | 设置设置短脸，企业版本有效          |
| setFaceVLevel()                          | 设置V脸，企业版本有效               |
| setMotionTmpl()                          | 设置动效，企业版本有效              |
| setGreenScreenFile()                     | 设置绿幕文件，企业版本有效          |
| switchCamera()                           | 切换前后置摄像头，支持在推流中动态切换|
| setMute(mute)                            | 静音接口                              |
| setRenderRotation(rotation)              | 设置本地预览图像的顺时针旋转角度      |
| setMirror(enable)                        | 设置播放端水平镜像                    |
| playBGM(path)                            | 播放背景音乐，用于混音处理            |
| stopBGM()                                | 停止播放背景音乐                      |
| pauseBGM()                               | 暂停播放背景音乐                      |
| resumeBGM()                              | 继续播放背景音乐                      |
| getMusicDuration(path)                   | 获取音乐文件时长                      |
| setMicVolume()                           | 设置混音时麦克风的音量大小            |
| setBGMVolume()                           | 设置混音时背景音乐的音量大小          |
| setVoiceChangerType()                    | 设置变声类型                          |
| setReverb()                              | 设置推流端混响效果                    |
| startRecord(videoFilePath)               | 开始视频录制                            |
| stopRecord()                             | 停止视频录制                            |
| setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener) | 设置视频录制回调    |
| snapshot(ITXSnapshotListener)            |  截取视频画面                            |
| setAudioProcessListener(listener)                    | 设置自定义音频处理回调        |
| sendCustomVideoData(buffer, bufferType, w, h) | 推送自定义视频数据                   |
| sendCustomVideoTexture(textureID, w, h)  | 发送客户自定义的视频纹理                   |
| sendCustomPCMData(pcmBuffer)             | 推送自定义音频数据                         |
| sendMesageEx(byte[] msg)                 |  向播放端发送消息 (消息大小不允许超过2K）  |


## TXLivePushConfig

##### API列表

| 名称                                    | 描述                  |
| ------------------------------------- | ------------------- |
| enableAEC(enable)                     | 开启回声消除(连麦专用)        |
| enableNearestIP(enable)               | 开启就近选路              |
| enablePureAudioPush(enable)           | 开启纯音频推流             |
| enableScreenCaptureAutoRotate(enable) | 设置录屏是否自适应旋转         |
| setConnectRetryCount(count)           | 设置推流端重连次数           |
| setConnectRetryInterval(interval)     | 设置推流端重连间隔           |
| setEyeScaleLevel(level)               | 设置大眼效果              |
| setFaceSlimLevel(level)               | 设置瘦脸效果              |
| setFrontCamera(front)                 | 设置是否使用前置摄像头         |
| setHomeOrientation(homeOrientation)   | 设置采集的视频的旋转角度        |
| setPauseFlag(flag)                    | 设置后台推流,后台推流的选项      |
| setPauseImg(img)                      | 设置后台暂停,后台播放的暂停图片    |
| setPauseImg(time, fps)                | 设置推流暂停时,后台播放暂停图片的方式 |
| setVideoEncodeGop(gop)                | 设置视频编码GOP           |
| setVideoResolution(resolution)        | 设置视频分辨率              |
| setWatermark(watermark, x, y, width)  | 设置水印图片              |
| setWatermark(watermark, x,y)          | 设置水印图片              |


## TXLivePlayer

##### API列表

| 名称                                       | 描述                  |
| ---------------------------------------- | ------------------- |
| setConfig(TXLivePlayConfig config)       | 设置播放配置信息            |
| getConfig()                              | 获取播放配置信息            |
| setPlayerView(TXCloudVideoView view)     | 把渲染 view 绑定到 player |
| setPlayListener(ITXLivePlayListener listener) | 设置TXLivePlayer 的回调  |
| startPlay(url, type)                     | 开始播放                |
| stopPlay(isNeedClearLastImg)             | 停止播放                |
| pause()                                  | 暂停播放                |
| resume()                                 | 恢复播放                |
| prepareLiveSeek()                        | 直播时移准备，拉取该直播流的起始播放时间 |
| setAudioRoute(audioRoute)                | 设置声音播放模式(切换扬声器，听筒) |
| switchStream(playUrl)                    | flv直播无缝切换  |
| enableHardwareDecode(enable)             | 启用或禁用视频硬解码.         |
| isPlaying()                              | 是否正在播放              |
| setRenderMode(mode)                      | 设置图像的渲染（填充）模式       |
| setRenderRotation(rotation)              | 设置图像的顺时针旋转角度        |
| startRecord(recordType)                  | 开启截流录制              |
| stopRecord()                             | 停止截流录制              |
| setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener) | 设置视频录制回调  |
| setMute(mute)                            | 设置静音                |
| snapshot(TXLivePlayer.ITXSnapshotListener listener) | 截取视频图像              |
| setSurface(Surface surface)              | 设置渲染surface         |
| addVideoRawData(byte[] yuvBuffer)        | 设置播放yuv数据接收buffer   |
| setVideoRawDataListener(ITXVideoRawDataListener listener) | 设置视频yuv数据回调         |
| setAudioRawDataListener(ITXAudioRawDataListener listener) | 设置音频pcm数据回调         |


## TXLivePlayConfig

##### API列表

| 名称                                | 描述                    |
| --------------------------------- | --------------------- |
| enableAEC(enable)                 | 开启回声消除(连麦专用)          |
| setConnectRetryCount(count)       | 设置播放器重连次数             |
| setConnectRetryInterval(interval) | 设置播放器重连间隔             |
| setEnableMessage(enable)          | 设置消息通道是否打开            |
| setAutoAdjustCacheTime(bAuto)     | 设置是否根据网络状况自动调整播放器缓存时间 |
| setCacheTime(time)                | 设置播放器缓存时间             |
| setMaxAutoAdjustCacheTime(time)   | 设置自动调整时播放器最大缓存时间      |
| setMinAutoAdjustCacheTime(time)   | 设置自动调整时播放器最小缓存时间      |



## TXLivePusher接口详情

#### 1.setConfig(TXLivePushConfig config)

接口详情：void setConfig(TXLivePushConfig config)

设置推流器配置信息.

- **参数说明**

| 参数     | 类型                 | 说明      |
| ------ | ------------------ | ------- |
| config | TXLivePushConfig * | 推流器配置信息 |


- **示例代码** : 

```
TXLivePushConfig mLivePushConfig = new TXLivePushConfig();
mLivePushConfig.setBeautyFilter(...);
......
mLivePusher.setConfig(mLivePushConfig);
```



#### 2.getConfig() 

接口详情：TXLivePushConfig getConfig() 

获取推流配置信息 


- **示例代码** : 

```
mLivePusher.getConfig() 
```



#### 3.setPushListener(ITXLivePushListener listener) 

接口详情：void setPushListener(ITXLivePushListener listener)

设置推流事件状态回调 ，具体的事件及状态参看推流事件说明

- **参数说明**

| 参数       | 类型                  | 说明       |
| -------- | ------------------- | -------- |
| listener | ITXLivePushListener | 推流事件回调接口 |

- **示例代码** : 

```
mLivePusher.setPushListener(new ITXLivePushListener() {
    @Override
    public void onPushEvent(int i, Bundle bundle) {
        // ...
    }

    @Override
    public void onNetStatus(Bundle bundle) {
        // ...
    }
});
```



#### 4.setVideoProcessListener(VideoCustomProcessListener listener)

接口详情：void setVideoProcessListener(VideoCustomProcessListener listener)

设置自定义视频处理回调，在主播预览及编码前回调出来，用户可以用来做自定义美颜或者增加视频特效 

- **参数说明**

| 参数       | 类型                         | 说明        |
| -------- | -------------------------- | --------- |
| listener | VideoCustomProcessListener | 自定义视频处理回调 |

- **示例代码** : 

```
public interface VideoCustomProcessListener {

    /**
    * 增值版回调人脸坐标
    * @param points   归一化人脸坐标，每两个值表示某点P的X,Y值。值域[0.f, 1.f]
    */
    void onDetectFacePoints(float[] points);
    
    /**
    * 在OpenGL线程中回调，在这里可以进行采集图像的二次处理
    * @param textureId  纹理ID
    * @param width      纹理的宽度
    * @param height     纹理的高度
    * @return           返回给SDK的纹理
    * 说明：SDK回调出来的纹理类型是GLES20.GL_TEXTURE_2D，接口返回给SDK的纹理类型也必须是GLES20.GL_TEXTURE_2D
    */
    int onTextureCustomProcess(int textureId, int width, int height);

    /**
    * 在OpenGL线程中回调，可以在这里释放创建的OpenGL资源
    */
    void onTextureDestoryed();
}
```



#### 5. startCameraPreview(TXCloudVideoView view) 

接口详情：void startCameraPreview(TXCloudVideoView view) 

启动摄像头预览，默认是使用前置摄像头，可以通过TXLivePushConfig.setFrontCamera()设置。接口支持推流过程中切换不同的 TXCloudVideoView 。要先调用 stopCameraPreview()，再调用 startCameraPreview()

- **参数说明**

| 参数   | 类型               | 说明          |
| ---- | ---------------- | ----------- |
| view | TXCloudVideoView | 预览视频的渲染view |


- **示例代码** : 

```
TXCloudVideoView mCaptureView = (TXCloudVideoView) view.findViewById(R.id.video_view);
mLivePusher.startCameraPreview(mCaptureView);
```



#### 6. stopCameraPreview(isNeedClearLastImg)                                

接口详情：void stopCameraPreview(boolean isNeedClearLastImg)

关闭摄像头预览。可以保留或者清除最后一帧画面，如果停止预览后还留在推流页面建议保留，否则清除。

注意：关闭摄像头是同步操作，正常会耗时100~200ms，在某些手机上耗时会多一些，如果觉得耗时有影响可以抛到异步线程调用该接口

- **参数说明**

| 参数                 | 类型      | 说明                                       |
| ------------------ | ------- | ---------------------------------------- |
| isNeedClearLastImg | boolean | 是否需要清除最后一帧画面；true：清除最后一帧画面， false：保留最后一帧画面. |


- **示例代码** : 

```
mLivePusher.stopCameraPreview(true);
```



#### 7.startPusher(url)

接口详情：void startPusher(String url)

启动推流 (在 startPush 之前需要先 startCameraPreview 启动摄像头预览，否则数据无法推流上去)

注意推流 url 有排他性，也就是一个推流 Url 同时只能有一个推流端在推流


- **参数说明**

| 参数   | 类型           | 说明                                       |
| ---- | ------------ | ---------------------------------------- |
| url  | const String | 一个合法的推流地址，支持 rtmp 协议（URL 以 “rtmp://” 打头 ，腾讯云推流 URL 的获取方法见 [DOC]( https://cloud.tencent.com/document/product/454/7915 "腾讯云-推拉流地址Doc") ） |

- **示例代码** : 

```
mLivePusher.startPusher(rtmpUrl.trim());
```



#### 8.stopPusher()

接口详情：void stopPusher()

停止推流

- **示例代码** : 

```
mLivePusher.stopPusher();
```



#### 9.pausePusher()

接口详情：void pausePusher()

暂停摄像头推流。在正常推流中，如果App被切到后台，可以调用 pausePusher，这样SDK会停止采集摄像头的画面，同时会推送一个垫片和静音数据。该垫片可以通过 TXLivePushConfig.setPauseImg() 接口设置，如果没有设置则垫片是一个纯黑色画面。

- **示例代码** : 

```
mLivePusher.pausePusher();
```



#### 10.resumePusher()

接口详情：void resumePusher()

恢复摄像头推流。等App切回前台之后，调用 resumePusher，SDK 会停止推送垫片，继续采集摄像头的画面和麦克风声音，进行推流

- **示例代码** : 

```
mLivePusher.resumePusher();
```



#### 11.startScreenCapture()

接口详情：void startScreenCapture()

启动屏幕录制。由于录屏是基于 Android 系统的原生能力实现的，处于安全考虑，Android 系统会在开始录屏前弹出一个提示，旨在告诫用户：“有 App 要截取您屏幕上的所有内容”。

注意：该接口在Android API 21接口才生效。录屏接口和摄像头预览（startCameraPreview）互斥，同时只能由一个生效

- **示例代码** : 

```
mLivePusher.startScreenCapture();
```



#### 12.stopScreenCapture()

接口详情：void stopScreenCapture()

停止屏幕录制。

- **示例代码** : 

```
mLivePusher.stopScreenCapture();
```



#### 13.setVideoQuality(quality, adjustBitrate, adjustResolution) 

接口详情：void setVideoQuality(int quality,  boolean adjustBitrate,  boolean adjustResolution)

设定推流的画面清晰度。SDK 中提供了六种基础档位，根据主播的场景模式来选择相对应的模式。不同模式对应不同的分辨率和码率。根据我们服务大多数客户的经验进行积累和配置，我们找到分辨率和码率的最优的搭配，从而实现很好的画质效果。其中 STANDARD、HIGH、SUPER 适用于直播模式，MAIN_PUBLISHER 和 SUB_PUBLISHER 适用于连麦直播中的大小画面，VIDEOCHAT 用于实时音视频。

具体值如下：

- **参数说明**

| 参数               | 类型      | 说明       |
| ---------------- | ------- | -------- |
| quality          | int     | 画质档次     |
| adjustBitrate    | boolean | 动态码率开关   |
| adjustResolution | boolean | 动态切分辨率开关 |

- **画质档位说明**

| 档位       | 常量值                                      | 分辨率      | 视频码率     |
| -------- | ---------------------------------------- | -------- | -------- |
| STANDARD | TXLiveConstants.VIDEO_QUALITY_STANDARD_DEFINITION | 360*640  | 300~800  |
| HIGH     | TXLiveConstants.VIDEO_QUALITY_HIGH_DEFINITION | 540*960  | 600~1500 |
| SUPER    | TXLiveConstants.VIDEO_QUALITY_SUPER_DEFINITION | 720*1280 | 600~1800 |

- **示例代码** : 

```
mLivePusher.setVideoQuality(TXLiveConstants.VIDEO_QUALITY_HIGH_DEFINITION, true, true);;
```



#### 14. setBeautyFilter(style, beautyLevel, whiteningLevel, ruddyLevel)

接口详情：boolean setBeautyFilter(int style, int beautyLevel, int whiteningLevel, int ruddyLevel)

设置美颜风格、磨皮程度、美白级别和红润级别。

- **参数说明**

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| style          | int  | 磨皮风格：  0：光滑  1：自然  2：朦胧                  |
| beautyLevel    | int  | 磨皮等级： 取值为 0-9.取值为 0 时代表关闭美颜效果.默认值: 0,即关闭美颜效果 |
| whiteningLevel | int  | 美白等级： 取值为 0-9.取值为 0 时代表关闭美白效果.默认值: 0,即关闭美白效果 |
| ruddyLevel     | int  | 红润等级： 取值为 0-9.取值为 0 时代表关闭美白效果.默认值: 0,即关闭美白效果 |


- **示例代码** : 

```
mLivePusher.setBeautyFilter(mBeautyStyle, mBeautyLevel, mWhiteningLevel, mRuddyLevel);
```


#### 15. setExposureCompensation(float value)

接口详情：void setExposureCompensation(float value)

调整曝光

- **参数说明**

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| value           | float  | 曝光比例，表示该手机支持最大曝光调整值的比例，取值范围从-1到1。负数表示调低曝光，正数表示调高曝光， 0 表示不调整曝光  |

- **示例代码** : 

```
mLivePusher.setExposureCompensation(0.5f);
```



#### 16. setFilter()

接口详情：setFilter(Bitmap bmp)

设置指定素材滤镜特效

- **参数说明**

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| bmp           | Bitmap  | 指定素材，即颜色查找表图片。图片要求png 格式  |



- **示例代码** : 

```
mLivePusher.setFilter(bitmap);
```



#### 17. setChinLevel()

接口详情：setChinLevel(int chinLevel)

设置下巴拉伸或收缩（企业版本有效，普通版本设置此参数无效）

- **参数说明**

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| chinLevel      | int  | 下巴拉伸或收缩级别取值范围 -9 ~ 9； 0 表示关闭  |


- **示例代码** : 

```
mLivePusher.setChinLevel(0);
```


#### 18. setEyeScaleLevel()

接口详情：setEyeScaleLevel(int eyeScaleLevel)

设置大眼级别（企业版本有效，普通版本设置此参数无效）

- **参数说明**

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| eyeScaleLevel  | int  | 大眼级别取值范围 0 ~ 9； 0 表示关闭，值越大 效果越明显  |


- **示例代码** : 

```
mLivePusher.eyeScaleLevel(1);
```


#### 19. setFaceShortLevel()

接口详情：setFaceShortLevel(int faceShortlevel)

设置短脸级别（企业版本有效，普通版本设置此参数无效）

- **参数说明**

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| faceShortlevel  | int  | 短脸级别取值范围 0 ~ 9； 0 表示关闭，值越大 效果越明显  |


- **示例代码** : 

```
mLivePusher.setFaceShortLevel(1);
```



#### 20. setFaceVLevel()

接口详情：setFaceVLevel(int faceVLevel)

设置V脸级别（企业版本有效，普通版本设置此参数无效）

- **参数说明**

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| faceVLevel  | int  | V脸级别取值范围 0 ~ 9； 0 表示关闭，值越大 效果越明显  |


- **示例代码** : 

```
mLivePusher.setFaceVLevel(1);
```



#### 21. setMotionTmpl()

接口详情：setMotionTmpl(java.lang.String motionPath)

设置 P 图动效（企业版本有效，普通版本设置此参数无效）

- **参数说明**

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| motionPath     | String | 动效完整路径                           |

- **示例代码** : 

```
mLivePusher.setMotionTmpl(motionPath);
```


#### 22. setGreenScreenFile()

接口详情：setGreenScreenFile(java.lang.String file)

设置绿幕文件（企业版本有效，普通版本设置此参数无效）

- **参数说明**

| 参数             | 类型   | 说明                                       |
| -------------- | ---- | ---------------------------------------- |
| file     | String |  绿幕文件路径，支持 mp4 文件; null 表示关闭绿幕  |

- **示例代码** : 

```
mLivePusher.setGreenScreenFile(file);
```



#### 23.switchCamera()

接口详情：void switchCamera()

切换摄像头，前置摄像头时调用后变成后置，后置摄像头时调用后变成前置。该接口在启动预览startCameraPreview(TXCloudVideoView) 后调用才能生效，预览前调用无效。SDK启动预览默认使用前置摄像头。

- **示例代码** : 

```
mLivePusher.switchCamera();
```



#### 24.setMute(mute)

接口详情：void setMute(mute)

设置静音接口。设置为静音后SDK不再推送麦克风采集的声音，而是推送静音。

- **参数说明**

| 参数   | 类型      | 说明   |
| ---- | ------- | ---- |
| mute | boolean | 是否静音 |

- **示例代码** : 

```
mLivePusher.setMute(true);
```



#### 25.setRenderRotation(rotation)   

接口详情：void setRenderRotation(int rotation)   

设置本地预览图像的顺时针旋转角度。一般运用于横屏推流场景，结合 LivePushConfig.setHomeOrientation()  一起使用

- **参数说明**

| 参数       | 类型   | 说明          |
| -------- | ---- | ----------- |
| rotation | int  | 值一般为 0 和 90 |

- **示例代码** : 

```
// 竖屏状态，进行竖屏推流，本地渲染相对正方向的角度为 0
mLivePushConfig.setHomeOrientation(TXLiveConstants.VIDEO_ANGLE_HOME_DOWN);
mLivePusher.setRenderRotation(0);

// 横屏状态，进行横屏推流，本地渲染相对正方向的角度为 90
mLivePushConfig.setHomeOrientation(TXLiveConstants.VIDEO_ANGLE_HOME_RIGHT);
mLivePusher.setRenderRotation(90);
```



#### 26.setMirror(enable)  

接口详情：void setMirror(boolean enable)

设置播放端水平镜像。注意这个只影响播放端效果，不影响推流主播端。推流端看到的镜像效果是固定的，使用前置摄像头时推流端看到的是镜像画面，使用后置摄像头时推流端看到的是非镜像。

- **参数说明**

| 参数     | 类型      | 说明                                     |
| ------ | ------- | -------------------------------------- |
| enable | boolean | true 表示播放端看到的是镜像画面，false表示播放端看到的是非镜像画面 |

- **示例代码** : 

```
//观众端播放看到的是镜像画面
mLivePusher.setMirror(true);
```



#### 27.playBGM(path)

接口详情：boolean playBGM(String path)

播放背景音乐。该接口用于混音处理，比如将背景音乐与麦克风采集到的声音混合后播放。返回结果中，true 表示播放成功，false 表示播放失败。

- **参数说明**

| 参数   | 类型     | 说明               |
| ---- | ------ | ---------------- |
| path | String | 背景音乐文件位于手机中的绝对路径 |

- **示例代码** : 

```
mLivePusher.playBGM(musicFilePath);
```



#### 28.stopBGM()

接口详情：boolean stopBGM()

停止播放背景音乐。返回结果中，true 表示停止播放成功，false 表示停止播放失败。


- **示例代码** : 

```
mLivePusher.stopBGM();
```



#### 29.pauseBGM()

接口详情：boolean pauseBGM()

暂停播放背景音乐。返回结果中，true 表示暂停播放成功，false 表示暂停播放失败。


- **示例代码** : 

```
mLivePusher.pauseBGM();
```



#### 30.resumeBGM()

接口详情：boolean resumeBGM()

恢复播放背景音乐。返回结果中，true 表示恢复播放成功，false 表示恢复播放失败。


- **示例代码** : 

```
mLivePusher.resumeBGM();
```

#### 31.getMusicDuration(path)

接口详情：int getMusicDuration(java.lang.String path)

获取音乐文件时长，单位ms。

- **参数说明**

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| path   |音乐文件路径 | 如果 path == null ，获取当前播放歌曲时长。如果 path != null ，则获取path路径歌曲时长。|

- **示例代码** : 
```
mLivePusher.getMusicDuration(path);
```


#### 32.setMicVolume()

接口详情：boolean setMicVolume(float x)

设置混音时麦克风的音量大小。返回结果中，true 表示设置麦克风的音量成功，false 表示设置麦克风的音量失败。

- **参数说明**

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| x    | float | 音量大小，1为正常音量，建议值为0~2，如果需要调大音量可以设置更大的值。推荐在 UI 上实现相应的一个滑动条，由主播自己设置 |


- **示例代码** : 

```
mLivePusher.setMicVolume(2f);
```



#### 33.setBGMVolume()

接口详情：boolean setBGMVolume(float x)

设置混音时背景音乐的音量大小。返回结果中，true 表示设置背景音的音量成功，false 表示设置背景音的音量失败。

- **参数说明**

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| x    | float | 音量大小，1为正常音量，建议值为0~2，如果需要调大音量可以设置更大的值。推荐在 UI 上实现相应的一个滑动条，由主播自己设置 |


- **示例代码** : 

```
mLivePusher.setBGMVolume(2f);
```


#### 34.setVoiceChangerType()

接口详情：void setVoiceChangerType(int voiceChangerType)

设置设置变声类型。

- **参数说明**

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| voiceChangerType    | int | 变声类型 |


- **示例代码** : 

```
mLivePusher.setVoiceChangerType(1);
```


#### 35.setReverb()

接口详情：void setReverb(int reverbType)

设置推流端混响效果

- **参数说明**

| 参数   | 类型    | 说明                                       |
| ---- | ----- | ---------------------------------------- |
| setReverb    | int | 混响类型，设置推流端混响效果 |


- **示例代码** : 

```
mLivePusher.setReverb(TXLiveConstants.REVERB_TYPE_1);
```


#### 36.startRecord(videoFilePath)

接口详情： int startRecord(final String videoFilePath)

开始录制视频。该接口用于主播端将推流预览实时保存到本地文件。

注意：该接口需要在startpusher后调用，另外生成的视频文件由应用负责管理，SDK不做清理

接口返回 0 启动录制成功；-1 表示正在录制，忽略这次录制启动；-2 表示还未开始推流，这次启动录制失败

- **参数说明**

| 参数            | 类型     | 说明                               |
| ------------- | ------ | -------------------------------- |
| videoFilePath | String | 录制的视频文件位于手机中的绝对路径，调用者保证应用拥有该路径权限 |

- **示例代码** : 

```
String videoFile = Environment.getExternalStorageDirectory() + File.separator + "TXUGC/test.mp4";
mLivePusher.startRecord(videoFile);
```


#### 37.stopRecord()

接口详情： void stopRecord()

停止录制视频。录制结果会通过录制回调异步通知出来

- **示例代码** : 

```
mLivePusher.stopRecord();
```



#### 38.setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener)

接口详情：void setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener)

设置视频录制回调，用于接收视频录制进度及录制结果

- **参数说明**

| 参数       | 类型                                    | 说明     |
| -------- | ------------------------------------- | ------ |
| listener | TXRecordCommon.ITXVideoRecordListener | 视频录制回调 |

- **示例代码** : 

```
mLivePusher.setVideoRecordListener(new TXRecordCommon.ITXVideoRecordListener(){
    @Override
    public void onRecordEvent(int event, Bundle param) {
    }

    @Override
    public void onRecordProgress(long milliSecond) {
        Log.d(TAG, "record progress:" + milliSecond);
    }

    @Override
    public void onRecordComplete(TXRecordCommon.TXRecordResult result) {
        if (result.retCode == TXRecordCommon.RECORD_RESULT_OK) {
            String videoFile        = result.videoPath;
            String videoCoverPic    = result.coverPath;
        } else {
            Log.d(TAG, "record error:" + result.retCode + ", error msg:" + result.descMsg);
        }
    }
});
```



#### 39.snapshot(ITXSnapshotListener)

接口详情： void snapshot(final ITXSnapshotListener listener)

截取视频图像。该接口用于主播端实时截取一帧视频。

注意：截图结果会通过异步回调通知，回调线程是主线程

- **参数说明**

| 参数       | 类型                  | 说明       |
| -------- | ------------------- | -------- |
| listener | ITXSnapshotListener | 视频画面回调接口 |

- **示例代码** : 

```
mLivePusher.snapshot(new TXLivePusher.ITXSnapshotListener() {
    @Override
    public void onSnapshot(Bitmap bmp) {
        //bmp 一帧视频画面
    }
});
```

#### 40.setAudioProcessListener(listener)

接口详情：void setAudioProcessListener(TXLivePusher.AudioCustomProcessListener listener)

该接口设置自定义音频处理回调。数据回调时机是在音频数据送到编码器编码前。

- **示例代码** : 
```
mLivePusher.setAudioProcessListener(new TXLivePusher.AudioCustomProcessListener() {
    @Override
    public void onRecordPcmData(byte[] data, long ts, int sampleRate, int channels, int bits) {
       // data - pcm 数据
        // ts - pcm 对应时间戳
        // sampleRate - 音频采样率
        // channels - 音频通道
        // bits - 音频 bits
    }
});
```


#### 41.sendCustomVideoData(buffer, bufferType, w, h)

接口详情： int sendCustomVideoData(byte[] buffer, int bufferType, int w, int h)

该接口是向 SDK 塞入您自定义采集和处理后的视频数据（美颜、滤镜等），目前支持 i420 格式。该接口适用场景是只想使用我们 SDK 来 来编码和推流。调用该接口前提是，不再调用 TXLivePusher 的 startCameraPreview 接口。

返回结果的说明：

| 结果    | 说明                                       |
| ----- | ---------------------------------------- |
| >0    | 发送成功,但帧率过高,超过了TXLivePushConfig中设置的帧率,帧率过高会导致视频编码器输出的码率超过TXLivePushConfig中设置的码率,返回值表示当前YUV视频帧提前的毫秒数 |
| 0     | 发送成功                                     |
| -1    | 视频分辨率非法                                  |
| -2    | YUV数据长度与设置的视频分辨率所要求的长度不一致                |
| -3    | 视频格式非法                                   |
| -4    | 视频图像长宽不符合要求,画面比要求的小了                     |
| -1000 | SDK内部错误                                  |

- **参数说明**

| 参数         | 类型     | 说明                                       |
| ---------- | ------ | ---------------------------------------- |
| buffer     | byte[] | 视频数据                                     |
| bufferType | int    | 视频格式.目前只支持 TXLivePusher.YUV_420P和TXLivePusher.RGB_RGBA |
| w          | int    | 视频图像的宽度                                  |
| h          | int    | 视频图像的高度                                  |

- **示例代码** : 

```
//以下是简单的实例，获取摄像机预览回调的视频数据并推流
@Override
public void onPreviewFrame(byte[] data, Camera camera) {
    // 假设摄像机获取的视频格式是 NV21, 预览画面大小为 1280X720
    if (!isPush) {
    } else {
        // 开始自定义推流
        // 需要将视频格式转码为 I420
        byte[] buffer = new byte[data.length];
        buffer = nv21ToI420(data, mPreviewWidth, mPreviewHeight);

        int customModeType = 0;
        customModeType |= TXLiveConstants.CUSTOM_MODE_VIDEO_CAPTURE;
        // 只能分辨率的宽和高小于或者等于预览画面的宽和高的分辨率 
        // 还能选择 480x640 等，但不能选择 540x960。因指定分辨率的高(960) > 预览画面的高(720)，编码器无法裁剪画面。
        mLivePushConfig.setVideoResolution(TXLiveConstants.VIDEO_RESOLUTION_TYPE_1280_720);
        mLivePushConfig.setAutoAdjustBitrate(false);
        mLivePushConfig.setVideoBitrate(1200);
        mLivePushConfig.setVideoEncodeGop(3);
        mLivePushConfig.setVideoFPS(15);
        mLivePushConfig.setCustomModeType(customModeType);
        mLivePusher.setConfig(mLivePushConfig);

        int result= mLivePusher.sendCustomVideoData(buffer, TXLivePusher.YUV_420P, mPreviewWidth, mPreviewHeight);
    }
}

/**
 * nv21转I420
 * @param data
 * @param width
 * @param height
 * @return
 */
public static byte[] nv21ToI420(byte[] data, int width, int height) {
    byte[] ret = new byte[data.length];
    int total = width * height;

    ByteBuffer bufferY = ByteBuffer.wrap(ret, 0, total);
    ByteBuffer bufferU = ByteBuffer.wrap(ret, total, total / 4);
    ByteBuffer bufferV = ByteBuffer.wrap(ret, total + total / 4, total / 4);

    bufferY.put(data, 0, total);
    for (int i=total; i<data.length; i+=2) {
        bufferV.put(data[i]);
        bufferU.put(data[i+1]);
    }
    return ret;
}
```



#### 42.sendCustomVideoTexture(buffer, bufferType, w, h)

接口详情： int sendCustomVideoTexture(int textureID, int w, int h)

发送客户自定义的视频纹理。注意，1)该接口需要在OpenGL线程调用 2)必须使用硬件加速。

返回结果的说明：

| 结果    | 说明                                       |
| ----- | ---------------------------------------- |
| 0     | 发送成功                                     |
| -1    | 视频分辨率非法                               |
| -3    | 视频格式非法                                 |
| -4    | 视频图像长宽不符合要求,画面比要求的小了      |
| -1000 | SDK内部错误                                  |


- **参数说明**

| 参数         | 类型     | 说明                                 |
| ---------- | ------ | ---------------------------------------- |
| textureID  | int    | 视频纹理ID                               |
| w          | int    | 视频图像的宽度                           |
| h          | int    | 视频图像的高度                           |


- **示例代码** : 

```

```


#### 43. sendCustomPCMData(pcmBuffer)

接口详情：void sendCustomPCMData(byte[] pcmBuffer)

该接口是向 SDK 塞入您自定义采集和处理后的音频数据，请使用单声道或双声道、16位宽、48000Hz 的 PCM 声音数据。如果是单声道,请保证传入的PCM长度为2048；如果是双声道,请保证传入的PCM长度为4096。该接口一般结合 sendCustomVideoData(buffer, bufferType, w, h) 一起使用


- **参数说明**

| 参数        | 类型     | 说明       |
| --------- | ------ | -------- |
| pcmBuffer | byte[] | pcm 音频数据 |

- **示例代码** : 

```
//以下是简单的实例，获取麦克风采集音频数据。
AudioRecord mAudioRecord = null;
int mMinBufferSize = 0; //最小缓冲区大小

private static final int DEFAULT_SOURCE = MediaRecorder.AudioSource.MIC;
// 设置采样率为 48000
private static final int DEFAULT_SAMPLE_RATE = 48000;
// 支持单声道(CHANNEL_IN_MONO) 和 双声道(CHANNEL_IN_STEREO)
private static final int DEFAULT_CHANNEL_CONFIG = AudioFormat.CHANNEL_IN_STEREO;  
// 量化位数
private static final int DEFAULT_AUDIO_FORMAT = AudioFormat.ENCODING_PCM_16BIT;    

private boolean mIsCaptureStarted = false;
private volatile boolean mIsLoopExit = true;

private Thread mCaptureThread;
private OnAudioFrameCapturedListener mAudioFrameCapturedListener;

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);

    // 启动音频采集
    startCapture();
}

public interface OnAudioFrameCapturedListener {
    public void onAudioFrameCaptured(byte[] audioData);
}

public boolean isCaptureStarted() {
    return mIsCaptureStarted;
}

public void setOnAudioFrameCapturedListener(OnAudioFrameCapturedListener listener) {
    mAudioFrameCapturedListener = listener;
}

public boolean startCapture() {
    return startCapture(DEFAULT_SOURCE, DEFAULT_SAMPLE_RATE, DEFAULT_CHANNEL_CONFIG,
            DEFAULT_AUDIO_FORMAT);
}

public boolean startCapture(int audioSource, int sampleRateInHz, int channelConfig, int audioFormat) {

    if (mIsCaptureStarted) {
        Log.e(TAG, "audio Capture already started !");
        return false;
    }

    // SDK 要求双声道要 4096, 单声道 2048
    mMinBufferSize = 4096;
    if (mMinBufferSize == AudioRecord.ERROR_BAD_VALUE) {
        Log.e(TAG, "Invalid AudioRecord parameter !");
        return false;
    }
    Log.d(TAG , "getMinBufferSize = "+mMinBufferSize+" bytes !");

    mAudioRecord = new AudioRecord(audioSource,sampleRateInHz,channelConfig,audioFormat,mMinBufferSize);
    if (mAudioRecord.getState() == AudioRecord.STATE_UNINITIALIZED) {
        Log.e(TAG, "AudioRecord initialize fail !");
        return false;
    }

    mAudioRecord.startRecording();

    mIsLoopExit = false;
    mCaptureThread = new Thread(new AudioCaptureRunnable());
    mCaptureThread.start();

    mIsCaptureStarted = true;
    Log.d(TAG, "Start audio capture success !");

    return true;
}

public void stopCapture() {
    if (!mIsCaptureStarted) {
        return;
    }

    mIsLoopExit = true;
    try {
        mCaptureThread.interrupt();
        mCaptureThread.join(1000);
    } catch (InterruptedException e) {
        e.printStackTrace();
    }

    if (mAudioRecord.getRecordingState() == AudioRecord.RECORDSTATE_RECORDING) {
        mAudioRecord.stop();
    }

    mAudioRecord.release();

    mIsCaptureStarted = false;
    mAudioFrameCapturedListener = null;

    Log.d(TAG, "Stop audio capture success !");
}

private class AudioCaptureRunnable implements Runnable {
    @Override
    public void run() {
        while (!mIsLoopExit) {
                
            byte[] buffer = new byte[mMinBufferSize];

            int ret = mAudioRecord.read(buffer, 0, mMinBufferSize);
            if (ret == AudioRecord.ERROR_INVALID_OPERATION) {
                Log.e(TAG , "AudioRecord Error ERROR_INVALID_OPERATION");
            } else if (ret == AudioRecord.ERROR_BAD_VALUE) {
                Log.e(TAG , "AudioRecord Error ERROR_BAD_VALUE");
            } else {
                if (mAudioFrameCapturedListener != null) {
                    mAudioFrameCapturedListener.onAudioFrameCaptured(buffer);
                }
                if (isPush) {
                    mLivePusher.sendCustomPCMData(buffer);
                }
            }
            SystemClock.sleep(10);
        }
    }
}
```

#### 44. sendMessageEx(byte[] msg)

接口详情：void sendMessageEx(byte[] msg)

该接口用于向音视频流中塞入自定义的音视频数据，数据被伪装在 SEI 解码器信息中，几乎所有的播放器都不会主动解析 SEI 信息，所以这种在音视频流塞“私货”的方案是非常安全的，但是需要TXLivePlayer才能解读这些信息，具体方法请参考[DOC](https://cloud.tencent.com/document/product/454/7886#Message)

- **参数说明**

| 参数        | 类型     | 说明       |
| --------- | ------ | -------- |
| msg | byte[] | 在音视频流中塞入自定义数据 |



## TXLivePushConfig接口详情

#### 1. enableAEC(enable)

接口详情：void enableAEC(boolean enable)

开启回声消除。连麦时必须开启，非连麦正常推流时不要开启。默认关闭

- **参数说明**

| 参数     |   类型    | 说明                               |
| ------ | :-----: | -------------------------------- |
| enable | boolean | true 表示开启，false 表示关闭，默认值为 false。 |


- **示例代码** : 

```
mLivePushConfig.enableAEC(true);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



#### 2. enableNearestIP(enable)

接口详情：void enableNearestIP(boolean enable)

开启就近选路。我们 SDK 不绑定腾讯云，如果要推流到非腾讯云地址或者海外推流，请在推流前设置 TXLivePushConfig 中的 enableNearestIP 设置为 false。但如果您要推流的地址为腾讯云地址，可以不用设置。

- **参数说明**

| 参数     |   类型    | 说明                              |
| ------ | :-----: | ------------------------------- |
| enable | boolean | true 表示开启，false 表示关闭，默认值为 true。 |


- **示例代码** : 

```
mLivePushConfig.enableNearestIP(true);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



#### 3. enablePureAudioPush(enable)

接口详情：void enablePureAudioPush(boolean enable)

开启纯音频推流。该接口只有在推流启动前设置启动纯音频推流才会生效，推流过程中设置不会生效。

- **参数说明**

| 参数     |   类型    | 说明                               |
| ------ | :-----: | -------------------------------- |
| enable | boolean | true 表示开启，false 表示关闭。默认值为 false。 |


- **示例代码** : 

```
mLivePushConfig.enablePureAudioPush(true);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



#### 4. enableScreenCaptureAutoRotate(enable)

接口详情：void enableScreenCaptureAutoRotate(boolean enable)

设置录屏是否自适应旋转。该接口只对录屏生效

- **参数说明**

| 参数     |   类型    | 说明                                       |
| ------ | :-----: | ---------------------------------------- |
| enable | boolean | true 表示开启，视频内容为根据屏幕旋转后最大化显示；false 表示关闭，视频内容为屏幕内容缩放居中显示。默认值为 true。 |


- **示例代码** : 

```
mLivePushConfig.enableScreenCaptureAutoRotate(true);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



#### 5. setConnectRetryCount(count)

接口详情：void setConnectRetryCount(int count)

设置推流端重连次数。当SDK与服务器异常断开连接时,SDK会尝试与服务器重连，通过此函数设置SDK重连次数。一般结合 setConnectRetryInterval 一起使用

- **参数说明**

| 参数    |  类型  | 说明                             |
| ----- | :--: | ------------------------------ |
| count | int  | SDK重连次数，最小值为 1， 最大值为 10，默认值为 3 |


- **示例代码** : 

```
mLivePushConfig.setConnectRetryCount(5);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



#### 6. setConnectRetryInterval(interval)

接口详情：void setConnectRetryInterval(int  interval)

设置推流端重连间隔。当SDK与服务器异常断开连接时,SDK会尝试与服务器重连。通过此函数来设置两次重连间隔时间。一般结合 setConnectRetryCount 一起使用

- **参数说明**

| 参数       |  类型  | 说明                                 |
| -------- | :--: | ---------------------------------- |
| interval | int  | SDK重连间隔，单位秒。最小值为 3，最大值为 30， 默认值为 3 |


- **示例代码** : 

```
mLivePushConfig.setConnectRetryInterval(10);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



#### 7. setEyeScaleLevel(level)

接口详情：void setEyeScaleLevel(int level)

设置大眼效果。[商用企业版](https://cloud.tencent.com/document/product/454/7873#Android) 调用该接口才能生效。

- **参数说明**

| 参数    |  类型  | 说明                              |
| ----- | :--: | ------------------------------- |
| level | int  | 大眼等级取值为0-9。取值为 0 表示关闭大眼效果。默认值:0 |


- **示例代码** : 

```
mLivePushConfig.setEyeScaleLevel(1);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



#### 8. setFaceSlimLevel(level)

接口详情：void setFaceSlimLevel(int level)

设置瘦脸效果。[商用企业版](https://cloud.tencent.com/document/product/454/7873#Android) 调用该接口才能生效。

- **参数说明**

| 参数    |  类型  | 说明                             |
| ----- | :--: | ------------------------------ |
| level | int  | 瘦脸等级取值为0-9。取值为0时代表关闭瘦脸效果。默认值：0 |


- **示例代码** : 

```
mLivePushConfig.setFaceSlimLevel(1);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



#### 9. setFrontCamera(front)

接口详情：void setFrontCamera(boolean front)

设置是否使用前置摄像头。默认使用前置摄像头

- **参数说明**

| 参数    |   类型    | 说明                                       |
| ----- | :-----: | ---------------------------------------- |
| front | boolean | true 表示使用前置摄像头， false表示使用后置摄像头，默认值:false |


- **示例代码** : 

```
mLivePushConfig.setFrontCamera(true);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



#### 10. setHomeOrientation(homeOrientation)

接口详情：void setHomeOrientation(int homeOrientation)

设置采集的视频的旋转角度。该接口主要运用在横屏推流场景，一般结合 TXLivePusher.setRenderRotation(rotation) 一起使用。

- **参数说明**

| 参数              |  类型  | 说明                                       |
| --------------- | :--: | ---------------------------------------- |
| homeOrientation | int  | 采集的视频的旋转角度，具体值参考 TXLiveConstants 中 **视频旋转角度** 的定义 |

- **示例代码** : 

```
// 竖屏状态, 手机 Home 键在正下方。   旋转 0 度
mLivePushConfig.setHomeOrientation(TXLiveConstants.VIDEO_ANGLE_HOME_DOWN); 
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
// 竖屏状态，本地渲染相对正方向的角度为0。
mLivePusher.setRenderRotation(0);


// 横屏状态，手机 Home 键在右手方。   旋转 270 度
mLivePushConfig.setHomeOrientation(TXLiveConstants.VIDEO_ANGLE_HOME_RIGHT);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
// 横屏状态，本地渲染相对正方向的角度为90。
mLivePusher.setRenderRotation(90);
```



#### 11. setPauseFlag(flag)

接口详情：void setPauseFlag(int flag)

设置推流暂停时，设置是否停止视频采集或者停止音频采集。一般运用在后台推流场景。建议结合 setPauseImg() 一起使用

- **参数说明**

| 参数   |  类型  | 说明                                       |
| ---- | :--: | ---------------------------------------- |
| flag | int  | 暂停推流时，按照flag选项推流，具体值参考 TXLiveConstants 中 **后台推流选项** 的定义 |

- **示例代码** : 

```
mLivePushConfig.setPauseFlag(TXLiveConstants.PAUSE_FLAG_PAUSE_VIDEO | TXLiveConstants.PAUSE_FLAG_PAUSE_AUDIO);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



#### 12. setPauseImg(img)

接口详情：void setPauseImg(Bitmap img)

设置后台暂停时，推送的垫片。一般运用在后台推流场景。建议结合 setPauseFlag() 一起使用

- **参数说明**

| 参数   |   类型   | 说明                            |
| ---- | :----: | ----------------------------- |
| img  | Bitmap | 后台播放的暂停图片，图片最大尺寸不能超过1920*1920 |

- **示例代码** : 

```
Bitmap bitmap = decodeResource(getResources(),R.drawable.pause_publish);
mLivePushConfig.setPauseImg(bitmap);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



#### 13.setPauseImg(time, fps)

接口详情：void setPauseImg(int time, int fps)

设置推流暂停时，后台垫片的持续时间及帧率 。一般运用在后台推流场景。建议结合 setPauseFlag() 一起使用

- **参数说明**

| 参数   |  类型  | 说明                       |
| ---- | :--: | ------------------------ |
| time | int  | 后台垫片的最长持续时间，单位是秒，默认值是300 |
| fps  | int  | 后台垫片的帧率，最小值为3，最大值为8，默认是5 |

- **示例代码** : 

```
mLivePushConfig.setPauseImg(300,5);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



#### 14.setVideoEncodeGop(gop)

接口详情：void setVideoEncodeGop(int gop)

设置视频编码GOP。

注意：gop过大会增加延时，无特殊要求建议使用TXLivePusher.setVideoQuality，由SDK内部根据档位调整到合适的值

- **参数说明**

| 参数   |  类型  | 说明                 |
| ---- | :--: | ------------------ |
| gop  | int  | 视频编码GOP，单位 秒，默认值为3 |

- **示例代码** : 

```
mLivePushConfig.setVideoEncodeGop(1);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



#### 15.setVideoResolution(resolution)

接口详情：void setVideoResolution(int resolution)

设置视频编码分辨率，可以设置的值参考**推流视频分辨率**。

注意：无特殊要求建议使用TXLivePusher.setVideoQuality，由SDK内部根据档位调整到合适的值

- **参数说明**

| 参数         |  类型  | 说明                                       |
| ---------- | :--: | ---------------------------------------- |
| resolution | int  | 视频编码分辨率，默认值VIDEO_RESOLUTION_TYPE_540_960 |

- **示例代码** : 

```
mLivePushConfig.setVideoResolution(TXLiveConstants.VIDEO_RESOLUTION_TYPE_540_960);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



#### 16.setWatermark(watermark, x, y,) 

接口详情：void setWatermark(Bitmap watermark, int x, int y)

设置水印图片。所要求的水印图片格式为 png，因为 png 这种图片格式有透明度信息，因而能够更好地处理锯齿等问题。如果您需要对水印图片的位置做机型适配，建议使用 setWatermark(watermark, x, y, width) 接口。

- **参数说明**

| 参数        |   类型   | 说明          |
| --------- | :----: | ----------- |
| watermark | Bitmap | 水印图片        |
| x         |  int   | 水印位置的 X 轴坐标 |
| y         |  int   | 水印位置的 Y 轴坐标 |

- **示例代码** : 

```
//设置视频水印
mLivePushConfig.setWatermark(BitmapFactory.decodeResource(getResources(),R.drawable.watermark), 10, 10);
//后面两个参数分别是水印位置的 X 轴坐标和 Y 轴坐标
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



#### 17.setWatermark(watermark, x, y, width) 

接口详情：void setWatermark(Bitmap watermark, float x, float y, float width)

设置水印图片。要求的水印图片格式为 png，因为 png 这种图片格式有透明度信息，因而能够更好地处理锯齿等问题。
如果您需要对水印图片的位置做机型适配，建议使用该接口。

- **参数说明**

| 参数        |   类型   | 说明                   |
| --------- | :----: | -------------------- |
| watermark | Bitmap | 水印图片                 |
| x         |  int   | 归一化水印位置的X轴坐标，取值[0,1] |
| y         |  int   | 归一化水印位置的Y轴坐标，取值[0,1] |
| y         |  int   | 归一化水印宽度，取值[0,1]      |

- **示例代码** : 

```
//设置视频水印
//参数分别是水印图片的 Bitmap、水印位置的 X 轴坐标，水印位置的 Y 轴坐标，水印宽度。后面三个参数取值范围是[0, 1]
//后面两个参数分别是水印位置的X轴坐标和 Y 轴坐标
mLivePushConfig.setWatermark(mBitmap, 0.02f, 0.05f, 0.2f);
mLivePusher.setConfig(mLivePushConfig);    // 重新设置 config
```



## TXLivePlayer接口详情

#### 1.setConfig(TXLivePlayConfig config)

接口详情：void setConfig(TXLivePlayConfig config)

设置获取播放器器配置信息。

注意：请在startPlay前设置，不支持播放过程中设置config。

- **参数说明**

| 参数     | 类型               | 说明       |
| ------ | ---------------- | -------- |
| config | TXLivePlayConfig | 播放器器配置信息 |


- **示例代码** : 

```
TXLivePlayConfig mPlayConfig = new TXLivePlayConfig();
mPlayConfig.setConnectRetryCount(3);
......
mLivePlayer.setConfig(mPlayConfig);
......
mLivePlayer.startPlay(...);
```



#### 2. setPlayerView(TXCloudVideoView view) 

接口详情：void setPlayerView(TXCloudVideoView view) 

把渲染 view 绑定到 TXLivePlayer。支持在播放过程中， 不停止播放情况下，将同一个 player绑定到不同的 TXCloudVideoView。

- **参数说明**

| 参数   | 类型               | 说明           |
| ---- | ---------------- | ------------ |
| view | TXCloudVideoView | 播放画面渲染的 View |

- **示例代码** : 

```
// 初始化
TXCloudVideoView playerView = (TXCloudVideoView) view.findViewById(R.id.video_view);
//关联 player 对象与界面 view
mLivePlayer.setPlayerView(playerView);
```



#### 3. setPlayListener(ITXLivePlayListener listener)

接口详情：void setPlayListener(ITXLivePlayListener listener)

设置TXLivePlayer 的回调，用于接收播放事件及播放器状态。

```
// 初始化  
mLivePlayer.setPlayListener(new ITXLivePlayListener() {
    @Override
    public void onPlayEvent(int i, Bundle bundle) {
        // 收到播放器事件，具体事件定义请参看TXLiveConstants.PLAY_EVT_xxx
    }

    @Override
    public void onNetStatus(Bundle bundle) {
        // 收到播放器当前状态，2s一次刷新，具体状态请参看TXLiveConstants.NET_STATUS_xxx
    }
});
```



#### 4.startPlay(url, type)

接口详情：int startPlay(String url，int type)

启动播放。返回结果中，0 表示启动播放成功；-1 表示启动播放失败，因 playUrl 为空； -2 表示启动播放失败，因 playUrl 非法； -3 表示启动播放失败，因 playType 非法

- **参数说明**

| 参数   | 类型     | 说明                                       |
| ---- | ------ | ---------------------------------------- |
| url  | String | 一个合法的拉流地址，视频播放 URL（URL 以 “rtmp://” 打头 ，腾讯云拉流 URL 的获取方法见 [DOC]( https://cloud.tencent.com/document/product/454/7915 "腾讯云-推拉流地址Doc") ），我们建议使用 FLV 格式 |
| type | int    | 播放类型，参考 TXLivePlayer 中定义的播放类型枚举值         |

- **示例代码** : 

```
int result = mLivePlayer.startPlay(playUrl,TXLivePlayer.PLAY_TYPE_LIVE_FLV); 
```



#### 5.stopPlay(isNeedClearLastImg)

接口详情：int stopPlay(boolean isNeedClearLastImg)

停止播放。返回结果中，0 表示停止播放成功，非0 表示停止播放失败。

- **参数说明**

| 参数                 | 类型   | 说明                                       |
| ------------------ | ---- | ---------------------------------------- |
| isNeedClearLastImg | int  | 是否需要清除最后一帧画面。true 表示清除最后一帧画面，正常停止播放时，推荐清除。 false 表示保留最后一帧画面，异常停止播放(如网络异常,导致播放被迫停止)，而SDK使用者希望重连服务器，继续播放时，推荐保留 |

- **示例代码** : 

```
mLivePlayer.stopPlay(true);
```



#### 6.pause()

接口详情：void pause()

点播场景是暂停播放。直播场景是没有暂停播放这说法，调用该方法意味这停止拉流。

- **示例代码** : 

```
mLivePlayer.pause();
```



#### 7.resume()

接口详情：void resume()

点播场景是从 pause 位置恢复播放。直播场景则是重新拉流。

- **示例代码** : 

```
mLivePlayer.resume();
```


#### 8.prepareLiveSeek()

接口详情：int  prepareLiveSeek()

直播时移准备，拉取该直播流的起始播放时间。使用时移功能需在播放开始后调用此方法，否则时移失败。不支持非腾讯云地址。

- **示例代码** : 

```
mLivePlayer.prepareLiveSeek();
```


#### 9.setAudioRoute()

接口详情：void setAudioRoute(int audioRoute)

设置声音播放模式(切换扬声器，听筒)

- **示例代码** : 

```
// 设置扬声器
mLivePlayer.setAudioRoute(TXLiveConstants.AUDIO_ROUTE_SPEAKER);
// 设置听筒
mLivePlayer.setAudioRoute(TXLiveConstants.AUDIO_ROUTE_RECEIVER);
```


#### 10.switchStream(playUrl)

接口详情：void switchStream(java.lang.String playUrl)

flv直播无缝切换 

- **参数说明**

| 参数               | 类型 | 说明                                   |
| ------------------ | ---- | ---------------------------------------- |
| playUrl | String   | 播放的流地址. playUrl必须是当前播放直播流的不同清晰度，切换到无关流地址可能会失败 |


- **示例代码** : 

```
mLivePlayer.switchStream(playUrl);
```


#### 11.enableHardwareDecode(enable)

接口详情：void enableHardwareDecode(enable)

启用或禁用视频硬解码，SDK默认是视频软解码。

注意：硬件解码只在 Android 系统 4.2 以上（API 级别 16） 的手机支持。硬件解码失败后，SDK内部会自动切换成软解。该接口设置只在startPlay前设置生效。


- **示例代码** : 

```
mLivePlayer.enableHardwareDecode(true);
......
mLivePlayer.startPlay(...)
```



#### 12.isPlaying()

接口详情：boolean isPlaying()

是否正在播放

返回true表示正在播放，false表示尚未播放。

- **示例代码** : 

```
boolean isPlaying = mLivePlayer.isPlaying();
```



#### 13.setRenderMode(mode)

接口详情： void setRenderMode(int mode)

设置图像的渲染（填充）模式。

注意：该接口目前只支持如下两种模式。

TXLiveConstants.RENDER_MODE_FULL_FILL_SCREEN（视频画面全屏铺满）：将图像等比例铺满整个屏幕,多余部分裁剪掉，此模式下画面不留黑边，但视频长宽比例和view不对的情况下会显示不全。

TXLiveConstants.RENDER_MODE_ADJUST_RESOLUTION（视频画面自适应屏幕）：将图像等比例缩放,缩放后的宽和高都不会超过显示区域,居中显示,可能会留有黑边

- **参数说明**

| 参数   | 类型   | 说明                                       |
| ---- | ---- | ---------------------------------------- |
| mode | int  | TXLiveConstants.RENDER_MODE_FULL_FILL_SCREEN或者 TXLiveConstants.RENDER_MODE_ADJUST_RESOLUTION。默认是FULL_FILL_SCREEN |

- **示例代码** : 

```
// 设置填充模式为自适应
mLivePlayer.setRenderMode(TXLiveConstants.RENDER_MODE_ADJUST_RESOLUTION);
// 设置填充模式为全屏
mLivePlayer.setRenderMode(TXLiveConstants.RENDER_MODE_FULL_FILL_SCREEN);
```



#### 14.setRenderRotation(rotation)

接口详情：void setRenderRotation(int rotation)

设置图像的顺时针旋转角度，即设置图像呈现效果为竖屏或者横屏。

可设置的值为TXLiveConstants.RENDER_ROTATION_PORTRAIT（竖屏），TXLiveConstants.RENDER_ROTATION_LANDSCAPE（横屏）。

- **参数说明**

| 参数       | 类型   | 说明             |
| -------- | ---- | -------------- |
| rotation | int  | 竖屏或者横屏渲染，默认是竖屏 |

- **示例代码** : 

```
// 设置画面渲染方向为横屏
mLivePlayer.setRenderRotation(TXLiveConstants.RENDER_ROTATION_LANDSCAPE);
// 设置画面渲染方向为竖屏
mLivePlayer.setRenderRotation(TXLiveConstants.RENDER_ROTATION_PORTRAIT);
```



#### 15.startRecord()

接口详情：int startRecord(int recordType)

启动截流录制。截流录制是直播播放场景下的一种扩展功能：观众在观看直播时，可以通过点击录制按钮把一段直播的内容录制下来，并通过视频分发平台（比如腾讯云的点播系统）发布出去，这样就可以在微信朋友圈等社交平台上以 UGC 消息的形式进行传播。

注意：该接口正在Android 4.4，API 18以上接口使用，并且开始播放后才能调用。

- **参数说明**

| 参数         | 类型   | 说明               |
| ---------- | ---- | ---------------- |
| recordType | int  | 目前该参数废弃，只支持纯视频录制 |

- **示例代码** : 

```
int recordType = TXRecordCommon.RECORD_TYPE_STREAM_SOURCE;
mLivePlayer.startRecord(recordType);
```



#### 16.stopRecord()()

接口详情：int stopRecord()

停止截流录制。返回结果中，0 表示成功，非0表示失败。录制结果会通过录制回调通知出来

- **示例代码** : 

```
mLivePlayer.stopRecord();
```



#### 17.setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener)

接口详情：void setVideoRecordListener(TXRecordCommon.ITXVideoRecordListener listener)

设置视频录制回调，用于接收视频录制进度及录制结果

- **参数说明**

| 参数       | 类型                                    | 说明     |
| -------- | ------------------------------------- | ------ |
| listener | TXRecordCommon.ITXVideoRecordListener | 视频录制回调 |

- **示例代码** : 

```
mLivePusher.setVideoRecordListener(new TXRecordCommon.ITXVideoRecordListener(){
    @Override
    public void onRecordEvent(int event, Bundle param) {
    }

    @Override
    public void onRecordProgress(long milliSecond) {
        Log.d(TAG, "record progress:" + milliSecond);
    }

    @Override
    public void onRecordComplete(TXRecordCommon.TXRecordResult result) {
        if (result.retCode == TXRecordCommon.RECORD_RESULT_OK) {
            String videoFile        = result.videoPath;
            String videoCoverPic    = result.coverPath;
        } else {
            Log.d(TAG, "record error:" + result.retCode + ", error msg:" + result.descMsg);
        }
    }
});
```



#### 18.setMute(mute)

接口详情：void setMute(boolean mute)

设置是否静音播放。该接口在播放前和播放过程中设置都是生效的。

- **参数说明**

| 参数   | 类型      | 说明         |
| ---- | ------- | ---------- |
| mute | boolean | 是否静音，默认非静音 |

- **示例代码** : 

```
mLivePlayer.setMute(true);
```



#### 19. snapshot(TXLivePlayer.ITXSnapshotListener listener)

接口详情：void snapshot(TXLivePlayer.ITXSnapshotListener listener)

截取视频截图。该接口截取截取当前直播流的中一帧视频画面。如果您需要截取当前的整个 UI 界面，请调用系统 API 来实现。截图结果回调接口会异步在主线程回调。

- **示例代码** : 

```
mLivePlayer.snapshot(new ITXSnapshotListener() {
    @Override
    public void onSnapshot(Bitmap bmp) {
        if (null != bmp) {
           //获取到截图 bitmap
        }
    }
});
```



#### 20. setSurface(Surface surface)

接口详情：void  setSurface(Surface surface)

设置渲染surface。可以用来接管SDK的渲染。
注意：这个接口只适用于硬件解码，并且不能设置setPlayViiew。

- **示例代码** : 

```
TextureView videoView = (TextureView) findViewById(R.id.video_view);
videoView.setSurfaceTextureListener(new TextureView.SurfaceTextureListener() {
    @Override
    public void onSurfaceTextureAvailable(SurfaceTexture surface, int width, int height) {
        mLivePlayer.setSurface(new Surface(surface));
    }

    @Override
    public void onSurfaceTextureSizeChanged(SurfaceTexture surface, int width, int height) {

    }

    @Override
    public boolean onSurfaceTextureDestroyed(SurfaceTexture surface) {
        if (mLivePlayer != null) {
            mLivePlayer.setSurface(null);
        }
        return false;
    }

    @Override
    public void onSurfaceTextureUpdated(SurfaceTexture surface) {

    }
});
```



#### 21. addVideoRawData(byte[] yuvBuffer)

接口详情：void  addVideoRawData(byte[] yuvBuffer)

设置播放yuv数据接收buffer。和setVideoRawDataListener接口配合，可以用来接管SDK的渲染。
注意：这个接口只适用于软件解码，并且不能设置setPlayViiew。buffer的大小请用视频实际分辨率计算。



#### 22. setVideoRawDataListener(ITXVideoRawDataListener listener)

接口详情：void  setVideoRawDataListener(ITXVideoRawDataListener listener)

设置视频yuv数据回调。和addVideoRawData接口配合，可以用来接管SDK的渲染。
注意：这个接口只适用于软件解码，并且不能设置setPlayViiew。

 **示例代码** : 

```
public void onPlayEvent(int event, Bundle param) {
    ......
    if (event == TXLiveConstants.PLAY_EVT_CHANGE_RESOLUTION) {
        videoWidth = param.getInt(TXLiveConstants.EVT_PARAM1,0);
        videoHeight = param.getInt(TXLiveConstants.EVT_PARAM2,0);
        mLivePlayer.addVideoRawData(new byte[videoWidth*videoHeight*3/2]);
    } 
    ......
}
    
    
mLivePlayer.setVideoRawDataListener(new TXLivePlayer.ITXVideoRawDataListener() {
    @Override
    public void onVideoRawDataAvailable(byte[] buf, int width, int height, int timestamp) {
        mLivePlayer.addVideoRawData(new byte[videoWidth*videoHeight*3/2]);
    }
});

```



#### 23. setAudioRawDataListener(ITXAudioRawDataListener listener)

接口详情：void  setAudioRawDataListener(ITXAudioRawDataListener listener)

设置音频pcm数据回调。

 **示例代码** : 

```
mLivePlayer.setAudioRawDataListener(new TXLivePlayer.ITXAudioRawDataListener() {
    @Override
    public void onPcmDataAvailable(byte[] buf, long timestamp) {
        //音频pcm数据
    }

    @Override
    public void onAudioInfoChanged(int sampleRate, int channels, int bits) {
        //音频采样率，通道数
    }
});
```



## TXLivePlayConfig接口详情

#### 1. enableAEC(enable)

接口详情：void enableAEC(boolean enable)

开启回声消除。连麦时必须开启，非连麦时不要开启。

- **参数说明**

| 参数     |   类型    | 说明                               |
| ------ | :-----: | -------------------------------- |
| enable | boolean | true 表示开启，false 表示关闭。默认值为 false。 |


- **示例代码** : 

```
mPlayConfig.enableAEC(true);
mLivePlayer.setConfig(mPlayConfig);    // 重新设置 config
```



#### 2. setConnectRetryCount(count)

接口详情：void setConnectRetryCount(int count)

设置播放器重连次数。当SDK与服务器异常断开连接时,SDK会尝试与服务器重连，通过此函数设置SDK重连次数。一般结合 setConnectRetryInterval 一起使用

- **参数说明**

| 参数    |  类型  | 说明                             |
| ----- | :--: | ------------------------------ |
| count | int  | SDK重连次数，最小值为 1， 最大值为 10，默认值为 3 |


- **示例代码** : 

```
mPlayConfig.setConnectRetryCount(5);
mLivePlayer.setConfig(mPlayConfig);    // 重新设置 config
```



#### 3. setConnectRetryInterval(interval)

接口详情：void setConnectRetryInterval(int  interval)

设置播放器重连间隔。当SDK与服务器异常断开连接时,SDK会尝试与服务器重连。通过此函数来设置两次重连间隔时间。一般结合 setConnectRetryCount 一起使用

- **参数说明**

| 参数       |  类型  | 说明                                 |
| -------- | :--: | ---------------------------------- |
| interval | int  | SDK重连间隔，单位秒。最小值为 3，最大值为 30， 默认值为 3 |


- **示例代码** : 

```
mPlayConfig.setConnectRetryInterval(10);
mLivePlayer.setConfig(mPlayConfig);    // 重新设置 config
```



#### 4. setEnableMessage(enable)

接口详情：void setEnableMessage(boolean enable)

开启消息通道。

- **参数说明**

| 参数     |   类型    | 说明                                       |
| ------ | :-----: | ---------------------------------------- |
| enable | boolean | true 表示开启消息通道， false 表示关闭消息通道。默认值是 false。 |


- **示例代码** : 

```
mPlayConfig.setEnableMessage(true);
mLivePlayer.setConfig(mPlayConfig);    // 重新设置 config
```



#### 5. setAutoAdjustCacheTime(bAuto) 

接口详情：void setAutoAdjustCacheTime(boolean bAuto)

设置是否根据网络状况自动调整播放器缓存时间。一般结合 setMinAutoAdjustCacheTime(time 和 setMaxAutoAdjustCacheTime(time) 一起使用。

启用自动调整时,SDK将根据网络状况在一个范围内调整缓存时间，自动调整的范围可以通过修改MaxAutoAdjustCacheTime和修改MinAutoAdjustCacheTime来调整。

关闭自动调整时，SDK将使用固定的缓存时间，固定的缓存时间可以通过修改cacheTime来调整。

- **参数说明**

| 参数    |   类型    | 说明                                     |
| ----- | :-----: | -------------------------------------- |
| bAuto | boolean | true 表示启用自动调整，false 表示关闭自动调整。默认值是true。 |


- **示例代码** : 

```
//自动模式
mPlayConfig.setAutoAdjustCacheTime(true);
mPlayConfig.setMinAutoAdjustCacheTime(1);
mPlayConfig.setMaxAutoAdjustCacheTime(5);
mLivePlayer.setConfig(mPlayConfig);    // 重新设置 config
```



#### 6. setCacheTime(time)

接口详情：void setCacheTime(float time)

设置播放器缓存时间。播放器固定缓冲时间，需要设置setAutoAdjustCacheTime(false)。

- **参数说明**

| 参数   |  类型   | 说明                         |
| ---- | :---: | -------------------------- |
| time | float | 播放器缓存时间，单位秒，默认值为 5，取值需要大于0 |


- **示例代码** : 

```
//流畅模式
mPlayConfig.setAutoAdjustCacheTime(false);
mPlayConfig.setCacheTime(5);
mLivePlayer.setConfig(mPlayConfig);    // 重新设置 config
```



#### 7. setMaxAutoAdjustCacheTime(time)

接口详情：void setMinAutoAdjustCacheTime(float time)

设置自动调整时播放器最大缓存时间。结合 setAutoAdjustCacheTime(bAuto) 和 setMinAutoAdjustCacheTime(time) 一起使用。

- **参数说明**

| 参数   |  类型   | 说明                           |
| ---- | :---: | ---------------------------- |
| time | float | 播放器最大缓存时间，单位秒，默认值为 5，取值需要大于0 |


- **示例代码** : 

```
//极速模式
mPlayConfig.setAutoAdjustCacheTime(true);
mPlayConfig.setMinAutoAdjustCacheTime(1);
mPlayConfig.setMaxAutoAdjustCacheTime(1);
mLivePlayer.setConfig(mPlayConfig);    // 重新设置 config
```



#### 8. setMinAutoAdjustCacheTime(time) 

接口详情：void setMinAutoAdjustCacheTime(float time)

设置自动调整时播放器最小缓存时间。结合 setAutoAdjustCacheTime(bAuto) 和 setMaxAutoAdjustCacheTime(time) 一起使用。

- **参数说明**

| 参数   |  类型   | 说明                           |
| ---- | :---: | ---------------------------- |
| time | float | 播放器最小缓存时间，单位秒，默认值为 1，取值需要大于0 |


- **示例代码** : 

```
//极速模式
mPlayConfig.setAutoAdjustCacheTime(true);
mPlayConfig.setMinAutoAdjustCacheTime(1);
mPlayConfig.setMaxAutoAdjustCacheTime(1);
mLivePlayer.setConfig(mPlayConfig);    // 重新设置 config
```



## 枚举类型定义

#### 1. 推流视频分辨率

如果使用摄像头推流一般不使用以下参数。如果使用录屏推流，有横竖屏切换的场景，需要使用以下参数来改变推流的分辨率。

```
VIDEO_RESOLUTION_TYPE_360_640         =  0;    // 360 * 640 的分辨率
VIDEO_RESOLUTION_TYPE_540_960         =  1;    // 540 * 640 的分辨率
VIDEO_RESOLUTION_TYPE_720_1280        =  2;    // 720 * 1280 的分辨率
VIDEO_RESOLUTION_TYPE_640_360         =  3;    // 640 * 360 的分辨率
VIDEO_RESOLUTION_TYPE_960_540         =  4;    // 960 * 440 的分辨率
VIDEO_RESOLUTION_TYPE_1280_720        =  5;    // 1280 * 720 的分辨率
VIDEO_RESOLUTION_TYPE_320_480         =  6;    // 320 * 480 的分辨率
VIDEO_RESOLUTION_TYPE_180_320         =  7;    // 180 * 320 的分辨率
VIDEO_RESOLUTION_TYPE_270_480         =  8;    // 270 * 480 的分辨率
VIDEO_RESOLUTION_TYPE_320_180         =  9;    // 320 * 180 的分辨率
VIDEO_RESOLUTION_TYPE_480_270         =  10;   // 480 * 270 的分辨率
```

#### 2. 软硬编选项

推流编码的类型。如果你不清楚要何时开启硬件加速, 建议设置为 ENCODE_VIDEO_AUTO。默认是启用软件编码, 但手机 CPU 使用率超过 80% 或者帧率 <= 10, SDK 内部会自动切换为硬件编码

```
ENCODE_VIDEO_SOFTWARE               = 0; // 软编
ENCODE_VIDEO_HARDWARE               = 1; // 硬编
ENCODE_VIDEO_AUTO                   = 2; // 自动决定软硬编
```


#### 3. 图像平铺模式

播放器设置画面渲染的填充模式，铺满或者适应

```
RENDER_MODE_FULL_FILL_SCREEN     =  0; //视频画面全屏铺满:将图像等比例铺满整个屏幕,多余部分裁剪掉,此模式下画面不留黑边
RENDER_MODE_ADJUST_RESOLUTION    =  1; //视频画面自适应屏幕:将图像等比例缩放,缩放后的宽和高都不会超过显示区域,居中显示,可能会留有黑边

```

#### 4. 图像渲染角度

播放器设置画面渲染的旋转的角度，竖屏或者横屏

```
RENDER_ROTATION_PORTRAIT         =  0;      // 常规竖屏
RENDER_ROTATION_LANDSCAPE        =  270;    // 右旋90度，即横屏
```

#### 5. 视频旋转角度

在横屏推流场景中，推流端设置观众端观看画面旋转的角度。

```
VIDEO_ANGLE_HOME_RIGHT           =  0;      // home在右边
VIDEO_ANGLE_HOME_DOWN            =  1;      // home在下面
VIDEO_ANGLE_HOME_LEFT            =  2;      // home在左边
VIDEO_ANGLE_HOME_UP              =  3;      // home在上面
```

#### 6. 后台推流选项

setPauseFlag 的选项

```
PAUSE_FLAG_PAUSE_VIDEO = 1;     // pausePusher时，设置此标志位暂停原采集(camera, 录屏)的画面，采用pauseImg作为推流的画面，不设置此标志位，不会停止原采集(camera, 录屏)，继续推流
PAUSE_FLAG_PAUSE_AUDIO = 2;     // pausePusher时，设置此标志位暂停音频采集，推送静音数据，不设置此标志位，不会暂停音频采集，继续推送麦克风采集到的音频

```



#### 7. 播放类型

播放器支持播放类型。在 APP 中播放视频，直播我们建议使用FLV 格式。

```
PLAY_TYPE_LIVE_RTMP = 0       // 传入的URL为RTMP直播地址 
PLAY_TYPE_LIVE_FLV =  1       // 传入的URL为FLV直播地址 
PLAY_TYPE_LIVE_RTMP_ACC =  5  // 低延迟链路地址（仅适合于连麦场景） 
PLAY_TYPE_VOD_HLS =  3        // 传入的URL为HLS(m3u8)播放地址 
```

## ITXLivePushListener事件回调

#### 推流事件接口

| 接口定义                                 | 功能说明                |
| ------------------------------------ | ------------------- |
| onPushEvent(int event, Bundle param) | 推流事件通知接口 |
| onNetStatus(Bundle param)            | 推流状态通知接口 |

#### 推流事件列表

```
PUSH_EVT_CONNECT_SUCC = 1001,                      // 已经连接推流服务器
PUSH_EVT_PUSH_BEGIN = 1002,                        // 已经与服务器握手完毕,开始推流
PUSH_EVT_OPEN_CAMERA_SUCC = 1003,                  // 打开摄像头成功
PUSH_EVT_SCREEN_CAPTURE_SUCC = 1004;               // 录屏启动成功
PUSH_EVT_CHANGE_RESOLUTION = 1005,                 // 推流动态调整分辨率
PUSH_EVT_CHANGE_BITRATE = 1006,                    // 推流动态调整码率
PUSH_EVT_FIRST_FRAME_AVAILABLE = 1007,             // 首帧画面采集完成
PUSH_EVT_START_VIDEO_ENCODER = 1008,               // 编码器启动

PUSH_ERR_OPEN_CAMERA_FAIL = -1301,                 // 打开摄像头失败
PUSH_ERR_OPEN_MIC_FAIL = -1302,                    // 打开麦克风失败
PUSH_ERR_VIDEO_ENCODE_FAIL = -1303,                // 视频编码失败
PUSH_ERR_AUDIO_ENCODE_FAIL = -1304,                // 音频编码失败
PUSH_ERR_UNSUPPORTED_RESOLUTION = -1305,           // 不支持的视频分辨率
PUSH_ERR_UNSUPPORTED_SAMPLERATE = -1306,           // 不支持的音频采样率
PUSH_ERR_NET_DISCONNECT = -1307,                   // 网络断连,且经多次重连抢救无效,可以放弃治疗,更多重试请自行重启推流
PUSH_ERR_SCREEN_CAPTURE_START_FAILED  = -1308;     // 开始录屏失败,可能是被用户拒绝了
PUSH_ERR_SCREEN_CAPTURE_UNSURPORT = -1309;         // 录屏失败,不支持的Android系统版本,需要5.0以上的系统
PUSH_ERR_SCREEN_CAPTURE_DISTURBED = -1310;         // 录屏被其他应用打断了，先开MediaProjection的应用会被后开MediaProjection的应用停掉，SDK抛出此error
PUSH_ERR_MIC_RECORD_FAIL = -1311;                  // Android Mic打开成功，但是连续6次录不到音频数据 (Audio录制线程会退出)
PUSH_ERR_SCREEN_CAPTURE_SWITCH_DISPLAY_FAILED  = -1312;   // 录屏动态切横竖屏失败

PUSH_WARNING_NET_BUSY = 1101,                      // 网络状况不佳：上行带宽太小，上传数据受阻
PUSH_WARNING_RECONNECT = 1102,                     // 网络断连, 已启动自动重连 (自动重连连续失败超过三次会放弃)
PUSH_WARNING_HW_ACCELERATION_FAIL = 1103,          // 硬编码启动失败，采用软编码
PUSH_WARNING_VIDEO_ENCODE_FAIL = 1104,             // 视频编码失败,非致命错,内部会重启编码器
PUSH_WARNING_BEAUTYSURFACE_VIEW_INIT_FAIL = 1105,  // 视频编码码率异常，警告
PUSH_WARNING_VIDEO_ENCODE_BITRATE_OVERFLOW = 1106, // 视频编码码率异常，警告
PUSH_WARNING_DNS_FAIL = 3001,                      // RTMP -DNS解析失败
PUSH_WARNING_SEVER_CONN_FAIL = 3002,               // RTMP服务器连接失败
PUSH_WARNING_SHAKE_FAIL = 3003,                    // RTMP服务器握手失败
PUSH_WARNING_SERVER_DISCONNECT = 3004,             // RTMP服务器主动断开，请检查推流地址的合法性或防盗链有效期
PUSH_WARNING_SERVER_NO_DATA = 3005,                // 超过30s没有数据发送，主动断开连接。
```

#### 推拉流状态信息

SDK 指标监控，主要回调推流或拉流的状态数据。

| 推流状态                         |   类型   | 含义说明                                     |
| :--------------------------- | :----: | :--------------------------------------- |
| NET_STATUS_CPU_USAGE         | String | 当前进程的CPU使用率和本机总体的CPU使用率                  |
| **NET_STATUS_VIDEO_WIDTH**  |  int   | **当前视频的宽度（单位：像素值）**                      |
| **NET_STATUS_VIDEO_HEIGHT** |  int   | **当前视频的高度（单位：像素值）**                      |
| NET_STATUS_NET_SPEED         |  int   | 当前的发送速度（单位：kbps）                         |
| NET_STATUS_VIDEO_BITRATE     |  int   | 当前视频编码器输出的比特率，也就是编码器每秒生产了多少视频数据，单位： kbps |
| NET_STATUS_AUDIO_BITRATE     |  int   | 当前音频编码器输出的比特率，也就是编码器每秒生产了多少音频数据，单位： kbps |
| NET_STATUS_VIDEO_FPS         |  int   | 当前视频帧率，也就是视频编码器每条生产了多少帧画面                |
| NET_STATUS_CACHE_SIZE        |  int   | 音视频数据堆积情况，这个数字超过个位数，即说明当前上行带宽不足以消费掉已经生产的音视频数据 |
| NET_STATUS_CODEC_DROP_CNT    |  int   | 全局丢包次数，为了避免延迟持续恶性堆积，SDK在数据积压超过警戒线以后会主动丢包，丢包次数越多，说明网络问题越严重。 |
| NET_STATUS_SERVER_IP         | String | 连接的推流服务器的IP                              |


## ITXLivePlayListener事件回调

#### 播放事件接口

| 接口定义                                 | 功能说明                 |
| ------------------------------------ | -------------------- |
| onPlayEvent(int event, Bundle param) | TXLivePlayer 的播放事件通知 |
| onNetStatus(Bundle param)            | TXLivePlayer的播放状态通知  |

#### 播放事件列表

```
PLAY_EVT_CONNECT_SUCC = 2001,                   // 已经连接服务器
PLAY_EVT_RTMP_STREAM_BEGIN = 2002,              // 已经连接服务器，开始拉流
PLAY_EVT_RCV_FIRST_I_FRAME = 2003,              // 渲染首个视频数据包(IDR)
PLAY_EVT_PLAY_BEGIN = 2004,                     // 视频播放开始
PLAY_EVT_PLAY_PROGRESS = 2005,                  // 视频播放进度
PLAY_EVT_PLAY_END = 2006,                       // 视频播放结束
PLAY_EVT_PLAY_LOADING = 2007,                   // 视频播放loading
PLAY_EVT_START_VIDEO_DECODER = 2008,            // 解码器启动
PLAY_EVT_CHANGE_RESOLUTION = 2009,              // 视频分辨率改变

PLAY_ERR_NET_DISCONNECT = -2301,                // 网络断连,且经多次重连抢救无效,可以放弃治疗,更多重试请自行重启播放
PLAY_ERR_GET_RTMP_ACC_URL_FAIL = -2302,         // 获取加速拉流地址失败

PLAY_WARNING_VIDEO_DECODE_FAIL = 2101,          // 当前视频帧解码失败
PLAY_WARNING_AUDIO_DECODE_FAIL = 2102,          // 当前音频帧解码失败
PLAY_WARNING_RECONNECT = 2103,                  // 网络断连, 已启动自动重连 (自动重连连续失败超过三次会放弃)
PLAY_WARNING_RECV_DATA_LAG = 2104,              // 网络来包不稳：可能是下行带宽不足，或由于主播端出流不均匀
PLAY_WARNING_VIDEO_PLAY_LAG = 2105,             // 当前视频播放出现卡顿（用户直观感受）
PLAY_WARNING_HW_ACCELERATION_FAIL = 2106,       // 硬解启动失败，采用软解
PLAY_WARNING_VIDEO_DISCONTINUITY = 2107,        // 当前视频帧不连续，可能丢帧
PLAY_WARNING_FIRST_IDR_HW_DECODE_FAIL = 2108,   // 当前流硬解第一个I帧失败，SDK自动切软解
PLAY_WARNING_DNS_FAIL = 3001,                   // RTMP -DNS解析失败
PLAY_WARNING_SEVER_CONN_FAIL=: 3002,            // RTMP服务器连接失败
PLAY_WARNING_SHAKE_FAIL = 3003,                 // RTMP服务器握手失败
PLAY_WARNING_SERVER_DISCONNECT = 3004,          // RTMP服务器主动断开
```

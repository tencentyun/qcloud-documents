## TXUGCRecord

### 实例化

| API                                                          | 描述   |
| ------------------------------------------------------------ | ------ |
| [shareInstance](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#abd7245daa19d4334a17b2011263f4958) | 实例化 |



### 摄像头、麦克风相关逻辑

| API                                                          | 描述                                        |
| ------------------------------------------------------------ | ------------------------------------------- |
| [startCameraSimple](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a915a26f27fd043c9c3c4e52f9dd05f3f) | 开始画面预览                                |
| [startCameraCustom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#ac8ee6db04ab5058797f1b3f68a56160b) | 开始画面预览                                |
| [setVideoResolution](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a01023a47d639aca64ae8f0ae16f3ce86) | 切换视频录制分辨率，startCamera 之后调用有效 |
| [setVideoRenderMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#af15edcca37fcca57c047bbefa4ca8b9d) | 设置视频渲染模式，startCamera 之后调用有效   |
| [setVideoBitrate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a3f296f3b19e1d30e749b9b27302a50db) | 切换视频录制码率                            |
| [setZoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a9777fe95f7830746c1ba6b10446c37a0) | 调整焦距，startCamera 之后调用有效          |
| [switchCamera](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a8dedd99f945a42c1845313605c50aa61) | 切换前后摄像头，startCamera 之后调用有效    |
| [toggleTorch](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#aef955cde2331f108b22ef7125171b10d) | 打开闪关灯，startCamera 之后调用有效        |
| [stopCameraPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a9b6bf385590ce4bb1a5b0de8f203f6ed) | 结束画面预览                                |



### 录制相关逻辑

| API                                                          | 描述                                                     |
| ------------------------------------------------------------ | -------------------------------------------------------- |
| [setHomeOrientation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a96ce818b22e3f6db5ecd9b24323af851) | 设置横竖屏录制                                           |
| [setRenderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#aedfa7b798e073a450c2b2fbb5063955c) | 设置预览视频方向                                         |
| [setAspectRatio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a3268359a2df3834bbdac805f6f1fa3f4) | 设置视频录制比例                                         |
| [setRecordSpeed](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#afbafab57dedcc9b91f70bbbce36373a3) | 设置录制速率（精简版不支持）                             |
| [setMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a944c4afc32d8e8ce35a8077b0b55c2e8) | 设置是否静音录制                                         |
| [startRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#abd7692290a3855e606f4c2303ff2a19e) | 开始录制短视频，SDK 内部会自动生成视频路经               |
| [startRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#addfa5c2d0d1a99844326d90acd4ba1c9) | 开始录制短视频                                           |
| [startRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a6e3477949172b4232911799aac6595f1) | 开始录制短视频                                           |
| [pauseRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#aab84e356a72a3df115c82efea02264de) | 暂停录制短视频                                           |
| [pauseRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#ad3526e128777c1b0b93362659d4b26fb) | 暂停录制短视频                                           |
| [resumeRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a6c51e097fc18358c065a602204239b48) | 恢复录制短视频                                           |
| [stopRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a13313c5410c2a10a704b991f28141e6e) | 结束录制短视频                                           |
| [pauseAudioSession](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#ad9af84ae142b3fc65cbf5d8c01bfdc7e) | 使用其他播放器预览视频的时候，请先调用 pauseAudioSession |
| [resumeAudioSession](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a9cbec9edda8cf105bba9655567a76c65) | 重启 SDK 内部的 AudioSession                             |



### 录制效果设置相关逻辑

| API                                                          | 描述                             |
| ------------------------------------------------------------ | -------------------------------- |
| [setWaterMark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a7ee69499e0ca3bd9a7c996505725c384) | 设置全局水印（精简版不支持）     |
| [getBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a4fb05ae6b5face276ace62558731280a) | 获取美颜管理对象                 |
| [setBeautyStyle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a789cc2301e3eae49185365a86e885eb1) | 设置**美颜**和**美白**效果级别   |
| [setFilter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a1202f69d0af6c4fd2b022c61da4dd5b0) | 设置指定素材滤镜特效             |
| [setFilter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a44d7f0da7adb1aa2f62a3afd6d7c4b1c) | 设置两个滤镜效果（精简版不支持） |
| [setSpecialRatio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a6de9ce92116926fe9b53016151d55784) | 设置滤镜效果程度                 |
| [setEyeScaleLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#ae0e4341ef565cc5ba28101574179cd56) | 设置大眼级别                     |
| [setFaceScaleLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a52ad635b237ccb1eef53a4ed9e650035) | 设置瘦脸级别                     |
| [setFaceVLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a1bf6dd0f5a5c6c013323d31f60d494e2) | 设置 V 脸                        |
| [setChinLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a145d4ed3d5790a449a9884d282420216) | 设置下巴拉伸或收缩               |
| [setFaceShortLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#ac11082c88aba749acd7cd2c7a7caa953) | 设置短脸                         |
| [setNoseSlimLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#ae94b107a9c476337585906c79b42ee95) | 设置瘦鼻                         |
| [setGreenScreenFile](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#ab4682edfc605ba06e24fd7b3e758ce5d) | 设置绿幕文件                     |
| [selectMotionTmpl](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#ad050ac06c70810665b5c22b77dc20048) | 设置动效                         |
| [setMotionMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#aa6689d734b9f46cb84a848b7e8f39cbd) | 设置动效静音                     |



### 背景音相关逻辑

| API                                                          | 描述                                                |
| ------------------------------------------------------------ | --------------------------------------------------- |
| [setBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#ae77bca45c2b3a024b605143ad28d756e) | 设置背景音乐文件（精简版不支持）                    |
| [setBGMAsset](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a8c0020b6c543c7beb378c71ac691d912) | 设置背景音乐文件（精简版不支持）                    |
| [setBGMLoop](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#af04ec84d6367837b6a3ec009d42f3dc1) | 设置背景音乐是否循环播放（精简版不支持）            |
| [playBGMFromTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#abbd412ef428ecf60dbb94b7b72b4c60e) | 播放背景音乐（精简版不支持）                        |
| [stopBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a93a996c467709cb520c5805b672c00cd) | 停止播放背景音乐（精简版不支持）                    |
| [pauseBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a096218ccb76707c37e2f586548b9375a) | 暂停播放背景音乐（精简版不支持）                    |
| [resumeBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a072b30b60405a8f0df71b1f587c6af06) | 继续播放背景音乐（精简版不支持）                    |
| [setMicVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#aa53f05d91770488ead49d7f2f95ee803) | 设置麦克风的音量大小                                |
| [setBGMVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a3d063f395b28d58c0da4f82765f919da) | 设置背景音乐的音量大小                              |
| [setReverbType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#aa89352df472e2fa4c61e0d2a4ba66a34) | 设置混响效果（精简版不支持）                        |
| [setVoiceChangerType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#ab48b224e092bcec85da330d9ecec4ef6) | 设置变声类型（精简版不支持）                        |
| [snapshot](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__ios.html#a8a2c854e45ee9d741d098a6857edc019) | 截图/拍照，startCamera 之后调用有效（精简版不支持） |



## TXUGCRecordListener

### 短视频录制回调

| API                                                          | 描述                           |
| ------------------------------------------------------------ | ------------------------------ |
| [onRecordProgress](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordListener__ios.html#a5dd24e391f925ae8da1547374f25b695) | 短视频录制进度                 |
| [onRecordComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordListener__ios.html#a8766c15db94cea6b7f0ff0d304503dc5) | 短视频录制完成                 |
| [onRecordEvent](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordListener__ios.html#aa628297da5b9b7cdb197104097b23834) | 短视频录制事件通知（暂未使用） |



## TXUGCRecordTypeDef

### 视频录制关键类型定义

| API                                                          | 描述         |
| ------------------------------------------------------------ | ------------ |
| [TXUGCSimpleConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordTypeDef__ios.html#a1426a86a294de269e792ba146e4afa37) | 录制参数定义 |
| [TXUGCCustomConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordTypeDef__ios.html#a82925315129ec31125cdb42b75f25974) | 录制参数类   |
| [TXUGCRecordResult](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordTypeDef__ios.html#a3446e8347fa1ec3725df691eb485400b) | 录制结果     |



### 枚举类型说明

| API                                                          | 描述             |
| ------------------------------------------------------------ | ---------------- |
| [TXVideoQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordTypeDef__ios.html#ga0b1160a1d1f238eb36ea51792c18aa3e) | 录制视频质量类型 |
| [TXVideoResolution](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordTypeDef__ios.html#ga5a9bcf750e56b71fe39d60cfcd19e49f) | 录制分辨率类型   |
| [TXVideoRenderMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordTypeDef__ios.html#ga97fb98a2c5613b65bb6886f4c84d5f7f) | 视频渲染模式类型 |
| [TXVideoAspectRatio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordTypeDef__ios.html#gaacb6108218d9b544c66d0e026695e607) | 录制视频比例类型 |
| [TXVideoRecordSpeed](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordTypeDef__ios.html#ga05c27784a9a0eff768dc7fc003902d4a) | 录制视频速率     |
| [TXVideoHomeOrientation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordTypeDef__ios.html#ga0ee2b3bbccfc5dabcd157b98555bec80) | 横竖屏录制类型   |
| [TXVideoEncodeMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordTypeDef__ios.html#ga78ccacb3bb8b9291cfc91838d4b97897) | 编码方式         |
| [TXVideoReverbType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordTypeDef__ios.html#gafae9cd4ee113028dd1aa9ad61610baae) | 混响效果         |
| [TXVideoVoiceChangerType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordTypeDef__ios.html#gabbc238c80be048e48c0453dd297fd297) | 变声类型         |
| [TXVideoBeautyStyle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordTypeDef__ios.html#ga135391ff71d01b1b480cdc121c65f715) | 美颜类型         |
| [TXAudioSampleRate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordTypeDef__ios.html#gae746c57de845784f17c465dcd08b077f) | 音频采样率       |
| [TXUGCRecordResultCode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecordTypeDef__ios.html#ga59aed832d7c79e175e84f5f543c8e45e) | 录制结果错误码   |


[](id:error)
## 错误码

### 录制结果错误码定义

| 符号                                     | 值   | 含义                                                         |
| ---------------------------------------- | ---- | ------------------------------------------------------------ |
| UGC_RECORD_RESULT_OK                     | 0    | 录制成功（业务层主动结束录制）,会生成最终视频                |
| UGC_RECORD_RESULT_OK_INTERRUPT           | 1    | 录制成功（因为进后台，或则闹钟，电话打断等自动结束录制），会生成最终视频 |
| UGC_RECORD_RESULT_OK_UNREACH_MINDURATION | 2    | 录制成功（录制时长未达到设置的最小时长），会生成最终视频     |
| UGC_RECORD_RESULT_OK_BEYOND_MAXDURATION  | 3    | 录制成功（录制时长超过设置的最大时长），会生成最终视频       |
| UGC_RECORD_RESULT_FAILED                 | 1001 | 录制失败，不会生成最终视频                                   |


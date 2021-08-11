## TXUGCRecord


### 短视频录制基础接口
| API | 描述 |
|-----|-----|
| [getInstance](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a1069b1a0b6fe60220c8c33234e92a21f) | 获取录制实例 |
| [setVideoRecordListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#acd229e0c77d3eea61dc0762557417478) | 设置录制回调接口 |
| [release](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a23b477d0e2d399f75d585d154c346591) | 释放资源                              |
| [setVideoProcessListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a2a378860dee249f986c086b8dea9ffed) | 设置自定义图像处理回调（ 精简版不支持） |



### 录制效果设置相关函数

| API | 描述 |
|-----|-----|
| [setWatermark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a51fe216c94456dcd7781830c3e4e26fd) | 设置全局水印（ 精简版不支持） |
| [getBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#ab6fd77465f53dab034c7704288b0d8bf) | 获取美颜管理对象            |



### 摄像头,麦克风相关函数

| API                                                          | 描述                                                     |
| ------------------------------------------------------------ | -------------------------------------------------------- |
| [startCameraSimplePreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#af7df0c081288d4fa899213cbe42ab09d) | 启动摄像头预览，简化参数                                 |
| [startCameraCustomPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a55f15e0faaee96f742f35201b920c5b4) | 启动摄像头预览，自定义参数                               |
| [setVideoResolution](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#abd1f86f7fe776c2734c9f4de45d1931a) | 设置录制分辨率                                           |
| [setVideoBitrate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a6422a1f0e41e910f35aad752c9b3d023) | 设置录制比特率                                           |
| [stopCameraPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a9b6bf385590ce4bb1a5b0de8f203f6ed) | 停止摄像头预览                                           |
| [switchCamera](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a5afaa0dd12faeb1232c986727b4dac1d) | 切换前后摄像头                                           |
| [setMicVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a64c284b39bc21caceb6dca801ad9d395) | 设置麦克风的音量大小                                     |
| [toggleTorch](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#af311fa19051d64a5ad64fca96dbc2995) | toggleTorch，打开闪关灯                                  |
| [getMaxZoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#afa83806e4c432618f3b3eacc54693200) | 获取摄像头支持的最大焦距，此方法同时可以检查是否支持变焦 |
| [setZoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a4824a12ec5d48a73c1dd5330f0698942) | 设置焦距                                                 |
| [setFocusPosition](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a589fdf6466566526d49e8877599e12a2) | 设置手动聚焦                                             |
| [setVideoRenderMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#afbe37accb0355ec912b74ed7a003ca09) | 设置视频渲染模式                                         |



### 录制相关函数

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [startRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#abd7692290a3855e606f4c2303ff2a19e) | 开始视频录制，SDK 内部会自动生成视频路经和视频封面，在 [ITXVideoRecordListener](#itxvideorecordlistener) 里面返回 |
| [startRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#ac10931870767702b8103da24a4336da3) | 开始视频录制                                                 |
| [startRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a91a872a1b48867bea52c12288ee860b1) | 开始视频录制                                                 |
| [stopRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a13313c5410c2a10a704b991f28141e6e) | 停止视频录制                                                 |
| [pauseRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#aab84e356a72a3df115c82efea02264de) | 暂停视频录制                                                 |
| [resumeRecord](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a6c51e097fc18358c065a602204239b48) | 继续视频录制                                                 |
| [setAspectRatio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#ae5875c95109dcb60e21fde5efa86d157) | 设置宽高比                                                   |
| [setRecordSpeed](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#ad0f3ba58555a1e212e2abd185d5e3a41) | 录制速度（ 精简版不支持）                                    |
| [setMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#ae1cc2014b473efd1fc6002d1869cd3ab) | 设置静音                                                     |
| [setHomeOrientation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#ab6cf83f6fb86c30369ff3a49f65c3183) | 设置 home 键方向                                             |
| [setRenderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#aa36b38c81fc1a326fa4e7bed26e4efc6) | 设置渲染方向                                                 |



### 背景音相关函数

| API                                                          | 描述                                      |
| ------------------------------------------------------------ | ----------------------------------------- |
| [setReverb](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#aea6ef8fdb2142efc693064aa42f02586) | 设置混响（ 精简版不支持）                 |
| [setVoiceChangerType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a9ae874d5c32001ba2879691b012a35ac) | 设置变声（ 精简版不支持）                 |
| [setBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#adbd9b380aac0204e378b28d6bc461f01) | 设置背景音乐文件（ 精简版不支持）         |
| [setBGMNofify](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a7232f0ee5d704217a637c794ea561b21) | 设置背景音乐播放回调接口（ 精简版不支持） |
| [playBGMFromTime](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a41cdb72a1b5952daa77cafc008c12013) | 播放背景音乐（ 精简版不支持）             |
| [stopBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#adb0738baa0caf8971c629db775662e8e) | 停止播放背景音乐（ 精简版不支持）         |
| [pauseBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#aa108fd51c5988a963f165933e1b7d8ee) | 暂停播放背景音乐（ 精简版不支持）         |
| [resumeBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#af5a020dca59ebadffb99891ff5e1d642) | 继续播放背景音乐（ 精简版不支持）         |
| [seekBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#abd479e0f220b6fb59d6c2f8a930148e6) | 定位 BGM 开始结束时间（ 精简版不支持）    |
| [setBGMVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#aef3bca7adc0c23eff963471400ee5879) | 设置背景音乐的音量大小（ 精简版不支持）   |
| [getMusicDuration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a0bd597c5880c79cb7fa6631da933cc1c) | 获取音乐文件时长（ 精简版不支持）         |



### 截图相关函数

| API                                                          | 描述                 |
| ------------------------------------------------------------ | -------------------- |
| [snapshot](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a65c196156de46b640b80f8266bd3369a) | 设置短视频预处理回调 |



### 废弃接口

| API                                                          | 描述                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| [setMotionTmpl](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#af85168f51d1951878e392eb029ff16cc) | setMotionTmpl 设置动效文件（ 仅支持企业版和企业版 Pro） |
| [setMotionMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a95d1f517930285127b316f648c508efc) | 设置动效是否静音（ 仅支持企业版和企业版 Pro）           |
| [setGreenScreenFile](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a5e3398c309da55c1bba1b58028a4da16) | 设置绿幕文件（仅支持企业版 Pro）                        |
| [setFaceVLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a0d5e0b622666e0b302a6a51db6894bdd) | 设置V脸（仅支持企业版 Pro）                             |
| [setFaceShortLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a028d164b127ad73d7b3dd4add0321c4b) | 设置短脸（仅支持企业版 Pro 和企业版 Pro EX）            |
| [setChinLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#afd1255e5cc581ee4228fc26313a24933) | 设置下巴长度（仅支持企业版 Pro 和企业版 Pro EX）        |
| [setNoseSlimLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#aced93b26f34cefdc8097df9583abb8eb) | 设置瘦鼻效果（仅支持企业版 Pro 和企业版 Pro EX）        |
| [setEyeScaleLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#aae535870773f6e21317b393a5b8eff7c) | 设置大眼效果（仅支持企业版 Pro 和企业版 Pro EX）        |
| [setFaceScaleLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a2e93f2b9f5fa784e9385599491e01c39) | 设置瘦脸效果（仅支持企业版 Pro）                        |
| [setBeautyStyle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a12bb7ad3513d079272a906d805956895) | 设置美颜类型                                            |
| [setBeautyDepth](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#af16fc3112bae6dc212ec0cb2cbb0b4b1) | 设置**美颜**和**美白**效果级别                          |
| [setFilter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a2005812aae2e7ced819230d2c3fb297e) | 设置指定素材滤镜特效                                    |
| [setFilter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a506d6d253f4505a9ae4c613f2dde28c0) | 设置组合滤镜特效                                        |
| [setSpecialRatio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a1f6b0c14db22ca60390b271ca4295cf5) | 设置滤镜效果程度                                        |

## TXUGCPartsManager

### 多段录制相关函数

| API                                                          | 描述                       |
| ------------------------------------------------------------ | -------------------------- |
| [TXUGCPartsManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a44ea49449da296b0e7440e1d3ba95a74) | 视频片段管理器             |
| [setPartsManagerObserver](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#af68a981d78fb6b33a04b2f87775127cc) | 设置视频片段处理回调       |
| [removePartsManagerObserver](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a66ed8147742d77af95294a7016b974bf) | 删除视频片段处理回调       |
| [addClipInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#ace3493c1e4b80f5eeecd78524242f1d3) | 添加视频片段到队列尾部     |
| [insertPart](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#abfdfcf7157a69611a6c1dc41e876103b) | 插入视频片段               |
| [getDuration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a08c13081c0665a4336a0f022c955fb69) | 获取所有分段的总时长       |
| [getPartsPathList](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a0e065b1b0d990a75b572725855dd6e1e) | 获取本次录制所有片段的路径 |
| [deleteLastPart](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a553f582941c1c26527f785414b11f055) | 删除最后一段分段           |
| [deletePart](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a914255b7b451e96a8c6d963d99113cce) | 删除指定分段               |
| [deleteAllParts](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#acda3a6b6d096a49fb105905bf7f4d33c) | 删除所有分段               |



## VideoCustomProcessListener

### 视频处理自定义监听接口

| API                                                          | 描述             |
| ------------------------------------------------------------ | ---------------- |
| [onTextureCustomProcess](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a619017ddecf52cb94b4182331f475cb3) | 纹理处理回调接口 |
| [onDetectFacePoints](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#a292bf542a191747e94adaf610aca7ad6) | 五官检测点回调   |
| [onTextureDestroyed](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXUGCRecord__android.html#ac60f1dbbb1af39c666247c6438595de0) | 纹理释放回调接口 |



## ITXVideoRecordListener

### 短视频预览回调接口

| API                                                          | 描述               |
| ------------------------------------------------------------ | ------------------ |
| [onRecordEvent](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXRecordCommon__android.html#a9e41a4daee4ee714b1348fac74131840) | 短视频录制事件通知 |
| [onRecordProgress](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXRecordCommon__android.html#ab3a5908127ab8c955ec6773a823cd921) | 短视频录制进度     |
| [onRecordComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXRecordCommon__android.html#aecedd2ceb34c986eee915a31481ccc7e) | 短视频录制完成     |



## ITXSnapshotListener

### 截图回调接口

| API                                                          | 描述         |
| ------------------------------------------------------------ | ------------ |
| [onSnapshot](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXRecordCommon__android.html#afbbd41ebf0f82d5b996608ba5fa72cb3) | 截图回调通知 |



## ITXBGMNotify

### 背景音事件回调接口

| API                                                          | 描述                   |
| ------------------------------------------------------------ | ---------------------- |
| [onBGMStart](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXRecordCommon__android.html#a6c2f1aeb77a3020b4767738b7ef0064d) | 音乐播放开始的回调通知 |
| [onBGMProgress](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXRecordCommon__android.html#a30ab555520fa5a478f633394b9cd4d14) | 音乐播放进度的回调通知 |
| [onBGMComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXRecordCommon__android.html#a444c6749e7cb77466940ec1de1c88546) | 音乐播放结束的回调通知 |



## TXRecordCommon

### 短视频录制关键类型定义
| API | 描述 |
|-----|-----|
| [TXRecordResult ](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXRecordCommon__android.html#classcom_1_1tencent_1_1ugc_1_1TXRecordCommon_1_1TXRecordResult) | 录制结果       |
| [TXUGCSimpleConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXRecordCommon__android.html#classcom_1_1tencent_1_1ugc_1_1TXRecordCommon_1_1TXUGCSimpleConfig) | 固定录制参数   |
| [TXUGCCustomConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXRecordCommon__android.html#classcom_1_1tencent_1_1ugc_1_1TXRecordCommon_1_1TXUGCCustomConfig) | 自定义录制参数 |



## 错误码

### 录制结果回调错误码

| 符号                                   | 值   | 含义                                                         |
| -------------------------------------- | ---- | ------------------------------------------------------------ |
| RECORD_RESULT_OK                       | 0    | 回调**录制成功**或者**暂停（停止）**接口返回成功             |
| RECORD_RESULT_OK_LESS_THAN_MINDURATION | 1    | 回调录制成功，时长小于最小值                                 |
| RECORD_RESULT_OK_REACHED_MAXDURATION   | 2    | 回调录制成功，时长达到最大值                                 |
| RECORD_RESULT_FAILED                   | -1   | 回调录制失败                                                 |
| RECORD_RESULT_SUSPEND_FOR_NO_TASK      | -2   | 暂停（或停止）中止，没有录制的任务                           |
| RECORD_RESULT_FILE_ERR                 | -3   | 录制文件不存在或者长度为0，一般开始和暂停（或停止）之间的间隔时间太短导致，用户可不用关心 |
| RECORD_RESULT_COMPOSE_SET_SRC_PATH_ERR | -4   | 回调合成的视频路径有误，通过 `mTXUGCPartsManager.getPartsPathList()` 查看文件是否为空或长度为0 |
| RECORD_RESULT_COMPOSE_SET_DST_PATH_ERR | -5   | 回调合成的视频目标路径有误，检查目标路径是否为空             |
| RECORD_RESULT_COMPOSE_START_ERR        | -6   | 回调合成启动失败，上一次合成还未结束                         |
| RECORD_RESULT_COMPOSE_CANCEL           | -7   | 回调合成取消                                                 |
| RECORD_RESULT_COMPOSE_VERIFY_FAIL      | -8   | 回调合成校验失败，**文件不存在**、**文件长度为0** 或**视频参数与其他视频不一致**。 |
| RECORD_RESULT_COMPOSE_INTERNAL_ERR     | -9   | 回调合成失败，内部错误                                       |


[](id:error)
### 开始录制的返回错误码

| 符号                                         | 值   | 含义                                                         |
| -------------------------------------------- | ---- | ------------------------------------------------------------ |
| START_RECORD_OK                              | 0    | 开始录制                                                     |
| START_RECORD_ERR_IS_IN_RECORDING             | -1   | 开始录制时存在未完成的任务，existing uncompleted record task |
| START_RECORD_ERR_VIDEO_PATH_IS_EMPTY         | -2   | 开始录制时视频文件路径为空                                   |
| START_RECORD_ERR_API_IS_LOWER_THAN_18        | -3   | 版本小于18                                                   |
| START_RECORD_ERR_NOT_INIT                    | -4   | 开始录制时还未初始化结束                                     |
| START_RECORD_ERR_LICENCE_VERIFICATION_FAILED | -5   | License 校验失败                                             |




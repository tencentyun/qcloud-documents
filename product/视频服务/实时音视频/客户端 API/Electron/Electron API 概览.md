## TRTCCloud @ TXLiteAVSDK

腾讯云视频通话功能的主要接口类。

- **主要文档地址**：[TRTC Electron SDK](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/index.html)
- **示例代码地址**：[TRTC Electron Demo](https://github.com/tencentyun/TRTCSDK/tree/master/Electron)

### 创建 TRTC 对象
```js
const TRTCCloud = require('trtc-electron-sdk');
this.rtcCloud = new TRTCCloud();
```

从v7.0.149起，TRTC Electron SDK 增加了 trtc.d.ts 文件，方便使用 typescript 的开发者

```javascript
// 开启了 ES Module 融合模式 (esModuleInterop=true)
import * as trtc_namespace from 'trtc-electron-sdk';

const TRTCCloud = require('trtc-electron-sdk');

const rtcCloud: trtc_namespace.TRTCCloud = new TRTCCloud();
// 获取 SDK 版本号
rtcCloud.getSDKVersion();
```

### 设置回调
```js
subscribeEvents = (rtcCloud) => {
    rtcCloud.on('onError', (errcode, errmsg) => {
    console.info('trtc_demo: onError :' + errcode + " msg" + errmsg);
    }); 
    rtcCloud.on('onEnterRoom', (elapsed) => {
    console.info('trtc_demo: onEnterRoom elapsed:' + elapsed);
    });
    rtcCloud.on('onExitRoom', (reason) => {
    console.info('onExitRoom: userenter reason:' + reason);
    });
};

subscribeEvents(this.rtcCloud);
```

### 创建与销毁 ITRTCCloud 单例

| API | 描述 |
|-----|-----|
| [getTRTCShareInstance](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#.getTRTCShareInstance) | 用于动态加载 dll 时，创建 [ITRTCCloud](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html) 对象单例。 |
| [destroyTRTCShareInstance](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#.destroyTRTCShareInstance) | 释放 [ITRTCCloud](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html) 单例对象并清理资源。 |

### 房间相关接口函数

| API | 描述 |
|-----|-----|
| [enterRoom](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#enterRoom) | 进入房间，若房间不存在，系统将自动创建一个新房间。 |
| [exitRoom](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#exitRoom) | 退出房间。 |
| [switchRole](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#switchRole) | 切换角色，仅适用于直播场景（TRTCAppSceneLIVE 和 TRTCAppSceneVoiceChatRoom）。 |
| [connectOtherRoom](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#connectOtherRoom) | 请求跨房连麦（主播跨房 PK）。 |
| [disconnectOtherRoom](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#disconnectOtherRoom)| 关闭跨房连麦（主播跨房 PK）。 |


### CDN 相关接口函数

| API | 描述 |
|-----|-----|
| [startPublishing](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#startPublishing) | 开始向腾讯云的直播 CDN 推流。 |
| [stopPublishing](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopPublishing) | 停止向腾讯云的直播 CDN 推流。 |
| [startPublishCDNStream](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#startPublishCDNStream) | 开始向非腾讯云的直播 CDN 转推。|
| [stopPublishCDNStream](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopPublishCDNStream) | 停止向非腾讯云的直播 CDN 推流。 |
| [setMixTranscodingConfig](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setMixTranscodingConfig) | 设置云端的混流转码参数。 |


### 视频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalPreview](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#startLocalPreview) | 启动本地摄像头采集和预览。 |
| [stopLocalPreview](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopLocalPreview) | 停止本地摄像头采集和预览。 |
| [muteLocalVideo](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#muteLocalVideo) | 是否屏蔽自己的视频画面。 |
| [startRemoteView](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#startRemoteView) | 开始显示远端视频画面。 |
| [stopRemoteView](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopRemoteView) | 停止显示远端视频画面，同时不再拉取该远端用户的视频数据流。 |
| [stopAllRemoteView](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopAllRemoteView) | 停止显示所有远端视频画面，同时不再拉取远端用户的视频数据流。 |
| [muteRemoteVideoStream](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#muteRemoteVideoStream) | 暂停接收指定的远端视频流。 |
| [muteAllRemoteVideoStreams](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#muteAllRemoteVideoStreams) | 停止接收所有远端视频流。 |
| [setVideoEncoderParam](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setVideoEncoderParam) | 设置视频编码器相关参数。 |
| [setNetworkQosParam](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setNetworkQosParam) | 设置网络流控相关参数。 |
| [setLocalViewFillMode](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setLocalViewFillMode) | 设置本地图像的渲染模式。 |
| [setRemoteViewFillMode](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setRemoteViewFillMode) | 设置远端图像的渲染模式。 |
| [setLocalViewRotation](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setLocalViewRotation) | 设置本地图像的顺时针旋转角度。 |
| [setRemoteViewRotation](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setRemoteViewRotation) | 设置远端图像的顺时针旋转角度。 |
| [setVideoEncoderRotation](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setVideoEncoderRotation) | 设置视频编码输出的（即远端用户观看到的以及服务器录制下来的）画面方向。 |
| [setLocalViewMirror](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setLocalViewMirror) | 设置本地摄像头预览画面的镜像模式。 |
| [setVideoEncoderMirror](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setVideoEncoderMirror) | 设置编码器输出的画面镜像模式。 |
| [enableSmallVideoStream](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#enableSmallVideoStream) | 开启大小画面双路编码模式。 |
| [setRemoteVideoStreamType](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setRemoteVideoStreamType) | 选定观看指定 userId 的大画面或小画面。 |
| [setPriorRemoteVideoStreamType](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setPriorRemoteVideoStreamType) | 设定观看方优先选择的视频质量。 |


### 音频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalAudio](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#startLocalAudio) | 开启本地音频的采集和上行。 |
| [stopLocalAudio](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopLocalAudio) | 关闭本地音频的采集和上行。 |
| [muteLocalAudio](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#muteLocalAudio) | 静音本地的音频。 |
| [muteRemoteAudio](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#muteRemoteAudio) | 静音某一个用户的声音，同时不再拉取该远端用户的音频数据流。 |
| [muteAllRemoteAudio](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#muteAllRemoteAudio) | 静音所有用户的声音，同时不再拉取远端用户的音频数据流。 |
| [setAudioCaptureVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setAudioCaptureVolume) | 设置 SDK 采集音量。 |
| [getAudioCaptureVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getAudioCaptureVolume) | 获取 SDK 采集音量。 |
| [setAudioPlayoutVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setAudioPlayoutVolume) | 设置 SDK 播放音量。 |
| [getAudioPlayoutVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getAudioPlayoutVolume) | 获取 SDK 播放音量。 |
| [enableAudioVolumeEvaluation](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#enableAudioVolumeEvaluation) | 启用或关闭音量大小提示。 |
| [startAudioRecording](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#startAudioRecording) | 开始录音。 |
| [stopAudioRecording](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopAudioRecording) | 停止录音。 |
| [setAudioQuality](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setAudioQuality) | 设置音频质量。 |


### 摄像头相关接口函数

| API | 描述 |
|-----|-----|
| [getCameraDevicesList](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getCameraDevicesList) | 获取摄像头设备列表。 |
| [setCurrentCameraDevice](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setCurrentCameraDevice) | 设置要使用的摄像头。 |
| [getCurrentCameraDevice](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getCurrentCameraDevice) | 获取当前使用的摄像头。 |


### 音频设备相关接口函数

| API | 描述 |
|-----|-----|
| [getMicDevicesList](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getMicDevicesList) | 获取麦克风设备列表。 |
| [getCurrentMicDevice](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getCurrentMicDevice) | 获取当前选择的麦克风。 |
| [setCurrentMicDevice](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setCurrentMicDevice) | 设置要使用的麦克风。 |
| [getCurrentMicDeviceVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getCurrentMicDeviceVolume) | 获取系统当前麦克风设备音量。 |
| [setCurrentMicDeviceVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setCurrentMicDeviceVolume) | 设置系统当前麦克风设备的音量。 |
| [setCurrentMicDeviceMute](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setCurrentMicDeviceMute) | 设置系统当前麦克风设备的静音状态。 |
| [getCurrentMicDeviceMute](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getCurrentMicDeviceMute) | 获取系统当前麦克风设备是否静音。 |
| [getSpeakerDevicesList](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getSpeakerDevicesList) | 获取扬声器设备列表。 |
| [getCurrentSpeakerDevice](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getCurrentSpeakerDevice) | 获取当前的扬声器设备。 |
| [setCurrentSpeakerDevice](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setCurrentSpeakerDevice) | 设置要使用的扬声器。 |
| [getCurrentSpeakerVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getCurrentSpeakerVolume) | 获取系统当前扬声器设备音量。 |
| [setCurrentSpeakerVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setCurrentSpeakerVolume) | 设置系统当前扬声器设备音量。 |
| [setCurrentSpeakerDeviceMute](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setCurrentSpeakerDeviceMute) | 设置系统当前扬声器设备的静音状态。 |
| [getCurrentSpeakerDeviceMute](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getCurrentSpeakerDeviceMute) | 获取系统当前扬声器设备是否静音。 |

### 美颜相关接口函数

| API | 描述 |
|-----|-----|
| [setBeautyStyle](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setBeautyStyle) | 设置美颜、美白以红润效果级别。 |
| [setWaterMark](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setWaterMark) | 设置水印。 |


### 辅流相关接口函数

| API | 描述 |
|-----|-----|
| [startRemoteSubStreamView](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#startRemoteSubStreamView) | 开始渲染远端用户的辅流（屏幕分享）画面。 |
| [stopRemoteSubStreamView](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopRemoteSubStreamView) | 停止渲染远端用户的辅流（屏幕分享）画面。 |
| [setRemoteSubStreamViewFillMode](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setRemoteSubStreamViewFillMode) | 设置辅流（屏幕分享）画面的渲染模式。 |
| [setRemoteSubStreamViewRotation](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setRemoteSubStreamViewRotation) | 设置辅流（屏幕分享）画面的顺时针旋转角度。 |
| [getScreenCaptureSources](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getScreenCaptureSources) | 枚举可共享的窗口列表。 |
| [selectScreenCaptureTarget](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#selectScreenCaptureTarget) | 设置屏幕共享参数，该方法在屏幕共享过程中也可以调用。 |
| [startScreenCapture](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#startScreenCapture) | 启动屏幕分享。 |
| [pauseScreenCapture](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#pauseScreenCapture) | 暂停屏幕分享。 |
| [resumeScreenCapture](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#resumeScreenCapture) | 恢复屏幕分享。 |
| [stopScreenCapture](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopScreenCapture) | 停止屏幕分享。 |
| [setSubStreamEncoderParam](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setSubStreamEncoderParam) | 设置辅流（屏幕分享）的编码器参数。 |
| [setSubStreamMixVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setSubStreamMixVolume) | 设置辅流（屏幕分享）的混音音量大小。 |


### 自定义消息发送

| API | 描述 |
|-----|-----|
| [sendCustomCmdMsg](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#sendCustomCmdMsg) | 发送自定义消息给房间内所有用户。 |
| [sendSEIMsg](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#sendSEIMsg) | 将小数据量的自定义数据嵌入视频帧中。 |


### 背景混音相关接口函数

| API | 描述 |
|-----|-----|
| [playBGM](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#playBGM) | 启动播放背景音乐。 |
| [stopBGM](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopBGM) | 停止播放背景音乐。 |
| [pauseBGM](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#pauseBGM) | 暂停播放背景音乐。 |
| [resumeBGM](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#resumeBGM) | 继续播放背景音乐。 |
| [getBGMDuration](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getBGMDuration) | 获取背景音乐文件总时长，单位毫秒。 |
| [setBGMPosition](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setBGMPosition) | 设置背景音乐播放进度。 |
| [setBGMVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setBGMVolume) | 设置背景音乐播放音量的大小。 |
| [setBGMPlayoutVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setBGMPlayoutVolume) | 设置背景音乐本地播放音量的大小。 |
| [setBGMPublishVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setBGMPublishVolume) | 设置背景音乐远端播放音量的大小。 |
| [startSystemAudioLoopback](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#startSystemAudioLoopback) | 打开系统声音采集（Mac 和 Windows 64位 SDK 尚不支持系统混音能力，目前只支持 Windows 32位，其他系统调用失效）。 |
| [stopSystemAudioLoopback](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopSystemAudioLoopback) | 关闭系统声音采集（Mac 和 Windows 64位 SDK 尚不支持系统混音能力，目前只支持 Windows 32位，其他系统调用失效）。 |
| [setSystemAudioLoopbackVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setSystemAudioLoopbackVolume) | 设置系统声音采集的音量（Mac 和 Windows 64位 SDK 尚不支持系统混音能力，目前只支持 Windows 32位，其他系统调用失效）。 |


### 音效相关接口函数

| API | 描述 |
|-----|-----|
| [playAudioEffect](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#playAudioEffect) | 播放音效。 |
| [setAudioEffectVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setAudioEffectVolume) | 设置音效音量。 |
| [stopAudioEffect](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopAudioEffect) | 停止音效。 |
| [stopAllAudioEffects](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopAllAudioEffects) | 停止所有音效。 |
| [setAllAudioEffectsVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setAllAudioEffectsVolume) | 设置所有音效的音量。 |
| [pauseAudioEffect](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#pauseAudioEffect) | 暂停音效。 |
| [resumeAudioEffect](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#resumeAudioEffect) | 恢复音效。 |


### 设备和网络测试

| API | 描述 |
|-----|-----|
| [startSpeedTest](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#startSpeedTest) | 开始进行网络测速（视频通话期间请勿测试，以免影响通话质量）。 |
| [stopSpeedTest](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopSpeedTest) | 停止网络测速。 |
| [startCameraDeviceTest](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#startCameraDeviceTest) | 开始进行摄像头测试。 |
| [stopCameraDeviceTest](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopCameraDeviceTest) | 停止摄像头测试。 |
| [startMicDeviceTest](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#startMicDeviceTest) | 开始进行麦克风测试。 |
| [stopMicDeviceTest](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopMicDeviceTest) | 停止麦克风测试。 |
| [startSpeakerDeviceTest](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#startSpeakerDeviceTest) | 开始进行扬声器测试。 |
| [stopSpeakerDeviceTest](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#stopSpeakerDeviceTest) | 停止扬声器测试。 |


### LOG 相关接口函数

| API | 描述 |
|-----|-----|
| [getSDKVersion](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getSDKVersion) | 获取 SDK 版本信息。 |
| [setLogLevel](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setLogLevel) | 设置 Log 输出级别。 |
| [setConsoleEnabled](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setConsoleEnabled) | 启用或禁用控制台日志打印。 |
| [setLogCompressEnabled](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setLogCompressEnabled) | 启用或禁用 Log 的本地压缩。 |
| [setLogDirPath](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setLogDirPath) | 设置日志保存路径。 |
| [setLogCallback](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setLogCallback) | 设置日志回调。 |
| [callExperimentalAPI](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#callExperimentalAPI) | 调用实验性 API 接口。 |


### 弃用接口函数

| API | 描述 |
|-----|-----|
| [setMicVolumeOnMixing](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setMicVolumeOnMixing) | 从 v6.9 版本开始废弃。 |


## TRTCCallback @ TXLiteAVSDK

腾讯云视频通话功能的回调接口类。

### 错误事件和警告事件

| API | 描述 |
|-----|-----|
| [onError](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onError) | 错误回调：SDK 不可恢复的错误，必须监听，并分情况给用户适当的界面提示。 |
| [onWarning](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onWarning) | 警告回调：用于告知您一些非严重性问题，例如出现了卡顿或可恢复的解码失败。 |


### 房间事件回调

| API | 描述 |
|-----|-----|
| [onEnterRoom](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onEnterRoom) | 已加入房间的回调。 |
| [onExitRoom](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onExitRoom) | 退出房间的事件回调。 |
| [onSwitchRole](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onSwitchRole) | 切换角色的事件回调。 |
| [onConnectOtherRoom](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onConnectOtherRoom) | 请求跨房连麦（主播跨房 PK）的结果回调。 |
| [onDisconnectOtherRoom](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onDisconnectOtherRoom) | 关闭跨房连麦（主播跨房 PK）的结果回调。 |


### 成员事件回调

| API | 描述 |
|-----|-----|
| [onRemoteUserEnterRoom](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onRemoteUserEnterRoom) | 有用户加入当前房间。 |
| [onRemoteUserLeaveRoom](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onRemoteUserLeaveRoom) | 有用户离开当前房间。 |
| [onUserVideoAvailable](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onUserVideoAvailable) | 用户是否开启摄像头视频。 |
| [onUserSubStreamAvailable](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onUserSubStreamAvailable) | 用户是否开启屏幕分享。 |
| [onUserAudioAvailable](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onUserAudioAvailable) | 用户是否开启音频上行。 |
| [onFirstVideoFrame](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onFirstVideoFrame) | 开始渲染本地或远程用户的首帧画面。 |
| [onFirstAudioFrame](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onFirstAudioFrame) | 开始播放远程用户的首帧音频（本地声音暂不通知）。 |
| [onSendFirstLocalVideoFrame](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onSendFirstLocalVideoFrame) | 首帧本地视频数据已经被送出。 |
| [onSendFirstLocalAudioFrame](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onSendFirstLocalAudioFrame) | 首帧本地音频数据已经被送出。 |
| [onUserEnter](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onUserEnter) | 废弃接口：有主播加入当前房间。 |
| [onUserExit](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onUserExit) | 废弃接口： 有主播离开当前房间。 |


### 统计和质量回调

| API | 描述 |
|-----|-----|
| [onNetworkQuality](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onNetworkQuality) | 网络质量：该回调每2秒触发一次，统计当前网络的上行和下行质量。 |
| [onStatistics](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onStatistics) | 技术指标统计回调。 |


### 服务器事件回调

| API | 描述 |
|-----|-----|
| [onConnectionLost](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onConnectionLost) | SDK 与服务器的连接断开。 |
| [onTryToReconnect](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onTryToReconnect) | SDK 尝试重新连接到服务器。 |
| [onConnectionRecovery](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onConnectionRecovery) | SDK 与服务器的连接恢复。 |
| [onSpeedTest](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onSpeedTest) | 服务器测速的回调，SDK 对多个服务器 IP 进行测速，每个 IP 的测速结果通过这个回调通知。 |


### 硬件设备事件回调

| API | 描述 |
|-----|-----|
| [onCameraDidReady](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onCameraDidReady) | 摄像头准备就绪。 |
| [onMicDidReady](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onMicDidReady) | 麦克风准备就绪。 |
| [onUserVoiceVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onUserVoiceVolume) | 用于提示音量大小的回调,包括每个 userId 的音量和远端总音量。 |
| [onDeviceChange](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onDeviceChange) | 本地设备通断回调。 |
| [onTestMicVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onTestMicVolume) | 麦克风测试音量回调。 |
| [onTestSpeakerVolume](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onTestSpeakerVolume) | 扬声器测试音量回调。 |
| [onAudioDeviceCaptureVolumeChanged](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onAudioDeviceCaptureVolumeChanged) | 当前音频采集设备音量变化回调。 |
| [onAudioDevicePlayoutVolumeChanged](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onAudioDevicePlayoutVolumeChanged) | 当前音频播放设备音量变化回调。 |


### 自定义消息的接收回调

| API | 描述 |
|-----|-----|
| [onRecvCustomCmdMsg](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onRecvCustomCmdMsg) | 收到自定义消息回调。 |
| [onMissCustomCmdMsg](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onMissCustomCmdMsg) | 自定义消息丢失回调。 |
| [onRecvSEIMsg](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onRecvSEIMsg) | 收到 SEI 消息的回调。 |


### CDN 旁路转推回调

| API | 描述 |
|-----|-----|
| [onStartPublishing](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onStartPublishing) | 开始向腾讯云的直播 CDN 推流的回调，对应于 TRTCCloud 中的 startPublishing() 接口。 |
| [onStopPublishing](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onStopPublishing) | 停止向腾讯云的直播 CDN 推流的回调，对应于 TRTCCloud 中的 stopPublishing() 接口。 |
| [onStartPublishCDNStream](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onStartPublishCDNStream) | 启动旁路推流到 CDN 完成的回调。 |
| [onStopPublishCDNStream](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onStopPublishCDNStream) | 停止旁路推流到 CDN 完成的回调。 |
| [onSetMixTranscodingConfig](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onSetMixTranscodingConfig) | 设置云端的混流转码参数的回调，对应于 TRTCCloud 中的 setMixTranscodingConfig() 接口。 |


### 音效回调

| API | 描述 |
|-----|-----|
| [onAudioEffectFinished](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onAudioEffectFinished) | 播放音效结束回调。 |


### 屏幕分享回调

| API | 描述 |
|-----|-----|
| [onScreenCaptureCovered](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onScreenCaptureCovered) | 当屏幕分享窗口被遮挡无法正常捕获时，SDK 会通过此回调通知，可在此回调里通知用户移开遮挡窗口。 |
| [onScreenCaptureStarted](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onScreenCaptureStarted) | 当屏幕分享开始时，SDK 会通过此回调通知。 |
| [onScreenCapturePaused](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onScreenCapturePaused) | 当屏幕分享暂停时，SDK 会通过此回调通知。 |
| [onScreenCaptureResumed](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onScreenCaptureResumed) | 当屏幕分享恢复时，SDK 会通过此回调通知。 |
| [onScreenCaptureStopped](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onScreenCaptureStopped) | 当屏幕分享停止时，SDK 会通过此回调通知。 |


### 背景混音事件回调

| API | 描述 |
|-----|-----|
| [onPlayBGMBegin](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onPlayBGMBegin) | 开始播放背景音乐。 |
| [onPlayBGMProgress](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onPlayBGMProgress) | 播放背景音乐的进度。 |
| [onPlayBGMComplete](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCallback.html#event:onPlayBGMComplete) | 播放背景音乐结束。 |


## 关键类型定义

### 关键类型

| 类名 | 描述 |
|-----|-----|
| [TRTCParams](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCParams.html)| 进房相关参数。 |
| [TRTCVideoEncParam](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCVideoEncParam.html) | 视频编码参数。 |
| [TRTCNetworkQosParam](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCNetworkQosParam.html) | 网络流控相关参数。 |
| [TRTCQualityInfo](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCQualityInfo.html)| 视频质量。 |
| [TRTCVolumeInfo](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCVolumeInfo.html) | 音量大小。 |
| [TRTCSpeedTestResult](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCSpeedTestResult.html)| 网络测速结果。 |
| [TRTCMixUser](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCMixUser.html)| 云端混流中每一路子画面的位置信息。 |
| [TRTCTranscodingConfig](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCTranscodingConfig.html)| 云端混流（转码）配置。 |
| [TRTCPublishCDNParam](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCPublishCDNParam.html)| CDN 旁路推流参数。 |
| [TRTCAudioRecordingParams](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCAudioRecordingParams.html)| 录音参数。 |
| [TRTCLocalStatistics](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCLocalStatistics.html)| 自己本地的音视频统计信息。 |
| [TRTCRemoteStatistics](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCRemoteStatistics.html) | 远端成员的音视频统计信息。 |
| [TRTCStatistics](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCStatistics.html)| 统计数据。 |

### 枚举值

| 枚举 | 描述 |
|-----|-----|
| [TRTCVideoResolution](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCVideoResolution)| 视频分辨率。 |
| [TRTCVideoResolutionMode](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCVideoResolutionMode)| 视频分辨率模式。 |
| [TRTCVideoStreamType](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCVideoStreamType) | 视频流类型。 |
| [TRTCQuality](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCQuality)| 画质级别。 |
| [TRTCVideoFillMode](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCVideoFillMode)| 视频画面填充模式。 |
| [TRTCBeautyStyle](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCBeautyStyle) | 美颜（磨皮）算法。 |
| [TRTCAppScene](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCAppScene)| 应用场景。 |
| [TRTCRoleType](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCRoleType)| 角色，仅适用于直播场景（TRTCAppSceneLIVE）。 |
| [TRTCQosControlMode](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCQosControlMode)| 流控模式。 |
| [TRTCVideoQosPreference](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCVideoQosPreference)| 画质偏好。 |
| [TRTCDeviceState](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCDeviceState)| 设备操作。 |
| [TRTCDeviceType](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCDeviceType)| 设备类型。 |
| [TRTCWaterMarkSrcType](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCWaterMarkSrcType)| 水印图片的源类型。 |
| [TRTCTranscodingConfigMode](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCTranscodingConfigMode)| 混流参数配置模式。 |

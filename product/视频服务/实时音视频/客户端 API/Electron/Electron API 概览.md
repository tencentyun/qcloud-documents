## TRTCCloud @ TXLiteAVSDK

腾讯云视频通话功能的主要接口类。

- **主要文档地址**：[TRTC Electron SDK](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/index.html)
- **示例代码地址**：[TRTC Electron Demo](https://github.com/tencentyun/TRTCSDK/tree/master/Electron)

### 创建 TRTC 对象
```js
const TRTCCloud = require('trtc-electron-sdk').default;
// import TRTCCloud from 'trtc-electron-sdk';
this.rtcCloud = new TRTCCloud();
```

从v7.9.348起，TRTC Electron SDK 增加了 trtc.d.ts 文件，方便使用 typescript 的开发者

```javascript
import TRTCCloud from 'trtc-electron-sdk';

const rtcCloud: TRTCCloud = new TRTCCloud();
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

### 创建与销毁 TRTCCloud 单例

| API | 描述 |
|-----|-----|
| [getTRTCShareInstance](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#.getTRTCShareInstance) | 用于动态加载 dll 时，创建 [TRTCCloud](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html) 对象单例。 |
| [destroyTRTCShareInstance](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#.destroyTRTCShareInstance) | 释放 [TRTCCloud](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html) 单例对象并清理资源。 |

### 房间相关接口函数

| API | 描述 |
|-----|-----|
| [enterRoom](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#enterRoom) | 进入房间，若房间不存在，系统将自动创建一个新房间。 |
| [exitRoom](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#exitRoom) | 退出房间。 |
| [switchRoom](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#switchRoom) | 切换房间。 |
| [switchRole](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#switchRole) | 切换角色，仅适用于直播场景（TRTCAppSceneLIVE 和 TRTCAppSceneVoiceChatRoom）。 |
| [connectOtherRoom](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#connectOtherRoom) | 请求跨房连麦（主播跨房 PK）。 |
| [disconnectOtherRoom](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#disconnectOtherRoom)| 关闭跨房连麦（主播跨房 PK）。 |
| [setDefaultStreamRecvMode](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setDefaultStreamRecvMode) | 设置音视频数据接收模式（需要在进房前设置才能生效）。 |


### CDN 相关接口函数

| API | 描述 |
|-----|-----|
| [startPublishing](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startPublishing) | 开始向腾讯云的直播 CDN 推流。 |
| [stopPublishing](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopPublishing) | 停止向腾讯云的直播 CDN 推流。 |
| [startPublishCDNStream](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startPublishCDNStream) | 开始向非腾讯云的直播 CDN 转推。|
| [stopPublishCDNStream](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopPublishCDNStream) | 停止向非腾讯云的直播 CDN 推流。 |
| [setMixTranscodingConfig](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setMixTranscodingConfig) | 设置云端的混流转码参数。 |


### 视频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalPreview](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startLocalPreview) | 启动本地摄像头采集和预览。 |
| [stopLocalPreview](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopLocalPreview) | 停止本地摄像头采集和预览。 |
| [muteLocalVideo](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#muteLocalVideo) | 是否屏蔽自己的视频画面。 |
| [startRemoteView](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startRemoteView) | 开始显示远端视频画面。 |
| [stopRemoteView](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopRemoteView) | 停止显示远端视频画面，同时不再拉取该远端用户的视频数据流。 |
| [stopAllRemoteView](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopAllRemoteView) | 停止显示所有远端视频画面，同时不再拉取远端用户的视频数据流。 |
| [muteRemoteVideoStream](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#muteRemoteVideoStream) | 暂停接收指定的远端视频流。 |
| [muteAllRemoteVideoStreams](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#muteAllRemoteVideoStreams) | 停止接收所有远端视频流。 |
| [setVideoEncoderParam](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setVideoEncoderParam) | 设置视频编码器相关参数。 |
| [setNetworkQosParam](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setNetworkQosParam) | 设置网络流控相关参数。 |
| [setLocalRenderParams](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setLocalRenderParams) | 设置本地图像（主流）的渲染参数。 |
| [setLocalViewFillMode](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setLocalViewFillMode) | 废弃接口：设置本地图像的渲染模式。 |
| [setRemoteRenderParams](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setRemoteRenderParams) | 设置远端图像的渲染参数。 |
| [setRemoteViewFillMode](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setRemoteViewFillMode) | 废弃接口：设置远端图像的渲染模式。 |
| [setLocalViewRotation](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setLocalViewRotation) | 废弃接口：设置本地图像的顺时针旋转角度。 |
| [setRemoteViewRotation](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setRemoteViewRotation) | 废弃接口：设置远端图像的顺时针旋转角度。 |
| [setVideoEncoderRotation](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setVideoEncoderRotation) | 设置视频编码输出的（即远端用户观看到的以及服务器录制下来的）画面方向。 |
| [setLocalViewMirror](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setLocalViewMirror) | 废弃接口：设置本地摄像头预览画面的镜像模式。 |
| [setVideoEncoderMirror](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setVideoEncoderMirror) | 设置编码器输出的画面镜像模式。 |
| [enableSmallVideoStream](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#enableSmallVideoStream) | 开启大小画面双路编码模式。 |
| [setRemoteVideoStreamType](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setRemoteVideoStreamType) | 选定观看指定 userId 的大画面或小画面。 |
| [setPriorRemoteVideoStreamType](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setPriorRemoteVideoStreamType) | 废弃接口：设定观看方优先选择的视频质量。 |
| [snapshotVideo](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#snapshotVideo) | 视频画面截图。 |


### 音频相关接口函数

| API | 描述 |
|-----|-----|
| [startLocalAudio](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startLocalAudio) | 开启本地音频的采集和上行。 |
| [stopLocalAudio](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopLocalAudio) | 关闭本地音频的采集和上行。 |
| [muteLocalAudio](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#muteLocalAudio) | 静音本地的音频。 |
| [muteRemoteAudio](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#muteRemoteAudio) | 静音某一个用户的声音，同时不再拉取该远端用户的音频数据流。 |
| [muteAllRemoteAudio](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#muteAllRemoteAudio) | 静音所有用户的声音，同时不再拉取远端用户的音频数据流。 |
| [setAudioCaptureVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setAudioCaptureVolume) | 设置 SDK 采集音量。 |
| [getAudioCaptureVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getAudioCaptureVolume) | 获取 SDK 采集音量。 |
| [setAudioPlayoutVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setAudioPlayoutVolume) | 设置 SDK 播放音量。 |
| [getAudioPlayoutVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getAudioPlayoutVolume) | 获取 SDK 播放音量。 |
| [enableAudioVolumeEvaluation](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#enableAudioVolumeEvaluation) | 启用或关闭音量大小提示。 |
| [startAudioRecording](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startAudioRecording) | 开始录音。 |
| [stopAudioRecording](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopAudioRecording) | 停止录音。 |
| [setAudioQuality](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setAudioQuality) | 废弃接口：设置音频质量。 |
| [setRemoteAudioVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setRemoteAudioVolume) | 设置远程用户播放音量。 |


### 摄像头相关接口函数

| API | 描述 |
|-----|-----|
| [getCameraDevicesList](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getCameraDevicesList) | 获取摄像头设备列表。 |
| [setCurrentCameraDevice](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setCurrentCameraDevice) | 设置要使用的摄像头。 |
| [getCurrentCameraDevice](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getCurrentCameraDevice) | 获取当前使用的摄像头。 |


### 音频设备相关接口函数

| API | 描述 |
|-----|-----|
| [getMicDevicesList](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getMicDevicesList) | 获取麦克风设备列表。 |
| [getCurrentMicDevice](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getCurrentMicDevice) | 获取当前选择的麦克风。 |
| [setCurrentMicDevice](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setCurrentMicDevice) | 设置要使用的麦克风。 |
| [getCurrentMicDeviceVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getCurrentMicDeviceVolume) | 获取系统当前麦克风设备音量。 |
| [setCurrentMicDeviceVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setCurrentMicDeviceVolume) | 设置系统当前麦克风设备的音量。 |
| [setCurrentMicDeviceMute](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setCurrentMicDeviceMute) | 设置系统当前麦克风设备的静音状态。 |
| [getCurrentMicDeviceMute](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getCurrentMicDeviceMute) | 获取系统当前麦克风设备是否静音。 |
| [getSpeakerDevicesList](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getSpeakerDevicesList) | 获取扬声器设备列表。 |
| [getCurrentSpeakerDevice](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getCurrentSpeakerDevice) | 获取当前的扬声器设备。 |
| [setCurrentSpeakerDevice](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setCurrentSpeakerDevice) | 设置要使用的扬声器。 |
| [getCurrentSpeakerVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getCurrentSpeakerVolume) | 获取系统当前扬声器设备音量。 |
| [setCurrentSpeakerVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setCurrentSpeakerVolume) | 设置系统当前扬声器设备音量。 |
| [setCurrentSpeakerDeviceMute](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setCurrentSpeakerDeviceMute) | 设置系统当前扬声器设备的静音状态。 |
| [getCurrentSpeakerDeviceMute](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getCurrentSpeakerDeviceMute) | 获取系统当前扬声器设备是否静音。 |

### 美颜相关接口函数

| API | 描述 |
|-----|-----|
| [setBeautyStyle](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setBeautyStyle) | 设置美颜、美白以红润效果级别。 |
| [setWaterMark](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setWaterMark) | 设置水印。 |


### 辅流相关接口函数

| API | 描述 |
|-----|-----|
| [startRemoteSubStreamView](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startRemoteSubStreamView) | 废弃接口：开始渲染远端用户的辅流（屏幕分享）画面。 |
| [stopRemoteSubStreamView](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopRemoteSubStreamView) | 废弃接口：停止渲染远端用户的辅流（屏幕分享）画面。 |
| [setRemoteSubStreamViewFillMode](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setRemoteSubStreamViewFillMode) | 废弃接口：设置辅流（屏幕分享）画面的渲染模式。 |
| [setRemoteSubStreamViewRotation](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setRemoteSubStreamViewRotation) | 废弃接口：设置辅流（屏幕分享）画面的顺时针旋转角度。 |
| [getScreenCaptureSources](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getScreenCaptureSources) | 枚举可共享的窗口列表。 |
| [selectScreenCaptureTarget](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#selectScreenCaptureTarget) | 设置屏幕共享参数，该方法在屏幕共享过程中也可以调用。 |
| [startScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startScreenCapture) | 启动屏幕分享。 |
| [pauseScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#pauseScreenCapture) | 暂停屏幕分享。 |
| [resumeScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#resumeScreenCapture) | 恢复屏幕分享。 |
| [stopScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopScreenCapture) | 停止屏幕分享。 |
| [setSubStreamEncoderParam](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setSubStreamEncoderParam) | 设置辅流（屏幕分享）的编码器参数。 |
| [setSubStreamMixVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setSubStreamMixVolume) | 设置辅流（屏幕分享）的混音音量大小。 |
| [addExcludedShareWindow](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#addExcludedShareWindow) | 将指定窗口加入屏幕分享的排除列表中，加入排除列表中的窗口不会被分享出去。|
| [removeExcludedShareWindow](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#removeExcludedShareWindow) | 将指定窗口从屏幕分享的排除列表中移除。|
| [removeAllExcludedShareWindow](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#removeAllExcludedShareWindow) | 将所有窗口从屏幕分享的排除列表中移除。|


### 自定义消息发送

| API | 描述 |
|-----|-----|
| [sendCustomCmdMsg](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#sendCustomCmdMsg) | 发送自定义消息给房间内所有用户。 |
| [sendSEIMsg](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#sendSEIMsg) | 将小数据量的自定义数据嵌入视频帧中。 |


### 背景混音相关接口函数

| API | 描述 |
|-----|-----|
| [playBGM](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#playBGM) | 废弃接口：启动播放背景音乐。 |
| [stopBGM](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopBGM) | 废弃接口：停止播放背景音乐。 |
| [pauseBGM](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#pauseBGM) | 废弃接口：暂停播放背景音乐。 |
| [resumeBGM](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#resumeBGM) | 废弃接口：继续播放背景音乐。 |
| [getBGMDuration](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getBGMDuration) | 废弃接口：获取背景音乐文件总时长，单位毫秒。 |
| [setBGMPosition](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setBGMPosition) | 废弃接口：设置背景音乐播放进度。 |
| [setBGMVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setBGMVolume) | 废弃接口：设置背景音乐播放音量的大小。 |
| [setBGMPlayoutVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setBGMPlayoutVolume) | 废弃接口：设置背景音乐本地播放音量的大小。 |
| [setBGMPublishVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setBGMPublishVolume) | 废弃接口：设置背景音乐远端播放音量的大小。 |
| [startSystemAudioLoopback](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startSystemAudioLoopback) | 打开系统声音采集。 |
| [stopSystemAudioLoopback](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopSystemAudioLoopback) | 关闭系统声音采集。 |
| [setSystemAudioLoopbackVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setSystemAudioLoopbackVolume) | 设置系统声音采集的音量。 |
| [startPlayMusic](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startPlayMusic) | 启动播放背景音乐。 |
| [stopPlayMusic](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopPlayMusic) | 停止播放背景音乐。 |
| [pausePlayMusic](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#pausePlayMusic) | 暂停播放背景音乐。 |
| [resumePlayMusic](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#resumePlayMusic) | 恢复播放背景音乐。 |
| [getMusicDurationInMS](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getMusicDurationInMS) | 获取背景音乐文件总时长，单位毫秒。 |
| [seekMusicToPosInTime](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#seekMusicToPosInTime) | 设置背景音乐播放进度。 |
| [setAllMusicVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setAllMusicVolume) | 设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小。 |
| [setMusicPlayoutVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setMusicPlayoutVolume) | 设置背景音乐本地播放音量的大小。 |
| [setMusicPublishVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setMusicPublishVolume) | 设置背景音乐远端播放音量的大小。 |


### 音效相关接口函数

| API | 描述 |
|-----|-----|
| [playAudioEffect](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#playAudioEffect) | 废弃接口：播放音效。 |
| [setAudioEffectVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setAudioEffectVolume) | 废弃接口：设置音效音量。 |
| [stopAudioEffect](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopAudioEffect) | 废弃接口：停止音效。 |
| [stopAllAudioEffects](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopAllAudioEffects) | 废弃接口：停止所有音效。 |
| [setAllAudioEffectsVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setAllAudioEffectsVolume) | 废弃接口：设置所有音效的音量。 |
| [pauseAudioEffect](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#pauseAudioEffect) | 废弃接口：暂停音效。 |
| [resumeAudioEffect](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#resumeAudioEffect) | 废弃接口：恢复音效。 |


### 设备和网络测试

| API | 描述 |
|-----|-----|
| [startSpeedTest](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startSpeedTest) | 开始进行网络测速（视频通话期间请勿测试，以免影响通话质量）。 |
| [stopSpeedTest](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopSpeedTest) | 停止网络测速。 |
| [startCameraDeviceTest](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startCameraDeviceTest) | 开始进行摄像头测试。 |
| [stopCameraDeviceTest](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopCameraDeviceTest) | 停止摄像头测试。 |
| [startMicDeviceTest](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startMicDeviceTest) | 开始进行麦克风测试。 |
| [stopMicDeviceTest](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopMicDeviceTest) | 停止麦克风测试。 |
| [startSpeakerDeviceTest](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startSpeakerDeviceTest) | 开始进行扬声器测试。 |
| [stopSpeakerDeviceTest](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopSpeakerDeviceTest) | 停止扬声器测试。 |


### LOG 相关接口函数

| API | 描述 |
|-----|-----|
| [getSDKVersion](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getSDKVersion) | 获取 SDK 版本信息。 |
| [setLogLevel](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setLogLevel) | 设置 Log 输出级别。 |
| [setConsoleEnabled](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setConsoleEnabled) | 启用或禁用控制台日志打印。 |
| [setLogCompressEnabled](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setLogCompressEnabled) | 启用或禁用 Log 的本地压缩。 |
| [setLogDirPath](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setLogDirPath) | 设置日志保存路径。 |
| [setLogCallback](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setLogCallback) | 设置日志回调。 |
| [callExperimentalAPI](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#callExperimentalAPI) | 调用实验性 API 接口。 |


### 弃用接口函数

| API | 描述 |
|-----|-----|
| [setMicVolumeOnMixing](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setMicVolumeOnMixing) | 从 v6.9 版本开始废弃。 |


## TRTCCallback @ TXLiteAVSDK

腾讯云视频通话功能的回调接口类。

### 错误事件和警告事件

| API | 描述 |
|-----|-----|
| [onError](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onError) | 错误回调：SDK 不可恢复的错误，必须监听，并分情况给用户适当的界面提示。 |
| [onWarning](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onWarning) | 警告回调：用于告知您一些非严重性问题，例如出现了卡顿或可恢复的解码失败。 |


### 房间事件回调

| API | 描述 |
|-----|-----|
| [onEnterRoom](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onEnterRoom) | 已加入房间的回调。 |
| [onExitRoom](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onExitRoom) | 退出房间的事件回调。 |
| [onSwitchRole](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onSwitchRole) | 切换角色的事件回调。 |
| [onConnectOtherRoom](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onConnectOtherRoom) | 请求跨房连麦（主播跨房 PK）的结果回调。 |
| [onDisconnectOtherRoom](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onDisconnectOtherRoom) | 关闭跨房连麦（主播跨房 PK）的结果回调。 |
| [onSwitchRoom](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onSwitchRoom) | 切换房间。 |


### 成员事件回调

| API | 描述 |
|-----|-----|
| [onRemoteUserEnterRoom](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onRemoteUserEnterRoom) | 有用户加入当前房间。 |
| [onRemoteUserLeaveRoom](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onRemoteUserLeaveRoom) | 有用户离开当前房间。 |
| [onUserVideoAvailable](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onUserVideoAvailable) | 用户是否开启摄像头视频。 |
| [onUserSubStreamAvailable](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onUserSubStreamAvailable) | 用户是否开启屏幕分享。 |
| [onUserAudioAvailable](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onUserAudioAvailable) | 用户是否开启音频上行。 |
| [onFirstVideoFrame](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onFirstVideoFrame) | 开始渲染本地或远程用户的首帧画面。 |
| [onFirstAudioFrame](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onFirstAudioFrame) | 开始播放远程用户的首帧音频（本地声音暂不通知）。 |
| [onSendFirstLocalVideoFrame](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onSendFirstLocalVideoFrame) | 首帧本地视频数据已经被送出。 |
| [onSendFirstLocalAudioFrame](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onSendFirstLocalAudioFrame) | 首帧本地音频数据已经被送出。 |
| [onUserEnter](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onUserEnter) | 废弃接口：有主播加入当前房间。 |
| [onUserExit](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onUserExit) | 废弃接口： 有主播离开当前房间。 |


### 统计和质量回调

| API | 描述 |
|-----|-----|
| [onNetworkQuality](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onNetworkQuality) | 网络质量：该回调每2秒触发一次，统计当前网络的上行和下行质量。 |
| [onStatistics](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onStatistics) | 技术指标统计回调。 |


### 服务器事件回调

| API | 描述 |
|-----|-----|
| [onConnectionLost](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onConnectionLost) | SDK 与服务器的连接断开。 |
| [onTryToReconnect](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onTryToReconnect) | SDK 尝试重新连接到服务器。 |
| [onConnectionRecovery](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onConnectionRecovery) | SDK 与服务器的连接恢复。 |
| [onSpeedTest](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onSpeedTest) | 服务器测速的回调，SDK 对多个服务器 IP 进行测速，每个 IP 的测速结果通过这个回调通知。 |


### 硬件设备事件回调

| API | 描述 |
|-----|-----|
| [onCameraDidReady](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onCameraDidReady) | 摄像头准备就绪。 |
| [onMicDidReady](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onMicDidReady) | 麦克风准备就绪。 |
| [onUserVoiceVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onUserVoiceVolume) | 用于提示音量大小的回调,包括每个 userId 的音量和远端总音量。 |
| [onDeviceChange](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onDeviceChange) | 本地设备通断回调。 |
| [onTestMicVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onTestMicVolume) | 麦克风测试音量回调。 |
| [onTestSpeakerVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onTestSpeakerVolume) | 扬声器测试音量回调。 |
| [onAudioDeviceCaptureVolumeChanged](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onAudioDeviceCaptureVolumeChanged) | 当前音频采集设备音量变化回调。 |
| [onAudioDevicePlayoutVolumeChanged](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onAudioDevicePlayoutVolumeChanged) | 当前音频播放设备音量变化回调。 |


### 自定义消息的接收回调

| API | 描述 |
|-----|-----|
| [onRecvCustomCmdMsg](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onRecvCustomCmdMsg) | 收到自定义消息回调。 |
| [onMissCustomCmdMsg](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onMissCustomCmdMsg) | 自定义消息丢失回调。 |
| [onRecvSEIMsg](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onRecvSEIMsg) | 收到 SEI 消息的回调。 |


### CDN 旁路转推回调

| API | 描述 |
|-----|-----|
| [onStartPublishing](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onStartPublishing) | 开始向腾讯云的直播 CDN 推流的回调，对应于 TRTCCloud 中的 startPublishing() 接口。 |
| [onStopPublishing](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onStopPublishing) | 停止向腾讯云的直播 CDN 推流的回调，对应于 TRTCCloud 中的 stopPublishing() 接口。 |
| [onStartPublishCDNStream](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onStartPublishCDNStream) | 启动旁路推流到 CDN 完成的回调。 |
| [onStopPublishCDNStream](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onStopPublishCDNStream) | 停止旁路推流到 CDN 完成的回调。 |
| [onSetMixTranscodingConfig](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onSetMixTranscodingConfig) | 设置云端的混流转码参数的回调，对应于 TRTCCloud 中的 setMixTranscodingConfig() 接口。 |

### 系统音量采集回调
| API | 描述 |
|-----|-----|
| [onSystemAudioLoopbackError](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onSystemAudioLoopbackError) | 系统音量采集状态的回调（仅在 Mac 上有效）。 |

### 音效回调

| API | 描述 |
|-----|-----|
| [onAudioEffectFinished](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onAudioEffectFinished) | 废弃接口：播放音效结束回调。 |

### 屏幕分享回调

| API | 描述 |
|-----|-----|
| [onScreenCaptureCovered](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onScreenCaptureCovered) | 当屏幕分享窗口被遮挡无法正常捕获时，SDK 会通过此回调通知，可在此回调里通知用户移开遮挡窗口。 |
| [onScreenCaptureStarted](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onScreenCaptureStarted) | 当屏幕分享开始时，SDK 会通过此回调通知。 |
| [onScreenCapturePaused](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onScreenCapturePaused) | 当屏幕分享暂停时，SDK 会通过此回调通知。 |
| [onScreenCaptureResumed](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onScreenCaptureResumed) | 当屏幕分享恢复时，SDK 会通过此回调通知。 |
| [onScreenCaptureStopped](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onScreenCaptureStopped) | 当屏幕分享停止时，SDK 会通过此回调通知。 |


### 截图回调

| API | 描述 |
|-----|-----|
| [onSnapshotComplete](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onSnapshotComplete) | 截图完成时，SDK 会通过此回调通知。 |


### 背景混音事件回调

| API | 描述 |
|-----|-----|
| [onPlayBGMBegin](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onPlayBGMBegin) | 废弃接口：开始播放背景音乐。 |
| [onPlayBGMProgress](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onPlayBGMProgress) | 废弃接口：播放背景音乐的进度。 |
| [onPlayBGMComplete](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onPlayBGMComplete) | 废弃接口：播放背景音乐结束。 |


## 关键类型定义

### 关键类型

| 类名 | 描述 |
|-----|-----|
| [TRTCParams](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCParams.html)| 进房相关参数。 |
| [TRTCVideoEncParam](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCVideoEncParam.html) | 视频编码参数。 |
| [TRTCNetworkQosParam](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCNetworkQosParam.html) | 网络流控相关参数。 |
| [TRTCQualityInfo](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCQualityInfo.html)| 视频质量。 |
| [TRTCVolumeInfo](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCVolumeInfo.html) | 音量大小。 |
| [TRTCSpeedTestResult](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCSpeedTestResult.html)| 网络测速结果。 |
| [TRTCMixUser](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCMixUser.html)| 云端混流中每一路子画面的位置信息。 |
| [TRTCTranscodingConfig](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCTranscodingConfig.html)| 云端混流（转码）配置。 |
| [TRTCPublishCDNParam](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCPublishCDNParam.html)| CDN 旁路推流参数。 |
| [TRTCAudioRecordingParams](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCAudioRecordingParams.html)| 录音参数。 |
| [TRTCLocalStatistics](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCLocalStatistics.html)| 自己本地的音视频统计信息。 |
| [TRTCRemoteStatistics](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCRemoteStatistics.html) | 远端成员的音视频统计信息。 |
| [TRTCStatistics](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCStatistics.html)| 统计数据。 |

### 枚举值

| 枚举 | 描述 |
|-----|-----|
| [TRTCVideoResolution](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCVideoResolution)| 视频分辨率。 |
| [TRTCVideoResolutionMode](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCVideoResolutionMode)| 视频分辨率模式。 |
| [TRTCVideoStreamType](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCVideoStreamType) | 视频流类型。 |
| [TRTCQuality](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCQuality)| 画质级别。 |
| [TRTCVideoFillMode](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCVideoFillMode)| 视频画面填充模式。 |
| [TRTCBeautyStyle](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCBeautyStyle) | 美颜（磨皮）算法。 |
| [TRTCAppScene](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCAppScene)| 应用场景。 |
| [TRTCRoleType](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCRoleType)| 角色，仅适用于直播场景（TRTCAppSceneLIVE）。 |
| [TRTCQosControlMode](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCQosControlMode)| 流控模式。 |
| [TRTCVideoQosPreference](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCVideoQosPreference)| 画质偏好。 |
| [TRTCDeviceState](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCDeviceState)| 设备操作。 |
| [TRTCDeviceType](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCDeviceType)| 设备类型。 |
| [TRTCWaterMarkSrcType](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCWaterMarkSrcType)| 水印图片的源类型。 |
| [TRTCTranscodingConfigMode](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCTranscodingConfigMode)| 混流参数配置模式。 |

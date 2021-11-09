## TRTCCloud

### 基础方法

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [sharedInstance](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#sharedInstance) | 创建 TRTCCloud 单例。 |
| [destroySharedInstance](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#destroySharedInstance) | 销毁 TRTCCloud单例。 |
| [registerListener](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#registerListener) | 设置事件监听。 |
| [unRegisterListener](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#unRegisterListener) | 移除事件监听。 |

### 房间相关接口函数

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [enterRoom](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#enterRoom) | 进入房间，若房间不存在，系统将自动创建一个新房间。           |
| [exitRoom](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#exitRoom) | 离开房间。                                                   |
| [switchRole](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#switchRole) | 切换角色，仅适用于直播场景（TRTC_APP_SCENE_LIVE 和 TRTC_APP_SCENE_VOICE_CHATROOM）。 |
| [setDefaultStreamRecvMode](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setDefaultStreamRecvMode) | 设置音视频数据接收模式，需要在进房前设置才能生效。           |
| [connectOtherRoom](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#connectOtherRoom) | 请求跨房通话（主播 PK）。          |
| [disconnectOtherRoom](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#disconnectOtherRoom) | 退出跨房通话。          |
| [switchRoom](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#switchRoom) | 切换房间。         |



### CDN 相关接口函数

| API                                                          | 描述                          |
| ------------------------------------------------------------ | ----------------------------- |
| [startPublishing](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#startPublishing) | 开始向腾讯云的直播 CDN 推流。      |
| [stopPublishing](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#stopPublishing) | 停止向腾讯云的直播 CDN 推流。      |
| [startPublishCDNStream](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#startPublishCDNStream) | 开始向友商云的直播 CDN 转推。      |
| [stopPublishCDNStream](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#stopPublishCDNStream) | 停止向非腾讯云地址转推。     |
| [setMixTranscodingConfig](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setMixTranscodingConfig) | 设置云端的混流转码参数。      |


### 视频相关接口函数

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [muteLocalVideo](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#muteLocalVideo) | 暂停/恢复推送本地的视频数据。                                |
| [startRemoteView](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#startRemoteView) | 开始显示远端视频画面。                                       |
| [stopRemoteView](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#stopRemoteView) | 停止显示远端视频画面，同时不再拉取该远端用户的视频数据流。   |
| [muteRemoteVideoStream](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#muteRemoteVideoStream) | 暂停/恢复接收指定的远端视频流。                              |
| [muteAllRemoteVideoStreams](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#muteAllRemoteVideoStreams) | 暂停/恢复接收所有远端视频流。                                |
| [setVideoEncoderParam](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setVideoEncoderParam) | 设置视频编码器相关参数。                                     |
| [setNetworkQosParam](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setNetworkQosParam) | 设置网络流控相关参数。                                       |
| [setVideoEncoderRotation](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setVideoEncoderRotation) | 设置视频编码输出的画面方向，即设置远端用户观看到的和服务器录制的画面方向。 |
| [setVideoEncoderMirror](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setVideoEncoderMirror) | 设置编码器输出的画面镜像模式。 |
| [setGSensorMode](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setGSensorMode) | 设置重力感应的适应模式。 
| [setVideoMuteImage](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setVideoMuteImage) | 设置暂停推送本地视频时要推送的图片。                                    |

### 音频相关接口函数

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [startLocalAudio](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#startLocalAudio) | 开启本地音频的采集和上行。                                   |
| [stopLocalAudio](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#stopLocalAudio) | 关闭本地音频的采集和上行。                                   |
| [muteLocalAudio](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#muteLocalAudio) | 静音/取消静音本地的音频。                                    |
| [setAudioRoute](https://comm.qq.com/trtc-react-native/api/classes/tx_device_manager.default.html#setAudioRoute) | 设置音频路由。                                               |
| [muteRemoteAudio](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#muteRemoteAudio) | 静音/取消静音指定的远端用户的声音。                          |
| [muteAllRemoteAudio](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#muteAllRemoteAudio) | 静音/取消静音所有用户的声音。                                |
| [setAudioCaptureVolume](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setAudioCaptureVolume) | 设置 SDK 采集音量。                                          |
| [getAudioCaptureVolume](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#getAudioCaptureVolume) | 获取 SDK 采集音量。                                          |
| [setAudioPlayoutVolume](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setAudioPlayoutVolume) | 设置 SDK 播放音量。                                          |
| [getAudioPlayoutVolume](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#getAudioPlayoutVolume) | 获取 SDK 播放音量。                                          |
| [enableAudioVolumeEvaluation](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#enableAudioVolumeEvaluation) | 启用音量大小提示。                                           |
| [startAudioRecording](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#startAudioRecording) | 开始录音。                                                   |
| [stopAudioRecording](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#stopAudioRecording) | 停止录音。                                                   |


### 设备管理接口

| API | 描述 |
|-----|-----|
| [getDeviceManager](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#getDeviceManager) | 获取设备管理模块，接口详情见 [设备管理接口](https://comm.qq.com/trtc-react-native/api/classes/tx_device_manager.default.html) 文档。 |


### 美颜滤镜相关接口函数

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [getBeautyManager](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#getBeautyManager) | 获取美颜管理对象，接口详情见 [美颜管理](https://comm.qq.com/trtc-react-native/api/classes/tx_beauty_manager.default.html) 文档。 |
| [setWatermark](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setWatermark) | 添加水印。                                                   |


### 音乐特效和人声特效

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [getAudioEffectManager](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#getAudioEffectManager) | 获取音效管理类 TXAudioEffectManager，用于管理 BGM，短音效和人声特效，接口详情见 [音效管理](https://comm.qq.com/trtc-react-native/api/classes/tx_audio_effect_manager.default.html) 文档。 |

### 网络测试

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [startSpeedTest](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#startSpeedTest) | 开始进行网络测速（视频通话期间请勿测试，以免影响通话质量）。 |
| [stopSpeedTest](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#stopSpeedTest) | 停止服务器测速。                                             |


### Log 相关接口函数

| API                                                          | 描述                        |
| ------------------------------------------------------------ | --------------------------- |
| [getSDKVersion](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#getSDKVersion) | 获取 SDK 版本信息。         |
| [setLogLevel](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setLogLevel) | 设置 Log 输出级别。         |
| [setLogDirPath](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setLogDirPath) | 修改日志保存路径。         |
| [setLogCompressEnabled](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setLogCompressEnabled) | 启用或禁用 Log 的本地压缩。         |
| [setConsoleEnabled](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setConsoleEnabled) | 启用或禁用控制台日志打印。  |


## TRTCCloudListener

腾讯云视频通话功能的事件回调接口。

### 错误事件和警告事件

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [onError](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onError) | 错误回调，表示 SDK 不可恢复的错误，一定要监听并分情况给用户适当的界面提示。 |
| [onWarning](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onWarning) | 警告回调，用于告知您一些非严重性问题，例如出现卡顿或者可恢复的解码失败。 |


### 房间事件回调

| API                                                          | 描述                                |
| ------------------------------------------------------------ | ----------------------------------- |
| [onEnterRoom](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onEnterRoom) | 已加入房间的回调。                  |
| [onExitRoom](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onExitRoom) | 离开房间的事件回调。                |
| [onSwitchRole](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onSwitchRole) | 切换角色的事件回调。                |
| [onConnectOtherRoom](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onConnectOtherRoom) | 请求跨房通话（主播 PK）的结果回调。         |
| [onDisConnectOtherRoom](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onDisConnectOtherRoom) | 结束跨房通话（主播 PK）的结果回调。        |
| [onSwitchRoom](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onSwitchRoom) | 切换房间 (switchRoom) 的结果回调。               |

### 成员事件回调

| API                                                          | 描述                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| [onRemoteUserEnterRoom](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onRemoteUserEnterRoom) | 有用户加入当前房间。                |
| [onRemoteUserLeaveRoom](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onRemoteUserLeaveRoom) | 有用户离开当前房间。                |
| [onUserVideoAvailable](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onUserVideoAvailable) | 远端用户是否存在可播放的主路画面（一般用于摄像头）。 |
| [onUserSubStreamAvailable](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onUserSubStreamAvailable) | 远端用户是否存在可播放的辅路画面（一般用于屏幕分享）。 |
| [onUserAudioAvailable](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onUserAudioAvailable) | 远端用户是否存在可播放的音频数据。        |
| [onFirstVideoFrame](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onFirstVideoFrame) | 开始渲染本地或远程用户的首帧画面。           |
| [onFirstAudioFrame](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onFirstAudioFrame) | 开始播放远程用户的首帧音频（本地声音暂不通知）。   |
| [onSendFirstLocalVideoFrame](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onSendFirstLocalVideoFrame) | 首帧本地视频数据已经被送出。    |
| [onSendFirstLocalAudioFrame](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onSendFirstLocalAudioFrame) | 首帧本地音频数据已经被送出。       |

### 播放背景音乐的回调接口

播放背景音乐的回调接口。

| API                                                          | 描述                     |
| ------------------------------------------------------------ | ------------------------ |
| [onMusicObserverStart](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onMusicObserverStart) | 音乐播放开始的回调通知。 |
| [onMusicObserverPlayProgress](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onMusicObserverPlayProgress) | 音乐播放进度的回调通知。 |
| [onMusicObserverComplete](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onMusicObserverComplete) | 音乐播放结束的回调通知。 |

### 统计和质量回调

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [onNetworkQuality](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onNetworkQuality) | 网络质量，该回调每2秒触发一次，统计当前网络的上行和下行质量。 |
| [onStatistics](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onStatistics) | 技术指标统计回调。                          |


### 服务器事件回调

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [onConnectionLost](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onConnectionLost) | SDK 跟服务器的连接断开。                |
| [onTryToReconnect](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onTryToReconnect) | SDK 尝试重新连接到服务器。                |
| [onConnectionRecovery](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onConnectionRecovery) | SDK 跟服务器的连接恢复。         |
| [onSpeedTest](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onSpeedTest) | 服务器测速的回调，SDK 对多个服务器 IP 做测速，每个 IP 的测速结果通过这个回调通知。 |


### 硬件设备事件回调

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [onCameraDidReady](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onCameraDidReady) | 摄像头准备就绪。                                             |
| [onMicDidReady](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onMicDidReady) | 麦克风准备就绪。                         |
| [onUserVoiceVolume](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onUserVoiceVolume) | 用于提示音量大小的回调，包括每个 userId 的音量和远端总音量。 |

### CDN 旁路转推回调

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [onStartPublishing](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onStartPublishing) | 开始向腾讯云的直播 CDN 推流的回调，对应于 [TRTCCloud](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#startPublishing) 中的 startPublishing() 接口。 |
| [onStopPublishing](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onStopPublishing) | 停止向腾讯云的直播 CDN 推流的回调，对应于 [TRTCCloud](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#stopPublishing) 中的 stopPublishing() 接口。 |
| [onStartPublishCDNStream](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onStartPublishCDNStream) | 启动旁路推流到 CDN 完成的回调。|
| [onStopPublishCDNStream](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onStopPublishCDNStream) | 停止旁路推流到 CDN 完成的回调。|
| [onSetMixTranscodingConfig](https://comm.qq.com/trtc-react-native/api/enums/trtc_cloud.TRTCCloudListener.html#onSetMixTranscodingConfig) | 设置云端的混流转码参数的回调，对应于 [TRTCCloud](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud.default.html#setMixTranscodingConfig) 中的 setMixTranscodingConfig() 接口。 |

## 关键类型定义

| 类名                                                         | 描述                                    |
| ------------------------------------------------------------ | --------------------------------------- |
| [TRTCCloudDef](https://comm.qq.com/trtc-react-native/api/classes/trtc_cloud_def.TRTCCloudDef.html) | 关键类型定义变量。                              |
| [TRTCParams](https://comm.qq.com/trtc-react-native/api/modules/trtc_cloud_def.html#TRTCParams) | 进房参数。                              |
| [TRTCSwitchRoomConfig](https://comm.qq.com/trtc-react-native/api/modules/trtc_cloud_def.html#TRTCSwitchRoomConfig) | 切换房间参数参数。                              |
| [TRTCVideoEncParam](https://comm.qq.com/trtc-react-native/api/modules/trtc_cloud_def.html#TRTCVideoEncParam) | 视频编码参数。                              |
| [TRTCNetworkQosParam](https://comm.qq.com/trtc-react-native/api/modules/trtc_cloud_def.html#TRTCNetworkQosParam) | 网络流控相关参数。                      |
| [TRTCRenderParams](https://comm.qq.com/trtc-react-native/api/modules/trtc_cloud_def.html#TRTCRenderParams) | 远端图像参数。 |
| [TRTCMixUser](https://comm.qq.com/trtc-react-native/api/modules/trtc_cloud_def.html#TRTCMixUser) | 云端混流中每一路子画面的位置信息。 |
| [TRTCTranscodingConfig](https://comm.qq.com/trtc-react-native/api/modules/trtc_cloud_def.html#TRTCTranscodingConfig) | 云端混流（转码）配置。 |
| [TXVoiceChangerType](https://comm.qq.com/trtc-react-native/api/modules/trtc_cloud_def.html#TXVoiceChangerType) | 变声类型定义（萝莉、大叔、重金属、外国人等）。 |
| [TXVoiceReverbType](https://comm.qq.com/trtc-react-native/api/modules/trtc_cloud_def.html#TXVoiceReverbType) | 变声类型定义（KTV、小房间、大会堂、低沉、洪亮等）。 |
| [AudioMusicParam](https://comm.qq.com/trtc-react-native/api/modules/trtc_cloud_def.html#AudioMusicParam) | 音乐和人声设置接口参数。 |
| [TRTCAudioRecordingParams](https://comm.qq.com/trtc-react-native/api/modules/trtc_cloud_def.html#TRTCAudioRecordingParams) | 录音参数。 |
| [TRTCPublishCDNParam](https://comm.qq.com/trtc-react-native/api/modules/trtc_cloud_def.html#TRTCPublishCDNParam) | CDN 转推参数。 |

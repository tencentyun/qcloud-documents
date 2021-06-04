## TRTC Unity Api概览

### 基础方法

| API                                                          | 描述                              |
| ------------------------------------------------------------ | --------------------------------- |
| [getTRTCShareInstance](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_getTRTCShareInstance) | 创建 TRTCCloud 单例。             |
| [destroyTRTCShareInstance](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_destroyTRTCShareInstance) | 释放 ITRTCCloud 单例对象。        |
| [addCallback](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_addCallback_trtc_ITRTCCloudCallback_) | 设置回调接口  TRTCCloudCallback。 |
| [removeCallback](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_removeCallback_trtc_ITRTCCloudCallback_) | 移除事件回调。                    |

### 房间相关接口函数

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [enterRoom](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_enterRoom_trtc_TRTCParams__trtc_TRTCAppScene_) | 进入房间，若房间不存在，系统将自动创建一个新房间。           |
| [exitRoom](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_exitRoom) | 离开房间。                                                   |
| [switchRole](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_switchRole_trtc_TRTCRoleType_) | 切换角色，仅适用于直播场景（TRTC_APP_SCENE_LIVE 和 TRTC_APP_SCENE_VOICE_CHATROOM）。 |
| [setDefaultStreamRecvMode](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setDefaultStreamRecvMode_System_Boolean_System_Boolean_) | 设置音视频数据接收模式，需要在进房前设置才能生效。           |
| [connectOtherRoom](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_connectOtherRoom_System_String_) | 请求跨房通话（主播 PK）。          |
| [disconnectOtherRoom](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_disconnectOtherRoom) | 退出跨房通话。          |
| [switchRoom](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_switchRoom_trtc_TRTCSwitchRoomConfig_) | 切换房间。  |



### CDN 相关接口函数

| API                                                          | 描述                          |
| ------------------------------------------------------------ | ----------------------------- |
| [startPublishing](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_startPublishing_System_String_trtc_TRTCVideoStreamType_) | 开始向腾讯云的直播 CDN 推流。      |
| [stopPublishing](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopPublishing) | 停止向腾讯云的直播 CDN 推流。      |
| [startPublishCDNStream](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_startPublishCDNStream_trtc_TRTCPublishCDNParam_) | 开始向友商云的直播 CDN 转推。      |
| [stopPublishCDNStream](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopPublishCDNStream) | 停止向非腾讯云地址转推。      |
| [setMixTranscodingConfig](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setMixTranscodingConfig_System_Nullable_trtc_TRTCTranscodingConfig__) | 设置云端的混流转码参数。     |

### 视频相关接口函数

| API                                                          | 描述                          |
| ------------------------------------------------------------ | ----------------------------- |
| [startLocalPreview](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_startLocalPreview_System_Boolean_System_Object_) | 开启本地视频的预览画面，目前仅支持自定义渲染。      |
| [stopLocalPreview](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopLocalPreview) | 停止本地视频采集及预览。      |
| [muteLocalVideo](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_muteLocalVideo_System_Boolean_) | 暂停/恢复推送本地的视频数据。      |
| [startRemoteView](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_startRemoteView_System_String_trtc_TRTCVideoStreamType_System_Object_) | 开始拉取并显示指定用户的远端画面，目前仅支持自定义渲染。      |
| [stopRemoteView](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopRemoteView_System_String_trtc_TRTCVideoStreamType_) | 停止显示远端视频画面，同时不再拉取该远端用户的视频数据流。     |
| [stopAllRemoteView](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopAllRemoteView) | 停止显示所有远端视频画面，同时不再拉取远端用户的视频数据流。     |
| [muteRemoteVideoStream](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_muteRemoteVideoStream_System_String_System_Boolean_) | 暂停/恢复接收指定的远端视频流。     |
| [muteAllRemoteVideoStreams](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_muteAllRemoteVideoStreams_System_Boolean_) | 暂停/恢复接收所有远端视频流。    |
| [setVideoEncoderParam](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setVideoEncoderParam_trtc_TRTCVideoEncParam__) | 设置视频编码器相关参数。    |
| [setNetworkQosParam](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setNetworkQosParam_trtc_TRTCNetworkQosParam__) | 设置网络流控相关参数。    |
| [setVideoEncoderMirror](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setVideoEncoderMirror_System_Boolean_) | 设置编码器输出的画面镜像模式。    |

### 音频相关接口函数

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [startLocalAudio](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_startLocalAudio_trtc_TRTCAudioQuality_) | 开启本地音频的采集和上行。                                   |
| [stopLocalAudio](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopLocalAudio) | 关闭本地音频的采集和上行。                                   |
| [muteLocalAudio](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_muteLocalAudio_System_Boolean_) | 静音/取消静音本地的音频。                                    |
| [muteRemoteAudio](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_muteRemoteAudio_System_String_System_Boolean_) | 静音/取消静音指定的远端用户的声音。                       |
| [muteAllRemoteAudio](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_muteAllRemoteAudio_System_Boolean_) | 静音/取消静音所有用户的声音。                                |
| [setRemoteAudioVolume](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setRemoteAudioVolume_System_String_System_Int32_) | 设置某个远程用户的播放音量。                                |
| [setAudioCaptureVolume](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setAudioCaptureVolume_System_Int32_) | 设置 SDK 采集音量。                                          |
| [getAudioCaptureVolume](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_getAudioCaptureVolume) | 获取 SDK 采集音量。                                          |
| [setAudioPlayoutVolume](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setAudioPlayoutVolume_System_Int32_) | 设置 SDK 播放音量。                                          |
| [getAudioPlayoutVolume](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_getAudioPlayoutVolume) | 获取 SDK 播放音量。                                          |
| [enableAudioVolumeEvaluation](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_enableAudioVolumeEvaluation_System_UInt32_) | 启用音量大小提示。                                         |
| [startAudioRecording](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_startAudioRecording_trtc_TRTCAudioRecordingParams__) | 开始录音。                                                   |
| [stopAudioRecording](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopAudioRecording) | 停止录音。                                                   |

### 设备管理接口

| API | 描述 |
|-----|-----|
| [getDeviceManager](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_getDeviceManager) | 获取设备管理模块。接口详情请参见 [设备管理详细接口](#equipment)。 |


### 音乐特效和人声特效

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [getAudioEffectManager](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_getAudioEffectManager) | 获取音效管理类 TXAudioEffectManager，用于管理BGM，短音效和人声特效。接口详情见 [音效管理详细接口](#music)。 |

### 自定义视频渲染

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [setLocalVideoRenderCallback](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setLocalVideoRenderCallback_trtc_TRTCVideoPixelFormat_trtc_TRTCVideoBufferType_trtc_ITRTCVideoRenderCallback_) | 设置本地视频自定义渲染。              |
| [setRemoteVideoRenderCallback](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setRemoteVideoRenderCallback_System_String_trtc_TRTCVideoPixelFormat_trtc_TRTCVideoBufferType_trtc_ITRTCVideoRenderCallback_) | 设置远端视频自定义渲染。             |

### 自定义消息发送

| API                                                          | 描述                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [sendSEIMsg](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_sendSEIMsg_System_Byte___System_Int32_System_Int32_) | 将小数据量的自定义数据嵌入视频帧中。                                          |


### 网络测试

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [startSpeedTest](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_startSpeedTest_System_Int32_System_String_System_String_) | 开始进行网络测速（视频通话期间请勿测试，以免影响通话质量）。 |
| [stopSpeedTest](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopSpeedTest) | 停止服务器测速。                                             |


### Log 相关接口函数

| API                                                          | 描述                        |
| ------------------------------------------------------------ | --------------------------- |
| [getSDKVersion](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_getSDKVersion) | 获取 SDK 版本信息。         |
| [setLogLevel](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setLogLevel_trtc_TRTCLogLevel_) | 设置 Log 输出级别。         |
| [setLogDirPath](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setLogDirPath_System_String_) | 修改日志保存路径。         |
| [setLogCompressEnabled](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_setLogCompressEnabled_System_Boolean_) | 启用或禁用 Log 的本地压缩。         |
| [callExperimentalAPI](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_callExperimentalAPI_System_String_) | 启用或禁用 Log 的本地压缩。         |



## ITRTCCloudCallback

腾讯云音频通话功能的事件回调接口。

### 错误事件和警告事件

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [onError](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onError_trtc_TXLiteAVError_String_IntPtr_) | 错误回调，表示 SDK 不可恢复的错误，一定要监听并分情况给用户适当的界面提示。 |
| [onWarning](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onWarning_trtc_TXLiteAVWarning_String_IntPtr_) | 警告回调，用于告知您一些非严重性问题，例如出现卡顿或者可恢复的解码失败。 |


### 房间事件回调

| API                                                          | 描述                                |
| ------------------------------------------------------------ | ----------------------------------- |
| [onEnterRoom](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onEnterRoom_System_Int32_) | 已加入房间的回调。                  |
| [onExitRoom](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onExitRoom_System_Int32_) | 离开房间的事件回调。                |
| [onSwitchRole](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onSwitchRole_trtc_TXLiteAVError_String_) | 切换角色的事件回调。                |
| [onConnectOtherRoom](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onConnectOtherRoom_System_String_trtc_TXLiteAVError_System_String_) | 请求跨房通话（主播 PK）的结果回调。         |
| [onDisConnectOtherRoom](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onDisconnectOtherRoom_trtc_TXLiteAVError_System_String_) | 结束跨房通话（主播 PK）的结果回调。        |
| [onSwitchRoom](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_switchRoom_trtc_TRTCSwitchRoomConfig_) | 切换房间 (switchRoom) 的结果回调      |


### 成员事件回调

| API                                                          | 描述                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| [onRemoteUserEnterRoom](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onRemoteUserEnterRoom_String_) | 有用户加入当前房间。                |
| [onRemoteUserLeaveRoom](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onRemoteUserLeaveRoom_String_System_Int32_) | 有用户离开当前房间。                |
| [onUserVideoAvailable](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onUserVideoAvailable_String_System_Boolean_) | 用户是否开启摄像头视频。                |
| [onUserAudioAvailable](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onUserAudioAvailable_String_System_Boolean_) | 远端用户是否存在可播放的音频数据。        |
| [onFirstVideoFrame](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onFirstVideoFrame_String_trtc_TRTCVideoStreamType_System_Int32_System_Int32_) | 开始渲染本地或远程用户的首帧画面。                |
| [onFirstAudioFrame](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onFirstAudioFrame_String_) | 开始播放远程用户的首帧音频（本地声音暂不通知）。   |
| [onSendFirstLocalVideoFrame](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onSendFirstLocalVideoFrame_trtc_TRTCVideoStreamType_) | 首帧本地视频数据已经被送出。              |
| [onSendFirstLocalAudioFrame](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onSendFirstLocalAudioFrame) | 首帧本地音频数据已经被送出。       |


### 统计和质量回调

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [onNetworkQuality](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onNetworkQuality_trtc_TRTCQualityInfo_trtc_TRTCQualityInfo___UInt32_) | 网络质量，该回调每2秒触发一次，统计当前网络的上行和下行质量。 |
| [onStatistics](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onStatistics_trtc_TRTCStatistics_) | 技术指标统计回调。                          |


### 服务器事件回调

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [onConnectionLost](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onConnectionLost) | SDK 跟服务器的连接断开。                |
| [onTryToReconnect](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onTryToReconnect) | SDK 尝试重新连接到服务器。                |
| [onConnectionRecovery](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onConnectionRecovery) | SDK 跟服务器的连接恢复。         |
| [onSpeedTest](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onSpeedTest_trtc_TRTCSpeedTestResult_System_Int32_System_Int32_) | 服务器测速的回调，SDK 对多个服务器 IP 做测速，每个 IP 的测速结果通过这个回调通知。 |


### 硬件设备事件回调

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [onCameraDidReady](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onCameraDidReady) | 摄像头准备就绪。                |
| [onMicDidReady](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onMicDidReady) | 麦克风准备就绪。                         |
| [onUserVoiceVolume](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onUserVoiceVolume_trtc_TRTCVolumeInfo___UInt32_UInt32_) | 用于提示音量大小的回调，包括每个 userId 的音量和远端总音量。 |
| [onDeviceChange](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onDeviceChange_String_trtc_TRTCDeviceType_trtc_TRTCDeviceState_) |本地设备通断回调。                |



[](id:reback)

### 自定义消息的接收回调

| API                                                          | 描述                  |
| ------------------------------------------------------------ | --------------------- |
| [onRecvSEIMsg](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onRecvSEIMsg_String_Byte___UInt32_) | 收到 SEI 消息的回调。 |

[](id:cdn)

### CDN 旁路转推回调

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [onStartPublishing](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onStartPublishing_System_Int32_String_) | 开始向腾讯云的直播 CDN 推流的回调，对应于 [TRTCCloud](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_startPublishing_System_String_trtc_TRTCVideoStreamType_) 中的 startPublishing() 接口。 |
| [onStopPublishing](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onStopPublishing_System_Int32_String_) | 停止向腾讯云的直播 CDN 推流的回调，对应于 [TRTCCloud](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloud.html#trtc_ITRTCCloud_stopPublishing) 中的 stopPublishing() 接口。 |
| [onStartPublishCDNStream](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onStartPublishCDNStream_System_Int32_String_) |启动旁路推流到 CDN 完成的回调。                |
| [onStopPublishCDNStream](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onStopPublishCDNStream_System_Int32_String_) |停止旁路推流到 CDN 完成的回调。                |
| [onSetMixTranscodingConfig](https://testcomm.qq.com/trtc/api/api/trtc.ITRTCCloudCallback.html#trtc_ITRTCCloudCallback_onSetMixTranscodingConfig_System_Int32_String_) |设置云端的混流转码参数的回调，对应于 TRTCCloud 中的 setMixTranscodingConfig() 接口。                |

[](id:key)

## 关键类型定义

| 类名                                                         | 描述                                    |
| ------------------------------------------------------------ | --------------------------------------- |
| [TRTCParams](https://testcomm.qq.com/trtc/api/api/trtc.TRTCParams.html) | 进房参数。                           |
| [TRTCVideoEncParam](https://testcomm.qq.com/trtc/api/api/trtc.TRTCVideoEncParam.html) | 视频编码参数。                           |
| [TRTCTranscodingConfig](https://testcomm.qq.com/trtc/api/api/trtc.TRTCTranscodingConfig.html) | 云端混流（转码）配置。                           |
| [TRTCSwitchRoomConfig](https://testcomm.qq.com/trtc/api/api/trtc.TRTCSwitchRoomConfig.html) | 切换房间参数参数。                              |
| [TRTCNetworkQosParam](https://testcomm.qq.com/trtc/api/api/trtc.TRTCNetworkQosParam.html) | 网络流控相关参数。                      |
| [TXVoiceReverbType](https://testcomm.qq.com/trtc/api/api/trtc.TXVoiceReverbType.html) | 变声类型定义（KTV、小房间、大会堂、低沉、洪亮...）。 |
| [AudioMusicParam](https://testcomm.qq.com/trtc/api/api/trtc.AudioMusicParam.html) | 音乐和人声设置接口参数。 |
| [TRTCAudioRecordingParams](https://testcomm.qq.com/trtc/api/api/trtc.TRTCAudioRecordingParams.html) | 录音参数。 |

[](id:equipment)

## 设备管理详细接口

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [isFrontCamera](https://testcomm.qq.com/trtc/api/api/trtc.ITXDeviceManager.html#trtc_ITXDeviceManager_isFrontCamera) | 判断当前是否为前置摄像头。                           |
| [switchCamera](https://testcomm.qq.com/trtc/api/api/trtc.ITXDeviceManager.html#trtc_ITXDeviceManager_switchCamera_System_Boolean_) | 切换摄像头。                           |
| [getCameraZoomMaxRatio](https://testcomm.qq.com/trtc/api/api/trtc.ITXDeviceManager.html#trtc_ITXDeviceManager_getCameraZoomMaxRatio) | 查询当前摄像头支持的最大缩放比例。                           |
| [setCameraZoomRatio](https://testcomm.qq.com/trtc/api/api/trtc.ITXDeviceManager.html#trtc_ITXDeviceManager_setCameraZoomRatio_System_Double_) | 设置当前摄像头的缩放比例。                           |
| [isAutoFocusEnabled](https://testcomm.qq.com/trtc/api/api/trtc.ITXDeviceManager.html#trtc_ITXDeviceManager_isAutoFocusEnabled) | 查询是否支持自动识别人脸位置。                           |
| [enableCameraAutoFocus](https://testcomm.qq.com/trtc/api/api/trtc.ITXDeviceManager.html#trtc_ITXDeviceManager_enableCameraAutoFocus_System_Boolean_) | 设置人脸自动识别。                           |
| [setCameraFocusPosition](https://testcomm.qq.com/trtc/api/api/trtc.ITXDeviceManager.html#trtc_ITXDeviceManager_setCameraFocusPosition_System_Int32_System_Int32_) | 设置摄像头焦点。                           |
| [enableCameraTorch](https://testcomm.qq.com/trtc/api/api/trtc.ITXDeviceManager.html#trtc_ITXDeviceManager_enableCameraTorch_System_Boolean_) | 开关闪光灯。                           |
| [setSystemVolumeType](https://testcomm.qq.com/trtc/api/api/trtc.ITXDeviceManager.html#trtc_ITXDeviceManager_setSystemVolumeType_trtc_TXSystemVolumeType_) | 设置通话时使用的系统音量类型。 |
| [setAudioRoute](https://testcomm.qq.com/trtc/api/api/trtc.ITXDeviceManager.html#trtc_ITXDeviceManager_setAudioRoute_trtc_TXAudioRoute_) | 设置音频路由。 |

[](id:music)

## 音乐特效和人声特效详细接口

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [setVoiceReverbType](https://testcomm.qq.com/trtc/api/api/trtc.ITXAudioEffectManager.html#trtc_ITXAudioEffectManager_setVoiceReverbType_trtc_TXVoiceReverbType_) | 设置人声的混响效果（KTV、小房间、大会堂、低沉、洪亮...）。 |
| [setMusicObserver](https://testcomm.qq.com/trtc/api/api/trtc.ITXAudioEffectManager.html#trtc_ITXAudioEffectManager_setMusicObserver_System_Int32_trtc_ITXMusicPlayObserver_) | 设置背景音乐的播放进度回调接口。 |
| [startPlayMusic](https://testcomm.qq.com/trtc/api/api/trtc.ITXAudioEffectManager.html#trtc_ITXAudioEffectManager_startPlayMusic_trtc_AudioMusicParam_) | 开始播放背景音乐。 |
| [stopPlayMusic](https://testcomm.qq.com/trtc/api/api/trtc.ITXAudioEffectManager.html#trtc_ITXAudioEffectManager_stopPlayMusic_System_Int32_) | 停止播放背景音乐。 |
| [pausePlayMusic](https://testcomm.qq.com/trtc/api/api/trtc.ITXAudioEffectManager.html#trtc_ITXAudioEffectManager_pausePlayMusic_System_Int32_) | 暂停播放背景音乐。 |
| [resumePlayMusic](https://testcomm.qq.com/trtc/api/api/trtc.ITXAudioEffectManager.html#trtc_ITXAudioEffectManager_resumePlayMusic_System_Int32_) | 恢复播放背景音乐。 |
| [setMusicPublishVolume](https://testcomm.qq.com/trtc/api/api/trtc.ITXAudioEffectManager.html#trtc_ITXAudioEffectManager_setMusicPublishVolume_System_Int32_System_Int32_) | 设置背景音乐的远端音量大小，即主播可以通过此接口设置远端观众能听到的背景音乐的音量大小。 |
| [setMusicPlayoutVolume](https://testcomm.qq.com/trtc/api/api/trtc.ITXAudioEffectManager.html#trtc_ITXAudioEffectManager_setMusicPlayoutVolume_System_Int32_System_Int32_) | 设置背景音乐的本地音量大小，即主播可以通过此接口设置主播自己本地的背景音乐的音量大小。 |
| [setAllMusicVolume](https://testcomm.qq.com/trtc/api/api/trtc.ITXAudioEffectManager.html#trtc_ITXAudioEffectManager_setAllMusicVolume_System_Int32_) | 设置全局背景音乐的本地和远端音量的大小。 |
| [setMusicPitch](https://testcomm.qq.com/trtc/api/api/trtc.ITXAudioEffectManager.html#trtc_ITXAudioEffectManager_setMusicPitch_System_Int32_System_Double_) | 调整背景音乐的音调高低。 |
| [setMusicSpeedRate](https://testcomm.qq.com/trtc/api/api/trtc.ITXAudioEffectManager.html#trtc_ITXAudioEffectManager_setMusicSpeedRate_System_Int32_System_Double_) | 调整背景音乐的变速效果。 |
| [getMusicCurrentPosInMS](https://testcomm.qq.com/trtc/api/api/trtc.ITXAudioEffectManager.html#methods) | 获取背景音乐当前的播放进度（单位：毫秒） |
| [seekMusicToPosInMS](https://testcomm.qq.com/trtc/api/api/trtc.ITXAudioEffectManager.html#trtc_ITXAudioEffectManager_seekMusicToPosInMS_System_Int32_System_Int32_) | 设置背景音乐的播放进度（单位：毫秒） |
| [getMusicDurationInMS](https://testcomm.qq.com/trtc/api/api/trtc.ITXAudioEffectManager.html#trtc_ITXAudioEffectManager_getMusicDurationInMS_System_String_)|获取景音乐文件的总时长（单位：毫秒）|

## TRTCCloud

### 基础方法

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [createInstance](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#.createInstance) | 创建 TrtcCloud 单例。 |
| [destroyInstance](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#.destroyInstance) | 销毁 TrtcCloud 单例。 |
| [on](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#on) | 设置 TrtcCloud 事件监听。 |
| [off](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#off) | 移除 TrtcCloud 事件监听。 |

### 房间相关接口函数

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [enterRoom](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#enterRoom) | 进入房间。           |
| [exitRoom](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#exitRoom) | 离开房间。                                                   |
| [switchRole](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#switchRole) | 切换角色，仅适用于直播场景（TRTCAppSceneLIVE 和 TRTCAppSceneVoiceChatRoom）。 |


### 视频相关接口函数

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [startLocalPreview](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#startLocalPreview) | 开启本地视频的预览画面。                                     |
| [stopLocalPreview](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#stopLocalPreview) | 停止本地视频采集及预览。                                     |
| [muteLocalVideo](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#muteLocalVideo) | 暂停/恢复推送本地的视频数据。                                |
| [startRemoteView](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#startRemoteView) | 开始显示远端视频画面。                                       |
| [stopRemoteView](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#stopRemoteView) | 停止显示远端视频画面，同时不再拉取该远端用户的视频数据流。   |
| [setLocalRenderParams](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#setLocalRenderParams) | 设置本地图像的渲染模式。 |
| [setRemoteRenderParams](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#setRemoteRenderParams) | 设置远端图像相关参数。 |
| [snapshotVideo](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#snapshotVideo) | 视频画面截图。 |


### 音频相关接口函数

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [startLocalAudio](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#startLocalAudio) | 开启本地音频的采集和上行。                                   |
| [stopLocalAudio](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#stopLocalAudio) | 关闭本地音频的采集和上行。                                   |
| [muteLocalAudio](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#muteLocalAudio) | 静音/取消静音本地的音频。                                    |
| [setAudioRoute](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#setAudioRoute) | 设置音频路由。                                               |
| [muteRemoteAudio](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#muteRemoteAudio) | 静音/取消静音指定的远端用户的声音。                          |
| [muteAllRemoteAudio](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#muteAllRemoteAudio) | 静音/取消静音所有用户的声音。                                |
| [enableAudioVolumeEvaluation](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#enableAudioVolumeEvaluation) | 启用音量大小提示。                                           |


### 美颜滤镜相关接口函数

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [setBeautyLevel](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#setBeautyLevel) | 设置美颜级别。 |
| [setBeautyStyle](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#setBeautyStyle) | 设置美颜（磨皮）算法 TRTC 内置多种不同的磨皮算法，您可以选择最适合您产品定位的方案。 |


### 辅流相关接口函数

| API                                                          | 描述           |
| ------------------------------------------------------------ | -------------- |
| [startScreenCapture](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#startScreenCapture) | 启动屏幕分享。 |
| [stopScreenCapture](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#stopScreenCapture) | 停止屏幕采集。 |
| [pauseScreenCapture](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#pauseScreenCapture) | 暂停屏幕分享。 |
| [resumeScreenCapture](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#resumeScreenCapture) | 恢复屏幕分享。 |



## TRTCCloudListener

腾讯云视频通话功能的事件回调接口。

### 错误事件和警告事件

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [onError](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onError) | 错误回调，表示 SDK 不可恢复的错误，一定要监听并分情况给用户适当的界面提示。 |
| [onWarning](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onWarning) | 警告回调，用于告知您一些非严重性问题，例如出现卡顿或者可恢复的解码失败。 |


### 房间事件回调

| API                                                          | 描述                                |
| ------------------------------------------------------------ | ----------------------------------- |
| [onEnterRoom](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onEnterRoom) | 已加入房间的回调。                  |
| [onExitRoom](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onExitRoom) | 离开房间的事件回调。                |
| [onSwitchRole](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onSwitchRole) | 切换角色的事件回调。                |

### 成员事件回调

| API                                                          | 描述                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| [onRemoteUserEnterRoom](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onRemoteUserEnterRoom) | 有用户加入当前房间。                |
| [onRemoteUserLeaveRoom](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onRemoteUserLeaveRoom) | 有用户离开当前房间。                |
| [onUserVideoAvailable](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onUserVideoAvailable) | 远端用户是否存在可播放的主路画面（一般用于摄像头）。 |
| [onUserSubStreamAvailable](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onUserSubStreamAvailable) | 远端用户是否存在可播放的辅路画面（一般用于屏幕分享）。 |
| [onUserAudioAvailable](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onUserAudioAvailable) | 远端用户是否存在可播放的音频数据。        |
| [onFirstVideoFrame](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onFirstVideoFrame) | 开始渲染本地或远程用户的首帧画面。           |
| [onFirstAudioFrame](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onFirstAudioFrame) | 开始播放远程用户的首帧音频（本地声音暂不通知）。   |
| [onSendFirstLocalVideoFrame](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onSendFirstLocalVideoFrame) | 首帧本地视频数据已经被送出。    |
| [onSendFirstLocalAudioFrame](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onSendFirstLocalAudioFrame) | 首帧本地音频数据已经被送出。       |



### 硬件设备事件回调

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [onUserVoiceVolume](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onUserVoiceVolume) | 用于提示音量大小的回调，包括每个 userId 的音量和远端总音量。 |



### 屏幕分享回调

| API                                                          | 描述             |
| ------------------------------------------------------------ | ---------------- |
| [onScreenCaptureStarted](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onScreenCaptureStarted) | 当屏幕分享开始时，SDK 会通过此回调通知 |
| [onScreenCapturePaused](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onScreenCapturePaused) | 当屏幕分享调用 pauseScreenCapture() 暂停时，SDK 会通过此回调通知。 |
| [onScreenCaptureResumed](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onScreenCaptureResumed) | 当屏幕分享调用 resumeScreenCapture() 恢复时，SDK 会通过此回调通知。 |
| [onScreenCaptureStopped](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onScreenCaptureStopped) | 当屏幕分享停止时，SDK 会通过此回调通知。 |

### 截图回调

| API                                                          | 描述             |
| ------------------------------------------------------------ | ---------------- |
| [onSnapshotComplete](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onSnapshotComplete) | 截图完成时回调。 |


## 关键类型定义

| 类名                                                         | 描述                                    |
| ------------------------------------------------------------ | --------------------------------------- |
| [TRTCParams](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/global.html#TRTCParams) | 进房参数。                              |
| [TRTCVideoEncParam](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/global.html#TRTCVideoEncParam) | 视频编码参数。                              |
| [TRTCRenderParams](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/global.html#TRTCRenderParams) | 远端图像参数。 |

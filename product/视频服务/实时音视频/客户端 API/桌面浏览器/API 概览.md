## 支持的平台

WebRTC 技术由 Google 最先提出，目前主要在桌面版 Chrome 浏览器、桌面版 Safari 浏览器以及移动版 Safari 浏览器上有较为完整的支持，其他平台（例如 Android 平台的浏览器）支持情况均比较差。
- 在移动端推荐使用 [小程序](https://cloud.tencent.com/document/product/647/17018) 解决方案，微信和手机 QQ 小程序均已支持，都是由各平台的 Native 技术实现，音视频性能更好，且针对主流手机品牌进行了定向适配。
- 如果您的应用场景主要为教育场景，那么教师端推荐使用稳定性更好的 [Electron](https://cloud.tencent.com/document/product/647/38549) 解决方案，支持大小双路画面，更灵活的屏幕分享方案以及更强大的弱网络恢复能力。

<table>
<thead><tr><th width="15%">操作系统</th>
<th width="24%">浏览器类型</th>
<th>浏览器最低<br>版本要求</th>
<th>接收（播放）</th>
<th>发送（上麦）</th>
<th>屏幕分享</th>
</tr>
</thead>
<tbody><tr>
<td>Mac OS</td>
<td>桌面版 Safari 浏览器</td>
<td>11+</td>
<td>支持</td>
<td>支持</td>
<td>支持（需要  Safari 13+ 版本）</td>
</tr><tr>
<td>Mac OS</td>
<td>桌面版 Chrome 浏览器</td>
<td>56+</td>
<td>支持</td>
<td>支持</td>
<td>支持（需要 Chrome 72+ 版本）</td>
</tr><tr>
<td>Mac OS</td>
<td>桌面版 Firefox 浏览器</td>
<td>56+</td>
<td>支持</td>
<td>支持</td>
<td>支持（需要 Firefox 66+ 版本）</td>
</tr><tr>
<td>Mac OS</td>
<td>桌面版 Edge 浏览器</td>
<td>80+</td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
</tr><tr>
<td>Windows</td>
<td>桌面版 Chrome 浏览器</td>
<td>56+</td>
<td>支持</td>
<td>支持</td>
<td>支持（需要 Chrome 72+ 版本）</td>
</tr><tr>
<td>Windows</td>
<td>桌面版 QQ 浏览器（极速内核）</td>
<td>10.4+</td>
<td>支持</td>
<td>支持</td>
<td>不支持</td>
</tr><tr>
<td>Windows</td>
<td>桌面版 Firefox 浏览器</td>
<td>56+</td>
<td>支持</td>
<td>支持</td>
<td>支持（需要 Firefox 66+ 版本）</td>
</tr><tr>
<td>Windows</td>
<td>桌面版 Edge 浏览器</td>
<td>80+</td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
</tr><tr>
<td>iOS 11.1.2+</td>
<td>移动版 Safari 浏览器</td>
<td>11+</td>
<td>支持</td>
<td>支持</td>
<td>不支持</td>
</tr><tr>
<td>iOS 12.1.4+</td>
<td>微信内嵌网页</td>
<td>-</td>
<td>支持</td>
<td>不支持</td>
<td>不支持</td>
</tr><tr>
<td>Android</td>
<td>移动版 QQ 浏览器</td>
<td>-</td>
<td>不支持</td>
<td>不支持</td>
<td>不支持</td>
</tr><tr>
<td>Android</td>
<td>移动版 UC 浏览器</td>
<td>-</td>
<td>不支持</td>
<td>不支持</td>
<td>不支持</td>
</tr><tr>
<td>Android</td>
<td>微信内嵌网页（TBS 内核）</td>
<td>-</td>
<td>支持</td>
<td>支持</td>
<td>不支持</td>
</tr><tr>
<td>Android</td>
<td>微信内嵌网页（XWEB 内核）</td>
<td>-</td>
<td>支持</td>
<td>不支持</td>
<td>不支持</td>
</tr>
</tbody></table>

## API 使用指引
详细的 API 使用介绍请参见以下指引：

| 功能                       | Sample Code 指引                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 基础音视频通话             | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-01-basic-video-call.html)                      |
| 互动直播                   | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-02-live-video.html)                            |
| 切换摄像头和麦克风         | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-03-advanced-switch-camera-mic.html)            |
| 设置本地视频属性           | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-04-advanced-set-video-profile.html)            |
| 动态关闭打开本地音频或视频 | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-05-advanced-dynamic-add-video.html)            |
| 屏幕分享                   | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-06-advanced-screencast.html)                   |
| 音量大小检测               | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-07-advanced-detect-volume.html)                |
| 自定义采集与自定义播放渲染 | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-08-advanced-customized-capture-rendering.html) |
| 房间内上行用户个数限制     | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-09-advanced-uplink-limits.html)                |
| 背景音乐和音效实现方案     | [指引链接](https://trtc-1252463788.file.myqcloud.com/web/docs/tutorial-12-advanced-audio-mixer.html)                  |


## TRTC

>!本文适用于4.x.x版本的 TRTC 桌面浏览器 SDK。

TRTC 是 [TRTC 桌面浏览器 SDK](https://trtc-1252463788.file.myqcloud.com/web/docs/index.html) 的主入口，通过 TRTC 方法可以创建一个实时音视频通信的客户端对象（Client）和本地音视频流对象（Stream）。TRTC 方法还可以检测浏览器的兼容性，是否支持屏幕分享，以及设置日志级别及日志上传。

| API                                                                                                              | 描述                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [VERSION](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.html#.VERSION)                                 | TRTC 桌面浏览器 SDK 版本号。                                                                                                                                  |
| [checkSystemRequirements](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.html#.checkSystemRequirements) | 检测浏览器是否兼容 TRTC 桌面浏览器 SDK。若当前浏览器不兼容 TRTC 桌面浏览器 SDK，建议引导用户去下载最新版本的 Chrome 浏览器。                                  |
| [isScreenShareSupported](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.html#.isScreenShareSupported)   | 检测浏览器是否支持屏幕分享。在创建屏幕分享流之前请调用该方法检查当前浏览器是否支持屏幕分享。                                                                  |
| [getDevices](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.html#.getDevices)                           | 返回媒体输入输出设备列表。                                                                                                                                    |
| [getCameras](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.html#.getCameras)                           | 返回摄像头设备列表。                                                                                                                                          |
| [getMicrophones](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.html#.getMicrophones)                   | 返回麦克风设备列表。                                                                                                                                          |
| [getSpeakers](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.html#.getSpeakers)                         | 返回扬声器设备列表。                                                                                                                                          |
| [createClient](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.html#.createClient)                       | 创建一个实时音视频通话的客户端对象，在每次会话中仅需要调用一次。                                                                                              |
| [createStream](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.html#.createStream)                       | 创建一个本地流 Stream 对象，本地流 Stream 对象通过 [publish()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#publish) 方法发布本地音视频流。 |

## TRTC.Logger

提供日志设置方法，包括设置 [日志输出等级](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.Logger.html#.LogLevel)、打开或关闭日志上传。

| API                                                                                                       | 描述               |
| --------------------------------------------------------------------------------------------------------- | ------------------ |
| [setLogLevel](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.Logger.html#.setLogLevel)           | 设置日志输出等级。 |
| [enableUploadLog](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.Logger.html#.enableUploadLog)   | 打开日志上传。     |
| [disableUploadLog](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.Logger.html#.disableUploadLog) | 关闭日志上传。     |

## Client

音视频通话客户端对象 Client 通过 [createClient()](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.html#.createClient) 创建，代表一次音视频会话。

| API                                                                                                       | 描述                                                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [setProxyServer](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#setProxyServer)           | 设置代理服务器。该方法适用于企业自己部署代理服务器，如 nginx+coturn 方案。                                                                                                      |
| [setTurnServer](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#setTurnServer)             | 设置 TURN 服务器。该方法配合 [setProxyServer()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#setProxyServer) 使用，适用于企业自己部署代理服务器和 TURN 中转。 |
| [join](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#join)                               | 加入一个音视频通话房间，进房代表开始一个音视频通话会话。若房间不存在，系统将自动创建一个新房间。                                                                                |
| [leave](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#leave)                             | 退出当前音视频通话房间，结束一次音视频通话会话。                                                                                                                                |
| [publish](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#publish)                         | 发布本地音视频流。该方法需要在 [join()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#join) 进房后调用，一次音视频会话中只能发布一个本地流。                   |
| [unpublish](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#unpublish)                     | 取消发布本地流。                                                                                                                                                                |
| [subscribe](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#subscribe)                     | 订阅远端流。                                                                                                                                                                    |
| [unsubscribe](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#unsubscribe)                 | 取消订阅远端流。                                                                                                                                                                |
| [switchRole](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#switchRole)                   | 切换用户角色，仅在 ‘live’ 互动直播模式下生效。                                                                                                                                  |
| [on](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#on)                                   | 监听客户端对象事件。                                                                                                                                                            |
| [getRemoteMutedState](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#getRemoteMutedState) | 获取当前房间内远端用户音视频 mute 状态列表。                                                                                                                                    |
| [getLocalAudioStats](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#getLocalAudioStats)   | 获取当前已发布本地流的音频统计数据。该方法需要在 [publish()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#publish) 后调用。                                   |
| [getLocalVideoStats](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#getLocalVideoStats)   | 获取当前已发布本地流的视频统计数据。该方法需要在 [publish()](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#publish) 后调用。                                   |
| [getRemoteAudioStats](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#getRemoteAudioStats) | 获取当前所有远端流的音频统计数据。                                                                                                                                              |
| [getRemoteVideoStats](https://trtc-1252463788.file.myqcloud.com/web/docs/Client.html#getRemoteVideoStats) | 获取当前所有远端流的视频统计数据。                                                                                                                                              |

## LocalStream

LocalStream 本地音视频流，通过 [createStream](https://trtc-1252463788.file.myqcloud.com/web/docs/TRTC.html#.createStream) 创建，是 [Stream](https://trtc-1252463788.file.myqcloud.com/web/docs/Stream.html) 的子类。

| API                                                                                                            | 描述                                                                                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [initialize](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#initialize)                   | 初始化本地音视频流对象。                                                                                                                                                                 |
| [setAudioProfile](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#setAudioProfile)         | 设置音频 Profile。该方法需要在调用 [initialize()](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#initialize) 之前调用。                                             |
| [setVideoProfile](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#setVideoProfile)         | 设置视频 Profile。该方法需要在调用 [initialize()](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#initialize) 之前调用。                                             |
| [setScreenProfile](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#setScreenProfile)       | 设置屏幕分享 Profile。该方法需要在调用 [initialize()](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#initialize) 之前调用。                                         |
| [setVideoContentHint](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#setVideoContentHint) | 设置视频内容提示，主要用于提升在不同场景下的视频编码质量。该方法需要在调用 [initialize()](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#initialize) 成功之后调用。 |
| [switchDevice](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#switchDevice)               | 切换媒体输入设备。                                                                                                                                                                       |
| [addTrack](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#addTrack)                       | 添加音频或视频轨道。                                                                                                                                                                     |
| [removeTrack](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#removeTrack)                 | 移除视频轨道。                                                                                                                                                                           |
| [replaceTrack](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#replaceTrack)               | 更换音频或视频轨道。                                                                                                                                                                     |
| [play](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#play)                               | 播放该音视频流。                                                                                                                                                                         |
| [stop](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#stop)                               | 停止播放音视频流。                                                                                                                                                                       |
| [resume](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#resume)                           | 恢复播放音视频。                                                                                                                                                                         |
| [close](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#close)                             | 关闭音视频流。                                                                                                                                                                           |
| [muteAudio](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#muteAudio)                     | 禁用音频轨道。                                                                                                                                                                           |
| [muteVideo](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#muteVideo)                     | 禁用视频轨道。                                                                                                                                                                           |
| [unmuteAudio](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#unmuteAudio)                 | 启用音频轨道。                                                                                                                                                                           |
| [unmuteVideo](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#unmuteVideo)                 | 启用视频轨道。                                                                                                                                                                           |
| [getId](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#getId)                             | 获取 Stream 唯一标识 ID。                                                                                                                                                                |
| [getUserId](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#getUserId)                     | 获取该流所属的用户 ID。                                                                                                                                                                  |
| [setAudioOutput](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#setAudioOutput)           | 设置声音输出设备。                                                                                                                                                                       |
| [getAudioLevel](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#getAudioLevel)             | 获取当前音量大小。只有当本地流或远端流中有音频数据才有效。                                                                                                                               |
| [hasAudio](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#hasAudio)                       | 是否包含音频轨道。                                                                                                                                                                       |
| [hasVideo](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#hasVideo)                       | 是否包含视频轨道。                                                                                                                                                                       |
| [getAudioTrack](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#getAudioTrack)             | 获取音频轨道。                                                                                                                                                                           |
| [getVideoTrack](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#getVideoTrack)             | 获取视频轨道。                                                                                                                                                                           |
| [getVideoFrame](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#getVideoFrame)             | 获取当前视频帧。                                                                                                                                                                         |
| [on](https://trtc-1252463788.file.myqcloud.com/web/docs/LocalStream.html#on)                                   | 监听 Stream 事件。                                                                                                                                                                       |



## RemoteStream

远端音视频流，通过监听 [Client.on('stream-added')](https://trtc-1252463788.file.myqcloud.com/web/docs/module-Event.html#.STREAM_ADDED) 事件获得。是 [Stream]() 的子类。

| API                                                                                                   | 描述                                                                                               |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| [getType](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#getType)               | 获取远端流类型。主要用于判断一个远端流是主音视频流还是辅路视频流，辅路视频流通常是一个屏幕分享流。 |
| [play](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#play)                     | 播放该音视频流。                                                                                   |
| [stop](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#stop)                     | 停止播放音视频流。                                                                                 |
| [resume](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#resume)                 | 恢复播放音视频。                                                                                   |
| [close](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#close)                   | 关闭音视频流。                                                                                     |
| [muteAudio](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#muteAudio)           | 禁用音频轨道。                                                                                     |
| [muteVideo](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#muteVideo)           | 禁用视频轨道。                                                                                     |
| [unmuteAudio](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#unmuteAudio)       | 启用音频轨道。                                                                                     |
| [unmuteVideo](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#unmuteVideo)       | 启用视频轨道。                                                                                     |
| [getId](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#getId)                   | 获取 Stream 唯一标识 ID。                                                                          |
| [getUserId](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#getUserId)           | 获取该流所属的用户 ID。                                                                            |
| [setAudioOutput](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#setAudioOutput) | 设置声音输出设备。                                                                                 |
| [setAudioVolume](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#setAudioVolume) | 设置播放音量大小。                                                                                 |
| [getAudioLevel](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#getAudioLevel)   | 获取当前音量大小。只有当本地流或远端流中有音频数据才有效。                                         |
| [hasAudio](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#hasAudio)             | 是否包含音频轨道。                                                                                 |
| [hasVideo](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#hasVideo)             | 是否包含视频轨道。                                                                                 |
| [getAudioTrack](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#getAudioTrack)   | 获取音频轨道。                                                                                     |
| [getVideoTrack](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#getVideoTrack)   | 获取视频轨道。                                                                                     |
| [getVideoFrame](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#getVideoFrame)   | 获取当前视频帧。                                                                                   |
| [on](https://trtc-1252463788.file.myqcloud.com/web/docs/RemoteStream.html#on)                         | 监听 Stream 事件。                                                                                 |


## RtcError

RtcError 错误对象。

| API                                                                                 | 描述         |
| ----------------------------------------------------------------------------------- | ------------ |
| [getCode](https://trtc-1252463788.file.myqcloud.com/web/docs/RtcError.html#getCode) | 获取错误码。 |



## 联系我们

关注公众号“腾讯云视频”，给公众号发关键字“技术支持”，会有专人联系。
![](https://main.qcloudimg.com/raw/30ad559e5f1f35dccc56149208aba552.jpg)

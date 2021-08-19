## Version 8.9.102 @ 2021.08.11

**功能新增**
Windows & Mac：onStatistics 回调新增字段 gatewayRtt [onStatistics](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onStatistics)。

**问题修复**
- Mac：修复特殊机型写日志引起 crash。
- Mac：修复禁麦的操作使用 API 接口 setAudioCaptureVolume(0) 后，发现麦克风检测音量为 0。
- Windows：性能优化，修复打开摄像头后黑屏。
- Windows：修复屏幕捕获自动减低分辨率后不恢复。
- Windows & Mac：其他 bug 修复。

## Version 8.6.101 @ 2021.05.28

**功能新增**
- Windows & Mac：新增接口，支持屏幕分享时屏蔽应用窗口：[addExcludedShareWindow](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#addExcludedShareWindow)、[removeExcludedShareWindow](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#removeExcludedShareWindow)、[removeAllExcludedShareWindow](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#removeAllExcludedShareWindow)。
- Windows & Mac：获取可共享的窗口列表接口 [getScreenCaptureSources](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getScreenCaptureSources)，返回值列表元素新增 isMinimizeWindow 字段。
- Windows & Mac：支持构造函数传入参数。

**问题修复**
- Windows：插件加载不支持中文路径问题。
- Windows & Mac：修复 webgl context lost 问题。
- Windows & Mac：开启双路编码，进入房间后，切换小画面视频流，本地显示的远端成员画面卡住问题。
- Windows & Mac：在客户端进房拉流的时候出现远端成员画面先模糊一下，然后逐渐清晰问题。

## Version 8.4.1 @ 2021.03.26

**功能新增**
- Mac：开始支持采集 Mac 操作系统的输出声音[startSystemAudioLoopback](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startSystemAudioLoopback)，也就是跟 Windows 端一样的 SystemLoopback 能力，该功能可以让 SDK 采集当前系统的声音，开启这个功能后，主播就可以很方便地向其他用户直播音乐或者电影文件。
- Mac：系统音频采集回调 [onSystemAudioLoopbackError](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onSystemAudioLoopbackError)，您可以获取系统音频驱动的运行情况。
-  Mac：屏幕分享开始支持本地预览功能，您可以通过一个小窗口像用户展示屏幕分享的预览内容。
- 全平台：支持美颜插件机制。

**质量优化**
- 全平台：优化 [Music](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga865e618ff3a81236f9978723c00e86fb) 模式下的声音质量，更加适合类似 cloubhouse 的语音直播场景。
-  全平台：优化音视频链路的网络抗性，在 70% 的极端查网络环境下，音视频依然较为流畅。
-  Windows：优化部分场景下的直播音质，大幅减少了声音损伤问题。
-  Windows：性能优化，在部分使用场景下的性能较旧版本有 20%-30% 的提升。

**问题修复**
- Mac：修复 Mac mini (m1) 换到全屏分享后，再切回某个窗口，远端还是展示的全屏分享窗口的问题。
- Mac：解决 Mac 下屏幕分享无高亮的问题（Mac 系统 11.1，10.14.5 不出现绿框；Mac 系统 10.3.2 会出现绿框，但放大窗口会闪烁)。
-  Mac：修复 Mac mini m1 获取分享屏幕列表 crash，针对底层 sourceName 为 null 时上层返回""的问题。
-  Mac：修复 Mac mini m1，getCurrentMicDevice 导致 crash (sourceName) 可能为空问题
-  Windows：修复 Windows Server 2019 Datacenter x64 系统上启动桌面分享 crash 的问题。
-  Windows：修复分享窗口的同时改变目标窗口大小会偶发分享意外终止的 BUG。
-  Windows：修复部分型号的摄像头采集不出画面的问题。

## Version 8.2.7 @ 2021.01.06

**新增**
- Windows & Mac：新增 [switchRoom](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#switchRoom) 切换房间。
- Windows & Mac：新增 [setLocalRenderParams](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setLocalRenderParams) 设置本地图像（主流）的渲染参数。
- Windows & Mac：新增 [setRemoteRenderParams](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setRemoteRenderParams) 设置远端图像的渲染参数。
- Windows & Mac：新增 [startPlayMusic](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startPlayMusic) 启动播放背景音乐。
- Windows & Mac：新增 [stopPlayMusic](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopPlayMusic) 停止播放背景音乐。
- Windows & Mac：新增 [pausePlayMusic](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#pausePlayMusic) 暂停播放背景音乐。
- Windows & Mac：新增 [resumePlayMusic](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#resumePlayMusic) 恢复播放背景音乐。
- Windows & Mac：新增 [getMusicDurationInMS](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getMusicDurationInMS) 获取背景音乐文件总时长，单位毫秒。
- Windows & Mac：新增 [seekMusicToPosInTime](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#seekMusicToPosInTime) 设置背景音乐播放进度。
- Windows & Mac：新增 [setAllMusicVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setAllMusicVolume) 设置背景音乐的音量大小，播放背景音乐混音时使用，用来控制背景音音量大小。
- Windows & Mac：新增 [setMusicPlayoutVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setMusicPlayoutVolume) 设置背景音乐本地播放音量的大小。
- Windows & Mac：新增 [setMusicPublishVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setMusicPublishVolume) 设置背景音乐远端播放音量的大小。
- Windows & Mac：新增 [onSwitchRoom](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onSwitchRoom) 切换房间回调。
- Windows & Mac：新增 [setRemoteAudioVolume](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setRemoteAudioVolume) 设置远程用户播放音量。
- Windows & Mac：新增 [snapshotVideo](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#snapshotVideo) 视频画面截图。
- Windows & Mac：新增 [onSnapshotComplete](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onSnapshotComplete) 截图完成时回调。

**改进**
- Windows & Mac：enterRoom 和 switchRoom 支持 string 类型 strRoomId。
- Windows & Mac：其他 bug 修复。

## Version 7.9.348 @ 2020.11.12

**改进**
- Windows：修复录音路径设置不支持中文路径文件夹。
- Windows：窗口捕获指定区域捕获支持抗遮挡。

## Version 7.8.342 @ 2020.10.10

**新增**
- Windows & Mac：新增 [onAudioDeviceCaptureVolumeChanged](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onAudioDeviceCaptureVolumeChanged) 当前音频采集设备音量变化回调。
- Windows & Mac：新增 [onAudioDevicePlayoutVolumeChanged](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCallback.html#event:onAudioDevicePlayoutVolumeChanged) 当前音频播放设备音量变化回调。

## Version 7.7.330 @ 2020.09.11

**新增**
Windows & Mac：新增 [setAudioQuality](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setAudioQuality) 用于设置音频质量。

**改进**
- Windows：优化在某些低端摄像头下 CPU 使用率过高的问题。
- Windows：优化对多款 USB 摄像头和麦克风的兼容性，提升设备的打开成功率。
- Windows：优化摄像头和麦克风设备的选择策略，避免由于摄像头或麦克风在使用中插拔导致的采集异常问题。
- Windows & Mac：其他 bug 修复。

## Version 7.6.300 @ 2020.08.26

**新增**
Windows & Mac：新增 [setCurrentMicDeviceMute](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setCurrentMicDeviceMute) 、[getCurrentMicDeviceMute](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getCurrentMicDeviceMute)、[setCurrentSpeakerDeviceMute](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setCurrentSpeakerDeviceMute)、[getCurrentSpeakerDeviceMute](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#getCurrentSpeakerDeviceMute) 用于控制 PC 的麦克风和扬声器。

## Version 7.5.210 @ 2020.08.11

**改进**
- Windows & Mac：修复 SDK 回调乱序问题。
- Windows & Mac：解决切换渲染模式导致崩溃的问题。 
- Windows & Mac：修复某些分辨率渲染失败的问题。 
- Windows & Mac：其他 bug 修复。

## Version 7.4.204 @ 2020.07.01

**改进**
- Windows：优化 Windows 平台的回声抵消（AEC）效果。
- Windows：增强 Windows 平台的摄像头采集的设备兼容性。
- Windows：增强 Windows 平台的音频设备（麦克风和扬声器）的设备兼容性。
- Windows：修复 Windows 版本 onPlayAudioFrame 回调的 UserID 不正确的问题。
- Windows：64 位支持系统混音

## Version 7.2.174 @ 2020.04.20

**改进**
- Mac：修复 Mac 偶现本地自定义渲染分辨率不一致问题。
- Windows：优化 Windows 端 getCurrentCameraDevice 逻辑，在未使用摄像头时，返回第一个设备作为默认设备。
- Windows：修复高亮窗口在屏幕分享时显示为灰屏的问题。
- Windows：修复 Win10 系统获取屏幕分享缩略图偶现卡死问题。
- Windows & Mac：修复切换角色时，自定义流 ID 偶现未及时生效的问题。
- Windows & Mac：修复屏幕分享设置编码参数不生效的问题。
- Windows：修复 Windows 端屏幕分享后，webrtc 要很久才能看到画面的问题。

## Version 7.1.157 @ 2020.04.02

**新增**

支持使用 [主路](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCVideoStreamType) 进行 [屏幕分享](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startScreenCapture)。

**改进**
- 优化 [混流预设模版](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/global.html#TRTCTranscodingConfigMode) 易用性。
- 优化 [混流](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#setMixTranscodingConfig)，提升成功率。
- 优化 Windows 屏幕分享。


## Version 7.0.149 @ 2020.03.019

**新增**

[trtc.d.ts](https://cloud.tencent.com/document/product/647/38551#.E5.88.9B.E5.BB.BA-trtc-.E5.AF.B9.E8.B1.A1) 文件，方便使用 typescript 的开发者。

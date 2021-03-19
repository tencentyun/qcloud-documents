## Version 7.5 @ 2020.07.31

**新增**

- 新增对双栈 IPV6 和 IPV6 only 的支持。
- 新增进多房间拉流能力，用于支持超级小班课。
- 云端 MCU 混流新增支持设置背景图片（由于监管需要，图片必须先通过 TRTC 控制台进行上传）。
- 云端 MCU 混流新增支持 A+B=>C 和 A+B=>A 两种模式。
- 实时状态回调 onStatistics 新增播放缓冲时长字段 jitterBufferDelay。
- socks5 代理新增支持用户名密码校验。

**优化**

- 降低了端到端的连麦延时，7.5 版本的端到端通话和连麦延时在 7.4 版本的基础上缩短了40%。
- 优化播放端网络抖动评估算法，降低播放延迟。
- 优化采用竖屏分辨率推流时在部分摄像头上帧率极低的问题。

**修复**

- 修复在一个函数中连续调用 playBGM 和 pauseBGM 后播放不生效的问题。
- 修复屏幕分享高亮描边在高DPI情况下位置不对的问题。
- 修复窗口采集时，目标窗口最小化后高亮描边残留的问题。
- 修复  Windows 7 下屏幕分享鼠标闪烁的问题。

##  Version 7.4 @ 2020.06.24 

**优化**

- 优化 Windows 平台的回声抵消（AEC）效果，以避免在开启系统声音回采（startSystemAudioLoopback）后出现的回声问题。
- 增强 Windows 平台的摄像头采集的设备兼容性。
- 增强 Windows 平台的音频设备（麦克风和扬声器）的设备兼容性。
- 耳返支持音量设置。

**修复**

- 修复 Windows 摄像头采集在部分分辨率下视野变小的问题。
- 修复 Windows 版本 onPlayAudioFrame 回调的 UserID 不正确的问题。

  

##  Version 7.3 @ 2020.06.01 

**新增**

- 音频新增瞬态降噪支持，您可以通过 setAudioQuality(TRTCAudioQualitySpeech) 开启。
- 新增变声等音效的能力支持。
- 在兼容老接口的情况下，新增了全新的音效管理接口 TXAudioEffectManager，用于支持更加灵活和多样的音效能力。
- 视频编码参数 setVideoEncoderParam 新增 minVideoBitrate 选项，推荐对画质要求高的直播客户进行设置。

**优化**

- 支持全链路 128kbps 高音质立体声，通过 setAudioQuality(TRTCAudioQualityMusic) 接口即可设置。
- 支持 SPEECH 语音模式，适合会议场景下的语音通话，拥有更强的降噪（ANS）能力，通过 setAudioQuality(TRTCAudioQualitySpeech) 可以设置。
- 支持多路背景音乐并行播放，用于支持原声和伴唱分离的 K 歌场景。同时支持背景音乐循环播放。
- 支持先调用 muteLocalVideo 再调用 startLocalPreview 实现“只预览，不推流”的效果，您也可以通过在 enterRoom 前调用 startLocalPreview 实现该能力。

**修复**

- 修复屏幕分享切换分享目标时播放端卡顿。
- 修复了 MacBook 上使用 BootCamp 运行的 Windows 系统的兼容问题。
- 修复多声道硬件设备采集、播放的无声问题。
- 修复本地音频录制偶现的断断续续的 Bug。
- 修复暂停推流（muteLocalVideo，muteLocalAudio）时，发生强杀或 crash 后重进房，播放端不会自动播放音视频的问题。



## Version 7.2 @ 2020.04.16 

**优化**

优化 Windows 端 getCurrentCameraDevice 逻辑，在未使用摄像头时，返回第一个设备作为默认设备。

**修复**

- 修复 Electron 屏幕分享，高亮窗口在分享时显示为灰屏的问题。
- 修复 Win10 系统获取屏幕分享缩略图偶现卡死问题。
- 修复切换角色时，自定义流 ID 偶现未及时生效的问题。



##  Version 7.1 @ 2020.03.27 

**优化**

- 屏幕分享支持从主路推流。
- 优化混流预设模版易用性。
- 混流优化，提升成功率。

**修复**

- 修复关闭 AERO 时全屏分享看不到透明窗口的问题。
- 修复 win10 缩略图捕获失效。
- 修复 win8.0 及更低版本屏幕采集概率失效问题。
- 修复偶现日志模块死锁问题。
- 修复进房自动旁路的问题。

## Version 7.0 @ 2020.03.09 

**优化**

- 提升 mcu 混流易用性。
- 优化弱网抗抖动能力，弱网下，音频更流畅。

**修复**

- startPublishing 辅路不生效 Bug。
- 解决辅路帧率过低问题。
- 解决停止推流超过30分钟再恢复推流出现音画不同步问题。
- 解决多次交替进退房导致的内存泄露问题。



## Version 6.9 @ 2020.01.14 

**新增**

- enterRoom 参数 TRTCParams 中新增 streamId 属性，用于设定当前用户在 CDN 上的直播流 ID，更方便您绑定直播 CDN。
- enterRoom 参数 TRTCParams 中新增 cloudRecordFileName 属性，您可以设置本次直播在云端录制的文件名。同时我们优化了录制服务对视频流中断的抵抗能力，使得远程录制的文件更加完整。
- 新增场景 TRTCAppSceneAudioCall，在 enterRoom 时可以设置。该场景下，TRTC SDK 针对语音通话进行了全方位的优化。
- 新增场景 TRTCAppSceneVoiceChatRoom，在 enterRoom 时可以设置，可以开启 TRTC SDK 专门针对语音互动聊天室场景所作的各项优化。
- 新增 API：pauseAudioEffect、resumeAudioEffect 音效支持暂停/恢复控制。
- 新增 API：setBGMPlayoutVolume、setBGMPublishVolume，BGM 支持分别设置本地播放和推流混音音量。
- 新增 API：setRemoteSubStreamViewRotation 辅路视频播放支持调整渲染旋转角度。

**优化**

- Windows 优化部分USB设备兼容问题。
- 错误码优化，简化进房错误码。
- 优化偶现秒开慢的问题。
- 视频画面支持 1080P 高分辨率采集，让手机直播 PC 观看的场景获得更佳的画面清晰度。

**修复**

- Windows 修复屏幕采集切换采集窗口后遮挡红框不移除的问题。
- 修复偶现进房失败后无法恢复的问题。



## Version 6.8 @ 2019.11.15 

**新增**

- 新增进房可指定不自动拉流。
- 新增回调 onRemoteUserEnterRoom / onRemoteUserLeaveRoom，支持未上麦的主播进退房通知。

**优化**

- 录屏支持抗遮挡。
- 支持 socks5 代理。
- C# 性能优化。
- pts 生成机制优化。
- 优化网络切换后，自动选择较优的接入点。
- startRemoteView 支持提前调用。

**修复**

- C# 修复移除某个用户的渲染回调后，导致其他用户也无法接收数据。
- 修复已知 crash 等稳定性问题。



##  Version 6.7 @ 2019.09.30 

**新增**

- 新增音效接口支持。
- 新增64位 C# API 支持。

**优化**

- 转推耗时优化。
- 支持单个用户播放音量独立调节能力。



## Version 6.6 Patch @ 2019.09.10 

**新增**

- 新增 AGC 支持，解决部分机型声音小的问题。
- 新增系统音量类型设置接口。
- 新增音效接口，支持播放短音效。



## Version 6.6 @ 2019.08.02 

**新增**

- 新增音频本地录制功能。
- 新增首帧音频、首帧视频发送回调接口。

**优化**

- 进房优化，降低进房耗时，提升进房成功率。
- 支持 mute 远端视频接口。
- 进房错误码统一，通过 onEnterRoom 回调，result&lt;0表示进房错误。
- Demo 优化，新增低延时大房间支持。
- 升级回音消除库，实现系统混音，解决部分采样配置 ANS 不生效、部分机器音量小的问题。

**修复**

修复旁路混流相关的问题。



## Version 6.5 @ 2019.06.12 

**新增**

直播模式（TRTCAppSceneLIVE）新增“低延时大房间”功能：

- 采用专为音视频优化过的 UDP 协议，超强抗弱网能力。
- 平均观看延迟一秒作为，提升观众和主播之间的互动积极性。
- 最多支持10万人进入同一个房间。

**优化**

- 优化音量评估算法（enableAudioVolumeEvaluation），音量评估更灵敏。
- 优化高延迟和高丢包网络环境下的 QoE 算法，增强弱网抗性。 优化 onStatistics 状态回调，仅回调存在的流。
- 优化视频通话（TRTCAppSceneVideoCall）模式下的 QoE 算法，进一步提升 1v1 通话模式下的弱网流畅性。
- 优化弱网下音画不同步的 Bug 。
- 优化先 muteLocalVideo 之后再取消播放端画面的恢复速度。
- 优化直播 TXLivePlayer 播放缓冲逻辑，降低卡顿率。
- 优化 SDK 体积，SDK 体积缩减为原来的 50%。

**修复**

- 修复偶现的 enterRoom 没有回调的 Bug。 优化解码器性能，修复超低端 Android 手机上延迟越来越高的 Bug。
- 修复屏幕分享过程中直接退房，高亮窗口还残留的 Bug。



##  Version 6.4 @ 2019.04.25 

**新增**

- 新增混流 setMixTranscodingConfig API 的设置回调函数。
- 新增基于 Duilib 库的全功能版本 Demo。
- 优化美颜和渲染模块在部分 Windows 版本下的兼容和性能问题。

**优化**

- 提升弱网环境下的流畅度。
- 优化音量大小的回调算法，音量回调数值更加合理。
- 发送自定义音频、视频数据支持外部指定数据帧时间戳。
- 强化 setMixTranscodingConfig 接口，支持 roomID 参数，用于跨房连麦流混流。
- 强化 setMixTranscodingConfig 接口，支持 pureAudio 参数，用于纯语音通话场景下的语音混流和录制。
- 优化摄像头配置选择策略，设备选择支持传 deviceId。

**修复**

- 修复直播（TXLivePlayer）延时可能会升高且不恢复的 Bug。
- 修复设置日志路径为中文路径后日志文件位置异常 Bug。
- 修复直播（TXLivePlayer）播放混流和旁路直播流时音画不同步的 Bug。
- 修复直播屏幕分享参数设置 Bug。



##  Version 6.3 @ 2019.04.02 

**新增**

- 新增自定义视频采集接口：TRTCCloud >> sendCustomVideoData。
- 新增自定义音频采集接口：TRTCCloud >> sendCustomAudioData。
- 新增自定义视频渲染接口：TRTCCloud >> setLocalVideoRenderDelegate + setRemoteVideoRenderDelegate。
- 新增自定义音频数据回调接口：TRTCCloud >> setAudioFrameDelegate，支持：
  - 返回麦克风采集数据：TRTCAudioFrameDelegate >> onCapturedAudioFrame。
  - 返回每一路远程用户的音频数据：TRTCAudioFrameDelegate >> onPlayAudioFrame。
  - 返回混合后送入喇叭播放的音频数据：TRTCAudioFrameDelegate >>onMixedPlayAudioFrame。



## Version 6.2 @ 2019.03.08 

**新增**

新增音频数据回调 ITRTCAudioFrameCallback。

**优化**

- TRTCCloud 类改为纯虚接口 ITRTCCloud，支持通过 LoadLibirary 动态加载 DLL。
- 优化 camera 兼容性及采集性能。



## Version 6.1 @ 2019.01.31 

**优化**

- 支持屏幕分享 。
- 支持观看屏幕分享流 。
- 支持发送自定义视频数据 。
- 优化转推 CDN 和混流实现 。
- 进房区分直播和视频通话场景 。
- 提升稳定性，解决一些偶现 crash 。
- 优化 Windows 内存占用 。
- 优化流控，提升弱网表现。



## Version 6.0 @ 2019.01.18 

**优化**

- 更新架构为 LiteAV 内核 。
- 采用全新 QoS 算法，更低的卡顿率，更高的流畅性 。
- 采用全新的 Audio 模块，深度优化了各种网络情况下的声音质量 。
- 支持大小流双路编码功能（推荐仅在 Windows 和 Mac 设备上开启） 。
- 支持 CDN 转推和混流功能。

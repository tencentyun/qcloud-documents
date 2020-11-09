## Version 7.5 @ 2020.07.31

**新增**

- 新增对双栈 IPV6 和 IPV6 only 的支持。
- 新增进多房间拉流能力，用于支持超级小班课。
- 云端 MCU 混流新增支持设置背景图片（由于监管需要，图片必须先通过 TRTC 控制台进行上传）。
- 云端 MCU 混流新增支持 A+B=>C 和 A+B=>A 两种模式。
- 实时状态回调 onStatistics 新增播放缓冲时长字段 jitterBufferDelay。

**优化**

- 降低了端到端的连麦延时，7.5 版本的端到端通话和连麦延时在 7.4 版本的基础上缩短了40%。
- 降低了移动端的耳返延时，并支持对耳返设置变声和混响等音效。
- 优化播放端网络抖动评估算法，降低播放延迟。
- 降低 Android SDK 的端到端连麦通话延时。
- 进一步优化耳返时延。
- 优化播放 view 动态切换时画面黑屏的问题。

**修复**

- 修复在一个函数中连续调用 playBGM 和 pauseBGM 后播放不生效的问题。
- 修复偶现退房之后还能收到 onEnterRoom 回调的问题。
- 修复部分机型对超低分辨率编码失败无法恢复的问题。 

##  Version 7.4 @ 2020.06.24 

**优化**

耳返支持音量设置。

**修复**

- 修复 Android 版本横竖屏切换时本地画面闪一下的问题。
- 修复部分 Android 手机发送自定义视频无法正常编码的问题。
- 修复音频处理时偶发的一处数据包处理崩溃。



##  Version 7.3 @ 2020.06.01

**新增**

- 在兼容老接口的情况下，增加了全新的音效管理接口 TXAudioEffectManager，用于支持更加灵活和多样的音效能力。
- 视频编码参数 setVideoEncoderParam 新增 minVideoBitrate 选项，推荐对画质要求高的直播客户进行设置。

**优化**

- 音频新增瞬态降噪支持，您可以通过 setAudioQuality(TRTCAudioQualitySpeech) 开启。
- 音效文件支持 asset 打包的音效文件。
- 提升本地视频清晰度。
- 播放端自定义渲染支持纹理的方式，降低性能开销。
- 优化摄像头采集分辨率选取逻辑，提升视角效果。
- 优化了回声处理效果。
- 支持全链路 128kbps 高音质立体声，通过 setAudioQuality(TRTCAudioQualityMusic) 接口即可设置。
- 支持 SPEECH 语音模式，适合会议场景下的语音通话，拥有更强的降噪（ANS）能力，通过 setAudioQuality(TRTCAudioQualitySpeech) 可以设置。
- 支持多路背景音乐并行播放，用于支持原声和伴唱分离的 K 歌场景。同时支持背景音乐循环播放。
- 支持先调用 muteLocalVideo 再调用 startLocalPreview 实现“只预览，不推流”的效果，您也可以通过在 enterRoom 前调用 startLocalPreview 实现该能力。

**修复**

- 修复自定义视频采集时，偶现 SDK 内部 OpenGL 上下文错误 crash。
- 修复进房前 setLocalVideoRenderListener 自定义渲染回调不触发的问题。
- 修复横屏模式下切换前后摄像头，播放端画面会倒置的问题。
- 修复进房前调用 startLocalPreview，进房后播放端概率花屏问题。
- 修复硬编码器偶现 crash。
- 修复本地音频录制偶现的断断续续的 Bug。
- 修复暂停推流（muteLocalVideo，muteLocalAudio）时，发生强杀或 crash 后重进房，播放端不会自动播放音视频的问题。



##  Version 7.2 @ 2020.04.16 

**新增**

- 新增 Android 支持手机录屏，适用于手机端录屏直播。

**优化**

- 优化中低端 Android 手机在通话场景下的性能消耗，提升语音体验。
- 优化滤镜、绿幕等视效接口，归并到 TXCBeautyManager 类下，实现统一的调用方式。

**修复**

- 修复切换角色时，自定义流 ID 偶现未及时生效的问题。



##  Version 7.1 @ 2020.03.27 

**优化**

- C++ STL基础库全静态编译。
- 通话音量默认开启 ANS、AGC，提高通话模式下的音质。
- 优化混流预设模版易用性。
- 混流优化，提升成功率。

**修复**

- 修复进房频繁开关 AGC 的时候，处理声音变成全零的问题。
- 修复测速导致其他 API 调用响应较慢的问题。
- 修复被系统电话打断后上行音量翻倍及声音有噪音问题。
- 修复进房自动旁路的问题。



##  Version 7.0 @ 2020.03.09 

- 优化 3A 开启策略。
- 提升 mcu 混流易用性。
- 优化弱网抗抖动能力，弱网下，音频更流畅。
- 解决多次交替进退房导致的内存泄露问题。



##  Version 6.9 @ 2020.01.14 

**新增**

- 新增 API：snapshotVideo() 支持本地及远端视频画面截图。
- 新增加一种全局音量类型模式：setSystemVolumeType(TRTCSystemVolumeTypeVOIP)，即一直采用通话音量，主要用于解决蓝牙耳机自带麦克风的采集切换问题。
- 新增对 Android 10.0 系统的支持。
- enterRoom 参数 TRTCParams 中新增加 streamId 属性，用于设定当前用户在 CDN 上的直播流 ID，更方便您绑定直播 CDN。
- enterRoom 参数 TRTCParams 中新增加 cloudRecordFileName 属性，您可以设置本次直播在云端录制的文件名。同时我们优化了录制服务对视频流中断的抵抗能力，使得远程录制的文件更加完整。
- 新增场景 TRTCAppSceneAudioCall，在 enterRoom 时可以设置。该场景下，TRTC SDK 针对语音通话进行了全方位的优化。
- 新增场景 TRTCAppSceneVoiceChatRoom，在 enterRoom 时可以设置，可以开启 TRTC SDK 专门针对语音互动聊天室场景所作的各项优化。
- 新增 API：pauseAudioEffect、resumeAudioEffect 音效支持暂停/恢复控制。
- 新增 API：setBGMPlayoutVolume、setBGMPublishVolume，BGM 支持分别设置本地播放和推流混音音量。
- 新增 API：setRemoteSubStreamViewRotation 辅路视频播放支持调整渲染旋转角度。

**优化**

- 优化某些机型硬解时音画不同步的问题。
- 视频画面支持 1080P 高分辨率采集，让手机直播 PC 观看的场景获得更佳的画面清晰度。
- 错误码优化，简化进房错误码。
- 优化偶现秒开慢的问题。

**修复**

- 修复偶现 HTTP 组件 crash。
- 修复音效播放偶现没有完成回调的问题。
- 修复偶现进房失败后无法恢复的问题。



##  Version 6.8 @ 2019.11.15 

**新增**
- 企业版新增 P 图新功能，包括美肤、亮眼、白牙、祛皱、祛眼袋等新特性。
- 新增接口 getBeautyManager，聚合美颜、P 图动效接口。
- 新增耳返能力。
- 新增进房可指定不自动拉流。
- 新增回调 onRemoteUserEnterRoom / onRemoteUserLeaveRoom，支持未上麦的主播进退房通知。

**优化**

- pts 生成机制优化。
- 优化网络切换后，自动选择较优的接入点。
- startRemoteView 支持提前调用。

**修复**

修复已知 crash 等稳定性问题。



##  Version 6.7 @ 2019.09.30 

**新增**

- AAR 打包新增权限获取配置。
- 新增 Android 8.0 以上系统 CPU 占用评估。

**优化**

- 转推耗时优化。
- 支持单个用户播放音量独立调节能力。



## Version 6.6 Patch @ 2019.09.10 

**新增**

- 新增系统音量类型设置接口。
- 新增音效接口，支持播放短音效。

**优化**

自定义音频回调数据支持可修改。



## Version 6.6 @ 2019.08.02 

**新增**

- 新增音频本地录制功能。
- 新增首帧音频、首帧视频发送回调接口。

**优化**

- 进房优化，降低进房耗时，提升进房成功率。
- 支持 mute 远端视频接口。
- 进房错误码统一，通过 onEnterRoom 回调，result&lt;0表示进房错误。
- Demo 优化，新增低延时大房间支持。
- 播放器新增音量设置接口及音量大小回调接口。
- 自定义发送视频支持本地渲染。
- 自定义采集发送视频支持 1080P。
- 本地及远端渲染支持 SurfaceView 方式。

**修复**

- 修复旁路混流相关的问题。
- 修复本地预览角度不对的问题。



##  Version 6.5 @ 2019.06.12 

**新增**

直播模式（TRTCAppSceneLIVE）新增“低延时大房间”功能：

- 采用专为音视频优化过的 UDP 协议，超强抗弱网能力。
- 平均观看延迟一秒作为，提升观众和主播之间的互动积极性。
- 最多支持10万人进入同一个房间。

**优化**

- 优化音量评估算法（enableAudioVolumeEvaluation），音量评估更灵敏。
- 优化高延迟和高丢包网络环境下的 QoE 算法，增强弱网抗性。
- 优化 onStatistics 状态回调，仅回调存在的流
- 优化视频通话（TRTCAppSceneVideoCall）模式下的 QoE 算法，进一步提升 1v1 通话模式下的弱网流畅性。
- 优化解码器性能，修复超低端 Android 手机上延迟越来越高的 Bug。
- 优化弱网下音画不同步的 Bug。
- 优化先 muteLocalVideo 之后再取消播放端画面的恢复速度。
- 优化直播 TXLivePlayer 播放缓冲逻辑，降低卡顿率。

**修复**

- 修复自定义渲染回调（setRemoteVideoRenderDelegate），远端画面在分辨率是 540P 以上（包括540P）时只回调10次的 Bug。
- 修复偶现的 enterRoom 没有回调的 Bug。
- 修复关闭音频采集之后，播放也没有声音的 Bug。
- 修复移除后再添加本地渲染 view 之后绿屏的 Bug。



##  Version 6.4 @ 2019.04.25 

**新增**
- 新增混流 setMixTranscodingConfig API 的设置回调函数。
- 新增企业版支持（增加大眼、瘦脸、V 脸和动效挂架功能）。
- 新增本地显示镜像和编码器输出镜像接口。

**优化**

- 提升弱网环境下的流畅度。
- 优化音量大小的回调算法，音量回调数值更加合理。
- 发送自定义音频、视频数据支持外部指定数据帧时间戳。
- 强化 setMixTranscodingConfig 接口，支持 roomID 参数，用于跨房连麦流混流。
- 强化 setMixTranscodingConfig 接口，支持 pureAudio 参数，用于纯语音通话场景下的语音混流和录制。
- 优化低端 Android 设备上解码 720p 视频的性能问题。

**修复**
- 修复直播（TXLivePlayer）延时可能会升高且不恢复的 Bug。
- 修复声音免提切换无效 Bug。
- 修复 Android 禁用麦克风权限后，没有错误回调 Bug。
- 修复直播场景 setVideoEncoderRotation 无效的 Bug。
- 修复音量调节按钮无法调整观众端声音大小的问题。
- 修复 Android 9.0 系统上 Demo 打开后弹窗的问题。



## Version 6.3 @ 2019.04.02 

**新增**
- 新增 Android 平台64位的支持。
- 新增自定义视频采集接口：TRTCCloud >> sendCustomVideoData。
- 新增自定义音频采集接口：TRTCCloud >> sendCustomAudioData。
- 新增自定义视频渲染接口：TRTCCloud >> setLocalVideoRenderDelegate + setRemoteVideoRenderDelegate。
- 新增自定义音频数据回调接口：TRTCCloud >> setAudioFrameDelegate，支持：
  - 返回麦克风采集数据：TRTCAudioFrameDelegate >> onCapturedAudioFrame。
  - 返回每一路远程用户的音频数据：TRTCAudioFrameDelegate >> onPlayAudioFrame。
  - 返回混合后送入喇叭播放的音频数据：TRTCAudioFrameDelegate >>onMixedPlayAudioFrame。





##  Version 6.2 @ 2019.03.08 

**新增**

- 新增跨房间通话能力 connectOtherRoom，即已存在的两个 TRTC 房间可以相互连通，该功能可用于直播间中的主播 PK 功能。
- 增加 sendSEIMsg() 接口，支持通过视频帧中的 SEI 头信息发送自定义消息，一般用于在视频流中塞入时间戳信息。
- 增加滤镜浓度设置接口 setFilterConcentration() 。

**优化**

- 优化 CPU 使用率和稳定性。
- 提升弱网（即较差的网络环境）下的画面清晰度。
- 取消 TRTCCloud 的多实例能力，创建模式改为单例模式，避免多个 TRTCCloud 实例相互抢占网络资源，影响体验效果。

**修复**

修复纯语音通话场景（例如狼人杀）下的旁路推流功能，需要配合 TRTCParam 中的 bussInfo 字段使用。



##  Version 6.1 @ 2019.01.31 

**优化**

- 支持观看屏幕分享流 。
- 支持发送自定义视频数据 。
- 优化转推 CDN 和混流实现 。
- 进房区分直播和视频通话场景 。
- 提升稳定性，解决一些偶现 crash 。
- 优化流控，提升弱网表现。



##  Version 6.0 @ 2019.01.18 

**优化**

- 更新架构为 LiteAV 内核 。
- 采用全新 QoS 算法，更低的卡顿率，更高的流畅性 。
- 采用全新的 Audio 模块，深度优化了各种网络情况下的声音质量 。
- 支持大小流双路编码功能（推荐仅在 Windows 和 Mac 设备上开启） 。
- 支持 CDN 转推和混流功能。






















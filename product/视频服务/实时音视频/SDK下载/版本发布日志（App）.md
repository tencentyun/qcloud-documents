## Version 9.4 @ 2021.12.08

**功能新增：**
- 全平台：增加语音聚焦功能，您可以通过 [setRemoteAudioParallelParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a0e6e6434aaa03ce878280125a9c0fa4b) 接口让 SDK 只播放房间中音量最大的几路音频，这对于提升大型语音房间的性能表现非常有帮助。
- Mac：增加对系统声音采集 [startSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2979e32c019708dcc9209bb6d2db9486) 的双声道支持。
- iOS：增加对 24 位 wav 格式的背景音乐文件的支持。
- Android&iOS：本版本符合国家隐私安全规范的规定，已经经过腾讯内部多款产品的验证。

**问题修复：**
- 全平台：修复快速调用 [switchRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a1f3bed34f92b3ff908beb2d0ed2866c9) 可能导致切换房间失败的问题。
- iOS：修复在应用内录屏 [startScreenCaptureInApp](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abf51acf26b2212192f7145468886b791) 过程中设置 [setVideoEncoderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a200c174b27bbe7397b0639e707ee6547) 无效的问题。
- iOS：修复系统录屏 [startScreenCaptureByReplaykit](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abebcd402e310d5d7dcbef9f6b601cfc4) 过程中偶现的内存上涨问题。

**功能优化：**
- 全平台：提升进房速度，减少进房耗时的波动。
- Mac：解决了在屏幕采集的过程中开启鼠标采集后，CPU 和 内存占用率较高的问题。
- Android：调整屏幕分享时的屏幕采集分辨率，使其能始终对齐屏幕分辨率，避免分享出的画面出现黑边等问题。
- Android：提升视频硬解兼容性，解决部分手机在播放视频分辨率发生变化时可能出现的黑屏问题。
- Windows：优化音量增益算法，解决部分设备出现增益过大导致杂音比较明显的问题。

## Version 9.3 @ 2021.11.03

**故障修复**
- 全平台：修复 point2PointDelay 有时获取不到，数值为0的问题。
- 全平台：修复偶现解析失败 SEI 消息丢失的问题。
- Mac：修复在 MacOS 12 beta 上摄像头不出帧的问题。
- iOS&Mac：修复特定顺序提前调用 startRemoteView 看不到画面的问题。
- Windows：修复使用竖屏编码并开启美颜的情况下画面出现锯齿的问题。
- Windows：修复第三方美颜开启情况下，切换分辨率后自定义渲染不回调的问题。

**功能优化**
- 全平台：优化弱网情况下视频秒开速度。
- 全平台：优化弱网调控策略，同场景下更流畅。
- 全平台：优化测速功能，支持对当前网络带宽进行检测。
- 全平台：优化对 TCP 传输协议的支持，更好地应对复杂的网络环境。

## Version 9.2 @ 2021.09.23

**功能新增**
- Android&iOS：支持 Socks5 代理。
- Windows：TRTCAudioQualityMusic 高音质场景新增自适应回声消除功能，自动平衡音质与回声消除强度。
- 全平台：新增设置语音音调功能。

**故障修复**
- Windows：修复 Mac 安装 Windows 的环境部分摄像头不吐数据问题。
- Android：修复偶现 CDN/TRTC 互切后没有上行音频的问题。
- iOS：修复 Web 端屏幕分享导致 iOS 接受端自定义渲染花屏的问题。

**功能优化**
- Android：优化硬解码时导致 ANR 的问题。
- Android：优化摄像头本地预览角度兼容的问题。
- Android：优化首帧秒开速度。
- Android&iOS：优化合唱模式 3A 策略。
- Windows：优化 AGC 算法，降低出现声音过小和声音过大的问题的概率。
- 全平台：优化弱网环境抗抖动算法，视频播放更流畅。

## Version 9.1 @ 2021.09.04

**功能新增**
- 全平台：C++ 接口支持音频帧回调格式设置。
- Windows：播片增加 ac3 格式的支持。
- Windows：摄像头信息支持获取支持的分辨率列表，具体请参见 [ITXDeviceCollection.getDeviceProperties](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXDeviceManager__cplusplus.html#ad502f48cb2a4470943134e4b48904450)。
- Windows：支持 Nvidia、Intel、AMD 硬解。
- Mac：新增本地媒体录制支持。

**问题修复**
- 全平台：修复偶现的进房失败问题。
- Mac：修复屏幕分享时切换分辨率，预览画面闪一下的问题。
- Android：修复子房间切回主房间时，辅路视频画面显示异常的问题。
- Android：修复特定场景下偶现的帧率设置不生效问题。
- Windows：修复观众切换为 CDN 流后无法拉流的问题。
- Windows：修复播片功能播放特定格式视频画面消失的问题。

**质量优化**
- 全平台：优化弱网下音视频体验。
- Android：优化退房时的音频状态管理。
- Android：优化音频采集启动失败后的恢复逻辑，提升成功率。
- Android：优化特定条件下视频画面过曝的问题。

## Version 9.0 @ 2021.08.06

**功能新增**
- iOS：支持设置系统采集音量，详情请参见 [setSystemAudioLoopbackVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#afc45226807d84673bab78b21d1be54ae)。
- 全平台：支持设置自定义音轨的音量，详情请参见 [setMixExternalAudioVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#ae0031e4af8bb120ef6de164d99886418)。
- 全平台：状态回调可区分音频和视频的丢包率，详情请参见 [TRTCRemoteStatistics](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCStatistic__cplusplus.html#structliteav_1_1TRTCRemoteStatistics)。

**质量优化**
- 全平台：优化订阅流程，提升手动订阅的秒开速度。
- 全平台：修复特定场景 onExitRoom 回调重复的问题。

**问题修复**
- Android：修复自定义采集动态设置码率和帧率无效的问题。
- iOS：修复先开启录屏辅路，再开启摄像头推流导致的推流失败问题。
- iOS：修复本地视频录制模糊的问题。
- iOS：修复若干稳定性问题。
- Winodws：修复屏幕分享时采集帧率异常的问题。
- Windows：修复屏幕分享切换目标时，播放端会先显示一帧旧画面的问题。

## Version 8.9 @ 2021.07.15

**功能新增** 
- Android：自定义渲染支持指定外部 GLContext，可以更灵活使用 OpenGL 环境。
- Windows：采集系统播放声音 [startSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a157639a4fa3cc73ffc1982bbd8a8985e) 时支持指定扬声器设备。
- Windows：支持 NVIDIA 平台硬编码，提升推流性能表现。
- 全平台：新增云代理支持，针对企业防火墙内部的环境，安全配置更友好。
- 全平台：接口 [muteLocalVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a22804c4112dee8c76475619f891e2eb5) 和 [muteRemoteVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a74d8d9922a771114804517db66657f65) 增加对流类型的支持。
- 全平台：统计状态回调 [onStatistics](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#ae7e4117f9c8004c9bcc5a29d64e840c9) 新增对本地网关延迟的统计 gatewayRtt，用于判断用户到 WiFi 路由器的网络质量。
- 全平台：音频录制接口 [startAudioRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html#a5224523e00d5167eb75cee9b65f72677) 支持录制成更多的音频格式。

**质量优化**
- 全平台：优化某些场景下的声音播放出现颤抖的问题。
- Android：优化画面秒开速度。
- Android：升级音频前处理算法，通话声音更清晰。

**问题修复**
- Windows：修复 VODPlayer 播片推流时本地录制音频文件会有重音的问题。
- Windows：修复高 DPI 环境下并启用过滤窗口时部分场景 crash 的问题。
- iOS：修复外录屏辅路推流设置横屏无效的问题。
- iOS：修复只开启远端自定义渲染并指定使用 RGBA 格式数据时的内存泄漏问题。
- 全平台：修复偶现进房失败问题。

## Version 8.8 @ 2021.06.21

**功能新增**
Android&Mac&iOS：支持外部接管音频播放，请参见 API [enableCustomAudioRendering](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#addb4c87719393cd4c4765d66a8cd9803)。

**质量优化**
- 全平台：优化 mixExternalAudioFrame 易用性，不再需要您完美地控制调用时机。
- Mac：降低屏幕分享开启鼠标捕捉时 CPU 的开销。
- Windows：优化 AGC 声音增益效果，更快更及时地进行调整。
- Windows：优化启用窗口过滤时屏幕分享的性能开销。

**问题修复**
- iOS：修复播放 AAC 格式本地音频文件总时长不准的问题。
- Android：修复部分机型切换后台时播放声音卡顿的问题。

## Version 8.7 @ 2021.5.25
**功能新增**
- 全平台：增加外接音频设备的异常检测。注册 onStatistics 回调后， 您可以用 [TRTCLocalStatistics](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCTypeDef__cplusplus.html#structtrtc_1_1TRTCLocalStatistics) 中的 audioCaptureState 来实时检测长时间静音、破音、异常间断问题。
- Windows：自定义采集支持输入 RGBA 格式的视频数据。

**质量优化**
- 全平台：优化 BGM 资源管理，及时释放内存占用。
- 全平台：推流端退后台暂停视频上行时，播放端能及时收到 [onUserVideoAvailable(false)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html#a091f1c94ff1e2bc39c36e9d34285e87a) 的通知。
- Mac：优化屏幕分享时鼠标捕捉的 CPU 和内存占用。

**问题修复**
- Android ：修复 setRemoteViewFillMode 部分机型偶现不生效的问题。
- iOS/Mac：修复停止自定义美颜时的内存资源释放问题。

## Version 8.6 @ 2021.05.08
- 全平台：优化网络流控算法，进一步提升音视频传输质量。
- 全平台：优化切换角色上下麦时音频播放的流畅度。
- iOS&Mac&Windows：优化音频处理模块，提升了 SPEECH 模式和 DEFAULT 模式的语音质量。
- iOS&Mac：优化自定义音频采集在高 CPU 场景下的适应性。
- iOS&Android ：支持录屏视频通过辅路进行分享，对齐桌面端版本。
- Mac：增加对苹果 M1 架构的原生支持。
- Windows：优化内存分配逻辑，提高稳定性。


## Version 8.5 @ 2021.03.24
**功能新增**
-  Mac：优化屏幕分享功能，您可以在分享目标窗口的同时指定其他窗口一起分享出去，请参见 API [addIncludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a2e101f0ff00c8752eea1fa9a1a432233)。
-  全平台：新增播片功能，您可以使用 [TXVodPlayer](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TXVodPlayer__android.html#classcom_1_1tencent_1_1rtmp_1_1TXVodPlayer) 与 TRTCCloud 绑定，把点播正在播放的内容通过 TRTC 的辅路推流分享出去。
-  全平台：新增辅路自定义采集，请参见 API [sendCustomVideoData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#aeeff994b8a298fa4948a11225312f629)。
-  全平台：新增自定义混音功能，您可以将自己的一路音轨混入 SDK 的音频处理流程中，SDK 会先将两路音轨混合后再一起发布出去，请参见 API [mixExternalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a6d04ce887009661a551e23c61d41571f)。
-  全平台：支持指定纯视频混流，混流控制更灵活。

**质量优化**
- Mac：startSystemAudioLoopback 支持双声道。
- Windows：选择幻灯片窗口进行屏幕分享时，支持自动切换到放映窗口。
- 全平台：状态回调增加端到端延迟。

**问题修复**
- iOS：优化部分设备偶现后台 OpenGL 渲染 crash 的问题。
- iOS：优化屏幕画面静止时屏幕分享在播放无法播放的问题。


## Version 8.4 @ 2021.02.08
**功能新增**
- Mac：开始支持采集 Mac 操作系统的输出声音，也就是跟 Windows 端一样的 SystemLoopback 能力，该功能可以让 SDK 采集当前系统的声音，开启这个功能后，主播就可以很方便地向其他用户直播音乐或者电影文件。
-  Mac：屏幕分享开始支持本地预览功能，您可以通过一个小窗口像用户展示屏幕分享的预览内容。
-  Windows：新增进程音量调整能力，使用 [setApplicationPlayVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITXDeviceManager__cplusplus.html#af6722fa5e6e45738e007004c374948b1) 可以设置系统的音量合成器的音量大小。
-  全平台：新增本地音视频录制功能，主播可以在推流过程中把本地的音频和视频录制成一个 mp4 文件，请参见 [startLocalRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a5075d55a6fc31895eedd5b23a1b8826b)。

**质量优化**
- 全平台：优化 [Music](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#ga865e618ff3a81236f9978723c00e86fb) 模式下的声音质量，更加适合类似 cloubhouse 的语音直播场景。
-  全平台：优化音视频链路的网络抗性，在 70% 的极端查网络环境下，音视频依然较为流畅。
-  Windows：优化部分场景下的直播音质，大幅减少了声音损伤问题。
-  Windows：性能优化，在部分使用场景下的性能较旧版本有 20%-30% 的提升。

**问题修复**
-  Windows：修复 Windows Server 2019 Datacenter x64 系统上启动桌面分享 crash 的问题。
-  Windows：修复分享窗口的同时改变目标窗口大小会偶发分享意外终止的 BUG。
-  Windows：修复部分型号的摄像头采集不出画面的问题。
-  iOS：修复 snapvideoshot 会造成 CAAnimation 动画卡顿的问题。
-  iOS&Mac：修复使用同一个 View 轮流显示摄像头和屏幕分享画面时，屏幕分享画面黑屏的问题。
-  iOS：修复使用第三方美颜组件时在 iPhone 6s 上可能会出现花屏的问题。
-  iOS：修复点播与 TRTC 同时使用时，在停止点播播放时偶现 crash 的问题。
-  Android：修复使用蓝牙耳机时被电话打断，拒绝接听电话后声音通过扬声器播放的问题。

## Version 8.3 @ 2021.01.15

**功能新增**

这个版本我们重点优化了自定义采集相关的业务逻辑：
- iOS & Android & Mac：优化音频模块，以确保在您使用 [enableCustomAudioCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ab8f8aaa19d70c6a2c9d62ecceb6e974d) 采集音频数据送给 SDK 处理时 SDK 依然能够保持很好的回声抑制和降噪效果。
- iOS & Android：若需在 TRTC SDK 的基础上，继续增加自己的声音特效和声音处理逻辑，使用 8.3 版本会更加简单，因为您可以通过 [setCapturedRawAudioFrameDelegateFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a4b58b1ee04d0c692f383084d87111f86) 等接口，设置音频数据的回调格式，包括音频采样率、音频声道数和采样点数等，以便您能够以自己喜欢的音频格式处理这些音频数据。
- 全平台：若需自己采集视频数据，并同时使用 TRTC SDK 自带的音频模块，可能会遇到音画不对齐的问题。这是因为 SDK 内部的时间线有自己的控制逻辑，因此我们提供了 [generateCustomPTS](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ae5f2a974fa23954c5efd682dc464cdee) 接口。您可以在采集到的一帧视频画面时，调用此接口并记录一下当前的 PTS（时间戳），随后调用 [sendCustomVideoData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a76e8101153afc009f374bc2b242c6831) 时带上这个时间戳，即可很好地保证音画同步。
- Windows：版本 SDK 增加了对域名格式的 Socks5 代理地址的支持。

**问题修复**
- 全平台：修复偶现音频数据时间戳异常导致录制内容音画不同步的问题。
- Windows：优化窗口分享在高 DPI 环境下的兼容性。
- Windows：获取可分享的窗口列表时增加最小化的窗口，最小化窗口的缩略图是其进程的图标。
- Windows：修复 SDK 启动后非必要的 DXGI 占用问题。
- iOS：修复手动设置焦点会导致 ANR 的问题。
- iOS：修复偶现切换前后摄像头无效的问题。
- iOS：修复 VODPlayer 减速播放 crash。
- iOS：修复偶现进房后默认从听筒播放的问题。
- iOS & Android：优化回声消除和噪声抑制的效果，并且耳返也能听到混响的效果。
- Android：修复偶现硬解绿屏花屏的问题。
- Mac：修复窗口分享并开启高亮时，窗口贴边会造成高亮边框闪烁的问题。
- Mac：修复渲染视图移动时会黑屏的问题。


## Version 8.2 @ 2020.12.23

**功能新增**
- iOS&Android：新增回调混合本地采集与所有播放的音频数据，本地音频录制更方便啦。
- Android：视频渲染组件 TXCloudVideoView 支持通过 `addVideoView(new TextureView(getApplicationContext()))` 接口将 TextureView 用于本地渲染。
- Android：自定义渲染回调支持 RGBA 格式的视频数据。
- Windows：支持本地摄像头采集和播放远端视频流截图，请参见 [ITRTCCloud.snapshotVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a3769ecbff6c0c4ee7cc5e4b40aaafe96)。
- Windows：屏幕分享支持通过 addExcludedShareWindow 和 addIncludedShareWindow 接口排除或强制包含您所指定的窗口，从而实现更灵活的屏幕分享能力。
- Mac&iOS：自定义渲染的模式下也可以调用 TRTCCloud.snapshotVideo 截取视频流图片。

**质量优化**
- Android：在线直播编码质量优化，视频画面更清晰。
- Windows：优化回声消除算法，进一步提升回声消除的效果。

**问题修复**
- iOS：修复 VODPlayer 和 TRTC 同时使用时偶现的音频播放异常的问题。
- Android：修复自定义美颜引起的本地渲染黑屏问题。
- Windows：修复偶现的当前进程无法退出的问题。


## Version 8.1 @ 2020.12.03

**功能新增**
- 全平台：统计信息（onStatistics）中新增远端视频卡顿的相关统计指标。
- 全平台：支持通过音量调节接口 setAudioPlayoutVolume（100-150） 实现声音的增益效果。
- iOS&Android：新增 setLocalVideoProcessListener 接口，能更好地支持第三方美颜 SDK 的集成。
- C# ：同步升级至最新版本的 API 接口。

**质量优化**
- 全平台：优化戴耳机时的声音处理算法，提高声音音质。
- Android：优化音频前处理算法，降低 3A 算法对音质的影响。

**问题修复**
- iOS：修复部分偶现的强杀 App 导致的崩溃问题。
- Android：修复当采集帧率比较高时出现的美颜效果异常问题。
- Windows：修复高 DPI 下屏幕分享偶现的崩溃问题。


## Version 8.0 @ 2020.11.13

**新增**
- 全平台新增 C++ 统一 API，请参见 cpp_interface/[ITRTCCloud.h](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html)。
- 全平台支持字符串房间号，请参见 TRTCParams.strRoomId。
- 全平台新增 TXDeviceManager 设备管理类。
- 全平台新增 API TRTCCloud.switchRoom，支持不停止采集，直接切换房间。
- 全平台新增 API TRTCCloud.startRemoteView 开始渲染远端视频画面。
- 全平台新增 API TRTCCloud.stopRemoteView 停止渲染远端视频画面。
- 全平台新增 API TRTCCloud.getDeviceManager 获取设备管理类。
- 全平台新增 API TRTCCloud.startLocalAudio 开启本地音频的采集和上行。
- 全平台新增 API TRTCCloud.setRemoteRenderParams 设置远端图像的渲染配置。
- 全平台新增 API TRTCCloud.setLocalRenderParams 设置本地图像的渲染配置。

**优化**
- Android 优化软硬解切换逻辑。
- Windows 优化 System loopback 音频采集音质及回声消除效果。
- Windows 优化音频设备选择逻辑，降低无声率。
- Windows 优化双讲剪切效果。
- 全平台优化手动接收模式切换角色时的秒开效果。
- 全平台优化音频接收逻辑，提升音频效果。
- 全平台优化 sendCustomCmdMsg 可靠性。

**修复**
- iOS 修复 muteLocalVideo 调用导致本地视频渲染暂停的问题。
- iOS 修复在前后台切换时偶现调用系统组件可能导致卡死的问题。
- iOS 修复开启音效时，耳返音频断断续续的问题。
- Android 修复切通话音量播音效的时候电话打断，音效不会停止播放的问题。
- Android 修复偶现音频采集启动失败的问题。
- Windows 修复偶现本地视频渲染黑屏的问题。
- Windows 修复进程退出时可能 crash 的问题。
- Windows 优化蓝牙耳机支持，修复蓝牙耳机无声问题。
- Windows 修复屏幕分享结束时抢焦点的问题。
- 全平台修复状态回调丢包率统计异常问题。



## Version 7.9 @ 2020.10.27
**新增**
- Mac：屏幕分享支持过滤选定的窗口，用户可以将自己不希望分享出去的窗口排除掉，从而更好地保护用户的隐私。
- Windows：屏幕分享支持设置“正在分享”提示边框的描边颜色以及边框宽度。
- Windows：屏幕分享在分享整个桌面时支持开启高性能模式。
- 全平台：支持自定义加密，用户可以对编码后的音视频数据通过暴露的 C 接口进行二次处理。
- 全平台：在 TRTCRemoteStatistics 中新增音频卡顿信息回调 `audioTotalBlockTime` 和 `audioBlockRate`。

**优化**
- iOS：优化了音频模块的启动速度，让首个音频帧可以更快地采集并发送出去。
- Windows：优化系统回采的回声消除算法，让开启系统回采（SystemLoopback）时有更好的回声消除能力。
- Windows：优化屏幕分享功能中的窗口采集抗遮挡能力，支持设置过滤窗口。
- Android：针对大部分 Android 机型进行了耳返效果的优化，使耳返延迟降低到一个更舒适的水平。
- Android：针对 Music 模式（在 startLocalAudio 时指定）下的点对点延迟进行了进一步的优化。
- 全平台：在手动订阅模式下，优化了观众和主播角色互切时的声音流畅度。
- 全平台：优化了音视频通话中的弱网抗性，在较差的网络下也能有更优质的音频流畅度。

**修复**
- iOS：修复部分场景下偶现的视频画面不渲染问题。
- iOS：修复用户在戴耳机并且是 Default 音质下偶现的杂音问题。
- iOS：修复部分已知的内存泄露问题。
- iOS：修复偶现的 replaykit 扩展录屏结束后的 crash 问题。
- iOS：解决模拟器环境下的编译问题。
- Android：修复部分手机在 App 长时间切到后台，之后又再次切回前台时偶现的音画不同步问题。
- Android：修复切后台后没有释放麦克风的问题。
- Android：修复 SDK 内部部分 OpenGL 资源未及时释放的问题。
- Windows：修复个别场景下偶现的杂音问题。
- 全平台：修复部分偶现的崩溃问题，提升 SDK 的稳定性。

## Version 7.8 @ 2020.09.29
**新增**
- Mac：新增系统音量变化回调，详见 [TRTCCloudDelegate.onAudioDevicePlayoutVolumeChanged](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#af24c0f0258e83ab644e242ee0d01277f)。
- Windows：新增支持跨屏指定区域进行屏幕分享。
- Windows：新增窗口分享支持过滤指定窗口进行抗遮挡，详见 [TRTCCloud.addExcludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ae5141a9331c3675f17fbdc922f376b06) 和 [TRTCCloud.removeExcludedShareWindow](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a08504ce347b593c0191904611da5cfd2)。
- Windows：新增系统音量变化回调，详见 [ITRTCCloudCallback.onAudioDevicePlayoutVolumeChanged](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__cplusplus.html#a39cf2644243dceaccd82933f11f4db12)。

**优化**
- iOS：支持 VODPlayer 和 trtc 一起使用，并且支持回声消除。
- iOS&Mac：支持垫片推流，使用方法见 [TRTCCloud.setVideoMuteImage](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#ad730c168c066599b6c4c987fd7b7c3a2)。
- Android：支持垫片推流，使用方法见 [TRTCCloud.setVideoMuteImage](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a78195189ea5f3db9a05338f585bb925d)。
- Android：优化声音路由策略，支持戴耳机时，声音只从耳机播放。
- Android：支持部分系统下采用低延迟采集播放，降低 Android 系统通话延迟。
- Android：支持 VODPlayer 和 trtc 一起使用，并且支持回声消除。
- Windows：兼容虚拟摄像头 e2eSoft Vacm。
- Windows：支持同时调用 startLocalPreview 和 startCameraDeviceTest。
- Windows：支持屏幕分享走主路的同时，调用 startLocalPreview 开启本地预览。
- Windows：降低因 SDK 内部播放缓冲引发音频延迟较大的问题。
- Windows：优化音频启动逻辑，在仅播放的情况下不占用麦克风。



**修复**
- iOS：修复 iPhone SE 播放声音小的问题。
- iOS：修复子房间 (TRTCCloud.createSubCloud) 调用 muteRemoteAudio 触发 crash 的问题。
- iOS：修复偶现渲染 crash 问题。
- iOS：修复前后台切换时在部分 iPad 视频渲染偶现卡死主线程的问题。
- iOS：修复已知内存泄露。
- iOS：修复 iOS14 提示“查找并连接本地网络上的设备”的问题。
- Mac：修复 getCurrentCameraDevice 始终返回 nil 的问题。
- Mac：修复部分 USB 摄像头无法打开的问题。
- Mac：修复屏幕分享指定区域面积为0时的 crash 问题。
- Android：修复未配置 READ_PHONE_STATE 权限时，Android5.0 设备 crash 的问题。
- Android：修复蓝牙耳机断开再连上之后音频采集和播放异常的问题。
- Android：修复已知 crash 问题。
- Windows：修复64位 SDK 多次开关屏幕分享会 crash 的问题。
- Windows：修复部分系统使用 OpenGL 会 crash 的问题。


## Version 7.7 @ 2020.09.08

**优化**

- 全平台：优化辅路（即屏幕分享）的秒开速度。
- iOS：优化内部线程模型，提升在30路以上并发播放的场景中的运行稳定性。
- iOS&Android：优化 Audio 模块的性能，提升首帧的采集延迟，新版本可以更快的获得首个音频帧。
- iOS&Android：优化点播播放器（VodPlayer）和 TRTC 同时使用时的音量大小和音质表现。
- iOS&Android：增加对 wav 音频格式的背景音乐和音效文件的支持。
- Windows：优化在某些低端摄像头下 CPU 使用率过高的问题。
- Windows：优化对多款 USB 摄像头和麦克风的兼容性，提升设备的打开成功率。
- Windows：优化摄像头和麦克风设备的选择策略，避免由于摄像头或麦克风在使用中插拔导致的采集异常问题。

**修复**

- 全平台：修复弱网情况下调用 muteLocalVideo 和 muteLocalAudio 接口时会偶现播放异常的 BUG。
- iOS：修复播放音效在低端 iPhone 或 iPad 上可能会失败的 BUG。
- iOS：修复 iPad Pro 屏幕分享出的画面出现变形拉伸的问题。
- iOS：修复 App 内屏幕贡献在用户拒绝权限之后，还会持续弹出几次屏幕录制权限申请提示的问题。
- Windows：解决笔记本或者台式机在长时间休眠后，退房 [onExitRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__cplusplus.html#a0a45883a23a200b0e9ea38fdde1da4bd) 事件通知不会回调的问题。
- Windows：修复在 Music 音质模式下，开启系统混音 [stopSystemAudioLoopback](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#aab0258238e4414c386657151d01ffb23) 后会导致漏回声的问题。
- Windows：修复在快速调用 enterRoom 和 exitRoom 进退房的情况下，偶现的播放端无声的 BUG。
- Windows：修复 SDK 对 Visual Stuido 2010 项目的编译兼容性问题。
- Windows：修复手动接收模式（即 [setDefaultStreamRecvMode(false，false)](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a7a0238314fc1e1f49803c0b22c1019d5)）下会重复收到 onUserVideoAvailable 事件回调的问题。


## Version 7.6 @ 2020.08.21
**新增**

- Windows：新增 [updateLocalView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ae5211a2739df8d8ec6017559b3aa0299) 和 [updateRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a8c8247cbc679ea144ffb393b6b940c9e) 接口，用于优化实时调整 HWND 类型的渲染窗口时的体验。
- Windows：新增 [getCurrentMicDeviceMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a8a8badf62eee1021f9315f11df0f597f) 接口用于获取当前 Windows PC 是否被设置为静音。
- Windows：新增 [setCurrentMicDeviceMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a8a8badf62eee1021f9315f11df0f597f) 接口用于将当前 Windows PC 设置为全局静音。
- Mac：新增 [updateLocalView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abf20f249b4b43fff64f944b4aefe54cb) 和 [updateRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa27f954e6301fb57a143b27429b63d87) 接口，用于优化实时调整 View 渲染区域时的体验。
- Mac：新增 [getCurrentMicDeviceMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6ba78519e9c98c1eecd365154882d53f) 接口用于获取当前 Mac 电脑是否被设置为静音。
- Mac：新增 [setCurrentMicDeviceMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a88569e62fe75b7ea98cc012169f22bfe) 接口用于将当前 Mac 电脑设置为全局静音。
- iOS：新增 [updateLocalView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abf20f249b4b43fff64f944b4aefe54cb) 和 [updateRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa27f954e6301fb57a143b27429b63d87) 接口，用于优化实时调整 View 渲染区域时的体验。
- iOS: 为 TRTCCloudDelegate 增加了 [onCapturedRawAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#aeaeaf9e7091c75e1a072d576a57d7f5c) 回调，并修改了其他几个回调函数的名称，依次修改为 [onLocalProcessedAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a73a3e7de3c5c340957f119bb0f8744b0)、[onRemoteUserAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#aa392c17c27bae1505f148bf541b7746a)和 [onMixedPlayAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a5a8a0bf6f8d02c33b2fe01c6175dfd4e)。
- Android：为 TRTCCloudListener 增加了 [onCapturedRawAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#abffd560f5b2b2322ea3980bc5a91d22e) 回调，并修改了其他几个回调函数的名称，依次修改为 [onLocalProcessedAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a62c526c6c30a66671260bdf0c5c64e46)、[onRemoteUserAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a4af98a7d668c150ea8e99e3085505902) 和  [onMixedPlayAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a580e94224357c38adf6ed883ab3321f7)。

**优化**

- 全平台：优化 enterRoom 的协议策略，提升加入房间的速度，并提升成功率。
- 全平台：优化同时订阅超多路音频时的总体性能消耗和卡顿问题。
- Mac：屏幕分享开始支持分享指定窗口的指定区域。

**修复**

- 全平台：修复在不退房的情况下进入同一个房间时，SDK 不触发 onEnterRoom 回的 BUG。
- 全平台：修复几种可能导致黑屏的偶现内部 BUG 的问题。
- 全平台：修复提前调用 startRemoteSubStreamView 无法正常显示屏幕分享画面的问题。
- Windows：修复已知的几处句柄及 GDI 泄露。
- Windows：修复多个已知的 crash 问题。
- Windows：修复摄像头和麦克风拔掉后重新插入不会自动开启设备的问题。
- iOS：修复在 iOS 10 上背景音乐接口在传入特定规则的文件路径时会崩溃的 BUG。
- Android：修复频繁快速的 enterRoom 和 exitRoom 后偶现的无声问题。
- Android：修复偶现的录屏推流黑屏的问题。


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

新增 Android 支持手机录屏，适用于手机端录屏直播。

**优化**

- 优化中低端 Android 手机在通话场景下的性能消耗，提升语音体验。
- 优化滤镜、绿幕等视效接口，归并到 TXCBeautyManager 类下，实现统一的调用方式。

**修复**

修复切换角色时，自定义流 ID 偶现未及时生效的问题。



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

- 新增对 Android 10.0 系统的支持。
- 新增 API： snapshotVideo()，支持本地及远端视频画面截图。
- 新增 API：pauseAudioEffect、resumeAudioEffect 音效支持暂停/恢复控制。
- 新增 API：setBGMPlayoutVolume、setBGMPublishVolume，BGM 支持分别设置本地播放和推流混音音量。
- 新增 API：setRemoteSubStreamViewRotation 辅路视频播放支持调整渲染旋转角度。
- 新增一种全局音量类型模式：setSystemVolumeType(TRTCSystemVolumeTypeVOIP)，支持一直采用通话音量，主要用于解决蓝牙耳机自带麦克风的采集切换问题。
- enterRoom 参数 TRTCParams 中新增 streamId 属性，用于设定当前用户在 CDN 上的直播流 ID，更方便您绑定直播 CDN。
- enterRoom 参数 TRTCParams 中新增 cloudRecordFileName 属性，您可以设置本次直播在云端录制的文件名。
- 新增场景 TRTCAppSceneAudioCall，在 enterRoom 时可以设置。该场景下，TRTC SDK 针对语音通话进行了全方位的优化。
- 新增场景 TRTCAppSceneVoiceChatRoom，在 enterRoom 时可以设置，可以开启 TRTC SDK 专门针对语音互动聊天室场景所作的各项优化。

**优化**

- 优化录制服务对视频流中断的抵抗能力，使得远程录制的文件更加完整。
- 优化某些机型硬解时音画不同步的问题。
- 视频画面支持 1080P 高分辨率采集，让手机直播 PC 观看的场景获得更佳的画面清晰度。
- 优化错误码，简化进房错误码。
- 优化偶现秒开慢的问题。

**修复**

- 修复偶现 HTTP 组件 crash。
- 修复音效播放偶现没有完成回调的问题。
- 修复偶现进房失败后无法恢复的问题。



##  Version 6.8 @ 2019.11.15 

**新增**

- 新增耳返能力。
- 新增进房可指定不自动拉流。
- 新增接口 getBeautyManager，聚合美颜、P 图动效接口。
- 企业版新增 P 图新功能，包括美肤、亮眼、白牙、祛皱、祛眼袋等新特性。
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

## Version 6.6 @ 2019.08.02 

**新增**

- 新增音频本地录制功能。
- 新增首帧音频、首帧视频发送回调接口。
- 新增系统音量类型设置接口。
- 新增音效接口，支持播放短音效。
- 音频自定义回调接口输出的数据支持可修改。

**优化**

- 进房优化，降低进房耗时，提升进房成功率。
- 支持 mute 远端视频接口。
- 进房错误码统一，通过 onEnterRoom 回调，result&lt;0 表示进房错误。
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

- 优化弱网下音画不同步的 Bug。
- 优化 onStatistics 状态回调，仅回调存在的流。
- 优化直播 TXLivePlayer 播放缓冲逻辑，降低卡顿率。
- 优化先 muteLocalVideo 之后再取消播放端画面的恢复速度。
- 优化高延迟和高丢包网络环境下的 QoE 算法，增强弱网抗性。
- 优化解码器性能，修复超低端 Android 手机上延迟越来越高的 Bug。
- 优化音量评估算法（enableAudioVolumeEvaluation），音量评估更灵敏。
- 优化视频通话（TRTCAppSceneVideoCall）模式下的 QoE 算法，进一步提升 1v1 通话模式下的弱网流畅性。

  

**修复**

- 修复偶现的 enterRoom 没有回调的 Bug。
- 修复关闭音频采集之后，播放也没有声音的 Bug。
- 修复移除后再添加本地渲染 view 之后绿屏的 Bug。
- 修复自定义渲染回调（setRemoteVideoRenderDelegate），远端画面在分辨率是 540P 以上（包括 540P）时只回调10次的 Bug。



##  Version 6.4 @ 2019.04.25 

**新增**

- 新增本地显示镜像和编码器输出镜像接口。
- 新增混流 setMixTranscodingConfig API 的设置回调函数。
- 新增企业版支持大眼、瘦脸、V 脸和动效挂架功能。

**优化**

- 提升弱网环境下的流畅度。
- 优化音量大小的回调算法，音量回调数值更加合理。
- 发送自定义音频、视频数据支持外部指定数据帧时间戳。
- 强化 setMixTranscodingConfig 接口，支持 roomID 参数，用于跨房连麦流混流。
- 强化 setMixTranscodingConfig 接口，支持 pureAudio 参数，用于纯语音通话场景下的语音混流和录制。
- 优化低端 Android 设备上解码 720p 视频的性能问题。

**修复**
- 修复声音免提切换无效 Bug。
- 修复直播（TXLivePlayer）延时可能会升高且不恢复的 Bug。
- 修复直播场景 setVideoEncoderRotation 无效的 Bug。
- 修复 Android 禁用麦克风权限后，没有错误回调 Bug。
- 修复 Android 9.0 系统上 Demo 打开后弹窗的问题。
- 修复音量调节按钮无法调整观众端声音大小的问题。



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

- 增加滤镜浓度设置接口 setFilterConcentration() 。
- 新增 sendSEIMsg() 接口，支持通过视频帧中的 SEI 头信息发送自定义消息，一般用于在视频流中塞入时间戳信息。
- 新增跨房间通话能力 connectOtherRoom，即已存在的两个 TRTC 房间可以相互连通，该功能可用于直播间中的主播 PK 功能。



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

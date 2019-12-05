### Version 3.4
- IOS&Android：短视频录制新增回删、多比例切换、焦距调节等功能。
- IOS&Android：短视频编辑新增片尾水印功能。
- IOS&Android：修复第三方推流FLV直播兼容性问题。
- IOS：解决IOS11兼容性问题。
- Android：解决点播回调不精确问题。

### Version 3.3
- IOS&Android：点播HLS支持EXT-X-DISCONTINUITY标签。
- Android：支持后台采集推流。
- 解决Android在某些机型上录制绿屏及播放黑屏的问题。
- 解决Android BGM部分机型播放异常及进度回调不精确的问题。
- 修复过去一周客户提出的部分bug。

### Version 3.2
- iOS&Android 点播支持 mp4 视频本地缓存播放。
- 解决异常情况下后台录制花屏问题。
- 解决BGM低采样率不支持的问题。
- 修复过去一周客户提出的部分bug。

### Version 3.1
- iOS & Android：美颜算法优化，新增红润效果及多套美颜风格。
- iOS：新增光滑与自然两种美颜风格。
- Android：新增光滑、自然、朦胧三种美颜风格。
- Android：短视频编辑新增变速、背景音、字幕功能。
- 商用企业版新增V脸、瘦鼻、瘦下巴等特性。

### Version 3.0
- iOS&Android：重构美颜模块，提升美颜效果同时降低GPU使用率。
- iOS & Android：对点播播放器进行了内部重构，支持 x2 x4 等多倍速播放。
- iOS & Android：优化连麦底层网络组件抗抖动能力，并对AEC回音消除组件进行了更好的机型适配。
- iOS & Android：TXUGCRecord 增加了 pauseRecord 和 resumeRecord 接口，用于支持多段录制。
- iOS：提供了快速裁剪和编辑接口。

### Version 2.0.5
- Android：短视频编辑添加水印功能。
- Android：短视频录制新增多段录制功能。
- iOS & Android：修复若干bug。

### Version 2.0.4
- iOS：短视频编辑添加滤镜、水印、背景音、字幕、变速等功能。
- Android：优化短视频裁剪、拼接功能，新增编辑滤镜功能。
- iOS & Android：UGC录制增加美颜回调预处理接口。
- iOS & Android：短视频上传增加断点续传能力。

### Version 2.0.3
- Android：新增UGC裁剪与拼接功能。
- Android：优化播放端Player及渲染View，支持动画、悬浮框、大小屏切换等。
- Android：软硬编新增Auto选项，SDK根据手机性能自动启用硬编或者软编。
- iOS：优化IOS过曝问题，曝光更自然。
- iOS & Android：针对弱网环境优化自适应码率控制，新增两种低分辨率（180×320、270×480）推流支持。
- iOS & Android：优化Demo目录及代码结构，降低接入成本，新增小视频录制、裁剪、拼接、连麦Demo，简单易用。

### Version 2.0.2
- iOS：新增UGC裁剪与拼接功能。
- iOS：精简版支持Bitcode。
- Android：特权版新增大眼瘦脸功能。
- Android：优化硬编效果，提升编码质量。
- Android：开发播放端数据接口，硬解数据以Surface形式提供，软解数据以buffer形式提供。
- iOS & Android：优化前置摄像头在开启P图、绿幕后的镜像表现。
- iOS & Android：优化UGC上传协议。

### Version 2.0.1
- iOS & Android：优化连麦，增加多人连麦能力。
- iOS & Android：增加 UGC 小视频添加背景音乐功能。
- iOS & Android：新增纯音频推流功能。
- iOS & Android：新增播放端截图功能。
- iOS & Android：FFMPEG库更新到安全版本。
- iOS & Android：优化FLV、RTMP数据包头解析。
- Android：新增混响功能，预设多种混响效果。
- Android：特权版新增绿幕功能。
- iOS：优化软解性能，开放播放端数据回调接口，客户可以自定义播放渲染。

### Version 2.0.0
- iOS & Android：增加 UGC 小视频的采集和发布功能。
- iOS & Android：增加截流录制功能，观众可以在观看直播时截取一段形成 UGC 小视频，然后分享出来。
- iOS：增加了新的“美白”滤镜，适合较为偏爱映客美颜效果的客户。

### Version 1.9.2
- iOS & Android：增加了对本地文件播放的支持。（startPlay 中设置 PLAY_TYPE_LOCAL_VIDEO）
- iOS & Android：重新设计了播放器中缓冲区的方案，对于低延迟链路的声音流畅性有优化。
- iOS：增加了 setReverbType 接口，可设置多种声音混响效果。
- iOS：优化了直播过程中添加水印的性能。

### Version 1.9.1
- iOS & Android：优化了摄像头直播中的美颜效果和清晰度体验。
- iOS & Android：美颜增加了滤镜功能，多种主流滤镜效果供您的主播选择。
- iOS & Android：增加了 setVideoQuality 接口，画质选择更简单更声音。
- iOS ：解决了某些客户反馈的iOS过曝问题，在人造光源比较强的场景下会有明显差异。
- iOS：进一步优化了耳返的延迟（混响功能 由于还有bug没有解决完，Delay一周Release）。
历史版本功能可参看 变更历史。

### Version 1.9.0
- iOS ：支持开启Bitcode，用于减少AppStore的安装包体积；
- iOS ：软硬编美颜统一，统一使用GPU加速方案；
- iOS + Android：音频模块优化，连麦支持背景音播放；
- iOS + Android：点播多线程优化（直播在上个版本已支持多实力）
- iOS + Android：解决网络卡顿时，播放停止（stopPlay）阻塞UI线程时间较长的问题；
- iOS ： 新增耳返功能，即主播在插上耳机唱歌时，可以实时听到自己发音的效果；
- Android：由于系统API的延迟问题，暂时尚未支持，我们会继续努力。

### Version 1.9.0
- iOS ：支持开启Bitcode，用于减少AppStore的安装包体积；
- iOS ：软硬编美颜统一，统一使用GPU加速方案；
- iOS + Android：音频模块优化，连麦支持背景音播放；
- iOS + Android：点播多线程优化（直播在上个版本已支持多实力）
- iOS + Android：解决网络卡顿时，播放停止（stopPlay）阻塞UI线程时间较长的问题；
- iOS ： 新增耳返功能，即主播在插上耳机唱歌时，可以实时听到自己发音的效果；
- Android：由于系统API的延迟问题，暂时尚未支持，我们会继续努力。

### Version 1.8.2
- 基于腾讯云加速链路实现连麦功能，且支持1v1服务端混流 （连麦模式下暂时不支持混音，1.8.3解决）
- 直播支持多实例播放能力，点播暂时不支持多实例播放；

### Version 1.8.1
- IOS解决命名冲突问题；
- IOS、Android直播支持多实例播放能力，点播暂时不支持多实例播放；
- 优化弱网环境下的播放体验；
- 混音功能优化；

### Version 1.8.0
- IOS新增精简版，包含直播推流与播放功能；
- Android硬件解码优化，解决多线程引发的Crash及ANR问题；
- 动态码率调整优化，提升码率调整精度；
- 推流新增镜像接口；
- IOS上层采集优化；
- Android新美颜优化，FPS控制更准确；
- 混音功能新增进度回调接口；
- SDK增加对HTTPS支持；

### Version 1.7.2
- Android采集编码重构；
- Android软编支持新美颜效果；
- Android硬编新增云端黑名单控制；
- 解决Android摄像头频繁打开关闭引发的多线程问题；
- Android录屏隐私模式新增推送主播音频能力；
- 解决Android HLS、MP4点播前后台切换花屏问题；
- 解决IOS模拟器播放花屏问题； 

### Version 1.7.1
- 修复IOS直播偶现黑屏的问题；
- 修复IOS模拟器编译不通过的问题；
- 修复IOS偶现物理键锁屏、切后台等Crash问题；
- 修复Android某些机型预览摄像头倒置的问题；
- 修复Android某些机型硬编码率过高的问题；
- 优化Android混音接口，使用更简单；

### Version 1.7.0
- IOS、Android新增ZoomIn、ZoomOut接口
- 新增点播 MPEG4 v3解码支持
- 新增智能控速模式，根据网速自适应调整码率及分辨率
- 修复HLS、MP4录制快进问题，及多种异常模式下录制的HLS、MP4播放问题
- IOS 采集优化，彻底修复闪屏等相关问题
- Android JNI优化，修复偶现回调失败问题

### Version 1.6.2
- IOS更新新的美颜算法，性能及效果有较大提升。（开启硬件加速后才有效）
- Android更新新的美颜算法，解决部分机型旧美颜算法不生效的问题，同时性能及效果有显著提升。（api 18 以上且开启硬件加速后才有效）
- IOS SDK增加replaykit录屏能力支持。
- 直播播放新增Pause/Resume接口，支持暂停与恢复。
- 解决Android硬编长时间推流之后引起的无数据问题。
- 解决长时间推流时间戳跳变引起的音画不同步等流异常问题。
- 解决AAC解码在某些场景下引起的Crash问题。

### Version 1.6.1
- Android SDK 增加手机录屏功能，可以手游直播了（支持隐私模式）
- 新增背景混音能力，主播可以选择喜欢的歌曲进行伴音。
- 优化APP切后台的推流逻辑，采用贴片的方式解决主播端APP切后台之后，观众端持续重连最终断开的问题；
- 强化客户自定义采集接口能力，客户可以采集不同格式的视频数据提供给SDK发送；
- IOS点播增加静音能力 （感谢蘑菇街团队的建议）
- 修复推流播放释放错乱引起的闪屏问题

### Version 1.6.0
- 增加音频数据加速处理能力，提升速播体验，用户无感知降低播放延迟；
- 针对推流后台主动拒绝的情况，增加了PUSH_WARNING_SERVER_DISCONNECT通知；
- 优化首次打开黑屏问题，首帧展示之前OpenGL渲染层不展示；
- IOS增加横屏推流及本地播放支持，使用详见接口变更
- 支持短时间内切到后台后可以保持rtmp推流连接
- 引入openGL冲突检查机制，避免player释放问题引起的IOS闪屏；
- 优化log性能，增加对外log回调接口 (setLogLevel接口不影响LOG回调函数的行为)；

### Version 1.5.2
- 增加音频解码对HE-AAC V2的支持；
- 推流及播放VideoView支持调整大小、支持保留最后一帧渲染；
- 优化就近接入，智能选择最优线路；
- 彻底解决跟Libyuv符号冲突的问题；
- 新增Android硬编支持机型到top100；
- 解决硬编码画面静止时自动重连的bug；
- 解决StopPlay在点播场景下卡2秒的问题；
- 解决推流端切换到后台或者断开网络推流失败后，播放端一直在自动重连的bug

### Version 1.5.1
- Andriod推流支持硬件加速（白名单列表持续追加中）
- MP4和HLS点播支持硬件解码
- 解决与互动直播的库冲突
- 点播增加重连机制

### Version 1.5.0
- 重构推流和播放器SDK，提高SDK的稳定性
- 增加GOP设置参数，秀场场景下推荐3秒（默认值）
- 解决跟AVGSDK的符号冲突问题
- 修复横屏推流中的崩溃问题

###  Version 1.4.2
- 支持MP4 和 HLS 在线点播
- 不再使用aar作为android sdk的打包方式，改为传统的jar+lib模式
- android sdk新增arm64模式

###  Version 1.4.1
- 提升推流性能，提升声音编解码性能
- 增加FLV点播支持

###  Version 1.3.1
- 提升播放性能
- 优化缓存策略，提供多种参数配置
- 推流端增加水印支持

###  Version 1.2.1
- 优化美颜/美白效果
- iOS和安卓增加硬件解码支持，iOS增加硬件编码支持

###  Version 1.1.1
- 推流SDK支持RTMP协议，并支持美颜/美白、分辨率设置等功能
- 播放SDK支持FLV/RTMP协议，支持画面裁剪，支持横竖屏切换




__功能__

腾讯云直播推流用 RTMP SDK 的参数配置模块。

__介绍__

主要负责 TXLivePusher 对应的参数设置，**其中绝大多数设置项在推流开始之后再设置是无效的**。 


 

__属性列表__

| 属性 | 类型 | 字段含义 | 推荐取值 | 特别说明 |
|-----|-----|-----|-----|-----|
| homeOrientation | int | HOME 键所在方向，用来切换横竖屏推流，默认值：HOME_ORIENTATION_DOWN（竖屏推流）。 | - | 常用的还有 HOME_ORIENTATION_RIGHT 和 HOME_ORIENTATION_LEFT，也就是横屏推流。 改变该字段的设置以后，本地摄像头的预览画面方向也会发生改变，请调用 [TXLivePush](https://cloud.tencent.com/document/product/454/34755) 的 setRenderRotation 进行矫正。 |
| touchFocus | BOOL | 是否允许点击曝光聚焦，默认值：NO。 | - | - |
| enableZoom | BOOL | 是否允许双指手势放大预览画面，默认值：NO。 | - | - |
| watermark | TXImage * | 水印图片，设为 nil 等同于关闭水印。 | - | - |
| watermarkPos | CGPoint | 水印图片位置，水印大小为图片实际大小，待废弃，推荐使用 watermarkNormalization。 | - | - |
| watermarkNormalization | CGRect | 水印图片相对于推流分辨率的归一化坐标。 | 假设推流分辨率为：540 x 960，该字段设置为：（0.1，0.1，0.1，0.0），那么水印的实际像素坐标为：（540 × 0.1，960 × 0.1，水印宽度 × 0.1，水印高度会被自动计算）。 | watermarkNormalization 的优先级高于 watermarkPos。 |
| localVideoMirrorType | int | 本地预览画面的镜像类型，默认值：LocalVideoMirrorType_Auto 即前置摄像头镜像，后置摄像头不镜像。 | - | - |
| pauseTime | int | 垫片推流的最大持续时间，单位秒，默认值：300s。 | - | 调用 TXLivePusher 的 pausePush  接口，会暂停摄像头采集并进入垫片推流状态，如果该状态一直保持， 可能会消耗主播过多的手机流量，本字段用于指定垫片推流的最大持续时间，超过后即断开与云服务器的连接。 |
| pauseFps | int | 垫片推流时的视频帧率，取值范围3 - 8，默认值：5FPS。 | - | - |
| pauseImg | TXImage * | 垫片推流时使用的图片素材，最大尺寸不能超过1920 × 1920。 | - | - |
| videoResolution | int | 视频分辨率，默认值：VIDEO_RESOLUTION_TYPE_360_640。 | - | 推荐直接使用 TXLivePusher 的 setVideoQuality 接口调整画面质量。 |
| videoFPS | int | 视频帧率，默认值：15FPS。 | - | 推荐直接使用 TXLivePusher 的 setVideoQuality 接口调整画面质量。 |
| videoEncodeGop | int | 视频编码 GOP，也就是常说的关键帧间隔，单位秒；默认值：3s。 | - | 推荐直接使用 TXLivePusher 的 setVideoQuality 接口调整画面质量。 |
| videoBitratePIN | int | 视频编码的平均码率，默认值：700kbps。 | - | 推荐直接使用 TXLivePusher 的 setVideoQuality 接口调整画面质量。 |
| enableAutoBitrate | BOOL | 码率自适应开关，开启后，SDK 会根据网络情况自动调节视频码率，调节范围在 (videoBitrateMin - videoBitrateMax)。 | NO | - |
| autoAdjustStrategy | int | 码率自适应算法。 | AUTO_ADJUST_BITRATE_STRATEGY_1 | - |
| videoBitrateMax | int | 码率自适应 - 最高码率，默认值：1000kpbs。 | - | - |
| videoBitrateMin | int | 码率自适应 - 最低码率，默认值：400kpbs。 | 不要设置太低的数值，过低的码率会导致运动画面出现大面积马赛克。 | - |
| audioSampleRate | int | 音频采样率，采样率越高音质越好，对于有音乐的场景请使用48000的采样率。 | AUDIO_SAMPLE_RATE_48000 | - |
| audioChannels | int | 音频声道数，默认值：1（单声道）。 | - | - |
| enableAudioPreview | BOOL | 是否开启耳返特效。 | NO | 开启耳返会消耗更多的 CPU，只有在主播带耳机唱歌的时候才有必要开启此功能。 |
| enablePureAudioPush | BOOL | 是否为纯音频推流。 | NO | 如果希望实现纯音频推流的功能，需要在推流前就设置该参数，否则播放端会有兼容性问题。 |
| connectRetryCount | int | 推流遭遇网络连接断开时 SDK 默认重试的次数，取值范围1 - 10，默认值：3。 | - | - |
| connectRetryInterval | int | 网络重连的时间间隔，单位秒，取值范围3 - 30，默认值：3。 | - | - |
| customModeType | int | 自定义采集和自定义处理开关。 | - | 该字段需要使用与运算符进行级联操作（自定义采集和自定义处理不能同时开启）：开启自定义视频采集：\_config.customModeType &#124;= CUSTOM_MODE_VIDEO_CAPTURE；开启自定义音频采集：\_config.customModeType &#124;= CUSTOM_MODE_AUDIO_CAPTURE。 |
| sampleBufferSize | CGSize | 仅开启自定义采集时有效，用于设置编码分辨率。 | - | 此值设置需与调用 sendVideoSampleBuffer 时传入的 SampleBuffer 的宽高比一致，否则会引起画面变形。 如果指定 autoSampleBufferSize 为 YES，则不需要设置该字段。 |
| autoSampleBufferSize | BOOL | 仅开启自定义采集时有效，YES 代表编码分辨率等于输入的 SampleBuffer 的分辨率，默认值：NO。 | - | - |
| enableNAS | BOOL | 是否开启噪声抑制（注意：早期版本引入了拼写错误，考虑到接口兼容一直没有修正，正确拼写应该是 ANS）。 | NO：ANS 对于直播环境中由其它设备外放的音乐是不友好的，通过 playBGM 设置的背景音不受影响。 | 如果直播场景只有主播在说话，ANS 有助于让主播的声音更清楚，但如果主播在吹拉弹唱，ANS 会损伤乐器的声音。 |
| enableAEC | BOOL | 是否开启回声抑制。 | NO：回声抑制会启用通话模式音量，导致音质变差，非连麦场景下请不要开启。 | 只有在连麦模式下才需要开启 AEC，如果是普通的直播，将主播的手机和观众的手机放在一起所产生的啸叫是正常现象。 |
| enableHWAcceleration | BOOL | 开启视频硬件加速， 默认值：YES。 | - | - |
| enableAudioAcceleration | BOOL | 开启音频硬件加速， 默认值：YES。 | - | - |
| enableAGC | BOOL | 开启音频自动增益， 默认值：NO。 | - | - |
| volumeType | TXSystemAudioVolumeType | 系统音量类型， 默认值：SYSTEM_VOLUME_TYPE_AUTO。 | - | - |
| frontCamera | BOOL | 是否前置摄像头，待废弃，建议直接使用 TXLivePusher 的 frontCamera 属性和 switchCamera 函数。 | - | - |
| beautyFilterDepth | float | 美颜强度，待废弃，建议直接使用 TXLivePusher 的 setBeautyStyle 函数。 | - | - |
| whiteningFilterDepth | float | 美白强度，待废弃，建议直接使用 TXLivePusher 的 setBeautyStyle 函数。 | - | - |
| enableNearestIP | BOOL | 是否开启就近选路，待废弃，默认值：YES。 | - | - |
| rtmpChannelType | int | RTMP 传输通道的类型，待废弃，默认值为：AUTO。 | - | - |



 

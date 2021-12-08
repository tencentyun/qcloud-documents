## TRTCCloud @ TXLiteAVSDK

### 创建实例和事件回调
| API | 描述 |
|-----|-----|
| [sharedInstance](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ac5da416bb06d461c7e1e555e3fd143ee) | 创建 TRTCCloud 实例（单例模式） |
| [destroySharedInstance](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a69e76ca12b727c7cbcbdda274fc007a2) | 销毁 TRTCCloud 实例（单例模式）  |
| [setListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a22fe2f31f2ef62fb3c6cba083dc6c016) | 设置 TRTC 事件回调 |
| [setListenerHandler](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a48c867145dcc09289f7af41871b4fdd9) | 设置驱动 TRTCCloudDelegate 事件回调的队列 |

### 房间相关接口函数
| API | 描述 |
|-----|-----|
| [enterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#abfc1841af52e8f6a5f239a846a1e5d5c) | 进入房间 |
| [exitRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a41d16a97a9cb8f16ef92f5ef5bfebee1) | 离开房间 |
| [switchRole](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a915a4b3abca0e41f057022a4587faf66) | 切换角色 |
| [switchRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a09fbe471def0c1790357fc2b70149784) | 切换房间 |
| [ConnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ac1ab7e4a017b99bb91d89ce1b0fac5fd) | 请求跨房通话 |
| [DisconnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#af777ac398ac47c8e5649c983fa2053fa) | 退出跨房通话 |
| [setDefaultStreamRecvMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a0b8d004665d5003ce1d9a48a9ab551b3) | 设置订阅模式（需要在进入房前设置才能生效） |
| [createSubCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3c4a93d24e0ef076168b44cf3545a8d4) | 创建子房间示例（用于多房间并发观看） |
| [destroySubCloud](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a6dc091ead812c50497c4b4e87e5c2fcf) | 销毁子房间示例 |

### CDN 相关接口函数
| API | 描述 |
|-----|-----|
| [startPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a1c168a9aa35ccd0b24981526425e4730) | 开始向腾讯云直播 CDN 上发布音视频流 |
| [stopPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3067efa528fb9ffb8cf7685ce29925d4) | 停止向腾讯云直播 CDN 上发布音视频流 |
| [startPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a41aefb8be652f8f6803020e543acaadc) | 开始向非腾讯云 CDN 上发布音视频流 |
| [stopPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a0e1e8a1eb1cac3f5e5d4433b4aa21e8e) | 停止向非腾讯云 CDN 上发布音视频流 |
| [setMixTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#af7cf5544f9b8027e9526c32319a13838) | 设置云端混流的排版布局和转码参数 |

### 视频相关接口函数
| API | 描述 |
|-----|-----|
| [startLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a84098740a2e69e3d1f02735861614116) | 开启本地摄像头的预览画面（移动端） |
| [updateLocalView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ae91432ada1767f793c460c7b897b6809) | 更新本地摄像头的预览画面 |
| [stopLocalPreview](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#af6ee50bf2c4c592294061077fc727505) | 停止摄像头预览 |
| [muteLocalVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ac334d2c625c487d38eb3311de6831643) | 暂停/恢复发布本地的视频流 |
| [setVideoMuteImage](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a78195189ea5f3db9a05338f585bb925d) | 设置本地画面被暂停期间的替代图片 |
| [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a360eac7e67afcfab4390e7f37fa29a69) | 订阅远端用户的视频流，并绑定视频渲染控件 |
| [updateRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a9be8a4c5ea4da16fb1ca42e8e258effd) | 更新远端用户的视频渲染控件 |
| [stopRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a2391ba04b2d54fa1664b52f8f8546a32) | 停止订阅远端用户的视频流，并释放渲染控件 |
| [stopAllRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#addaac0786ac0bd6e73a5f35c038df127) | 停止订阅所有远端用户的视频流，并释放全部渲染资源 |
| [muteRemoteVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a4048ba6edaa0a959d0918a72cf98b576) | 暂停/恢复订阅远端用户的视频流 |
| [muteAllRemoteVideoStreams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a2d8a7b74068026a85158262cc9aedd66) | 暂停/恢复订阅所有远端用户的视频流 |
| [setVideoEncoderParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ae047d96922cb1c19135433fa7908e6ce) | 设置视频编码器的编码参数 |
| [setNetworkQosParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a02631a5e4251657875535c38ab319239) | 设置网络质量控制的相关参数 |
| [setLocalRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a916eab6c78587300165008f61a473f8b) | 设置本地画面的渲染参数 |
| [setRemoteRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a2e37d4b9555c58148ad507938375505f) | 设置远端画面的渲染模式 |
| [setVideoEncoderRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a272afecae1d291033cb9cd4b1d7b52e0) | 设置视频编码器输出的画面方向 |
| [setVideoEncoderMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a32d9ba3696b305373508253f9bee8236) | 设置编码器输出的画面镜像模式 |
| [setGSensorMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#abbbe1548bfba0bd082a08478ce35e9bc) | 设置重力感应的适配模式 |
| [enableEncSmallVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3a040c5012cf572b9dfabcca87f2cbb7) | 开启大小画面双路编码模式 |
| [setRemoteVideoStreamType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a2a018cc1010587ea9b0fbd791eb3c54f) | 切换指定远端用户的大小画面 |
| [snapshotVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ae75285c95fc53651e24fa23c4141093b) | 视频画面截图 |

### 音频相关接口函数
| API | 描述 |
|-----|-----|
| [startLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a1dadf09b10a2d128e4cef11707934329) | 开启本地音频的采集和发布 |
| [stopLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a272bba21d046347ac42d76069ba5972c) | 停止本地音频的采集和发布 |
| [muteLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a37f52481d24fa0f50842d3d8cc380d86) | 暂停/恢复发布本地的音频流 |
| [muteRemoteAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a8d8b8edf120036d4049cc3639a1ce81f) | 暂停/恢复播放远端的音频流 |
| [muteAllRemoteAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a5b63c0796404b80323ae67aafe0384ba) | 暂停/恢复播放所有远端用户的音频流 |
| [setAudioRoute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a4a3dda74823afa597b42b981257e9e22) | 设置音频路由 |
| [setRemoteAudioVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3dabe4a4e13509cf1bd5b3d58aabaa06) | 设定某一个远端用户的声音播放音量 |
| [setAudioCaptureVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a6af5e2c4819a683042f382688aff41e9) | 设定本地音频的采集音量 |
| [getAudioCaptureVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a81037b960fb2b3501b1e8e60f2b5f9f3) | 获取本地音频的采集音量 |
| [setAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a0b20e1eec637c82190c5264d78d686af) | 设定远端音频的播放音量 |
| [getAudioPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a5a1636fa1300b0b4e2829846c36450a2) | 获取远端音频的播放音量 |
| [enableAudioVolumeEvaluation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a43e99323fd5680fd377b95b97f0885c3) | 启用音量大小提示 |
| [startAudioRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a8b04666d32535637308605d5e15b7220) | 开始录音 |
| [stopAudioRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a7d55e5f15d1291afc89f7e1dfe0a25d8) | 停止录音 |
| [startLocalRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a5d6bf60e9d3051f601988e55106b296c) | 开启本地媒体录制 |
| [stopLocalRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ae982c3c04c0195711ee4e56132522c4b) | 停止本地媒体录制 |
| [checkAudioCapabilitySupport](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a225161d0c1028708b4c043653ea0ee4b) | 查询是否支持音频某种能力（仅适用于 Android） |
| [setRemoteAudioParallelParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a6d7f5080d804137be1bd3541f533b275) | 设置远端音频流智能并发播放策略 |

### 设备管理相关接口
| API | 描述 |
|-----|-----|
| [getDeviceManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ae66395bc404d205fcd7fe9082ca85ce9) | 获取设备管理类（TXDeviceManager） |

### 美颜特效和图像水印
| API | 描述 |
|-----|-----|
| [getBeautyManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3fdfeb3204581c27bbf1c8b5598714fb) | 获取美颜管理类（TXBeautyManager） |
| [setWatermark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a1083aaf0441e3d90ce6641d278a97a63) | 添加水印 |

### 背景音乐和声音特效
| API | 描述 |
|-----|-----|
| [getAudioEffectManager](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3646dad993287c3a1a38a5bc0e6e33aa) | 获取音效管理类（TXAudioEffectManager） |

### 屏幕分享相关接口
| API | 描述 |
|-----|-----|
| [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aacbe76e164030701d261a2edbc43668f) | 启动屏幕分享 |
| [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ab6c3014f6f88c775aa91fccea19ce8a4) | 停止屏幕分享 |
| [pauseScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a56af9ada2d43cfb497fe44fa6d4b99cf) | 暂停屏幕分享 |
| [resumeScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a155ed7b6bcf2edf3259d26b8f8fdfe7e) | 恢复屏幕分享 |
| [setSubStreamEncoderParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a34d994fbba559994aaf3a1f20420a885) | 设置屏幕分享（即辅路）的视频编码参数（桌面系统和移动系统均已支持） |

### 自定义采集和自定义渲染
| API | 描述 |
|-----|-----|
| [enableCustomVideoCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa29d36eaa707f6acf622e2f87f14b26a) | 启用/关闭视频自定义采集模式 |
| [sendCustomVideoData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ad898c0d44a55b86af57de9854638193e) | 向 SDK 投送自己采集的视频帧 |
| [enableCustomAudioCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a206b9ce3594aa535b633d4f7c8f97210) | 启用音频自定义采集模式 |
| [sendCustomAudioData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a30a542b7d540c8699595a22ca3401f29) | 向 SDK 投送自己采集的音频数据 |
| [enableMixExternalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a7b7d3707d2ed8e8f1221faf73af49027) | 启用/关闭自定义音轨 |
| [mixExternalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a899a1e9d42c9bf9ce1474aec13ac6747) | 向 SDK 混入自定义音轨 |
| [setMixExternalAudioVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a362490afb9028595635b52d041a2bfb0) | 设置推流时混入外部音频的推流音量和播放音量 |
| [generateCustomPTS](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a0b36383129314d70f150c08de182e2b8) | 生成自定义采集时的时间戳 |
| [setLocalVideoProcessListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a0b565dc8c77df7fb826f0c45d8ad2d85) | 设置第三方美颜的视频数据回调 |
| [setLocalVideoRenderListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa3cbb7a501c3151d94473965e2538c7a) | 设置本地视频自定义渲染回调 |
| [setRemoteVideoRenderListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a4fca6803d13e4c7ff00dcac2974637e4) | 设置远端视频自定义渲染回调 |
| [setAudioFrameListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a034b6fce9a517267acd874c243efc575) | 设置音频数据自定义回调 |
| [setCapturedRawAudioFrameCallbackFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a9047b34857b12d85688b3b3f1ca1c3f0) | 设置本地麦克风采集出的原始音频帧回调格式 |
| [setLocalProcessedAudioFrameCallbackFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ac0f65e13815edc05ebd765826a94e3dc) | 设置经过前处理后的本地音频帧回调格式 |
| [setMixedPlayAudioFrameCallbackFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a98a2e38d75366fbc2c4da92fec5c0a30) | 设置最终要由系统播放出的音频帧回调格式 |
| [enableCustomAudioRendering](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#addb4c87719393cd4c4765d66a8cd9803) | 开启音频自定义播放 |
| [getCustomAudioRenderingFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a1c1c268173ab9b1bc24d34766e433931) | 获取可播放的音频数据 |

### 自定义消息发送接口
| API | 描述 |
|-----|-----|
| [sendCustomCmdMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa4847ad53acc9ab5990194b21ff5b070) | 使用 UDP 通道发送自定义消息给房间内所有用户  |
| [sendSEIMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a034f9e1effbdadf8b9bfb7f3f06486c4) | 使用 SEI 通道发送自定义消息给房间内所有用户  |

### 网络测试接口
| API | 描述 |
|-----|-----|
| [startSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a6db053500be88a8735bfc69730447912) | 开始进行网速测试（进入房间前使用） |
| [stopSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3e862cef0e818ddecdc3dc4d66a6f8f9) | 停止网络测速 |

### 调试相关接口
| API | 描述 |
|-----|-----|
| [getSDKVersion](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aeb5168abbd62c631b65247e6289d1e2d) | 获取 SDK 版本信息 |
| [setLogLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a0ec9520dda7e2062f7455956d093113b) | 设置 Log 输出级别 |
| [setConsoleEnabled](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a2942d9d05045d3f0e0add45a3e10b3ee) | 启用/禁用控制台日志打印 |
| [setLogCompressEnabled](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a495d2122a4098ab371d825c1f0bb90f5) | 启用/禁用日志的本地压缩 |
| [setLogDirPath](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a44c20358d08da798e0f15d142c9c3914) | 设置本地日志的保存路径 |
| [setLogListener](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a299a71f4addb3638c7790de446fbdf37) | 设置日志回调 |
| [showDebugView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ad2cdb5d447114534f53bad5bdc48afba) | 显示仪表盘 |
| [setDebugViewMargin](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa2014c293033e9ea60aa6ffd525ee2fa) | 设置仪表盘的边距 |
| [callExperimentalAPI](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a37f331dd0cfff51ab5a3becf4950a55e) | 调用实验性接口 |
| [setNetEnv](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a28ae49c86c5e5ba7e5ad2eae171bde76) | 设置 TRTC 的后台集群(仅适用于腾讯云研发团队) |

### 废弃接口
| API | 描述 |
|-----|-----|
| [setMicVolumeOnMixing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ab356494d1b7dd924be69b23aa631a85a) | 设置麦克风的音量大小 |
| [setBeautyStyle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a46ffe2b60f916a87345fb357110adf10) | 设置美颜、美白以及红润效果级别 |
| [setEyeScaleLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a4ff69ce783f648f23dd737641344ac52) | 设置大眼级别 |
| [setFaceSlimLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a78a159a2a45d24dbd5722eb73d237e8a) | 设置瘦脸级别 |
| [setFaceVLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a58bb7ce1fbbc40a50647d64693ac5d41) | 设置 V 脸级别 |
| [setChinLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a774eb948494cecec024771434ccd9d3c) | 设置下巴拉伸或收缩幅度 |
| [setFaceShortLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa14091f0d02330cbd02da5186e9dd874) | 设置短脸级别 |
| [setNoseSlimLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3f806534b2596d7e29ea0ea6c070b591) | 设置瘦鼻级别 |
| [selectMotionTmpl](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a521a0446d0922d480a1eec4b86f1ecb2) | 设置动效贴纸 |
| [setMotionMute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a066cbf8f4f6c1cd23fe9451b82c5a073) | 设置动效静音 |
| [setFilter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a925323ab809957ccaeb4cef30841cb72) | 设置色彩滤镜效果 |
| [setFilterConcentration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a5fb4c8bc9948e61a75b9ef85f618309d) | 设置色彩滤镜浓度 |
| [setGreenScreenFile](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aef56a36b901d5e525ee539e7d5642063) | 设置绿幕背景视频 |
| [playBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3df738557f5c658c37174ac9aeae9684) | 启动播放背景音乐 |
| [stopBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a3ee7bdd15de4ba9010aa5ece3abff0ab) | 停止播放背景音乐 |
| [pauseBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a21ddee03e6f4cec028a24e5d5e30955e) | 停止播放背景音乐 |
| [resumeBGM](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aaa8b34ef2b334bd22a1cb6541a4c6702) | 停止播放背景音乐 |
| [getBGMDuration](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ae7342a8bcfda22a872aa684f06a4677f) | 获取背景音乐总时长（单位：毫秒） |
| [setBGMPosition](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a78f901b6175352a31b0236776bfdc661) | 设置背景音乐的播放进度 |
| [setBGMVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ada9c2b4aaf9a1a9ab9cd846593fdf9e6) | 设置背景音乐的音量大小 |
| [setBGMPlayoutVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ab1e1c94c9efd967dbffb46d3ba08fef5) | 设置背景音乐的本地播放音量 |
| [setBGMPublishVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a535eab48f9df390f4de5ebd5afcd59e3) | 设置背景音乐的远端播放音量 |
| [setReverbType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a6f4f89be3c810acfa2430ad65fd7ea68) | 设置混响效果 |
| [setVoiceChangerType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a37acaf3b2539e0b1c18123a646e91189) | 设置变声类型 |
| [playAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ad1ed7667282eccfac1992c1e547a5aeb) | 播放音效 |
| [setAudioEffectVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a214846db40c2d1be2fe8008c6637f631) | 设置音效音量 |
| [setAudioEffectVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a214846db40c2d1be2fe8008c6637f631) | 停止播放音效 |
| [stopAllAudioEffects](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a770543c80d3a5629a26d1382535fb6c4) | 停止所有音效 |
| [setAllAudioEffectsVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a9bb41c4ff1a5b24ca742fe3ce45a2bc0) | 设置所有音效音量 |
| [pauseAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ab32923d04ce164b82879b3e05833959f) | 暂停音效 |
| [resumeAudioEffect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a33ab6e798d3da245435166464b702d4f) | 暂停音效 |
| [enableAudioEarMonitoring](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a9306bca7c6a13e0443a3fa1b40c9f343) | 开启（或关闭）耳返 |
| [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a360eac7e67afcfab4390e7f37fa29a69) | 开始显示远端视频画面 |
| [stopRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a2391ba04b2d54fa1664b52f8f8546a32) | 停止显示远端视频画面，同时不再拉取该远端用户的视频数据流 |
| [setRemoteViewFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ab4197bc2efb62b471b49f926bab9352f) | 设置远端图像的渲染模式 |
| [setRemoteViewRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a8478d804d2a07520ce2bc5466b727839) | 设置远端图像的顺时针旋转角度 |
| [setLocalViewFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#af36ab721c670e5871e5b21a41518b51d) | 设置本地图像的渲染模式 |
| [setLocalViewRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a87fd1307871debc7c051de4878eb6d69) | 设置本地图像的顺时针旋转角度 |
| [setLocalViewMirror](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa353b5cf5662c43252eb8e5132f041c1) | 设置本地摄像头预览画面的镜像模式 |
| [startRemoteSubStreamView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#acdbe3829d20f58cedd5a0c2f49ea24dc) | 开始显示远端用户的辅路画面 |
| [stopRemoteSubStreamView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ae5f540d795425046c9166b0a2361a8de) | 停止显示远端用户的辅路画面 |
| [setRemoteSubStreamViewFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a73f66e66ffee44e19ebb4d8c56c89718) | 设置辅路画面的填充模式 |
| [setRemoteSubStreamViewRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#affdf177b468fdf40a41782e2e47524cc) | 设置辅路画面的顺时针旋转角度 |
| [setPriorRemoteVideoStreamType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ad2efc2703c86ee009bd4a1d440d0c1e0) | 设定优先观看大画面还是小画面 |
| [setAudioQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a955cccaddccb0c993351c656067bee55) | 设置音频质量 |
| [startLocalAudio](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a1dadf09b10a2d128e4cef11707934329) | 设置音频质量 |
| [switchCamera](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a1b43a65a32f9dcb81b39b9c51c5bc4c6) | 切换摄像头 |
| [isCameraZoomSupported](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ac7ae26eca2f9a673121803d6d175b034) | 查询当前摄像头是否支持缩放 |
| [setZoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a9f761eebdf04f724e0d1591c41c6045f) | 设置摄像头缩放倍数（焦距） |
| [isCameraTorchSupported](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a645183ba7c0cea748973796cb38aad8c) | 查询是否支持开关闪光灯 |
| [enableTorch](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a09253f6547914d54058831b61325e770) | 开关/关闭闪光灯 |
| [isCameraFocusPositionInPreviewSupported](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#abd39aca40adfc8da6beaf32141f84cfa) | 查询摄像头是否支持设置焦点 |
| [setFocusPosition](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa7c65fb033727804e7a79b8f135c776c) | 设置摄像头焦点坐标位置 |
| [isCameraAutoFocusFaceModeSupported](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a23f25ffb81215a32517da78455459ff2) | 查询是否支持自动识别人脸位置 |
| [setSystemVolumeType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a5438dcc45dc2f26a3771a5feddcdef5d) | 设置系统音量类型 |
| [enableCustomVideoCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa29d36eaa707f6acf622e2f87f14b26a) | 启用视频自定义采集模式 |
| [sendCustomVideoData](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ad898c0d44a55b86af57de9854638193e) | 投送自己采集的视频数据 |
| [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aacbe76e164030701d261a2edbc43668f) | 启动屏幕分享（Android） |
| [muteLocalVideo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#ac334d2c625c487d38eb3311de6831643) | 暂停/恢复发布本地的视频流 |
| [muteRemoteVideoStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a4048ba6edaa0a959d0918a72cf98b576) | 暂停 / 恢复订阅远端用户的视频流 |
| [startSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a6db053500be88a8735bfc69730447912) |  开始进行网络测速（进入房间前使用） |

### 错误和警告事件
| API | 描述 |
|-----|-----|
| [onError](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a511d0007e1990e63e853e46ce3f02670) | 错误事件回调 |
| [onWarning](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a9871472ee8195dfc5d0c34fae3294465) | 警告事件回调 |

### 房间相关事件回调
| API | 描述 |
|-----|-----|
| [onEnterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#abf0525c3433cbd923fd1f13b42c416a2) | 进入房间成功与否的事件回调 |
| [onExitRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ad5ac26478033ea9c0339462c69f9c89e) | 离开房间的事件回调 |
| [onSwitchRole](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a6a4b7f39bc5dfb0c5d75ef8802e2e758) | 切换角色的事件回调 |
| [onSwitchRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a9778a84932f02de9be52ea7513f606c1) | 切换房间的结果回调 |
| [onConnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ac9fd524ab9de446f4aaf502f80859e95) | 请求跨房通话的结果回调 |
| [onDisConnectOtherRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a6f7db4f0aaadad2cdfa822ba0060414c) | 结束跨房通话的结果回调 |

### 用户相关事件回调
| API | 描述 |
|-----|-----|
| [onRemoteUserEnterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a891f38e4cdeaf3ff18937726f0269c2c) | 有用户加入当前房间 |
| [onRemoteUserLeaveRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#abfec3607f97823956fad77a7a63dc441) | 有用户离开当前房间 |
| [onUserVideoAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ac1a0222f5b3e56176151eefe851deb05) | 某远端用户发布/取消了主路视频画面 |
| [onUserSubStreamAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a80bcaac82e5372245746a4bc63656390) | 某远端用户发布/取消了辅路视频画面 |
| [onUserAudioAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ac474bbf919f96c0cfda87c93890d871f) | 某远端用户发布/取消了自己的音频 |
| [onFirstVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a0c1ccf1bec2d3261e9f11894b32e357e) | SDK 开始渲染自己本地或远端用户的首帧画面 |
| [onFirstAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a3516aaef4cb63e512cd713e4ec96d118) | SDK 开始播放远端用户的首帧音频 |
| [onSendFirstLocalVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a181788d7441d41022ce014095ee05353) | 自己本地的首个视频帧已被发布出去 |
| [onSendFirstLocalAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#acb73daf4ce82cd03f787f057b233b412) | 自己本地的首个音频帧已被发布出去 |
| [onRemoteVideoStatusUpdated](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#aa75cd2a93cfb096357e2de226ff2ea47) | 远端视频状态变化的事件回调 |

### 网络和技术指标统计回调
| API | 描述 |
|-----|-----|
| [onNetworkQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#aba07d4191391dadef900422521f34e5b) | 网络质量的实时统计回调 |
| [onStatistics](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a24a6ee3b3709a42af226be7258521612) | 音视频技术指标的实时统计回调 |
| [onSpeedTestResult](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a0dc9967589d6d3277f0e429e520f2c51) | 网速测试的结果回调 |

### 与云端连接情况的事件回调
| API | 描述 |
|-----|-----|
| [onConnectionLost](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#aed43a70b4a95eb95181e2b410013bf54) | SDK 与云端的连接已经断开 |
| [onTryToReconnect](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a1c8654b64e4bde42a8a24954ecf2cb2d) | SDK 正在尝试重新连接到云端 |
| [onConnectionRecovery](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a36d96a42ec4b00a0e3808f7f8460cd7f) | SDK 与云端的连接已经恢复 |

### 硬件设备相关事件回调
| API | 描述 |
|-----|-----|
| [onCameraDidReady](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#aaa74021e5fd2564afb2df50e25eedeff) | 摄像头准备就绪 |
| [onMicDidReady](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#afdac7dee94451913a4dc9982badc8035) | 麦克风准备就绪 |
| [onAudioRouteChanged](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a1a608275247d2912e26bd83f648d6378) | 当前音频路由发生变化（仅适用于移动设备） |
| [onUserVoiceVolume](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a4e3b79968ccbb86de5b79e326a2daafa) | 音量大小的反馈回调 |

### 自定义消息的接收事件回调
| API | 描述 |
|-----|-----|
| [onRecvCustomCmdMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a51fd654c5ec030ff84f208f2ba50298d) | 收到自定义消息的事件回调 |
| [onMissCustomCmdMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a98af11ba5b25d3124bd9533dc5197127) | 自定义消息丢失的事件回调 |
| [onRecvSEIMsg](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ad3640e6bf80a1f93991644701e9b0d96) | 收到 SEI 消息的回调 |

### CDN 相关事件回调
| API | 描述 |
|-----|-----|
| [onStartPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a03d0ef687b2973b9b13cb041bd35bb85) | 开始向腾讯云直播 CDN 上发布音视频流的事件回调 |
| [onStopPublishing](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ad3cb7e5ceb69954d762eafca5a0e3a62) | 停止向腾讯云直播 CDN 上发布音视频流的事件回调 |
| [onStartPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a64df36d6c56dd69d8b6f051fd9fffcbc) | 开始向非腾讯云 CDN 上发布音视频流的事件回调 |
| [onStopPublishCDNStream](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a6c3d63538897ddb9ed1b170819c41dca) | 停止向非腾讯云 CDN 上发布音视频流的事件回调 |
| [onSetMixTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#af1c79a5ec3e0c106939e7f0d7849d694) | 设置云端混流的排版布局和转码参数的事件回调 |

### 屏幕分享相关事件回调
| API | 描述 |
|-----|-----|
| [onScreenCaptureStarted](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a7d15537d26fb001045ff95157d59ed3f) | 屏幕分享开启的事件回调 |
| [onScreenCapturePaused](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a12c57991389e32f04a56774df5d1ce76) | 屏幕分享暂停的事件回调 |
| [onScreenCaptureResumed](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ade88963a254d297d3be1993e8a599f6e) | 屏幕分享恢复的事件回调 |
| [onScreenCaptureStopped](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a6c09b21b733da7d314d1db2cb03c8bcb) | 屏幕分享停止的事件回调 |

### 本地录制和本地截图的事件回调
| API | 描述 |
|-----|-----|
| [onLocalRecordBegin](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a6d252931944577cc08d40db1f5ecd7bb) | 本地录制任务已经开始的事件回调 |
| [onLocalRecording](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a22f09234dc198d33fa38bbb595fb5764) | 本地录制任务正在进行中的进展事件回调 |
| [onLocalRecordComplete](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a0a3eef0daeb5107290cb5190ceb9467b) | 本地录制任务已经结束的事件回调 |

### 废弃的事件回调
| API | 描述 |
|-----|-----|
| [onUserEnter](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#aff18b3bc5b1e448b21b7614e5716e73e) | 有主播加入当前房间（已废弃） |
| [onUserExit](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a0d1361e52e96b4c7c1a5f1b89f4ef0fb) | 有主播离开当前房间（已废弃） |
| [onAudioEffectFinished](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#abe967d855abae66836877fe0dacf8b5f) | 音效播放已结束（已废弃） |
| [onSpeedTest](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ab77a0dff287e1642527cd414fc5fe5f5) | 服务器测速的结果回调（已废弃） |

### 视频数据自定义回调
| API | 描述 |
|-----|-----|
| [onRenderVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a41b44f9b0583bbf56ad9e96065ea825c) | 自定义视频渲染回调 |
| [onGLContextCreated](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#af4a7a3a4e4945bf216d87f81b6926dab) | SDK 内部 OpenGL 环境已经创建的通知 |
| [onProcessVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a22afb08b2a1a18563c7be28c904b166a) | 用于对接第三方美颜组件的视频处理回调 |
| [onGLContextDestory](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a5f6d5ef01d3cd610959433107f78aa60) | SDK 内部 OpenGL 环境被销的通知 |

### 音频数据自定义回调
| API | 描述 |
|-----|-----|
| [onCapturedRawAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#abffd560f5b2b2322ea3980bc5a91d22e) | 本地麦克风采集到的原始音频数据回调 |
| [onLocalProcessedAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a62c526c6c30a66671260bdf0c5c64e46) | 本地采集并经过音频模块前处理后的音频数据回调 |
| [onRemoteUserAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a4af98a7d668c150ea8e99e3085505902) | 混音前的每一路远程用户的音频数据 |
| [onMixedPlayAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a580e94224357c38adf6ed883ab3321f7) | 将各路待播放音频混合之后并在最终提交系统播放之前的数据回调 |
| [onMixedAllAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a96923a9286a88b83d6890f607884ceb3) | SDK 所有音频混合后的音频数据（包括采集到的和待播放的） |

### 更多事件回调接口
| API | 描述 |
|-----|-----|
| [onLog](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#a77d78090666e330606b670bf8ce2d854) | 本地 LOG 的打印回调 |

### 视频相关枚举值定义
| API | 描述 |
|-----|-----|
| [TRTCVideoResolution](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp01d5e1111c2ba49a53879c343fd484f2) | 视频分辨率 |
| [TRTCVideoResolutionMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp509a1d5f7a44e1d60cf25e4afb640347) | 视频宽高比模式 |
| [TRTCVideoStreamType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp8f7c7bceb683fdba0c3cb0a4766dd281) | 视频流类型 |
| [TRTCVideoFillMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCVideoFillMode) | 视频画面填充模式 |
| [TRTCVideoRotation](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp9edface2441370ef72f70dd4945ff0f9) | 视频画面旋转方向 |
| [TRTCBeautyStyle](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrpa173483f8f2f9cbfd604328c0a8cba50) | 美颜（磨皮）算法 |
| [TRTCVideoPixelFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrpde7f16ea7692e7c649e9a16638f48dbe) | 视频像素格式 |
| [TRTCVideoBufferType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp2c1424df181810edcbd68a9d2cb4adde) | 视频数据传递方式 |
| [TRTCVideoMirrorType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrpa367a3c86bde4916b80b03acd05ec218) | 视频的镜像类型 |
| [TRTCSnapshotSourceType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCSnapshotSourceType) | 本地视频截图的数据源 |

### 网络相关枚举值定义
| API | 描述 |
|-----|-----|
| [TRTCAppScene](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrpa53ec28e9d73b79c701a709f44efbebe) | 应用场景 |
| [TRTCRoleType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp32cd3ba884366b8a2d45cad705f28b18) | 角色 |
| [TRTCQosControlMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp39c937e1be1c70563f58a5a6fdde96a1) | 流控模式（已废弃） |
| [TRTCVideoQosPreference](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp3a953a9777c6e1447a27bc454f9f00b9) | 画质偏好 |
| [TRTCQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp43d6beae8b3d7c79f02df2f125c090a7) | 网络质量 |
| [TRTCAVStatusType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp5f5cc2365ee675bbc0f5a14095b1e0fc) | 视频状态类型 |
| [TRTCAVStatusChangeReason](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp66f48a69ecc92051ca32055008a19c3e) | 视频状态变化原因类型 |

### 音频相关枚举值定义
| API | 描述 |
|-----|-----|
| [TRTCAudioSampleRate](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp2b7efdf7211746ab55166bb4d55ed619) | 音频采样率 |
| [TRTCAudioQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp96d66d1098694549803eaba6baedb9c0) | 声音音质 |
| [TRTCAudioRoute](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp7340a7d82950a691c95bde594a44959f) | 音频路由（即声音的播放模式） |
| [TRTCReverbType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp30e899d6cb29154e1d73867d199b7191) | 声音混响模式 |
| [TRTCVoiceChangerType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrpac19166c196a2905657f2a3b52a68ce0) | 变声类型 |
| [TRTCSystemVolumeType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp70bfa071c4ebab5e7ed1811a780a53d9) | 系统音量类型（仅适用于移动设备） |
| [TRTCAudioCapabilityType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp29e12a3869cc165605dc0121e56888a3) | 系统支持的音频能力类型（仅适用于 Android 设备） |

### 更多枚举值定义
| API | 描述 |
|-----|-----|
| [TRTCLogLevel](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp2f4911d8563ae1db783b963d626681d8) | Log 级别 |
| [TRTCGSensorMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp7821baad731a6db4d8977d304fafce63) | 重力感应开关（仅适用于移动端） |
| [TRTCTranscodingConfigMode](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp5e2e800d31dc99373db17e2def3afc99) | 云端混流的排版模式 |
| [TRTCRecordType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrpaa193560ab798cc5dcdb9624ce9740aa) | 媒体录制类型 |
| [TRTCMixInputType](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrpa7e631ba74d7c9f6832a6ad3be7a81af) | 混流输入类型 |
| [TRTCAudioRecordingContent](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#amgrp25c9df32061d8ad991f04b21fc6acacb) | 音频录制内容类型 |

### TRTC 核心类型定义
| API | 描述 |
|-----|-----|
| [TRTCParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#a7ff9e03272f5c8e7b585e8c4eea784e1) | 进房参数 |
| [TRTCVideoEncParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCVideoEncParam) | 视频编码参数 |
| [TRTCNetworkQosParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCNetworkQosParam) | 网络流控（Qos）参数集 |
| [TRTCRenderParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCRenderParams) | 视频画面的渲染参数 |
| [TRTCQualityInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCQualityInfo) | 网络质量 |
| [TRTCVolumeInfo](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCVolumeInfo) | 音量大小 |
| [TRTCSpeedTestParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCSpeedTestParams) | 测速参数 |
| [TRTCSpeedTestResult](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCSpeedTestResult) | 网络测速结果 |
| [TRTCTexture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCTexture) | 视频纹理数据（仅适用于 Android 平台，包含纹理 ID 及 EGL 环境） |
| [TRTCVideoFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCVideoFrame) | 视频帧信息 |
| [TRTCAudioFrame](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCAudioFrame) | 音频帧数据 |
| [TRTCMixUser](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#ac5b1947f21f77726cbff822eaf0003f9) | 云端混流中各路画面的描述信息 |
| [TRTCTranscodingConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#a6066a5537ad8c1bc6158d43e8a4765db) | 云端混流的排版布局和转码参数 |
| [TRTCPublishCDNParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCPublishCDNParam) | 向非腾讯云 CDN 上发布音视频流时需设置的转推参数 |
| [TRTCAudioRecordingParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCAudioRecordingParams) | 本地音频文件的录制参数 |
| [TRTCLocalRecordingParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCLocalRecordingParams) | 本地媒体文件的录制参数 |
| [TRTCAudioEffectParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#ad82a59c2209c0596dabaee1152820494) | 音效参数（已废弃） |
| [TRTCSwitchRoomConfig](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#a1b79e0e45a5f137df2e1995af7c0885c) | 房间切换参数 |
| [TRTCAudioFrameCallbackFormat](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#a9b833660fc60bd0b4e0c0625d2ad84f6) | 音频自定义回调的格式参数 |
| [TRTCScreenShareParams](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__android.html#classcom_1_1tencent_1_1trtc_1_1TRTCCloudDef_1_1TRTCScreenShareParams) | 屏幕分享参数（仅适用于 Android 平台） |


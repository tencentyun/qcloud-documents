## TRTCParams

__功能__

进房相关参数。

__介绍__

只有该参数填写正确，才能顺利调用 enterRoom 进入 roomId 所指定的音视频房间。




__属性列表__

| 属性 | 类型 | 是否必填|字段含义 | 推荐取值 |
|-----|-----|-----|-----|-----|
| sdkAppId | uint |是| 应用标识，腾讯云基于 sdkAppId 完成计费统计。 | 在 [实时音视频控制台](https://console.cloud.tencent.com/rav/) 创建应用后可在帐号信息页面中得到该 ID。 |
| userId | string | 是|用户标识。当前用户的 userId，相当于用户名，使用 UTF-8 编码。 | 如果一个用户在您的帐号系统中的 ID 为“abc”，则 userId 即可设置为“abc”。 |
| userSig | string | 是|用户签名，当前 userId 对应的验证签名，相当于登录密码。 | 具体计算方法请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |
| roomId | uint | 是|房间号码，在同一个房间内的用户可以看到彼此并进行视频通话。 | 您可以自定义设置该参数值，但不可重复。如果您的用户帐号 ID （userId）为数字类型，可直接使用创建者的用户 ID 作为 roomId。 |
| role | [TRTCRoleType](https://cloud.tencent.com/document/product/647/36780#trtcroletype) | 否| 直播场景下的角色，仅适用于直播场景（TRTCAppSceneLIVE），视频通话场景下指定无效。 | 默认值：主播（TRTCRoleAnchor）。 |
| privateMapKey | string | 否|房间签名，当您希望某个房间只能让特定的 userId 进入时，需要使用 privateMapKey 进行权限保护。 | 仅建议有高级别安全需求的客户使用，更多详情请参见 [进房权限保护](https://cloud.tencent.com/document/product/647/32240)。 |
| businessInfo | string |  否|业务数据，部分高级特性才需要使用该字段。 | 不建议使用。 |




## TRTCVideoEncParam

__功能__

视频编码参数。

__介绍__

该设置决定远端用户看到的画面质量（同时也是云端录制出的视频文件的画面质量）。




__属性列表__

| 属性 | 类型 | 字段含义 | 推荐取值 | 特别说明 |
|-----|-----|-----|-----|-----|
| videoResolution | [TRTCVideoResolution](https://cloud.tencent.com/document/product/647/36780#trtcvideoresolution) | 视频分辨率。 |<li>视频通话建议选择360 × 640及以下分辨率，resMode 选择 Portrait。</li><li>手机直播建议选择 540 × 960，resMode 选择 Portrait。</li><li>Window 和 iMac 建议选择 640 × 360 及以上分辨率，resMode 选择 Landscape。 |  TRTCVideoResolution 默认只有横屏模式的分辨率，例如640 × 360。如需使用竖屏分辨率，请指定 resMode 为 Portrait，例如640 × 360结合 Portrait 则为360 × 640。 |
| resMode | [TRTCVideoResolutionMode](https://cloud.tencent.com/document/product/647/36780#trtcvideoresolutionmode) | 分辨率模式（横屏分辨率 - 竖屏分辨率）。 | 手机直播建议选择 Portrait，Window 和 iMac 建议选择 Landscape。 | 如果 videoResolution 指定分辨率 640 × 360，resMode 指定模式为 Portrait，则最终编码出的分辨率为360 × 640。 |
| videoFps | uint | 视频采集帧率。 | 15fps或20fps。<li>5fps以下，卡顿感明显。</li><li>10fps以下，会有轻微卡顿感。</li><li>20fps以上，则过于浪费（电影的帧率为24fps）。 | 很多 Android 手机的前置摄像头并不支持15fps以上的采集帧率，部分过于突出美颜功能的 Android 手机前置摄像头的采集帧率可能低于10fps。 |
| videoBitrate | uint | 视频上行码率。 | 推荐设置请参考 [TRTCVideoResolution](#trtcvideoresolution) 定义处的注释说明。 | 码率太低会导致视频中出现大量马赛克。 |




## TRTCNetworkQosParam

__功能__

网络流控相关参数。

__介绍__

网络流控相关参数，该设置决定 SDK 在各种网络环境下的调控方向（例如弱网下选择“保清晰”或“保流畅”）。




__属性列表__

| 属性 | 类型 | 字段含义 | 推荐取值 | 特别说明 |
|-----|-----|-----|-----|-----|
| preference | [TRTCVideoQosPreference](https://cloud.tencent.com/document/product/647/36780#trtcvideoqospreference) | 弱网下选择“保清晰”或“保流畅”。 | - | <li>弱网下保流畅：在遭遇弱网环境时，画面会变得模糊，且出现较多马赛克，但可以保持流畅不卡顿。</li><li>弱网下保清晰：在遭遇弱网环境时，画面会尽可能保持清晰，但可能容易出现卡顿。 |
| controlMode | [TRTCQosControlMode](https://cloud.tencent.com/document/product/647/36780#trtcqoscontrolmode) | 视频分辨率（云端控制 - 客户端控制）。 | 云端控制 | <li>Server 模式（默认）：云端控制模式，若无特殊原因，请直接使用该模式。</li><li>Client 模式：客户端控制模式，用于 SDK 开发内部调试，客户请勿使用。 |




## TRTCQualityInfo

__功能__

视频质量。

__介绍__

表示视频质量的好坏，通过该参数值，您可以在 UI 界面上用图标表征 userId 的通话线路质量。


__属性列表__

| 属性 | 类型 | 字段含义 |
|-----|-----|-----|
| userId | string | 用户标识。 |
| quality | [TRTCQuality](https://cloud.tencent.com/document/product/647/36780#trtcquality) | 视频质量。 |




## TRTCVolumeInfo

__功能__

音量大小。

__介绍__

表示语音音量的评估大小，通过该参数值，您可以在 UI 界面上用图标表征 userId 是否在说话。




__属性列表__

| 属性 | 类型 | 字段含义 |
|-----|-----|-----|
| userId | string | 说话者的 userId，字符编码格式为 UTF-8。 |
| volume | uint | 说话者的音量，取值范围0 - 100。 |




## TRTCSpeedTestResult

__功能__

网络测速结果。

__介绍__

您可以在用户进入房间前通过 TRTCCloud 的 startSpeedTest 接口进行测速 （注意：请不要在通话中调用），测速结果每2 - 3秒钟返回1次，每次返回1个 IP 地址的测试结果。

__属性列表__

| 属性 | 类型 | 字段含义 |
|-----|-----|-----|
| ip | string | 服务器 IP 地址。 |
| quality | [TRTCQuality](https://cloud.tencent.com/document/product/647/36780#trtcquality) | 网络质量，内部通过评估算法测算出的网络质量，loss 越低，rtt 越小，得分便越高。 |
| upLostRate | float | 上行丢包率，范围是0 - 1.0，例如，0.3表示每向服务器发送10个数据包可能会在中途丢失3个。 |
| downLostRate | float | 下行丢包率，范围是0 - 1.0，例如，0.2表示每从服务器收取10个数据包可能会在中途丢失2个。 |
| rtt | int | 延迟（毫秒），指 SDK 到腾讯云服务器的一次网络往返时间，该值越小越好，正常数值范围是10ms - 100ms。 |




## TRTCMixUser

__功能__

云端混流中每一路子画面的位置信息。

__介绍__

[TRTCMixUser](https://cloud.tencent.com/document/product/647/36780#trtcmixuser) 用于指定每一路（即每一个 userId）视频画面的具体摆放位置。




__属性列表__

| 属性 | 类型 | 字段含义 |
|-----|-----|-----|
| userId | string | 参与混流的 userId。 |
| roomId | string | 参与混流的 roomId，跨房流传入的实际 roomId，当前房间流传入 roomId = NULL。 |
| rect | RECT | 图层位置坐标以及大小，左上角为坐标原点(0,0) （绝对像素值）。 |
| zOrder | int | 图层层次（1 - 15）不可重复。 |
| pureAudio | bool | 是否纯音频。 |
| streamType | [TRTCVideoStreamType](https://cloud.tencent.com/document/product/647/36780#trtcvideostreamtype) | 参与混合的是主路画面（TRTCVideoStreamTypeBig）或屏幕分享（TRTCVideoStreamTypeSub）画面。 |




## TRTCTranscodingConfig

__功能__

云端混流（转码）配置。

__介绍__

包括最终编码质量和各路画面的摆放位置。




__属性列表__

| 属性 | 类型 | 字段含义 | 推荐取值 |
|-----|-----|-----|-----|
| mode | [TRTCTranscodingConfigMode](https://cloud.tencent.com/document/product/647/36780#trtctranscodingconfigmode) | 转码 config 模式。 | - |
| appId | uint | 腾讯云直播 AppID。 | 请在 [实时音视频控制台](https://console.cloud.tencent.com/rav) 选择已经创建的应用，单击【帐号信息】，在“直播信息”中获取。 |
| bizId | uint | 腾讯云直播 bizid。 | 请在 [实时音视频控制台](https://console.cloud.tencent.com/rav) 选择已经创建的应用，单击【帐号信息】，在“直播信息”中获取。 |
| videoWidth | uint | 最终转码后的视频分辨率的宽度（px）。 | - |
| videoHeight | uint | 最终转码后的视频分辨率的高度（px）。 | - |
| videoBitrate | uint | 最终转码后的视频分辨率的码率（kbps）。 | - |
| videoFramerate | uint | 最终转码后的视频分辨率的帧率（FPS）。 | 15 |
| videoGOP | uint | 最终转码后的视频分辨率的关键帧间隔（又称为 GOP），单位为秒。 | 3 |
| audioSampleRate | uint | 最终转码后的音频采样率。 | 48000 |
| audioBitrate | uint | 最终转码后的音频码率（kbps）。 | 64 |
| audioChannels | uint | 最终转码后的音频声道数。 | 2 |
| mixUsersArray | [TRTCMixUser[]](https://cloud.tencent.com/document/product/647/36780#trtcmixuser) | 每一路子画面的位置信息。 | - |
| mixUsersArraySize | uint | 数组 mixUsersArray 的大小。 | - |




## TRTCPublishCDNParam

__功能__

CDN 旁路推流参数。




__属性列表__

| 属性 | 类型 | 字段含义 |
|-----|-----|-----|
| appId | uint | 腾讯云 AppID，请在 [实时音视频控制台](https://console.cloud.tencent.com/rav) 选择已经创建的应用，单击【帐号信息】，在“直播信息”中获取。 |
| bizId | uint | 腾讯云直播 bizid，请在 [实时音视频控制台](https://console.cloud.tencent.com/rav) 选择已经创建的应用，单击【帐号信息】，在“直播信息”中获取。 |
| url | string | 旁路转推的 URL。 |




## TRTCAudioRecordingParams

__功能__

录音参数。

__介绍__

请正确填写参数，确保录音文件顺利生成。




__属性列表__

| 属性 | 类型 | 字段含义 | 特别说明 |
|-----|-----|-----|-----|
| filePath | string | 文件路径（必填），录音文件的保存路径。该路径需要用户自行指定，请确保路径存在且可写。 | 该路径需精确到文件名及格式后缀，格式后缀决定录制文件的格式，目前支持的格式有 PCM、WAV 和 AAC。例如，指定路径为 path/to/audio.aac，则会生成一个 AAC 格式的文件。请指定一个有读写权限的合法路径，否则录音文件无法生成。 |




## TRTCAudioEffectParam

__功能__

音效。




__属性列表__

| 属性 | 类型 | 字段含义 | 推荐取值 |
|-----|-----|-----|-----|
| effectId | int | 音效 ID， 【特殊说明】SDK 允许播放多路音效，因此需要音效 ID 进行标记，用于控制音效的开始、停止、音量等。 | - |
| path | string | 音效路径。 | - |
| loopCount | int | 循环播放次数。 | 取值范围为0 - 任意正整数，默认值：0。0表示播放音效一次；1表示播放音效两次；以此类推。 |
| publish | bool | 音效是否上行。 | YES：音效在本地播放的同时，会上行至云端，因此远端用户也能听到该音效；NO：音效不会上行至云端，因此只能在本地听到该音效。默认值：NO。 |
| volume | int | 音效音量。 | 取值范围为0 - 100；默认值：100。 |




## TRTCLocalStatistics

__功能__

自己本地的音视频统计信息。




__属性列表__

| 属性 | 类型 | 字段含义 |
|-----|-----|-----|
| width | uint | 视频宽度。 |
| height | uint | 视频高度。 |
| frameRate | uint | 帧率（fps）。 |
| videoBitrate | uint | 视频发送码率（Kbps）。 |
| audioSampleRate | uint | 音频采样率（Hz）。 |
| audioBitrate | uint | 音频发送码率（Kbps）。 |
| streamType | [TRTCVideoStreamType](https://cloud.tencent.com/document/product/647/36780#trtcvideostreamtype) | 流类型（大画面 &#124、小画面 &#124或辅路画面）。 |



## TRTCRemoteStatistics

__功能__

远端成员的音视频统计信息。




__属性列表__

| 属性 | 类型 | 字段含义 |
|-----|-----|-----|
| userId | string | 用户 ID，指定是哪个用户的视频流。 |
| finalLoss | uint | 该线路的总丢包率（％）<br>该值越小越好，例如，丢包率为0表示网络很好。丢包率是该线路的 userId 从上行到服务器再到下行的总丢包率。如果 downLoss 为 0%，但是 finalLoss 不为0，说明该 userId 上行时出现了无法恢复的丢包。 |
| width | uint | 视频宽度。 |
| height | uint | 视频高度。 |
| frameRate | uint | 接收帧率（fps）。 |
| videoBitrate | uint | 视频码率（Kbps）。 |
| audioSampleRate | uint | 音频采样率（Hz）。 |
| audioBitrate | uint | 音频码率（Kbps）。 |
| streamType | [TRTCVideoStreamType](https://cloud.tencent.com/document/product/647/36780#trtcvideostreamtype) | 流类型（大画面 &#124、小画面 &#124或辅路画面）。 |



## TRTCStatistics

__功能__

统计数据。




__属性列表__

| 属性 | 类型 | 字段含义 |
|-----|-----|-----|
| upLoss | uint | C -> S 上行丢包率（％），该值越小越好，例如，丢包率为0表示网络很好， 丢包率为30%则意味着 SDK 向服务器发送的数据包中会有30%丢失在上行传输中。 |
| downLoss | uint | S -> C 下行丢包率（％），该值越小越好，例如，丢包率为0表示网络很好，丢包率为30%则意味着 SDK 向服务器发送的数据包中会有30%丢失在下行传输中。 |
| appCpu | uint | 当前 App 的 CPU 使用率（％）。 |
| systemCpu | uint | 当前系统的 CPU 使用率（％）。 |
| rtt | uint | 延迟（毫秒），指 SDK 到腾讯云服务器的一次网络往返时间，该小越好。一般低于50ms的 rtt 相对理想，而高于100ms的 rtt 会引入较大的通话延时。由于数据上下行共享一条网络连接，所以 local 和 remote 的 rtt 相同。 |
| receivedBytes | uint | 总接收字节数（包含信令和音视频）。 |
| sentBytes | uint | 总发送字节总数（包含信令和音视频）。 |
| localStatisticsArray | [TRTCLocalStatistics[]](https://cloud.tencent.com/document/product/647/36780#trtclocalstatistics) | 本地的音视频统计信息，可能有主画面、小画面以及辅路画面等多路的情况，因此参数值为一个数组。 |
| localStatisticsArraySize | uint | 数组 localStatisticsArray 的大小。 |
| remoteStatisticsArray | [TRTCRemoteStatistics[]](https://cloud.tencent.com/document/product/647/36780#trtcremotestatistics) | 远端成员的音视频统计信息，可能有主画面、小画面以及辅路画面等多路的情况，因此参数值为一个数组。 |
| remoteStatisticsArraySize | uint | 数组 remoteStatisticsArray 的大小。 |



## TRTCVideoResolution

__功能__

视频分辨率。

__介绍__

此处仅定义横屏分辨率，如需使用竖屏分辨率（例如360 × 640），需要同时指定 TRTCVideoResolutionMode 为 Portrait。

| 枚举 | 含义 |
|-----|-----|
| TRTCVideoResolution_120_120 | [C] 建议码率80kbps。 |
| TRTCVideoResolution_160_160 | [C] 建议码率100kbps。 |
| TRTCVideoResolution_270_270 | [C] 建议码率200kbps。 |
| TRTCVideoResolution_480_480 | [C] 建议码率350kbps。 |
| TRTCVideoResolution_160_120 | [C] 建议码率100kbps。 |
| TRTCVideoResolution_240_180 | [C] 建议码率150kbps。 |
| TRTCVideoResolution_280_210 | [C] 建议码率200kbps。 |
| TRTCVideoResolution_320_240 | [C] 建议码率250kbps。 |
| TRTCVideoResolution_400_300 | [C] 建议码率300kbps。 |
| TRTCVideoResolution_480_360 | [C] 建议码率400kbps。 |
| TRTCVideoResolution_640_480 | [C] 建议码率600kbps。 |
| TRTCVideoResolution_960_720 | [C] 建议码率1000kbps。 |
| TRTCVideoResolution_160_90 | [C] 建议码率150kbps。 |
| TRTCVideoResolution_256_144 | [C] 建议码率200kbps。 |
| TRTCVideoResolution_320_180 | [C] 建议码率250kbps。 |
| TRTCVideoResolution_480_270 | [C] 建议码率350kbps。 |
| TRTCVideoResolution_640_360 | [C] 建议码率550kbps。 |
| TRTCVideoResolution_960_540 | [C] 建议码率850kbps。 |
| TRTCVideoResolution_1280_720 | [C] 摄像头采集 - 建议码率1200kbps [S] 屏幕分享 - 建议码率 低清：400kbps 高清：600kbps。 |
| TRTCVideoResolution_1920_1080 | [S] 屏幕分享 - 建议码率800kbps。 |


## TRTCVideoResolutionMode

__功能__

视频分辨率模式。

__介绍__

- 横屏分辨率：TRTCVideoResolution_640_360 + TRTCVideoResolutionModeLandscape = 640 × 360
- 竖屏分辨率：TRTCVideoResolution_640_360 + TRTCVideoResolutionModePortrait = 360 × 640。

| 枚举 | 含义 |
|-----|-----|
| TRTCVideoResolutionModeLandscape | 横屏分辨率。 |
| TRTCVideoResolutionModePortrait | 竖屏分辨率。 |


## TRTCVideoStreamType

__功能__

视频流类型。

__介绍__

TRTC 内部有三种不同的音视频流，分别是：
- 主画面：最常用的一条线路，一般用来传输摄像头的视频数据。
- 小画面：跟主画面的内容相同，但是分辨率和码率更低。
- 辅流画面：一般用于屏幕分享或远程播放视频（例如老师播放视频给学生观看）。

>?
>- 如果主播的上行网络和性能比较好，则可以同时送出大小两路画面。
>- SDK 不支持单独开启小画面，小画面必须依附于主画面而存在。

| 枚举 | 含义 |
|-----|-----|
| TRTCVideoStreamTypeBig | 主画面视频流。 |
| TRTCVideoStreamTypeSmall | 小画面视频流。 |
| TRTCVideoStreamTypeSub | 辅流（屏幕分享）。 |


## TRTCQuality

__功能__

画质级别。

__介绍__

TRTC SDK 对画质定义六种不同的级别，Excellent 表示最好，Down 表示不可用。

| 枚举 | 含义 |
|-----|-----|
| TRTCQuality_Unknown | 未定义。 |
| TRTCQuality_Excellent | 最好。 |
| TRTCQuality_Good | 好。 |
| TRTCQuality_Poor | 一般。 |
| TRTCQuality_Bad | 差。 |
| TRTCQuality_Vbad | 很差。 |
| TRTCQuality_Down | 不可用。 |


## TRTCVideoFillMode

__功能__

视频画面填充模式。

__介绍__

如果画面的显示分辨率不等于画面的原始分辨率时，您需要设置画面的填充模式：
- TRTCVideoFillMode_Fill，图像铺满屏幕，超出显示视窗的视频部分将被裁剪，画面显示可能不完整。
- TRTCVideoFillMode_Fit，图像长边填满屏幕，短边区域会被填充黑色，画面的内容完整。

| 枚举 | 含义 |
|-----|-----|
| TRTCVideoFillMode_Fill | 图像铺满屏幕，超出显示视窗的视频部分将被裁剪。 |
| TRTCVideoFillMode_Fit | 图像长边填满屏幕，短边区域会被填充黑色。 |


## TRTCBeautyStyle

__功能__

美颜（磨皮）算法。

__介绍__

TRTC SDK 内置多种不同的磨皮算法，您可以选择最适合您产品定位的方案。

| 枚举 | 含义 |
|-----|-----|
| TRTCBeautyStyleSmooth | 光滑，适用于美女秀场，效果比较明显。 |
| TRTCBeautyStyleNature | 自然，磨皮算法更多地保留了面部细节，主观感受上会更加自然。 |


## TRTCAppScene

__功能__

应用场景。

__介绍__

TRTC 可用于视频会议和在线直播等多种应用场景，针对不同的应用场景，TRTC SDK 的内部会进行不同的优化配置：
- VideoCall：视频通话场景，即绝大多数时间都是两人或两人以上视频通话的场景，例如1v1在线课程辅导，1vN (N \< 8) 视频会议或者小班课堂等。
- LIVE：在线直播场景，即绝大多数时间都是一人直播，偶尔有多人视频互动的场景，例如美女秀场连麦等场景。

| 枚举 | 含义 |
|-----|-----|
| TRTCAppSceneVideoCall | 视频通话场景，内部编码器和网络协议优化侧重流畅性，降低通话延迟和卡顿率。 |
| TRTCAppSceneLIVE | 在线直播场景，内部编码器和网络协议优化侧重性能和兼容性，性能和清晰度表现更佳。 |


## TRTCRoleType

__功能__

角色，仅适用于直播场景（TRTCAppSceneLIVE）。

__介绍__

在直播场景中，多数用户仅为观众，个别用户为主播，这种角色区分有利于 TRTC 进行更好的定向优化。

- Anchor：主播，可以上行视频和音频，一个房间里最多支持20个主播同时上行音视频。
- Audience：观众，只能观看，不能上行视频和音频，一个房间里的观众人数没有上限。

| 枚举 | 含义 |
|-----|-----|
| TRTCRoleAnchor | 主播。 |
| TRTCRoleAudience | 观众。 |


## TRTCQosControlMode

__功能__

流控模式。

__介绍__

TRTC SDK 内部需要时刻根据网络情况调整内部的编解码器和网络模块，以便能够对网络的变化做出反应。 为了支持快速算法升级，SDK 内部设置了两种不同的流控模式：
- ModeServer：云端控制，默认模式，推荐选择。
- ModeClient：本地控制，用于 SDK 开发内部调试，客户请勿使用。

>?推荐您使用云端控制，当升级 Qos 算法时，您无需升级 SDK 即可体验更好的效果。


| 枚举 | 含义 |
|-----|-----|
| TRTCQosControlModeClient | 客户端控制（用于 SDK 开发内部调试，客户请勿使用）。 |
| TRTCQosControlModeServer | 云端控制 （默认）。 |


## TRTCVideoQosPreference

__功能__

画质偏好。

__介绍__

指当 TRTC SDK 在遇到弱网络环境时，您期望“保清晰”或“保流畅”：

- Smooth：弱网下保流畅。即在遭遇弱网环境时首先确保声音的流畅和优先发送，画面会变得模糊且会有较多马赛克，但可以保持流畅不卡顿。
- Clear：弱网下保清晰。即在遭遇弱网环境时，画面会尽可能保持清晰，但可能会更容易出现卡顿。

| 枚举 | 含义 |
|-----|-----|
| TRTCVideoQosPreferenceSmooth | 弱网下保流畅。 |
| TRTCVideoQosPreferenceClear | 弱网下保清晰。 |


## TRTCLogLevel

__功能__

Log 级别。

| 枚举 | 含义 |
|-----|-----|
| TRTCLogLevelNone | 不输出任何 SDK Log。 |
| TRTCLogLevelVerbose | 输出所有级别的 Log。 |
| TRTCLogLevelDebug | 输出 DEBUG，INFO，WARNING，ERROR 和 FATAL 级别的 Log。 |
| TRTCLogLevelInfo | 输出 INFO，WARNING，ERROR 和 FATAL 级别的 Log。 |
| TRTCLogLevelWarn | 只输出 WARNING，ERROR 和 FATAL 级别的 Log。 |
| TRTCLogLevelError | 只输出 ERROR 和 FATAL 级别的 Log。 |
| TRTCLogLevelFatal | 只输出 FATAL 级别的 Log。 |


## TRTCDeviceState

__功能__

设备操作。

| 枚举 | 含义 |
|-----|-----|
| TRTCDeviceStateAdd | 添加设备。 |
| TRTCDeviceStateRemove | 移除设备。 |
| TRTCDeviceStateActive | 设备已启用。 |


## TRTCDeviceType

__功能__

设备类型。

| 枚举 | 含义 |
|-----|-----|
| TRTCDeviceTypeUnknow | - |
| TRTCDeviceTypeMic | 麦克风。 |
| TRTCDeviceTypeSpeaker | 扬声器。 |
| TRTCDeviceTypeCamera | 摄像头。 |


## TRTCWaterMarkSrcType

__功能__

水印图片的源类型。

| 枚举 | 含义 |
|-----|-----|
| TRTCWaterMarkSrcTypeFile | 图片文件路径，支持 BMP、GIF、JPEG、PNG、TIFF、Exif、WMF 和 EMF 文件格式。 |
| TRTCWaterMarkSrcTypeBGRA32 | BGRA32 格式内存块。 |
| TRTCWaterMarkSrcTypeRGBA32 | RGBA32 格式内存块。 |


## TRTCTranscodingConfigMode

__功能__

混流参数配置模式。

__介绍__

目前仅支持手动配置模式，即需要指定 [TRTCTranscodingConfig](https://cloud.tencent.com/document/product/647/36780#trtctranscodingconfig) 的全部参数。

| 枚举 | 含义 |
|-----|-----|
| TRTCTranscodingConfigMode_Unknown | 未定义。 |
| TRTCTranscodingConfigMode_Manual | 手动配置混流参数。 |

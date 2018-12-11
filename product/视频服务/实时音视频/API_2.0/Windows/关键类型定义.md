<div id="trtc-doc">

## TRTCVideoEncParam
### `videoResolution`
`TRTCVideoResolution TRTCVideoEncParam::videoResolution`

视频分辨率

> __您在 TRTCVideoResolution 只能找到横屏模式的分辨率，比如： 640x360 这样的分辨率 如果想要使用竖屏分辨率，请指定 ResolutionMode 为 Portrait，比如：640x360 + Portrait = 360x640__
### `codecMode`
`TRTCVideoCodecMode TRTCVideoEncParam::codecMode`

编码器的编码模式（流畅 - 兼容）

Smooth 模式（默认）：能够获得理论上最低的卡顿率，但性能略逊于 Compatible 模式 Compatible 模式：使用最标准的视频编码模式，卡顿率高于 Smooth 模式，但性能优异，推荐在低端设备上开启 
### `videoFps`
`uint32_t TRTCVideoEncParam::videoFps`

视频采集帧率，推荐设置为 15fps 或 20fps，10fps以下会有明显的卡顿感，20fps以上则没有必要

> __很多廉价的 USB 摄像头可能并不支持 15fps 以上的采集帧率__
### `videoBitrate`
`uint32_t TRTCVideoEncParam::videoBitrate`

视频上行码率

> __推荐设置请参考 TRTCVideoResolution 定义处的注释说明__

### `TRTCVideoEncParam`
` TRTCVideoEncParam()`


## TRTCVolumeInfo
### `userId`
`TXString TRTCVolumeInfo::userId`

说话者的userId 
### `volume`
`uint32_t TRTCVolumeInfo::volume`

说话者的音量, 取值范围 0~100 

### `TRTCVolumeInfo`
` TRTCVolumeInfo()`


## TRTCQualityInfo
### `userId`
`TXString TRTCQualityInfo::userId`

用户标识 
### `quality`
`TRTCQuality TRTCQualityInfo::quality`

视频质量 

### `TRTCQualityInfo`
` TRTCQualityInfo()`


## TRTCParams
### `sdkAppId`
`uint32_t TRTCParams::sdkAppId`

应用标识 - [必填] - 腾讯视频云基于 sdkAppId 完成计费统计 
### `roomId`
`uint32_t TRTCParams::roomId`

房间号码 - [必填] - 指定房间号，在同一个房间里的用户（userId）可以彼此看到对方并进行视频通话 
### `userId`
`TXString TRTCParams::userId`

用户标识 - [必填] - 当前用户的 userid，相当于用户名 
### `userSig`
`TXString TRTCParams::userSig`

用户签名 - [必填] - 当前 userId 对应的验证签名，相当于登录密码 
### `privateMapKey`
`TXString TRTCParams::privateMapKey`

房间签名 - [非必选] - 如果您希望某个房间（roomId）只让特定的某些用户（userId）才能进入，就需要使用 privateMapKey 进行权限保护 
### `businessInfo`
`TXString TRTCParams::businessInfo`

业务数据 - [非必选] - 某些非常用的高级特性才需要用到此字段 

### `TRTCParams`
` TRTCParams()`


## TRTCVideoFrame

视频帧数据 
### `videoFormat`
`TRTCVideoFrameFormat TRTCVideoFrame::videoFormat`

视频帧的格式 
### `data`
`char* TRTCVideoFrame::data`

视频数据 
### `length`
`uint32_t TRTCVideoFrame::length`

视频数据的长度，单位是字节，对于i420而言， length = width * height * 3 / 2，对于BGRA32而言， length = width * height * 4 
### `width`
`uint32_t TRTCVideoFrame::width`

画面的宽度 
### `height`
`uint32_t TRTCVideoFrame::height`

画面的高度 
### `timestamp`
`uint64_t TRTCVideoFrame::timestamp`

时间戳，单位ms 
### `rotation`
`TRTCVideoRotation TRTCVideoFrame::rotation`

画面旋转角度 

### `TRTCVideoFrame`
` TRTCVideoFrame()`


## TRTCAudioFrame

视频帧数据 
### `audioFormat`
`TRTCAudioFrameFormat TRTCAudioFrame::audioFormat`

音频帧的格式 
### `data`
`char* TRTCAudioFrame::data`

音频数据 
### `length`
`uint32_t TRTCAudioFrame::length`

音频数据的长度 
### `sampleRate`
`uint32_t TRTCAudioFrame::sampleRate`

采样率 
### `channel`
`uint32_t TRTCAudioFrame::channel`

声道数 
### `timestamp`
`uint64_t TRTCAudioFrame::timestamp`

时间戳，单位ms 

### `TRTCAudioFrame`
` TRTCAudioFrame()`


## TRTCSpeedTestResult
### `ip`
`TXString TRTCSpeedTestResult::ip`

服务器ip地址 
### `quality`
`TRTCQuality TRTCSpeedTestResult::quality`

网络质量 
### `upLostRate`
`float TRTCSpeedTestResult::upLostRate`

上行丢包率，范围是[0,1.0] 
### `downLostRate`
`float TRTCSpeedTestResult::downLostRate`

下行丢包率，范围是[0,1.0] 
### `rtt`
`int TRTCSpeedTestResult::rtt`

延迟（毫秒）：代表 SDK 跟服务器一来一回之间所消耗的时间，-1表示都未收到服务器的回复包，说明网络非常差 

### `TRTCSpeedTestResult`
` TRTCSpeedTestResult()`



</div>
<style>
#trtc-doc h2 code, #trtc-doc h3 code, #trtc-doc h4 code { display:block; padding:3px 5px; background: #E3F3FF; color: #333; text-shadow:0px 1px #BCD2E2; }
//#trtc-doc h2{ font-size:28px !important;}
#trtc-doc table td:nth-child(1){font-family: 'Lucida Console', Monaco, monospace; font-size:14px !important; color: #4078c0}
#trtc-doc table tr:nth-child(even){background: #fafafa;}
</style>

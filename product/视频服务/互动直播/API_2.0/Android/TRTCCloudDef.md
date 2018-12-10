<div id="trtc-doc">

## TRTCCloudDef
| 值 | 类型 | 含义 |
|-----|-----|-----|
| TRTC_VIDEO_RESOLUTION_120_120 | final int | 视频分辨率，由宽 x 高组成  |
| TRTC_VIDEO_RESOLUTION_160_160 | final int | 建议码率 80kbps  |
| TRTC_VIDEO_RESOLUTION_270_270 | final int | 建议码率 100kbps  |
| TRTC_VIDEO_RESOLUTION_480_480 | final int | 建议码率 200kbps  |
| TRTC_VIDEO_RESOLUTION_160_120 | final int | 建议码率 350kbps  |
| TRTC_VIDEO_RESOLUTION_240_180 | final int | 建议码率 100kbps  |
| TRTC_VIDEO_RESOLUTION_280_210 | final int | 建议码率 150kbps  |
| TRTC_VIDEO_RESOLUTION_320_240 | final int | 建议码率 200kbps  |
| TRTC_VIDEO_RESOLUTION_400_300 | final int | 建议码率 250kbps  |
| TRTC_VIDEO_RESOLUTION_480_360 | final int | 建议码率 300kbps  |
| TRTC_VIDEO_RESOLUTION_640_480 | final int | 建议码率 400kbps  |
| TRTC_VIDEO_RESOLUTION_960_720 | final int | 建议码率 600kbps  |
| TRTC_VIDEO_RESOLUTION_160_90 | final int | 建议码率 1000kbps  |
| TRTC_VIDEO_RESOLUTION_256_144 | final int |  |
| TRTC_VIDEO_RESOLUTION_320_180 | final int |  |
| TRTC_VIDEO_RESOLUTION_480_270 | final int | 建议码率 250kbps  |
| TRTC_VIDEO_RESOLUTION_640_360 | final int | 建议码率 350kbps  |
| TRTC_VIDEO_RESOLUTION_960_540 | final int | 建议码率 550kbps  |
| TRTC_VIDEO_RESOLUTION_1280_720 | final int | 建议码率 850kbps  |
| TRTC_VIDEO_RESOLUTION_MODE_LANDSCAPE | final int | 建议码率 1200kbps  |
| TRTC_VIDEO_RESOLUTION_MODE_PORTRAIT | final int | 竖屏分辨率  |
| TRTC_VIDEO_CODEC_MODE_SMOOTH | final int | 启用流畅编码模式，该模式下视频的弱网抗性和卡顿率明显好于兼容模式  |
| TRTC_VIDEO_CODEC_MODE_COMPATIBLE | final int | 强制启用兼容编码模式，支持绝大多数硬件编码器，性能优异，但卡顿率高于流畅编码模式  |
| TRTC_VIDEO_STREAM_TYPE_BIG | final int | 大画面  |
| TRTC_VIDEO_STREAM_TYPE_SMALL | final int | 小画面  |
| TRTC_VIDEO_STREAM_TYPE_SUB | final int | 辅路画面(屏幕分享)  |
| VIDEO_QOS_CONTROL_CLIENT | final int | 客户端控制（用于调试）  |
| VIDEO_QOS_CONTROL_SERVER | final int | 云端控制（推荐线上使用）  |
| TRTC_VIDEO_QOS_PREFERENCE_SMOOTH | final int | 流畅  |
| TRTC_VIDEO_QOS_PREFERENCE_CLEAR | final int | 清晰  |
| TRTC_BEAUTY_STYLE_SMOOTH | final int | 美颜风格  |
| TRTC_BEAUTY_STYLE_NATURE | final int |  |
| TRTC_VIDEO_RENDER_MODE_FILL | final int | 视频画面全屏铺满:将图像等比例铺满整个屏幕,多余部分裁剪掉,此模式下画面不留黑边  |
| TRTC_VIDEO_RENDER_MODE_FIT | final int | 视频画面自适应屏幕:将图像等比例缩放,缩放后的宽和高都不会超过显示区域,居中显示,可能会留有黑边  |
| TRTC_VIDEO_ROTATION_0 | final int | 视频旋转角度  |
| TRTC_VIDEO_ROTATION_90 | final int |  |
| TRTC_VIDEO_ROTATION_180 | final int |  |
| TRTC_VIDEO_ROTATION_270 | final int |  |
| TRTC_GSENSOR_MODE_DISABLE | final int | 关闭重力感应  |
| TRTC_GSENSOR_MODE_UIAUTOLAYOUT | final int | 开启重力感应（适用于UI开启了屏幕旋转自动布局的场景）  |
| TRTC_GSENSOR_MODE_UIFIXLAYOUT | final int | 开启重力感应（适用于UI关闭了屏幕旋转自动布局的场景）  |
| TRTC_VIDEO_FRAME_FORMAT_BGRA32 | final int | 视频帧的格式  |
| TRTC_VIDEO_FRAME_FORMAT_I420 | final int |  |
| TRTC_AUDIO_ROUTE_SPEAKER | final int | 扬声器播放  |
| TRTC_AUDIO_ROUTE_EARPIECE | final int | 听筒播放  |
| TRTC_REVERB_TYPE_0 | final int | 混响类型  |
| TRTC_REVERB_TYPE_1 | final int |  |
| TRTC_REVERB_TYPE_2 | final int |  |
| TRTC_REVERB_TYPE_3 | final int |  |
| TRTC_REVERB_TYPE_4 | final int |  |
| TRTC_REVERB_TYPE_5 | final int |  |
| TRTC_REVERB_TYPE_6 | final int |  |
| TRTC_REVERB_TYPE_7 | final int |  |
| TRTC_VOICE_CHANGER_TYPE_0 | final int | 变声类型  |
| TRTC_VOICE_CHANGER_TYPE_1 | final int |  |
| TRTC_VOICE_CHANGER_TYPE_2 | final int |  |
| TRTC_VOICE_CHANGER_TYPE_3 | final int |  |
| TRTC_VOICE_CHANGER_TYPE_4 | final int |  |
| TRTC_VOICE_CHANGER_TYPE_5 | final int |  |
| TRTC_VOICE_CHANGER_TYPE_6 | final int |  |
| TRTC_VOICE_CHANGER_TYPE_7 | final int |  |
| TRTC_VOICE_CHANGER_TYPE_8 | final int |  |
| TRTC_VOICE_CHANGER_TYPE_9 | final int |  |
| TRTC_VOICE_CHANGER_TYPE_10 | final int |  |
| TRTC_VOICE_CHANGER_TYPE_11 | final int |  |
| TRTC_AUDIO_FRAME_FORMAT_PCM | final int | 音频帧的格式  |
| TRTC_DEBUG_VIEW_LEVEL_GONE | final int | 界面不显示log  |
| TRTC_DEBUG_VIEW_LEVEL_STATUS | final int | 界面上半部分显示状态log  |
| TRTC_DEBUG_VIEW_LEVEL_ALL | final int | 界面上半部分显示状态log，下半部分显示关键事件  |
| TRTC_LOG_LEVEL_VERBOSE | final int | 输出所有级别的log  |
| TRTC_LOG_LEVEL_DEBUG | final int | 输出 DEBUG，INFO，WARNING，ERROR 和 FATAL 级别的log  |
| TRTC_LOG_LEVEL_INFO0 | final int | 输出 INFO，WARNNING，ERROR 和 FATAL 级别的log  |
| TRTC_LOG_LEVEL_WARN | final int | 输出WARNNING，ERROR 和 FATAL 级别的log  |
| TRTC_LOG_LEVEL_ERROR | final int | 只输出ERROR 和 FATAL 级别的log  |
| TRTC_LOG_LEVEL_FATAL | final int | 只输出 FATAL 级别的log  |
| TRTC_LOG_LEVEL_NULLL | final int | 不输出任何sdk log  |
| TRTC_QUALITY_UNKNOWN | final int | 网络质量常量定义  |
| TRTC_QUALITY_Excellent | final int |  |
| TRTC_QUALITY_Good | final int |  |
| TRTC_QUALITY_Poor | final int |  |
| TRTC_QUALITY_Bad | final int |  |
| TRTC_QUALITY_Vbad | final int |  |
| TRTC_QUALITY_Down | final int |  |



## TRTCVideoFrame

视频帧数据 
### `videoFormat`
`int com.tencent.trtc.TRTCCloudDef.TRTCVideoFrame.videoFormat`

视频帧的格式 
### `textureId`
`int com.tencent.trtc.TRTCCloudDef.TRTCVideoFrame.textureId`

视频纹理 
### `data`
`byte [] com.tencent.trtc.TRTCCloudDef.TRTCVideoFrame.data`

视频数据 
### `width`
`int com.tencent.trtc.TRTCCloudDef.TRTCVideoFrame.width`

画面的宽度 
### `height`
`int com.tencent.trtc.TRTCCloudDef.TRTCVideoFrame.height`

画面的高度 
### `timestamp`
`long com.tencent.trtc.TRTCCloudDef.TRTCVideoFrame.timestamp`

时间戳 
### `rotation`
`int com.tencent.trtc.TRTCCloudDef.TRTCVideoFrame.rotation`

画面旋转角度 

## TRTCAudioFrame

音频帧数据 
### `audioFormat`
`int com.tencent.trtc.TRTCCloudDef.TRTCAudioFrame.audioFormat`

音频帧的格式 
### `data`
`byte [] com.tencent.trtc.TRTCCloudDef.TRTCAudioFrame.data`

音频数据 
### `sampleRate`
`int com.tencent.trtc.TRTCCloudDef.TRTCAudioFrame.sampleRate`

采样率 
### `channel`
`int com.tencent.trtc.TRTCCloudDef.TRTCAudioFrame.channel`

声道数 
### `timestamp`
`long com.tencent.trtc.TRTCCloudDef.TRTCAudioFrame.timestamp`

时间戳 

## TRTCQuality

网络质量 
### `userId`
`String com.tencent.trtc.TRTCCloudDef.TRTCQuality.userId`

用户id 
### `quality`
`int com.tencent.trtc.TRTCCloudDef.TRTCQuality.quality`

网络质量 

## TRTCParams

进房参数 
### `sdkAppId`
`int com.tencent.trtc.TRTCCloudDef.TRTCParams.sdkAppId`

应用标识 [必填] 腾讯视频云基于 sdkAppId 完成计费统计 
### `userId`
`String com.tencent.trtc.TRTCCloudDef.TRTCParams.userId`

用户标识 [必填] 当前用户的 userid，相当于用户名 
### `userSig`
`String com.tencent.trtc.TRTCCloudDef.TRTCParams.userSig`

用户签名 [必填] 当前 userId 对应的验证签名，相当于登录密码 
### `roomId`
`int com.tencent.trtc.TRTCCloudDef.TRTCParams.roomId`

房间号码 [必填] 指定房间号，在同一个房间里的用户（userId）可以彼此看到对方并进行视频通话 
### `privateMapKey`
`String com.tencent.trtc.TRTCCloudDef.TRTCParams.privateMapKey`

房间签名 [非必选] 如果您希望某个房间（roomId）只让特定的某些用户（userId）才能进入，就需要使用 privateMapKey 进行权限保护 
### `businessInfo`
`String com.tencent.trtc.TRTCCloudDef.TRTCParams.businessInfo`

业务数据 [非必选] 某些非常用的高级特性才需要用到此字段 

### `TRTCParams`
` TRTCParams(int sdkAppId, String userId, String userSig, int roomId, String privateMapKey, String businessInfo)`


## TRTCVideoEncParam

编码参数 
### `videoResolution`
`int com.tencent.trtc.TRTCCloudDef.TRTCVideoEncParam.videoResolution`

视频分辨率

> __您在 TRTCVideoResolution 只能找到横屏模式的分辨率，比如： 640x360 这样的分辨率 如果想要使用竖屏分辨率，请指定 ResolutionMode 为 Portrait，比如：640x360 + Portrait = 360x640__
### `videoResolutionMode`
`int com.tencent.trtc.TRTCCloudDef.TRTCVideoEncParam.videoResolutionMode`

分辨率模式（横屏分辨率 - 竖屏分辨率）

> __如果 videoResolution 指定分辨率 640x360，resMode 指定模式为 Portrait，则最终编码出的分辨率为 360x640__
### `codecMode`
`int com.tencent.trtc.TRTCCloudDef.TRTCVideoEncParam.codecMode`

编码器的编码模式（流畅 - 兼容）

Smooth 模式（默认）：能够获得理论上最低的卡顿率，但性能略逊于 Compatible 模式 Compatible 模式：使用最标准的视频编码模式，卡顿率高于 Smooth 模式，但性能优异，推荐在低端设备上开启 
### `videoFps`
`int com.tencent.trtc.TRTCCloudDef.TRTCVideoEncParam.videoFps`

视频采集帧率，推荐设置为 15fps 或 20fps，10fps以下会有明显的卡顿感，20fps以上则没有必要

> __很多 Android 手机的前置摄像头并不支持 15fps 以上的采集帧率 部分过于突出美颜功能的 Android 手机前置摄像头的采集帧率可能低于 10fps__
### `videoBitrate`
`int com.tencent.trtc.TRTCCloudDef.TRTCVideoEncParam.videoBitrate`

视频上行码率

> __推荐设置请参考 TRTCVideoResolution 定义处的注释说明__

## TRTCVolumeInfo

音量大小 
### `userId`
`String com.tencent.trtc.TRTCCloudDef.TRTCVolumeInfo.userId`

说话者的userId, 空则为自己 
### `volume`
`int com.tencent.trtc.TRTCCloudDef.TRTCVolumeInfo.volume`

说话者的音量, 取值范围 0~100 

## TRTCSpeedTestResult

网络测速结果 
### `ip`
`String com.tencent.trtc.TRTCCloudDef.TRTCSpeedTestResult.ip`

服务器ip地址 
### `quality`
`int com.tencent.trtc.TRTCCloudDef.TRTCSpeedTestResult.quality`

网络质量 
### `upLostRate`
`float com.tencent.trtc.TRTCCloudDef.TRTCSpeedTestResult.upLostRate`

上行丢包率，范围是[0,1.0] 
### `downLostRate`
`float com.tencent.trtc.TRTCCloudDef.TRTCSpeedTestResult.downLostRate`

下行丢包率，范围是[0,1.0] 
### `rtt`
`int com.tencent.trtc.TRTCCloudDef.TRTCSpeedTestResult.rtt`

延迟（毫秒）：代表 SDK 跟服务器一来一回之间所消耗的时间，这个值越小越好 


</div>
<style>
#trtc-doc h2 code, #trtc-doc h3 code, #trtc-doc h4 code { display:block; padding:3px 5px; background: #E3F3FF; color: #333; text-shadow:0px 1px #BCD2E2; }
//#trtc-doc h2{ font-size:28px !important;}
#trtc-doc table td:nth-child(1){font-family: 'Lucida Console', Monaco, monospace; font-size:14px !important; color: #4078c0}
#trtc-doc table tr:nth-child(even){background: #fafafa;}
</style>

<div id="trtc-doc">

## TRTCParams
### `sdkAppId`
`@property (assign) UInt32 sdkAppId;`

应用标识 [必填] 腾讯视频云基于 sdkAppId 完成计费统计 
### `userId`
`@property (strong) NSString *_Nonnull userId;`

用户标识 [必填] 当前用户的 userid，相当于用户名 
### `userSig`
`@property (strong) NSString *_Nonnull userSig;`

用户签名 [必填] 当前 userId 对应的验证签名，相当于登录密码 
### `roomId`
`@property (assign) UInt32 roomId;`

房间号码 [必填] 指定房间号，在同一个房间里的用户（userId）可以彼此看到对方并进行视频通话 
### `privateMapKey`
`@property (strong) NSString *_Nonnull privateMapKey;`

房间签名 [非必选] 如果您希望某个房间（roomId）只让特定的某些用户（userId）才能进入，就需要使用 privateMapKey 进行权限保护 
### `bussInfo`
`@property (strong) NSString *_Nonnull bussInfo;`

业务数据 [非必选] 某些非常用的高级特性才需要用到此字段 

## TRTCVideoEncParam
### `videoResolution`
`@property (assign) TRTCVideoResolution videoResolution;`

视频分辨率

> __您在 TRTCVideoResolution 只能找到横屏模式的分辨率，比如： 640x360 这样的分辨率 如果想要使用竖屏分辨率，请指定 ResolutionMode 为 Portrait，比如：640x360 + Portrait = 360x640__
### `resMode`
`@property (assign) TRTCVideoResolutionMode resMode;`

分辨率模式（横屏分辨率 - 竖屏分辨率）

> __如果 videoResolution 指定分辨率 640x360，resMode 指定模式为 Portrait，则最终编码出的分辨率为 360x640__
### `codecMode`
`@property (assign) TRTCVideoCodecMode codecMode;`

编码器的编码模式（流畅 - 兼容）

Smooth 模式（默认）：能够获得理论上最低的卡顿率，但性能略逊于 Compatible 模式 Compatible 模式：使用最标准的视频编码模式，卡顿率高于 Smooth 模式，但性能优异，推荐在低端设备上开启 
### `videoFps`
`@property (assign) int videoFps;`

视频采集帧率，推荐设置为 15fps 或 20fps，10fps以下会有明显的卡顿感，20fps以上则没有必要

> __很多 Android 手机的前置摄像头并不支持 15fps 以上的采集帧率 部分过于突出美颜功能的 Android 手机前置摄像头的采集帧率可能低于 10fps__
### `videoBitrate`
`@property (assign) int videoBitrate;`

视频上行码率

> __推荐设置请参考 TRTCVideoResolution 定义处的注释说明__

## TRTCVolumeInfo
### `userId`
`@property (strong) NSString * userId;`

说话者的userId, nil为自己 
### `volume`
`@property (assign) NSUInteger volume;`

说话者的音量, 取值范围 0~100 

## TRTCQualityInfo
### `userId`
`@property (copy) NSString * userId;`

用户ID 
### `quality`
`@property (assign) TRTCQuality quality;`

视频质量 

## TRTCMediaDeviceInfo
### `type`
`@property (assign) TRTCMediaDeviceType type;`

设备类型 
### `deviceId`
`@property (copy) NSString * deviceId;`

设备ID 
### `deviceName`
`@property (copy) NSString * deviceName;`

设备名称 

## TRTCSpeedTestResult
### `ip`
`@property (strong) NSString * ip;`

服务器ip地址 
### `quality`
`@property (assign) TRTCQuality quality;`

网络质量 
### `upLostRate`
`@property (assign) float upLostRate;`

上行丢包率，范围是[0,1.0] 
### `downLostRate`
`@property (assign) float downLostRate;`

下行丢包率，范围是[0,1.0] 
### `rtt`
`@property (assign) uint32_t rtt;`

延迟（毫秒）：代表 SDK 跟服务器一来一回之间所消耗的时间，这个值越小越好 


</div>
<style>
#trtc-doc h2 code, #trtc-doc h3 code, #trtc-doc h4 code { display:block; padding:3px 5px; background: #E3F3FF; color: #333; text-shadow:0px 1px #BCD2E2; }
//#trtc-doc h2{ font-size:28px !important;}
#trtc-doc table td:nth-child(1){font-family: 'Lucida Console', Monaco, monospace; font-size:14px !important; color: #4078c0}
#trtc-doc table tr:nth-child(even){background: #fafafa;}
</style>

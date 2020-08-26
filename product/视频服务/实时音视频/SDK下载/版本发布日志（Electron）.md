## Version 7.6.300 @ 2020.8.26

**新增**
- Windows & Mac：新增 [setCurrentMicDeviceMute](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setCurrentMicDeviceMute) 、[getCurrentMicDeviceMute](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getCurrentMicDeviceMute)、[setCurrentSpeakerDeviceMute](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setCurrentSpeakerDeviceMute)、[getCurrentSpeakerDeviceMute](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#getCurrentSpeakerDeviceMute) 用于控制 PC 的麦克风和扬声器。

## Version 7.5.210 @ 2020.8.11

**改进**
- Windows & Mac：修复SDK回调乱序问题 
- Windows & Mac：解决切换渲染模式导致崩溃的问题 
- Windows & Mac：修复某些分辨率渲染失败的问题 
- Windows & Mac：其他bug修复

## Version 7.4.204 @ 2020.7.1

**改进**
- Windows：优化 Windows 平台的回声抵消（AEC）效果。
- Windows：增强 Windows 平台的摄像头采集的设备兼容性。
- Windows：增强 Windows 平台的音频设备（麦克风和扬声器）的设备兼容性。
- Windows：修复 Windows 版本 onPlayAudioFrame 回调的 UserID 不正确的问题。
- Windows：64 位支持系统混音

## Version 7.2.174 @ 2020.4.20

**改进**
- Mac：修复 Mac 偶现本地自定义渲染分辨率不一致问题。
- Windows：优化 Windows 端 getCurrentCameraDevice 逻辑，在未使用摄像头时，返回第一个设备作为默认设备。
- Windows：修复高亮窗口在屏幕分享时显示为灰屏的问题。
- Windows：修复 Win10 系统获取屏幕分享缩略图偶现卡死问题。
- Windows & Mac：修复切换角色时，自定义流 ID 偶现未及时生效的问题。
- Windows & Mac：修复屏幕分享设置编码参数不生效的问题。
- Windows：修复 Windows 端屏幕分享后，webrtc 要很久才能看到画面的问题。

## Version 7.1.157 @ 2020.4.2

**新增**

支持使用 [主路](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCVideoStreamType) 进行 [屏幕分享](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#startScreenCapture)。

**改进**
- 优化 [混流预设模版](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/global.html#TRTCTranscodingConfigMode) 易用性。
- 优化 [混流](https://trtc-1252463788.file.myqcloud.com/electron_sdk/docs/TRTCCloud.html#setMixTranscodingConfig)，提升成功率。
- 优化 Windows 屏幕分享。


## Version 7.0.149 @ 2020.3.19

**新增**

[trtc.d.ts](https://cloud.tencent.com/document/product/647/38551#.E5.88.9B.E5.BB.BA-trtc-.E5.AF.B9.E8.B1.A1) 文件，方便使用 typescript 的开发者。

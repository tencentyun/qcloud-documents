## 概述
音视频通信 SDK 包含三大模块：
1. AVSDK
2. BugReport
3. IMSDK

**特别注意：**这三大模块的组件，在编译时存在一定的依赖，在运行时互有调用，因此 App 开发者在更新替换 SDK 的时候，务必要保证下文清单中，所有文件的完整性。如果仅局部地替换个别文件，又或者仅替换某一模块的文件，很可能会引入各种无法预料的异常。

## AVSDK 文件清单
AVSDK 实现了音视频通信的核心能力。AVSDK 的文件可以分成三大类：
1. 头文件
2. Debug 版文件
3. Release 版文件

### 头文件
- 文件位置：%root%\libs\include
*%root%表示腾讯云官网提供的 SDK 包的根目录*
- 文件清单：
1.av_audio_ctrl.h
2.av_common.h
3.av_context.h
4.av_device.h
5.av_device_base.h
6.av_device_mgr.h
7.av_device_test.h
8.av_endpoint.h
9.av_error.h
10.av_export.h
11.av_room.h
12.av_room_multi.h
13.av_sdk.h
14.av_video_ctrl.h
15.basictypes.h
16.build_config.h

### Debug 版文件
- 文件位置：%root%\libs\win\debug
- 核心组件：
1.qavsdk.dll
2.qavsdk.lib
3.xPlatform.dll
- 视频组件：
1.AdvVideoDev.dll
2.IntelDec.dll
3.IntelEnc.dll
4.IntelUtil.dll
5.TcVpxDec.dll
6.TcVpxEnc.dll
7.VP8.dll
- 音频组件：
1.QQAudioHook.dll
2.QQAudioHookService.dll
3.TRAE.dll

### Release 版文件
- 文件位置：%root%\libs\win\release
- 核心组件：
1.qavsdk.dll
2.qavsdk.lib
3.xPlatform.dll
- 视频组件：
1.AdvVideoDev.dll
2.IntelDec.dll
3.IntelEnc.dll
4.IntelUtil.dll
5.TcVpxDec.dll
6.TcVpxEnc.dll
7.VP8.dll
- 音频组件：
1.QQAudioHook.dll
2.QQAudioHookService.dll
3.TRAE.dll

## BugReport 文件清单
BugReport 支持 Windows 平台的 Crash 监控，能够发现并上报 Crash 现场信息，为定位和解决 Crash 提供更多线索。文件清单如下：
### 头文件
- 文件位置：%root%\libs\include\crash_report.h

### Debug 版文件
- 文件位置：%root%\libs\win\debug
- 文件清单：
1.bugreport.exe
2.libeay32.dll
3.tinyxml.dll

### Release 版文件
- 文件位置：%root%\libs\win\release
- 文件清单：
1.bugreport.exe
2.libeay32.dll
3.tinyxml.dll

## IMSDK 文件清单
IMSDK 实现了音视频通信中要用到的第三方账号体系接入，账号登录鉴权等能力。 文件清单如下：
### 头文件
- 文件位置：%root%\libs\include\timsdk
- 文件清单：
1.tim.h
2.tim_comm.h
3.tim_comm_c.h
4.tim_conv.h
5.tim_int.h
6.tim_msg.h

### Debug 版文件
- 文件位置：%root%\libs\win\debug
- 文件清单：
1.libtim.dll
2.libtim.lib

### Release 版文件
- 文件位置：%root%\libs\win\release
- 文件清单：
1.libtim.dll
2.libtim.lib
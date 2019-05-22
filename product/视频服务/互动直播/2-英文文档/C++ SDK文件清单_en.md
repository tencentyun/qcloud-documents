## Overview
Audio/video messaging SDK contains three modules:
1. AVSDK
2. BugReport
3. IMSDK

**Note:** The components of the three modules call each other when running due to a certain dependency among them during compilation. This means that App develops should ensure the integrity of all the files in the list below when updating or replacing SDK. Only replacing individual files or the files of a module may introduce various unpredictable exceptions.

## AVSDK File List
AVSDK offers core capabilities of audio/video messaging. AVSDK files are divided into three categories:
1. Header files
2. "Debug" files
3. "Release" files

### 1. Header files
- File location: %root%\libs\include
*%root% is the root directory of the SDK provided by Tencent Cloud official website*
- File list:
(1) av_audio_ctrl.h
(2) av_common.h
(3) av_context.h
(4) av_device.h
(5) av_device_base.h
(6) av_device_mgr.h
(7) av_device_test.h
(8) av_endpoint.h
(9) av_error.h
(10) av_export.h
(11) av_room.h
(12) av_room_multi.h
(13) av_sdk.h
(14) av_video_ctrl.h
(15) basictypes.h
(16) build_config.h

### 2. "Debug" files
- File location: %root%\libs\win\debug
- Key components:
(1) qavsdk.dll
(2) qavsdk.lib
(3) xPlatform.dll
- Video components:
(1) AdvVideoDev.dll
(2) IntelDec.dll
(3) IntelEnc.dll
(4) IntelUtil.dll
(5) TcVpxDec.dll
(6) TcVpxEnc.dll
(7) VP8.dll
- Audio components:
(1) QQAudioHook.dll
(2) QQAudioHookService.dll
(3) TRAE.dll

### 3. "Release" files
- File location: %root%\libs\win\release
- Key components:
(1) qavsdk.dll
(2) qavsdk.lib
(3) xPlatform.dll
- Video components:
(1) AdvVideoDev.dll
(2) IntelDec.dll
(3) IntelEnc.dll
(4) IntelUtil.dll
(5) TcVpxDec.dll
(6) TcVpxEnc.dll
(7) VP8.dll
- Audio components:
(1) QQAudioHook.dll
(2) QQAudioHookService.dll
(3) TRAE.dll

## BugReport File List
BugReport supports Crash monitoring on Windows platform, which can identify and report real-time information about Crash, providing more clues for locating and resolving Crash. The file list is as follows:
### 1. Header files
- File location: %root%\libs\include\crash_report.h

### 2. "Debug" files
- File location: %root%\libs\win\debug
- File list:
(1) bugreport.exe
(2) libeay32.dll
(3) tinyxml.dll

### 3. "Release" files
- File location: %root%\libs\win\release
- File List:
(1) bugreport.exe
(2) libeay32.dll
(3) tinyxml.dll

## IMSDK File List
IMSDK offers the capabilities applied in audio/video messaging such as accessing third-party account system and authenticating login account. The file list is as follows:
### 1. Header files
- File location: %root%\libs\include\timsdk
- File List:
(1) tim.h
(2) tim_comm.h
(3) tim_comm_c.h
(4) tim_conv.h
(5) tim_int.h
(6) tim_msg.h

### 2. "Debug" files
- File location: %root%\libs\win\debug
- File list:
(1) libtim.dll
(2) libtim.lib

### 3. "Release" files
- File location: %root%\libs\win\release
- File list:
(1) libtim.dll
(2) libtim.lib

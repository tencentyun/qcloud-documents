此页面仅更新播放器 SDK 的版本历史，如您想了解全功能版 SDK 的版本历史，请参见 [全功能版 SDK 版本历史](https://cloud.tencent.com/document/product/1449/76109)。

> ? 全功能版 SDK 是多个基础 SDK 的集合，它包含了直播、短视频、音视频通话（TRTC）和播放器等子产品 SDK 的功能模块。


## 播放器 SDK

### 播放器 SDK 10.8 @ 2022.10.27
**功能优化:**
- Android&iOS：循环播放单轮结束增加 VOD_PLAY_EVT_LOOP_ONCE_COMPLETE 事件
-  Android：合规优化启动时调用2次：NetworkInfo.getExtraInfo 问题
 
**缺陷修复**: 
- Android&iOS：修复特殊场景导致私有加密视频播放失败问题
- Andoird&iOS：修复部分视频通过 gzip 传输播放失败问题
- Andoird&iOS：修复播放结束后进度条时长不匹配问题
- iOS：修复 appid&fileid 播放 v2 协议取视频源地址错误问题


### 播放器 SDK 10.7 @ 2022.09.20

**功能优化:**

- Android&iOS：点播播放 startPlay 接口变更为 startVodPlay
- Android&iOS： 直播播放 startPlay 接口变更为 startLivePlay
- iOS：修复长时间退到后台，返回播放器，无法继续播放的问题
- Android： 修复低版本 Android 系统部分视频播放失败问题

### 播放器 SDK 10.6 @ 2022.08.31

**功能优化:** 

- Android&iOS：fileid 播放方式新增雪碧图、URL 等信息回调
- Android&iOS：包体大小优化

**缺陷修复:** 

-  iOS：修复部分场景下私有加密视频离线下载播放失败问题

### 播放器 SDK 10.5 @ 2022.08.12
**缺陷修复**: 
- Android&iOS：修复播放失败不带视频格式后缀短链异常

### 播放器 SDK 10.4.0 @ 2022.07.21

**功能优化:** 
Android&iOS：HLS 直播支持自适应播放。

**缺陷修复:** 
- Android：修复 onNetStatus 和进度回调间隔异常 。
- Android：修复播放器没有调用 setConfig 引起的空指针异常。
- iOS：修复部分场景下重播卡顿问题。


### 播放器 SDK 10.3.0 @ 2022.07.06
**新功能：** 
iOS：视频播放支持画中画模式。

**缺陷修复：** 
- Android：修复硬解后台连续播放视频列表会中断问题。
- Android&iOS：修复 Seek 完成事件不回调问题。

### 播放器 SDK 10.2.0 @ 2022.06.23
**功能优化：** 
Android&iOS：优化播放过程中回调 cachedBytes、IP 地址等参数。

**缺陷修复：** 
- Android&iOS：修复硬解播放H265格式视频失败问题。
- Android&iOS：修复播放 HLS 直播异常。
- iOS：修复某些场景下获取 supportedBitrates 异常。

### 播放器 SDK 10.1.0 @ 2022.05.31
- Android&iOS： 视频超分效果优化
- Android&iOS：修复嵌套 m3u8 refer header 子流传递问题
- iOS： 解决与第三方 SDK ffmpeg 冲突问题
- Android&iOS： 优化播放器内核性能

### 播放器 SDK 9.5.29040 @ 2022.05.13
Android&iOS：修复播放带封面 mp3 失败的问题。

### 播放器 SDK 9.5.29036 @ 2022.05.06
Android：修复 SurfaceView 重复 Add 和 Remove 导致黑屏问题。

### 播放器 SDK Android 9.5.29035, iOS 9.5.29036 @ 2022.04.28
- Android&iOS：新增视频预下载功能。
- Android&iOS：支持 onPrepared 事件之前播放器暂停（Pause）能力。
- Android&iOS：支持 Pause 状态下切码流继续保持 Pause 状态。
- Android&iOS：优化播放性能。

### 播放器 SDK 9.5.29016 @ 2022.03.30
- Android&iOS： 支持缓存流量精细化控制，预加载 buffer 和启播 buffer 可以分开控制。
- Android&iOS： 支持启播前指定偏好分辨率播放，找最适合的分辨率启播。

### 播放器 SDK 9.5.29015 @ 2022.03.25
Android：优化播放性能。

### 播放器 SDK 9.5.29011 @ 2022.03.10
iOS： 优化版本适配问题。

### 播放器 SDK 9.5.29009  @ 2022.03.03
- Android&iOS：支持终端极速高清，可通过插件接入。
- Android&iOS：优化视频私有加密。
- Android&iOS：优化精准 seek 到帧。
- Android&iOS：HLS 支持 EXT-X-DISCONTINUITY 标签。
- Android&iOS：优化播放器内核， 提升性能。
- Android&iOS：播放器组件提供沉浸式短视频、Feed 视频流、视频试看、视频封面和视频动态水印等功能 Demo。

### 播放器 SDK 9.5 @ 2022.01.11
- Android：修复视频列表中任意视频播放到最后连续切换两次清晰度会重播的问题。
- Android&iOS：修复不同时间点回看播放时间点不准的问题。

### 播放器 SDK 9.4 @ 2021.12.09
- iOS：修复切换 HLS 码流出现黑屏的问题。
- iOS：修复点播播放器在播放视频的时候频繁 seek 会有杂音的问题。
- Android：修复防盗链雪碧图获取失败的问题。
- Android：修复点播播放器离线下载 HLS 偶现报错的问题。
- Android&iOS：修复播放器精准 seek 不准的问题。

### 播放器 SDK 9.3 @ 2021.11.04
- Android&iOS：修复点播播放器开启预加载，调用 startPlay 后听到声音异常的问题。
- Android&iOS：修复点播播放器硬解播放 hevc 视频时回调分辨率为0的问题。

### 播放器 SDK 9.2 @ 2021.09.26
- Android&iOS：点播放器支持 HLS 加固加密播放。
- Android：修复播放特殊字符的地址失败的问题。
- Android：修复设备频繁切换前后台，偶现有声无画的问题。

### 播放器 SDK 9.1 @ 2021.09.02
- Android：修复 Android5.x 特定设备出现播放崩溃的问题。
- Android：优化直播播放特定条件下视频画面过曝的问题。

### 播放器 SDK 9.0 @ 2021.08.06
- iOS：修复在开启 smoothSwitchBitrate 后，反复切换清晰度导致的 Crash 问题。
- iOS：优化点播播放器在网络恢复后播放进度异常的问题。

### 播放器 SDK 8.9 @ 2021.07.15
Android：修复点播播放器断网后的回调事件逻辑错误的问题。

### 播放器 SDK 8.8 @ 2021.06.21
- iOS：修复点播播放器启动停止播放多次触发内存泄漏的问题。
- Android：修复在 Android 11上播放 HLS 文件的报错问题。
- Android：修复播放器播放默认直播卡顿，其他直播偶现音画加速的问题。
- Android&iOS：修复 VodPlayer 播放特定视频 seek 慢的问题。
- Android&iOS：修复点播暂停播放后，调 seek 设置进度，画面显示慢的问题。

## 播放器 Adapter
### 播放器 Adapter 1.2.0 @ 2022.03.10
Android&iOS：支持通过 FileId 播放自适应码流、转码和原始视频。

### 播放器 Adapter 发布 @ 2021.07.22
首次发布 iOS & Android 播放器组件 Adapter。


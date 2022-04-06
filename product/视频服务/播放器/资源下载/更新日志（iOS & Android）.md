## 播放器 SDK
### 超级播放器 9.5.29016 @ 2022.03.30
- Android&iOS： 支持缓存流量精细化控制，预加载 buffer 和启播 buffer 可以分开控制。
- Android&iOS： 支持启播前指定偏好分辨率播放，找最适合的分辨率启播。

### 播放器 SDK 9.5.29015 @ 2022.03.25
- Android：优化播放性能。

### 播放器 SDK 9.5.29011 @ 2022.03.10
- iOS： 优化版本适配问题。

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

## 超级播放器 Adapter
### 超级播放器 Adapter 1.2.0 @ 2022.03.10
- Android&iOS：支持通过 FileId 播放自适应码流、转码和原始视频。

### 超级播放器 Adapter 发布 @ 2021.07.22
- 首次发布 iOS & Android 超级播放器 Adapter。


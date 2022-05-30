本文档主要介绍如何使用屏幕分享，目前一个 TRTC 音视频房间只能有一路屏幕分享。

Windows 平台下的屏幕分享支持主路分享和辅路分享两种方案：

- **辅路分享**
在 TRTC 中，我们可以单独为屏幕分享开启一路上行的视频流，并称之为“辅路（**substream**）”。辅路分享即主播同时上行摄像头画面和屏幕画面两路画面。这是腾讯会议的使用方案，您可以在调用 `startScreenCapture` 接口时，通过将 `TRTCVideoStreamType` 参数指定为 `TRTCVideoStreamTypeSub ` 来启用该模式。

- **主路分享**
在 TRTC 中，我们一般把摄像头走的通道叫做“主路（**bigstream**）”，主路分享即用摄像头通道分享屏幕。该模式下，主播只有一路上行视频流，要么上行摄像头画面，要么上行屏幕画面，两者是互斥的。您可以在调用 `startScreenCapture` 接口时，通过将 `TRTCVideoStreamType` 参数指定为 `TRTCVideoStreamTypeBig` 来启用该模式。

## 依赖的 API

| API 功能 | C++ 版本 |  C# 版本 | Electron 版本 | 
|---------|---------|---------|---------|
|选择分享目标| [selectScreenCaptureTarget](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a9d16af81b2ea2db7b91a8346add13393) | [selectScreenCaptureTarget](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a2aabe079ed38fb5122be988434a81a92) | [selectScreenCaptureTarget](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#selectScreenCaptureTarget) |
|开始屏幕分享| [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a984f461eebe77819f40c4129fc5a71bb) | [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#adde6382876b0afab78bab89e8be8e254) | [startScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#startScreenCapture) |
|暂停屏幕分享| [pauseScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a0dcd89ed2e23706239db98b55dd806d4) | [pauseScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a448e432a91c092f80421d377425fb1bb) | [pauseScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#pauseScreenCapture) |
|恢复屏幕分享| [resumeScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a9dc10db068b9d8c6a0fcb8b085359f33) | [resumeScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ad1fc32927622168e9b3cbb3f70043450) | [resumeScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#resumeScreenCapture)|
|结束屏幕分享| [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#a0e09090fe4281c0e78d8eb38496a8ed0) | [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ad02093be5c603f66f356978169946a18) | [stopScreenCapture](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#stopScreenCapture) |


## 获取分享目标
通过 `getScreenCaptureSources` 可以枚举可共享的窗口列表，列表通过出参 sourceInfoList 返回。
>? Windows 里的桌面屏幕也是一个窗口，叫桌面窗口（Desktop），有两台显示器时，每一台显示器都有一个对应的桌面窗口。所以，getScreenCaptureSources 返回的窗口列表里也会有 Desktop 窗口。

根据获取到的窗口信息，您可以实现一个简单的列表页面，将可以分享的目标罗列出来供用户选择，如下图：

![](https://qcloudimg.tencent-cloud.cn/raw/a29a0f4beb6862293391e1f3c004da4d.png)

## 开始屏幕分享

 - 选取分享目标后，使用 `startScreenCapture` 接口可以启动屏幕分享。
 - 分享过程中，您依然可以通过调用 `selectScreenCaptureTarget` 更换分享目标。
 - `pauseScreenCapture` 和  `stopScreenCapture` 的区别在于 pause 会停止屏幕内容的采集，并以暂停那一刻的画面垫片，所以在远端看到一直都是最后一帧画面，直到 resume。
 

## 设定画面质量
您可以通过 `setSubStreamEncoderParam` 接口设定屏幕分享的画面质量，包括分辨率、码率和帧率，我们提供如下建议参考值：

| 清晰度级别 | 分辨率 | 帧率 | 码率 | 
|:-------------:|:---------:|:---------:| :---------: | 
| 超高清（HD+） | 1920 × 1080 | 10 | 800kbps |
|  高清（HD） | 1280 × 720 | 10 | 600kbps |
| 标清（SD） | 960 × 720 | 10 | 400kbps |

## 观看屏幕分享
  当房间里有一个用户启动了屏幕分享，会通过辅流进行分享。房间里的其他用户会通过 ITRTCCloudCallback 中的 [onUserSubStreamAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudCallback__cplusplus.html) 事件获得这个通知。
  希望观看屏幕分享的用户可以通过 [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__cplusplus.html) 接口来启动渲染远端用户辅流画面。

```C++
//示例代码：观看屏幕分享的画面
void CTRTCCloudSDK::onUserSubStreamAvailable(const char * userId, bool available) {
    LINFO(L"onUserSubStreamAvailable userId[%s] available[%d]\n", UTF82Wide(userId).c_str(), available);
    liteav::ITRTCCloud* trtc_cloud_ = getTRTCShareInstance();
    if (available) {
        trtc_cloud_->startRemoteView(userId, liteav::TRTCVideoStreamTypeSub, hWnd);
    } else {
        trtc_cloud_->stopRemoteView(userId, liteav::TRTCVideoStreamTypeSub);
    }
}
```

## 常见问题
####  1. 一个房间里可以同时有多路屏幕分享吗？
目前一个 TRTC 音视频房间只能有一路屏幕分享。

####  2. 指定窗口分享（SourceTypeWindow），当窗口大小变化时，视频流的分辨率会不会也跟着变化？
默认情况下，SDK 内部会自动根据分享的窗口大小进行编码参数的调整。
如需固定分辨率，需调用 setSubStreamEncoderParam 接口设置屏幕分享的编码参数，或在调用 startScreenCapture 时指定对应的编码参数。

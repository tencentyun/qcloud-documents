腾讯云 TRTC 支持屏幕分享功能，Mac 平台下的屏幕分享支持主路分享和辅路分享两种方案：
- **辅路分享**
在 TRTC 中，我们可以单独为屏幕分享开启一路上行的视频流，并称之为“辅路（**substream**）”。辅路分享即主播同时上行摄像头画面和屏幕画面两路画面。这是腾讯会议的使用方案，您可以在调用 `startScreenCapture` 接口时，通过将 `TRTCVideoStreamType` 参数指定为 `TRTCVideoStreamTypeSub ` 来启用该模式。观看该路画面需要使用专门的 `startRemoteSubStreamView` 接口。

- **主路分享**
在 TRTC 中，我们一般把摄像头走的通道叫做“主路（**bigstream**）”，主路分享即用摄像头通道分享屏幕。该模式下，主播只有一路上行视频流，要么上行摄像头画面，要么上行屏幕画面，两者是互斥的。您可以在调用 `startScreenCapture` 接口时，通过将 `TRTCVideoStreamType` 参数指定为 `TRTCVideoStreamTypeBig` 来启用该模式。

## 支持的平台

| iOS | Android | Mac OS | Windows |Electron| 微信小程序 | Chrome 浏览器|
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|  &#10003; |  &#10003; |  &#10003;  |&#10003;  |   &#10003;  |   ×   |  &#10003;  |

## 获取分享目标
通过 [getScreenCaptureSourcesWithThumbnailSize](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a37df498cbc8d9b1135e3caafdcee906f) 可以枚举可共享的窗口列表，每一个可共享的目标都是一个`TRTCScreenCaptureSourceInfo` 对象。

Mac OS 里的桌面屏幕也是一个可共享目标，普通的 Mac 窗口的 type 为 `TRTCScreenCaptureSourceTypeWindow`，桌面屏幕的 type 为 `TRTCScreenCaptureSourceTypeScreen`。

除了 type，每一个 `TRTCScreenCaptureSourceInfo` 还有如下字段信息：

| 字段 | 类型 | 含义|
|:-------:|:--------:| :---------------:|
| type |TRTCScreenCaptureSourceType| 采集源类型：指定类型为窗口或屏幕|
| sourceId | NSString| 采集源 ID：对于窗口，该字段指示窗口句柄；<br>对于屏幕，该字段指示屏幕 ID |
| sourceName| NSString | 窗口名字，如果是屏幕则返回 Screen0 Screen1... |
| extInfo| NSDictionary | 共享窗口的附加信息 | 
| thumbnail| NSImage | 窗口缩略图 |
| icon | NSImage | 窗口图标 |

有了上面这些信息，您就可以实现一个简单的列表页面，将可以分享的目标罗列出来供用户选择，如下图：
![](https://main.qcloudimg.com/raw/ae43c4ec148a0e25368fea0ea20063b7.jpg)

## 选择分享目标
TRTC SDK 支持三种分享模式，您可以通过 [selectScreenCaptureTarget](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a01ead6fb3106ea266caa922f5901bf18) 来指定：

- **整个屏幕分享**：
即把整个屏幕窗口分享出去，支持多显示器分屏的情况。需要指定一个 type 为 `TRTCScreenCaptureSourceTypeScreen` 的 screenSource 参数 ，并将 rect 设为 { 0, 0, 0, 0 }。

- **指定区域分享**：
即把屏幕的某个区域分享出去，需要用户圈定区域的位置坐标。需要指定一个 type 为 `TRTCScreenCaptureSourceTypeScreen` 的 screenSource 参数 ，并将 captureRect 设为非 NULL，例如 { 100, 100, 300, 300 }。

- **指定窗口分享**：
即把目标窗口的内容分享出去，需要用户选择要分享的是哪一个窗口。需要指定一个 type 为 `TRTCScreenCaptureSourceTypeWindow` 的 screenSource 参数 ，并将 captureRect 设为 { 0, 0, 0, 0 }。


>? 两个额外参数：
> - 参数 capturesCursor 用于指定是否捕获鼠标指针。
> - 参数 highlight 用于指定是否高亮正在共享的窗口，以及当捕获图像被遮挡时提示用户移走遮挡。（这一分部的 UI 特效是 SDK 内部实现的）


## 开始屏幕分享

 - 选取分享目标之后，使用 [startScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a59b16baa51d86cc0465dc6edd3cbfc97) 接口可以启动屏幕分享。
 - 两个函数 [pauseScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a6f536bcc3df21b38885809d840698280) 和  [stopScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#aa8ea0235691fc9cde0a64833249230bb) 的区别在于 pause 会停止屏幕内容的采集，并以暂停那一刻的画面垫片，所以在远端看到一直都是最后一帧画面，直到 [resumeScreenCapture](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af257a8fb6969fe908ca68a039e6dba15)。
 
```Objective-C
 /**
 *  7.6 【屏幕共享】启动屏幕分享
 *  @param view 渲染控件所在的父控件
 */
- (void)startScreenCapture:(NSView *)view;

/**
 *  7.7 【屏幕共享】停止屏幕采集
 *  @return 0：成功 <0:失败
 */
- (int)stopScreenCapture;

/**
 *  7.8 【屏幕共享】暂停屏幕分享
 *  @return 0：成功 <0:失败
 */
- (int)pauseScreenCapture;

/**
 *  7.9 【屏幕共享】恢复屏幕分享
 *
 *  @return 0：成功 <0:失败
 */
- (int)resumeScreenCapture;
```

## 设定画面质量
您可以通过 [setSubStreamEncoderParam](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#abc0f3cd5c320d0e65163bd07c3c0a735) 接口设定屏幕分享的画面质量，包括分辨率、码率和帧率，我们提供如下建议参考值：

| 清晰度级别 | 分辨率 | 帧率 | 码率 | 
|:-------------:|:---------:|:---------:| :---------: | 
| 超高清（HD+） | 1920 × 1080 | 10 | 800kbps |
| 高清（HD） | 1280 × 720 | 10 | 600kbps |
| 标清（SD） | 960 × 720 | 10 | 400kbps |

## 观看屏幕分享
- **观看 Mac / Windows 屏幕分享**
  当房间里有一个 Mac / Windows 用户启动了屏幕分享，会通过辅流进行分享。房间里的其他用户会通过 TRTCCloudDelegate 中的 [onUserSubStreamAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#ac45fb0751f7dbd2466a35c8828c9911b) 事件获得这个通知。
  希望观看屏幕分享的用户可以通过 [startRemoteSubStreamView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a68d048ccd0d018995e33e9e714e14474) 接口来启动渲染远端用户辅流画面。

- **观看 Android / iOS 屏幕分享**
  若用户通过 Android / iOS 进行屏幕分享，会通过主流进行分享。房间里的其他用户会通过 TRTCCloudDelegate 中的 [onUserVideoAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDelegate__ios.html#a533d6ea3982a922dd6c0f3d05af4ce80) 事件获得这个通知。
  希望观看屏幕分享的用户可以通过 [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#af85283710ba6071e9fd77cc485baed49) 接口来启动渲染远端用户主流画面。

```Objective-C
//示例代码：观看屏幕分享的画面

- (void)onUserSubStreamAvailable:(NSString *)userId available:(BOOL)available {
    if (available) {
        [self.trtcCloud startRemoteSubStreamView:userId view:self.capturePreviewWindow.contentView];
    } else {
        [self.trtcCloud stopRemoteSubStreamView:userId];
    }
}
```

## 常见问题
**一个房间里可以同时有多个人共享屏幕吗？**
目前一个 TRTC 音视频房间只能有一路屏幕分享。

**指定窗口分享（SourceTypeWindow），当窗口大小变化时，视频流的分辨率会不会也跟着变化？**
默认情况下，SDK 内部会自动根据分享的窗口大小进行编码参数的调整。
如需固定分辨率，需调用 setSubStreamEncoderParam 接口设置屏幕分享的编码参数，或在调用 startScreenCapture 时指定对应的编码参数。

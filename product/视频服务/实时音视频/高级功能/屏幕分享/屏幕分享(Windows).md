腾讯云 TRTC 服务支持屏幕分享功能，屏幕分享的画面走单独的一路音视频流，与摄像头画面并行，而且支持音画同步。一般而言，我们称摄像头这一路画面为“主路（或主画面）”，屏幕分享这一路画面为“辅路（**substream**）”。本文主要介绍在 Windows 平台下如何使用 TRTC SDK 提供的屏幕分享功能。

## 支持的平台

| iOS | Android | Mac OS | Windows | 微信小程序 | Chrome 浏览器|
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|     ✖  |    ✖    |    ✔   |    ✔    |    ✖     |   ✔     |

## 获取分享目标
通过 `getScreenCaptureSources` 可以枚举可共享的窗口列表，列表通过出参 sourceInfoList 返回。
>? Windows 里的桌面屏幕也是一个窗口，叫桌面窗口（Desktop），有两台显示器时，每一台显示器都有一个对应的桌面窗口。所以，getScreenCaptureSources 返回的窗口列表里也会有 Desktop 窗口。

sourceInfoList 中每一个 sourceInfo 可以分享的目标，它由如下字段描述。

| 字段 | 类型 | 含义|
|:-------:|:--------:| :---------------:|
| type |TRTCScreenCaptureSourceType| 采集源类型，指定类型为窗口或屏幕|
| sourceId | HWND| 采集源 ID<br>对于窗口，该字段指示窗口句柄；<br>对于屏幕，该字段指示屏幕 ID |
| sourceName| string | 窗口名字，如果是屏幕则返回 Screen0 Screen1... |
| thumbWidth| int32 | 窗口缩略图宽度 | 
| thumbHeight| int32 | 窗口缩略图高度 |
| thumbBGRA| buffer | 窗口缩略图的二进制 buffer |
| iconWidth | int32 | 窗口图标的宽度 |
| iconHeight| int32 | 窗口图标的高度 |
| iconBGRA | buffer | 窗口图标的二进制 buffer |

根据上述信息，您可以实现一个简单的列表页面，将可以分享的目标罗列出来供用户选择，如下图：

![](https://main.qcloudimg.com/raw/e370bcac46cc9ab5eb75e34378664d97.jpg)

## 选择分享目标
TRTC SDK 支持三种分享模式，您可以通过 `selectScreenCaptureTarget` 来指定：

- **整个屏幕分享**：
即分享整个屏幕窗口，支持多显示器分屏的情况。需要指定一个 sourceInfoList 中 type 为 `TRTCScreenCaptureSourceTypeScreen` 的 source 参数 ，并将 captureRect 设为 { 0, 0, 0, 0 }。

- **指定区域分享**：
即分享屏幕的某个区域，需要用户圈定区域的位置坐标。需要指定一个 sourceInfoList 中 type 为 `TRTCScreenCaptureSourceTypeScreen` 的 source 参数 ，并将 captureRect 设为非 NULL，例如 { 100, 100, 300, 300 }。

- **指定窗口分享**：
即分享目标窗口的内容，需要用户选择要分享的窗口。需要指定一个 sourceInfoList 中 type 为 `TRTCScreenCaptureSourceTypeWindow` 的 source 参数，并将 captureRect 设为 { 0, 0, 0, 0 }。


>? 两个额外参数：
> - 参数 captureMouse 用于指定是否捕获鼠标指针。
> - 参数 highlightWindow 用于指定是否高亮正在共享的窗口，以及当捕获图像被遮挡时提示用户移走遮挡。这部分的 UI 特效是由 SDK 内部实现的。


## 开始屏幕分享

 - 选取分享目标后，使用 `startScreenCapture` 接口可以启动屏幕分享。
 - 分享过程中，您依然可以通过调用 `selectScreenCaptureTarget` 更换分享目标。
 - `pauseScreenCapture` 和  `stopScreenCapture` 的区别在于 pause 会停止屏幕内容的采集，并以暂停那一刻的画面垫片，所以在远端看到一直都是最后一帧画面，直到 resume。
 
```C++
    /**
    * \brief 7.5 【屏幕共享】启动屏幕分享
    * \param：rendHwnd - 承载预览画面的 HWND
    */
    void startScreenCapture(HWND rendHwnd);

    /**
    * \brief 7.6 【屏幕共享】暂停屏幕分享
    */
    void pauseScreenCapture();

    /**
    * \brief 7.7 【屏幕共享】恢复屏幕分享
    */
    void resumeScreenCapture();

    /**
    * \brief 7.8 【屏幕共享】关闭屏幕分享
    */
    void stopScreenCapture();
```

## 设定画面质量
您可以通过 `setSubStreamEncoderParam` 接口设定屏幕分享的画面质量，包括分辨率、码率和帧率，我们提供如下建议参考值：

| 清晰度级别 | 分辨率 | 帧率 | 码率 | 
|:-------------:|:---------:|:---------:| :---------: | 
| 高清 | 1920 × 1080 | 10 | 800kbps |
| 标清 | 1280 × 720 | 10 | 600kbps |
| 低清 | 1280 × 720 | 10 | 400kbps |

## 观看屏幕分享
当房间里有一个用户启动了屏幕分享，房间里的其他用户会通过  TRTCCloudCallback 的 `onUserSubStreamAvailable` 获得这个通知。
希望观看屏幕分享的用户可以通过 `startRemoteSubStreamView` 来启动渲染远端用户辅流画面。

```C++
//示例代码：观看屏幕分享的画面
void CTRTCCloudSDK::onUserSubStreamAvailable(const char * userId, bool available)
{
	    LINFO(L"onUserSubStreamAvailable userId[%s] available[%d]\n", UTF82Wide(userId).c_str(), available);
	   if (available)  {
	         startRemoteSubStreamView(userId, hWnd);
	   } else {
	         stopRemoteSubStreamView(userId);
	   }
}
```

## 常见问题
 **一个房间里可以同时有多路屏幕分享吗？**
目前一个 TRTC 音视频房间只能有一路屏幕分享。

 **指定窗口分享（SourceTypeWindow），当窗口大小变化时，视频流的分辨率会不会也跟着变化？**
不会跟着变化，当窗口大小变化时，窗口画面会被等比例缩放到目标分辨率上。





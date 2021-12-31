腾讯云 TRTC 在 Android 系统上支持屏幕分享，即将当前系统的屏幕内容通过 TRTC SDK 分享给房间里的其他用户。关于此功能，有两点需要注意：

- 移动端 TRTC Android 8.6 之前的版本屏幕分享并不像桌面端版本一样支持“辅路分享”，因此在启动屏幕分享时，摄像头的采集需要先被停止，否则会相互冲突；8.6 及之后的版本支持“辅路分享”，则不需要停止摄像头的采集。
- 当一个 Android 系统上的后台 App 在持续使用 CPU 时，很容易会被系统强行杀掉，而且屏幕分享本身又必然会消耗 CPU。要解决这个看似矛盾的冲突，我们需要在 App 启动屏幕分享的同时，在 Android 系统上弹出悬浮窗。由于 Android 不会强杀包含前台 UI 的 App 进程，因此该种方案可以让您的 App 可以持续进行屏幕分享而不被系统自动回收。如下图所示：
![](https://main.qcloudimg.com/raw/e7dad1db0a99add95ac372634bddc2bf.png)


## 支持的平台

| iOS | Android | Mac OS | Windows |Electron| 微信小程序 | Chrome 浏览器|
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|  &#10003; |  &#10003; |  &#10003;  |&#10003;  |   &#10003;  |   ×   |  &#10003;  |

## 启动屏幕分享
要开启 Android 端的屏幕分享，只需调用 `TRTCCloud` 中的  [startScreenCapture()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa6671fc587513dad7df580556e43be58) 接口即可。但如果要达到稳定和清晰的分享效果，您需要关注如下三个问题：

#### 添加 Activity
在 manifest 文件中粘贴如下 activity（若项目代码中存在则不需要添加）。
```xml
<activity 
    android:name="com.tencent.rtmp.video.TXScreenCapture$TXScreenCaptureAssistantActivity" 
    android:theme="@android:style/Theme.Translucent"/>
```

#### 设定视频编码参数
通过设置 [startScreenCapture()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#aa6671fc587513dad7df580556e43be58)  中的首个参数 `encParams` ，您可以指定屏幕分享的编码质量。如果您指定 `encParams` 为 null，SDK 会自动使用之前设定的编码参数，我们推荐的参数设定如下：

| 参数项 | 参数名称 | 常规推荐值 |  文字教学场景 |
|---------|---------|---------|-----|
| 分辨率 | videoResolution | 1280 × 720 | 1920 × 1080 |
| 帧率 | videoFps | 10 FPS | 8 FPS |
| 最高码率 | videoBitrate| 1600 kbps | 2000 kbps |
| 分辨率自适应 | enableAdjustRes | NO | NO |

- 由于屏幕分享的内容一般不会剧烈变动，所以设置较高的 FPS 并不经济，推荐10 FPS即可。
- 如果您要分享的屏幕内容包含大量文字，可以适当提高分辨率和码率设置。
- 最高码率（videoBitrate）是指画面在剧烈变化时的最高输出码率，如果屏幕内容变化较少，实际编码码率会比较低。

#### 弹出悬浮窗以避免被强杀
从 Android 7.0 系统开始，切入到后台运行的普通 App 进程，但凡有 CPU 活动，都很容易会被系统强杀掉。 所以当 App 在切入到后台默默进行屏幕分享时，通过弹出悬浮窗的方案，可以避免被系统强杀掉。 同时，在手机屏幕上显示悬浮窗也有利于告知用户当前正在做屏幕分享，避免用户泄漏个人隐私。

- **方案1：弹出普通的悬浮窗**
要弹出类似“腾讯会议”的迷你悬浮窗，您只需要参考示例代码 [FloatingView.java](https://github.com/tencentyun/TRTCSDK/blob/master/Android/TRTC-API-Example/Basic/ScreenShare/src/main/java/com/tencent/trtc/screenshare/FloatingView.java) 中的实现即可：
```java
public void showView(View view, int width, int height) {
        mWindowManager = (WindowManager) mContext.getSystemService(Context.WINDOW_SERVICE);
        //TYPE_TOAST仅适用于4.4+系统，假如要支持更低版本使用TYPE_SYSTEM_ALERT(需要在manifest中声明权限)
        //7.1（包含）及以上系统对TYPE_TOAST做了限制
        int type = WindowManager.LayoutParams.TYPE_TOAST;
        if (Build.VERSION.SDK_INT > Build.VERSION_CODES.N) {
            type = WindowManager.LayoutParams.TYPE_PHONE;
        }
        mLayoutParams = new WindowManager.LayoutParams(type);
        mLayoutParams.flags = WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE;
        mLayoutParams.flags |= WindowManager.LayoutParams.FLAG_WATCH_OUTSIDE_TOUCH;
        mLayoutParams.width = width;
        mLayoutParams.height = height;
        mLayoutParams.format = PixelFormat.TRANSLUCENT;
        mWindowManager.addView(view, mLayoutParams);
}
```

- **方案2：弹出摄像头预览窗**
由于 TRTC Android 8.6之前的版本屏幕分享并不像桌面端版本一样支持“辅路分享”，因此在启动屏幕分享时，摄像头这一路的视频数据无法上行，否则会相互冲突。8.6及之后版本支持“辅路分享”，则无此冲突，但一样可以使用以下方法。
那要如何才能做到同时分享屏幕和摄像头画面呢？
答案很简单：只需要在屏幕上悬浮一个摄像头画面即可，这样一来，TRTC 在采集屏幕画面的同时也会将摄像头画面一并分享出去。

## 观看屏幕分享
- **观看 Mac / Windows 屏幕分享**
  当房间里有一个 Mac / Windows 用户启动了屏幕分享，会通过辅流进行分享。房间里的其他用户会通过 TRTCCloudDelegate 中的 [onUserSubStreamAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloudCallback__csharp.html#a15be39bb902bf917321b26701e961286) 事件获得这个通知。
  希望观看屏幕分享的用户可以通过 [startRemoteSubStreamView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#ae029514645970e7d32470cf1c7aca716) 接口来启动渲染远端用户辅流画面。

- **观看 Android / iOS 屏幕分享**
  若用户通过 Android / iOS 进行屏幕分享，会通过主流进行分享。房间里的其他用户会通过 TRTCCloudListener 中的 [onUserVideoAvailable](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudListener__android.html#ac1a0222f5b3e56176151eefe851deb05) 事件获得这个通知。
  希望观看屏幕分享的用户可以通过 [startRemoteView](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#a57541db91ce032ada911ea6ea2be3b2c) 接口来启动渲染远端用户主流画面。


```java
//示例代码：观看屏幕分享的画面
 @Override
 public void onUserSubStreamAvailable(String userId, boolean available) {
    startRemoteSubStreamView(userId);
}
```

## 常见问题
 **一个房间里可以同时有多路屏幕分享吗？**
目前一个 TRTC 音视频房间只能有一路屏幕分享。



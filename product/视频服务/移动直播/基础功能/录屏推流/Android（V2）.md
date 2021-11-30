## 功能介绍
手机录屏直播，即可以直接把主播的手机画面作为直播源，同时可以叠加摄像头预览，应用于游戏直播、移动端 App 演示等需要手机屏幕画面的场景。腾讯云 LiteAVSDK 通过 V2TXLivePusher 接口提供录屏推流能力，如下是 LiteAVSDK 腾讯云工具包 App 中演示摄像头推流的相关操作界面：
>?直播中叠加摄像头预览，即通过在手机上添加浮框，显示摄像头预览画面。录屏的时候会把浮框预览画面一并录制下来，达到叠加摄像头预览的效果。

![](https://main.qcloudimg.com/raw/7ea3ae48fc9bfa67ada5e248c0212a9f.png)

## 限制说明
- Android 5.0 系统以后开始支持录屏功能。
- 悬浮窗在部分手机和系统上需要通过手动设置打开。

## 示例代码
针对开发者的接入反馈的高频问题，腾讯云提供有更加简洁的 API-Example 工程，方便开发者可以快速的了解相关 API 的使用，欢迎使用。

| 所属平台 |                         GitHub 地址                          |
| :------: | :----------------------------------------------------------: |
|   iOS    | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/MLVB-API-Example-OC) |
| Android  | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/Android/MLVB-API-Example) |


## 对接攻略
[](id:step1)
### 步骤1：创建 Pusher 对象
创建一个 **V2TXLivePusher** 对象，我们后面主要用它来完成推流工作。

```java
V2TXLivePusher mLivePusher = new V2TXLivePusherImpl(context, V2TXLiveDef.V2TXLiveMode.TXLiveMode_RTMP);
```

[](id:step2)
### 步骤2：启动推流
经过 [步骤1](#step1) 的准备之后，用下面这段代码就可以启动推流了：
```java
String rtmpUrl = "rtmp://2157.livepush.myqcloud.com/live/xxxxxx";
mLivePusher.startMicrophone();
mLivePusher.startScreenCapture();
mLivePusher.startPush(rtmpUrl);
```
- **startScreenCapture** 的作用是启动屏幕录制，由于录屏是基于 Android 系统的原生能力实现的，处于安全考虑，Android 系统会在开始录屏前弹出提示，允许即可。
- **startPush** 的作用是告诉 LiteAV SDK 音视频流要推到哪个推流 URL 上去。

[](id:step3)
### 步骤3：设置 Logo 水印
设置 V2TXLivePusher 中的 [setWatermark](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__android.html#a4f56a5a937d87e5b1ae6f77c5bab2335) 可以让 SDK 在推出的视频流中增加一个水印，水印位置位是由传入参数 `(x, y, scale)` 所决定。

- SDK 所要求的水印图片格式为 PNG 而不是 JPG，因为 PNG 这种图片格式有透明度信息，因而能够更好地处理锯齿等问题（将 JPG 图片修改后缀名是不起作用的）。
- `(x, y, scale)` 参数设置的是水印图片相对于推流分辨率的归一化坐标。假设推流分辨率为：540 × 960，该字段设置为：`（0.1，0.1，0.1）`，那么水印的实际像素坐标为：（540 × 0.1，960 × 0.1，水印宽度 × 0.1，水印高度会被自动计算）。

```java 
//设置视频水印 
mLivePusher.setWatermark(BitmapFactory.decodeResource(getResources(),R.drawable.watermark), 0.03f, 0.015f, 1f); 
```

[](id:step4)
### 步骤4：推荐的清晰度
调用 V2TXLivePusher 中的`setVideoQuality`接口，可以设定观众端的画面清晰度。之所以说是观众端的画面清晰度，是因为主播看到的视频画面是未经编码压缩过的高清原画，不受设置的影响。而`setVideoQuality`设定的视频编码器的编码质量，观众端可以感受到画质的差异。详情请参见 [设定画面质量](https://cloud.tencent.com/document/product/454/56600)。

[](id:step5)
### 步骤5：提醒主播“网络不好”
手机连接 Wi-Fi 网络不一定就非常好，如果 Wi-Fi 信号差或者出口带宽很有限，可能网速不如4G，如果主播在推流时遇到网络很差的情况，需要有一个友好的提示，提示主播应当切换网络。    
![](https://main.qcloudimg.com/raw/ede09b70402bee1d88f86492226c6b46.png)  

通过 V2TXLivePusherObserver 里的 [onWarning](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLiveCode__android.html) 可以捕获 **V2TXLIVE_WARNING_NETWORK_BUSY** 事件，它代表当前主播的网络已经非常糟糕，出现此事件即代表观众端会出现卡顿。此时就可以像上图一样在 UI 上弹出一个“弱网提示”。
<dx-codeblock>
::: objectiveC objectiveC
@Override
public void onWarning(int code, String msg, Bundle extraInfo) {
    if (code == V2TXLiveCode.V2TXLIVE_WARNING_NETWORK_BUSY) {
        showNetBusyTips(); // 显示网络繁忙的提示
    }
} 
:::
</dx-codeblock>

[](id:step6)
### 步骤6：横竖屏适配
大多数情况下，主播习惯以“竖屏持握”手机进行直播拍摄，观众端看到的也是竖屏分辨率的画面（例如 540 × 960 这样的分辨率）；有时主播也会“横屏持握”手机，这时观众端期望能看到是横屏分辨率的画面（例如 960 × 540 这样的分辨率），如下图所示： 
![](https://main.qcloudimg.com/raw/b1e58275542aac52fb861745d95246cc.png)    

V2TXLivePusher 默认推出的是竖屏分辨率的视频画面，如果希望推出横屏分辨率的画面，可以修改 [setVideoQuality](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__android.html#a2695806cb6c74ccce4b378d306ef0a02) 接口的参数来设定观众端的画面横竖屏模式。

```java 
mLivePusher.setVideoQuality(mVideoResolution, isLandscape ? V2TXLiveVideoResolutionModeLandscape : V2TXLiveVideoResolutionModePortrait);   
```

[](id:step7)
### 步骤7：结束推流
因为用于推流的 `V2TXLivePusher` 对象同一时刻只能有一个在运行，所以结束推流时要做好清理工作。
```java
//结束录屏直播，注意做好清理工作
public void stopPublish() {
    mLivePusher.stopScreenCapture();
    mLivePusher.setObserver(null);
    mLivePusher.stopPush();
}
```

## 事件处理

### 事件监听
SDK 通过 [V2TXLivePusherObserver](http://doc.qcloudtrtc.com/group__V2TXLivePusherObserver__android.html) 代理来监听推流相关的事件通知和错误通知，详细的事件表和错误码表请参见 [错误码表](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLiveCode__android.html)。

### 错误通知
SDK 发现部分严重问题，推流无法继续。

| 事件 ID                              | 数值 | 含义说明                        |
| :------------------------------------ | :---- | :------------------------------- |
| V2TXLIVE_ERROR_FAILED                | -1   | 暂未归类的通用错误            |
| V2TXLIVE_ERROR_INVALID_PARAMETER     | -2   | 调用 API 时，传入的参数不合法 |
| V2TXLIVE_ERROR_REFUSED               | -3   | API 调用被拒绝                |
| V2TXLIVE_ERROR_NOT_SUPPORTED         | -4   | 当前 API 不支持调用           |
| V2TXLIVE_ERROR_INVALID_LICENSE       | -5   | license 不合法，调用失败      |
| V2TXLIVE_ERROR_REQUEST_TIMEOUT       | -6   | 请求服务器超时                |
| V2TXLIVE_ERROR_SERVER_PROCESS_FAILED | -7   | 服务器无法处理您的请求        |

### 警告事件
SDK 发现部分警告问题，但 WARNING 级别的事件都会触发一些尝试性的保护逻辑或者恢复逻辑，而且有很大概率能够恢复。

| 事件 ID                                       | 数值  | 含义说明                                                     |
| :-------------------------------------------- | :---- | :----------------------------------------------------------- |
| V2TXLIVE_WARNING_NETWORK_BUSY                 | 1101  | 网络状况不佳：上行带宽太小，上传数据受阻                   |
| V2TXLIVE_WARNING_VIDEO_BLOCK                  | 2105  | 当前视频播放出现卡顿                                         |
| V2TXLIVE_WARNING_CAMERA_START_FAILED          | -1301 | 摄像头打开失败                                             |
| V2TXLIVE_WARNING_CAMERA_OCCUPIED              | -1316 | 摄像头正在被占用中，可尝试打开其他摄像头                   |
| V2TXLIVE_WARNING_CAMERA_NO_PERMISSION         | -1314 | 摄像头设备未授权，通常在移动设备出现，可能是权限被用户拒绝了 |
| V2TXLIVE_WARNING_MICROPHONE_START_FAILED      | -1302 | 麦克风打开失败                                             |
| V2TXLIVE_WARNING_MICROPHONE_OCCUPIED          | -1319 | 麦克风正在被占用中，例如移动设备正在通话时，打开麦克风会失败 |
| V2TXLIVE_WARNING_MICROPHONE_NO_PERMISSION     | -1317 | 麦克风设备未授权，通常在移动设备出现，可能是权限被用户拒绝了 |
| V2TXLIVE_WARNING_SCREEN_CAPTURE_NOT_SUPPORTED | -1309 | 当前系统不支持屏幕分享                                     |
| V2TXLIVE_WARNING_SCREEN_CAPTURE_START_FAILED  | -1308 | 开始录屏失败，如果在移动设备出现，可能是权限被用户拒绝了   |
| V2TXLIVE_WARNING_SCREEN_CAPTURE_INTERRUPTED   | -7001 | 录屏被系统中断                                             |

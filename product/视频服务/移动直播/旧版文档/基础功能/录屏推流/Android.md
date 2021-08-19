
## 功能介绍
手机录屏直播，即可以直接把主播的手机画面作为直播源，同时可以叠加摄像头预览，应用于游戏直播、移动端 App 演示等需要手机屏幕画面的场景。
>?直播中叠加摄像头预览，即通过在手机上添加浮框，显示摄像头预览画面。录屏的时候会把浮框预览画面一并录制下来，达到叠加摄像头预览的效果。具体实现方法可参见  [小直播源码](https://github.com/tencentyun/MLVBSDK/blob/master/Android/XiaoZhiBo/app/src/main/java/com/tencent/qcloud/xiaozhibo/anchor/screen/widget/FloatingCameraView.java)。

![](https://main.qcloudimg.com/raw/5be5fa0002348a29614bb129084455a5.png)

## 限制说明
- Android 5.0 系统以后开始支持录屏功能。 
- 悬浮窗在部分手机和系统上需要通过手动设置打开。
- 录屏直播时，请先关闭小米的**神隐模式**。

![](https://main.qcloudimg.com/raw/2574ba9cf80d92fec94f59bcd1a94607.jpg)


## 对接攻略
[](id:step_1)
### 步骤 1：添加 Activity

在 manifest 文件中粘贴如下 activity（若项目代码中存在则不需要添加）。
```xml
<activity 
    android:name="com.tencent.rtmp.video.TXScreenCapture$TXScreenCaptureAssistantActivity" 
    android:theme="@android:style/Theme.Translucent"/>
```

[](id:step_2)
### 步骤 2：创建 Pusher 对象
创建一个 **TXLivePusher** 对象，我们后面主要用它来完成推流工作。

不过在创建 LivePush 对象之前，还需要您指定一个 **LivePushConfig** 对象，该对象的用途是决定 LivePush 推流时各个环节的配置参数，例如推流用多大的分辨率、每秒钟要多少帧画面（FPS）以及多少秒一个I帧（ Gop）等等。

LivePushConfig 在 new 出来之后便已经装配了一些我们反复调过的参数，如果您不需要自己定制这些配置，简单地塞给 LivePush 对象就可以了。如果您有相关领域的经验基础，需要对这些默认配置进行调整，可以阅读 [进阶篇](https://cloud.tencent.com/document/product/454/34771) 中的内容。

```java
TXLivePusher mLivePusher = new TXLivePusher(getActivity());
mLivePushConfig = new TXLivePushConfig();
mLivePusher.setConfig(mLivePushConfig);
```

### 步骤 3：启动推流
经过 [步骤 1](#step_1) 和 [步骤 2](#step_2) 的准备之后，用下面这段代码就可以启动推流了：
```java
String rtmpUrl = "rtmp://2157.livepush.myqcloud.com/live/xxxxxx";
mLivePusher.startPusher(rtmpUrl);
mLivePusher.startScreenCapture();
```
- **startPusher** 的作用是告诉 RTMP SDK 音视频流要推到哪个推流 URL 上去。
- **startScreenCapture** 的作用是启动屏幕录制，由于录屏是基于 Android 系统的原生能力实现的，处于安全考虑，Android 系统会在开始录屏前弹出一个提示，旨在告诫用户：“有 App 要截取您屏幕上的所有内容”。

### 步骤 4：隐私模式
隐私模式是录屏直播的一项基础功能：主播在录屏直播过程中，如果有些操作不希望观众看到（例如输入游戏的账号密码等等），那么此时主播可以启动**隐私模式**。在隐私模式下，主播的推流还是持续的，观众也一直能看到画面，只是看到的画面是一张提示“主播正在操作隐私内容哦~”的等待中画面。
![](https://main.qcloudimg.com/raw/5f8f56261955821c0f74ad1d47794560.png)

要实现这样功能，您可以按如下步骤进行对接：
- **4.1) 设置 pauseImg**
在开始推流前，使用 [TXLivePushConfig](https://cloud.tencent.com/document/product/454/34771) 的 setPauseImg 接口设置一张等待图片，例如“主播把画面切走一会儿...”。
- **4.2) 隐私模式开关**
在用于工具条的悬浮窗口上增加一个用于开关隐私模式的按钮，打开隐私模式的响应逻辑为对 TXLivePusher##pausePush 接口函数的调用，关闭隐私模式的响应逻辑为对 [TXLivePusher##resumePush](https://cloud.tencent.com/document/product/454/34772#resumepusher) 接口函数的调用。
```java
public void triggerPrivateMode() {
        if (mInPrivacy) {
            Toast.makeText(getApplicationContext(), “隐私模式已开启”, Toast.LENGTH_SHORT).show();
            mTVPrivateMode.setText(getString(R.string.private_mode_off));
            mTVPrivateMode.setCompoundDrawables(mDrawableLockOn,null,null,null);
            mPrivateBtn.setImageResource(R.mipmap.lock_off);
            mTXLivePusher.pausePusher();
        } else {
            Toast.makeText(getApplicationContext(), “隐私模式已关闭”, Toast.LENGTH_SHORT).show();
            mTXLivePusher.resumePusher();
            mPrivateBtn.setImageResource(R.mipmap.lock_on);
            mTVPrivateMode.setText(getString(R.string.private_mode_on));
            mTVPrivateMode.setCompoundDrawables(mDrawableLockOff,null,null,null);
        }
        mInPrivacy = !mInPrivacy;
    }
```
 
### 步骤 5：设置 Logo 水印
**据相关政策规定，直播视频必须加上水印。**腾讯视频云目前支持两种水印设置方式：一种是在推流 SDK 进行设置，原理是在 SDK 内部进行视频编码前就给画面打上水印。另一种方式是在云端打水印，也就是云端对视频进行解析并添加水印 Logo。

这里我们特别建议您使用 SDK 添加水印，因为在云端打水印有三个明显的问题：
 - 这是一种很耗云端机器的服务，而且不是免费的，会拉高您的费用成本。
 - 在云端打水印对于推流期间切换分辨率等情况的兼容并不理想，会有很多花屏的问题发生。
 - 在云端打水印会引入额外的3s以上的视频延迟，这是转码服务所引入的。

SDK 所要求的水印图片格式为 png，因为 png 这种图片格式有透明度信息，因而能够更好地处理锯齿等问题（建议您不要在 Windows 下将 jpg 格式的图片修改后缀名就直接使用，因为专业的 png 图标都是需要由专业的美工设计师处理的）。

```java
//设置视频水印
mLivePushConfig.setWatermark(BitmapFactory.decodeResource(getResources(),R.drawable.watermark), 10, 10);
mLivePusher.setConfig(mLivePushConfig);
```

### 步骤 6：推荐的清晰度
影响画质的主要因素有：**分辨率**、**帧率**和**码率**。
- **分辨率**
手机录屏直播提供了三个级别的分辨率可供选择：360\*640，540\*960，720\*1280，设置接口为 TXLivePushConfig 中的 [setVideoResolution](https://cloud.tencent.com/document/product/454/34771#setvideoresolution)。
- **帧率**
FPS <=10 会明显感觉到卡顿，手机录屏直播推荐设置20FPS - 25FPS 的帧率，设置接口为TXLivePushConfig 中的 [setVideoFPS](https://cloud.tencent.com/document/product/454/34771#setvideofps)。
- **码率**
编码器每秒编出的数据大小，单位是kbps，例如800kbps代表编码器每秒产生800kb（或100KB）的数据。设置接口为 TXLivePushConfig 中的 [setVideoBitrate](https://cloud.tencent.com/document/product/454/34771#setvideobitrate )。

相比于摄像头直播，录屏直播的不确定性会大很多，其中一个最大的不确定性因素就是录屏的场景。
-  一种极端就是手机屏幕停在一个界面保持不动，例如桌面，这个时候编码器可以用很小的码率输出就能完成任务。
- 另一种极端情况就是手机屏幕每时每刻都在发生剧烈的变化，例如主播在玩《神庙逃跑》，这个时候即使540 * 960的普通分辨率也至少需要2Mbps的码率才能保证没有马赛克。

| 档位   | 分辨率 | FPS |  码率-游戏录屏（捕鱼达人） | 码率-游戏录屏（神庙逃跑） |
|---------|---------|---------|---------|-----|
| 标清 | VIDEO_RESOLUTION_TYPE_360_640 | 20   | 800kbps |  1200kbps|
| 高清 | VIDEO_RESOLUTION_TYPE_540_960 | 20   | 1200kbps | 2000kbps|
| 超清 | VIDEO_RESOLUTION_TYPE_720_1280 | 20 | 1600kbps | 3000kbps|

### 步骤 7：提醒主播“网络不好”
<p>步骤 10 中会介绍 RTMP SDK 的推流事件处理，其中 <strong>PUSH_WARNING_NET_BUSY</strong> 这个很有用，它的含义是：<strong>当前主播的上行网络质量很差，观众端已经出现卡顿。</strong>

当收到此 WARNING 时，您可以通过 UI 提醒主播换一下网络出口，或者建议主播离 Wi-Fi 近一点，或者让他提醒一声：“领导，我在直播呢，别上淘宝了行不！什么？没上淘宝？那韩剧也是一样的啊。”</p>

### 步骤 8：横竖屏适配
腾讯云 RTMP SDK 中内部已经实现了动态横竖屏切换视频逻辑，所以在使用录屏直播时无需关注这个问题，主播的手机在横竖屏切换的时候，观众端看到的画面会同主播的视角保持一致。

### 步骤 9：向 SDK 填充自定义 Audio 数据
如果您希望把音频的采集替换成自己的逻辑，需要为 CustomMode 设置项追加 CUSTOM_MODE_AUDIO_CAPTURE，于此同时，您也需要指定声音采样率等和声道数等关键信息。
```java
// (1)将 CustomMode 设置为：自己采集音频数据，SDK只负责编码&发送
_config.customModeType |= CUSTOM_MODE_AUDIO_CAPTURE;
//
// (2)设置音频编码参数：音频采样率和声道数
_config.audioSampleRate = 44100;
_config.audioChannels   = 1;
```
之后，调用 **sendCustomPCMData** 向 SDK 塞入您自己的 PCM 数据即可。

[](id:step10)
### 步骤 10：事件处理
####  事件监听
RTMP SDK 通过 [ITXLivePushListener](https://cloud.tencent.com/document/product/454/34770) 代理来监听推流相关的事件，注意 ITXLivePushListener  只能监听得到 PUSH_前缀的推流事件。

####  常规事件 
一次成功的推流都会通知的事件，例如收到1003就意味着摄像头的画面会开始渲染了。

| 事件 ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_EVT_CONNECT_SUCC            |  1001| 已经成功连接到腾讯云推流服务器|
|PUSH_EVT_PUSH_BEGIN              |  1002| 与服务器握手完毕，一切正常，准备开始推流|
|PUSH_EVT_OPEN_CAMERA_SUCC    | 1003    | 推流器已成功打开摄像头（Android 部分手机这个过程需要1秒 - 2秒）| 

####  错误通知 
SDK 发现了一些严重问题，推流无法继续了，例如，用户禁用了 App 的 Camera 权限导致摄像头打不开。

| 事件 ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_ERR_OPEN_CAMERA_FAIL        | -1301| 打开摄像头失败|
|PUSH_ERR_OPEN_MIC_FAIL           | -1302| 打开麦克风失败|
|PUSH_ERR_VIDEO_ENCODE_FAIL       | -1303| 视频编码失败|
|PUSH_ERR_AUDIO_ENCODE_FAIL       | -1304| 音频编码失败|
|PUSH_ERR_UNSUPPORTED_RESOLUTION  | -1305| 不支持的视频分辨率|
|PUSH_ERR_UNSUPPORTED_SAMPLERATE  | -1306| 不支持的音频采样率|
|PUSH_ERR_NET_DISCONNECT          | -1307| 网络断连，且经三次重连无效，可以放弃，更多重试请自行重启推流|

####  警告事件 
SDK 发现了一些问题，但这并不意味着无法解决，很多 WARNING 都会触发一些重试性的保护逻辑或者恢复逻辑，而且有很大概率能够恢复，所以，千万不要“小题大做”。
- **PUSH_WARNING_NET_BUSY**
主播网络不给力，如果您需要 UI 提示，这个 WARNING 相对比较有用（[步骤10](#step10)）。
- **PUSH_WARNING_SERVER_DISCONNECT**
推流请求被后台拒绝了，会触发有限次数的重试逻辑，有可能可以在某一次重试中推流成功。但实际上，大部分场景中都是推流地址里的 txSecret 计算错了，或者被其他人占用了测试地址，所以这个 WARNING 对您的调试帮助意义更大。

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_WARNING_NET_BUSY            |  1101| 网络状况不佳：上行带宽太小，上传数据受阻|
|PUSH_WARNING_RECONNECT           |  1102| 网络断连，已启动自动重连（自动重连连续失败超过三次会放弃）|
|PUSH_WARNING_HW_ACCELERATION_FAIL|  1103| 硬编码启动失败，采用软编码|
|PUSH_WARNING_DNS_FAIL            |  3001 |  RTMP -DNS 解析失败（会触发重试流程）        |
|PUSH_WARNING_SEVER_CONN_FAIL     |  3002|  RTMP 服务器连接失败（会触发重试流程）  |
|PUSH_WARNING_SHAKE_FAIL          |  3003|  RTMP 服务器握手失败（会触发重试流程）  |
|PUSH_WARNING_SERVER_DISCONNECT      |  3004|  RTMP 服务器主动断开连接（会触发重试流程）  |

>?全部事件定义请参阅头文件**“TXLiveConstants.java”**。

### 步骤 11：结束推流
结束推流很简单，不过要做好清理工作，因为用于推流的 TXLivePusher 对象同一时刻只能有一个在运行，所以清理工作不当会导致下次直播遭受不良的影响。
```java
//结束录屏直播，注意做好清理工作
public void stopPublish() {
    mTXLivePusher.stopScreenCapture();
    mTXLivePusher.setPushListener(null);
    mTXLivePusher.stopPusher();
}
```

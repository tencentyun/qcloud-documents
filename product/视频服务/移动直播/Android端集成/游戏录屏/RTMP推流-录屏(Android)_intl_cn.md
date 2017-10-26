
## 手机录屏
RTMP SDK 1.6.1 开始支持手机录屏直播，即可以直接把主播的手机画面作为直播源，同时可以叠加摄像头预览，应用于游戏直播、移动端APP演示等需要手机屏幕画面的场景。

![](//mc.qcloudimg.com/static/img/bf82394c56c13298f322df25c5de4e16/image.png)

录屏功能在 iOS 和 Android 下有两套截然不同的实现方案：
- **Android 平台**
Android 5.0 系统以后开始支持，主播只需要在直播前安装并启动直播App，然后按Home将App切到后台，之后主播屏幕上的内容都可以作为直播内容。其内部原理是使用Android系统提供的录屏API进行画面采集，并由RTMP SDK底层模块负责编码和RTMP推流。

- **iOS 平台**
iOS 10.0 系统以后开始支持，基于iOS系统的扩展方式实现，即游戏直播开始时，iOS系统会唤起支持录屏直播的系统扩展（由直播App负责安装），并将屏幕图像传给这个系统扩展并由它完成编码和直播推流。

## 功能体验
我们在小直播Demo中，基于腾讯云 RTMP SDK 实现了两个平台的手机录屏功能，您可以扫描下图中的二维码安装并体验之。
![](//mc.qcloudimg.com/static/img/5cb1860bdcc58b8286a9fb4a421ee1c1/screencapturedemo.jpg)

## 对接攻略

### step 1: 添加Activity
在manifest文件中黏贴进如下一个activity
```xml
<activity 
    android:name="com.tencent.rtmp.video.TXScreenCapture$TXScreenCaptureAssistantActivity" 
    android:theme="@android:style/Theme.Translucent"/>
```

### step 2: 创建Pusher对象
创建一个**TXLivePusher**对象，我们后面主要用它来完成推流工作。

不过在创建 LivePush 对象之前，还需要您指定一个**LivePushConfig**对象，该对象的用途是决定 LivePush 推流时各个环节的配置参数，比如推流用多大的分辨率、每秒钟要多少帧画面（FPS）以及Gop（表示多少秒一个I帧）等等。

LivePushConfig 在new出来之后便已经装配了一些我们反复调过的参数，如果您不需要自己定制这些配置，简单地塞给LivePush对象就可以了。如果您有相关领域的经验基础，需要对这些默认配置进行调整，可以阅读**进阶篇**中的内容。

```java
TXLivePusher mLivePusher = new TXLivePusher(getActivity());
mLivePushConfig = new TXLivePushConfig();
mLivePusher.setConfig(mLivePushConfig);
```

### step 3: 启动推流
经过step1 和 step2 的准备之后，用下面这段代码就可以启动推流了：
```java
String rtmpUrl = "rtmp://2157.livepush.myqcloud.com/live/xxxxxx";
mLivePusher.startPusher(rtmpUrl);
mLivePusher.startScreenCapture();
```
- **startPusher** 的作用是告诉 RTMP SDK 音视频流要推到哪个推流URL上去。
- **startScreenCapture** 的作用是启动屏幕录制，由于录屏是基于 Android 系统的原生能力实现的，处于安全考虑，Android 系统会在开始录屏前弹出一个提示，旨在告诫用户：“有 App 要截取您屏幕上的所有内容”。

### step 4: 隐私模式
隐私模式是录屏直播的一项基础功能：主播在录屏直播过程中，如果有些操作不希望观众看到（比如输入游戏的账号密码等等），那么此时TA可以启动**隐私模式**，隐私模式下，主播的推流还是持续的，观众也一直能看到的画面，只是看到的画面是一张提示“主播正在忙...”的等待中画面。
![](//mc.qcloudimg.com/static/img/558efb32484da9813253620c0c4b1165/image.png)

要实现这样功能，您可以按如下步骤进行对接：
- **4.1) 设置pauseImg**
在开始推流前，使用 TXLivePushConfig 的 setPauseImg 接口设置一张等待图片，比如“主播把画面切走一会儿...”。

- **4.2) 隐私模式开关**
在用于工具条的悬浮窗口上增加一个用于开关隐私模式的按钮，打开隐私模式的响应逻辑为对 TXLivePusher##pausePush 接口函数的调用，关闭隐私模式的响应逻辑为对 TXLivePusher##resumePush 接口函数的调用。
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
 
### step 5: 设置Logo水印
最近相关政策规定，直播的视频必须要打上水印，所以这个之前看起来并不是特别起眼的功能现在要重点说一下：
腾讯视频云目前支持两种水印设置方式：一种是在推流SDK进行设置，原理是在SDK内部进行视频编码前就给画面打上水印。另一种方式是在云端打水印，也就是云端对视频进行解析并添加水印Logo。

这里我们特别建议您使用<font color='red'>SDK添加水印</font>，因为在云端打水印有三个明显的问题：
 （1）这是一种很耗云端机器的服务，而且不是免费的，会拉高您的费用成本；
 （2）在云端打水印对于推流期间切换分辨率等情况的兼容并不理想，会有很多花屏的问题发生。
 （3）在云端打水印会引入额外的3s以上的视频延迟，这是转码服务所引入的。

SDK所要求的水印图片格式为png，因为png这种图片格式有透明度信息，因而能够更好地处理锯齿等问题。（您可千万别把jpg图片在windows下改个后缀名就塞进去了，专业的png图标都是需要由专业的美工设计师处理的）

```java
//设置视频水印
mLivePushConfig.setWatermark(BitmapFactory.decodeResource(getResources(),R.drawable.watermark), 10, 10);
mLivePusher.setConfig(mLivePushConfig);
```

### step 6: 推荐的清晰度
影响画质的主要因素是三个：**分辨率**、**帧率**和**码率**。
- **分辨率**
手机录屏直播提供了三个级别的分辨率可供选择：360\*640，540\*960，720\*1280，设置接口为TXLivePushConfig 中的 setVideoResolution。
- **帧率**
FPS <=10 会明显感觉到卡顿，手机录屏直播推荐设置 20 - 25 FPS 的帧率，设置接口为TXLivePushConfig 中的 setVideoFPS。
- **码率**
编码器每秒编出的数据大小，单位是kbps，比如800kbps代表编码器每秒产生800kb（或100KB）的数据。设置接口为TXLivePushConfig 中的 setVideoBitrate。

相比于摄像头直播，录屏直播的不确定性会大很多，其中一个最大的不确定性因素就是录屏的场景。
（1） 一种极端就是手机屏幕停在一个界面保持不动，比如桌面，这个时候编码器可以用很小的码率输出就能完成任务。

（2）另一种极端情况就是手机屏幕每时每刻都在发生剧烈的变化，比如主播在玩《神庙逃跑》，这个时候即使 540 * 960 的普通分辨率也至少需要 2Mbps 的码率才能保证没有马赛克。

| 档位   | 分辨率 | FPS |  码率-游戏录屏（扑鱼达人） | 码率-游戏录屏（神庙逃跑） |
|---------|---------|---------|---------|
| 标清 | VIDEO_RESOLUTION_TYPE_360_640 | 20   | 800kbps |  1200kbps|
| 高清 | VIDEO_RESOLUTION_TYPE_540_960 | 20   | 1200kbps | 2000kbps|
| 超清 | VIDEO_RESOLUTION_TYPE_720_1280 | 20 | 1600kbps | 3000kbps|

### step 7: 提醒主播“网络不好”
step 9 中会介绍 RTMP SDK 的推流事件处理，其中 **PUSH_WARNING_NET_BUSY** 这个很有用，它的含义是：<font color='blue'>**当前主播的上行网络质量很差，观众端已经出现了卡顿。**</font>

当收到此WARNING时，您可以通过UI提醒主播换一下网络出口，或者离WiFi近一点，或者让他吼一嗓子：“领导，我在直播呢，别上淘宝了行不！什么？没上淘宝？那韩剧也是一样的啊。”

### step 8: 横竖屏适配
腾讯云 RTMP SDK 中内部已经实现了动态横竖屏切换视频逻辑，所以在使用录屏直播时无需关注这个问题，主播的手机在横竖屏切换的时候，观众端看到的画面会同主播的视角保持一致。

### step 9: 向SDK填充自定义Audio数据
如果你希望把音频的采集替换成自己的逻辑，需要为 CustomMode 设置项追加 CUSTOM_MODE_AUDIO_CAPTURE，于此同时，您也需要指定声音采样率等和声道数等关键信息。
```java
// (1)将 CustomMode 设置为：自己采集音频数据，SDK只负责编码&发送
_config.customModeType |= CUSTOM_MODE_AUDIO_CAPTURE;
//
// (2)设置音频编码参数：音频采样率和声道数
_config.audioSampleRate = 44100;
_config.audioChannels   = 1;
```
之后，调用**sendCustomPCMData**向SDK塞入您自己的PCM数据即可。

### step 10: 事件处理
####  事件监听
RTMP SDK 通过 TXLive<font color='red'>Push</font>Listener 代理来监听推流相关的事件，注意 TXLive<font color='red'>Push</font>Listener 只能监听得到 <font color='red'>PUSH_</font> 前缀的推流事件。

####  常规事件 
一次成功的推流都会通知的事件，比如收到1003就意味着摄像头的画面会开始渲染了

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_EVT_CONNECT_SUCC            |  1001| 已经成功连接到腾讯云推流服务器|
|PUSH_EVT_PUSH_BEGIN              |  1002| 与服务器握手完毕,一切正常，准备开始推流|
|PUSH_EVT_OPEN_CAMERA_SUCC    | 1003    | 推流器已成功打开摄像头（Android部分手机这个过程需要1-2秒）| 

####  错误通知 
SDK发现了一些严重问题，推流无法继续了，比如用户禁用了APP的Camera权限导致摄像头打不开。

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_ERR_OPEN_CAMERA_FAIL        | -1301| 打开摄像头失败|
|PUSH_ERR_OPEN_MIC_FAIL           | -1302| 打开麦克风失败|
|PUSH_ERR_VIDEO_ENCODE_FAIL       | -1303| 视频编码失败|
|PUSH_ERR_AUDIO_ENCODE_FAIL       | -1304| 音频编码失败|
|PUSH_ERR_UNSUPPORTED_RESOLUTION  | -1305| 不支持的视频分辨率|
|PUSH_ERR_UNSUPPORTED_SAMPLERATE  | -1306| 不支持的音频采样率|
|PUSH_ERR_NET_DISCONNECT          | -1307| 网络断连,且经三次抢救无效,可以放弃治疗,更多重试请自行重启推流|

####  警告事件 
SDK发现了一些问题，但这并不意味着无可救药，很多 WARNING 都会触发一些重试性的保护逻辑或者恢复逻辑，而且有很大概率能够恢复，所以，千万不要“小题大做”哦。

- PUSH_WARNING_NET_BUSY
主播网络不给力，如果您需要UI提示，这个 warning 相对比较有用（step10）。

- PUSH_WARNING_SERVER_DISCONNECT
推流请求被后台拒绝了，会触发有限次数的重试逻辑，有可能可以在某一次重试中推流成功。但实话实说，大部分场景中都是推流地址里的txSecret计算错了，或者被其他人占用了测试地址，所以这个 warning 对您的调试帮助意义更大。

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_WARNING_NET_BUSY            |  1101| 网络状况不佳：上行带宽太小，上传数据受阻|
|PUSH_WARNING_RECONNECT           |  1102| 网络断连, 已启动自动重连 (自动重连连续失败超过三次会放弃)|
|PUSH_WARNING_HW_ACCELERATION_FAIL|  1103| 硬编码启动失败，采用软编码|
|PUSH_WARNING_DNS_FAIL            |  3001 |  RTMP -DNS解析失败（会触发重试流程）        |
|PUSH_WARNING_SEVER_CONN_FAIL     |  3002|  RTMP服务器连接失败（会触发重试流程）  |
|PUSH_WARNING_SHAKE_FAIL          |  3003|  RTMP服务器握手失败（会触发重试流程）  |
|PUSH_WARNING_SERVER_DISCONNECT      |  3004|  RTMP服务器主动断开连接（会触发重试流程）  |

> 全部事件定义请参阅头文件**“TXLiveConstants.java”**

### step 11: 结束推流
结束推流很简单，不过要做好清理工作，因为用于推流的 TXLivePusher 对象同一时刻只能有一个在运行，所以清理工作不当会导致下次直播遭受不良的影响。
```java
//结束录屏直播，注意做好清理工作
public void stopPublish() {
    mTXLivePusher.stopScreenCapture();
    mTXLivePusher.setPushListener(null);
    mTXLivePusher.stopPusher();
}
```

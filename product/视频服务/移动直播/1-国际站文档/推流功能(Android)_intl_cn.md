## 基础知识
**推流** 是指将音视频数据采集编码之后，推送到您指定的视频云平台上，这里涉及大量的音视频基础知识，而且需要长时间的打磨和优化才能达到符合预期的效果。

腾讯视频云 SDK 主要帮您解决在智能手机上的推流问题，它的接口非常简单易用，只需要一个推流URL就能驱动：
![](//mc.qcloudimg.com/static/img/ca7f200c31a9323c032e9e000831ea63/image.jpg)

## 特别说明
- **<font color='red'>不绑定腾讯云</font>**
> SDK 不绑定腾讯云，如果要推流到非腾讯云地址，请在推流前设置 TXLivePushConfig 中的 enableNearestIP 设置为 NO。但如果您要推流的地址为腾讯云地址，请务必在推流前将其设置为 YES，否则推流质量可能会因为运营商 DNS 不准确而受到影响。

## 准备工作

- **获取开发包**
[下载](https://cloud.tencent.com/document/product/454/7873) SDK 开发包，并按照[工程配置](https://cloud.tencent.com/document/product/454/7877)指引将 SDK 嵌入您的 APP 开发工程。

- **获取测试URL**
[开通](https://console.cloud.tencent.com/live)直播服务后，可以使用 [直播控制台>>直播码接入>>推流生成器](https://console.cloud.tencent.com/live/livecodemanage) 生成推流地址，详细信息可以参考 [获得推流播放URL](https://cloud.tencent.com/document/product/454/7915)。

## 代码对接
本篇攻略主要是面向**摄像头直播**的解决方案，该方案主要用于美女秀场直播、个人直播以及活动直播等场景。

### step 1: 添加界面元素
为了能够展示摄像头预览的影像，您需要在您的布局xml文件里加入如下一段代码，他会在您的UI上安插一个TXCloudVideoView控件，这是我们用来显示摄像头影像的专用控件：
```xml
<com.tencent.rtmp.ui.TXCloudVideoView
            android:id="@+id/video_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:visibility="gone"/>
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

TXCloudVideoView mCaptureView = (TXCloudVideoView) view.findViewById(R.id.video_view);
mLivePusher.startCameraPreview(mCaptureView);
```
- **startPusher** 的作用是告诉 SDK 音视频流要推到哪个推流URL上去。
- **startCameraPreview** 则是将界面元素和Pusher对象关联起来，从而能够将手机摄像头采集到的画面渲染到屏幕上。

### step 4: 设定清晰度

使用 setVideoQuality 接口的可以设定推流的画面清晰度：

![](//mc.qcloudimg.com/static/img/c52dc506047402db04ac285fa7520e65/image.png)

- **quality**
SDK 提供了六种基础档位，根据我们服务大多数客户的经验进行积累和配置。其中 STANDARD、HIGH、SUPER 适用于直播模式，MAIN_PUBLISHER 和 SUB_PUBLISHER 适用于连麦直播中的大小画面，VIDEOCHAT 用于实时音视频。

- **adjustBitrate**
是否开启 Qos 流量控制，开启后SDK 会根据主播上行网络的好坏自动调整视频码率。相应的代价就是，主播如果网络不好，画面会很模糊且有很多马赛克。

- **adjustResolution**
是否允许动态分辨率，开启后 SDK 会根据当前的视频码率选择相匹配的分辨率，这样能获得更好的清晰度。相应的代价就是，动态分辨率的直播流所录制下来的文件，在很多播放器上会有兼容性问题。

![](//mc.qcloudimg.com/static/img/07deb1e7e01daba3227175a0fcec1fa5/image.png)

### step 5: 美颜滤镜
![](//mc.qcloudimg.com/static/img/aac647073cf0641141900e775e929418/image.png)
- **美颜**
setBeautyFilter 接口可以设置美颜风格、磨皮程度、美白级别和红润级别，配合 540 * 960 分辨率（setVideoQuality - VIDEO_QUALITY_HIGH_DEFINITION），可以达到最佳的画质效果：
 ```java
 //style             磨皮风格：  0：光滑  1：自然  2：朦胧
 //beautyLevel       磨皮等级： 取值为0-9.取值为0时代表关闭美颜效果.默认值:0,即关闭美颜效果.
 //whiteningLevel    美白等级： 取值为0-9.取值为0时代表关闭美白效果.默认值:0,即关闭美白效果.
 //ruddyLevel        红润等级： 取值为0-9.取值为0时代表关闭美白效果.默认值:0,即关闭美白效果. 
 //
 public boolean setBeautyFilter(int style, int beautyLevel, int whiteningLevel, int ruddyLevel);
 ```

- **滤镜**
setFilter 接口可以设置滤镜效果，滤镜本身是一张直方图文件，我们设计师团队提供了八种素材，默认打包在了Demo中，您可以随意使用，不用担心版权问题。

 setSpecialRatio 接口则可以设置滤镜的程度，从0到1，越大滤镜效果越明显，默认取值0.5。
```java
Bitmap bmp = null;
bmp = decodeResource(getResources(), R.drawable.langman);
if (mLivePusher != null) {
       mLivePusher.setFilter(bmp);
}
```
> 如果要自定义滤镜，一定要用 PNG 格式的图片，<font color='red'>不要用 JPG，不要用 JPG，不要用 JPG...</font>

- **曝光**
setExposureCompensation 可以调节曝光值，这个调整项在 iOS 端是没有的（我们使用了系统的自动曝光）。但是 Android 机型差异太大，很多千元机的自动曝光效果实在一般，所以我们推荐在您的 UI 界面上提供一个自动曝光的操作滑竿，让主播可以自己调节曝光值大小。
>setExposureCompensation 的参数为 -1 到 1 的浮点数： 0 表示不调整， -1 是将曝光降到最低， 1 表示是将曝光加强到最高。

### step 6: 控制摄像头
- **切换前置或后置摄像头** 
默认是使用**前置**摄像头（可以通过修改 TXLivePushConfig 的配置函数 setFrontCamera 来修改这个默认值），调用一次switchCamera 切换一次，注意切换摄像头前必须保证 TXLivePushConfig 和 TXLivePusher 对象都已经初始化。
```java
// 默认是前置摄像头
mLivePusher.switchCamera();
```
- **打开或关闭闪光灯** 
只有后置摄像头才可以打开闪光灯，另外该接口需要在启动预览之后调用
```java
//mFlashTurnOn为true表示打开，否则表示关闭
if (!mLivePusher.turnOnFlashLight(mFlashTurnOn)) {
        Toast.makeText(getActivity().getApplicationContext(),
            "打开闪光灯失败:绝大部分手机不支持前置闪光灯!", Toast.LENGTH_SHORT).show();
}
```
- **摄像头自动或手动对焦**
大部分后置摄像头才支持对焦，SDK 支持两种对焦模式：**手动对焦**和**自动对焦**。
自动对焦是系统提供的能力，但有些机型并不支持自动对焦。手动对焦和自动对焦是互斥的，开启自动对焦后，手动对焦将不生效。
SDK 默认配置是手动对焦，您可以通过 TXLivePushConfig 的配置函数 setTouchFocus 接口进行切换：
```java
mLivePushConfig.setTouchFocus(mTouchFocus);
mLivePusher.setConfig(mLivePushConfig);
```

### step 7: 设置Logo水印
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

### step 8: 硬件编码
TXLivePushConfig 中的 **setHardwareAcceleration** 设置接口可以开启或关闭硬件编码。
```java
if (!HWSupportList.isHWVideoEncodeSupport()){
    Toast.makeText(getActivity().getApplicationContext(), 
                   "当前手机型号未加入白名单或API级别过低（最低18）,请慎重开启硬件编码！", 
                   Toast.LENGTH_SHORT).show();
}
mLivePushConfig.setHardwareAcceleration(mHWVideoEncode);
mLivePusher.setConfig(mLivePushConfig);  
```

mHWVideoEncode 有以下选项。

|  硬件加速选项 | 含义 |
| :-----------| :-----------|
| ENCODE_VIDEO_HARDWARE | 开启硬件加速 |
| ENCODE_VIDEO_SOFTWARE | 禁用硬件加速，默认禁用硬件加速 |
| ENCODE_VIDEO_AUTO | 自动选择是否启用硬件加速 |


- **兼容性评估**
Android 手机目前对硬件加速的支持已较前两年有明显的进步，目前支持度还是不错的，但仍有个别机型有兼容性问题，目前 RTMP SDK 通过一个内部的黑名单进行控制，避免在部分兼容性差的机型上出现问题。如果您使用硬件编码失败，SDK 内部会自动切换为软件编码。

- **效果差异**
开启硬件加速后手机耗电量会有明显降低，机身温度也会比较理想，但画面大幅运动时马赛克感会比软编码要明显很多，而且越是早起的低端机，马赛克越是严重。所以如果您是对画质要求很高的客户，不推荐开启硬件加速。

- **推荐的设计**
我们在 setVideoQuality 的高清档（推荐档位）和标清档均推荐使用软件编码，如果您担心CPU和发热问题，可以做一个简单的保护逻辑： 
> 如果发现推流的 **FPS** ( 通过 TXLivePushListener 的 NET_STATUS_VIDEO_FPS 事件可以获知 ) 持续过低，比如半分钟内持续低于 10 帧/秒，表示 CPU 负载过重，则切换为硬编码。

### step 9: 后台推流
常规模式下，App一旦切到后台，摄像头的采集能力就被 Android 系统停掉了，这就意味着 SDK 不能再继续采集并编码出音视频数据。如果我们什么都不做，那么故事将按照如下的剧本发展下去：
 - 阶段一（切后台开始 -> 之后的10秒内）- CDN因为没有数据所以无法向观众提供视频流，观众看到画面卡主。
 - 阶段二（10秒 -> 70秒内）- 观众端的播放器因为持续收不到直播流而直接退出，直播间已经人去楼空。
 - 阶段三（70秒以后）- 推流的 RTMP 链路被服务器直接断掉，主播需要重新开启直播才能继续。
主播可能只是短暂接个紧急电话而已，但各云商的安全保护措施会让主播的直播被迫提前结束。

我们可以采用如下方案规避：
![](//mc.qcloudimg.com/static/img/6325a9f7918602bd8db15228e6ffe189/image.png)

- **9.1) 设置pauseImg**
在开始推流前，使用 TXLivePushConfig 的 setPauseImg 接口设置一张等待图片，图片含义推荐为“主播暂时离开一下下，稍后回来”。
- **9.2) 设置setPauseFlag**
在开始推流前，使用 TXLivePushConfig 的 setPauseFlag 接口设置切后台pause推流时需要停止哪些采集，停止视频采集则会推送pauseImg设置的默认图，停止音频采集则会推送静音数据。
>  setPauseFlag(PAUSE_FLAG_PAUSE_VIDEO|PAUSE_FLAG_PAUSE_AUDIO);//表示同时停止视频和音频采集，并且推送填充用的音视频流；
>         
>  setPauseFlag(PAUSE_FLAG_PAUSE_VIDEO);//表示停止摄像头采集视频画面，但保持麦克风继续采集声音，用于主播更衣等场景；

- **9.3) 切后台处理**
推流中，如果App被切了后台，调用 TXLivePusher 中的 pausePush 接口函数，之后，SDK 虽然采集不到摄像头的画面了，但可以用您刚才设置的 PauseImg 持续推流。
```java
// activity 的 onStop 生命周期函数
@Override
public void onStop(){
    super.onStop();
    mCaptureView.onPause();  // mCaptureView 是摄像头的图像渲染view
    mLivePusher.pausePusher(); // 通知 SDK 进入“后台推流模式”了
}
```
- **9.4) 切前台处理**
等待App切回前台之后，调用 TXLivePusher 的 resumePush 接口函数，之后，SDK 会继续采集摄像头的画面进行推流。
```java
// activity 的 onStop 生命周期函数
@Override
public void onResume() {
    super.onResume();
    mCaptureView.onResume();     // mCaptureView 是摄像头的图像渲染view
    mLivePusher.resumePusher();  // 通知 SDK 重回前台推流
}
```

### step 10: 提醒主播“网络不好”
step 13 中会介绍 SDK 的推流事件处理，其中 **PUSH_WARNING_NET_BUSY** 这个很有用，它的含义是：<font color='blue'>**当前主播的上行网络质量很差，观众端已经出现了卡顿。**</font>

当收到此WARNING时，您可以通过UI提醒主播换一下网络出口，或者离WiFi近一点，或者让她吼一嗓子：“领导，我在直播呢，别上淘宝了行不！什么？没上淘宝？那韩剧也是一样的啊。”

### step 11: 横屏推流
有时候用户在直播的时候需要更广的视角，则拍摄的时候需要“横屏持握”，这个时候其实是期望观看端能看到横屏画面，就需要做横屏推流，下面两幅示意图分别描述了横竖屏持握进行横竖屏推流在观众端看到的效果：
![](//mc.qcloudimg.com/static/img/cae1940763d5fd372ad962ed0e066b91/image.png)

- **调整观众端表现**
通过对 LivePushConfig 中的 **setHomeOrientation** 设置项进行配置，它控制的是观众端看到的视频宽高比是 **16:9** 还是 **6:19**，调整后的结果可以用播放器Demo查看以确认是否符合预期。

- **调整主播端表现**
观众端的画面表现符合预期以后，剩下要做的就是调整主播端的预览画面，这时可以通过 TXLivePusher 中的 setRenderRotation 接口，来旋转主播端看到的画面旋转方向，此接口提供了** 0，90，180，270** 四个参数供设置旋转角度。

- **Activity自动旋转**
Android 系统的 Activity 本身支持跟随手机的重力感应进行旋转（设置 android:configChanges），[CODE](https://cloud.tencent.com/document/product/454/9876)演示了如何做到下面这种重力感应效果：
![](//mc.qcloudimg.com/static/img/7255ffae57f3e9b7d929a5cb11f85c79/image.png)


### step 12: 背景混音
SDK 1.6.1 开始支持背景混音，支持主播带耳机和不带耳机两种场景，您可以通过 TXLivePusher 中的如下这组接口实现背景混音功能：

| 接口 | 说明 |
|---------|---------|
| playBGM | 通过path传入一首歌曲，[小直播Demo](https://cloud.tencent.com/doc/api/258/6164)中我们是从iOS的本地媒体库中获取音乐文件 |
| stopBGM|停止播放背景音乐|
| pauseBGM|暂停播放背景音乐|
| resumeBGM|继续播放背景音乐|
| setMicVolume|设置混音时麦克风的音量大小，推荐在UI上实现相应的一个滑动条，由主播自己设置|
| setBGMVolume|设置混音时背景音乐的音量大小，推荐在UI上实现相应的一个滑动条，由主播自己设置|

### step 13: 结束推流
结束推流很简单，不过要做好清理工作，因为用于推流的 TXLivePusher 和用于显示影像的 TXCloudVideoView 都是不能多实例并行运转的，所以清理工作不当会导致下次直播遭受不良的影响。
```java
//结束推流，注意做好清理工作
public void stopRtmpPublish() {
    mLivePusher.stopCameraPreview(true); //停止摄像头预览
    mLivePusher.stopPusher();            //停止推流
    mLivePusher.setPushListener(null);   //解绑 listener
}
```


## 事件处理
### 1. 事件监听
SDK 通过 TXLive<font color='red'>Push</font>Listener 代理来监听推流相关的事件，注意 TXLive<font color='red'>Push</font>Listener 只能监听得到 <font color='red'>PUSH_</font> 前缀的推流事件。

### 2. 常规事件 
一次成功的推流都会通知的事件，比如收到1003就意味着摄像头的画面会开始渲染了

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_EVT_CONNECT_SUCC            |  1001| 已经成功连接到腾讯云推流服务器|
|PUSH_EVT_PUSH_BEGIN              |  1002| 与服务器握手完毕,一切正常，准备开始推流|
|PUSH_EVT_OPEN_CAMERA_SUCC    | 1003    | 推流器已成功打开摄像头（Android部分手机这个过程需要1-2秒）| 

### 3. 错误通知 
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

### 4. 警告事件 
SDK发现了一些问题，但这并不意味着无可救药，很多 WARNING 都会触发一些重试性的保护逻辑或者恢复逻辑，而且有很大概率能够恢复，所以，千万不要“小题大做”哦。

- **WARNING_NET_BUSY**
主播网络不给力。如果您需要UI提示，这个 warning 相对比较有用（step10）。

- <font color='red'>**WARNING_SERVER_DISCONNECT**</font>
推流请求被后台拒绝了。出现这个问题一般是由于推流地址里的 txSecret 计算错了，或者是推流地址被其他人占用了（一个推流URL同时只能有一个端推流）。

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



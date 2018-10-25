
## RTMP SDK介绍
腾讯视频云 RTMP SDK 是由腾讯音视频团队开发和推出的一套 RTMP 标准直播解决方案，包含**RTMP推流**、**在线直播观看**和**Vod视频回看**三大类功能，囊括了腾讯音视频团队多年的技术积累，在视频压缩、硬件加速、美颜滤镜、音频降噪、码率控制等方面都做了很多的优化处理。

如果您是一位刚刚接触视频直播的合作伙伴，您只需要几行代码就可以完成对接流程，而如果您是一位资深的移动端软件开发工程师，SDK所提供的丰富的设置接口，亦可让您能够定制出最符合需求的表现。

![rtmp sdk push](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tx_cloud_push_sdk_struct.jpg)

## 下载RTMP SDK
在 [SDK下载区](https://cloud.tencent.com/doc/api/258/6172#.E7.A7.BB.E5.8A.A8.E7.AB.AFsdk) 里找到指定平台的SDK压缩包，压缩包中包含了SDK本体和Demo的代码，参考 [工程配置(Android)](https://cloud.tencent.com/doc/api/258/5319) 在Xcode中将其运行起来，如果一起顺利可以看到如下界面。
![demo](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/pusher_demo_introduction_2.jpg)

## 对接攻略
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
- **startPusher** 的作用是告诉 RTMP SDK 音视频流要推到哪个推流URL上去。
- **startCameraPreview** 则是将界面元素和Pusher对象关联起来，从而能够将手机摄像头采集到的画面渲染到屏幕上。

### step 4: 美颜滤镜
对于摄像头直播的场景，美颜是必不可少的一个功能点，本SDK提供了一种简单版实现，包含磨皮（level 1 -> level 10）和美白 (level 1 -> level 3)两个功能。

您可以在您的APP得用户操作界面上使用滑竿等控件来让用户选择美颜效果，或者推荐您也可以先用Demo里的滑竿进行，达到您满意的效果后，将此时的数值固定到程序的设置参数里。

```java
mLivePusher.setBeautyFilter(mBeautyLevel, mWhiteningLevel);
```

### step 5: 控制摄像头
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
大部分后置摄像头才支持对焦，RTMP SDK支持两种对焦模式：**手动对焦**和**自动对焦**。
自动对焦是系统提供的能力，但有些机型并不支持自动对焦。手动对焦和自动对焦是互斥的，开启自动对焦后，手动对焦将不生效。
RTMP SDK 默认配置是手动对焦，您可以通过 TXLivePushConfig 的配置函数 setTouchFocus 接口进行切换：
```java
mLivePushConfig.setTouchFocus(mTouchFocus);
mLivePusher.setConfig(mLivePushConfig);
```

### step 6: 设置Logo水印
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

### step 7: 硬件编码
TXLivePushConfig 中的 **setHardwareAcceleration** 设置接口可以开启或关闭硬件编码。
```java
if (!HWSupportList.isHWVideoEncodeSupport()){
    Toast.makeText(getActivity().getApplicationContext(), 
				   "当前手机型号未加入白名单或API级别过低（最低16）,请慎重开启硬件编码！", 
				   Toast.LENGTH_SHORT).show();
}
mLivePushConfig.setHardwareAcceleration(true);
mLivePusher.setConfig(mLivePushConfig);  
```

- **机型白名单**
> 上述示例代码中的第一句为 HWSupportList.isHWVideoEncodeSupport 调用，改函数并不是RTMP SDK提供的函数，而是位于Demo的 HWSupportList.java 文件中。
> 
> HWSupportList 是我们的专业测试团队处理过的一个[白名单列表](https://mc.qcloudimg.com/static/archive/a1e796c150ea60246e07947b679e0662/archive.xls)，列表中的机型可以放心开启硬件加速的Android机型，后续时间里我们会持续增加这个列表的机型数量。

- **推荐的设计**
>  不在白名单中的机型<font color='red'>**并非一定有问题**</font>，只是因为Android机型众多，我们没有精力全部测试过，所以如果您希望**在列表以外的机型上开启硬件加速**，最好加一些安全机制，比如一个推荐的做法是：
>  
>  提供两种或两种以上的清晰度选项，比如标清（360\*640）和高清（540\*960）两个档位，其中标清因为编码计算压力不大，采用软编码即可；高清则使用硬件编码。
>  
>  如此一来，如果高清档位的硬件加速出现问题，可以有标清档位作为保底方案。


### step 8: 后台推流
常规模式下，App一旦切到后台，摄像头的采集能力就被 Android 系统停掉了，这就意味着 SDK 不能再继续采集并编码出音视频数据。如果我们什么都不做，那么故事将按照如下的剧本发展下去：
 - 阶段一（切后台开始 -> 之后的10秒内）- CDN因为没有数据所以无法向观众提供视频流，观众看到画面卡主。
 - 阶段二（10秒 -> 70秒内）- 观众端的播放器因为持续收不到直播流而直接推出，直播间已经人去楼空。
 - 阶段三（70秒以后）- 推流的 RTMP 链路被服务器直接断掉，主播需要重新开启直播才能继续。

主播可能只是短暂接个紧急电话而已，但上述的交互体验显然会让观众全部离开直播间，怎么优化呢？

实际上使用一些投机的办法是可以实现的，比如创建一个Service，并使用1\*1像素的 SurfaceView 持续采集Camera数据。但如果您是主播，发现有个App在切后台之后还能访问摄像头，您是否真的敢用这个App呢？

我们需要在保护隐私和照顾观众体验方面求得一个完美的平衡：SDK 1.6.1 开始我们引入了一种解决方案： 
![](//mc.qcloudimg.com/static/img/6325a9f7918602bd8db15228e6ffe189/image.png)


- **8.1) 设置pauseImg**
在开始推流前，使用 TXLivePushConfig 的 setPauseImg 接口设置一张等待图片，图片含义推荐为“主播暂时离开一下下，稍后回来”。
- **8.2) 设置setPauseFlag**
在开始推流前，使用 TXLivePushConfig 的 setPauseFlag 接口设置切后台pause推流时需要停止哪些采集，停止视频采集则会推送pauseImg设置的默认图，停止音频采集则会推送静音数据。
>  setPauseFlag(PAUSE_FLAG_PAUSE_VIDEO|PAUSE_FLAG_PAUSE_AUDIO);//表示同时停止视频和音频采集，并且推送填充用的音视频流；
>         
>  setPauseFlag(PAUSE_FLAG_PAUSE_VIDEO);//表示停止摄像头采集视频画面，但保持麦克风继续采集声音，用于主播更新等场景；

- **8.3) 切后台处理**
推流中，如果App被切了后台，调用 TXLivePusher 中的 pausePush 接口函数，之后，RTMP SDK 虽然采集不到摄像头的画面了，但可以用您刚才设置的 PauseImg 持续推流。
```java
// activity 的 onStop 生命周期函数
@Override
public void onStop(){
    super.onStop();
    mCaptureView.onPause();  // mCaptureView 是摄像头的图像渲染view
    mLivePusher.pausePusher(); // 通知 SDK 进入“后台推流模式”了
}
```
- **8.4) 切前台处理**
等待App切回前台之后，调用 TXLivePusher 的 resumePush 接口函数，之后，RTMP SDK 会继续采集摄像头的画面进行推流。
```java
// activity 的 onStop 生命周期函数
@Override
public void onResume() {
    super.onResume();
    mCaptureView.onResume();     // mCaptureView 是摄像头的图像渲染view
    mLivePusher.resumePusher();  // 通知 SDK 重回前台推流
}
```

### step 9: 推荐的清晰度
影响画质的主要因素是三个：**分辨率**、**帧率**和**码率**。
- **分辨率**：摄像头直播有三种 9:16 的常规分辨率可供选择：360\*640，540\*960，720\*1280。
- **帧率**：FPS <=10 会明显感觉到卡顿，摄像头直播推荐设置 20 FPS。
- **码率**：编码器每秒编出的数据大小，单位是kbps，比如800kbps代表编码器每秒产生800kb（或100KB）的数据。

好的画质是分辨率、帧率和码率三者之间的平衡，如下是几种清晰度档位的推荐设置结果。其中，括号中标注的是 TXLivePushConfig 的对应设置函数：

| 档位   | 分辨率（setVideoResolution） | FPS（setVideoFPS） | 码率（setVideoBitrate） |
|---------|---------|---------|---------|
| 标清 | VIDEO_RESOLUTION_TYPE_360_640 | 20 | 700kbps |
| 高清 | VIDEO_RESOLUTION_TYPE_540_960 | 20 | 1000kbps | 
| 超清 | VIDEO_RESOLUTION_TYPE_720_1280 | 20 | 1500kbps |

> 美女秀场领域，我们的客户一般是选择**高清**档位，因为它比较平衡：720p超清档拍人像比较浪费，360p的效果又不能在清晰度上跟竞品拉开差距。

### step 10: 提醒主播“网络不好”
step 13 中会介绍 RTMP SDK 的推流事件处理，其中 **PUSH_WARNING_NET_BUSY** 这个很有用，它的含义是：<font color='blue'>**当前主播的上行网络质量很差，观众端已经出现了卡顿。**</font>

当收到此WARNING时，您可以通过UI提醒主播换一下网络出口，或者离WiFi近一点，或者让他吼一嗓子：“领导，我在直播呢，别上淘宝了行不！什么？没上淘宝？那韩剧也是一样的啊。”

### step 11: 横屏推流
大多数情况下，用户习惯以“竖屏持握”进行直播拍摄，观看端看到的也是竖屏样式；有时候用户在直播的时候需要更广的视角，则拍摄的时候需要“横屏持握”，这个时候其实是期望观看端能看到横屏画面，就需要做横屏推流，下面两幅示意图分别描述了横竖屏持握进行横竖屏推流在观众端看到的效果。
![](//mc.qcloudimg.com/static/img/cae1940763d5fd372ad962ed0e066b91/image.png)
> <font color='red'>**注意：**</font> 横屏推流和竖屏推流，观众端看到的图像的宽高比是不同的，竖屏9:16，横屏16：9。

#### 调整观众端表现
通过对 LivePushConfig 中的 **setHomeOrientation** 设置项进行配置，它控制的是观众端看到的视频宽高比是 **16:9** 还是 **6:19**，调整后的结果可以用播放器查看以确认是否符合预期。

| 设置项 | 含义 |
|:---------|---------|
| VIDEO_ANGLE_HOME_RIGHT     | home键在右 |
| VIDEO_ANGLE_HOME_DOWN     | home键在下 |
| VIDEO_ANGLE_HOME_LEFT       | home键在左 |
| VIDEO_ANGLE_HOME_UP           | home键在上 |

#### 调整主播端表现
观众端的画面表现符合预期以后，剩下要做的就是调整主播端的预览画面，这时可以通过 TXLivePusher 中的 setRenderRotation 接口，来旋转主播端看到的画面旋转方向，此接口提供了** 0，90，180，270** 四个参数供设置旋转角度。

#### Activity自动旋转
Android 系统的 Activity 本身支持跟随手机的重力感应进行旋转（设置 android:configChanges），如何做到下面这种横竖屏推流跟随重力感应而变换的效果呢？
![](//mc.qcloudimg.com/static/img/7255ffae57f3e9b7d929a5cb11f85c79/image.png)

```java
    @Override
    public void onConfigurationChanged(Configuration newConfig) {
        // 自动旋转打开，Activity随手机方向旋转之后，只需要改变推流方向
        int mobileRotation = this.getActivity().getWindowManager().getDefaultDisplay().getRotation();
        int pushRotation = TXLiveConstants.VIDEO_ANGLE_HOME_DOWN;
        switch (mobileRotation) {
            case Surface.ROTATION_0:
                pushRotation = TXLiveConstants.VIDEO_ANGLE_HOME_DOWN;
                break;
            case Surface.ROTATION_90:
                pushRotation = TXLiveConstants.VIDEO_ANGLE_HOME_RIGHT;
                break;
            case Surface.ROTATION_270:、
                pushRotation = TXLiveConstants.VIDEO_ANGLE_HOME_LEFT;
                break;
            default:
                break;
        }
				
				//通过设置config是设置生效（可以不用重新推流，腾讯云是少数支持直播中热切换分辨率的云商之一）
        mLivePusher.setRenderRotation(0); 
        mLivePushConfig.setHomeOrientation(pushRotation);
        mLivePusher.setConfig(mLivePushConfig);
    }
```



### step 12: 背景混音
RTMP SDK 1.6.1 开始支持背景混音，支持主播带耳机和不带耳机两种场景，您可以通过 TXLivePusher 中的如下这组接口实现背景混音功能：

| 接口 | 说明 |
|---------|---------|
| playBGM | 通过path传入一首歌曲，[小直播Demo](https://cloud.tencent.com/doc/api/258/6164)中我们是从iOS的本地媒体库中获取音乐文件 |
| stopBGM|停止播放背景音乐|
| pauseBGM|暂停播放背景音乐|
| resumeBGM|继续播放背景音乐|
| setMicVolume|设置混音时麦克风的音量大小，推荐在UI上实现相应的一个滑动条，由主播自己设置|
| setBGMVolume|设置混音时背景音乐的音量大小，推荐在UI上实现相应的一个滑动条，由主播自己设置|

### step 13: 事件处理
####  事件监听
RTMP SDK 通过 TXLive<font color='red'>Push</font>Listener 代理来监听推流相关的事件，注意 TXLive<font color='red'>Push</font>Listener 只能监听得到 <font color='red'>PUSH_</font> 前缀的推流事件。

####  常规事件 
一次成功的推流都会通知的事件，比如收到1003就意味着摄像头的画面会开始渲染了

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_EVT_CONNECT_SUCC            |  1001| 已经成功连接到腾讯云推流服务器|
|PUSH_EVT_PUSH_BEGIN              |  1002| 与服务器握手完毕,一切正常，准备开始推流|
|PUSH_EVT_OPEN_CAMERA_SUCC	  | 1003	| 推流器已成功打开摄像头（Android部分手机这个过程需要1-2秒）| 

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
|PUSH_WARNING_DNS_FAIL			  |  3001 |  RTMP -DNS解析失败（会触发重试流程）        |
|PUSH_WARNING_SEVER_CONN_FAIL     |  3002|  RTMP服务器连接失败（会触发重试流程）  |
|PUSH_WARNING_SHAKE_FAIL          |  3003|  RTMP服务器握手失败（会触发重试流程）  |
|PUSH_WARNING_SERVER_DISCONNECT      |  3004|  RTMP服务器主动断开连接（会触发重试流程）  |

> 全部事件定义请参阅头文件**“TXLiveConstants.java”**

### step 14: 结束推流
结束推流很简单，不过要做好清理工作，因为用于推流的 TXLivePusher 和用于显示影像的 TXCloudVideoView 都是不能多实例并行运转的，所以清理工作不当会导致下次直播遭受不良的影响。
```java
//结束推流，注意做好清理工作
public void stopRtmpPublish() {
    mLivePusher.stopCameraPreview(true); //停止摄像头预览
	mLivePusher.stopPusher();            //停止推流
    mLivePusher.setPushListener(null);   //解绑 listener
}
```




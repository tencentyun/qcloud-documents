## 功能篇
腾讯视频云RTMP SDK由两部分构成：**推流器** + **播放器**，本文将主要介绍推流器的相关信息。

该SDK遵循标准RTMP视频推送协议，可以对接包括腾讯云在内的标准视频直播服务器。与此同时，SDK内部囊括了腾讯音视频团队多年的技术积累，在视频压缩、硬件加速、美颜滤镜、音频降噪、码率控制等方面都做了很多的优化处理。

如果您是一位刚刚接触视频直播的合作伙伴，您只需要几行代码就可以完成对接流程，而如果您是一位资深的移动端软件开发工程师，SDK所提供的丰富的设置接口，亦可让您能够定制出最符合需求的表现。

![rtmp sdk push](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tx_cloud_push_sdk_struct.jpg)

SDK开发包附带的推流器DEMO界面如下：

![demo](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/pusher_demo_introduction_2.jpg)

## 基础篇
腾讯视频云RTMP SDK的使用特别简单，您只需要在您的App里添加如下几行代码就可以完成对接工作了。目前SDK内部的默认参数设置参考直播场景精心校调过的。

### step 1: 添加界面元素
为了能够展示推流预览的界面，您需要在您的布局xml文件里加入如下一段代码：
```xml
<com.tencent.rtmp.ui.TXCloudVideoView
            android:id="@+id/video_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:visibility="gone"/>
```

### step 2: 创建Pusher对象
先创建一个**Pusher**对象，它是所有SDK调用接口的承载者。
```java
TXLivePusher mLivePusher = new TXLivePusher(getActivity());
```

### step 3: 启动推流
用下面这段代码就可以完成推流了：
```java
String rtmpUrl = "rtmp://2157.livepush.myqcloud.com/live/xxxxxx";
mLivePusher.startPusher(rtmpUrl);

TXCloudVideoView mCaptureView = (TXCloudVideoView) view.findViewById(R.id.video_view);
mLivePusher.startCameraPreview(mGLRootView);
```

其中 **startPusher** 使用来告诉SDK视频流要推到哪个服务器地址去，而 **startCameraPreview** 则是将界面元素和Pusher对象关联起来，从而能够将手机摄像头采集到的画面渲染到屏幕上。

> **【小细节】**
> 传进来的self.view将会作为画面渲染view的父view，建议此父view专门作为渲染使用，如果您想要在摄像头画面之上加弹幕、献花之类的UI控件，请另行创建一个与self.view平级的view，并将该view叠加在self.view之上。

### step 4: 美颜滤镜
如果您是定位美女秀场，美颜是必不可少的一个功能点，本SDK提供了一种简单版实现，包含磨皮（level 1 -> level 10）和美白 (level 1 -> level 3)两个功能。您可以在您的APP得用户操作界面上使用滑竿等空间来让用户选择美颜效果，或者推荐您也可以先用Demo里的滑竿进行，达到您满意的效果后，将此时的数值固定到程序的设置参数里。

接口函数setBeautyFilterDepth可以动态调整美颜及美白级别（不支持Neon指令优化的极个别Android手机无法开启）:

```java
if (!mLivePusher.setBeautyFilter(mBeautyLevel, mWhiteningLevel)) {
    Toast.makeText(getActivity().getApplicationContext(), "当前机型的性能无法支持美颜功能", 
		    Toast.LENGTH_SHORT).show();
}
```

### step 5: 控制摄像头
- **切换前置或后置摄像头** : 默认是使用**前置**摄像头（可以通过修改config配置项来修改这个默认值），调用一次switchCamera 切换一次，注意切换摄像头前必须保证 LivePushConfig 和 LivePush 对象都已经初始化。 

```java
	// 默认是前置摄像头
	mLivePusher.switchCamera();
```
- **打开或关闭闪光灯** : 只有后置摄像头才可以打开闪光灯，另外该接口需要在启动预览之后调用

```java
    //mFlashTurnOn为true表示打开，否则表示关闭
	if (!mLivePusher.turnOnFlashLight(mFlashTurnOn)) {
        Toast.makeText(getActivity().getApplicationContext(),
            "打开闪光灯失败:绝大部分手机不支持前置闪光灯!", Toast.LENGTH_SHORT).show();
    }
```
- **摄像头自动或手动对焦**：大部分后置摄像头才支持对焦，SDK支持2种对焦模式：手动对焦和自动对焦。自动对焦是系统提供的能力，但是跟机型相关，有些机型并不支持自动对焦。手动对焦和自动对焦是互斥的，开启自动对焦后，手动对焦将不生效。SDK默认配置是手动对焦，您可以通过以下接口切换：
```java
 mLivePushConfig.setTouchFocus(mTouchFocus);
```

### step 6: 设置Logo水印
这里要特别说明一下，因为腾讯云支持两种方式设置水印：一种是在推流SDK进行设置，原理是在SDK内部进行视频编码前就给画面打上水印。另一种方式是在云端打水印，也就是云端对视频进行解析并添加水印Logo。

 这里我们特别建议您`使用SDK添加水印`，因为在云端打水印有三个明显的问题：
 （1）这是一种很耗机器的服务，会拉高您的费用成本；
 （2）在云端打水印对于推流期间切换分辨率等情况的兼容并不理想，会有很多花屏的问题发生。
 （3）在云端打水印会引入额外的3s以上的视频延迟，这是转码服务所引入的。

 SDK所要求的水印图片格式为png，因为png这种图片格式有透明度信息，因而能够更好地处理锯齿等问题。（您可千万别把jpg图片在windows下改个后缀名就塞进去了，专业的png图标都是需要由专业的美工设计师处理的）

```java
	//设置视频水印
    mLivePushConfig.setWatermark(BitmapFactory.decodeResource(getResources(),R.drawable.watermark), 10, 10);
    mLivePusher.setConfig(mLivePushConfig);
```

### step 7: 硬件编码
通过PushConfig里的**setHardwareAcceleration**接口可以开启硬件编码。
```java
if (!HWSupportList.isHWVideoEncodeSupport()){
    Toast.makeText(getActivity().getApplicationContext(), 
				   "当前手机型号未加入白名单或API级别过低（最低16）,请慎重开启硬件编码！", 
				   Toast.LENGTH_SHORT).show();
}
mLivePushConfig.setHardwareAcceleration(mHWVideoEncode);
mLivePusher.setConfig(mLivePushConfig);  
```

> **是否硬件编码？**
> 如果您的产品定位美女秀场，主用360*640这种分辨率，硬件编码并不比软编码好，因为Android的硬编码不确定性比IOS要高很多，所以建议您不要开。
> 如果您的产品定位高清场景，540p或者720p高清推流，那就建议尽量开启，因为Android手机的CPU降频策略，以及核心多但每个核心晶体管都很少的现状，注定了软编码处理540p都很吃力，所以硬件编码才能把帧率撑到20帧以上。

> **白名单策略**
> 目前我们在Demo的HWSupportList.java文件里有一个白名单列表，这里是我们自己团队测试过的，可以放心开启硬件加速的Android机型，后续时间里我们会持续增加这个列表的机型数量。
> 
> 目前RTMP SDK测试团队已经测试过的机型以及通过情况见 [机型列表](https://mc.qcloudimg.com/static/archive/a1e796c150ea60246e07947b679e0662/archive.xls)，供您参考。

## 定制篇
刚才讲的是最基本的使用方法，能满足绝大部分需求。
如果您是一位资深的软件开发工程师，可能还有更专业的要求，比如您可能会关心SDK的运行状态，或者会尝试做一些视频参数的定制等等，接下来我们看一下进阶使用：

### 1. 如果您关心内部原理
首先，您需要了解一下视频云RTMP SDK的内部原理，在推流模式下，SDK内部的状态机制如下：

![SDK内部原理](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tencent_cloud_rtmp_sdk_pusher_status_14.jpg)

简单描述就是在您**调用startPusher**之后，RTMP SDK就会**尝试连接网络**，并且**启动摄像头和麦克风的音视频采集**，如果一切顺利，就会进入**推流主循环**，之后如果一切正常，SDK内部会按照每秒一次的频率通知**当前的内部状态**（net status），如果中途出现什么问题，则会以 **event**、 **warning** 或者 **error** 的形式通知出来。

### 2. 如果您关心状态
想要获得RTMP SDK的状态通知，您可以提供一个**Listener**给刚才提到的**Pusher**对象，之后SDK的所有信息都会通过这个Listener反馈给您的App.

```java
public class MyTestActivity implements ITXLivePushListener{
	@Override
    public void onPushEvent(int event, Bundle param) {
		// your code
    }

     public void onNetStatus(Bundle status) {
		// your code
    }
}

mLivePusher.setPushListener(this);
```

#### 事件通知
- **常规事件** ：一次成功的推流都会通知的事件，比如收到1003就意味着摄像头的画面会开始渲染了。

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_EVT_CONNECT_SUCC            |  1001| 已经成功连接到腾讯云推流服务器|
|PUSH_EVT_PUSH_BEGIN              |  1002| 与服务器握手完毕,一切正常，准备开始推流|
|PUSH_EVT_OPEN_CAMERA_SUCC	  | 1003	| 推流器已成功打开摄像头（Android部分手机这个过程需要1-2秒）| 

- **警告事件** ：SDK发现了一些问题，比如主播的上行网络质量不理想，但并不意味着流程进行不下去。

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_WARNING_NET_BUSY            |  1101| 网络状况不佳：上行带宽太小，上传数据受阻|
|PUSH_WARNING_RECONNECT           |  1102| 网络断连, 已启动自动重连 (自动重连连续失败超过三次会放弃)|
|PUSH_WARNING_HW_ACCELERATION_FAIL|  1103| 硬编码启动失败，采用软编码|
|PUSH_WARNING_DNS_FAIL			  |  3001 |  RTMP -DNS解析失败（会触发重试流程）        |
|PUSH_WARNING_SEVER_CONN_FAIL     |  3002|  RTMP服务器连接失败（会触发重试流程）  |
|PUSH_WARNING_SHAKE_FAIL          |  3003|  RTMP服务器握手失败（会触发重试流程）  |

- **错误通知** ：SDK发现了一些严重问题，严重到推流是无法继续的，比如用户禁用了APP的Camera权限导致摄像头打不开。

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_ERR_OPEN_CAMERA_FAIL        | -1301| 打开摄像头失败|
|PUSH_ERR_OPEN_MIC_FAIL           | -1302| 打开麦克风失败|
|PUSH_ERR_VIDEO_ENCODE_FAIL       | -1303| 视频编码失败|
|PUSH_ERR_AUDIO_ENCODE_FAIL       | -1304| 音频编码失败|
|PUSH_ERR_UNSUPPORTED_RESOLUTION  | -1305| 不支持的视频分辨率|
|PUSH_ERR_UNSUPPORTED_SAMPLERATE  | -1306| 不支持的音频采样率|
|PUSH_ERR_NET_DISCONNECT          | -1307| 网络断连,且经三次抢救无效,可以放弃治疗,更多重试请自行重启推流|

> 事件定义请参阅头文件**“TXLiveConstants.java”**

#### 网络状态回调 
  **onNetStatus** 通知每秒都会被触发一次，目的是实时反馈当前的推流器状态:
	
|   评估参数                   |  含义说明                    |   
| :------------------------  |  :------------------------ | 
|	NET_STATUS_VIDEO_BITRATE | 当前视频编码器输出的比特率，也就是编码器每秒生产了多少视频数据，单位 kbps|
|	NET_STATUS_AUDIO_BITRATE | 当前音频编码器输出的比特率，也就是编码器每秒生产了多少音频数据，单位 kbps|
|	NET_STATUS_VIDEO_FPS     | 当前视频帧率，也就是视频编码器每条生产了多少帧画面|
|	NET_STATUS_NET_SPEED     | 当前的发送速度|
|	NET_STATUS_NET_JITTER    | 网络抖动情况，抖动越大，网络越不稳定|
|	NET_STATUS_CACHE_SIZE    | 缓冲区大小，缓冲区越大，说明当前上行带宽不足以消费掉已经生产的视频数据|

### 3. 如果您关心参数
如果您希望定制视频编码参数，音频编码参数等等，您可以通过设置Config对象实现您的自定义需求，目前我们支持的setting接口如下：

| 参数名           |    含义                                          |   默认值  | 
| :-------------- | :-----------------------------------------------| :------: |
| setAudioSampleRate|   音频采样率：录音设备在一秒钟内对声音信号的采集次数   |  44100   |  
| setANS            |   噪声抑制：开启后可以滤掉背景杂音（32000以下采样率有效）                     |  关闭     |
| setVideoFPS     	|   视频帧率：即视频编码器每秒生产出多少帧画面，注意由于大部分安卓机器摄像头不支持30FPS以上的采集，推荐您设置FPS为20           |  20      |
| setVideoResolution|   视频分辨率：目前提供三种16：9分辨率可供您选择      |  640 * 360 |
| setVideoBitrate 	|   视频比特率：即视频编码器每秒生产出多少数据，单位 kbps |  800  |
| setAutoAdjustBitrate |   带宽自适应：该功能会根据当前网络情况，自动调整视频比特率，避免视频数据超出发送能力而导致画面卡顿 |   开|
| setMaxVideoBitrate| 最大输出码率：只有开启自适应码率, 该设置项才能启作用 |   1200 |
| setMinVideoBitrate| 最小输出码率：只有开启自适应码率, 该设置项才能启作用 |   800  |
| setWatermark | 设置水印图片以及其相对屏幕左上角位置 | 腾讯云Logo（demo）  |    
| setHomeOrientation |  设置视频图像旋转角度，比如是否要横屏推流	| home在右边（0）home在下面（1）home在左面（2）home在上面（3）|

这些参数的设置推荐您在启动推流之前就指定，因为大部分设置项是在重新推流之后才能生效的。参考代码如下：


```java
// 成员变量中声明 config 和 pusher
private TXLivePushConfig mLivePushConfig = new TXLivePushConfig();
private TXLivePusher     mLivePusher = new TXLivePusher(getActivity());
	
// 修改参数设置
mLivePushConfig.setVideoResolution(TXLiveConstants.VIDEO_RESOLUTION_640_360);
mLivePushConfig.setAutoAdjustBitrate(false);
mLivePushConfig.setVideoBitrate(800);
//设置视频水印
mLivePushConfig.setWatermark(BitmapFactory.decodeResource(
	getResources(),R.drawable.watermark), 10, 10);

mLivePusher.setConfig(mLivePushConfig);
```

### 4. 如果您想自己加工视频数据
有些研发能力比较强的客户，会有自定义图像处理的需求（比如自定义图像滤镜），同时又希望复用rtmp sdk的整体流程，如果是这样，您可以按照如下攻略进行定制。

- **Step1. 实现一个图像处理的so**
您需要自己实现一个so，比如test.so，然后按照如下定义导出一个C风格的函数，之所以强制使用C而不是java是因为图像处理的效率C和C++比较容易胜任。您实现的PVideoProcessHookFunc 处理时间不能过长，试想，如果该函数的处理时间超过50ms，那就意味着SDK推出的视频流，其帧率不可能达到20FPS。
```C
/* @brief 客户自定义的视频预处理函数原型
 * @param yuv_buffer：视频YUV数据，格式固定是YUV420 Planar
 * @param len_buffer：数据长度
 * @param width：     视频width
 * @param height：    视频height
 * @return
 * @remark （1）该函数会被SDK同步调用，故您需要同步返回预处理后的数据
 *         （2）处理后的数据长度必须和处理前保持一致
 *         （3）您或者直接处理yuv_buffer，或者将处理后的数据memcpy到yuv_buffer所指的内存区域，
 *             这块内存的生命期由SDK负责管理（也就是释放）
 */
typedef void (*PVideoProcessHookFunc)(unsigned char * yuv_buffer, int len_buffer, int width, int height);
```

- **Step2. 设置 setCustomModeType + setCustomVideoPreProcessLibrary**
它们是位于PushConfig中的两个设置项：
setCustomModeType设置项用来声明“您希望自定义滤镜”，setCustomVideoPreProcessLibrary用来指定您自己的so的文件路径以及导出函数的名字。
```java
//libtest.so是step1中您自己用C/C++实现的图像处理函数库
//MyVideoProcessFunc是该so导出的函数的名字，该函数必须符合step1中的PVideoProcessHookFunc定义
int customMode |= TXLiveConstants.CUSTOM_MODE_VIDEO_PREPROCESS;
String path = this.getActivity().getApplicationInfo().dataDir + "/lib";
mLivePushConfig.setCustomModeType(customMode);
mLivePushConfig.setCustomVideoPreProcessLibrary(path +"/libtest.so", "MyVideoProcessFunc");
```

### 5. 如果您想自己加工音频数据
类似视频数据处理思路，但是具体的函数和参数名称要换成音频相关的，java层示例代码如下：
```java
customMode |= TXLiveConstants.CUSTOM_MODE_AUDIO_PREPROCESS; //可以和VIDEO_PREPROCESS一起设置
String path = this.getActivity().getApplicationInfo().dataDir + "/lib";
mLivePushConfig.setCustomModeType(customMode);
mLivePushConfig.setCustomAudioPreProcessLibrary(path +"/libtest.so", "MyAudioProcessFunc");
```
其中MyAudioProcessFunc应当遵循如下的函数声明：
```C
/* @brief 客户自定义的音频预处理函数原型
 * @param pcm_buffer：   音频PCM数据
 * @param len_buffer：   数据长度
 * @param sample_rate：  采样频率
 * @param channels：     声道数
 * @param bit_size：     采样位宽
 * @return
 * @remark （1）该函数会被SDK同步调用，故您需要同步返回预处理后的数据
 *         （2）处理后的数据长度必须和处理前保持一致
 *         （3）您或者直接处理pcm_buffer，或者将处理后的数据memcpy到pcm_buffer所指的内存区域，
 *             这块内存的生命期由SDK负责管理（也就是释放）
 */
typedef void (*PAudioProcessHookFunc)(unsigned char * pcm_buffer, int len_buffer,
                                          int sample_rate, int channels, int bit_size);
```

### 6. 如果您只用SDK来推流
也有客户只是希望拿SDK用来推流，音视频采集部分由自己的代码控制，SDK用来做音视频编码和推流就可以了。
如果是这样，您可以按如下步骤实现：

- **Step1. 设置 setCustomModeType 和相关参数**
这里需要将CustomMode设置为CUSTOM_MODE_VIDEO_CAPTURE，含义是“不需要SDK采集音视频数据”，同时还需要设置视频分辨率。
```java
// (1)将 CustomMode 设置为：自己采集视频数据，SDK只负责编码发送
int customMode |= TXLiveConstants.CUSTOM_MODE_VIDEO_CAPTURE; 
mLivePushConfig.setCustomModeType(customMode);
//
// (2)设置视频编码参数，比如720p，相比如普通模式，VIDEO_CAPTURE模式您有六种分辨率可供选择
//  VIDEO_RESOLUTION_TYPE_360_640:  pYUVBuff的分辨率必须符合360*640
//  VIDEO_RESOLUTION_TYPE_540_960:  pYUVBuff的分辨率必须符合540*960
//  VIDEO_RESOLUTION_TYPE_720_1280: pYUVBuff的分辨率必须符合720*1280
//  VIDEO_RESOLUTION_TYPE_640_360:  pYUVBuff的分辨率必须符合640*360
//  VIDEO_RESOLUTION_TYPE_960_540:  pYUVBuff的分辨率必须符合960*540
//  VIDEO_RESOLUTION_TYPE_1280_720: pYUVBuff的分辨率必须符合1280*720
mLivePushConfig.setVideoResolution(TXLiveConstants.VIDEO_RESOLUTION_TYPE_1280_720);
```

- **Step2. 使用 sendCustomYUVData 向SDK填充数据**
之后的工作就是向SDK塞入您自己准备好的视频数据（YUV420 Planar），剩下的编码和网络发送等工作交给SDK来解决。
```java
//(1)先启动推流，不然您给SDK数据它也不会处理
mLivePusher.startPusher(rtmpUrl.trim());
//
//(2)此处示例代码我们用一个线程来模拟YUV数据发送
new Thread() {
    @Override
    public void run() {
        while (true) {
            try {
                FileInputStream in = new FileInputStream("/sdcard/test_1280_720.yuv");
                int len = 1280 * 720 * 3 / 2;  //yuv格式为i420
                byte buffer[] = new byte[len];
                int count = 0;
                while ((count = in.read(buffer)) != -1) {
                    if (len == count) {
						mLivePusher.sendCustomYUVData(buffer);
					} else {
					    break;
				    }
					sleep(50, 0);
			    }
				in.close();
            }catch (Exception e) { 
                e.printStackTrace(); 
            }
         }
	   }
	}.start();
```
- **Step3. 音频也是一样的**
音频也是同样的处理思路，只是使用对应的 CustomMode 应当设置为 CUSTOM_MODE_AUDIO_CAPTURE，于此同时，您也需要指定声音采样率等和声道数等关键信息。
```java
// (1)将 CustomMode 设置为：自己采集音频数据，SDK只负责编码&发送
int customMode |= TXLiveConstants.CUSTOM_MODE_AUDIO_PREPROCESS; 
mLivePushConfig.setCustomModeType(customMode);
//
// (2)设置音频编码参数：音频采样率和声道数
mLivePushConfig.setAudioSampleRate(44100); 
mLivePushConfig.setAudioChannels(1);      
```
之后，调用**sendCustomPCMData**向SDK塞入您自己的PCM数据即可。
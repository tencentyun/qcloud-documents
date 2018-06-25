## 功能篇
腾讯视频云RTMP SDK由两部分构成：**推流器** + **播放器**，本文将主要介绍推流器的相关信息。

该SDK遵循标准RTMP视频推送协议，可以对接包括腾讯云在内的标准视频直播服务器。与此同时，SDK内部囊括了腾讯音视频团队多年的技术积累，在视频压缩、硬件加速、美颜滤镜、音频降噪、码率控制等方面都做了很多的优化处理。

如果您是一位刚刚接触视频直播的合作伙伴，您只需要几行代码就可以完成对接流程，而如果您是一位资深的移动端软件开发工程师，SDK所提供的丰富的设置接口，亦可让您能够定制出最符合需求的表现。

![rtmp sdk push](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tx_cloud_push_sdk_struct.jpg)

SDK开发包附带的推流器DEMO界面如下：

![demo](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/pusher_demo_introduction_2.jpg)

-----------------------------------------------------------------------------------------------------------------

## 基础篇
腾讯视频云RTMP SDK的使用特别简单，您只需要在您的App里添加如下几行代码就可以完成对接工作了。目前SDK内部的默认参数设置参考直播场景精心校调过的。

### step 1: 创建Pusher对象
先创建一个**LivePush**对象，它是所有SDK调用接口的承载者。
在创建LivePush对象时，还需要您指定一个**LivePushConfig**配置项，该对象在创建后即初始化了一些校调过的参数，如果您不需要自己定制这些配置，简单的alloc出来并塞给LivePush对象就可以了，如果您需要配置，可以阅读文档后半部分**定制篇**中的内容。

```objectivec   
 TXLivePushConfig* _config = [[TXLivePushConfig alloc] init];    
 //在 _config中您可以对推流的参数（如：美白，硬件加速，前后置摄像头等）做一些初始化操作，需要注意 _config不能为nil  
 _txLivePush = [[TXLivePush alloc] initWithConfig: _config];
```

### step 2: 启动推流
用下面这段代码就可以完成推流了： 

```objectivec 
NSString rtmpUrl = "rtmp://2157.livepush.myqcloud.com/live/xxxxxx";    
[_txLivePush startPreview:self.view];  //startPreview传入的控件为预览控件所在的父控件    
[_txLivePush startPush:rtmpUrl];
```

**startPush** 使用来告诉SDK视频流要推到哪个服务器地址去。
**startPreview** 则是将界面view和Push对象关联起来，从而能够将手机摄像头采集到的画面渲染到屏幕上。

> **【小细节】**
> 传进来的self.view将会作为画面渲染view的父view，建议此父view专门作为渲染使用，如果您想要在摄像头画面之上加弹幕、献花之类的UI控件，请另行创建一个与self.view平级的view，并将该view叠加在self.view之上。


### step 3: 您还可以
- **切换前置或后置摄像头** : 默认是使用**前置**摄像头（可以通过修改config配置项来修改这个默认值），调用一次switchCamera 切换一次，注意切换摄像头前必须保证 LivePushConfig 和 LivePush 对象都已经初始化。  
  
```objectivec
	// 默认是前置摄像头   
	[_txLivePush switchCamera];
```

- **打开或关闭闪光灯** : 只有后置摄像头才可以打开闪光灯（您可以通过"TXLivePush.h"里面的frontCamera成员来确认当前摄像头是前置还是后置）

```objectivec
	if(!frontCamera)
	{
	BOOL bEnable = YES;
	//bEnable为YES，打开闪光灯; bEnable为NO，关闭闪光灯
	BOOL result = [_txLivePush toggleTorch: bEnable];
	//result为YES，打开成功;result为NO，打开失败
	}
```

- **设置Logo水印** : 这里要特别说明一下，因为腾讯云支持两种方式设置水印：一种是在推流SDK进行设置，原理是在SDK内部进行视频编码前就给画面打上水印。另一种方式是在云端打水印，也就是云端对视频进行解析并添加水印Logo。

 这里我们特别建议您`使用SDK添加水印`，因为在云端打水印有三个明显的问题：
 （1）这是一种很耗机器的服务，会拉高您的费用成本；
 （2）在云端打水印对于推流期间切换分辨率等情况的兼容并不理想，会有很多花屏的问题发生。
 （3）在云端打水印会引入额外的3s以上的视频延迟，这是转码服务所引入的。

 SDK所要求的水印图片格式为png，因为png这种图片格式有透明度信息，因而能够更好地处理锯齿等问题。（您可千万别把jpg图片在windows下改个后缀名就塞进去了，专业的png图标都是需要由专业的美工设计师处理的）

```objectivec
	//设置视频水印
	_config.watermark = [UIImage imageNamed:@"watermark.png"];
	_config.watermarkPos = (CGPoint){10, 10};
```

-----------------------------------------------------------------------------------------------------------------
## 定制篇
刚才讲的是最基本的使用方法，能满足绝大部分需求。
如果您是一位资深的软件开发工程师，可能还有更专业的要求，比如您可能会关心SDK的运行状态，或者会尝试做一些视频参数的定制等等，接下来我们看一下进阶使用：
### 1. SDK内部原理
首先，您需要了解一下视频云RTMP SDK的内部原理，在推流模式下，SDK内部的状态机制如下：

![SDK内部原理](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tencent_cloud_rtmp_sdk_pusher_status_14.jpg)
### 2. 如果您关心状态
如果您关心RTMP SDK的推流状态，您可以提供一个**Listener**给刚才提到的**Pusher**对象，之后SDK的所有信息都会通过这个Listener反馈给您的App.

```objectivec
@interface PublishController ()<TXLivePushListener>
@end

[mLivePusher setDelegate:self];

#pragma - TXLivePushListener
-(void) onPushEvent:(int)EvtID WithParam:(NSDictionary*)param
{
    // here your code.
}

-(void) onNetStatus:(NSDictionary *)param
{
    // here your code.
}
```

#### 事件通知
事件通知分为**常规事件**、**警告**以及**错误通知**三个部分，详细定义如下：

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PUSH_EVT_CONNECT_SUCC            |  1001| 已经连接推流服务器|
|PUSH_EVT_PUSH_BEGIN              |  1002| 已经与服务器握手完毕,开始推流|
|PUSH_WARNING_NET_BUSY            |  1101| 网络状况不佳：上行带宽太小，上传数据受阻|
|PUSH_WARNING_RECONNECT           |  1102| 网络断连, 已启动自动重连 (自动重连连续失败超过三次会放弃)|
|PUSH_WARNING_HW_ACCELERATION_FAIL|  1103| 硬编码启动失败，采用软编码|
|PUSH_WARNING_DNS_FAIL			  |  3001 |  RTMP -DNS解析失败        |
|PUSH_WARNING_SEVER_CONN_FAIL     |  3002|  RTMP服务器连接失败  |
|PUSH_WARNING_SHAKE_FAIL          |  3003|  RTMP服务器握手失败  |
|PUSH_ERR_OPEN_CAMERA_FAIL        | -1301| 打开摄像头失败|
|PUSH_ERR_OPEN_MIC_FAIL           | -1302| 打开麦克风失败|
|PUSH_ERR_VIDEO_ENCODE_FAIL       | -1303| 视频编码失败|
|PUSH_ERR_AUDIO_ENCODE_FAIL       | -1304| 音频编码失败|
|PUSH_ERR_UNSUPPORTED_RESOLUTION  | -1305| 不支持的视频分辨率|
|PUSH_ERR_UNSUPPORTED_SAMPLERATE  | -1306| 不支持的音频采样率|
|PUSH_ERR_NET_DISCONNECT          | -1307| 网络断连,且经三次抢救无效,可以放弃治疗,更多重试请自行重启推流|


详细的定义请参阅头文件**“TXLiveSDKTypeDef.h”**，网络状态回调 onNetStatus 中各参数的含义已经在注释中有明确的说明，此处不再赘述


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
| audioSampleRate|   音频采样率：录音设备在一秒钟内对声音信号的采集次数   |  44100   |  
| enableNAS          |   噪声抑制：开启后可以滤掉背景杂音                   |  开启     |
| enableHWAcceleration|   视频硬编码：开启后最高可支持720p， 30fps视频采集   |  开启   |  
| videoFPS     |   视频帧率：即视频编码器每秒生产出多少帧画面           |  20      |
| videoResolution|   视频分辨率：目前提供四种16：9分辨率可供您选择      |  640 * 360 |
| videoBitratePIN |   视频比特率：即视频编码器每秒生产出多少数据，单位 kbps |  800|
| enableAutoBitrate |   带宽自适应：该功能会根据当前网络情况，自动调整视频比特率 |   关闭|
| videoBitrateMax| 最大输出码率：只有开启自适应码率, 该设置项才能启作用 |   1200|
| videoBitrateMin| 最小输出码率：只有开启自适应码率, 该设置项才能启作用 |   800|
| homeOrientation| 设置视频图像旋转角度，因为手机一般默认是横屏采集视频画面  |   90   |
| beautyFilterDepth| 美颜级别：支持1~9 共9个级别，级别越高，效果越明显。0表示关闭  |   关闭   |
| frontCamera | 默认是前置还是后置摄像头 | 前置 |
| watermark | 水印图片（UIImage对象） | 腾讯云Logo（demo）  |    
| watermarkPos | 水印图片相对左上角坐标的位置 | （0, 0）  |                                                                        

这些参数的设置推荐您在启动推流之前就指定，因为大部分设置项是在重新推流之后才能生效的。参考代码如下：

```objectivec
//成员变量中声明 _config 和 _pusher
....
//初始化 _config
_config = [[TXLivePushConfig alloc] init];

// 修改参数设置为声音44100采样率，视频800固定码率
_config.audioSampleRate = 44100;
_config.enableAutoBitrate = NO;
_config.videoBitratePIN = 800;

//初始化 _pusher
_pusher = [[TXLivePush alloc] initWithConfig: _config];
```












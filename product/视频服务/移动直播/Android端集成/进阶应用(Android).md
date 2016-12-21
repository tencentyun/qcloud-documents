## 1. 推流原理
腾讯云 RTMP SDK 内部状态机原理如下图所示：
- **Step1 - 调用的起点：**TXLivePush 对象的 startPush 被调用后，推流的流程便会开始启动。

- **step2 - 连接服务器：**推流的第一步是尝试连接推流服务器，如果失败会抛出 NET_DISCONNECT 错误而不会继续执行后续流程。

- **step3 - 开始推流了：**PUSH_EVT_PUSH_BEGIN 是真正推流开始的标志，很多客户误认为调用了 startPush 就成功开始推流了，其实不然。

- **step4 - 推流主循环：**直播推流是一个持续的过程，受 SDK 内部一个主循环引擎的驱动，只有在用 stopPush 主动停止或者遭遇不可恢复的错误时才会跳出主循环。

![SDK内部原理](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tencent_cloud_rtmp_sdk_pusher_status_14.jpg)

## 2. 质量监控
RTMP SDK 在设计之初就尽量避免过于封闭，让您觉得 SDK 完全是个黑盒是我们所不希望看到的情况，所以我们提供了一种**状态反馈机制**：每1-2秒就会将内部各种状态参数反馈出来。

![](//mc.qcloudimg.com/static/img/48fd46af4e17b0299fd00a0e661a16f0/image.png)

您要做的就是提供一个 **TXLivePushListener** 监听器给 TXLivePusher 对象，RTMP SDK 会通过 onNetStatus 回调将所有内部状态全部通知出去。
  
|  推流状态                   |  含义说明                    |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE     |当前进程的CPU使用率和本机总体的CPU使用率|
| NET_STATUS_VIDEO_WIDTH  |当前视频的宽度（单位：像素值）    |
| NET_STATUS_VIDEO_HEIGHT|当前视频的高度（单位：像素值）    |
|	NET_STATUS_NET_SPEED     | 当前的发送速度（单位：kbps）|
|	NET_STATUS_VIDEO_BITRATE | 当前视频编码器输出的比特率，也就是编码器每秒生产了多少视频数据，单位： kbps|
|	NET_STATUS_AUDIO_BITRATE | 当前音频编码器输出的比特率，也就是编码器每秒生产了多少音频数据，单位： kbps|
|	NET_STATUS_VIDEO_FPS     | 当前视频帧率，也就是视频编码器每条生产了多少帧画面|
|	NET_STATUS_CACHE_SIZE    | 音视频数据堆积情况，这个数字超过个位数，即说明当前上行带宽不足以消费掉已经生产的音视频数据|
|	NET_STATUS_CODEC_DROP_CNT  |全局丢包次数，为了避免延迟持续恶性堆积，SDK在数据积压超过警戒线以后会主动丢包，丢包次数越多，说明网络问题越严重。|
| NET_STATUS_SERVER_IP     | 连接的推流服务器的IP |
|	NET_STATUS_NET_JITTER    | 网络抖动情况（指导作用很小，不推荐参考）|

### 2.1 推流质量的判断
有了上面这些状态信息，但怎么判断推流质量是否OK呢？下面几条是我们常用的质量判断指标，<font color='red'>**强烈推荐您了解一下**</font>：

**1. BITRATE 与 NET_SPEED 的关系**
>BITRATE( = VIDEO_BITRATE + AUDIO_BITRATE ) 指的是编码器每秒产生了多少音视频数据要推出去，NET_SPEED 指的是每秒钟实际推出了多少数据，所以如果 BITRATE == NET_SPEED 的情况是常态，则推流质量会非常良好；
>
>而如果 BITRATE >= NET_SPEED 这种情况的持续时间比较长，推流质量就很难有什么保障。

**2. CACHE_SIZE 和 DROP_CNT 的数值**
>BITRATE >= NET_SPEED 的情况一旦出现，编码器产生的音视频数据就会在主播的手机上积压起来，积压的严重程度以 CACHE_SIZE 这个状态值展示出来，如果 CACHE_SIZE 超过警戒线，SDK 会主动丢弃一些音视频数据，从而触发 DROP_CNT 的增长。
>
>如果 CACHE_SIZE 大小持续超过个位数，或者 DROP_CNT 有增加，都说明主播的网络质量不 OK，推流质量难保证。
>
>下图所示就是一个典型的<font color='blue'>上行带宽不足导致观众端反馈持续卡顿</font>的经典案例：
>![](//mc.qcloudimg.com/static/img/319d6197da603ca15ffc6e2afd778e48/image.png)

**3. CPU_USAGE 的大小** 
>普通场景下，RTMP SDK 在各个平台的推流 CPU 使用率均会要求保持在 50% 一下，尤其是在开启硬件编码的情况下。比如在小米3这款机型上，开启硬件加速后，720p超清画质推流也不过30%的CPU使用率。
>
>然而，一个直播APP中使用CPU的不可能只有RTMP SDK，弹幕、飘星、文本消息互动等等，都有可能会消耗一定的CPU，这些都是不可避免的。
>
>但是，如果系统的整体CPU使用率超过 80%，那么视频的采集和编码都有可能会有影响；如果CPU使用率达到 100%，那么主播端本身就已经卡的一塌糊涂了，观众端要有流畅的观看体验显然是不可能的。

**4. SERVER_IP 的 ping 值**
>如果主播到 SERVER_IP 给出的 ip 地址的 ping 值很高（比如超过 500ms），那么推流质量一定无法保障。**就近接入**是我们腾讯云应该做好的事情，如您发现有这样的案例，请反馈给我们，我们的运维团队会持续调整和优化之。

### 2.2 SDK推流质量专区

您在 2.1 中所看到的图表是源于我们实验测试用的内部数据分析系统，如果您有同样的分析需求，可以在[直播控制台](https://console.qcloud.com/live)的质量监控系统里看到类似的图表，这里的图表的格式更加简明，对其理解不需要太多专业的音视频基础知识。
![](//mc.qcloudimg.com/static/img/4bf231da79ec8e45bdc4c16c927da47f/image.png)

## 3. 参数校调
如果您希望定制视频编码参数，音频编码参数等等，您可以通过设置Config对象实现您的自定义需求，目前我们支持的setting接口如下：

| 参数名           |    含义                                          |   默认值  | 
| :-------------- | :-----------------------------------------------| :------: |
| setAudioSampleRate|   音频采样率：录音设备在一秒钟内对声音信号的采集次数   |  44100   |  
| setANS          |   噪声抑制：开启后可以滤掉背景杂音（32000以下采样率有效） |  关闭     |
| setHardwareAcceleration|   视频硬编码：开启后最高可支持720p， 30fps视频采集   |  开启   |  
| setVideoFPS     |   视频帧率：即视频编码器每秒生产出多少帧画面，注意由于大部分机器性能不足以支持30FPS以上的编码，推荐您设置FPS为20           |  20      |
| setVideoResolution|   视频分辨率：目前提供四种16：9分辨率可供您选择      |  640 * 360 |
| setVideoBitrate |   视频比特率：即视频编码器每秒生产出多少数据，单位 kbps |  800|
| setAutoAdjustBitrate   |   带宽自适应：该功能会根据当前网络情况，自动调整视频比特率 |   关闭|
| setAutoAdjustStrategy |   如果开启带宽自适应，可以通过该接口设置动态调整码率的策略 |   STRATEGY_1 |
| setMaxVideoBitrate| 最大输出码率：只有开启自适应码率, 该设置项才能启作用 |   1200|
| setMinVideoBitrate| 最小输出码率：只有开启自适应码率, 该设置项才能启作用 |   800|
| setVideoEncodeGop | 关键帧间隔（单位：秒）即多少秒出一个I帧 | 3s |
| setHomeOrientation| 设置视频图像旋转角度，比如是否要横屏推流  |   home在右边（0）home在下面（1）home在左面（2）home在上面（3）   |
| setBeautyFilter| 美颜级别：支持1~9 共9个级别，级别越高，效果越明显。0表示关闭  |   关闭   |
| setFrontCamera | 默认是前置还是后置摄像头 | 前置 |
| setWatermark | 水印图片（UIImage对象） | 腾讯云Logo（demo）  |    
| setTouchFocus| 是否开启手动对焦| 开启 |
| setPauseImg | 设置后台推流时垫片用的图片 | Demo中打包的一张资源图片 | 

这些参数的设置推荐您在启动推流之前就指定，因为大部分设置项是在重新推流之后才能生效的。参考代码如下：

```java
//成员变量中声明 _config 和 _pusher
....
//初始化 _config
mLivePushConfig = new TXLivePushConfig();

// 修改参数设置为声音44100采样率，视频800固定码率
mLivePushConfig.setAudioSampleRate(44100);
mLivePushConfig.setAutoAdjustBitrate(false);
mLivePushConfig.setVideoBitrate(800);

mLivePusher.setConfig(mLivePushConfig);
```

## 4. 智能控速
### 4.1 背景说明
RTMP 推流质量对于观看体验非常关键，因为如果主播的推流质量不佳，那么所有观众看到的视频画面都是卡顿的，据统计，视频云客户群 80% 以上的直播间卡顿问题均是由于 RTMP 推流质量不佳导致的。

![](//mc.qcloudimg.com/static/img/4bf231da79ec8e45bdc4c16c927da47f/image.png)

在众多的推流质量问题中，主播的上行网络不给力引发的问题又是最主要的，上行带宽不足会导致音视频数据在主播端堆积并丢弃，从而使观众端看到的视频画面出现卡顿甚至长时间卡死。

所以，优化主播上行卡顿问题能够有效地提升推流质量，进而提升观看端的质量，尤其在国内运营商普遍限制上行带宽的情况下。

但是网络问题不随人的意志为转移，主播家里买的 4Mbps 宽带套餐，不可能因为主播装一个 App 就让其变成 8Mbps，因此，我们只能采用顺势而为的做法 —— **主动适应上行网络的情况**。


### 4.2 可选方案
1.7.0 版本开始，RTMP SDK 提供了针对三种场景的推荐方案：

#### 【秀场直播】
- **场景特点**
秀场模式的分辨率一般采用  360\*640 的分辨率， 码率上相应的采用 800kbps ，该模式下我们一般更关注画面清晰度和声音流畅度。如果主播的网络遭遇波动，主动降低画质来确保流畅性未必是我们追求的效果。

 因为秀场模式的码率本来就不高，这个时候压低码率的收益非常有限，码率降得少了没什么实质性改善，码率降得多了，就必然会引入区域性的马赛克，同时会大幅牺牲画面色彩的丰富度。

- **流控方案**
针对上述场景特点，我们**推荐不要做流控**，当主播的网络遭遇波动时，RTMP SDK 会通过 **PUSH_WARNING_NET_BUSY** 事件通知给您的App。这个时候建议您通过 UI 上的提示，提醒一下主播自己现在接入的WiFi不太给力，是不是考虑坐的离路由器近一点？
```
mLivePushConfig.setVideoBitrate(700);  // 700kbps
mLivePushConfig.setAutoAdjustBitrate(false);   //固定码率推流
mLivePushConfig.setVideoResolution(VIDEO_RESOLUTION_TYPE_360_640); //设置推流分辨率
```

#### 【手游直播】
- **场景特点**
跟秀场模式不同，手游直播场景下的分辨率和码率都比较高，比如 540p 甚至 720p 的分辨率是非常常见的，码率也一般在 1.5Mbps 以上，有些画面变化幅度比较大的游戏（比如 TempleRun）的甚至要2.5Mbps以上的上行带宽才能扛得住。

 于此同时，手游直播的主播一般都更加职业和专注，倾向于会选择网络较好的场景进行长时间的直播，期间网络波动的情况更多的是偶发性的临时波动。

- **流控方案**
针对上述场景特点，我们推荐采用 **AUTO_ADJUST_BITRATE_STRATEGY_2** 策略自动调整码率，该方案的特点是快速探测，快速调整，比较适合大码率的手游直播场景。
```java
TXLivePushConfig* _config;
mLivePushConfig.setMinVideoBitrate(500);//动态调整的最小码率
mLivePushConfig.setMaxVideoBitrate(1000);//动态调整的最大码率
mLivePushConfig.setVideoBitrate(800);//刚开始进入的默认码率
mLivePushConfig.setAutoAdjustBitrate(true);//是否开启动态调整码率
mLivePushConfig.setAutoAdjustStrategy(AUTO_ADJUST_BITRATE_STRATEGY_2);
mLivePushConfig.setVideoResolution(VIDEO_RESOLUTION_TYPE_360_640);//默认分辨率 
```

- **进阶应用**
每一数值的码率都有最适合的分辨率与之搭配，比如 600kbps 的码率配合 360p 的分辨率，不管是颜色还是清晰度都是挺不错的，但如果 600kbps 的码率要配合 720p 的分辨率，画面就会大大缩水，这是由于视频编码率通常要牺牲更多的画质来换取更高的分辨率。

 基于这个原因，在 720p 的分辨率场景下，如果简单的将码率从 1.5Mbps 降低到 500kbps，后果就是运动画面下的(720p - 500kbps) 的马赛克要远多于(360p - 500kbps) 。

 所以，对于高清场景的游戏推流，我们更推荐采用 **AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_2** ，它会在降低码率的同时，相应的调整分辨率，以保持码率和分辨率之间的最佳平衡点。
```java
TXLivePushConfig* _config;
mLivePushConfig.setMinVideoBitrate(800);//动态调整的最小码率
mLivePushConfig.setMaxVideoBitrate(3000);//动态调整的最大码率
mLivePushConfig.setVideoBitrate(1800);//刚开始进入的默认码率
mLivePushConfig.setAutoAdjustBitrate(true);//是否开启动态调整码率
mLivePushConfig.setAutoAdjustStrategy(AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_2);
mLivePushConfig.setVideoResolution(VIDEO_RESOLUTION_TYPE_720_1280);//默认分辨率 
```
 
#### 【移动场景】
- **场景特点**
移动场景是个很宽泛的概念，我们团队将带宽不稳定的场景统称为移动场景，该场景下，主播的上行网络会经常发生变动，这一段时间可能是1Mbps， 下一段时间可能就变成 300kbps了。

- **流控方案**
针对这种场景，我们推荐采用 **AUTO_ADJUST_BITRATE_STRATEGY_1**，该策略模式下会尽量让带宽跟着网络情况持续做适应性调整。带来的收益就是在带宽不稳定的情况下推流质量会灵活应对，当然，这也有代价，那就是当网络稳定的情况下，推流码率也会“很不安分”，相比于固定码率会带来更多的波动。
```java
TXLivePushConfig* _config;
mLivePushConfig.setMinVideoBitrate(500);//动态调整的最小码率
mLivePushConfig.setMaxVideoBitrate(1000);//动态调整的最大码率
mLivePushConfig.setVideoBitrate(800);//刚开始进入的默认码率
mLivePushConfig.setAutoAdjustBitrate(true);//是否开启动态调整码率
mLivePushConfig.setAutoAdjustStrategy(AUTO_ADJUST_BITRATE_STRATEGY_1);
mLivePushConfig.setVideoResolution(VIDEO_RESOLUTION_TYPE_360_640);//默认分辨率 
```

## 5. 替换数据源
### 5.1 如果您想加工视频数据
有些研发能力比较强的客户，会有自定义图像处理的需求（比如堆加字幕），同时又希望复用rtmp sdk的整体流程，如果是这样，您可以按照如下攻略进行定制。

```objectivec
//（1）设置CustomMode为 CUSTOM_MODE_VIDEO_PREPROCESS
_config.customModeType |= CUSTOM_MODE_VIDEO_PREPROCESS;
//
//（2）设置自定义视频数据的函数 MyHookVideoFunc
_config.pVideoFuncPtr = MyHookVideoFunc;
```

这里的pVideoFuncPtr是一个函数指针，在您指定了CustomMode为VIDEO_PREPROCESS之后，SDK不会再自己对采集到的视频做预处理，而是转而调用传给他的YUV处理函数（示例代码中的MyHookVideoFunc），其中pVideoFuncPtr应当遵循如下的函数声明：
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

> 您的预处理函数，MyHookVideoFunc的处理时间不能过长，试想，如果该函数的处理时间超过50ms，那就意味着SDK推出的视频流，其帧率不可能达到20FPS。

### 5.2 如果您想加工音频数据
类似视频数据处理，但是具体的名称要换成音频相关的。
```objectivec
//（1）设置CustomMode为 CUSTOM_MODE_AUDIO_PREPROCESS
_config.customModeType |= CUSTOM_MODE_AUDIO_PREPROCESS;
//
//（2）设置自定义视频数据的函数 MyHookAudioFunc
_config.pAudioFuncPtr = MyHookAudioFunc;
```
其中pAudioFuncPtr应当遵循如下的函数声明：
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

### 5.3 如果您只是用SDK来推流
也有客户只是希望拿SDK用来推流，音视频采集部分由自己的代码控制，SDK用来做音视频编码和推流就可以了。
如果是这样，您可以按如下步骤实现：

- **Step1. 设置 setCustomModeType 和相关参数**
这里需要将CustomMode设置为CUSTOM_MODE_VIDEO_CAPTURE，含义是“不需要SDK采集音视频数据”，同时还需要设置视频分辨率。
```
// (1)将 CustomMode 设置为：自己采集视频数据，SDK只负责编码发送
_config.customModeType |= CUSTOM_MODE_VIDEO_CAPTURE;
//
// (2)设置视频编码输出分辨率，VIDEO_CAPTURE模式您有六种分辨率可供选择
//  VIDEO_RESOLUTION_TYPE_360_640:  pYUVBuff的分辨率必须符合360*640
//  VIDEO_RESOLUTION_TYPE_540_960:  pYUVBuff的分辨率必须符合540*960
//  VIDEO_RESOLUTION_TYPE_720_1280: pYUVBuff的分辨率必须符合720*1280
//  VIDEO_RESOLUTION_TYPE_640_360:  pYUVBuff的分辨率必须符合640*360
//  VIDEO_RESOLUTION_TYPE_960_540:  pYUVBuff的分辨率必须符合960*540
//  VIDEO_RESOLUTION_TYPE_1280_720: pYUVBuff的分辨率必须符合1280*720
_config.videoResolution = VIDEO_RESOLUTION_TYPE_1280_720;
```

- **Step2. 使用 sendCustomVideoData 向SDK填充Video数据**
之后的工作就是向SDK塞入您自己准备好的视频数据（目前支持的格式为：420SP、420YpCbCr、420P、BGRA8888、RGBA8888、NV12），剩下的编码和网络发送等工作交给SDK来解决。
```
//(1)先启动推流，注意不再要startPreview或者startScreenCapture
[_txLivePublisher startPush:rtmpUrl]
//
//(2)此处示例代码简单描述怎么向SDK塞入您自己的YUV数据
[_txLivePublisher sendCustomVideoData: buffer dataLen:len 
          videoType:VIDEO_TYPE_420P width:720 height:1280];
```

- **Step3. 使用 sendCustomPCMData 向SDK填充Audio数据**
在视频改用外部采集的情况下，音频还可以继续由SDK内部采集处理，如果你希望把音频的采集也替换成自己的逻辑，需要为 CustomMode 设置项追加 CUSTOM_MODE_AUDIO_CAPTURE，于此同时，您也需要指定声音采样率等和声道数等关键信息。
```java
// (1)将 CustomMode 设置为：自己采集音频数据，SDK只负责编码&发送
_config.customModeType |= CUSTOM_MODE_AUDIO_CAPTURE;
//
// (2)设置音频编码参数：音频采样率和声道数
_config.audioSampleRate = 44100;
_config.audioChannels   = 1;
```
之后，调用**sendCustomPCMData**向SDK塞入您自己的PCM数据即可。

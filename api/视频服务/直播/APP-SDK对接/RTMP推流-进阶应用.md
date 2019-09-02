
>!为了减少文档篇幅，同时由于RTMP SDK 在两个平台的接口相似度极高，所以本文中所有示例代码仅给出 Objective-C 的版本。

## 1. RTMP SDK 推流原理
腾讯云 RTMP SDK 内部状态机原理如下图所示：
- **Step1 - 调用的起点：**TXLivePush 对象的 startPush 被调用后，推流的流程便会开始启动。

- **step2 - 连接服务器：**推流的第一步是尝试连接推流服务器，如果失败会抛出 NET_DISCONNECT 错误而不会继续执行后续流程。

- **step3 - 开始推流了：**PUSH_EVT_PUSH_BEGIN 是真正推流开始的标志，很多客户误认为调用了 startPush 就成功开始推流了，其实不然。

- **step4 - 推流主循环：**直播推流是一个持续的过程，受 SDK 内部一个主循环引擎的驱动，只有在用 stopPush 主动停止或者遭遇不可恢复的错误时才会跳出主循环。

![SDK内部原理](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tencent_cloud_rtmp_sdk_pusher_status_14.jpg)

## 2. 了解 SDK 推流质量
RTMP SDK 在设计之初就尽量避免过于封闭，让您觉得 SDK 完全是个黑盒是我们所不希望看到的情况，所以我们提供了一种**状态反馈机制**：每1秒 - 2秒就会将内部各种状态参数反馈出来。

![](//mc.qcloudimg.com/static/img/48fd46af4e17b0299fd00a0e661a16f0/image.png)

您要做的就是提供一个 **TXLivePushListener** 监听器给 TXLivePush 对象，RTMP SDK 会通过 onNetStatus 回调将所有内部状态全部通知出去。
  
|  推流状态                   |  含义说明                    |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE     |当前进程的 CPU 使用率和本机总体的 CPU 使用率|
| NET_STATUS_VIDEO_WIDTH  |当前视频的宽度（单位：像素值）    |
| NET_STATUS_VIDEO_HEIGHT|当前视频的高度（单位：像素值）    |
|	NET_STATUS_NET_SPEED     | 当前的发送速度（单位：kbps）|
|	NET_STATUS_VIDEO_BITRATE | 当前视频编码器输出的比特率，也就是编码器每秒生产了多少视频数据，单位： kbps|
|	NET_STATUS_AUDIO_BITRATE | 当前音频编码器输出的比特率，也就是编码器每秒生产了多少音频数据，单位： kbps|
|	NET_STATUS_VIDEO_FPS     | 当前视频帧率，也就是视频编码器每条生产了多少帧画面|
|	NET_STATUS_CACHE_SIZE    | 音视频数据堆积情况，这个数字超过个位数，即说明当前上行带宽不足以消费掉已经生产的音视频数据|
|	NET_STATUS_CODEC_DROP_CNT  |全局丢包次数，为了避免延迟持续恶性堆积，SDK 在数据积压超过警戒线以后会主动丢包，丢包次数越多，说明网络问题越严重。|
| NET_STATUS_SERVER_IP     | 连接的推流服务器的 IP |
|	NET_STATUS_NET_JITTER    | 网络抖动情况（指导作用很小，不推荐参考）|

### 2.1 推流质量的判断
有了上面这些状态信息，但怎么判断推流质量是否OK呢？下面几条是我们常用的质量判断指标，**强烈推荐您了解一下**：

**1. BITRATE 与 NET_SPEED 的关系**
>BITRATE（ = VIDEO_BITRATE + AUDIO_BITRATE）指的是编码器每秒产生了多少音视频数据要推出去，NET_SPEED 指的是每秒钟实际推出了多少数据，所以如果 BITRATE == NET_SPEED 的情况是常态，则推流质量会非常良好；
>
>而如果 BITRATE >= NET_SPEED 这种情况的持续时间比较长，推流质量就很难有什么保障。

**2. CACHE_SIZE 和 DROP_CNT 的数值**
>BITRATE >= NET_SPEED 的情况一旦出现，编码器产生的音视频数据就会在主播的手机上积压起来，积压的严重程度以 CACHE_SIZE 这个状态值展示出来，如果 CACHE_SIZE 超过警戒线，SDK 会主动丢弃一些音视频数据，从而触发 DROP_CNT 的增长。
>
>如果 CACHE_SIZE 大小持续超过个位数，或者 DROP_CNT 有增加，都说明主播的网络质量不 OK，推流质量难保证。
>
>下图所示就是一个典型的**上行带宽不足导致观众端反馈持续卡顿**的经典案例：
>![](//mc.qcloudimg.com/static/img/319d6197da603ca15ffc6e2afd778e48/image.png)

**3. CPU_USAGE 的大小** 
>普通场景下，RTMP SDK 在各个平台的推流 CPU 使用率均会要求保持在50%以下，尤其是在开启硬件编码的情况下。例如，在小米3这款机型上，开启硬件加速后，720p超清画质推流也不过30%的 CPU 使用率。
>
>然而，一个直播 App 中使用 CPU 的不可能只有 RTMP SDK，弹幕、飘星、文本消息互动等等，都有可能会消耗一定的 CPU，这些都是不可避免的。
>
>但是，如果系统的整体 CPU 使用率超过 80%，那么视频的采集和编码都有可能会有影响；如果 CP U使用率达到 100%，那么主播端本身就已经卡的一塌糊涂了，观众端要有流畅的观看体验显然是不可能的。

**4. SERVER_IP 的 ping 值**
>如果主播到 SERVER_IP 给出的 IP 地址的 ping 值很高（例如超过 500ms），那么推流质量一定无法保障。**就近接入**是我们腾讯云应该做好的事情，如您发现有这样的案例，请反馈给我们，我们的运维团队会持续调整和优化之。

### 2.2 SDK推流质量专区

您在**2.1**中所看到的图表是源于我们实验测试用的内部数据分析系统，如果您有同样的分析需求，可以在 [云直播控制台](https://console.cloud.tencent.com/live) 的质量监控系统里看到类似的图表，这里的图表的格式更加简明，对其理解不需要太多专业的音视频基础知识。
![](//mc.qcloudimg.com/static/img/4bf231da79ec8e45bdc4c16c927da47f/image.png)

## 3. 校调推流参数
如果您希望定制视频编码参数，音频编码参数等等，您可以通过设置 Config 对象实现您的自定义需求，目前我们支持的 setting 接口如下：

| 参数名           |    含义                                          |   默认值  | 
| :-------------- | :-----------------------------------------------| :------: |
| audioSampleRate|   音频采样率：录音设备在一秒钟内对声音信号的采集次数   |  44100   |  
| enableNAS          |   噪声抑制：开启后可以滤掉背景杂音（32000以下采样率有效） |  关闭     |
| enableHWAcceleration|   视频硬编码：开启后最高可支持720p， 30fps视频采集   |  开启   |  
| videoFPS     |   视频帧率：即视频编码器每秒生产出多少帧画面，注意由于大部分机器性能不足以支持30FPS以上的编码，推荐您设置FPS为20           |  20      |
| videoResolution|   视频分辨率：目前提供四种16：9分辨率可供您选择      |  640 * 360 |
| videoBitratePIN |   视频比特率：即视频编码器每秒生产出多少数据，单位 kbps |  800|
| enableAutoBitrate |   带宽自适应：该功能会根据当前网络情况，自动调整视频比特率 |   关闭|
| videoBitrateMax| 最大输出码率：只有开启自适应码率, 该设置项才能启作用 |   1200|
| videoBitrateMin| 最小输出码率：只有开启自适应码率, 该设置项才能启作用 |   800|
| videoEncodeGop | 关键帧间隔（单位：秒）即多少秒出一个I帧 | 3s |
| homeOrientation| 设置视频图像旋转角度，例如是否要横屏推流  |   home在右边（0）home在下面（1）home在左面（2）home在上面（3）   |
| beautyFilterDepth| 美颜级别：支持1~9 共9个级别，级别越高，效果越明显。0表示关闭  |   关闭   |
| frontCamera | 默认是前置还是后置摄像头 | 前置 |
| watermark | 水印图片（UIImage 对象） | 腾讯云 Logo（demo）  |    
| watermarkPos | 水印图片相对左上角坐标的位置 | （0，0）  |                                                                        

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

## 4. 如果您想加工视频数据
有些研发能力比较强的客户，会有自定义图像处理的需求（例如堆加字幕），同时又希望复用 RTMP SDK 的整体流程，如果是这样，您可以按照如下攻略进行定制。

```objectivec
//（1）设置CustomMode为 CUSTOM_MODE_VIDEO_PREPROCESS
_config.customModeType |= CUSTOM_MODE_VIDEO_PREPROCESS;
//
//（2）设置自定义视频数据的函数 MyHookVideoFunc
_config.pVideoFuncPtr = MyHookVideoFunc;
```

这里的 pVideoFuncPtr 是一个函数指针，在您指定了 CustomMode为VIDEO_PREPROCESS 之后，SDK 不会再自己对采集到的视频做预处理，而是转而调用传给他的 YUV 处理函数（示例代码中的MyHookVideoFunc），其中 pVideoFuncPtr 应当遵循如下的函数声明：
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

> 您的预处理函数，MyHookVideoFunc 的处理时间不能过长，试想，如果该函数的处理时间超过50ms，那就意味着 SDK 推出的视频流，其帧率不可能达到20FPS。

## 5. 如果您想加工音频数据
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

## 6. 如果您只用 SDK 来推流
也有客户只是希望拿 SDK 用来推流，音视频采集部分由自己的代码控制，SDK 用来做音视频编码和推流就可以了。
如果是这样，您可以按如下步骤实现：

- **Step1. 设置 setCustomModeType 和相关参数**
这里需要将 CustomMode 设置为 CUSTOM_MODE_VIDEO_CAPTURE，含义是“不需要 SDK 采集音视频数据”，同时还需要设置视频分辨率。
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

- **Step2. 使用 sendCustomVideoData 向 SDK 填充 Video 数据**
之后的工作就是向 SDK 塞入您自己准备好的视频数据（目前支持的格式为：420SP、420YpCbCr、420P、BGRA8888、RGBA8888、NV12），剩下的编码和网络发送等工作交给 SDK 来解决。
```
//(1)先启动推流，注意不再要startPreview或者startScreenCapture
[_txLivePublisher startPush:rtmpUrl]
//
//(2)此处示例代码简单描述怎么向SDK塞入您自己的YUV数据
[_txLivePublisher sendCustomVideoData: buffer dataLen:len 
          videoType:VIDEO_TYPE_420P width:720 height:1280];
```

- **Step3. 使用 sendCustomPCMData 向 SDK 填充 Audio 数据**
在视频改用外部采集的情况下，音频还可以继续由 SDK 内部采集处理，如果您希望把音频的采集也替换成自己的逻辑，需要为 CustomMode 设置项追加 CUSTOM_MODE_AUDIO_CAPTURE，于此同时，您也需要指定声音采样率等和声道数等关键信息。
```java
// (1)将 CustomMode 设置为：自己采集音频数据，SDK只负责编码&发送
_config.customModeType |= CUSTOM_MODE_AUDIO_CAPTURE;
//
// (2)设置音频编码参数：音频采样率和声道数
_config.audioSampleRate = 44100;
_config.audioChannels   = 1;
```
之后，调用**sendCustomPCMData**向 SDK 塞入您自己的 PCM 数据即可。

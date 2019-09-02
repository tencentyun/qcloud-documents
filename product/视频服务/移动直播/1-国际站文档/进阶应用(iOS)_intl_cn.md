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

您要做的就是提供一个 **TXLivePushListener** 监听器给 TXLivePush 对象，RTMP SDK 会通过 onNetStatus 回调将所有内部状态全部通知出去。
  
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

您在 2.1 中所看到的图表是源于我们实验测试用的内部数据分析系统，如果您有同样的分析需求，可以在[直播控制台](https://console.cloud.tencent.com/live)的质量监控系统里看到类似的图表，这里的图表的格式更加简明，对其理解不需要太多专业的音视频基础知识。
![](//mc.qcloudimg.com/static/img/4bf231da79ec8e45bdc4c16c927da47f/image.png)

## 3. 参数校调
如果您希望定制视频编码参数，音频编码参数等等，您可以通过设置Config对象实现您的自定义需求，目前我们支持的setting接口如下：

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
| homeOrientation| 设置视频图像旋转角度，比如是否要横屏推流  |   home在右边（0）home在下面（1）home在左面（2）home在上面（3）   |
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
TXLivePushConfig* _config;
_config.videoBitratePIN	  = 700;  // 700kbps
_config.enableAutoBitrate = NO;   //固定码率推流
_config.videoResolution   = VIDEO_RESOLUTION_TYPE_360_640;//设置推流分辨率
```

#### 【手游直播】
- **场景特点**
跟秀场模式不同，手游直播场景下的分辨率和码率都比较高，比如 540p 甚至 720p 的分辨率是非常常见的，码率也一般在 1.5Mbps 以上，有些画面变化幅度比较大的游戏（比如 TempleRun）的甚至要2.5Mbps以上的上行带宽才能扛得住。

 于此同时，手游直播的主播一般都更加职业和专注，倾向于会选择网络较好的场景进行长时间的直播，期间网络波动的情况更多的是偶发性的临时波动。

- **流控方案**
针对上述场景特点，我们推荐采用 **AUTO_ADJUST_BITRATE_STRATEGY_2** 策略自动调整码率，该方案的特点是快速探测，快速调整，比较适合大码率的手游直播场景。
```
TXLivePushConfig* _config;
_config.videoBitrateMin   = 500;//动态调整的最小码率
_config.videoBitrateMax   = 1000;//动态调整的最大码率
_config.videoBitratePIN   = 800;//刚开始进入的默认码率
_config.enableAutoBitrate = YES;//是否开启动态调整码率
_config.videoResolution   = VIDEO_RESOLUTION_TYPE_360_640;//默认分辨率 
_config.autoAdjustStrategy= AUTO_ADJUST_BITRATE_STRATEGY_2;
```

- **进阶应用**
每一数值的码率都有最适合的分辨率与之搭配，比如 600kbps 的码率配合 360p 的分辨率，不管是颜色还是清晰度都是挺不错的，但如果 600kbps 的码率要配合 720p 的分辨率，画面就会大大缩水，这是由于视频编码率通常要牺牲更多的画质来换取更高的分辨率。

 基于这个原因，在 720p 的分辨率场景下，如果简单的将码率从 1.5Mbps 降低到 500kbps，后果就是运动画面下的(720p - 500kbps) 的马赛克要远多于(360p - 500kbps) 。

 所以，对于高清场景的游戏推流，我们更推荐采用 **AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_2** ，它会在降低码率的同时，相应的调整分辨率，以保持码率和分辨率之间的最佳平衡点。
 ```
 TXLivePushConfig* _config;
 _config.videoBitrateMin      = 800;//动态调整的最小码率
 _config.videoBitrateMax      = 3000;//动态调整的最大码率
 _config.videoBitratePIN      = 1800;//刚开始进入的默认码率
 _config.enableAutoBitrate    = YES;//是否开启动态调整码率
 _config.videoResolution      = VIDEO_RESOLUTION_TYPE_720_1280;//默认分辨率 
_ config.autoAdjustStrategy  = AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_2;
```
 
#### 【移动场景】
- **场景特点**
移动场景是个很宽泛的概念，我们团队将带宽不稳定的场景统称为移动场景，该场景下，主播的上行网络会经常发生变动，这一段时间可能是1Mbps， 下一段时间可能就变成 300kbps了。

- **流控方案**
针对这种场景，我们推荐采用 **AUTO_ADJUST_BITRATE_STRATEGY_1**，该策略模式下会尽量让带宽跟着网络情况持续做适应性调整。带来的收益就是在带宽不稳定的情况下推流质量会灵活应对，当然，这也有代价，那就是当网络稳定的情况下，推流码率也会“很不安分”，相比于固定码率会带来更多的波动。
 ```
 TXLivePushConfig* _config;
 _config.videoBitrateMin   = 500;//动态调整的最小码率
 _config.videoBitrateMax   = 1000;//动态调整的最大码率
 _config.videoBitratePIN   = 800;//刚开始进入的默认码率
 _config.enableAutoBitrate = YES;//是否开启动态调整码率
 _config.videoResolution   = VIDEO_RESOLUTION_TYPE_360_640;//默认分辨率 
 _config.autoAdjustStrategy= AUTO_ADJUST_BITRATE_STRATEGY_1;
```

## 5. 定制视频数据
研发实力不俗的客户，会有自定义图像处理的需求（比如堆加字幕），同时又希望复用rtmp sdk的整体流程，如果是这样，您可以按照如下攻略进行定制。

- **设置视频处理回调**
设置 **TXLivePush** 的 **videoProcessDelegate** 代理点，即可实现对视频画面的定制。

```objectivec
@protocol TXVideoCustomProcessDelegate <NSObject>

/**
 * 在OpenGL线程中回调，在这里可以进行采集图像的二次处理
 * @param textureId  纹理ID
 * @param width      纹理的宽度
 * @param height     纹理的高度
 * @return           返回给SDK的纹理
 * 说明：SDK回调出来的纹理类型是GL_TEXTURE_2D，接口返回给SDK的纹理类型也必须是GL_TEXTURE_2D
 */
-(GLuint)onTextureCustomProcess:(GLuint)texture width:(CGFloat)width height:(CGFloat)height;
 
/**
 * 在OpenGL线程中回调，可以在这里释放创建的OpenGL资源
 */
-(void)onTextureDestoryed;

@end
```

- **在回调函数中对视频数据进行加工**
实现 TXVideoCustomProcessDelegate 的 onTextureCustomProcess 函数，以实现对视频画面的自定义处理。textureId 指定的纹理是一块类型为 GLES20.GL_TEXTURE_2D 的纹理。

 对于 texture 数据的操作，需要一定的 OpenGL 基础知识，另外计算量不宜太大，因为 onTextureCustomProcess 的调用频率跟 FPS 相同，过于繁重的处理很容易造成 GPU 过热。


## 6. 替换数据源
如果您只希望使用 RTMP SDK 来推流，音视频采集和预处理（即美颜、滤镜这些）全部由自己的代码来控制，可以按如下步骤实现：

- **Step1. 不再调用 TXLivePush 的 startPreview 接口**
这样 SDK 本身就不会再采集视频数据和音频数据，而只是启动预处理、编码、流控、发送 等跟推流相关的工作

- **Step2. 使用 sendVideoSampleBuffer 向SDK填充Video数据**
sendVideoSampleBuffer 的作用是向 SDK 塞入您采集和处理后的视频数据，目前支持 RGBA 和 NV12 两种格式。

- **Step3. 使用 sendAudioSampleBuffer 向SDK填充Audio数据**
sendAudioSampleBuffer 的作用是向 SDK 塞入您采集和处理后的音频数据，请使用单声道、16位宽、48000Hz 的 PCM  声音数据。

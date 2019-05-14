## 介绍篇
腾讯视频云RTMP SDK由两部分构成：**推流器** + **播放器**，本文将主要介绍播放器SDK的相关信息。

该播放器SDK支持两种标准的流媒体协议：**RTMP** 和 **FLV**，一般而言，FLV 是我们更加推荐使用的格式。

![struct](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tx_cloud_play_sdk_struct.jpg)

SDK开发包附带的播放器DEMO界面如下：

![demo](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/player_demo_introduction.jpg)

-----------------------------------------------------------------------------------------------------------------

## 基础篇
腾讯视频云RTMP SDK的使用特别简单，您只需要在您的App里添加如下几行代码就可以完成对接工作了。目前SDK内部的默认参数设置参考直播场景精心校调过的。

### step 1 :创建控制器
为了能够展示推流预览的界面，您需要新建一个ViewController，继承自UIViewController，不妨起名为PlayerController。

```objectivec
#import "TxPush.h"
@interface PlayerController : UIViewController
{
    TXLivePlayer * _txLivePlayer;
	// ...  
}
```

### step 2: 创建Player对象
先创建一个**LivePlayer**对象，并且将它和当前的控制器的view关联起来。

```objectivec
_txLivePlayer = [[TXLivePlayer alloc] init];
[_txLivePlayer setupVideoWidget:[UIScreen mainScreen].bounds containView:self.view InsertIndex:0]
```

### step 3: 启动播放器
用下面这段代码就可以启动播放器了:

```objectivec
NSString* flvUrl = @"http://2157.liveplay.myqcloud.com/live/2157_xxxx.flv";
[_txLivePlayer startPlay:flvUrl Type:PLAY_TYPE_LIVE_FLV]; //推荐FLV
```

### step 4: 画面调整
如果你希望调整画面的显示方式，SDK也提供了多种选择：
![enter image description here](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/player_demo_render_mode.jpg)

##### setRenderMode
* RENDER_MODE_FULL_FILL_SCREEN  - 将图像等比例铺满整个屏幕，多余部分裁剪掉，此模式下画面不留黑边
* RENDER_MODE_ADJUST_RESOLUTION - 将图像等比例缩放，缩放后的宽和高都不会超过显示区域，居中显示，可能会留有黑边 

##### setRenderRotation
* RENDER_ROTATION_PORTRAIT - 常规的竖屏显示，如果是显示人像，则最适合这种模式了
* RENDER_ROTATION_LANDSCAPE - 横屏显示，游戏直播比较适合这种模式


### step 5: 硬件加速
对于蓝光级别（1080p）的画质，简单采用软件解码的方式很难获得较为流畅的播放体验，所以如果您的场景是以游戏直播为主，建议打开硬件加速开关。

```objectivec
  [_txLivePlayer stopPlay];
  _txLivePlayer.enableHWAcceleration = YES;
  [_txLivePlayer startPlay:_flvUrl Type:_type];
```
 强烈建议在切换硬件解码之前**stopPlay**，在切换之后再**startPlay**,否则会产生比较严重的花屏问题。
 
### step 6: 如何降低延迟并减少画面卡顿？
#### 延迟的产生
这里说的**延迟**是主播 -> 观众的时间延迟，而**卡顿**指的是出现500ms以上的播放停滞。
如果是在完美的网络环境下，可以做到超低延迟下没有卡顿，但现实是国内的网络环境并不完美，数据在经过互联网传输时必然会有抖动和丢包，从而对播放端的流畅播放产生影响。
![tx_live_service_lag](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tx_live_service_lag.jpg)

因此，为了缓解这些不稳定因素，云服务和终端APP都需要引入一些缓冲，但缓冲的加入就不可避免地引入了延迟。
所以，**延迟和流畅是一架天平的两端**，如果过分强调降低延迟，就会导致轻微的网络波动即产生明显的播放端卡顿。反推之，如果过分强调流畅，就意味着引入大量的延迟，一个典型的案例就是HLS协议，通过引入10-30秒的延迟来实现流畅的播放体验。

#### 三种可选模式
为了能够让您无需了解过多流控处理知识就能优化出较好的播放体验，腾讯视频云SDK经过多个版本的改进，优化出一套自动调节技术，并在其基础上推出了三种比较优秀的延迟控制方案：

- **自动模式**：如果您不太确定您的主要场景是什么，可以选择这个模式。
>当把播放器中的 setAutoAdjustCache 开关打开，即为自动模式，在该模式下，播放器会根据当前网络情况，对延迟进行自动调节，默认情况下，播放器会在1s - 5s 这个区间内自动调节延迟大小（您也可以通过setMinCacheTime 和 setMaxCacheTime对默认值进行修改），以保证在足够流畅的情况下尽量降低观众跟主播端的延迟，确保良好的互动体验。

- **极速模式**：主要适用于**秀场直播**和**全民直播**等对延迟要求比较苛刻的场景。
> 我们所谓的极速模式，即（setMinCacheTime = setMaxCacheTime = 1s） ， 而您也发现了，自动模式跟极速模式的差异只是MaxCacheTime 有所不同 （极速模式的 MaxCacheTime 一般比较低，而自动模式的MaxCacheTime 则相对较高 ），这种灵活性主要得益于SDK内部的自动调控技术，可以在不引入卡顿的情况下自动修正延时大小，而MaxCacheTime 反应的就是调节速度：MaxCacheTime的值越大，调控速度会越发保守，当然卡顿概率就会越低。
 
- **流畅模式**：主要适用于**游戏直播**和**点播场景**等对延迟要求不是特别高的场景。
> 当把播放器中的 setAutoAdjustCache 开关关闭，即为流畅模式，在该模式下，播放器采取的处理策略跟Adobe FLASH内核的缓存出策略如出一辙：当视频出现卡顿后，会进入 loading 状态直到缓冲区蓄满，之后进入playing状态，直到下一次遭遇无法抵御的网络波动。默认情况下，缓冲大小为5s，您可以通过setCacheTime进行更改。
> 
> 在延迟要求不高的场景下，这种简单的模式会更加可靠，我们在视频云SDK中引入这种模式主要是很多采纳了很多优秀客户的建议，即希望在播放过程中有平滑的loading和playing状态切换。但采用极速模式时，对于低时延的追求会导致这种切换往往非常频繁进而引发loading闪烁。

#### 代码对接
```objectivec
TXLivePlayConfig*  _config = [[TXLivePlayConfig alloc] init];
//自动模式
_config.bAutoAdjustCacheTime   = YES;
_config.minAutoAdjustCacheTime = 1;
_config.maxAutoAdjustCacheTime = 5;
//极速模式
_config.bAutoAdjustCacheTime   = YES;
_config.minAutoAdjustCacheTime = 1;
_config.maxAutoAdjustCacheTime = 1;
//流畅模式
_config.bAutoAdjustCacheTime   = NO;
_config.cacheTime              = 5;

[_txLivePlayer setConfig:_config];
```

-----------------------------------------------------------------------------------------------------------------
## 状态篇

### 1. 内部原理
下面这幅图展示了SDK播放器的内部技术细节：

![SDK内部原理](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tencent_cloud_rtmp_sdk_player_status_14.jpg)

简单描述就是在您**调用startPlay**之后，RTMP SDK就会**尝试连接网络**，如果一切顺利，就会进入**播放主循环**，SDK内部会按照每秒一次的频率通知**当前的内部状态**（net status），如果中途出现什么问题，则会以 **event**、 **warning** 或者 **error** 的形式通知出来。

### 2. 代码对接
想要获得RTMP SDK的状态通知，您可以提供一个**Listener**给刚才提到的**Player**对象，之后SDK的所有信息都会通过这个Listener反馈给您的App.

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

### 3. 事件通知
#### 3.1) 播放事件
播放中的几个关键时间是必须要关心的，否则流程可能无法顺利跑通。

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_BEGIN    |  2004|  视频播放开始，如果有转菊花什么的这个时候该停了 | 
|PLAY_EVT_PLAY_PROGRESS |  2005|  视频播放进度，会通知当前进度和总体进度      | 
|PLAY_EVT_PLAY_LOADING	|  2007|  视频播放loading，如果能够恢复，之后会有BEGIN事件|  

这里特别要提醒的是  BEGIN 和 LOADING 的状态互切：
在**流畅模式**下，LOADING 到 BEGIN  的时间一般都在1s以上，所以这种切换的中间过程是比较明显的。

在**极速模式**下，由于追求较低的延迟，LOADING 到BEGIN 的时间有可能会非常快也非常频繁，这就意味着如果您在这个时候做视频画面的显示和隐藏，体验会非常差，特别不推荐。

如果您使用了极速模式，推荐您可以像映客那样，无视LOADING事件通知，因为最常见的卡顿一般都是几百毫秒的微卡顿；或者最多在视频画面上叠加一个loading小动画，转个小菊花，不要把这种切换的UI表现做得过重，否则就不适合秀场模式了。

#### 3.2) 结束事件
| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_END      |  2006|  视频播放结束      | 
|PLAY_ERR_NET_DISCONNECT |  -2301  |  网络断连,且经多次重连抢救无效,可以放弃治疗,更多重试请自行重启播放 | 

一次播放流程的完结，或者是止于PLAY_END事件，这算是寿终正寝了；或者是止于NET_DISCONNECT事件，其原因可能是网络断连，也有可能是根本无法从服务器端拉取到数据。

>**协议的差异**
>
>如果播放的是RTMP协议的直播地址，协议本身有比较完善的命令（EOF）来通知服务器直播已经结束，也就是 PLAY_END。
>
> 如果播放的是点播地址，点播文件的结束也能通过特定的方法被播放器获知的，所以 PLAY_END 同样适用。
> 
> 但对于直播场景中最最常用的**FLV**协议，协议本身是不支持结束通知机制的，故您不可能收到 PLAY_END 事件，即使此时的主播已经停止推送数据了。如果您不做额外的查询业务逻辑来支持，您只能依靠 NET_DISCONNECT 这个事件来通知用户：**“主播暂时不在家！”**。

#### 3.3) 警告事件
如下的这些事件，您可以不用关心，我们通知出来只是告诉您内部发生了什么，如果您需要做数据上报，倒是可以用一下：

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_WARNING_VIDEO_DECODE_FAIL   |  2101  | 当前视频帧解码失败  |
| PLAY_WARNING_AUDIO_DECODE_FAIL   |  2102  | 当前音频帧解码失败  |
| PLAY_WARNING_RECONNECT           |  2103  | 网络断连, 已启动自动重连 (重连超过三次就直接抛送 PLAY_ERR_NET_DISCONNECT 了) |
| PLAY_WARNING_RECV_DATA_LAG       |  2104  | 网络来包不稳：可能是下行带宽不足，或由于主播端出流不均匀|
| PLAY_WARNING_VIDEO_PLAY_LAG      |  2105  | 当前视频播放出现卡顿|
| PLAY_WARNING_HW_ACCELERATION_FAIL|  2106  | 硬解启动失败，采用软解   |
| PLAY_WARNING_VIDEO_DISCONTINUITY |  2107  | 当前视频帧不连续，可能丢帧|
| PLAY_WARNING_DNS_FAIL            |  3001  | RTMP-DNS解析失败（仅播放RTMP地址时会抛送）|
| PLAY_WARNING_SEVER_CONN_FAIL     |  3002  | RTMP服务器连接失败（仅播放RTMP地址时会抛送）|
| PLAY_WARNING_SHAKE_FAIL          |  3003  | RTMP服务器握手失败（仅播放RTMP地址时会抛送）|

#### 3.4) 连接事件
此外还有几个连接服务器的事件，您也可以不用特别关心，这里也只要是用来测定和统计服务器连接时间和服务器响应速度用的，在用户界面交互上难有什么用处：

| 事件ID                     |    数值  |  含义说明                    |   
| :-----------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_CONNECT_SUCC     |  2001    | 已经连接服务器                |
| PLAY_EVT_RTMP_STREAM_BEGIN|  2002    | 已经连接服务器，开始拉流（仅播放RTMP地址时会抛送） |
| PLAY_EVT_RCV_FIRST_I_FRAME|  2003    | 网络接收到首个可渲染的视频数据包(IDR)  |


#### 3.5) 网络状态回调 
  **onNetStatus** 通知每秒都会被触发一次，目的是实时反馈当前的推流器状态，它就像汽车的仪表盘，可以告知您目前SDK内部的一些具体情况，以便您能对当前网络状况和视频质量等有所了解。
  
|   评估参数                   |  含义说明                   |   
| :------------------------  |  :------------------------ | 
|	NET_STATUS_VIDEO_BITRATE | 当前流媒体的视频码率，单位 kbps|
|	NET_STATUS_AUDIO_BITRATE | 当前流媒体的音频码率，单位 kbps|
|	NET_STATUS_VIDEO_FPS     | 当前流媒体的视频帧率          |
|	NET_STATUS_NET_SPEED     | 当前的网络数据接收速度        |
|	NET_STATUS_NET_JITTER    | 网络抖动情况，抖动越大，网络越不稳定|
|	NET_STATUS_CACHE_SIZE    | 缓冲区（jitterbuffer）大小，缓冲区当前长度为 0，说明离卡顿就不远了|


















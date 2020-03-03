## 介绍篇
腾讯视频云 RTMP SDK 由两部分构成：**推流器** + **播放器**，本文将主要介绍播放器 SDK 的相关信息。

该播放器 SDK 支持两种标准的流媒体协议：**RTMP** 和 **FLV**，一般而言，FLV 是我们更加推荐使用的格式。

![struct](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tx_cloud_play_sdk_struct.jpg)

SDK 开发包附带的播放器 DEMO 界面如下：

![demo](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/player_demo_introduction.jpg)

## 基础篇
腾讯视频云 RTMP SDK 的使用特别简单，您只需要在您的 App 里添加如下几行代码就可以完成对接工作了。目前 SDK 内部的默认参数设置参考直播场景精心校调过的。

### step 1 :创建控制器
为了能够展示播放界面，您需要新建一个 ViewController，继承自 UIViewController，不妨起名为 PlayerController。

```objectivec
#import "TxPush.h"
@interface PlayerController : UIViewController
{
    TXLivePlayer * _txLivePlayer;
	// ...  
}
```

### step 2: 创建 Player 对象
先创建一个 **LivePlayer** 对象，并且将它和当前的控制器的 view 关联起来。

```objectivec
_txLivePlayer = [[TXLivePlayer alloc] init];
[_txLivePlayer setupVideoWidget:[UIScreen mainScreen].bounds containView:_myView insertIndex:0]
```

### step 3: 绑定渲染界面
step2中的示例代码有一个叫做_myView 参数，该参数的作用就是指定视频图像的渲染区域：SDK 会在_myView 之上构建一个图像控件用于实时渲染视频画面。

如果您想要在渲染画面之上实现弹幕、献花之类的 UI 控件，可以如下图这般创建一个与_myView 平级的兄弟 view，并将其叠加在_myView 之上，简言之，让_myView 只用来渲染对于编写清晰的 UI 代码会比较有帮助。
 ![](//mccdn.qcloud.com/static/img/75b41bd0e9d8a6c2ec8406dc706de503/image.png)

如果您想要调整渲染界面的大小，只需要调整 myView 的大小就可以了，内部的视频画面会跟随 myView 的大小变化而自动地适应。

> **【如何做动画？】**
> 针对 myView 做动画是比较自由的，不过请注意做动画的目标属性应该是 myView 的 transform 属性而不是 frame 属性。
>
```objectivec
  [UIView animateWithDuration:0.5 animations:^{
            _myView.transform = CGAffineTransformMakeScale(0.3, 0.3); //缩小1/3
        }];
```

### step 4: 启动播放器
用下面这段代码就可以启动播放器了:

```objectivec
NSString* flvUrl = @"http://2157.liveplay.myqcloud.com/live/2157_xxxx.flv";
[_txLivePlayer startPlay:flvUrl type:PLAY_TYPE_LIVE_FLV]; //推荐FLV
```

### step 5: 填充&适应&旋转
如果您希望调整画面的显示方式，SDK 也提供了多种选择：
![](//mc.qcloudimg.com/static/img/ef948faaf1d62e8ae69e3fe94ab433dc/image.png)

- **setRenderMode**

| 可选值 | 含义  |
|---------|---------|
| RENDER_MODE_FILL_SCREEN | 将图像等比例铺满整个屏幕，多余部分裁剪掉，此模式下画面不会留黑边，但可能因为部分区域被裁剪而显示不全。 | 
| RENDER_MODE_FILL_EDGE | 将图像等比例缩放，适配最长边，缩放后的宽和高都不会超过显示区域，居中显示，画面可能会留有黑边。 | 

- **setRenderRotation**

| 可选值 | 含义  |
|---------|---------|
| HOME_ORIENTATION_DOWN | 正常播放（Home 键在画面正下方） | 
| HOME_ORIENTATION_RIGHT | 画面顺时针旋转90度（Home 键在画面正右方） | 
| HOME_ORIENTATION_UP | 画面顺时针旋转180度（Home 键在画面正上方） | 
| HOME_ORIENTATION_LEFT | 画面顺时针旋转270度（Home 键在画面正左方） | 



### step 6: 硬件加速
对于蓝光级别（1080p）的画质，简单采用软件解码的方式很难获得较为流畅的播放体验，所以如果您的场景是以游戏直播为主，建议打开硬件加速开关。

```objectivec
  [_txLivePlayer stopPlay];
  _txLivePlayer.enableHWAcceleration = YES;
  [_txLivePlayer startPlay:_flvUrl type:_type];
```
 强烈建议在切换硬件解码之前 **stopPlay**，在切换之后再 **startPlay**,否则会产生比较严重的花屏问题。
 
### step 7: 如何降低延迟并减少画面卡顿？
#### 延迟的产生
这里说的**延迟**是主播 -> 观众的时间延迟，而**卡顿**指的是出现500ms以上的播放停滞。
如果是在完美的网络环境下，可以做到超低延迟下没有卡顿，但现实是国内的网络环境并不完美，数据在经过互联网传输时必然会有抖动和丢包，从而对播放端的流畅播放产生影响。
![tx_live_service_lag](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tx_live_service_lag.jpg)

因此，为了缓解这些不稳定因素，云服务和终端 APP 都需要引入一些缓冲，但缓冲的加入就不可避免地引入了延迟。
所以，**延迟和流畅是一架天平的两端**，如果过分强调降低延迟，就会导致轻微的网络波动即产生明显的播放端卡顿。反推之，如果过分强调流畅，就意味着引入大量的延迟，一个典型的案例就是 HLS 协议，通过引入10-30秒的延迟来实现流畅的播放体验。

#### 三种可选模式
为了能够让您无需了解过多流控处理知识就能优化出较好的播放体验，腾讯视频云 SDK 经过多个版本的改进，优化出一套自动调节技术，并在其基础上推出了三种比较优秀的延迟控制方案：

- **自动模式**：如果您不太确定您的主要场景是什么，可以选择这个模式。
>当把播放器中的 setAutoAdjustCache 开关打开，即为自动模式，在该模式下，播放器会根据当前网络情况，对延迟进行自动调节，默认情况下，播放器会在1s - 5s这个区间内自动调节延迟大小（您也可以通过  setMinCacheTime 和 setMaxCacheTime 对默认值进行修改），以保证在足够流畅的情况下尽量降低观众跟主播端的延迟，确保良好的互动体验。

- **极速模式**：主要适用于**秀场直播**和**全民直播**等对延迟要求比较苛刻的场景。
> 我们所谓的极速模式，即（setMinCacheTime = setMaxCacheTime = 1s） ， 而您也发现了，自动模式跟极速模式的差异只是 MaxCacheTime 有所不同 （极速模式的 MaxCacheTime 一般比较低，而自动模式的 MaxCacheTime 则相对较高 ），这种灵活性主要得益于 SDK 内部的自动调控技术，可以在不引入卡顿的情况下自动修正延时大小，而 MaxCacheTime 反应的就是调节速度：MaxCacheTime 的值越大，调控速度会越发保守，当然卡顿概率就会越低。
 
- **流畅模式**：主要适用于**游戏直播**和**点播场景**等对延迟要求不是特别高的场景。
> 当把播放器中的 setAutoAdjustCache 开关关闭，即为流畅模式，在该模式下，播放器采取的处理策略跟Adobe FLASH内核的缓存出策略如出一辙：当视频出现卡顿后，会进入 loading 状态直到缓冲区蓄满，之后进入 playing 状态，直到下一次遭遇无法抵御的网络波动。默认情况下，缓冲大小为5s，您可以通过setCacheTime 进行更改。
> 
> 在延迟要求不高的场景下，这种简单的模式会更加可靠，我们在视频云 SDK 中引入这种模式主要是很多采纳了很多优秀客户的建议，即希望在播放过程中有平滑的 loading 和 playing 状态切换。但采用极速模式时，对于低时延的追求会导致这种切换往往非常频繁进而引发 loading 闪烁。

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

## 状态篇

### 1. 内部原理
下面这幅图展示了 SDK 播放器的内部技术细节：

![SDK内部原理](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tencent_cloud_rtmp_sdk_player_status_14.jpg)

简单描述就是在您**调用 startPlay** 之后，RTMP SDK就会**尝试连接网络**，如果一切顺利，就会进入**播放主循环**，SDK内部会按照每秒一次的频率通知**当前的内部状态**（net status），如果中途出现什么问题，则会以 **event**、 **warning** 或者 **error** 的形式通知出来。

### 2. 代码对接
想要获得 RTMP SDK 的状态通知，您可以提供一个 **Listener** 给刚才提到的 **Player** 对象，之后 SDK 的所有信息都会通过这个 Listener 反馈给您的 App.

```objectivec
@interface PlayController ()<UITextFieldDelegate, TXLivePlayListener>
@end
_txLivePlayer.delegate = self;

#pragma - TXLivePlayListener
-(void) onPlayEvent:(int)EvtID withParam:(NSDictionary*)param;
{
    // here your code.
}

-(void) onNetStatus:(NSDictionary*) param;
{
    // here your code.
}
```

### 3. 播放事件
播放中的几个关键时间是必须要关心的，否则流程可能无法顺利跑通。

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_BEGIN    |  2004|  视频播放开始，如果有转菊花什么的这个时候该停了 | 
|PLAY_EVT_PLAY_PROGRESS |  2005|  视频播放进度，会通知当前进度和总体进度      | 
|PLAY_EVT_PLAY_LOADING	|  2007|  视频播放 loading，如果能够恢复，之后会有 BEGIN 事件|  

这里特别要提醒的是  BEGIN 和 LOADING 的状态互切：
在**流畅模式**下，LOADING 到 BEGIN  的时间一般都在1s以上，所以这种切换的中间过程是比较明显的。

在**极速模式**下，由于追求较低的延迟，LOADING 到 BEGIN 的时间有可能会非常快也非常频繁，这就意味着如果您在这个时候做视频画面的显示和隐藏，体验会非常差，特别不推荐。

如果您使用了极速模式，推荐您可以像映客那样，无视 LOADING 事件通知，因为最常见的卡顿一般都是几百毫秒的微卡顿；或者最多在视频画面上叠加一个 loading 小动画，转个小菊花，**建议不要把这种切换的 UI 表现做得过重**，否则就不适合秀场模式了。

### 4. 结束事件
| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_END      |  2006|  视频播放结束      | 
|PLAY_ERR_NET_DISCONNECT |  -2301  |  网络断连,且经多次重连抢救无效,可以放弃治疗,更多重试请自行重启播放 | 

一次播放流程的完结，或者是止于 PLAY_END 事件，这算是寿终正寝了；或者是止于 NET_DISCONNECT 事件，其原因可能是网络断连，也有可能是根本无法从服务器端拉取到数据。

>**协议的差异**
>
>如果播放的是 RTMP 协议的直播地址，协议本身有比较完善的命令（EOF）来通知服务器直播已经结束，也就是 PLAY_END。如果播放的是点播地址，点播文件的结束也能通过特定的方法被播放器获知的，所以 PLAY_END 同样适用。
> 
> 但对于 **FLV** 协议，协议本身是不支持结束通知机制的，故您不可能收到 PLAY_END 事件，只能依靠 NET_DISCONNECT 这个事件来获知：**“主播已离开！”**。
> 
> 推荐的做法是在主播结束推流后，利用聊天室的消息通道群发下线消息来通知所有观众。

### 5. 警告事件
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
| PLAY_WARNING_DNS_FAIL            |  3001  | RTMP-DNS 解析失败（仅播放 RTMP 地址时会抛送）|
| PLAY_WARNING_SEVER_CONN_FAIL     |  3002  | RTMP 服务器连接失败（仅播放 RTMP 地址时会抛送）|
| PLAY_WARNING_SHAKE_FAIL          |  3003  | RTMP 服务器握手失败（仅播放 RTMP 地址时会抛送）|

### 6. 连接事件
此外还有几个连接服务器的事件，您也可以不用特别关心，这里也只要是用来测定和统计服务器连接时间和服务器响应速度用的，在用户界面交互上难有什么用处：

| 事件ID                     |    数值  |  含义说明                    |   
| :-----------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_CONNECT_SUCC     |  2001    | 已经连接服务器                |
| PLAY_EVT_RTMP_STREAM_BEGIN|  2002    | 已经连接服务器，开始拉流（仅播放 RTMP 地址时会抛送） |
| PLAY_EVT_RCV_FIRST_I_FRAME|  2003    | 网络接收到首个可渲染的视频数据包（IDR）  |


### 7. 状态回调 
 **onNetStatus** 通知每秒都会被触发一次，目的是实时反馈当前的推流器状态，它就像汽车的仪表盘，可以告知您目前SDK内部的一些具体情况，以便您能对当前网络状况和视频质量等有所了解。
  
|   评估参数                   |  含义说明                   |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE     | 当前瞬时 CPU 使用率 | 
| NET_STATUS_VIDEO_WIDTH  | 视频分辨率 - 宽 |
| NET_STATUS_VIDEO_HEIGHT| 视频分辨率 - 高 |
|	NET_STATUS_NET_SPEED     | 当前的网络数据接收速度 |
|	NET_STATUS_NET_JITTER    | 网络抖动情况，抖动越大，网络越不稳定 |
|	NET_STATUS_VIDEO_FPS     | 当前流媒体的视频帧率    |
|	NET_STATUS_VIDEO_BITRATE | 当前流媒体的视频码率，单位kbps|
|	NET_STATUS_AUDIO_BITRATE | 当前流媒体的音频码率，单位kbps|
|	NET_STATUS_CACHE_SIZE    | 缓冲区（jitterbuffer）大小，缓冲区当前长度为 0，说明离卡顿就不远了|
| NET_STATUS_SERVER_IP | 连接的服务器 IP | 

















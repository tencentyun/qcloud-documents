## 基础知识
RTMP SDK 包含推流和播放两方面功能，推流为主播端功能，播放（分为直播和点播）为观众端功能。对接之前，我们先列表如下一些基本知识会大有裨益：

- **直播和点播**
<font color='blue'>直播</font> 的视频源是实时生成的，有人推流直播才有意义。所以，一旦主播停播，直播URL也就进失效了，而且由于是实时直播，所以播放器在播直播视频的时候是没有进度条的。

 <font color='blue'>点播</font> 的视频源是云端的一个文件，文件只要没有被提供方删除，就随时可以播放， 而且由于整个视频都在服务器上，所以播放的时候是有进度条的哦。

- **协议的支持**
通常使用的直播协议如下，APP端推荐使用 FLV 协议的直播地址(以“http”打头，以“.flv”结尾)：
![](//mc.qcloudimg.com/static/img/94c348ff7f854b481cdab7f5ba793921/image.jpg)

 通常使用的点播协议如下，现在比较流行的是HLS(以“http”打头，以“.m3u8”结尾)的点播地址：
![](//mc.qcloudimg.com/static/img/4b42a00bb7ce2f58f362f35397734177/image.jpg)

## 特别说明
腾讯云 RTMP SDK <font color='red'>**不会对**</font> 播放地址的来源做限制，即您可以用它来播放腾讯云或非腾讯云的播放地址。但 RTMP SDK 中的播放器只支持 FLV 、RTMP 和 HLS（m3u8）三种格式的直播地址，以及 MP4、 HLS（m3u8）和 FLV 三种格式的点播地址。

## 对接攻略

### step 1: 创建Player
```objectivec
_txLivePlayer = [[TXLivePlayer alloc] init];
[_txLivePlayer setupVideoWidget:[UIScreen mainScreen].bounds containView:_myView insertIndex:0]
```

### step 2: 给画面“找块地”
接下来我们要给播放器的视频画面找个地方来显示，iOS系统中使用view作为基本的界面渲染单位，所以您只需要准备一个view并调整好布局就可以了。

- **推荐的布局！**
> RTMP SDK 播放器的内部并不是直接把画面渲染在您提供的view上，而是在这个view之上创建一个用于OpenGL渲染的子视图（subView），不过这个渲染用的subView的大小会跟随您提供的view大小变化而自动调整，所以您无需关注这一点。
>![](//mccdn.qcloud.com/static/img/75b41bd0e9d8a6c2ec8406dc706de503/image.png)
>
> 如果您想要在渲染画面之上实现弹幕、献花之类的UI控件，我们推荐您”另起炉灶“（再创建一个平级的view），这是一种常见的设计风格，也可以避免很多前后画面覆盖的问题。

- **如何做动画？**
> 针对view做动画是比较自由的，不过请注意此处动画所修改的目标属性应该是<font color='red'>transform</font>属性而不是frame属性。
>
```objectivec
  [UIView animateWithDuration:0.5 animations:^{
            _myView.transform = CGAffineTransformMakeScale(0.3, 0.3); //缩小1/3
        }];
```

### step 3: 启动播放
```objectivec
NSString* flvUrl = @"http://2157.liveplay.myqcloud.com/live/2157_xxxx.flv";
//用 setupVideoWidget 给播放器绑定决定渲染区域的view，其首个参数 frame 在 1.5.2 版本后已经废弃
[_txLivePlayer setupVideoWidget:CGRectMake(0, 0, 0, 0) containView:_myView insertIndex:0];
//使用 startPlay 即可开始播放，如果是直播的话我们推荐 FLV 协议
[_txLivePlayer startPlay:flvUrl type:PLAY_TYPE_LIVE_FLV];
```

- **setupVideoWidget** 
1.5.2 版本以后，frame 参数被废弃，画面区域的大小改成了时刻铺满您传入的view，如需修改画面的大小及位置，直接调整view即可达到您的目标。

- **startPlay** 
type 参数支持如下几种选项，有很多客户反馈 <font color='red'>**播放有快进现象**</font>，那是因为把 LIVE_FLV 和 VOD_FLV 弄混了导致的。

| 可选值 | 枚举值 | 含义 |
|---------|---------|---------|
| PLAY_TYPE_LIVE_RTMP | 0 | 传入的URL为RTMP直播地址 |
| PLAY_TYPE_LIVE_FLV | 1 | 传入的URL为FLV直播地址 |
| PLAY_TYPE_VOD_FLV | 2 | 传入的URL为RTMP点播地址 |
| PLAY_TYPE_VOD_HLS | 3 | 传入的URL为HLS(m3u8)点播地址 |
| PLAY_TYPE_VOD_MP4 | 4 | 传入的URL为MP4点播地址 |
| PLAY_TYPE_LIVE_RTMP_ACC | 5 | 低延迟连麦链路直播地址（仅适合于连麦场景） |
| PLAY_TYPE_LOCAL_VIDEO | 6 | 手机本地视频文件 |

### step 4: 画面调整

- **view：大小和位置**
如需修改画面的大小及位置，直接调整 setupVideoWidget 的参数 view 的大小和位置，即可达到您的目标。

- **setRenderMode：铺满or适应**

| 可选值 | 含义  |
|---------|---------|
| RENDER_MODE_FILL_SCREEN | 将图像等比例铺满整个屏幕，多余部分裁剪掉，此模式下画面不会留黑边，但可能因为部分区域被裁剪而显示不全。 | 
| RENDER_MODE_FILL_EDGE | 将图像等比例缩放，适配最长边，缩放后的宽和高都不会超过显示区域，居中显示，画面可能会留有黑边。 | 

- **setRenderRotation：画面旋转**

| 可选值 | 含义  |
|---------|---------|
| RENDER_ROTATION_PORTRAIT | 正常播放（Home键在画面正下方） | 
| RENDER_ROTATION_LANDSCAPE | 画面顺时针旋转270度（Home键在画面正左方） | 

![](//mc.qcloudimg.com/static/img/ef948faaf1d62e8ae69e3fe94ab433dc/image.png)


### step 5: 进度调整
调整播放进度这个操作 <font color='red'>**仅对点播有效**</font> ，因为直播的视频源是实时的，没有调整进度的可能。
```objectivec
// 调整进度
[_txLivePlayer seek:slider.value];
```

### step 6: 暂停播放
- **点播**
暂停对于点播的含义相信您不需要我再做赘述。

- **直播**
在直播过程中调用pause，效果等同于暂时停止拉流，播放器不会被销毁，但会显示最后一帧画面。

```objectivec
// 暂停
[_txLivePlayer pause];
// 恢复
[_txLivePlayer resume];
```

### step 7: 结束播放
结束播放时 <font color='red'>**记得销毁view控件**</font> ，尤其是在下次startPlay之前，否则会产生大量的内存泄露以及闪屏问题。

```objectivec
// 停止播放
[_txLivePlayer stopPlay];
[_txLivePlayer removeVideoWidget]; // 记得销毁view控件
```

### step 8: 硬件加速
对于蓝光级别（1080p）的画质，简单采用软件解码的方式很难获得较为流畅的播放体验，所以如果您的场景是以游戏直播为主，一般都推荐开启硬件加速。

软解和硬解的切换需要在切换之前先**stopPlay**，切换之后再**startPlay**，否则会产生比较严重的花屏问题。

```objectivec
  [_txLivePlayer stopPlay];
  _txLivePlayer.enableHWAcceleration = YES;
  [_txLivePlayer startPlay:_flvUrl type:_type];
```

### step 9: 截流录制（仅直播）
截流录制是直播播放场景下的一种扩展功能：观众在观看直播时，可以通过点击录制按钮把一段直播的内容录制下来，并通过视频分发平台（比如腾讯云的点播系统）发布出去，这样就可以在微信朋友圈等社交平台上以 UGC 消息的形式进行传播。

![](//mc.qcloudimg.com/static/img/2963b8f0af228976c9c7f2b11a514744/image.png)

```objectivec
//如下代码用于展示直播播放场景下的录制功能
//
//指定一个 TXVideoRecordListener 用于同步录制的进度和结果
_txLivePlayer.recordDelegate = recordListener;
//启动录制，可放于录制按钮的响应函数里，目前只支持录制视频源，弹幕消息等等目前还不支持
[_txLivePlayer startRecord: RECORD_TYPE_STREAM_SOURCE]; 
// ...
// ...
//结束录制，可放于结束按钮的响应函数里
[_txLivePlayer stopRecord];                             
```
- 录制的进度以时间为单位，由 TXVideoRecordListener 的 onRecordProgress 通知出来。
- 录制好的文件以 MP4 文件的形式，由 TXVideoRecordListener 的 onRecordComplete 通知出来。
- 视频的上传和发布由 TXUGCPublish 负责，具体使用方法可以参考 [短视频-文件发布](https://cloud.tencent.com/document/product/584/9367#6.-.E6.96.87.E4.BB.B6.E5.8F.91.E5.B8.8310)。

### step 10: mp4本地缓存播放（仅点播）
点播播放器支持对mp4的本地缓存，在观看同一个视频的时候可以节省流量，默认没有开启，开启此功能需要配置两个参数：本地缓存目录及需要缓存的视频个数。

```objectivec
//如下代码用于展示点播场景下mp4本地缓存播放
//指定一个本地mp4缓存目录
_txLivePlayerConfig.cacheFolderPath = 
    [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) objectAtIndex:0];
//指定本地最多缓存多少文件，避免缓存太多数据
_txLivePlayerConfig.maxCacheItems = 2;
[_txLivePlayer setConfig: _txLivePlayerConfig]; 
// ...
//开始播放
[_txLivePlayer startPlay:playUrl type:_playType];                            
```

### step 11: 变速播放（仅点播）
点播播放器支持变速播放，通过接口`setRate`设置点播播放速率来完成，支持快速与慢速播放，如0.5X、1.0X、1.2X、2X等。

 ```objectivec
//如下代码用于展示点播倍速播放
//设置1.2倍速播放
[_txLivePlayer setRate:1.2]; 
// ...
//开始播放
[_txLivePlayer startPlay:playUrl type:_playType];
```

## 状态监听
腾讯云 RTMP SDK 一直坚持白盒化设计原则，你可以为 TXLivePlayer 对象绑定一个 **TXLivePlayListener**，之后SDK 的内部状态信息均会通过 onPlayEvent（事件通知） 和 onNetStatus（质量反馈）通知给您。

### 1. 播放事件
| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_BEGIN    |  2004|  视频播放开始，如果有转菊花什么的这个时候该停了 | 
|PLAY_EVT_PLAY_PROGRESS |  2005|  视频播放进度，会通知当前进度和总体进度，**仅在点播时有效**      | 
|PLAY_EVT_PLAY_LOADING	|  2007|  视频播放loading，如果能够恢复，之后会有BEGIN事件|  

- **不要在收到 PLAY_LOADING 后隐藏播放画面**
因为PLAY_LOADING -> PLAY_BEGIN 的时间长短是不确定的，可能是 5s 也可能是 5ms，有些客户考虑在 LOADING 时隐藏画面， BEGIN 时显示画面，会造成严重的画面闪烁（尤其是直播场景下）。推荐的做法是在视频播放画面上叠加一个半透明的 loading 动画。

- **LOADING 频繁与否多是由cacheTime决定的**
TXLivePlayConfig 中可以配置播放器的 cacheTime 属性，如果 cacheTime 属性被设置的很小，那么 LOADING 就会变得非常频繁，如果你您发现有频繁LOADING的情况出现，请参考[卡顿&延迟](#.E5.8D.A1.E9.A1.BF.26amp.3B.E5.BB.B6.E8.BF.9F) 进行校调。

- **PLAY_PROGRESS 播放进度的处理**
如果您对如何处理点播时的 PLAY_EVT_PLAY_PROGRESS 事件没有思路，可以参考示例代码-[进度处理](https://cloud.tencent.com/document/product/454/7896)。

### 2. 结束事件
| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_END      |  2006|  视频播放结束      | 
|PLAY_ERR_NET_DISCONNECT |  -2301  |  网络断连,且经多次重连抢救无效,可以放弃治疗,更多重试请自行重启播放 | 

- **<font color='red'>如何判断直播已结束？</font>**
如果是**点播**，我们可以通过 PLAY_EVT_PLAY_END 事件判断是否已经播放结束。

 如果是**直播**，仅靠 SDK 本身是无法获知主播是否已经结束推流的。可预期的表现是：主播结束推流后，RTMP SDK 会很快发现数据流拉取失败（WARNING_RECONNECT），然后开始重试，直至三次重试失败后抛出 PLAY_ERR_NET_DISCONNECT 事件。

 出现这个问题的原因是标准播放协议中本身没有通用的 STOP 标准，所以推荐的做法是通过聊天室群发 **“直播已结束”** 这类系统消息来完成你的目标。


### 3. 警告事件
如下的这些事件您可以不用关心，我们只是基于白盒化的SDK设计理念，将事件信息同步出来

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

### 4. 连接事件
此外还有几个连接服务器的事件，主要用于测定和统计服务器连接时间，您也无需关心：

| 事件ID                     |    数值  |  含义说明                    |   
| :-----------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_CONNECT_SUCC     |  2001    | 已经连接服务器                |
| PLAY_EVT_RTMP_STREAM_BEGIN|  2002    | 已经连接服务器，开始拉流（仅播放RTMP地址时会抛送） |
| PLAY_EVT_RCV_FIRST_I_FRAME|  2003    | 网络接收到首个可渲染的视频数据包(IDR)  |


### 5. 状态回调 
 **onNetStatus** 通知每秒都会被触发一次，目的是实时反馈当前的推流器状态，它就像汽车的仪表盘，可以告知您目前SDK内部的一些具体情况，以便您能对当前网络状况和视频质量等有所了解。
  
|   评估参数                   |  含义说明                   |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE     | 当前瞬时CPU使用率 | 
| NET_STATUS_VIDEO_WIDTH  | 视频分辨率 - 宽 |
| NET_STATUS_VIDEO_HEIGHT| 视频分辨率 - 高 |
|	NET_STATUS_NET_SPEED     | 当前的网络数据接收速度 |
|	NET_STATUS_NET_JITTER    | 网络抖动情况，抖动越大，网络越不稳定 |
|	NET_STATUS_VIDEO_FPS     | 当前流媒体的视频帧率    |
|	NET_STATUS_VIDEO_BITRATE | 当前流媒体的视频码率，单位 kbps|
|	NET_STATUS_AUDIO_BITRATE | 当前流媒体的音频码率，单位 kbps|
|	NET_STATUS_CACHE_SIZE    | 缓冲区（jitterbuffer）大小，缓冲区当前长度为 0，说明离卡顿就不远了|
| NET_STATUS_SERVER_IP | 连接的服务器IP | 

## 卡顿&延迟
在直播场景下，能决定一款 APP 产品的用户体验好坏的关键指标就是：卡顿率的高低和延迟的高低。

**播放器本身在其中起到了更为关键的决定性作用**，同样的网络环境和播放地址，不同的播放器可能会表现出完全不同的延迟和卡顿率。（比如 PC 浏览器上主流的 flash 播放器会因为播放策略过于简单粗暴，产生延迟越对越多的问题）

所以，在您完成本篇文档前面部分罗列的功能代码对接后，请务必阅读 [卡顿优化-播放端优化](https://cloud.tencent.com/document/product/454/7946#5.-.E6.92.AD.E6.94.BE.E7.AB.AF.E7.9A.84.E4.BC.98.E5.8C.969) 来校调出最适合您的业务场景的播放模式。

- **三种模式的特性对比**

![](//mc.qcloudimg.com/static/img/1d5a860ff74f9d026a36c04dd8bb27ef/image.jpg)

- **三种模式的对接代码**

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

//设置完成之后再启动播放

```

注意：各家云商一般都会在CDN端引入 **1.5s - 2s** 左右的延迟，这是不可避免的，所以 **总延迟 = CDN延迟 + CacheTime。**


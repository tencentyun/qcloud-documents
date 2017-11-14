## 基础知识
本文主要介绍视频云 SDK 的直播播放功能，在此之前，先了解如下一些基本知识会大有裨益：

- **直播和点播**
<font color='blue'>直播（LIVE）</font> 的视频源是主播实时推送的。因此，主播停止推送后，播放端的画面也会随即停止，而且由于是实时直播，所以播放器在播直播 URL 的时候是没有进度条的。

 <font color='blue'>点播（VOD）</font> 的视频源是云端的一个视频文件，只要未被从云端移除，视频就可以随时播放， 播放中您可以通过进度条控制播放位置，腾讯视频和优酷土豆等视频网站上的视频观看就是典型的点播场景。

- **协议的支持**
通常使用的直播协议如下，APP端推荐使用 FLV 协议的直播地址(以“http”打头，以“.flv”结尾)：
![](//mc.qcloudimg.com/static/img/94c348ff7f854b481cdab7f5ba793921/image.jpg)

## 特别说明
- **是否有限制？**
视频云 SDK <font color='red'>**不会对**</font> 播放地址的来源做限制，即您可以用它来播放腾讯云或非腾讯云的播放地址。但视频云 SDK 中的播放器只支持 FLV 、RTMP 和 HLS（m3u8）三种格式的直播地址，以及 MP4、 HLS（m3u8）和 FLV 三种格式的点播地址。

- **历史因素**
SDK 早期版本只有 TXLivePlayer 一个 Class 承载直播和点播功能，但是由于点播功能越做越多，我们最终在 SDK 3.5 版本开始，将点播功能单独分离出来，交由 TXVodPlayer 来负责。但是为了保证编译通过，您在 TXLivePlayer 中依然可以看到类似 seek 等点播才具备的功能。

## 对接攻略

### step 1: 创建Player
视频云 SDK 中的 TXLivePlayer 模块负责实现直播播放功能。
```objectivec
TXLivePlayer _txLivePlayer = [[TXLivePlayer alloc] init];
```

### step 2: 渲染View
接下来我们要给播放器的视频画面找个地方来显示，iOS系统中使用 view 作为基本的界面渲染单位，所以您只需要准备一个 view 并调整好布局就可以了。

```objectivec
//用 setupVideoWidget 给播放器绑定决定渲染区域的view，其首个参数 frame 在 1.5.2 版本后已经被废弃
[_txLivePlayer setupVideoWidget:CGRectMake(0, 0, 0, 0) containView:_myView insertIndex:0];
```

内部原理上讲，播放器并不是直接把画面渲染到您提供的 view （示例代码中的 \_myView）上，而是在这个view之上创建一个用于OpenGL渲染的子视图（subView）。

如果您要调整渲染画面的大小，只需要调整你所常见的 view 的大小和位置即可，SDK 会让视频画面跟着您的 view 的大小和位置进行实时的调整。

![](//mccdn.qcloud.com/static/img/75b41bd0e9d8a6c2ec8406dc706de503/image.png)
 
> **如何做动画？**
> 针对view做动画是比较自由的，不过请注意此处动画所修改的目标属性应该是 <font color='red'>transform</font> 属性而不是 frame 属性。
```objectivec
  [UIView animateWithDuration:0.5 animations:^{
            _myView.transform = CGAffineTransformMakeScale(0.3, 0.3); //缩小1/3
        }];
```

### step 3: 启动播放
```objectivec
NSString* flvUrl = @"http://2157.liveplay.myqcloud.com/live/2157_xxxx.flv";
[_txLivePlayer startPlay:flvUrl type:PLAY_TYPE_LIVE_FLV];
```

| 可选值 | 枚举值 | 含义 |
|---------|---------|---------|
| PLAY_TYPE_LIVE_RTMP | 0 | 传入的URL为RTMP直播地址 |
| PLAY_TYPE_LIVE_FLV | 1 | 传入的URL为FLV直播地址 |
| PLAY_TYPE_LIVE_RTMP_ACC | 5 | 低延迟链路地址（仅适合于连麦场景） |
| PLAY_TYPE_VOD_HLS | 3 | 传入的URL为HLS(m3u8)播放地址 |

> **关于HLS(m3u8)**
> 在 APP 上我们不推荐使用 HLS 这种播放协议播放直播视频源（虽然它很适合用来做点播），因为延迟太高，在 APP 上推荐使用 LIVE_FLV 或者 LIVE_RTMP 播放协议。


### step 4: 画面调整

- **view：大小和位置**
如需修改画面的大小及位置，直接调整 setupVideoWidget 的参数 view 的大小和位置，SDK 会让视频画面跟着您的 view 的大小和位置进行实时的调整。

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


### step 5: 暂停播放
对于直播播放而言，并没有真正意义上的暂停，所谓的直播暂停，只是**画面冻结**和**关闭声音**，而云端的视频源还在不断地更新着，所以当您调用 resume 的时候，会从最新的时间点开始播放，这跟点播是有很大不同的（点播播放器的暂停和继续与播放本地视频文件时的表现相同)。

```objectivec
// 暂停
[_txLivePlayer pause];
// 恢复
[_txLivePlayer resume];
```

### step 6: 结束播放
结束播放时，如果要推出当前的UI界面，要记得用 <font color='red'>** removeVideoWidget **</font> 销毁view控件，否则会产生内存泄露或闪屏问题。

```objectivec
// 停止播放
[_txLivePlayer stopPlay];
[_txLivePlayer removeVideoWidget]; // 记得销毁view控件
```

### step 7: 硬件加速
对于蓝光级别（1080p）的画质，简单采用软件解码的方式很难获得较为流畅的播放体验，所以如果您的场景是以游戏直播为主，一般都推荐开启硬件加速。

软解和硬解的切换需要在切换之前先**stopPlay**，切换之后再**startPlay**，否则会产生比较严重的花屏问题。

```objectivec
  [_txLivePlayer stopPlay];
  _txLivePlayer.enableHWAcceleration = YES;
  [_txLivePlayer startPlay:_flvUrl type:_type];
```

### step 8: 屏幕截图
通过调用 **snapshot** 您可以截取当前直播画面为一帧屏幕，此功能只会截取当前直播流的视频画面，如果您需要截取当前的整个 UI 界面，请调用 iOS 的系统 API 来实现。

![](//mc.qcloudimg.com/static/img/f63830d29c16ce90d8bdc7440623b0be/image.jpg)

### step 9: 截流录制
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


<h2 id="RealTimePlay">超低延时播放</h2>
支持 <font color='red'>**400ms**</font> 左右的超低延迟播放时腾讯云直播播放器的一个特点，它可以用于一些对时延要求极为苛刻的场景，比如**远程夹娃娃**或者**主播连麦**，等等，关于这个特性，您需要知道：

- **该功能是不需要开通的**
该功能并不需要提前开通，但是要求直播流必须位于腾讯云，跨云商实现低延时链路的难度不仅仅是技术层面的。

- **播放地址需要带防盗链**
播放URL 不能用普通的 CDN URL， 必须要带防盗链签名，防盗链签名的计算方法见 [**txTime&txSecret**](https://cloud.tencent.com/document/product/454/9875)。

- **播放类型需要指定ACC**
在调用 startPlay 函数时，需要指定 type 为 <font color='red'>**PLAY_TYPE_LIVE_RTMP_ACC**</font>，SDK 会使用 RTMP-UDP 协议拉取直播流。

- **该功能有并发播放限制**
目前最多同时<font color="red"> 10 路 </font>并发播放，所以您只能在互动场景中使用（比如连麦主播 或者 夹娃娃直播中的操作者这一路）。

- **Obs的延时是不达标的**
推流端如果是 [TXLivePusher](https://cloud.tencent.com/document/product/454/7879)，请使用 [setVideoQuality](https://cloud.tencent.com/document/product/454/7879#step-4.3A-.E8.AE.BE.E5.AE.9A.E6.B8.85.E6.99.B0.E5.BA.A6) 将 `quality`  设置为 MAIN_PUBLISHER 或者 VIDEO_CHAT。如果是 Windows 端，请使用我们的 [Windows SDK](https://cloud.tencent.com/document/product/454/7873#Windows)， Obs 的推流端积压比较严重，是无法达到低延时效果的。


## SDK事件监听
你可以为 TXLivePlayer 对象绑定一个 **TXLivePlayListener**，之后SDK 的内部状态信息均会通过 onPlayEvent（事件通知） 和 onNetStatus（状态反馈）通知给您。

### 1. 播放事件
| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_BEGIN    |  2004|  视频播放开始，如果有转菊花什么的这个时候该停了 | 
|PLAY_EVT_PLAY_LOADING	|  2007|  视频播放loading，如果能够恢复，之后会有BEGIN事件|  

- **不要在收到 PLAY_LOADING 后隐藏播放画面**
因为PLAY_LOADING -> PLAY_BEGIN 的时间长短是不确定的，可能是 5s 也可能是 5ms，有些客户考虑在 LOADING 时隐藏画面， BEGIN 时显示画面，会造成严重的画面闪烁（尤其是直播场景下）。推荐的做法是在视频播放画面上叠加一个半透明的 loading 动画。

- **LOADING 频繁与否多是由 cacheTime 决定的**
TXLivePlayConfig 中可以配置播放器的 cacheTime 属性，如果 cacheTime 属性被设置的很小，那么 LOADING 就会变得非常频繁，如果你您发现有频繁 LOADING 的情况出现，请参考[卡顿&延迟](#.E5.8D.A1.E9.A1.BF.26amp.3B.E5.BB.B6.E8.BF.9F) 进行校调。

### 2. 结束事件
| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_END      |  2006|  视频播放结束      | 
|PLAY_ERR_NET_DISCONNECT |  -2301  |  网络断连,且经多次重连亦不能恢复,更多重试请自行重启播放 | 

- **<font color='red'>如何判断直播已结束？</font>**
如果是**点播**，我们可以通过 PLAY_EVT_PLAY_END 事件判断是否已经播放结束。

 如果是**直播**，仅靠 SDK 本身是无法获知主播是否已经结束推流的。可预期的表现是：主播结束推流后，SDK 会很快发现数据流拉取失败（WARNING_RECONNECT），然后开始重试，直至三次重试失败后抛出 PLAY_ERR_NET_DISCONNECT 事件。

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


## 视频宽高 

**视频的宽高（分辨率）是多少？**
站在 SDK 的角度，如果只是拿到一个 URL 字符串，它是回答不出这个问题的。要知道视频画面的宽和高各是多少个 pixel, SDK 需要先访问云端服务器，直到加载到足够能够分析出视频画面大小的信息才行，所以对于视频信息而言，SDK 也只能以通知的方式告知您的应用程序。 

 **onNetStatus** 通知每秒都会被触发一次，目的是实时反馈当前的推流器状态，它就像汽车的仪表盘，可以告知您目前SDK内部的一些具体情况，以便您能对当前网络状况和视频信息等有所了解。
  
|   评估参数                   |  含义说明                   |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE     | 当前瞬时CPU使用率 | 
| **NET_STATUS_VIDEO_WIDTH**  | 视频分辨率 - 宽 |
| **NET_STATUS_VIDEO_HEIGHT**| 视频分辨率 - 高 |
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


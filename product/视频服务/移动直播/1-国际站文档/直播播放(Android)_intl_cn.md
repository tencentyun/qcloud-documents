## 基础知识
RTMP SDK 包含推流和播放两方面功能，推流为主播端功能，播放（分为直播和点播）为观众端功能。对接之前，我们先列表如下一些基本知识会大有裨益：

- **直播和点播**
<font color='blue'>直播</font> 的视频源是实时生成的，有人推流直播才有意义。所以，一旦主播停播，直播URL也就失效了，而且由于是实时直播，所以播放器在播直播视频的时候是没有进度条的。

 <font color='blue'>点播</font> 的视频源是云端的一个文件，文件只要没有被提供方删除，就随时可以播放， 而且由于整个视频都在服务器上，所以播放的时候是有进度条的哦。

- **协议的支持**
通常使用的直播协议如下，APP端推荐使用 FLV 协议的直播地址(以“http”打头，以“.flv”结尾)：
![](//mc.qcloudimg.com/static/img/94c348ff7f854b481cdab7f5ba793921/image.jpg)

 通常使用的点播协议如下，现在比较流行的是HLS(以“http”打头，以“.m3u8”结尾)的点播地址：
![](//mc.qcloudimg.com/static/img/4b42a00bb7ce2f58f362f35397734177/image.jpg)

## 特别说明
SDK <font color='red'>**不会对**</font> 播放地址的来源做限制，即您可以用它来播放腾讯云或非腾讯云的播放地址。但 SDK 中的播放器只支持 FLV 、RTMP 和 HLS（m3u8）三种格式的直播地址，以及 MP4、 HLS（m3u8）和 FLV 三种格式的点播地址。

## 对接攻略

### step 1: 添加View
为了能够展示播放器的视频画面，我们第一步要做的就是在布局xml文件里加入如下一段代码：
```xml
<com.tencent.rtmp.ui.TXCloudVideoView
            android:id="@+id/video_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:visibility="gone"/>
```

### step 2: 创建Player
接下来创建一个**TXLivePlayer**的对象，并使用 setPlayerView 接口将这它与我们刚刚添加到界面上的**video_view**控件进行关联。
```java
//mPlayerView即step1中添加的界面view
TXCloudVideoView mPlayerView = (TXCloudVideoView) view.findViewById(R.id.video_view);
//创建player对象
TXLivePlayer mLivePlayer = new TXLivePlayer(getActivity());
//关键player对象与界面view
mLivePlayer.setPlayerView(mPlayerView);
```

### step 3: 启动播放器
```java
String flvUrl = "http://2157.liveplay.myqcloud.com/live/2157_xxxx.flv";
mLivePlayer.startPlay(flvUrl, TXLivePlayer.PLAY_TYPE_LIVE_FLV); //推荐FLV
```
type 参数支持如下几种选项，有很多客户反馈 <font color='red'>**播放有快进现象**</font>，那是因为把 LIVE_FLV 和 VOD_FLV 弄混了导致的。

| 可选值 | 枚举值 | 含义 |
|---------|---------|---------|
| PLAY_TYPE_LIVE_RTMP | 0 | 传入的URL为RTMP直播地址 |
| PLAY_TYPE_LIVE_FLV | 1 | 传入的URL为FLV直播地址 |
| PLAY_TYPE_VOD_FLV | 2 | 传入的URL为FLV点播地址 |
| PLAY_TYPE_VOD_HLS | 3 | 传入的URL为HLS(m3u8)点播地址 |
| PLAY_TYPE_VOD_MP4 | 4 | 传入的URL为MP4点播地址 |
| PLAY_TYPE_LIVE_RTMP_ACC | 5 | 低延迟连麦链路直播地址（仅适合于连麦场景） |
| PLAY_TYPE_LOCAL_VIDEO | 6 | 手机本地视频文件 |

### step 4: 画面调整

- **view：大小和位置**
如需修改画面的大小及位置，直接调整 step1中添加的 “video_view” 控件的大小和位置即可。

- **setRenderMode：铺满or适应**

| 可选值 | 含义  |
|---------|---------|
| RENDER_MODE_FILL_SCREEN | 将图像等比例铺满整个屏幕，多余部分裁剪掉，此模式下画面不会留黑边，但可能因为部分区域被裁剪而显示不全。 | 
| RENDER_MODE_ADJUST_RESOLUTION | 将图像等比例缩放，适配最长边，缩放后的宽和高都不会超过显示区域，居中显示，画面可能会留有黑边。 | 

- **setRenderRotation：画面旋转**

| 可选值 | 含义  |
|---------|---------|
| RENDER_ROTATION_PORTRAIT | 正常播放（Home键在画面正下方） | 
| RENDER_ROTATION_LANDSCAPE | 画面顺时针旋转270度（Home键在画面正左方） | 

![](//mc.qcloudimg.com/static/img/ef948faaf1d62e8ae69e3fe94ab433dc/image.png)


### step 5: 进度调整
调整播放进度这个操作 <font color='red'>**仅对点播有效**</font> ，因为直播的视频源是实时的，没有调整进度的可能。
```java
// 调整进度
mLivePlayer.seek(seekBar.getProgress());
```

### step 6: 暂停播放
- **点播**
暂停对于点播的含义相信您不需要我再做赘述。

- **直播**
在直播过程中调用pause，效果等同于暂时停止拉流，播放器不会被销毁，但会显示最后一帧画面。

```java
// 暂停
mLivePlayer.pause();
// 继续
mLivePlayer.resume();
```

### step 7: 结束播放
结束播放时 <font color='red'>**记得销毁view控件**</font> ，尤其是在下次startPlay之前，否则会产生大量的内存泄露以及闪屏问题。

同时，在退出播放界面时，记得一定要调用渲染View的`onDestroy()`函数，否则可能会产生内存泄露和 <font color='red'> “Receiver not registered” </font>报警。
```java
@Override
public void onDestroy() {
    super.onDestroy();
    mLivePlayer.stopPlay(true); // true代表清除最后一帧画面
    mPlayerView.onDestroy(); 
}
```

stopPlay 的布尔型参数含义为—— “是否清除最后一帧画面”。早期版本的 RTMP SDK 的直播播放器没有 pause 的概念，所以通过这个布尔值来控制最后一帧画面的清除。

如果是点播播放结束后，也想保留最后一帧画面，您可以在收到播放结束事件后什么也不做，默认停在最后一帧。

### step 8: 硬件加速
对于蓝光级别（1080p）的画质，简单采用软件解码的方式很难获得较为流畅的播放体验，所以如果您的场景是以游戏直播为主，一般都推荐开启硬件加速。

软解和硬解的切换需要在切换之前先**stopPlay**，切换之后再**startPlay**，否则会产生比较严重的花屏问题。

```java
 mLivePlayer.stopPlay(true);
 mLivePlayer.enableHardwareDecode(true);
 mLivePlayer.startPlay(flvUrl, type);
```

### step 9: 截流录制（仅直播）
截流录制是直播播放场景下的一种扩展功能：观众在观看直播时，可以通过点击录制按钮把一段直播的内容录制下来，并通过视频分发平台（比如腾讯云的点播系统）发布出去，这样就可以在微信朋友圈等社交平台上以 UGC 消息的形式进行传播。

![](//mc.qcloudimg.com/static/img/2963b8f0af228976c9c7f2b11a514744/image.png)

```java
//指定一个 ITXVideoRecordListener 用于同步录制的进度和结果
mLivePlayer.setVideoRecordListener(recordListener);
//启动录制，可放于录制按钮的响应函数里，目前只支持录制视频源，弹幕消息等等目前还不支持
mLivePlayer.startRecord(int recordType);
// ...
// ...
//结束录制，可放于结束按钮的响应函数里
mLivePlayer.stopRecord();
```

- 录制的进度以时间为单位，由 ITXVideoRecordListener 的    onRecordProgress 通知出来。
- 录制好的文件以 MP4 文件的形式，由 ITXVideoRecordListener 的  onRecordComplete 通知出来。
- 视频的上传和发布由 TXUGCPublish 负责，具体使用方法可以参考 [短视频-文件发布](https://cloud.tencent.com/document/product/584/9367#6.-.E6.96.87.E4.BB.B6.E5.8F.91.E5.B8.8310)。


### step 10:视频截图
视频截图功能满足了观众想将主播直播过程中的精彩画面进行截图保存的需求。视频截图只会截图当前视频流的一帧原始画面，而不会截取整个屏幕内容。
```
mLivePlayer.snapshot(new ITXSnapshotListener() {
    @Override
    public void onSnapshot(Bitmap bmp) {
        if (null != bmp) {
           //获取到截图bitmap
        }
    }
});
```

### step 11: mp4本地缓存播放（仅点播）
点播播放器支持对mp4的本地缓存，在观看同一个视频的时候可以节省流量，默认没有开启，开启此功能需要配置两个参数：本地缓存目录及需要缓存的视频个数。

```
//如下代码用于展示点播场景下mp4本地缓存播放
//指定一个本地mp4缓存目录
mPlayConfig.setCacheFolderPath(Environment.getExternalStorageDirectory().getPath(); +"/txcache");
//指定本地最多缓存多少文件，避免缓存太多数据
mPlayConfig.setMaxCacheItems(2);
mLivePlayer.setConfig(mPlayConfig); 
// ...
//开始播放
mLivePlayer.startPlay(playUrl,_playType);                         
```

### step 12: 变速播放（仅点播）
点播播放器支持变速播放，通过接口`setRate`设置点播播放速率来完成，支持快速与慢速播放，如0.5X、1.0X、1.2X、2X等。

 ```
//如下代码用于展示点播倍速播放
//设置1.2倍速播放
mLivePlayer.setRate(1.2); 
// ...
//开始播放
mLivePlayer.startPlay(playUrl,_playType);
```

## 状态监听
腾讯云 RTMP SDK 一直坚持白盒化设计原则，你可以为 TXLivePlayer 对象绑定一个 **TXLivePlayListener**，之后SDK 的内部状态信息均会通过 onPlayEvent（事件通知） 和 onNetStatus（质量反馈）通知给您。

### 1. 播放事件
| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_BEGIN    |  2004|  视频播放开始，如果有转菊花什么的这个时候该停了 | 
|PLAY_EVT_PLAY_PROGRESS |  2005|  视频播放进度，会通知当前进度和总体进度，**仅在点播时有效**      | 
|PLAY_EVT_PLAY_LOADING  |  2007|  视频播放loading，如果能够恢复，之后会有BEGIN事件|  

- **不要在收到 PLAY_LOADING 后隐藏播放画面**
因为PLAY_LOADING -> PLAY_BEGIN 的时间长短是不确定的，可能是 5s 也可能是 5ms，有些客户考虑在 LOADING 时隐藏画面， BEGIN 时显示画面，会造成严重的画面闪烁（尤其是直播场景下）。推荐的做法是在视频播放画面上叠加一个半透明的 loading 动画。

- **LOADING 频繁与否多是由cacheTime决定的**
TXLivePlayConfig 中可以配置播放器的 cacheTime 属性，如果 cacheTime 属性被设置的很小，那么 LOADING 就会变得非常频繁，如果你您发现有频繁LOADING的情况出现，请参考[卡顿&延迟](#.E5.8D.A1.E9.A1.BF.26amp.3B.E5.BB.B6.E8.BF.9F) 进行校调。

- **PLAY_PROGRESS 播放进度的处理**
如果您对如何处理点播时的 PLAY_EVT_PLAY_PROGRESS 事件没有思路，可以参考示例代码-[播放进度](https://cloud.tencent.com/document/product/454/7887)。

### 2. 结束事件
| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_END      |  2006|  视频播放结束      | 
|PLAY_ERR_NET_DISCONNECT |  -2301  |  网络断连,且经多次重连抢救无效,可以放弃治疗,更多重试请自行重启播放 | 

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


### 5. 状态回调 
 **onNetStatus** 通知每秒都会被触发一次，目的是实时反馈当前的推流器状态，它就像汽车的仪表盘，可以告知您目前SDK内部的一些具体情况，以便您能对当前网络状况和视频质量等有所了解。
  
|   评估参数                   |  含义说明                   |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE     | 当前瞬时CPU使用率 | 
| NET_STATUS_VIDEO_WIDTH  | 视频分辨率 - 宽 |
| NET_STATUS_VIDEO_HEIGHT| 视频分辨率 - 高 |
|   NET_STATUS_NET_SPEED     | 当前的网络数据接收速度 |
|   NET_STATUS_NET_JITTER    | 网络抖动情况，抖动越大，网络越不稳定 |
|   NET_STATUS_VIDEO_FPS     | 当前流媒体的视频帧率    |
|   NET_STATUS_VIDEO_BITRATE | 当前流媒体的视频码率，单位 kbps|
|   NET_STATUS_AUDIO_BITRATE | 当前流媒体的音频码率，单位 kbps|
|   NET_STATUS_CACHE_SIZE    | 缓冲区（jitterbuffer）大小，缓冲区当前长度为 0，说明离卡顿就不远了|
| NET_STATUS_SERVER_IP | 连接的服务器IP | 

## 卡顿&延迟
在直播场景下，能决定一款 APP 产品的用户体验好坏的关键指标就是：卡顿率的高低和延迟的高低。

**播放器本身在其中起到了更为关键的决定性作用**，同样的网络环境和播放地址，不同的播放器可能会表现出完全不同的延迟和卡顿率。（比如 PC 浏览器上主流的 flash 播放器会因为播放策略过于简单粗暴，产生延迟越对越多的问题）

所以，在您完成本篇文档前面部分罗列的功能代码对接后，请务必阅读 [卡顿优化-播放端优化](https://cloud.tencent.com/document/product/454/7946#5.-.E6.92.AD.E6.94.BE.E7.AB.AF.E7.9A.84.E4.BC.98.E5.8C.969) 来校调出最适合您的业务场景的播放模式。

- **三种模式的特性对比**

![](//mc.qcloudimg.com/static/img/1d5a860ff74f9d026a36c04dd8bb27ef/image.jpg)

- **三种模式的对接代码**

```java
TXLivePlayConfig mPlayConfig = new TXLivePlayConfig();

//自动模式
mPlayConfig.setAutoAdjustCacheTime(true);
mPlayConfig.setMinAutoAdjustCacheTime(1);
mPlayConfig.setMaxAutoAdjustCacheTime(5);

//极速模式
mPlayConfig.setAutoAdjustCacheTime(true);
mPlayConfig.setMinAutoAdjustCacheTime(1);
mPlayConfig.setMaxAutoAdjustCacheTime(1);

//流畅模式
mPlayConfig.setAutoAdjustCacheTime(false);
mPlayConfig.setCacheTime(5);

mLivePlayer.setConfig(mPlayConfig);
//设置完成之后再启动播放

```


注意：各家云商一般都会在CDN端引入 **1.5s - 2s** 左右的延迟，这是不可避免的，所以 **总延迟 = CDN延迟 + CacheTime。**


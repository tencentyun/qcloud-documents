本文主要介绍腾讯云视立方 SDK 的直播播放功能。

## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | &#10003;  | &#10003;                                                            | -  | -  | &#10003;  | &#10003;                                                            |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 示例代码
针对开发者的接入反馈的高频问题，腾讯云提供有更加简洁的 API-Example 工程，方便开发者可以快速的了解相关 API 的使用，欢迎使用。

| 所属平台 |                         GitHub 地址                          |
| :------: | :----------------------------------------------------------: |
|   iOS    | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/MLVB-API-Example) |
| Android  | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/Android/MLVB-API-Example) |

## 对接攻略
[](id:step1)
### 步骤1：下载 SDK 开发包
[下载](https://cloud.tencent.com/document/product/1449/56978) SDK 开发包，并按照 [SDK 集成指引](https://cloud.tencent.com/document/product/1449/56987) 将 SDK 嵌入您的 App 工程中。

### 步骤2：添加 View
为了能够展示播放器的视频画面，我们第一步要做的就是在布局 xml 文件里加入如下一段代码：
```xml
<com.tencent.rtmp.ui.TXCloudVideoView
            android:id="@+id/video_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:visibility="gone"/>
```

### 步骤3：创建 Player
视频云 SDK 中的 **TXLivePlayer** 模块负责实现直播播放功能，并使用 **setPlayerView** 接口将它与我们刚添加到界面上的 **video_view** 控件进行关联。
```java
//mPlayerView 即步骤1中添加的界面 view
TXCloudVideoView mView = (TXCloudVideoView) view.findViewById(R.id.video_view);

//创建 player 对象
TXLivePlayer mLivePlayer = new TXLivePlayer(getActivity());

//关键 player 对象与界面 view
mLivePlayer.setPlayerView(mView);
```

### 步骤4：启动播放
```java
String flvUrl = "http://2157.liveplay.myqcloud.com/live/2157_xxxx.flv";
mLivePlayer.startPlay(flvUrl, TXLivePlayer.PLAY_TYPE_LIVE_FLV); //推荐 FLV
```

| 可选值 | 枚举值 | 含义 |
|---------|---------|---------|
| PLAY_TYPE_LIVE_RTMP | 0 | 传入的 URL 为 RTMP 直播地址 |
| PLAY_TYPE_LIVE_FLV | 1 | 传入的 URL 为 FLV 直播地址 |
| PLAY_TYPE_LIVE_RTMP_ACC | 5 | 低延迟链路地址（仅适合于连麦场景） |
| PLAY_TYPE_VOD_HLS | 3 | 传入的 URL 为 HLS（m3u8）播放地址 |


>?在 App 上我们不推荐使用 HLS 这种播放协议播放直播视频源（虽然它很适合用来做点播），因为延迟太高，在 App 上推荐使用 LIVE_FLV 或者 LIVE_RTMP 播放协议。

### 步骤5：画面调整

- **view：大小和位置**
如需修改画面的大小及位置，直接调整**步骤1**中添加的 video_view 控件的大小和位置即可。

- **setRenderMode：铺满或适应**

| 可选值 | 含义  |
|---------|---------|
| RENDER_MODE_FULL_FILL_SCREEN | 将图像等比例铺满整个屏幕，多余部分裁剪掉，此模式下画面不会留黑边，但可能因为部分区域被裁剪而显示不全 | 
| RENDER_MODE_ADJUST_RESOLUTION | 将图像等比例缩放，适配最长边，缩放后的宽和高都不会超过显示区域，居中显示，画面可能会留有黑边 | 

- **setRenderRotation：画面旋转**

| 可选值 | 含义  |
|---------|---------|
| RENDER_ROTATION_PORTRAIT | 正常播放（Home 键在画面正下方） | 
| RENDER_ROTATION_LANDSCAPE | 画面顺时针旋转270度（Home 键在画面正左方） | 

```Java
// 设置填充模式
mLivePlayer.setRenderMode(TXLiveConstants.RENDER_MODE_ADJUST_RESOLUTION);
// 设置画面渲染方向
mLivePlayer.setRenderRotation(TXLiveConstants.RENDER_ROTATION_LANDSCAPE);
```

![](//mc.qcloudimg.com/static/img/ef948faaf1d62e8ae69e3fe94ab433dc/image.png)


### 步骤6：暂停播放
对于直播播放而言，并没有真正意义上的暂停，所谓的直播暂停，只是**画面冻结**和**关闭声音**，而云端的视频源还在不断地更新着，所以当您调用 resume 的时候，会从最新的时间点开始播放，这跟点播是有很大不同的（点播播放器的暂停和继续与播放本地视频文件时的表现相同）。

```java
// 暂停
mLivePlayer.pause();
// 继续
mLivePlayer.resume();
```

### 步骤7：结束播放
结束播放时**需要销毁 view 控件**，尤其是在下次 startPlay 之前，否则**会产生大量的内存泄露以及闪屏问题**。

同时，在退出播放界面时，**需要调用渲染 View 的`onDestroy()`函数**，否则**可能会产生内存泄露和 Receiver not registered** 报警。
```java
@Override
public void onDestroy() {
    super.onDestroy();
    mLivePlayer.stopPlay(true); // true 代表清除最后一帧画面
    mView.onDestroy(); 
}
```

stopPlay 的布尔型参数含义为：“是否清除最后一帧画面”。早期版本的 RTMP SDK 的直播播放器没有 pause 的概念，所以通过这个布尔值来控制最后一帧画面的清除。

如果是点播播放结束后，也想保留最后一帧画面，您可以在收到播放结束事件后什么也不做，默认停在最后一帧。

<h3 id="Message">步骤8：消息接收</h3>
此功能可以在推流端将一些自定义 message 随着音视频线路直接下发到观众端，适用场景如下：

- 冲顶大会：推流端将**题目**下发到观众端，可以做到“音-画-题”完美同步。
- 秀场直播：推流端将**歌词**下发到观众端，可以在播放端实时绘制出歌词特效，因而不受视频编码的降质影响。
- 在线教育：推流端将**激光笔**和**涂鸦**操作下发到观众端，可以在播放端实时地划圈划线。

通过如下方案可以使用此功能：
- TXLivePlayConfig 中的 **setEnableMessage** 开关置为 **true**。
- TXLivePlayer 通过 **TXLivePlayListener** 监听消息，消息编号：**PLAY_EVT_GET_MESSAGE（2012）**

```java
//Android 示例代码
    mTXLivePlayer.setPlayListener(new ITXLivePlayListener() {
        @Override
        public void onPlayEvent(int event, Bundle param) {
            if (event == TXLiveConstants.PLAY_ERR_NET_DISCONNECT) {
                roomListenerCallback.onDebugLog("[AnswerRoom] 拉流失败：网络断开");
                roomListenerCallback.onError(-1, "网络断开，拉流失败");
            }
            else if (event == TXLiveConstants.PLAY_EVT_GET_MESSAGE) {
                String msg = null;
                try {
                    msg = new String(param.getByteArray(TXLiveConstants.EVT_GET_MSG), "UTF-8");
                    roomListenerCallback.onRecvAnswerMsg(msg);
                } catch (UnsupportedEncodingException e) {
                    e.printStackTrace();
                }
            }
        }
        @Override
        public void onNetStatus(Bundle status) {
        }
        });
```

### 步骤9：屏幕截图
通过调用 **snapshot**，您可以截取当前直播画面为一帧屏幕，此功能只会截取当前直播流的视频画面，如果您需要截取当前的整个 UI 界面，请调用 Android 的系统 API 来实现。

![](//mc.qcloudimg.com/static/img/f63830d29c16ce90d8bdc7440623b0be/image.jpg)

```java
mLivePlayer.snapshot(new ITXSnapshotListener() {
    @Override
    public void onSnapshot(Bitmap bmp) {
        if (null != bmp) {
           //获取到截图 bitmap
        }
    }
});
```

### 步骤10：截流录制
截流录制是直播播放场景下的一种扩展功能：观众在观看直播时，可以通过单击录制按钮把一段直播的内容录制下来，并通过视频分发平台（如腾讯云的点播系统）发布出去，这样就可以在微信朋友圈等社交平台上以 UGC 消息的形式进行传播。

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

- 录制的进度以时间为单位，由 ITXVideoRecordListener 的 onRecordProgress 通知出来。
- 录制好的文件以 MP4 文件的形式，由 ITXVideoRecordListener 的  onRecordComplete 通知出来。
- 视频的上传和发布由 TXUGCPublish 负责，具体使用方法可以参考 [短视频 - 文件发布](https://cloud.tencent.com/document/product/584/15535#.E5.AF.B9.E6.8E.A5.E6.B5.81.E7.A8.8B)。

### 步骤11：清晰度无缝切换
日常使用中，网络情况在不断发生变化。在网络较差的情况下，最好适度降低画质，以减少卡顿；反之，网速比较好，可以观看更高画质。
传统切流方式一般是重新播放，会导致切换前后画面衔接不上、黑屏、卡顿等问题。使用无缝切换方案，在不中断直播的情况下，能直接切到另条流上。

清晰度切换在直播开始后，任意时间都可以调用。调用方式如下
```java
// 正在播放的是流 http://5815.liveplay.myqcloud.com/live/5815_62fe94d692ab11e791eae435c87f075e.flv，
// 现切换到码率为900kbps的新流上
mLivePlayer.switchStream("http://5815.liveplay.myqcloud.com/live/5815_62fe94d692ab11e791eae435c87f075e_900.flv");
```

>?清晰度无缝切换功能需要在后台配置 PTS 对齐，如您需要可 [提交工单](https://console.cloud.tencent.com/workorder) 申请使用。


### 步骤12：直播回看
时移功能是腾讯云推出的特色能力，可以在直播过程中，随时观看回退到任意直播历史时间点，并能在此时间点一直观看直播。非常适合游戏、球赛等互动性不高，但观看连续性较强的场景。

```java
// 设置直播回看前，先调用 startPlay
// 开始播放 ...
TXLiveBase.setAppID("1253131631"); // 配置 appId
mLivePlayer.prepareLiveSeek();     // 后台请求直播起始时间
```
配置正确后，在 PLAY_EVT_PLAY_PROGRESS 事件里，当前进度就不是从0开始，而是根据实际开播时间计算而来。
调用 seek 方法，就能从历史事件点重新直播
```java
mLivePlayer.seek(600); // 从第10分钟开始播放
```

接入时移需要在后台打开以下配置：

- 录制：配置时移时长、时移储存时长。
- 播放：时移获取元数据。

时移功能处于公测申请阶段，如您需要可 [提交工单](https://console.cloud.tencent.com/workorder) 申请使用。

<h2 id="Delay">延时调节</h2>
腾讯云 SDK 的直播播放（LVB）功能，并非基于 ffmpeg 做二次开发， 而是采用了自研的播放引擎，所以相比于开源播放器，在直播的延迟控制方面有更好的表现，我们提供了三种延迟调节模式，分别适用于：秀场、游戏以及混合场景。

- **三种模式的特性对比**

| 控制模式 | 卡顿率 | 平均延迟 | 适用场景 | 原理简述 |
|---------|---------|---------| ------ | ----- |
| 极速模式 | 较流畅偏高 | 2s - 3s | 美女秀场（冲顶大会）| 在延迟控制上有优势，适用于对延迟大小比较敏感的场景|
| 流畅模式 | 卡顿率最低 | >= 5s | 游戏直播（企鹅电竞） | 对于超大码率的游戏直播（例如吃鸡）非常适合，卡顿率最低|
| 自动模式 | 网络自适应 | 2s - 8s | 混合场景 | 观众端的网络越好，延迟就越低；观众端网络越差，延迟就越高 |


- **三种模式的对接代码**

```java
TXLivePlayConfig mPlayConfig = new TXLivePlayConfig();
//
//自动模式
mPlayConfig.setAutoAdjustCacheTime(true);
mPlayConfig.setMinAutoAdjustCacheTime(1);
mPlayConfig.setMaxAutoAdjustCacheTime(5);
//
//极速模式
mPlayConfig.setAutoAdjustCacheTime(true);
mPlayConfig.setMinAutoAdjustCacheTime(1);
mPlayConfig.setMaxAutoAdjustCacheTime(1);
//
//流畅模式
mPlayConfig.setAutoAdjustCacheTime(false);
mPlayConfig.setCacheTime(5);
//
mLivePlayer.setConfig(mPlayConfig);
//设置完成之后再启动播放
```

>?更多关于卡顿和延迟优化的技术知识，可以阅读 [视频卡顿怎么办？](https://cloud.tencent.com/document/product/454/7946)

<h2 id="RealTimePlay">超低延时播放</h2>

支持**400ms左右的超低延迟播放**，是腾讯云直播播放器的一个特点，它可以用于一些对时延要求极为苛刻的场景，例如**远程夹娃娃或者主播连麦**等，关于这个特性，您需要知道：

- **该功能是不需要开通的**
该功能并不需要提前开通，但是要求直播流必须位于腾讯云，跨云商实现低延时链路的难度不仅仅是技术层面的。

- **播放地址需要带防盗链**
播放 URL 不能用普通的 CDN URL，必须要带防盗链签名，防盗链签名的计算方法见 [**txTime&txSecret**](https://cloud.tencent.com/document/product/267/32735)。

- **播放类型需要指定 ACC**
在调用 startPlay 函数时，需要指定 type 为 **PLAY_TYPE_LIVE_RTMP_ACC**，SDK 会使用 RTMP-UDP 协议拉取直播流。

- **该功能有并发播放限制**
目前最多同时**10路**并发播放，设置这个限制的原因并非是技术能力限制，而是希望您只考虑在互动场景中使用（例如连麦时只给主播使用， 或者夹娃娃直播中只给操控娃娃机的玩家使用），避免因为盲目追求低延时而产生不必要的费用损失（低延迟线路的价格要贵于 CDN 线路）。

- **Obs 的延时是不达标的**
推流端如果是 [TXLivePusher](https://cloud.tencent.com/document/product/454/7885)，请使用 [setVideoQuality](https://cloud.tencent.com/document/product/454/7885#7.-.E8.AE.BE.E5.AE.9A.E7.94.BB.E9.9D.A2.E6.B8.85.E6.99.B0.E5.BA.A6) 将`quality`设置为 MAIN_PUBLISHER 或者 VIDEO_CHAT。Obs 的推流端积压比较严重，是无法达到低延时效果的。

- **该功能按播放时长收费**
本功能按照播放时长收费，费用跟拉流的路数有关系，跟音视频流的码率无关，具体价格请参考 [价格总览](https://cloud.tencent.com/document/product/454/8008)。



## SDK 事件监听
您可以为 TXLivePlayer 对象绑定一个 **TXLivePlayListener**，之后 SDK 的内部状态信息均会通过 onPlayEvent（事件通知） 和 onNetStatus（状态反馈）通知给您。

### 1. 播放事件
| 事件 ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_CONNECT_SUCC     |  2001    | 已经连接服务器                |
| PLAY_EVT_RTMP_STREAM_BEGIN|  2002    | 已经连接服务器，开始拉流（仅播放 RTMP 地址时会抛送） |
| PLAY_EVT_RCV_FIRST_I_FRAME|  2003    | 网络接收到首个可渲染的视频数据包（IDR）  |
|PLAY_EVT_PLAY_BEGIN    |  2004|  视频播放开始，如果有转菊花什么的这个时候该停了 | 
|PLAY_EVT_PLAY_LOADING  |  2007|  视频播放 loading，如果能够恢复，之后会有 BEGIN 事件|  
|PLAY_EVT_GET_MESSAGE   |  2012|  用于接收夹在音视频流中的消息，详情参考 [消息接收](#Message)|  

**不要在收到 PLAY_LOADING 后隐藏播放画面**：因为 PLAY_LOADING -> PLAY_BEGIN 的时间长短是不确定的，可能是5s或5ms，有些用户考虑在 LOADING 时隐藏画面， BEGIN 时显示画面，会造成严重的画面闪烁（尤其是直播场景下）。**推荐的做法是在视频播放画面上叠加一个半透明的 loading 动画**。

### 2. 结束事件
| 事件 ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_END      |  2006|  视频播放结束      | 
|PLAY_ERR_NET_DISCONNECT |  -2301  |  网络断连，且经多次重连亦不能恢复,更多重试请自行重启播放 | 

#### 如何判断直播已结束？
基于各种标准的实现原理不同，很多直播流通常没有结束事件（2006）抛出，此时可预期的表现是：主播结束推流后，SDK 会很快发现数据流拉取失败（WARNING_RECONNECT），然后开始重试，直至三次重试失败后抛出 PLAY_ERR_NET_DISCONNECT 事件。

因此，2006和-2301都要监听，用来作为直播结束的判定事件。


### 3. 警告事件
如下的这些事件您可以不用关心，我们只是基于白盒化的 SDK 设计理念，将事件信息同步出来。

| 事件 ID                 |    数值  |  含义说明                    |   
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



## 视频宽高 

#### 视频的宽高（分辨率）是多少？
要知道视频画面的宽和高各是多少个 pixel, SDK 需要先访问云端服务器，直到加载到能够分析出视频画面大小的信息才行，所以对于视频信息而言，SDK 也只能以通知的方式告知您的应用程序。 

#### onNetStatus 通知
 **onNetStatus** 通知每秒都会被触发一次，目的是实时反馈当前的推流器状态，它就像汽车的仪表盘，可以告知您目前 SDK 内部的一些具体情况，以便您能对当前网络状况和视频信息等有所了解。 
  
|   评估参数                   |  含义说明                   |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE     | 当前瞬时 CPU 使用率 | 
| **NET_STATUS_VIDEO_WIDTH**  | 视频分辨率 - 宽 |
| **NET_STATUS_VIDEO_HEIGHT**| 视频分辨率 - 高 |
|   NET_STATUS_NET_SPEED     | 当前的网络数据接收速度 |
|   NET_STATUS_NET_JITTER    | 网络抖动情况，抖动越大，网络越不稳定 |
|   NET_STATUS_VIDEO_FPS     | 当前流媒体的视频帧率    |
|   NET_STATUS_VIDEO_BITRATE | 当前流媒体的视频码率，单位：kbps|
|   NET_STATUS_AUDIO_BITRATE | 当前流媒体的音频码率，单位：kbps|
|   NET_STATUS_CACHE_SIZE    | 缓冲区（jitterbuffer）大小，缓冲区当前长度为0，说明离卡顿就不远了|
| NET_STATUS_SERVER_IP | 连接的服务器 IP | 

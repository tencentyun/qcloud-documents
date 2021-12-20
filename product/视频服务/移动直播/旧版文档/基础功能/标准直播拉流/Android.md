## 基础知识
本文主要介绍视频云 SDK 的直播播放功能。

#### **直播和点播**
- **直播（LIVE）**的视频源是主播实时推送的。因此，主播停止推送后，播放端的画面也会随即停止，而且由于是实时直播，所以播放器在播直播 URL 的时候是没有进度条的。

- **点播（VOD）**的视频源是云端的一个视频文件，只要未被从云端移除，视频就可以随时播放， 播放中您可以通过进度条控制播放位置，腾讯视频和优酷、土豆等视频网站上的视频观看就是典型的点播场景。

#### **协议的支持**
通常使用的直播协议如下，App 端推荐使用 FLV 协议的直播地址（以“http”开头，以“.flv”结尾）：

| 直播协议 | 优点 | 缺点 | 播放延迟 |
|---------|---------|---------|---------|
| FLV | 成熟度高、高并发无压力 | 需集成 SDK 才能播放 | 2s - 3s |
| RTMP | 优质线路下理论延迟最低 | 高并发情况下表现不佳 | 1s - 3s |
| HLS（m3u8） | 手机浏览器支持度高 | 延迟非常高 | 10s - 30s |


## 特别说明
- **是否有限制？**
视频云 SDK **不会对**播放地址的来源做限制，即您可以用它来播放腾讯云或非腾讯云的播放地址。但视频云 SDK 中的播放器只支持 FLV 、RTMP 和 HLS（m3u8）三种格式的直播地址，以及 MP4、 HLS（m3u8）和 FLV 三种格式的点播地址。

- **历史因素**
SDK 早期版本只有 TXLivePlayer 一个 Class 承载直播和点播功能，但是由于点播功能越做越多，我们最终在 SDK 3.5 版本开始，将点播功能单独分离出来，交由 TXVodPlayer 负责。但是为了保证编译通过，您在 TXLivePlayer 中依然可以看到类似 seek 等点播才具备的功能。


## 对接攻略
[](id:step_1)
### step 1：添加 View
为了能够展示播放器的视频画面，我们第一步要做的就是在布局 xml 文件里加入如下一段代码：
```xml
<com.tencent.rtmp.ui.TXCloudVideoView
            android:id="@+id/video_view"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_centerInParent="true"
            android:visibility="visible"/>
```

[](id:step_2)
### step 2：创建 Player
视频云 SDK 中的 **TXLivePlayer** 模块负责实现直播播放功能，并使用 **setPlayerView** 接口将它与我们刚刚添加到界面上的 **video_view** 控件进行关联。
```java
//mPlayerView 即 step1 中添加的界面 view
TXCloudVideoView mView = (TXCloudVideoView) view.findViewById(R.id.video_view);

//创建 player 对象
TXLivePlayer mLivePlayer = new TXLivePlayer(getActivity());

//关键 player 对象与界面 view
mLivePlayer.setPlayerView(mView);
```

[](id:step_3)
### step 3：启动播放
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

**关于 HLS(m3u8)**
在 App 上我们不推荐使用 HLS 这种播放协议播放直播视频源（虽然它很适合用做点播），因为延迟太高。在 App 上推荐使用 LIVE_FLV 或者 LIVE_RTMP 播放协议。

[](id:step_4)
### step 4：画面调整

- **view：大小和位置**
如需修改画面的大小及位置，直接调整 [step1](#step_1) 中添加的`video_view`控件的大小和位置即可。

- **setRenderMode：铺满or适应**
<table>
<thead><tr><th>可选值</th><th>含义</th></tr></thead>
<tbody><tr>
<td>RENDER_MODE_FULL_FILL_SCREEN</td>
<td>将图像等比例铺满整个屏幕，多余部分裁剪掉，此模式下画面不会留黑边，但可能因为部分区域被裁剪而显示不全。</td>
</tr><tr>
<td>RENDER_MODE_ADJUST_RESOLUTION</td>
<td>将图像等比例缩放，适配最长边，缩放后的宽和高都不会超过显示区域，居中显示，画面可能会留有黑边。</td></tr>
</tbody></table>

- **setRenderRotation：画面旋转**
<table>
<thead><tr><th>可选值</th><th>含义</th></tr>
</thead>
<tbody><tr>
<td>RENDER_ROTATION_PORTRAIT</td>
<td>正常播放（Home 键在画面正下方）</td>
</tr><tr>
<td>RENDER_ROTATION_LANDSCAPE</td>
<td>画面顺时针旋转 270 度（Home 键在画面正左方）</td></tr>
</tbody></table>

```Java
// 设置填充模式
mLivePlayer.setRenderMode(TXLiveConstants.RENDER_MODE_ADJUST_RESOLUTION);
// 设置画面渲染方向
mLivePlayer.setRenderRotation(TXLiveConstants.RENDER_ROTATION_LANDSCAPE);
```

![](https://main.qcloudimg.com/raw/89e7b5b2b6b944fe8377cf9f2bcff573.jpg)

[](id:step_5)
### step 5：暂停播放
对于直播播放而言，并没有真正意义上的暂停，所谓的直播暂停，只是**画面冻结**和**关闭声音**，而云端的视频源还在不断地更新着，所以当您调用 resume 的时候，会从最新的时间点开始播放，这是和点播对比的最大不同点（点播播放器的暂停和继续与播放本地视频文件时的表现相同)。

```java
// 暂停
mLivePlayer.pause();
// 继续
mLivePlayer.resume();
```

[](id:step_6)
### step 6：结束播放
结束播放时**记得销毁 view 控件**，尤其是在下次 startPlay 之前，否则会产生大量的内存泄露以及闪屏问题。
同时，在退出播放界面时，记得一定要调用渲染 View 的 `onDestroy()` 函数，否则可能会产生内存泄露和“Receiver not registered”报警。
```java
@Override
public void onDestroy() {
    super.onDestroy();
    mLivePlayer.stopPlay(true); // true 代表清除最后一帧画面
    mView.onDestroy(); 
}
```

stopPlay 的布尔型参数含义为—— “是否清除最后一帧画面”。早期版本的 RTMP SDK 的直播播放器没有 pause 的概念，所以通过这个布尔值来控制最后一帧画面的清除。
如果是点播播放结束后，也想保留最后一帧画面，您可以在收到播放结束事件后什么也不做，默认停在最后一帧。

[](id:step_7)[](id:Message)
### step 7：消息接收
此功能可以在推流端将一些自定义 message 随着音视频线路直接下发到观众端，适用场景例如：
 
- 冲顶大会：推流端将**题目**下发到观众端，可以做到“音-画-题”完美同步。
- 秀场直播：推流端将**歌词**下发到观众端，可以在播放端实时绘制出歌词特效，因而不受视频编码的降质影响。
- 在线教育：推流端将**激光笔**和**涂鸦**操作下发到观众端，可以在播放端实时地划圈、划线。

通过如下方案可以使用此功能：
- TXLivePlayConfig 中的 **setEnableMessage** 开关置为 **true**。
- TXLivePlayer 通过 **TXLivePlayListener** 监听消息，消息编号：**PLAY_EVT_GET_MESSAGE （2012）**

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

[](id:step_8)
### step 8：屏幕截图
通过调用 **snapshot** 您可以截取当前直播画面为一帧屏幕，此功能只会截取当前直播流的视频画面，如果您需要截取当前的整个 UI 界面，请调用 Android 的系统 API 来实现。
![](https://main.qcloudimg.com/raw/1439eff8e2b9629abf92960e1b784f56.jpg)
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

[](id:step_9)
### step 9：截流录制
截流录制是直播播放场景下的一种扩展功能：观众在观看直播时，可以通过单击录制按钮把一段直播的内容录制下来，并通过视频分发平台（例如腾讯云的点播系统）发布出去，这样就可以在微信朋友圈等社交平台上以 UGC 消息的形式进行传播。
![](https://main.qcloudimg.com/raw/c5277659170dccb7e317f4386e75c265.png)

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

- 录制的进度以时间为单位，由 ITXVideoRecordListener 的 `onRecordProgress` 通知出来。
- 录制好的文件以 MP4 文件的形式，由 ITXVideoRecordListener 的 `onRecordComplete` 通知出来。
- 视频的上传和发布由 TXUGCPublish 负责，具体使用方法可以参考 [视频上传（Android）](https://cloud.tencent.com/document/product/584/15535)。

[](id:step_10)
### step 10：清晰度无缝切换
日常使用中，网络情况在不断发生变化。在网络较差的情况下，最好适度降低画质，以减少卡顿；反之，网速比较好，可以提高观看画质。
传统切流方式一般是重新播放，会导致切换前后画面衔接不上、黑屏、卡顿等问题。使用无缝切换方案，在不中断直播的情况下，能直接切到另条流上。

清晰度切换在直播开始后，任意时间都可以调用。调用方式如下：
```java
// 正在播放的是流http://5815.liveplay.myqcloud.com/live/5815_62fe94d692ab11e791eae435c87f075e.flv，
// 现切换到码率为900kbps的新流上
mLivePlayer.switchStream("http://5815.liveplay.myqcloud.com/live/5815_62fe94d692ab11e791eae435c87f075e_900.flv");
```
当 switchStream() 方法没有回调时，则需要检查返回值，如果 URL 相同或上一个切换没完成，则切换时会返回错误。错误码解析请参见 [错误码表](https://cloud.tencent.com/document/product/454/17246)。

>? 清晰度无缝切换功能需要在后台配置 PTS 对齐，如您需要可 [提交工单](https://console.cloud.tencent.com/workorder) 申请使用。

[](id:step_11)
### step 11：直播回看
时移功能是腾讯云推出的特色能力，可以在直播过程中，随时观看回退到任意直播历史时间点，并能在此时间点一直观看直播。非常适合游戏、球赛等互动性不高，但观看连续性较强的场景。

```java
// 设置直播回看前，先调用startPlay
// 开始播放 ...
TXLiveBase.setAppID("1253131631"); // 配置appId
mLivePlayer.prepareLiveSeek();     // 后台请求直播起始时间
```
配置正确后，在 PLAY_EVT_PLAY_PROGRESS 事件里，当前进度就不是从0开始，而是根据实际开播时间计算而来。
调用 seek 方法，就能从历史时间点重新直播：
```java
mLivePlayer.seek(600); // 从第10分钟开始播放
```

>? time 为视频流时间点，当前取值为600，单位为秒。


接入时移功能需要在后台打开2处配置：

1. 录制：配置时移时长、时移储存时长。
2. 播放：时移获取元数据。

>? 时移功能处于公测申请阶段，如您需要可 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请使用。

[](id:Delay)
## 延时调节
腾讯云 SDK 的直播播放功能，并非基于 ffmpeg 做二次开发， 而是采用了自研的播放引擎，所以相比于开源播放器，在直播的延迟控制方面有更好的表现，我们提供了三种延迟调节模式，分别适用于：秀场、游戏以及混合场景。

- **三种模式的特性对比**
<table>
<thead><tr><th>控制模式</th><th>卡顿率</th><th>平均延迟</th><th>适用场景</th><th>原理简述</th></tr></thead>
<tbody><tr>
<td>极速模式</td>
<td>较流畅偏高</td>
<td>2s - 3s</td>
<td>美女秀场（冲顶大会）</td>
<td>在延迟控制上有优势，适用于对延迟大小比较敏感的场景</td>
</tr><tr>
<td>流畅模式</td>
<td>卡顿率最低</td>
<td>≥ 5s</td>
<td>游戏直播（企鹅电竞）</td>
<td>对于超大码率的游戏直播（例如绝地求生）非常适合，卡顿率最低</td>
</tr><tr>
<td>自动模式</td>
<td>网络自适应</td>
<td>2s - 8s</td>
<td>混合场景</td>
<td>观众端的网络越好，延迟就越低；观众端网络越差，延迟就越高</td>
</tr>
</tbody></table>

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
mPlayConfig.setMinAutoAdjustCacheTime(5);
mPlayConfig.setMaxAutoAdjustCacheTime(5);
//
mLivePlayer.setConfig(mPlayConfig);
//设置完成之后再启动播放
```

>? 更多关于卡顿和延迟优化的技术知识，可以阅读 [如何优化视频卡顿？](https://cloud.tencent.com/document/product/454/7946)

[](id:RealTimePlay)
## 超低延时播放
支持**400ms**左右的超低延迟播放是腾讯云直播播放器的一个特点，它可以用于一些对时延要求极为苛刻的场景，例如**远程夹娃娃**或者**主播连麦**等，关于这个特性，您需要知道：

- **播放地址需要带防盗链**
播放 URL 不能用普通的 CDN URL，必须要带防盗链签名和 bizid 参数，防盗链签名的计算方法请参见 [防盗链计算](https://cloud.tencent.com/document/product/267/32735)。
bizid 的获取需要进入 [域名管理](https://console.cloud.tencent.com/live/domainmanage) 页面，在默认域名中出现的第一个数字即为 bizid，如图所示：
![](https://main.qcloudimg.com/raw/d4bae92945f16569ab5446d320fcf663.png)
如果您的防盗链地址为：
`rtmp://domain/live/test?txTime=5c2acacc&txSecret=b77e812107e1d8b8f247885a46e1bd34`
则加速流地址为：
`rtmp://domain/live/test?txTime=5c2acacc&txSecret=b77e812107e1d8b8f247885a46e1bd34&bizid=2157`

>? 防盗链计算默认使用推流防盗链 Key。

- **播放类型需要指定 ACC**
在调用 startPlay 函数时，需要指定 type 为 **PLAY_TYPE_LIVE_RTMP_ACC**，SDK 会使用 RTMP-UDP 协议拉取直播流。
- **该功能有并发播放限制**
目前最多同时10路并发播放，设置这个限制的原因并非是技术能力限制，而是希望您只考虑在互动场景中使用（例如连麦时只给主播使用，或者夹娃娃直播中只给操控娃娃机的玩家使用），避免因为盲目追求低延时而产生不必要的费用损失（低延迟线路的价格要贵于 CDN 线路）。
- **Obs 的延时是不达标的**
推流端如果是 [TXLivePusher](https://cloud.tencent.com/document/product/454/7885)，请使用 [setVideoQuality](https://cloud.tencent.com/document/product/454/7885#7.-.E8.AE.BE.E5.AE.9A.E7.94.BB.E9.9D.A2.E6.B8.85.E6.99.B0.E5.BA.A6) 将 `quality`  设置为 MAIN_PUBLISHER 或者 VIDEO_CHAT。
- **该功能按播放时长收费**
本功能按照播放时长收费，费用跟拉流的路数有关系，跟音视频流的码率无关，具体价格请参考 [价格总览](https://cloud.tencent.com/document/product/454/8008#ACC)。



## SDK 事件监听
您可以为 TXLivePlayer 对象绑定一个 **TXLivePlayListener**，之后 SDK 的内部状态信息均会通过 onPlayEvent（事件通知） 和 onNetStatus（状态反馈）通知给您。

### 播放事件
| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_EVT_CONNECT_SUCC     |  2001    | 已经连接服务器            |
| PLAY_EVT_RTMP_STREAM_BEGIN|  2002    | 已经连接服务器，开始拉流（仅播放 RTMP 地址时会抛送） |
| PLAY_EVT_RCV_FIRST_I_FRAME|  2003    | 收到首帧数据，越快收到此消息说明链路质量越好  |
| PLAY_EVT_PLAY_BEGIN    |  2004|  视频播放开始，如果您自己做 loading，会需要它 | 
| PLAY_EVT_PLAY_PROGRESS    |  2005|  播放进度，如果您在直播中收到此消息，说明错用成了 TXVodPlayer |
| PLAY_EVT_PLAY_END    |  2006|  播放结束，HTTP-FLV 的直播流是不抛这个事件的 |
| PLAY_EVT_PLAY_LOADING |  2007|  视频播放进入缓冲状态，缓冲结束之后会有 PLAY_BEGIN 事件|  
| PLAY_EVT_START_VIDEO_DECODER  |  2008| 视频解码器开始启动（2.0 版本以后新增） |  
| PLAY_EVT_CHANGE_RESOLUTION    |  2009|  视频分辨率发生变化（分辨率在 EVT_PARAM 参数中）|  
| PLAY_EVT_GET_PLAYINFO_SUCC    |  2010|  如果您在直播中收到此消息，说明错用成了 TXVodPlayer|  
| PLAY_EVT_CHANGE_ROTATION  |  2011|  如果您在直播中收到此消息，说明错用成了 TXVodPlayer|  
| PLAY_EVT_GET_MESSAGE  |  2012|  获取夹在视频流中的自定义 SEI 消息，消息的发送需使用 TXLivePusher |  
| PLAY_EVT_VOD_PLAY_PREPARED    |  2013|  如果您在直播中收到此消息，说明错用成了 TXVodPlayer|  
| PLAY_EVT_VOD_LOADING_END  |  2014|  如果您在直播中收到此消息，说明错用成了 TXVodPlayer|  
| PLAY_EVT_STREAM_SWITCH_SUCC   |  2015|  直播流切换完成，请参考 [清晰度无缝切换](#step_10) |  

**不要在收到 PLAY_LOADING 后隐藏播放画面**
因为 `PLAY_LOADING -> PLAY_BEGIN` 的等待时间长短是不确定的，可能是5s也可能是5ms，有些客户考虑在 LOADING 时隐藏画面， BEGIN 时显示画面，会造成严重的画面闪烁（尤其是直播场景下）。推荐的做法是在视频播放画面上叠加一个背景透明的 loading 动画。

### 结束事件
| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
|PLAY_EVT_PLAY_END      |  2006|  视频播放结束      | 
|PLAY_ERR_NET_DISCONNECT |  -2301  |  网络断连，且经多次重连亦不能恢复，更多重试请自行重启播放 | 

 **如何判断直播已结束？**
RTMP 协议中规定了直播结束事件，但是 HTTP-FLV 则没有，如果您在播放 FLV 的地址时直播结束了，可预期的 SDK 的表现是：SDK 会很快发现数据流拉取失败（WARNING_RECONNECT），然后开始重试，直至三次重试失败后抛出 PLAY_ERR_NET_DISCONNECT 事件。
所以`2006`和`-2301`都要监听，用来作为直播结束的判定事件。


### 警告事件
如下的这些事件您可以不用关心，我们只是基于白盒化的 SDK 设计理念，将事件信息同步出来。

| 事件ID                 |    数值  |  含义说明                    |   
| :-------------------  |:-------- |  :------------------------ | 
| PLAY_WARNING_VIDEO_DECODE_FAIL   |  2101  | 当前视频帧解码失败  |
| PLAY_WARNING_AUDIO_DECODE_FAIL   |  2102  | 当前音频帧解码失败  |
| PLAY_WARNING_RECONNECT           |  2103  | 网络断连，已启动自动重连（重连超过三次就直接抛送 PLAY_ERR_NET_DISCONNECT）|
| PLAY_WARNING_RECV_DATA_LAG       |  2104  | 网络来包不稳：可能是下行带宽不足，或由于主播端出流不均匀|
| PLAY_WARNING_VIDEO_PLAY_LAG      |  2105  | 当前视频播放出现卡顿|
| PLAY_WARNING_HW_ACCELERATION_FAIL|  2106  | 硬解启动失败，采用软解   |
| PLAY_WARNING_VIDEO_DISCONTINUITY |  2107  | 当前视频帧不连续，可能丢帧|
| PLAY_WARNING_DNS_FAIL            |  3001  | RTMP-DNS 解析失败（仅播放 RTMP 地址时会抛送）|
| PLAY_WARNING_SEVER_CONN_FAIL     |  3002  | RTMP 服务器连接失败（仅播放 RTMP 地址时会抛送）|
| PLAY_WARNING_SHAKE_FAIL          |  3003  | RTMP 服务器握手失败（仅播放 RTMP 地址时会抛送）|


## 获取视频分辨率
通过 onPlayEvent 通知的 **PLAY_EVT_CHANGE_RESOLUTION** 事件可以获取视频流当前的宽高比，这是获取视频流分辨率的最快速办法，大约会在启动播放后的100ms - 200ms左右就能得到。
视频的宽高信息位于 TXLivePlayListener 的 `onPlayEvent(int event, Bundle param)` 通知中的 **param** 参数中。

| 参数 | 含义 | 数值 |
|---------|---------|---------|
| EVT_PARAM1 | 视频宽度 | 分辨率数值，如1920 |
| EVT_PARAM2 | 视频高度 | 分辨率数值，如1080 |

## 定时触发的状态通知

 **onNetStatus** 通知每秒都会被触发一次，目的是实时反馈当前的推流器状态，它就像汽车的仪表盘，可以告知您目前 SDK 内部的一些具体情况，以便您能对当前网络状况和视频信息等有所了解。
  
|   评估参数                   |  含义说明                   |   
| :------------------------  |  :------------------------ | 
| NET_STATUS_CPU_USAGE     | 当前瞬时 CPU 使用率 | 
| NET_STATUS_VIDEO_WIDTH  | 视频分辨率 - 宽 |
| NET_STATUS_VIDEO_HEIGHT| 视频分辨率 - 高 |
|   NET_STATUS_NET_SPEED     | 当前的网络数据接收速度 |
|   NET_STATUS_NET_JITTER    | 网络抖动情况，抖动越大，网络越不稳定 |
|   NET_STATUS_VIDEO_FPS     | 当前流媒体的视频帧率    |
|   NET_STATUS_VIDEO_BITRATE | 当前流媒体的视频码率，单位 kbps|
|   NET_STATUS_AUDIO_BITRATE | 当前流媒体的音频码率，单位 kbps|
|   NET_STATUS_CACHE_SIZE    | 缓冲区（jitterbuffer）大小，缓冲区当前长度为0，说明离卡顿就不远了|
| NET_STATUS_SERVER_IP | 连接的服务器 IP | 

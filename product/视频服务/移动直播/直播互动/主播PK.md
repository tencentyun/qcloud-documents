## 主播 PK 方案介绍
### 主播 PK 流程
**一般情况主播 PK 流程如下：**
 - PK 前：主播们各自用 RTC 地址推流。
 - PK 时：主播们之间相互播放对方的 RTC 流地址。
 - PK 后：主播们停止播放对方的 RTC 地址。

### 方案演示
下面是 [MLVB-API-Example Demo](https://cloud.tencent.com/document/product/454/60985) 的演示效果。
<dx-tabs>
::: 直播前
<table>
<tr> 
  <th style="text-align:center" width=15%>主播 A 和<br>主播 B</th>
    <td><div align=center><img src="https://qcloudimg.tencent-cloud.cn/raw/2ba7a460bc235b1902c6681265708d72.jpeg" width=250px></div></td>
  <td><div align=center><img src="https://qcloudimg.tencent-cloud.cn/raw/801563570d4579d1564aa3ea86e9b174.jpeg" width=250px></div></td>
  <td><div align=center><img src="https://qcloudimg.tencent-cloud.cn/raw/3a4ba9ffa543ae83329d10de0df7a1ff.jpeg" width=250px></div></td>
</tr><tr>
  <th style="text-align:center">观众</th>
<td><div align=center><img src="https://qcloudimg.tencent-cloud.cn/raw/a051c9a0c54159344839398afc2a98de.jpeg" width=250px></div></td>
<td><div align=center><img src="https://qcloudimg.tencent-cloud.cn/raw/fc81c197632a2813de0a1220102c0239.jpeg" width=250px></div></td>
<td><div align=center><img src="https://qcloudimg.tencent-cloud.cn/raw/d3a312da2056d86e8d45fe30e536f9a9.jpeg" width=250px></div></td>
</tr></table>
:::
::: PK 操作
<table>
<tr> 
  <th style="text-align:center" width=15%>主播 A</th>
    <td><div align=center><img src="https://qcloudimg.tencent-cloud.cn/raw/802cc1411e89b0ad0a6f367e764d392e.png" width=250px></div></td>
    <td><div align=center><img src="https://qcloudimg.tencent-cloud.cn/raw/8d19ef3684718ef3452efd71a25af3bc.png" width=250px></div></td>
</tr><tr>
  <th style="text-align:center">主播 B</th>
  <td><div align=center><img src="https://qcloudimg.tencent-cloud.cn/raw/33e97d536e3acb493df44dce26154735.png" width=250px></div></td>
<td><div align=center><img src="https://qcloudimg.tencent-cloud.cn/raw/1aa60704584fd713e4f7bcb849953611.png" width=250px></div></td>
</tr><tr>
  <th style="text-align:center">主播 A 的观众</th>
  <td  colspan=2><div align=center><img src="https://qcloudimg.tencent-cloud.cn/raw/0c588816f4fd646d3ee09a88b121101d.png" width=250px></div></td>
</tr></table>
:::
::: PK 中
<table>
<tr> 
  <th><div align=center width=15%>主播 A（手机 A)</div></th>
  <th><div align=center>主播 B（手机 B）</div></th>
  <th><div align=center>主播 A 的观众（手机 C)</div></th>
</tr><tr>
  <td>
  <div align=center><img src="https://main.qcloudimg.com/raw/d3f44a38c294cec0e0d5d4597948795f.png" width=250px></div>
</td><td>
  <div align=center><img src="https://main.qcloudimg.com/raw/3d56a195860bc82fab2653aaf37b9414.png" width=250px></div>
</td><td>
  <div align=center><img src="https://main.qcloudimg.com/raw/df3ae3b3dcebb39404e50dfbc7667ad5.png" width=250px></div>
</td>
</tr></table>
:::
</dx-tabs>

## RTC PK 功能实现
如下示意图，主播 A 有观众 A，主播 B 有观众 B，如果主播 A 和 B 进行 PK，需要做的事情非常简单：
- 主播 A：开始播放主播 B 的流，同时发起混流指令，把 A 和 B 的内容合成一路，供主播 A 的观众观看。
- 主播 B：开始播放主播 A 的流，同时发起混流指令，把 B 和 A 的内容合成一路，供主播 B 的观众观看。
- 观众 A 和 B：无需变化，继续 CDN 播放即可，只不过会看到各自主播混流后的 PK 画面。

<img src="https://qcloudimg.tencent-cloud.cn/raw/a917bf9068f5890ddc55e5ff2b7cd32a.png">

[](id:step1)
### 1. 主播 A 开始推流
调用 `V2TXLivePusher` 组件开始主播 A 的推流。URL 拼装方案请参见 [如何拼装 URL](https://cloud.tencent.com/document/product/454/7915#rtc_push)。
<dx-codeblock>
::: java java
V2TXLivePusher pusher = new V2TXLivePusherImpl(this, V2TXLiveMode.TXLiveMode_RTC);
pushURLA= "trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=A&usersig=xxx";
pusher.startPush(pushURLA);
:::
::: Objective-C ObjectiveC
V2TXLivePusher *pusher = [[V2TXLivePusher alloc] initWithLiveMode:V2TXLiveMode_RTC];
NSString *pushURLA = @"trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=A&usersig=xxx";
[pusher startPush:pushURLA];
:::
</dx-codeblock>

[](id:step2)
### 2. 主播 B 开始推流
调用 `V2TXLivePusher` 组件开始主播 B 的推流。URL 拼装方案请参见 [如何拼装 URL](https://cloud.tencent.com/document/product/454/7915#rtc_play)。
<dx-codeblock>
::: java java
V2TXLivePusher pusher = new V2TXLivePusherImpl(this, V2TXLiveMode.TXLiveMode_RTC);
pushURLB "trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=B&usersig=xxx";
pusher.startPush(pushURLB);
:::
::: Objective-C ObjectiveC
V2TXLivePusher *pusher = [[V2TXLivePusher alloc] initWithLiveMode:V2TXLiveMode_RTC];
NSString *pushURLB = @"trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=B&;usersig=xxx";
[pusher startPush:pushURLB];
:::
</dx-codeblock>

[](id:step3)
### 3. 开始 PK 
主播 A 和主播 B 分别调用  `V2TXLivePlayer`  开始播放对方的流，此时主播 A 和主播 B 即进入 RTC PK 互动直播场景中。URL 拼装方案请参见 [如何拼装 URL](https://cloud.tencent.com/document/product/454/7915#rtc)。
<dx-codeblock>
::: java java
// 主播A
V2TXLivePlayer player = new V2TXLivePlayerImpl(mContext);
playURLB = "trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&userId=A&usersig=xxx&appscene=live"
player.startPlay(playURLB);
...

// 主播B
V2TXLivePlayer player = new V2TXLivePlayerImpl(mContext);
playURLA= "trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&userId=B&usersig=xxx&appscene=live"
player.startPlay(playURLA);
:::
::: Objective-C ObjectiveC
// 主播A
V2TXLivePlayer *player = [[V2TXLivePlayer alloc] init];
NSString *playURLB = "trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&userId=A&usersig=xxx&appscene=live"
[player setRenderView:view];
[player startPlay:playURLB];
...

// 主播B
V2TXLivePlayer *player = [[V2TXLivePlayer alloc] init];
 NSString *playURLA = "trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&userId=B&usersig=xxx&appscene=live"
[player setRenderView:view];
[player startPlay:playURLA];
:::
</dx-codeblock>

[](id:step4)
### 4. PK 成功，观看 PK 内容
PK 成功后，观众有两种方式可以观看 PK 内容。
1. 主播 A 和主播 B 的观众各自调用 V2TXLivePlayer 开始播放另外一名主播的推流内容。
2. 主播 A 和主播 B 进行混流，观众端播放 URL 保持不变。
主播 A 和主播 B 发起一次混流操作，也就是主播将自己和对方主播混合成一路流，自己直播间的观众就可以在看到自己和对方主播进行互动。 主播 A 和 B 各自调用 setMixTranscodingConfig 接口启动云端混流，调用时需要设置音频相关的参数，例如 `音频采样率 audioSampleRate`、`音频码率 audioBitrate` 和 `声道数 audioChannels` 等。

**示例代码** ：
<dx-codeblock>
::: java java
// 主播 A 
V2TXLiveDef.V2TXLiveTranscodingConfig config = new V2TXLiveDef.V2TXLiveTranscodingConfig();

// 设置分辨率为 720 × 1280, 码率为 1500kbps，帧率为 20FPS
config.videoWidth      = 720;
config.videoHeight     = 1280;
config.videoBitrate    = 1500;
config.videoFramerate  = 20;
config.videoGOP        = 2;
config.audioSampleRate = 48000;
config.audioBitrate    = 64;
config.audioChannels   = 2;
config.mixStreams      = new ArrayList<>();

// 主播 A 摄像头的画面位置
V2TXLiveDef.V2TXLiveMixStream local = new V2TXLiveDef.V2TXLiveMixStream();
local.userId   = "localUserId";
local.streamId = null; // 本地画面不用填写 streamID，远程需要
local.x        = 0;
local.y        = 0;
local.width    = videoWidth;
local.height   = videoHeight;
local.zOrder   = 0;   // zOrder 为 0 代表主播画面位于最底层
config.mixStreams.add(local);

// PK主播 B 的画面位置
V2TXLiveDef.V2TXLiveMixStream remoteB = new V2TXLiveDef.V2TXLiveMixStream();
remoteB.userId   = "remoteUserIdB";
remoteB.streamId = "remoteStreamIdB"; // 本地画面不用填写 streamID，远程需要
remoteB.x        = 400; //仅供参考
remoteB.y        = 800; //仅供参考
remoteB.width    = 180; //仅供参考
remoteB.height   = 240; //仅供参考
remoteB.zOrder   = 1;
config.mixStreams.add(remoteB);

// 发起云端混流
pusher.setMixTranscodingConfig(config);

//主播 B
V2TXLiveDef.V2TXLiveTranscodingConfig config = new V2TXLiveDef.V2TXLiveTranscodingConfig();

// 设置分辨率为 720 × 1280, 码率为 1500kbps，帧率为 20FPS
config.videoWidth      = 720;
config.videoHeight     = 1280;
config.videoBitrate    = 1500;
config.videoFramerate  = 20;
config.videoGOP        = 2;
config.audioSampleRate = 48000;
config.audioBitrate    = 64;
config.audioChannels   = 2;
config.mixStreams      = new ArrayList<>();

// 主播 B 摄像头的画面位置
V2TXLiveDef.V2TXLiveMixStream local = new V2TXLiveDef.V2TXLiveMixStream();
local.userId   = "localUserId";
local.streamId = null; // 本地画面不用填写 streamID，远程需要
local.x        = 0;
local.y        = 0;
local.width    = videoWidth;
local.height   = videoHeight;
local.zOrder   = 0;   // zOrder 为 0 代表主播画面位于最底层
config.mixStreams.add(local);

// PK主播 A 的画面位置
V2TXLiveDef.V2TXLiveMixStream remoteA = new V2TXLiveDef.V2TXLiveMixStream();
remoteA.userId   = "remoteUserIdA";
remoteA.streamId = "remoteStreamIdA"; // 本地画面不用填写 streamID，远程需要
remoteA.x        = 400; //仅供参考
remoteA.y        = 800; //仅供参考
remoteA.width    = 180; //仅供参考
remoteA.height   = 240; //仅供参考
remoteA.zOrder   = 1;
config.mixStreams.add(remoteA);

// 发起云端混流
pusher.setMixTranscodingConfig(config);
:::
::: Objective-C ObjectiveC
// 主播 A 
V2TXLiveTranscodingConfig *config = [[V2TXLiveTranscodingConfig alloc] init];

// 设置分辨率为 720 × 1280, 码率为 1500kbps，帧率为 20FPS
config.videoWidth      = 720;
config.videoHeight     = 1280;
config.videoBitrate    = 1500;
config.videoFramerate  = 20;
config.videoGOP        = 2;
config.audioSampleRate = 48000;
config.audioBitrate    = 64;
config.audioChannels   = 2;

// 主播 A 摄像头的画面位置
V2TXLiveMixStream *local = [[V2TXLiveMixStream alloc] init];
local.userId   = @"localUserId";
local.streamId = nil; // 本地画面不用填写 streamID，远程需要
local.x        = 0;
local.y        = 0;
local.width    = videoWidth;
local.height   = videoHeight;
local.zOrder   = 0;   // zOrder 为 0 代表主播画面位于最底层

// PK主播 B 的画面位置
V2TXLiveMixStream *remoteB = [[V2TXLiveMixStream alloc] init];
remoteB.userId   = @"remoteUserIdB";
remoteB.streamId = @"remoteStreamIdB"; // 本地画面不用填写 streamID，远程需要
remoteB.x        = 400; //仅供参考
remoteB.y        = 800; //仅供参考
remoteB.width    = 180; //仅供参考
remoteB.height   = 240; //仅供参考
remoteB.zOrder   = 1;

//设置混流 streams
config.mixStreams = @[local,remoteB];

// 发起云端混流
pusher.setMixTranscodingConfig(config);

// 主播 B
V2TXLiveTranscodingConfig *config = [[V2TXLiveTranscodingConfig alloc] init];

// 设置分辨率为 720 × 1280, 码率为 1500kbps，帧率为 20FPS
config.videoWidth      = 720;
config.videoHeight     = 1280;
config.videoBitrate    = 1500;
config.videoFramerate  = 20;
config.videoGOP        = 2;
config.audioSampleRate = 48000;
config.audioBitrate    = 64;
config.audioChannels   = 2;

// 主播 A 摄像头的画面位置
V2TXLiveMixStream *local = [[V2TXLiveMixStream alloc] init];
local.userId   = @"localUserId";
local.streamId = nil; // 本地画面不用填写 streamID，远程需要
local.x        = 0;
local.y        = 0;
local.width    = videoWidth;
local.height   = videoHeight;
local.zOrder   = 0;   // zOrder 为 0 代表主播画面位于最底层

// PK主播 A 的画面位置
V2TXLiveMixStream *remoteA = [[V2TXLiveMixStream alloc] init];
remoteA.userId   = @"remoteUserIdA";
remoteA.streamId = @"remoteStreamIdA"; // 本地画面不用填写 streamID，远程需要
remoteA.x        = 400; //仅供参考
remoteA.y        = 800; //仅供参考
remoteA.width    = 180; //仅供参考
remoteA.height   = 240; //仅供参考
remoteA.zOrder   = 1;

//设置混流 streams
config.mixStreams = @[local,remoteA];

// 发起云端混流
pusher.setMixTranscodingConfig(config);
:::
</dx-codeblock>

>! 发起云端混流后，默认混流 ID，是发起混流者的 ID，如果需要指定流 ID，需要进行传入。

[](id:que)
## 常见问题
[](id:que1)
#### 1. 为什么使用 `V2TXLivePusher&V2TXLivePlayer` 接口时，同一台设备不支持使用相同 streamid 同时推流和拉流，而 `TXLivePusher&TXLivePlayer` 可以支持？

当前 `V2TXLivePusher&V2TXLivePlayer` 是 [腾讯云 TRTC](https://cloud.tencent.com/document/product/647/45151) 协议实现，其基于 UDP 的超低延时的私有协议，考虑到用户的具体使用场景，不支持**同一台设备，使用相同的 streamid，一边推超低延时流，一边拉超低延时的流**。

[](id:que2)
#### 2. V2TXLivePusher&V2TXLivePlayer 如何设置音质或者画质呢？
我们有提供对应的音质和画质的设置接口，具体请参见 [设置画面质量](https://cloud.tencent.com/document/product/454/56600)。

[](id:que3)
#### 3. `V2TXLivePusher#startPush` 收到错误码：`-5` 代表什么意思？
`-5` 表示由于许可证无效，因此无法调用API，对应的枚举值为：[V2TXLIVE_ERROR_INVALID_LICENSE](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLiveCode__ios.html)，更多错误码请参见 [API 状态码](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLiveCode__ios.html)。

[](id:que4)
#### 4. RTC连麦方案的时延性有可以参考的数据吗？
主播连麦的延时 &lt; 200ms，主播和观众的延时在 100ms - 1000ms。

[](id:que5)
#### 5. RTC 推流成功后，使用 CDN 拉流一直提示404？
检查一下是否有开启实时音视频服务的旁路直播功能，基本原理是 RTC 协议推流后，如果需要使用 CDN 播放，RTC 会在后台服务中旁路流信息到 CDN 上。


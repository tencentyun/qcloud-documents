本文主要讲述如何实现 RTC 连麦功能。
如下示意图，用户 A 是主播，B 和 C 都是观众，如果 B 连麦，需要做的事情非常简单：

- 观众 B：启动 `trtc://` 协议推流，播放流也从 CDN 切到超低延迟的 `trtc://` 协议。
- 主播 A：开始播放观众 B 的流，同时发起混流指令，把 A 和 B 的内容合成一路。
- 观众 C：无需变化，继续 CDN 播放即可，只不过会看到混流后的连麦画面。
<img src="https://main.qcloudimg.com/raw/00e5376f86d39517b3f8c9ad1dca16e4.png">

[](id:step_live1)

### 1. 主播 RTC 推流
主播 A 开始推流，调用 `V2TXLivePusher` 组件开始主播 A 的推流。
<dx-codeblock>
::: java java
V2TXLivePusher pusher = new V2TXLivePusherImpl(this, V2TXLiveMode.TXLiveMode_RTC);
pushURLA= "trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&amp;userId=A&amp;usersig=xxx";
pusher.startPush(pushURLA);
:::
::: Objective-C ObjectiveC
V2TXLivePusher *pusher = [[V2TXLivePusher alloc] initWithLiveMode:V2TXLiveMode_RTC];
NSString *pushURLA = @"trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&amp;userId=A&amp;usersig=xxx";
[pusher startPush:pushURLA];
:::
</dx-codeblock>

[](id:step_live2)
### 2. 观众 CDN 拉流

所有观众观看主播 A 直播，调用 `V2TXLivePlayer` 开始播放主播 A 的流。
<dx-codeblock>
::: java java
V2TXLivePlayer player = new V2TXLivePlayerImpl(mContext);
/**
 * 这里使用CDN拉流，支持flv，hls，webrtc协议，任选一种协议。flv，hls等标准协议价格更合理，webrtc快直播能够提供更低延迟的互动体验。
 * playURLA= "http://3891.liveplay.myqcloud.com/live/streamidA.flv";
 * playURLA= "http://3891.liveplay.myqcloud.com/live/streamidA.hls";
 * playURLA= "webrtc://3891.liveplay.myqcloud.com/live/streamidA"
 */
player.startPlay(playURLA);
:::
::: Objective-C ObjectiveC
V2TXLivePlayer * player = [[V2TXLivePlayer alloc] init];
/**
 * 这里使用CDN拉流，支持flv，hls，webrtc协议，任选一种协议。flv，hls等标准协议价格更合理，webrtc快直播能够提供更低延迟的互动体验。
 * NSString *playURLA= @"http://3891.liveplay.myqcloud.com/live/streamidA.flv";
 * NSString *playURLA= @"http://3891.liveplay.myqcloud.com/live/streamidA.hls";
 * NSString *playURLA= @"webrtc://3891.liveplay.myqcloud.com/live/streamidA"
 */
[player setRenderView:view];
[player startPlay:playURLA];
:::
</dx-codeblock>

[](id:step_live3)
### 3. 观众发起连麦
其中观众 B 调用 `V2TXLivePusher` 发起推流（后续会称呼为连麦观众 B）。
<dx-codeblock>
::: java java
V2TXLivePusher pusher = new V2TXLivePusherImpl(this,V2TXLiveMode.TXLiveMode_RTC);
pushURLB= "trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&amp;userId=B&amp;usersig=xxx";
pusher.startPush(pushURLB);
:::
::: Objective-C ObjectiveC
V2TXLivePusher *pusher = [[V2TXLivePusher alloc] initWithLiveMode:V2TXLiveMode_RTC];
NSString *pushURLB = @"trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&amp;userId=B&amp;usersig=xxx";
[pusher startPush:pushURLB];
:::
</dx-codeblock>

[](id:step_live4)
### 4. 进入连麦状态
主播 A 调用 `V2TXLivePlayer` 使用 RTC 协议拉取放**连麦观众 B** 的流。
<dx-codeblock>
::: java java
V2TXLivePlayer player = new V2TXLivePlayerImpl(mContext);
playURLB= "trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&amp;userId=B&amp;usersig=xxx&amp;appscene=live";
player.startPlay(playURLB);
:::
::: Objective-C ObjectiveC
V2TXLivePlayer * player = [[V2TXLivePlayer alloc] init];
NSString* playURLB = @"trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&amp;userId=B&amp;usersig=xxx&amp;appscene=live";
[player setRenderView:view];
[player startPlay:playURLB];
:::
</dx-codeblock>

同时，**连麦观众 B** 调用 `V2TXLivePlayer` 切换至 RTC 协议，开始播放主播 A 的流。
<dx-codeblock>
::: java java
V2TXLivePlayer player = new V2TXLivePlayerImpl(mContext);
playURLA= "trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&amp;userId=A&amp;usersig=xxx&amp;appscene=live";
player.startPlay(playURLA);
:::
::: Objective-C ObjectiveC
V2TXLivePlayer * player = [[V2TXLivePlayer alloc] init];
NSString* playURLA = @"trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&amp;userId=A&amp;usersig=xxx&amp;appscene=live";
[player setRenderView:view];
[player startPlay:playURLA];
:::
</dx-codeblock>

此时主播 A 和 **连麦观众 B**  即可进入超低延时的实时互动场景中。


[](id:step_live5)
### 5. 连麦成功后，进行混流

为了保证观众可以看到连麦观众 B 的画面，这里主播 A 需要发起一次混流操作。也就是将主播 A 自己和连麦观众 B，混合成一路流。观众可以在一路流上看到主播和连麦观众进行互动。A 调用 setMixTranscodingConfig 接口启动云端混流，调用时需要设置音频相关的参数，例如 `音频采样率 audioSampleRate`、`音频码率 audioBitrate` 和 `声道数 audioChannels` 等。
如果您的业务场景中也包含视频，需同时设置视频相关的参数，例如 `视频宽度 videoWidth`、`视频高度 videoHeight`、`视频码率 videoBitrate`、`视频帧率 videoFramerate` 等。

**示例代码** ：
<dx-codeblock>
::: java java
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

// 主播摄像头的画面位置
V2TXLiveDef.V2TXLiveMixStream local = new V2TXLiveDef.V2TXLiveMixStream();
local.userId   = "localUserId";
local.streamId = null; // 本地画面不用填写 streamID，远程需要
local.x        = 0;
local.y        = 0;
local.width    = videoWidth;
local.height   = videoHeight;
local.zOrder   = 0;   // zOrder 为 0 代表主播画面位于最底层
config.mixStreams.add(local);

// 连麦者的画面位置
V2TXLiveDef.V2TXLiveMixStream remoteA = new V2TXLiveDef.V2TXLiveMixStream();
remoteA.userId   = "remoteUserIdA";
remoteA.streamId = "remoteStreamIdA"; // 本地画面不用填写 streamID，远程需要
remoteA.x        = 400; //仅供参考
remoteA.y        = 800; //仅供参考
remoteA.width    = 180; //仅供参考
remoteA.height   = 240; //仅供参考
remoteA.zOrder   = 1;
config.mixStreams.add(remoteA);

// 连麦者的画面位置
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
:::
::: Objective-C ObjectiveC
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

// 主播摄像头的画面位置
V2TXLiveMixStream *local = [[V2TXLiveMixStream alloc] init];
local.userId   = @"localUserId";
local.streamId = nil; // 本地画面不用填写 streamID，远程需要
local.x        = 0;
local.y        = 0;
local.width    = videoWidth;
local.height   = videoHeight;
local.zOrder   = 0;   // zOrder 为 0 代表主播画面位于最底层

// 连麦者的画面位置
V2TXLiveMixStream *remoteA = [[V2TXLiveMixStream alloc] init];
remoteA.userId   = @"remoteUserIdA";
remoteA.streamId = @"remoteStreamIdA"; // 本地画面不用填写 streamID，远程需要
remoteA.x        = 400; //仅供参考
remoteA.y        = 800; //仅供参考
remoteA.width    = 180; //仅供参考
remoteA.height   = 240; //仅供参考
remoteA.zOrder   = 1;

// 连麦者的画面位置
V2TXLiveMixStream *remoteB = [[V2TXLiveMixStream alloc] init];
remoteB.userId   = @"remoteUserIdB";
remoteB.streamId = @"remoteStreamIdB"; // 本地画面不用填写 streamID，远程需要
remoteB.x        = 400; //仅供参考
remoteB.y        = 800; //仅供参考
remoteB.width    = 180; //仅供参考
remoteB.height   = 240; //仅供参考
remoteB.zOrder   = 1;

//设置混流 streams
config.mixStreams = @[local,remoteA,remoteB];

// 发起云端混流
pusher.setMixTranscodingConfig(config);
:::
</dx-codeblock>

>! 发起云端混流后，默认混流 ID，是发起混流者的 ID，如果需要指定流 ID，需要进行传入。


这样其他观众在观看时，就可以看到 A，B 两个主播的连麦互动。



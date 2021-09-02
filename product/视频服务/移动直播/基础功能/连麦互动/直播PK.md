
## PK 方案介绍
目前，在 [**连麦互动 - RTMP方案**](https://cloud.tencent.com/document/product/454/14606) 中，腾讯云移动直播 SDK 提供连麦互动组件 `MLVBLiveRoom` 用来帮助开发者快速实现 PK 需求，为了更好的满足开发者针对 PK 功能的需求，腾讯云新增了基于 RTC 协议的 PK 方案，同时提供了更加简单灵活的 V2 接口。

移动直播 V2 接口同时支持通过 RTMP 协议及 RTC 协议进行推流/PK，开发者可根据自身需求选择适合的方案，对比如下：

| 对比项   | RTMP 方案                  | RTC 方案                                           |
| -------- | -------------------------- | -------------------------------------------------- |
| 协议     | RTMP 基于 TCP 协议            | RTC 基于 UDP 协议（更适合流媒体传输）                 |
| QoS      | 弱网抗性能力弱             | 50%丢包率可正常视频观看，70%丢包率可正常语音连麦 |
| 支持区域 | 仅支持中国内地（大陆）地区 | 全球覆盖                                           |
| 使用产品 | 需开通移动直播、云直播服务 | 需开通移动直播、云直播、实时音视频服务             |
| 价格     | 0.016元/分钟               | 阶梯价格，详情请参见 [费用介绍](https://cloud.tencent.com/document/product/454/60981) |


## RTC PK 方案演示
移动直播 SDK 提供了新的 V2 接口：` V2TXLivePusher` （推流）、` V2TXLivePlayer` （拉流），用来帮助客户实现更加灵活、更低延时、更多人数的直播互动场景。开播端可以利用 V2 提供的 RTC 推流能力，默认情况下，观众端观看则可使用 CDN 方式进行拉流。 CDN 观看费用较低。如果主播端有 PK 需求，直接互相播放对方的流即可。RTC PK 需要另外开通服务，具体步骤请参见 [TODO](https://tcloud-doc.isd.com/document/product/454/60985?!editLang=zh&!preview#step4) 配置。
下面是 [MLVB-API-Example](https://github.com/tencentyun/MLVBSDK/tree/master/Android/MLVB-API-Example) Demo 的演示效果。

### 演示图示

####  直播前
<table>
<tr> 
	<th><div align=center>主播 A（手机 A)</div></th>
	<th><div align=center>主播 B（手机 B）</div></th>
	<th><div align=center>主播 A 的观众（手机 B）</div></th>
</tr><tr>
	<td>
	<div align=center><img src="https://main.qcloudimg.com/raw/d1468d2b7b57458e1b4c9d399edafe25.png"></div>
</td><td>
	<div align=center><img src="https://main.qcloudimg.com/raw/b4d8c701b5e7214f96fc9391ce8c8a5f.png"></div>
</td><td>
	<div align=center><img src="https://main.qcloudimg.com/raw/5553ac9e0039c38be81979d4678638ab.png"></div>
</td>
</tr></table>

####  PK 中
<table>
<tr> 
	<th><div align=center>主播 A（手机 A）</div></th>
	<th><div align=center>主播 B（手机 B）</div></th>
	<th><div align=center>主播 A 的观众（手机 C）</div></th>
</tr><tr>
<td>
	<div align=center><img src="https://main.qcloudimg.com/raw/a4b22306830a0cf7754df0668d0f7dfa.png"></div>
</td><td>
	<div align=center><img src="https://main.qcloudimg.com/raw/1c22fd4c4b7cbf8696050386ad3591ab.png"></div>
</td><td>
	<div align=center><img src="https://main.qcloudimg.com/raw/e85046243380bb1c505033c74e1f97a4.png"></div>
</td>
</tr></table>

## RTC PK 功能实现
如下示意图，主播 A 有观众 A，主播 B 有观众 B，如果主播 A 和 B 进行 PK，需要做的事情非常简单：
- 主播 A：开始播放主播 B 的流，同时发起混流指令，把 A 和 B 的内容合成一路，供主播 A 的观众观看。
- 主播 B：开始播放主播 A 的流，同时发起混流指令，把 B 和 A 的内容合成一路，供主播 B 的观众观看。
- 观众 A 和 B：无需变化，继续 CDN 播放即可，只不过会看到各自主播混流后的 PK 画面。

<img src="https://main.qcloudimg.com/raw/638542d7e0bbb8fb3979ebfb00177f9d.png">


### 1. 主播 A 开始推流
调用 `V2TXLivePusher` 组件开始主播 A 的推流。
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

### 2. 主播 B 开始推流
调用 `V2TXLivePusher` 组件开始主播 B 的推流。
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

### 3. 开始 PK 
主播 A 和主播 B 分别调用  `V2TXLivePlayer`  开始播放对方的流，此时主播 A 和主播 B 即进入 RTC PK 互动直播场景中。
<dx-codeblock>
::: java java
// 主播A
V2TXLivePlayer player = new V2TXLivePlayerImpl(mContext);
playURLB = "trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&userId=B&usersig=xxx&appscene=live"
player.startPlay(playURLB);
...

// 主播B
V2TXLivePlayer player = new V2TXLivePlayerImpl(mContext);
playURLA= "trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&userId=A&usersig=xxx&appscene=live"
player.startPlay(playURLA);
:::
::: Objective-C ObjectiveC
// 主播A
V2TXLivePlayer *player = [[V2TXLivePlayer alloc] init];
NSString *playURLB = "trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&userId=B&usersig=xxx&appscene=live"
[player setRenderView:view];
[player startPlay:playURLB];
...

// 主播B
V2TXLivePlayer *player = [[V2TXLivePlayer alloc] init];
 NSString *playURLA = "trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&userId=A&usersig=xxx&appscene=live"
[player setRenderView:view];
[player startPlay:playURLA];
:::
</dx-codeblock>

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

>? 此处开发者可能会有疑问：貌似新的 RTC 连麦方案还需要我们自己维护一套房间和用户状态，这样不是更麻烦吗？是的，**没有更好的方案，只有更适合自己的方案**，我们也有考虑到这样的场景：
- 如果对时延和并发要求并不高的场景，可以继续使用连麦互动的旧方案。
- 如果既想用到 V2 相关的接口，但是又不想维护一套单独的房间状态，可以尝试搭配 [腾讯云 IM SDK](https://cloud.tencent.com/document/product/269)，快速实现相关逻辑。
	
## RTC 连麦方案怎么计算费用
RTC 连麦互动直播服务费用按所有参与连麦的用户产生的 [视频时长](#v_duration) 和 [语音时长](#s_duration) 来统计连麦服务产生的用量。

>!时长统计精度为秒，以当月累计秒数转换成分钟数后进行计费，不足一分钟按一分钟计。

[](id:v_duration)
### 视频时长
视频时长是指所有用户观看其他参与连麦的用户视频流的累计时间。RTC 连麦会根据用户**实际接收到的视频分辨率**划分视频档位，然后分别对不同档位的视频时长进行计费。

**视频档位与分辨率的对应关系如下表所示**：

| 视频档位 | 实际接收分辨率               |
| -------- | ---------------------------- |
| 标清 SD  | 不高于640 × 480（含）        |
| 高清 HD  | 640 × 480 - 1280 × 720（含） |
| 超清 HD+ | 高于1280 × 720               |

- 用户观看视频时，不管该视频里面有没有包含音频，都只统计一次视频时长，不会重复计算语音时长。
- 单个用户同时观看多路视频流时，其观看的每一路视频时长将分别统计后叠加计算。


[](id:s_duration)
### 语音时长
语音时长指所有用户收听其他参与连麦的用户音频流的时间。

- 只有当用户没有观看视频流时，才会统计语音时长。
- 当用户同时收听多个用户音频流时，统计语音时长时会去除掉重叠部分的时长。

[](id:Fixed_price)
### 服务定价
RTC 连麦互动直播服务的刊例价如下表所示：

| 计费项   | 单价（元/千分钟） |
| -------- | ----------------- |
| 语音     | 7.00              |
| 标清 SD  | 14.00             |
| 高清 HD  | 28.00             |
| 超清 HD+ | 105.00            |

[](id:Billing_method)
### 计费方式
即支付方式，RTC 连麦互动直播支持**预付费套餐包**和**后付费**，默认采用预付费套餐包，后付费只能通过购买的套餐包消耗完或过期后自动开通，无法直接开通。

[](id:pre-payment)
#### 预付费套餐包
RTC 连麦互动直播服务为您提供音视频通用套餐包，可按照 **1:2:4:15** 分别抵扣语音、标清 SD、高清 HD 和超清 HD+ 时长，例如1分钟高清视频时长扣除4分钟通用套餐包时长。
通用套餐包定价如下表所示：
<table>
     <tr>
         <th style="text-align:center">套餐包类型</th>  
         <th style="text-align:center">套餐包时长（千分钟）</th> 
         <th style="text-align:center">刊例价（元/千分钟）</th> 
         <th style="text-align:center">套餐内单价（元/千分钟）</th> 
         <th style="text-align:center">套餐包价格（元）</th> 
          <th style="text-align:center">折扣</th> 
     </tr>
     <tr>
         <td style="text-align:center" rowspan="4">固定套餐包</td>   
         <td style="text-align:center">25</td>   
         <td style="text-align:center">7.00</td>
         <td style="text-align:center">6.720</td>
         <td style="text-align:center">168.00</td>   
         <td style="text-align:center">96%</td>     
     </tr> 
     <tr>
         <td style="text-align:center">250 </td>   
         <td style="text-align:center">7.00</td>
         <td style="text-align:center">6.352</td>
         <td style="text-align:center">1588.00</td>   
         <td style="text-align:center">91%</td>   
     </tr> 
     <tr>
         <td style="text-align:center">1000 </td>   
         <td style="text-align:center">7.00</td>
         <td style="text-align:center">5.968</td>
         <td style="text-align:center">5968.00</td>   
         <td style="text-align:center">85%</td>   
     </tr> 
     <tr>
         <td style="text-align:center">3000</td>   
         <td style="text-align:center">7.00</td>
         <td style="text-align:center">5.630</td>
         <td style="text-align:center">16888.00</td>   
         <td style="text-align:center">80%</td>   
     </tr> 
     <tr>
         <td style="text-align:center" rowspan="5">自定义套餐包</td>   
         <td style="text-align:center">0 ＜ X ＜ 25</td>   
         <td style="text-align:center">7.00</td>
         <td style="text-align:center">7.000</td>
         <td style="text-align:center" rowspan="5">套餐内单价乘以套餐包时长 X</td>   
         <td style="text-align:center">100%</td>    
     </tr> 
     <tr>
         <td style="text-align:center">25 ≤ X ＜ 250</td>   
         <td style="text-align:center">7.00</td>
         <td style="text-align:center">6.720</td>
         <td style="text-align:center">96%</td>    
     </tr> 
     <tr>
         <td style="text-align:center">250 ≤ X ＜ 1000</td>   
         <td style="text-align:center">7.00</td>
         <td style="text-align:center">6.352</td>
         <td style="text-align:center">91%</td>   
     </tr> 
     <tr>
         <td style="text-align:center">1000 ≤ X ＜ 3000</td>
         <td style="text-align:center">7.00</td>
         <td style="text-align:center">5.968</td>
         <td style="text-align:center">85%</td>   
     </tr> 
     <tr> 
         <td style="text-align:center">X ≥ 3000</td>   
         <td style="text-align:center">7.00</td>
         <td style="text-align:center">5.630</td>
         <td style="text-align:center">80%</td>   
     </tr> 
</table>


>?表格中套餐内单价按每千分钟单价向上取整精确到小数点后3位，实际计费按每分钟单价精确到小数点后8位。

通用套餐包说明：

- 通用套餐包的有效期为购买当日 - 次年当月最后一天。
  例如，2020年05月01日购买的套餐包，其有效时间为2020年05月01日 - 2021年05月31日。
- 通用套餐包可以叠加购买，根据各类型用量实际产生的时间实时从通用套餐包中扣除相应分钟数，优先使用先过期的套餐包进行抵扣。
- 新购套餐包支付成功后5分钟左右生效，**新购套餐包生效后会立即扣除购买新套餐包当日0点起产生的未被其他套餐包抵扣过的用量**。
- 为了不影响您线上业务的正常运行，**通用套餐包用完或过期后不会自动停服**，超出套餐包的用量将采用 [后付费](#post-payment) 的计费方式。
- 所有通用套餐包到期后未消耗的分钟数将自动清零且无法恢复。

[](id:post-payment)
#### 后付费
当服务用量无套餐包可抵扣或超出套餐包余量时，将采用后付费的方式，按 [刊例价](#Fixed_price) 计费。
RTC 连麦互动直播服务后付费有 [日结](#daily) 和 [月结](#monthly) 两种结算周期。

- **日结后付费：**[](id:daily)
  2020年09月01日起首次在 实时音视频 控制台创建 [应用](https://cloud.tencent.com/document/product/647/46351#.E5.BA.94.E7.94.A8 ) 的用户，后付费生效后默认采用**日结**方式结算。按日计费，每天上午10点扣除前一天产生的费用。
- **月结后付费：**[](id:monthly)
  2020年08月31日及之前首次在实时音视频控制台创建 [应用](https://cloud.tencent.com/document/product/647/46351#.E5.BA.94.E7.94.A8 ) 的用户，后付费生效后默认采用**月结**方式结算。按月计费，每月01日 - 05日从您的账户余额中扣除前一月产生的费用，详情以 [计费账单](https://cloud.tencent.com/document/product/555/14192#.E4.BA.8C.E3.80.81.E6.96.B0.E7.89.88.E8.B4.A6.E5.8D.95.E5.8A.9F.E8.83.BD.E7.AE.80.E4.BB.8B) 为准。

>!
- 后付费只能通过先购买套餐包，待购买的所有套餐包都消耗完或过期后自动开通，无法直接开通。
- 结算周期无法自主变更，若您希望将月结变更为日结，可以 [提交工单](https://console.cloud.tencent.com/workorder/category) 寻求帮助。
- 若您的账户因余额不足而无法抵扣账单费用时，您使用的其他腾讯云服务也可能会因为账户欠费而自动停服。例如，云端录制依赖**云直播**和**云点播**，如果腾讯云账户欠费，将导致云端录制失败。

[](id:Billing_examples)
### 计费示例
>!本文计费示例采用刊例价计算，您可以通过 [购买套餐包](https://buy.cloud.tencent.com/trtc) 的方式节省费用。

#### 纯语音连麦示例
假设用户 A、B、C 三人使用RTC连麦互动直播服务连麦30分钟。A、B、C 三人始终没有接收视频画面。
则产生的语音时长**总费用**为 `语音时长单价 × 所有用户语音时长之和 = 7.00元/千分钟 × (30分钟 + 30分钟 + 30分钟) / 1000 = 0.63元`。

#### 纯视频连麦示例
假设用户 A、B 使用 RTC 连麦互动直播服务连麦45分钟。A、B 都始终观看对方的视频流。A 、B 实际观看到的视频分辨率如下表所示：

<table>
     <tr>
         <th style="text-align:center">时间</th>  
         <th style="text-align:center"> A 接收 B 的分辨率</th> 
         <th style="text-align:center"> B 接收 A 的分辨率</th> 
     </tr>
     <tr>
         <td style="text-align:center" rowspan="1">前30分钟</td>   
         <td style="text-align:center">1280 × 720（高清）</td>
         <td style="text-align:center">1920 × 1080（超清）</td>   
     </tr> 
     <tr>
         <td style="text-align:center" rowspan="1">后15分钟</td>   
         <td style="text-align:center">640 × 360（标清）</td> 
         <td style="text-align:center">640 × 360（标清）</td>
     </tr> 
</table>

**分析：**
- A 产生的用量及费用：
  - A 观看 B 的分辨率前30分钟位于高清档，后15分钟位于标清档。
  - A 产生的费用为 ` 高清视频时长单价 × 高清视频时长 + 标清视频时长单价 × 标清视频时长 = 28元/千分钟 × (30分钟 / 1000) + 14元/千分钟 × (15分钟 / 1000）= 1.05元`。
- B 产生的用量及费用：
  - B 观看 A 的分辨率前30分钟位于超清档，后15分钟位于标清档。
  - B 产生的费用为 `超清视频时长单价 × 超清视频时长 + 标清视频时长单价 × 标清视频时长 = 105元/千分钟 × (30分钟 / 1000) + 14元/千分钟 × (15分钟 / 1000）= 3.36元`。

则产生的**总费用**为 `用户 A 产生的费用 + 用户 B 产生的费用 = 4.41元 `。

#### 语音时长和视频时长混合示例
假设用户 A、B 使用RTC连麦互动直播服务连麦45分钟。A 始终观看 B 的视频流；B 前30分钟观看了 A 的视频流，后15分钟没有观看 A 的视频流 仅收听 A 的音频流。A 、B 实际接收到的视频分辨率如下表所示：

<table>
     <tr>
         <th style="text-align:center">时间</th>  
         <th style="text-align:center">A 接收 B 的分辨率</th> 
         <th style="text-align:center">B 接收 A 的分辨率</th> 
     </tr>
     <tr>
         <td style="text-align:center" rowspan="1">前30分钟</td>   
         <td style="text-align:center">1280 × 720（高清）</td>
         <td style="text-align:center">1920 × 1080（超清）</td>   
     </tr> 
     <tr>
         <td style="text-align:center" rowspan="1">后15分钟</td>   
         <td style="text-align:center">640 × 360（标清）</td> 
         <td style="text-align:center">语音（无视频）</td>
     </tr> 
</table>

**分析：**
- A 产生的用量及费用：
  - A 接收 B 的分辨率前30分钟位于高清档，后15分钟位于标清档。
  - A 产生的费用为 ` 高清视频时长单价 × 高清视频时长 + 标清视频时长单价 × 标清视频时长 = 28元/千分钟 × (30分钟 / 1000） + 14元/千分钟 × (15分钟 / 1000)= 1.05元`。
- B 产生的用量及费用：
  - B 接收 A 的分辨率前30分钟位于超清档，后15分钟没有接收 A 的视频流。
  - B 产生的费用为 `超清视频时长单价 × 超清视频时长 + 语音时长单价 × 语音时长 = 105元/千分钟 × (30分钟 / 1000) + 7元/千分钟 × (15分钟 / 1000）= 3.255元`。

则产生的**总费用**为 `用户 A 产生的费用 + 用户 B 产生的费用 = 4.305元 `。

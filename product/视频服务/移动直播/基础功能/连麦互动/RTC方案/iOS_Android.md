## 基于 RTC 协议的连麦方案
目前，在 [**连麦互动 - RTMP方案**](https://cloud.tencent.com/document/product/454/14606) 中，腾讯云移动直播 SDK 提供连麦互动组件 `MLVBLiveRoom` 用来帮助开发者快速实现连麦需求，为了更好的满足开发者针对连麦功能的需求，腾讯云新增了基于 RTC 协议的连麦方案，同时提供了更加简单灵活的 V2 接口。

移动直播 V2 接口同时支持通过 RTMP 协议及 RTC 协议进行推流/连麦，开发者可根据自身需求选择适合的方案，对比如下：

| 对比项   | RTMP 方案                  | RTC 方案                                           |
| -------- | -------------------------- | -------------------------------------------------- |
| 协议     | RTMP 基于 TCP 协议            | RTC 基于 UDP 协议（更适合流媒体传输）                 |
| QoS      | 弱网抗性能力弱             | 50%丢包率可正常视频观看，70%丢包率可正常语音连麦 |
| 支持区域 | 仅支持中国内地（大陆）地区 | 全球覆盖                                           |
| 使用产品 | 需开通移动直播、云直播服务 | 需开通移动直播、云直播、实时音视频服务             |
| 价格     | 0.016元/分钟               | 阶梯价格，详情请参见 [RTC 连麦方案怎么计算费用](#price)  |


## RTC 连麦方案如何接入
移动直播 SDK 提供了新的 V2 接口：` V2TXLivePusher` （推流）、` V2TXLivePlayer` （拉流），用来帮助客户实现更加灵活、更低延时、更多人数的直播互动场景。开播端可以利用 V2 提供的 RTC 推流能力，默认情况下，观众端观看则可使用 CDN 方式进行拉流。 CDN 观看费用较低。如果观众端有连麦需求，连麦观众上麦后，可以从 CDN 切换到 RTC 进行观看，这样延时更低，互动效果更好。以下是相关示例代码和具体的步骤说明，方便您快速接入：

### 示例工程

| 平台    | 源码地址                                                     |  目标文件夹  |
| -------| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Android | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/Android/MLVB-API-Example) | [LiveLink](https://github.com/tencentyun/MLVBSDK/tree/master/Android/MLVB-API-Example/Basic/LiveLink) |
| iOS      | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/MLVB-API-Example)|[LiveLink](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/MLVB-API-Example/Basic/LiveLink) |

### 演示图示

####  直播前
<table>
        <tr> 
                <th><div align=center>主播端（手机 A)</div></th>
                <th><div align=center>连麦观众（手机 B）</div></th>
                <th><div align=center>普通观众（手机 C）</div></th>
        </tr>
        <tr>
                <td>
                  <div align=center>
                    <img src="https://main.qcloudimg.com/raw/f46b67807534a6f95905a9334189e2a3.jpeg" style="width: 250px;height: 510px">
                    </div>
                  </td>
                <td>
                  <div align=center>
                    <img src="https://main.qcloudimg.com/raw/502949e9fe3133c10e5f985122bcada3.jpeg" style="width: 250px;height: 510px">
                    </div>
                </td>
                <td>
                  <div align=center>
                    <img src="https://main.qcloudimg.com/raw/53c6cd620e83c4a82ca9cdb25aae81e8.jpg" style="width: 250px;height: 510px">
                    </div>
                </td>
        </tr>
</table>

####  连麦中
<table>
        <tr> 
                <th><div align=center>主播端（手机 A）</div></th>
                <th><div align=center>连麦观众（手机 B）</div></th>
                <th><div align=center>普通观众（手机 C）</div></th>
        </tr>
        <tr>
                <td>
                  <div align=center>
                    <img src="https://main.qcloudimg.com/raw/bc7e2b8bb14e1da6d1fbf6acbaf768e1.png" style="width: 250px;height: 510px">
                    </div>
                  </td>
                <td>
                  <div align=center>
                     <img src="https://main.qcloudimg.com/raw/86ff2214e670457a14c1eaa0b4246e6b.png" style="width: 250px;height: 510px">
                    </div>
                </td>
                <td>
                  <div align=center>
                    <img src="https://main.qcloudimg.com/raw/4be01085e5b39229288428ca735bd53d.png" style="width: 250px;height: 510px"> 
                    </div>
                </td>
        </tr>
</table>

[](id:step1)
### 步骤1：服务开通 
RTC 连麦互动直播需要在开始接入前，先开通腾讯云 [**实时音视频**](https://cloud.tencent.com/document/product/647) 服务，具体步骤如下：

1. 您需要 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. 登录实时音视频控制台，选择 **[应用管理](https://console.cloud.tencent.com/trtc/app)**。
3.  单击 **创建应用**，输入应用名称，例如 `V2Demo`，单击 **确定**。
![](https://main.qcloudimg.com/raw/3d1853c6540a47f1b02de37dccf01f74.png)
4. 创建成功后，单击右侧 **应用信息**，查看应用对应的 `SDKAppID` 信息。
5. 单击 **快速上手**，加载完成后，记录出现的 **UserSig 的密钥**。
> !
> - 本文提到的生成 UserSig 的方案是在客户端代码中配置 UserSig，该UserSig 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此 **该方法仅适合本地跑通 Demo 和功能调试**。
> - 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。
6. 在播放端，推荐使用CDN播放，所以需要在 [实时音视频控制台](https://console.cloud.tencent.com/trtc/app) 开启**旁路推流**功能。
<img src="https://main.qcloudimg.com/raw/f5f2ae04edfb169ec78d2bca1fb10321.png" width="500">

> ?在服务开通后，建议先可以编译和体验一下上述示例代码章节中腾讯云提供的移动直播的 API-Example 工程，配合上下文可以快速的了解相关 API 的使用。

[](id:step2)
### 步骤2：V2TXLivePusher RTC 推流
#### URL 拼接
具体的推流 URL字符串，需要开发者按照下方协议解析中的规则，在工程代码中自行拼接。URL 的示例如下：

**推流 URL**
```http
trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=A&usersig=xxxxx
```

在上述的 URL 中，存在一些关键字段，关于其中关键字段的含义信息，详见下表：

| 字段名称              | 字段含义                                                     |
| --------------------- | ------------------------------------------------------------ |
| **trtc://**           | 互动直播推流 URL 的前缀字段                                  |
| **cloud.tencent.com** | 互动直播特定域名，**请勿修改**                               |
| **push**              | 标识位，表示推流                                             |
| **streamid**       | 流 ID，需要由开发者自定义                                            |
| **sdkappid**      | 对应 [服务开通](#step1) 一节中生成的 SDKAppID |
| **userId**           | 主播 ID，需要由开发者自定义                                  |
| **usersig**         | 对应 [服务开通](#step1) 中获取的 UserSig 密钥 |


#### 示例代码

```java
// 创建⼀个 V2TXLivePusher 对象，并指定模式为 TXLiveMode_RTC；
V2TXLivePusher pusher = new V2TXLivePusherImpl(this, V2TXLiveDef.V2TXLiveMode.TXLiveMode_RTC);
pusher.setObserver(new MyPusherObserver());
pusher.setRenderView(mSurfaceView);
pusher.startCamera(true);
pusher.startMicrophone();
// 传⼊互动直播RTC推流协议地址，即可开始推流，其中streamid设置为自定义值，比如12345687；；
pusher.startPush("trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=finnguan&usersig=xxxxx");
```


### 步骤3：V2TXLivePlayer CDN 播放

#### URL 拼接
具体的播放 URL 字符串，需要开发者按照 `域名 + streamID`，在工程代码中自行拼接。

#### 示例代码
```java
// 创建⼀个 V2TXLivePlayer 对象；
V2TXLivePlayer player = new V2TXLivePlayerImpl(mContext);
player.setObserver(new MyPlayerObserver(playerView));
player.setRenderView(mSurfaceView);
// 传⼊互动直播播放协议地址，即可开始播放，streamid对应推流时设置的streamid，比如12345687；
player.startPlay("https://3891.liveplay.myqcloud.com/live/streamid.flv");
```


### 步骤4：实现观众连麦
![](https://min-cos-1300507594.cos.ap-beijing.myqcloud.com/blog/min.helloworld/24e495dd1a910f53069237ecdf28491e.jpg)
#### 1. 主播 RTC 推流

主播 A 开始推流，调用 `V2TXLivePusher`组件开始主播 A 的推流。

```java
V2TXLivePusher pusherA = new V2TXLivePusherImpl(this, V2TXLiveMode.TXLiveMode_RTC);
...
/**
 * pushURLA= "trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=A&usersig=xxx";
 */
pusherA.startPush(pushURLA);
```

#### 2. 观众 CDN 拉流

所有观众观看主播 A 直播，调用 `V2TXLivePlayer` 开始播放主播 A 的流。

```java
V2TXLivePlayer playerA = new V2TXLivePlayerImpl(mContext);
...
/**
 * 这里使用CDN拉流，支持flv，hls，webrtc协议，任选一种协议。flv，hls等标准协议价格更合理，webrtc快直播能够提供更低延迟的互动体验。
 * playURLA= "http://3891.liveplay.myqcloud.com/live/streamidA.flv";
 * playURLA= "http://3891.liveplay.myqcloud.com/live/streamidA.hls";
 * playURLA= "webrtc://3891.liveplay.myqcloud.com/live/streamidA"
 */
playerA.startPlay(playURLA);
```


#### 3. 观众发起连麦

其中观众 B 调用 `V2TXLivePusher` 发起推流（后续会称呼为连麦观众B）。

```java
V2TXLivePusher pusherB = new V2TXLivePusherImpl(this,V2TXLiveMode.TXLiveMode_RTC);
...
/*
 * pushURLB= "trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=B&usersig=xxx";
 */
pusherB.startPush(pushURLB);
```

#### 4. 进入连麦状态

主播 A 调用 `V2TXLivePlayer` 使用RTC协议拉取放**连麦观众 B** 的流。

```java
V2TXLivePlayer playerB = new V2TXLivePlayerImpl(mContext);
...
/**
 * playURLB= "trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&userId=B&usersig=xxx";
 */
playerB.startPlay(playURLB);
```
同时，**连麦观众 B** 调用 `V2TXLivePlayer` 切换至 RTC 协议，开始播放主播 A 的流。

```java
V2TXLivePlayer playerA = new V2TXLivePlayerImpl(mContext);
...
/**
 *playURLA= "trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&userId=A&usersig=xxx";
 */
playerA.startPlay(playURLA);
```
此时主播 A 和**连麦观众 B** 即可进入超低延时的实时互动场景中。


#### 5. 连麦成功后，进行混流

为了保证观众可以看到连麦观众B的画面，这里主播 A 需要发起一次混流操作。也就是将主播A自己和连麦观众 B，混合成一路流。观众可以在一路流上看到主播和连麦观众进行互动。 A 调用 setMixTranscodingConfig 接口启动云端混流，调用时需要设置音频相关的参数，例如 `音频采样率 audioSampleRate`、`音频码率 audioBitrate` 和 `声道数 audioChannels` 等。
如果您的业务场景中也包含视频，需同时设置视频相关的参数，例如 `视频宽度 videoWidth`、`视频高度 videoHeight`、`视频码率 videoBitrate`、`视频帧率 videoFramerate` 等。

**示例代码**：
```java
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
```

> ! 发起云端混流后，默认混流 ID，是发起混流者的 ID，如果需要指定流 ID，需要进行传入。

这样其他观众在观看时，就可以看到 A，B 两个主播的连麦互动。

### 步骤5：实现主播 PK
1. 主播 A 开始推流，调用 `V2TXLivePusher` 组件开始主播 A 的推流。
<dx-codeblock>
::: java java
V2TXLivePusher pusherA = new V2TXLivePusherImpl(this, V2TXLiveMode.TXLiveMode_RTC);
...
/**
 * pushURLA= "trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=A&usersig=xxx";
 */
pusherA.startPush(pushURLA);
:::
</dx-codeblock>
2. 主播 B 开始推流，调用 `V2TXLivePusher`组件开始主播 B 的推流。
<dx-codeblock>
::: java java
V2TXLivePusher pusherB = new V2TXLivePusherImpl(this, V2TXLiveMode.TXLiveMode_RTC);
...
/**
 * pushURLB "trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=B&usersig=xxx";
 */
pusherB.startPush(pushURLB);
:::
</dx-codeblock>
3. **开始 PK**，主播 A 和主播 B 分别调用 `V2TXLivePlayer` 开始播放对方的流，此时主播 A 和主播 B 即进入 RTC 连麦互动直播场景中。
<dx-codeblock>
::: java java
V2TXLivePlayer playerA = new V2TXLivePlayerImpl(mContext);
...
/**
 * 这里使用CDN拉流，支持flv，hls，webrtc协议，任选一种协议。flv，hls等标准协议价格更合理，webrtc快直播能够提供更低延迟的互动体验。
 * playURLA= "http://3891.liveplay.myqcloud.com/live/streamidB.flv";
 * playURLA= "http://3891.liveplay.myqcloud.com/live/streamidB.hls";
 * playURLA= "webrtc://3891.liveplay.myqcloud.com/live/streamidB"
 */
playerA.startPlay(playURLA);

V2TXLivePlayer playerB = new V2TXLivePlayerImpl(mContext);
...
/**
 * 这里使用CDN拉流，支持flv，hls，webrtc协议，任选一种协议。flv，hls等标准协议价格更合理，webrtc快直播能够提供更低延迟的互动体验。
 * playURLB= "http://3891.liveplay.myqcloud.com/live/streamidA.flv";
 * playURLB= "http://3891.liveplay.myqcloud.com/live/streamidA.hls";
 * playURLB= "webrtc://3891.liveplay.myqcloud.com/live/streamidA"
 */
playerB.startPlay(playURLB);
:::
</dx-codeblock>
4. **PK 成功后**，主播 A 和主播 B 的观众各自调用 `V2TXLivePlayer` 开始播放另外一名主播的推流内容。

> ? 此处开发者可能会有疑问：貌似新的 RTC 连麦方案还需要我们自己维护一套房间和用户状态，这样不是更麻烦吗？是的，**没有更好的方案，只有更适合自己的方案**，我们也有考虑到这样的场景：
> - 如果对时延和并发要求并不高的场景，可以继续使用连麦互动的旧方案。
> - 如果既想用到 V2 相关的接口，但是又不想维护一套单独的房间状态，可以尝试搭配 [腾讯云 IM SDK](https://cloud.tencent.com/document/product/269)，快速实现相关逻辑。


[](id:price)
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
视频互动直播服务的刊例价如下表所示：

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
RTC连麦互动直播服务为您提供音视频通用套餐包，可按照**1:2:4:15**分别抵扣语音、标清 SD、高清 HD 和超清 HD+ 时长，例如1分钟高清视频时长扣除4分钟通用套餐包时长。
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

假设用户 A、B 使用RTC连麦互动直播服务连麦45分钟。A、B 都始终观看对方的视频流。A 、B 实际观看到的视频分辨率如下表所示：

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


## 常见问题

#### 1. 为什么使用 `V2TXLivePusher&V2TXLivePlayer` 接口时，同一台设备不支持使用相同 streamid 同时推流和拉流，而 `TXLivePusher&TXLivePlayer` 可以支持？
是的，目前 `V2TXLivePusher&V2TXLivePlayer` 是 [腾讯云 TRTC](https://cloud.tencent.com/document/product/647/45151) 协议实现，其基于 UDP 的超低延时的私有协议暂时还不支持**同一台设备，使用相同的 streamid，一边推超低延时流，一边拉超低延时的流**，同时考虑到用户的使用场景，所以暂时并未支持，后续会酌情考虑此问题的优化。

#### 2. [**服务开通**](#step1) 章节中生成参数都是什么意思呢？
SDKAppID 用于标识您的应用，UserID 用于标识您的用户，而 UserSig 则是基于前两者计算出的安全签名，它由 **HMAC SHA256** 加密算法计算得出。只要攻击者不能伪造 UserSig，就无法盗用您的云服务流量。UserSig 的计算原理如下图所示，其本质就是对 SDKAppID、UserID、ExpireTime 等关键信息进行了一次哈希加密：
```Cpp
//UserSig 计算公式，其中 secretkey 为计算 usersig 用的加密密钥

usersig = hmacsha256(secretkey, (userid + sdkappid + currtime + expire + 
                                 base64(userid + sdkappid + currtime + expire)))
```

#### 3. V2TXLivePusher&V2TXLivePlayer 如何设置音质或者画质呢？
我们有提供对应的音质和画质的设置接口，详情见 API 文件：[设置推流音频质量](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a88956a3ad5e030af7b2f7f46899e5f13) 和 [设置推流视频参数](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLivePusher__ios.html#a0b08436c1e14a8d7d9875fae59ac6d84)。

#### 4. 收到一个错误码：`-5`，代表什么意思？
-5表示由于许可证无效，因此无法调用API，对应的枚举值为：[V2TXLIVE_ERROR_INVALID_LICENSE](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLiveCode__ios.html)，更多错误码请参见 [API 状态码](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__V2TXLiveCode__ios.html)。

#### 5. RTC连麦方案的时延性有可以参考的数据吗？
新的 RTC 连麦方案中，主播连麦的延时 < 200ms，主播和观众的延时在 100ms - 1000ms。

#### 6. RTC 推流成功后，使用 CDN 拉流一直提示404？
检查一下是否有开启实时音视频服务的旁路直播功能，基本原理是 RTC 协议推流后，如果需要使用 CDN 播放，RTC 会在后台服务中旁路流信息到 CDN 上。

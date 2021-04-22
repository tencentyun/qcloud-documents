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


## 开始体验 RTC 连麦方案
视频云工具包是腾讯云开源的一套完整的音视频服务解决方案，包含实时音视频（TRTC）、移动直播（MLVB）、短视频（UGC）等多个 SDK 的能力展示，其中包含RTC连麦方案相关体验 UI — **连麦演示( 新方案 )** 。

### 体验地址
| 平台    | Demo 体验                                                    | 源码地址                                                     | 目标文件夹                                                   |
| ------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Android | <img width="150" src="https://main.qcloudimg.com/raw/bff0cfca4585c448f308b339a6c17c1c.png"> | [Github](https://github.com/tencentyun/LiteAVProfessional_Android) | [Demo/livelinkmicdemonew](https://github.com/tencentyun/LiteAVProfessional_Android/tree/master/Demo/livelinkmicdemonew) |
| iOS     | <img width="150" src="https://main.qcloudimg.com/raw/83973196cc1fc9972320182eb283d406.png"> | [Github](https://github.com/tencentyun/LiteAVProfessional_iOS) | [Demo/TXLiteAVDemo/LiveLinkMicDemoNew](https://github.com/tencentyun/LiteAVProfessional_iOS/tree/master/Demo/TXLiteAVDemo/LiveLinkMicDemoNew) |



### 体验说明
<table>
        <tr> 
                <th><div align=center>主播 A</div></th>
                <th><div align=center>主播 B</div></th>
                <th><div align=center>观众</div></th>
        </tr>
        <tr>
                <td>
									<div align=center>
										<img src="https://liteav.sdk.qcloud.com/doc/res/mlvb/picture/anchor.gif">
										</div>
									</td>
                <td>
									<div align=center>
										<img src="https://liteav.sdk.qcloud.com/doc/res/mlvb/picture/link_audience.gif">
										</div>
								</td>
								<td>
									<div align=center>
										<img src="https://liteav.sdk.qcloud.com/doc/res/mlvb/picture/others_audience.gif">
										</div>
								</td>
        </tr>
</table>

### 步骤图示
![](https://liteav.sdk.qcloud.com/doc/res/mlvb/picture/v2_demo_use_step.png)
> =体验 Demo 功能时需要注意，由于超低延时直播的协议特性，目前RTC连麦方案并不支持：**同一台设备，使用相同的 streamid，一边推超低延时流，一边拉超低延时的流**。

## RTC 连麦方案如何接入

新版本的移动直播 SDK 提供了新的 V2 接⼝：` V2TXLivePusher ` (推流)、 `V2TXLivePlayer`  (拉流)，用来帮助客户实现**更加灵活、更低延时、更多人数**的直播互动场景，接下来将介绍基于 ` V2TXLivePusher ` 和 `V2TXLivePlayer` 组件如何快速实现观众连麦和主播 PK 等互动场景服务。

[](id:RegistrationService)
### 步骤1：服务开通 
超低延时直播需要在开始接入前，先开通腾讯云 [**实时音视频**](https://cloud.tencent.com/document/product/647) 服务，具体步骤如下：

1. 您需要 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. 登录实时音视频控制台，选择【[应用管理](https://console.cloud.tencent.com/trtc/app)】。
3.  单击【创建应用】，输入应用名称，例如 `V2Demo` ，单击【确定】。
![](https://min-cos-1300507594.cos.ap-beijing.myqcloud.com/blog/min.helloworld/21ef2f952c428c08cedfbef88ba16407.png)
4. 创建成功后，单击右侧【应用信息】，查看应用对应的 `SDKAppID` 信息。
5. 单击【快速上手】，加载完成后，记录出现的 **UserSig 的密钥**。

> !
> - 本文提到的生成 UserSig 的方案是在客户端代码中配置 UserSig，该UserSig 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此 **该方法仅适合本地跑通 Demo 和功能调试** 。
> - 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

> ?在服务开通后，建议先可以编译&体验一下腾讯云提供的 SimpleCode（一个极简的Demo），配合下文说明，方便您快速了解API的使用。
> - [Android](https://github.com/tencentyun/MLVBSDK/tree/master/Android/SimpleDemo)
> - [iOS](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/SimpleDemo)

### 步骤2：了解推拉流协议
在直播场景中，不论是推流还是拉流都离不开对应的 URL，在超低延时直播中，URL 的示例如下：

- **推流URL**
```http
trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=A&usersig=xxxxx
```
- **拉流URL**
```http
trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&userId=A&usersig=xxx
```

在上述的 URL 中，存在一些关键字段，关于其中关键字段的含义信息，详见下表：

| 字段名称              | 字段含义                                                     |
| --------------------- | ------------------------------------------------------------ |
| **trtc://**           | 低延时推流URL的前缀字段                                      |
| **cloud.tencent.com** | 低延时直播特定域名，**请勿修改**                             |
| **push**              | 标识位，表示推流                                             |
| **play**              | 标识位，表示拉流                                             |
| **sdkappid**          | 对应 [**服务开通**](#RegistrationService) 一节中生成的 SDKAppID |
| **userId**            | 主播 ID，需要由开发者自定义                                  |
| **usersig**           | 对应 [**服务开通**](#RegistrationService) 中获取的 UserSig 密钥 |


### 步骤3：了解 V2TXLivePusher 推流

#### URL 拼接
具体的推流 URL字符串，需要开发者按照协议解析中的规则，在工程代码中自行拼接。

#### 示例代码
<dx-codeblock>
::: Java
// 创建⼀个 V2TXLivePusher 对象，并指定模式为 TXLiveMode_RTC；
V2TXLivePusher pusher = new V2TXLivePusherImpl(this, V2TXLiveDef.V2TXLiveMode.TXLiveMode_RTC);
pusher.setObserver(new MyPusherObserver());
pusher.setRenderView(mSurfaceView);
pusher.startCamera(true);
pusher.startMicrophone();
// 传⼊低延时协议推流地址，即可开始推流；
pusher.startPush("trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=finnguan&usersig=xxxxx");
:::
::: Objective-C
// 创建⼀个 V2TXLivePusher 对象，并指定模式为 TXLiveMode_RTC；
V2TXLivePusher *pusher = [[V2TXLivePusher alloc] initWithLiveMode:V2TXLiveMode_RTC];
[pusher setObserver:self];
[pusher setRenderView:videoView];
[pusher startCamera:true];
[pusher startMicrophone];
// 传⼊低延时协议推流地址，即可开始推流；
[pusher startPush:@"trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&userId=finnguan&usersig=xxxxx"];
:::
</dx-codeblock>


### 步骤4：了解 V2TXLivePlayer 播放

#### URL 拼接
具体的播放 URL 字符串，需要开发者按照协议解析中的规则 + 推流的 URL，在工程代码中自行拼接。

#### 示例代码
<dx-codeblock>
::: Java
// 创建⼀个 V2TXLivePlayer 对象；
V2TXLivePlayer player = new V2TXLivePlayerImpl(mContext);
player.setObserver(new MyPlayerObserver(playerView));
player.setRenderView(mSurfaceView);
// 传⼊低延时协议播放地址，即可开始播放；
player.startPlay("trtc://cloud.tencent.com/play/streamid?sdkappid=1400188366&userId=A&usersig=xxx");
:::
::: Objective-C
V2TXLivePlayer *player = [[V2TXLivePlayer alloc] init];
[player setObserver:self];
[player setRenderView:videoView];
[player startPlay:@"trtc://cloud.tencent.com/play/streamid?sdkappid=1400188366&userId=A&usersig=xxx"];
:::
</dx-codeblock>


### 步骤5：实现观众连麦
![](https://min-cos-1300507594.cos.ap-beijing.myqcloud.com/blog/min.helloworld/24e495dd1a910f53069237ecdf28491e.jpg)
1. 主播 A 开始直播，调用 `V2TXLivePusher` 开始主播 A 的推流。
<dx-codeblock>
::: Java
V2TXLivePusher pusherA = new V2TXLivePusherImpl(this, V2TXLiveMode.TXLiveMode_RTC);
...
pusherA.startPush(pushURLA);
:::
::: Objective-C
V2TXLivePusher *pusherA = [[V2TXLivePusher alloc] initWithLiveMode:V2TXLiveMode_RTC];
...
[pusherA startPush:pushURLA];
:::
</dx-codeblock>
2. 所有观众观看主播 A 直播，调用 `V2TXLivePlayer` 开始播放主播 A 的流。
<dx-codeblock>
::: Java
V2TXLivePlayer playerA = new V2TXLivePlayerImpl(mContext);
...
playerA.startPlay(playURLA);
:::
::: Objective-C
V2TXLivePlayer *player = [[V2TXLivePlayer alloc] init];
...
[player startPlay:playURLA];
:::
</dx-codeblock>
3. **开始连麦**，其中观众 B 调用 `V2TXLivePusher` 发起推流（后续会称呼为连麦观众B）。
<dx-codeblock>
::: Java
V2TXLivePusher pusherB = new V2TXLivePusherImpl(this, V2TXLiveMode.TXLiveMode_RTC);
...
pusherB.startPush(pushURLB);
:::
::: Objective-C
V2TXLivePusher *pusherB = [[V2TXLivePusher alloc] initWithLiveMode:V2TXLiveMode_RTC];
...
[pusherB startPush:pushURLB];
:::
</dx-codeblock>
4. **收到连麦消息后**，主播 A 调用 `V2TXLivePlayer` 开始播放**连麦观众B**的流，此时主播 A 和**连麦观众 B** 即可进入超低延时的实时互动场景中。
<dx-codeblock>
::: Java
V2TXLivePlayer playerB = new V2TXLivePlayerImpl(mContext);
...
playerB.startPlay(playURLB);
:::
::: Objective-C
V2TXLivePlayer *playerB = [[V2TXLivePlayer alloc] init];
...
[playerB startPlay:playURLB];
:::
</dx-codeblock>
5. **连麦成功后**，其他观众调用 `V2TXLivePlayer` 同时也开始播放**连麦观众 B** 的流。

### 步骤6：实现主播 PK
1. 主播 A 开始直播，调用 `V2TXLivePusher` 开始主播 A 的推流。
<dx-codeblock>
::: Java
V2TXLivePusher pusherA = new V2TXLivePusherImpl(this, V2TXLiveMode.TXLiveMode_RTC);
...
pusherA.startPush(pushURLA);
:::
::: Objective-C
V2TXLivePusher *pusherA = [[V2TXLivePusher alloc] initWithLiveMode:V2TXLiveMode_RTC];
...
[pusherA startPush:pushURLA];
:::
</dx-codeblock>
2. 主播 B 开始直播，调用 `V2TXLivePusher` 开始主播 B 的推流。
<dx-codeblock>
::: Java
V2TXLivePusher pusherB = new V2TXLivePusherImpl(this, V2TXLiveMode.TXLiveMode_RTC);
...
pusherB.startPush(pushURLB);
:::
::: Objective-C
V2TXLivePusher *pusherB = [[V2TXLivePusher alloc] initWithLiveMode:V2TXLiveMode_RTC];
...
[pusherB startPush:pushURLB];
:::
</dx-codeblock>
3. **开始 PK**，主播 A 和主播 B 分别调用 `V2TXLivePlayer` 开始播放对方的流，此时主播 A 和主播 B 即进入超低延时的实时互动场景中。
<dx-codeblock>
::: Java
V2TXLivePlayer playerA = new V2TXLivePlayerImpl(mContext);
...
playerA.startPlay(playURLA);

V2TXLivePlayer playerB = new V2TXLivePlayerImpl(mContext);
...
playerB.startPlay(playURLB);
:::
::: Objective-C
V2TXLivePlayer *playerA = [[V2TXLivePlayer alloc] init];
...
[playerA startPlay:playURLA];

V2TXLivePlayer *playerB = [[V2TXLivePlayer alloc] init];
...
[playerB startPlay:playURLB];
:::
</dx-codeblock>

4. **PK 成功后**，主播 A 和主播 B 的观众各自调用 `V2TXLivePlayer` 开始播放另外一名主播的推流内容。

> ?此处开发者可能会有疑问：貌似新的RTC连麦方案还需要我们自己维护一套房间&用户状态，这样不是更麻烦吗？是的，**没有更好的方案，只有更适合自己的方案**，我们也有考虑到这样的场景：
> - 如果对时延和并发要求并不高的场景，可以继续使用连麦互动的旧方案。
> - 如果既想用到 V2 相关的接口，但是又不想维护一套单独的房间状态，可以尝试搭配 [腾讯云 IM SDK](https://cloud.tencent.com/document/product/269)，快速实现相关逻辑。

[](id:price)
## RTC 连麦方案怎么计算费用

RTC 连麦方案采用腾讯云实时音视频 TRTC 来实现，由 TRTC **按麦上用户产生的时长** 向您收取相关费用。时长类型及刊例价如下表所示：

| 计费时长类型 | 拉流分辨率                   | 单价（元/千分钟） |
| ------------ | ---------------------------- | ----------------- |
| 纯语音       | -                            | 7.00              |
| 标清 SD      | 不高于640 × 480（含）        | 14.00             |
| 高清 HD      | 640 × 480 - 1280 × 720（含） | 28.00             |
| 超清 HD+     | 高于1280 × 720               | 105.00            |

>?
- 麦上用户指的是主播和上麦的观众，计费时长按拉流时间统计，时长类型取决于拉流分辨率。
- 同一个用户拉取同一路音视频流的语音费用已包含在视频费用中，不会重复计算语音费用。
- 当麦上用户仅推流、不拉流时，由于统计不到拉流时长和拉流分辨率，则计费时长按推流时间统计，时长类型按语音统计。

首次在 TRTC 控制台 [创建应用](https://cloud.tencent.com/document/product/647/50493) 的腾讯云账户，可自动获得10000分钟 [免费试用](https://cloud.tencent.com/document/product/647/44360) 时长。试用时长用完或过期后将自动停服，后续可通过 [官网](https://cloud.tencent.com/product/trtc) 购买套餐包来重新激活服务。

## 常见问题

#### 1. 为什么使用 `V2TXLivePusher&V2TXLivePlayer` 接口时，同一台设备不支持使用相同 streamid 同时推流和拉流，而 `TXLivePusher&TXLivePlayer` 可以支持？
是的，目前 `V2TXLivePusher&V2TXLivePlayer` 是 [腾讯云 TRTC](https://cloud.tencent.com/document/product/647/45151) 协议实现，其基于 UDP 的超低延时的私有协议暂时还不支持同一台设备使用相同的 streamid 进行通信，同时考虑到用户的使用场景，所以暂时并未支持，后续会酌情考虑此问题的优化。

#### 2. [**服务开通**](#RegistrationService) 章节中生成参数都是什么意思呢？
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

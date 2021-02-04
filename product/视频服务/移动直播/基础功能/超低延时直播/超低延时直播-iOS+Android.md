## 什么是超低延时直播？
超低延时直播，是腾讯云基于目前市场需求推出的新的直播场景解决方案，可以快速实现超低延时的互动直播功能，支持30w观众的并发播放，以及30人的实时连麦互动，适用于主播和观众有着较强的同步需求，需要频繁互动的场景。

<img src="https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/mlvb/ultra-low_latency_live/rtc_compare_cdn.gif">

> ?上图为超低延时直播和标准的CDN直播的真实对比视频（使用[scrcpy工具](https://github.com/Genymobile/scrcpy)配合录制），从左至右分别为：源视频、**超低延时直播（延时80ms）**、标准的CDN直播；

 
### 方案优势：
 - **超高并发**：支持最大30w观众的超高并发播放，完美保障诸如体育赛事、博览会等大型社会活动；
 - **超低延时**：主播互动延时小于400ms，观众观看时延小于1s，相比传统直播延时降低80%，助力解锁更多互动直播场景；
 - **超强抗性**：通过智能网络质量调控和编码优化降低卡顿率， 50%丢包率可正常视频观看。60%丢包率可正常语音连麦；
 - **灵活简单**：新的移动直播V2 接口在设计上更加简单，尤其是在连麦等互动场景上，可以非常灵活的接入业务系统；

### 适用场景
 - **教育大班课**：超低延时观看保证老师、学生之间的同步性支撑抢答、互动答题、无缝上麦等场景优化互动教学体验；
 - **赛事直播**：超低延时观看保证所有观众的赛事进展实时同步，不再担心被剧透，共庆欢胜时刻；
 - **秀场直播**：超低延时观看助力主播及时反馈，增强直播间互动性，促进直播间观众打赏；
 - **电商直播**：超低延时观看助力主播助播实时解答观众提问，更能解锁秒杀、连麦等玩法，提高转化和留存。


 
## 体验超低延时直播
视频云工具包是腾讯云开源的一套完整的音视频服务解决方案，包含实时音视频（TRTC）、移动直播（MLVB）、短视频（UGC）等多个SDK的能力展示，其中包含超低延时直播相关体验UI -- **连麦演示( 新方案 )** 。
> ?因为超低延时播直播的特性，即推流/播放，目前将其能力的展示整合在连麦演示（新方案）中，具体说明见下文。

### 体验步骤

<table>
  <tr>
	  <th><div align="center">源码下载</div></th>
    <th><div align="center">体验安装</div></th>
    <th><div align="center">推流演示</div></th>
    <th><div align="center">播放演示</div></th>
  </tr>
  <tr>
	  <td><a href='https://github.com/tencentyun/LiteAVProfessional_Android'> Android </a></td>
    <td><img width="150" src="https://main.qcloudimg.com/raw/492e319bbd98ff3cfd9a5959f1a6622b.png"> </td>
    <td rowspan="2">
      <div align="center">
        <img src="https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/mlvb/ultra-low_latency_live/push.gif"/>
      </div>
    </td>
    <td rowspan="2">
      <div align="center">
        <img src="https://demovideo-1252463788.cos.ap-shanghai.myqcloud.com/mlvb/ultra-low_latency_live/play.gif"/>
      </div>
    </td>
  </tr>
  <tr>
	  <td><a href='https://github.com/tencentyun/LiteAVProfessional_iOS'> iOS </a></td>
    <td><img width="150" src="https://main.qcloudimg.com/raw/4b21d7814a8a2aeb502f9f5ef0049e07.png"></td>
  </tr>
</table>

#### 推流体验
 - No1. 下载视频云工具包，安装登录后，进入连麦演示（新方案）中；
 - No2. 允许相关权限申请，点击Pusher，默认选择为RTC，即超低演示直播模式，随机输入一个`steamId`，比如：`11223344`，然后点击开始推流按钮；
 - No3. 开始推流后，也可点击右下侧的菜单按钮，放大窗口，设置诸如美颜，BGM，切换摄像头等操作； 
 ![](https://main.qcloudimg.com/raw/e2160adc79b02798488fb674de423545.png)

#### 播放体验
 - No1. 下载视频云工具包，安装登录后，进入连麦演示（新方案）中；
 - No2. 允许相关权限申请，点击Player，默认选择为RTC，即超低演示直播模式，输入对应推流时设置`steamId`，比如：`11223344`，然后点击开始播放按钮；
 - No3. 开始播放后，也可点击右下侧的菜单按钮，放大窗口，设置诸如静音等操作；
![](https://main.qcloudimg.com/raw/3490e23ff34ecda11ebd5f0a57d404b7.png)
> =因为超低延时直播的协议特性，目前连麦互动新方案并不支持：**同一台设备，使用相同的streamid，一边推超低延时流，一边拉超低延时的流**，这一点可能在体验Demo功能时需要注意。


## 如何实现超低延时直播？
新版本的移动直播SDK，提供了新的V2 接⼝：`V2TXLivePusher` (推流)、 `V2TXLivePlayer`  (拉流)，用来帮助客户实现**更加灵活、更低延时**的直播业务场景。同时考虑的客户对于标准直播的需求，移动直播 V2 接⼝兼容⽀持两种直播协议：
- 标准直播协议：标准的 RTMP 推流和 FLV 拉流，其URL分别以 `rtmp://` 和`http://`字符开始 ；
- 超低延时直播协议：基于UDP实现的私有协议，其URL均以 `trtc://` 字符开始；
标准直播协议和低延时直播协议，除了 URL 不同，在接入方式上基本⼀致，但是超低延时直播协议具备更低的时延，在直播效果和体验上有着更好的表现，现在开始接入吧～

[](id:step1)
### 步骤1：开通服务
超低延时直播需要在开始接入前，先开通腾讯云[**实时音视频**](https://cloud.tencent.com/document/product/647)服务，具体步骤如下：

- 您需要[注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)；

- 登录实时音视频控制台，选择【[应用管理](https://console.cloud.tencent.com/trtc/app)】；

- 点击【创建应用】，输入应用名称，例如 `V2Demo` ，单击【确定】；
![](https://main.qcloudimg.com/raw/f5f17df813b60d07ec7b9737aa361259.png)

- 创建成功后，点击右侧【应用信息】，查看应用对应的`SDKAppID`信息；

- 单击【快速上手】，加载完成后，记录出现的**UserSig的密钥**。

> !本文提到的生成 UserSig 的方案是在客户端代码中配置 UserSig，该UserSig 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此 **该方法仅适合本地跑通 Demo 和功能调试** 。正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)

> ?在服务开通后，建议先可以编译&体验一下腾讯云提供的SimpleCode（一个极简的Demo），配合下文说明，方便您快速了解API的使用；
> - [Android](https://git.code.oa.com/parkhuang/liteav_app/tree/dev/borry/v2/Android/MLVBSimpleDemo)
> - [iOS](https://git.code.oa.com/parkhuang/liteav_app/tree/dev/borry/v2/iOS/MLVBSimpleDemo)

[](id:step2)
### 步骤2：拼装 URL
在直播场景中，不论是推/拉流都离不开对应的URL，在超低延时直播中，URL的示例如下：

- **低延时推流地址**
```http
trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&amp;userId=A&amp;usersig=xxxxx
```

- **低延时播放地址**
```http
trtc://cloud.tencent.com/play/streamid?sdkappid=1400188888&amp;userId=A&amp;usersig=xxx
```

在上述的URL中，存在一些关键字段，关于其中关键字段的含义信息，详见下表：

| 字段名称 | 字段含义 |
| ------ | ------ |
| **trtc://** | 低延时推流URL的前缀字段 |
| **cloud.tencent.com** | 低延时直播特定域名，**请勿修改** |
| **push** | 标识位，表示推流 |
| **play** | 标识位，表示拉流 |
| **sdkappid** | 对应 [服务开通](#step1) 一节中生成的`SDKAppID` |
| **userId** | 主播ID，需要由开发者自定义 |
| **usersig** | 对应[服务开通](#step1) 中获取的UserSig密钥 |


[](id:step3)
### 步骤3：低延时播放
>! 要实现低延时直播，该直播流地址必须是使用 [**低延时推流**](#step4) 推出来的，否则会出现无法播放的问题。

使用 `V2TXLivePlayer` 对象可以推出可供低延时播放的直播流，具体做法如下（拼装出正确的 URL 是关键）：
#### 示例代码
<dx-codeblock>
::: Java
// 创建⼀个 V2TXLivePlayer 对象；
V2TXLivePlayer player = new V2TXLivePlayerImpl(mContext);
player.setObserver(new MyPlayerObserver(playerView));
player.setRenderView(mSurfaceView);
// 传⼊低延时协议播放地址，即可开始播放；
player.startPlay("trtc://cloud.tencent.com/play/streamid?sdkappid=1400188366&amp;amp;userId=A&amp;usersig=xxx");
:::
::: Objective-C
V2TXLivePlayer *player = [[V2TXLivePlayer alloc] init];
[player setObserver:self];
[player setRenderView:videoView];
[player startPlay:@"trtc://cloud.tencent.com/play/streamid?sdkappid=1400188366&amp;amp;userId=A&amp;usersig=xxx"];
:::
</dx-codeblock>

[](id:step4)
### 步骤4：低延时推流
使用 `V2TXLivePusher` 对象可以推出可供低延时播放的直播流，具体做法如下（拼装出正确的 URL 是关键）：

#### 示例代码
<dx-codeblock>
::: Java
// 创建⼀个 V2TXLivePusher 对象，并指定模式为 TXLiveMode_RTC；
V2TXLivePusher pusher = new V2TXLivePusherImpl(this, V2TXLiveDef.V2TXLiveMode.TXLiveMode_RTC);
pusher.setObserver(new MyPusherObserver());
pusher.setRenderView(mSurfaceView);
pusher.startCamera(TXDeviceManager.CAMERA_TYPE_FRONT);
pusher.startMicrophone();
// 传⼊低延时协议推流地址，即可开始推流；
pusher.startPush("trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&amp;userId=finnguan&amp;usersig=xxxxx");
:::
::: Objective-C
// 创建⼀个 V2TXLivePusher 对象，并指定模式为 TXLiveMode_RTC；
V2TXLivePusher *pusher = [[V2TXLivePusher alloc] initWithLiveMode:V2TXLiveMode_RTC];
[pusher setObserver:self];
[pusher setRenderView:videoView];
[pusher startCamera:TX_CAMERA_TYPE_FRONT];
[pusher startMicrophone];
// 传⼊低延时协议推流地址，即可开始推流；
[pusher startPush:@"trtc://cloud.tencent.com/push/streamid?sdkappid=1400188888&amp;userId=finnguan&amp;usersig=xxxxx"]
:::
</dx-codeblock>

[](id:step5)
### 步骤5：使用低延时播放实现连麦和 PK（可选功能）

在超低延时播放的场景中，一般都伴随着中/高频的连麦需求，包括观众连麦和主播PK，目前新的V2接口可以**非常灵活、简单**的实现类似的互动需求，且最多支持30人同时连麦，功能更强大，稳定性更高，只需如下简单四步：
- **步骤一**：调用V2TXLivePusher开始主播A的推流；
- **步骤二**：所有观众侧调用V2TXLivePlayer开始播放主播A的推流；
- **步骤三**：开始连麦，连麦观众B调用V2TXLivePusher发起推流；
- **步骤四**：收到连麦消息后，主播A和其他观众调用V2TXLivePlayer开始播放观众B的推流；

此时我们的主播A，观众B，其他观众即进入超低延时的实时互动场景中，更详细的步骤调用&amp;代码示例，详见：[连麦互动(新方案)]()；

## 怎么计算费用？
超低延时直播能力由腾讯云实时音视频 TRTC 提供，由 TRTC **按麦下用户产生的时长** 向您收取相关费用。时长类型及刊例价如下表所示：

| 计费时长类型 | 拉流分辨率                   | 单价（元/千分钟） |
| ------------ | ---------------------------- | ----------------- |
| 纯语音       | -                            | 7.00              |
| 标清 SD      | 不高于640 × 480（含）        | 14.00             |
| 高清 HD      | 640 × 480 - 1280 × 720（含） | 28.00             |
| 超清 HD+     | 高于1280 × 720               | 105.00            |

>?
- 麦下用户指的是不上麦的观众，计费时长按拉流时间统计，时长类型取决于拉流分辨率。
- 同一个用户拉取同一路音视频流的语音费用已包含在视频费用中，不会重复计算语音费用。

首次在 TRTC 控制台 [创建应用](https://cloud.tencent.com/document/product/647/50493) 的腾讯云账户，可自动获得10000分钟 [免费试用](https://cloud.tencent.com/document/product/647/44360) 时长。试用时长用完或过期后将自动停服，后续可通过 [官网](https://cloud.tencent.com/product/trtc) 购买套餐包来重新激活服务。

注：TRTC 正在内测 **按麦下用户产生的带宽** 计费，如果您希望调整计费方式，可邮件联系 TRTC 产品经理 shixinwang@tencent.com申请。


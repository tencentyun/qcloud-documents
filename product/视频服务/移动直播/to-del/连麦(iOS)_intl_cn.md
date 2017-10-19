本文档主要介绍腾讯云连麦功能的对接方案，如果您想要了解连麦的原理，欢迎阅读 [如何实现连麦功能？](https://cloud.tencent.com/document/product/454/8092)

## 更新版本
RTMP SDK 1.8.2 开始才支持连麦功能，请到 [下载页](https://cloud.tencent.com/document/product/454/7873) 更新最新版本的 RTMP SDK。同时，我们的 小直播 [DEMO](https://cloud.tencent.com/document/product/454/6991) 也已经集成了这套解决方案的示例代码。

## 名词解释
- **session_id ？**
>session_id 是一个**数字**（如1234，不能是英文字符），在连麦用的推流 URL 和播放 URL 中都会用到，代表连麦房间号。
>
>如果我们做的足够好，是可以把主播的推流**直播码**直接用作连麦房间号的，毕竟直播码就是直播房间号的技术代称，这样也可以省去您加参数的步骤。但由于历史原因，常规直播系统和连麦系统两套后台系统的key值类型不同（一个是数字，一个是字符串），所以采用多加一个 session_id 的参数来绕开兼容问题。
> 
>塞翁失马，焉知非福。由于推流 URL 都是您的服务器拼装下发的，所以 session_id 怎么生成？要不要用后即废？哪些人能够获取？这些权限控制掌握在你的后台系统上也未尝不是个好事情。
 
- **大主播？小主播？**
>文档中我们会反复提到“大主播”和“小主播”的概念，这是从观众视角的一种称谓，“大主播”指的是拥有大画面的那位主播，一般都是房间的开房者。“小主播”则是位于屏幕左下角或者右下角的连麦者，一般都是以小画面的形式出现。


## 化繁为简
不管是同房连麦，还是跨房连麦，连麦本质就是 **一路推流 + 几路播放** 的故事：

- **一路推流**：
只要是主播，不管是“大主播”还是“小主播”，都要推流才能让别人看到自己的影像。推流用自己的直播码推流 URL 即可，额外要做的是在推流 URL 中拼接一段参数，以便告诉服务器这条直播流支持连麦。

- **几路播放**：
想要跟几个人连麦，就要播放几路的音视频数据。但对于连麦而言，时延必须控制在 1 秒以内，所以必须要使用低延时的播放解决方案：
 + 使用 **对方的直播码 + sessionid + 推流防盗链KEY** 拼装出低延迟播放 URL。对，没写错，是推流防盗链KEY。
 + 使用 **PLAY_TYPE_LIVE_RTMP_ACC** 播放参数让 TXLivePlayer 的表现更适应低延时场景。

## 同房连麦
### step1. “大主播”推流
我们在 [iOS推流](https://cloud.tencent.com/document/product/454/7879) 中有详细介绍如何在主播端开启直播功能，这里您可以直接参考，流程上都是一样的。所以，如果您是第一次接触RTMP SDK，务必要先阅读一下基础推流功能的文档。

![](//mc.qcloudimg.com/static/img/779bb742c46a415b505cb8b21c6b2c59/image.png)

需要您注意的是，在连麦场景中有三处差异需要您关注：

- **1.1 推流URL加连麦参数**
在[如何获取推流地址](https://cloud.tencent.com/document/product/454/7915#.E5.90.8E.E5.8F.B0.E8.87.AA.E5.8A.A8.E6.8B.BC.E8.A3.85.EF.BC.9F)中，我们详细介绍了推流地址的拼装规则，如果要做连麦，推流地址里面还要额外加一段参数：
![](//mc.qcloudimg.com/static/img/a066ac2f6caf1764b69477a9aa031d0e/image.png)

 **&mix=layer:s;session_id:1234;t_id:1** 的作用是告诉腾讯云：这条直播流是支持连麦的，连麦房间号为 1234。
 
 [session_id](#.E5.90.8D.E8.AF.8D.E8.A7.A3.E9.87.8A) 的值可以是任意的 **<font color='red'>数字</font>**（如1234，不能是英文字符），但要注意，两个不同房间的 session_id 不要相同，否则后台系统会乱掉。layer 和 tid 是用于后台混流用的参数，[Step5.2](#step5.-.E5.A4.9A.E8.B7.AF.E6.B7.B7.E6.B5.81) 中会做详细说明。
 
- **1.2 TXLivePushConfig**
  + 开启回音消除 enableAEC 
 + 开启硬件加速 enableHWAcceleration 
 + 设置推流分辨率为 VIDEO_RESOLUTION_360_640 （秀场直播最流行的分辨率）
 + 设置推流的码率为 800kbps （这是适合360p的码率，如果想用更高的分辨率，就要需要更高的码率来配合）
 + 设置音频采样率为 <font color='red'>AUDIO_SAMPLE_RATE_48000</font> （不要用其它的）

 ``` 
 //先设置推流参数
 _txLivePush.config.enableAEC = YES;
 _txLivePush.config.enableHWAcceleration = YES;
 _txLivePush.config.videoResolution = VIDEO_RESOLUTION_360_640; // 秀场直播最流行的分辨率
 _txLivePush.config.videoBitratePIN = 800; // 这是适合360p的码率，如果想用更高的分辨率，就要需要更高的码率来配合
 _txLivePush.config.audioSampleRate = AUDIO_SAMPLE_RATE_48000;  // 不要用其它的
 _txLivePush.config.audioChannels   = 1; // 单声道
 //之后再启动推流
 [_txLivePush startPush:rtmpUrl];
```

### step2. 请求连麦
这一步的目的是让“大主播”在交互上有决定权，同时也是让“小主播（们）”拿到低延时链路的“船票”（session_id），这张船票会在 step4 中用到。
![](//mc.qcloudimg.com/static/img/8c22aa239260eb464e69ab5c1dacd87b/image.png)

如上图所示：观众 A 向主播请求 “我想跟你连麦”，主播回应同意或者拒绝。如果同意，主播的回应消息中一定要把 Step1.1 中的 session_id 带给 A。

在实现上，这里可以采用 C2C（Client To Client）消息通道，腾讯云 IM 通讯服务提供了 C2C 解决方案，您可以参考 [如何搭建聊天室](https://cloud.tencent.com/document/product/454/7980) 了解 IM 服务的使用方案。

### step3. “小主播”推流
观众 A 如果得到“大主播”的恩准，就跃身成为“小主播”，接下来“小主播”要开始推流，否则“大主播”看不到“小主播”的影像。
![](//mc.qcloudimg.com/static/img/e65523468a3cdf617f2215b5a07c139a/image.png)

“小主播”推流的对接方案跟 Step1 中“大主播”推流的对接方案一样，也是两处修改点：

- **3.1 推流URL加连麦参数**
 + 推流地址的拼接方式参考 Step1.1 。
 + “小主播”的推流地址中的直播码要用自己的，**不要跟“大主播”的相同**，否则会被腾讯云判定为重复推流而拒绝掉。
 + 对于同间连麦场景，“小主播“的推流地址中的 session_id 建议使用“大主播”的 session_id。
 + 跨房连麦场景中，由于两个主播在连麦前就已经开始推流了，所以 session_id 不要求相同（session_id 被要求是一个数字，如果直播码原本就是数字，可以直接拿直播码当 session_id 来用）。
 
- **3.2 TXLivePushConfig**
 + 开启回音消除 enableAEC 
 + 开启硬件加速 enableHWAcceleration 
 + 设置推流分辨率为 <font color='red'>VIDEO_RESOLUTION_320_480</font> （“小主播”不需要太高分辨率，因为在观众端看到都是小画面）
 + 设置推流的码率为 <font color='red'>300kbps</font>  （码率太高是种浪费）
 + 设置音频采样率为 <font color='red'>AUDIO_SAMPLE_RATE_48000</font> （不要用其它的）

 ``` 
 //先设置推流参数
 _txLivePush.config.enableAEC = YES;
 _txLivePush.config.enableHWAcceleration = YES;
 _txLivePush.config.videoResolution = VIDEO_RESOLUTION_320_480; // “小主播”不需要太高分辨率
 _txLivePush.config.videoBitratePIN = 300; // 码率太高是种浪费
 _txLivePush.config.audioSampleRate = AUDIO_SAMPLE_RATE_48000;  // 不要用其它的
 _txLivePush.config.audioChannels   = 1; // 单声道
 
 //之后再启动推流
 [_txLivePush startPush:rtmpUrl];
```


### step4. 低延时播放链路
经过 Step1 - Step3 之后，“大主播”和“小主播（们）”就已经都在推流了，所以在观众端已经可以同时看到两路（及以上）的画面。但这样还远远不够，因为主播们还无法看到彼此。

我们在 [iOS播放](https://cloud.tencent.com/document/product/454/7880) 中有详细介绍如何在观众端使用播放功能，如果主播们之间也像普通观众一样，采用 CDN 分发的[播放地址](https://cloud.tencent.com/document/product/454/7915#.E5.90.8E.E5.8F.B0.E8.87.AA.E5.8A.A8.E6.8B.BC.E8.A3.85.EF.BC.9F)，当然是可以看到画面听到声音的。

然而，问题出在 **延迟** 上，CDN 播放地址的延迟对于需要实时沟通的主播间通讯而言肯定无法接收。所以，我们需要需要调整 TXLivePlayer 的参数，目的是将大小主播间延迟控制在一秒以内：

#### 4.1 “小主播”看“大主播”
“小主播（们）”不能再继续使用之前的 CDN 观看地址，而是需要**切换**成加速链路，以便能低延迟接收“大主播”的音视频流。
![](//mc.qcloudimg.com/static/img/a98470959a254737e790f06622b2c4aa/image.png)

#### 4.2 “大主播”看“小主播”
“大主播”也需要看到小主播（们）的画面，所以需要**新增**一条低延迟链路来接收“小主播（们）”的音视频流。
![](//mc.qcloudimg.com/static/img/e17f48dc39b0883cac8af03c39fe53f6/image.png)

#### 4.3 启用低延迟播放
不管是“大主播”还是“小主播”，低延时的播放链路都是可以用过 **TXLivePlayer** 来实现的，具体做法如下：

- **4.3.1 生成低延时链路的URL**
![](//mc.qcloudimg.com/static/img/59c492abef77cddaf026cfd7509de678/image.png)
 + URL 必须选用 **rtmp** 播放协议 ，flv 是没有办法做到秒级延迟的。
 + session_id 必须是对方的，简言之，如果是“小主播（们）”这边拼装播放地址，session_id 就是“大主播”的。同房连麦场景，大小主播都共用一个session_id，我们就不用操心这事儿了。
 + 播放地址必须要加防盗链签名，签名方法参考 [推流防盗链的计算](https://cloud.tencent.com/document/product/454/7915#.E9.98.B2.E7.9B.97.E9.93.BE.E7.9A.84.E8.AE.A1.E7.AE.97.EF.BC.9F)。因为几乎所有腾讯云的客户都配置了推流防盗链KEY，为了减少您的接入成本，可以直接使用**推流**防盗链KEY。


- **4.3.2 修改播放器参数**
 + startPlay 的 type 参数需要选用 1.8.2 新增的 **PLAY_TYPE_LIVE_RTMP_ACC**
 + TXLivePlayConfig 中开启回音消除 enableAEC
 + TXLivePlayConfig 中开启硬件加速 enableHWAcceleration
 + TXLivePlayConfig 中将播放模式设置为极速模式，缓冲区改为 200ms
 
 ``` 
 //设置播放器参数
 _txLivePlay.config.enableAEC = YES;              // 开启回音消除
 _txLivePlay.config.bAutoAdjustCacheTime = YES;   // 极速模式 - 有明显的延迟修正表现
 _txLivePlay.config.minAutoAdjustCacheTime = 0.2; // 200ms
 _txLivePlay.config.maxAutoAdjustCacheTime = 0.2; // 200ms
 
 //之后再启动播放
 _txLivePlay.enableHWAcceleration = YES;          // 硬件解码
 [_txLivePlay startPlay:rtmpUrl type:PLAY_TYPE_LIVE_RTMP_ACC];
```

> **<font color='red'>特别提醒</font>**：<font color='black'>加速链路不能用于普通观众端播放！！！</font>
>
>因为加速链路采用了核心节点的带宽，成本几倍于普通 CDN 带宽成本，所以只适用于主播间的实时音视频链路。
>同时，腾讯云限制了一个 session_id 下的加速链路的数量，目前最多为 3 路，后续逐步放开，但最多不会超过 8 路。

### step5. 多路混流
Step1 和 Step3 中有介绍如何让“大主播”和“小主播”使用自己的直播码推流，只要在能拿到两条流的直播码，就可以让所有观众看到多画面叠加（或拼接）的视频流，也就是连麦场景正式成立。

但是如何才能实现多画面叠加（或拼接）的视频流呢？这里有两种方案：

#### 5.1 客户端混流 
源自 RTMP SDK 1.8.2 开始支持的多实例播放，也就是可以并行的播放多个直播 URL， 视频 View 也可以相互叠加。这样一来，只要观众端能拿到多个主播的 URL 就可以实现客户端混流。

- **客户端混流的优势**
  + 由于观众端的表现由App自行控制，能够支持更灵活的界面排布，比如观众可以随意拖拽小画面位置
  
- **客户端混流的不足**
  + 下行数据是多路，所以带宽消耗要高于服务端混流。

- **如何实现客户端混流**？
  + RTMP SDK 1.8.2 开始支持直播播放器多实例运行，所以创建多个 TXLivePlayer 即可实现观众端多路混流。
  + 播放地址推荐使用更稳定的 FLV 播放地址。
  + TXLivePlayConfig 必须采用 1s 固定缓冲区的极速模式，以避免多个播放实例的延迟差异过大，示例代码如下：
  
``` 
 //修改播放器参数
 _txLivePlay.config.enableAEC = NO;               // 观众端无需回音消除
 _txLivePlay.config.bAutoAdjustCacheTime = YES;   // 极速模式 - 有明显的延迟修正表现
 _txLivePlay.config.minAutoAdjustCacheTime = 1;   // 1000ms
 _txLivePlay.config.maxAutoAdjustCacheTime = 1;   // 1000ms
 //之后再启动播放
 _txLivePlay.enableHWAcceleration = YES;          // 硬件解码
 [_txLivePlay startPlay:flvUrl type:PLAY_TYPE_LIVE_FLV];
```

#### 5.2 服务端混流（Beta）
服务端混流是腾讯云近期推出的一项新解决方案，目前外网已经可以支持，但还处于 Beta 阶段，我们还在不断地优化和完善中。它是腾讯云视频转码集群的一个附加模块，可以将多路视频流直接在云端混成一路，减少下行的带宽压力。
![](//mc.qcloudimg.com/static/img/acc74a1e1a53eb7c248da22832ef894c/image.png)

- **服务端混流的优势**
  + 观众端平滑过渡，整个连麦过程中观看地址都是不变的。
  + 下行数据只有一路，所以对于高并发的直播场景，能有效降低带宽消耗。
  + 混流在服务端处理，音画同步问题处理的更好。

- **服务端混流的不足**
  + 目前处于Beta阶段，还只支持 1v1 混流，而且稳定性还稍有不足。

- **如何启用服务端混流？**
  + 在 Step1.1 中，"大主播" mix 参数要补充 layer 和 t_id ：`mix=layer:b;session_id:1234;t_id:1`
	+ 在 Step3.1 中，"小主播" mix 参数要补充 layer 和 t_id ：`mix=layer:s;session_id:1234;t_id:1`
  + layer:b 是代表“大主播”， layer:s 代表“小主播”，t_id 代表混流模板（目前仅支持 t_id 为 1 的混流模板，也就是大画面 + 小画面）
  + 如此操作之后，小主播一旦开始推流，大主播原来的直播流里就会出现一个右下角的小画面，不信您试试？



## 跨房连麦
腾讯云 RTMP 直播支持跨房连麦互动，所以小主播（们）可以是原房间里的普通观众，也可以是另一直播间里的其他主播。

![](//mc.qcloudimg.com/static/img/f864df3868777e1fd0255c9c1b5f3fc2/image.png)

在对接方案上，跨房连麦跟同房连麦并没有太多区别，我们参照同房连麦的思路进行说明：

### step1. “大主播”推流
参考同房连麦的 [step1](#step1.-.E2.80.9C.E5.A4.A7.E4.B8.BB.E6.92.AD.E2.80.9D.E6.8E.A8.E6.B5.81) 即可，不论同房连还是跨连房，“大主播”依然还是“大主播”，只要在推流地址里声明我可以连麦即可。

### step2. 请求连麦
- **同房连麦**：观众向主播发起请求，在得到“大主播”的同意和 session_id 后，升级为“小主播”。
- **跨房连麦**：两个房间的主播都正在推流，所以没有把普通观众升级为“小主播”的说法，但这里依然可以采用发起请求的交互方案，只是请求消息是从一个主播发给另一个主播。

### step3. “小主播”推流
- **同房连麦**：“小主播”推流使用的 session_id 推荐跟“大主播”保持一致，这样比较简单，而且 session_id 相同是两条直播流可以在后台混流的必要条件。
- **跨房连麦**：两个房间的主播本来就处于直播中状态，所以不需要提前协商 session_id，各自指定各自的 session_id，确保两边不相同即可。

### step4. 低延时播放链路
- **跨房连麦**：“小主播” 和 “大主播” 的 session_id 是不一样，所以在拼装低延迟播放URL时，一定要使用对方的session_id，不要用自己的，否则视频卡到崩溃也是很正常的。

### step5. 多路混流
- **跨房连麦**：目前不支持服务端混流，只支持客户端混流。我们会在春节后启用新的commen cgi 风格接口，届时大家会在 [腾讯云服务端API](https://cloud.tencent.com/document/product/454/7920) 中查到该接口的定义。










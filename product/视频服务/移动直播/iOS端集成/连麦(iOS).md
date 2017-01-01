## 何谓连麦
连麦（也叫上麦）是今年比较热门的直播功能，所谓连麦，是指一个直播间中可以不仅只有主播一个人，观众也可以参与进来跟主播进行双向的视频互动。

<div id="id_video_container_14651978969459056454" style="width:100%;height:720px;"></div>
<script src="https://qzonestyle.gtimg.cn/open/qcloud/video/h5/h5connect.js" charset="utf-8"></script>
<script type="text/javascript">
            (function(){
               var option ={"auto_play":"0","file_id":"14651978969459056454","app_id":"1252463788","width":1280,"height":720,"https":1};
               /*调用播放器进行播放*/
               new qcVideo.Player(
                       /*代码中的id_video_container将会作为播放器放置的容器使用,可自行替换*/
                       "id_video_container_14651978969459056454",
                       option
                   );
             })()
 </script>

## 原理解析
关于连麦的技术原理，还是非常简单的，您只要耐心读完下面的一段文字，一定可以理解：

### 1. 从 1 到 N 的变化

我们先从普通的直播模式说起，目前常规的直播遵循如下图所示的模式：主播端（TXLivePusher）将音视频数据推送给云服务器，多个观众端（TXLivePusher）就可以从云端拉流并播放音视频数据。

![](//mc.qcloudimg.com/static/img/a9b501afb5555e5ab790bfe8ad5268d3/image.png)

既然要做连麦，那么反向的一条线路就必不可少了。我们这里做个假设，**观众A** 从原来的普通观众变成了小主播，那么下图中就多出了一条直播流（图中红色虚线所示）：
> 腾讯云 RTMP 直播支持 <font color='red'>**跨房间**</font> 连麦互动，所以**小主播**可以是原来房间里的观众，也可以是另一直播间里的主播。

![](//mc.qcloudimg.com/static/img/5579e666d8ba1ee80c753f15ffbff3d1/image.png)

这看似很简单，而且直接用 RTMP SDK 按这个思路也是可以实现的。但效果却很难理想，因为有两个难题需要我们解决：

- **延迟问题**
常规直播解决方案中，从推流端到播放端，延迟一般在 2-3 秒。但是连麦场景中，大主播和小主播们之间的延迟如果超过1s，和谐的语音沟通就基本不可能了。

- **回音问题**
常规直播解决方案中，由于语音是单向的（主播说 =\> 观众听），所以没有必要去做AEC（回音消除）。但是连麦场景中有双向（或多向）的语音沟通，主播的声音流向小主播那一端的扬声器，如果不做回音消除，这些声音会再经由麦克风采集后返还给主播本人。

### 2. 如何降低延迟？
我们先看看怎么解决延迟问题，要解决延迟，先要弄明白延迟是怎么来的？
![](//mc.qcloudimg.com/static/img/ddf657b4af791b3cb8b7ad2ed62f57be/image.png)
上图中红色标记的三处是整条链路的主要延迟来源，一场延迟大约 3 秒的直播中，以上三个模块“贡献”了 80% 的力量。

#### 2.1 转码模块
- **延迟的原因：**
转码模块的主要工作是对主播推上来的音视频数据做进一步的加工处理，同时，如果您有多清晰度（超清、高清、标清）以及多格式（比如适合 Web 播放的 HLS）的需求，这也是转码模块需要去操心的。

- **应对的思路：**
在连麦场景中，大主播和小主播（们）之间如果都使用 RTMP 协议构建链路，那就不需要转码集群的参与，因为能够省掉这部分延迟。

#### 2.2 CDN集群
- **延迟的原因：**
CDN 集群存在目的是 **分发** 数据流：如果主播在上海，那么他/她肯定是向上海的服务器推流，这样才能保证较好的上传质量，问题来了，桂林和哈尔滨的观众怎么办呢？难道从上海的服务器上去拉流吗？显然这并不是一个好主意，可行的方案是通过 CDN 分发集群将音视频流按需分发到桂林和哈尔滨两个城市。

- **应对的思路：**
连麦场景中，大主播和小主播（们）之间如果都不走 CDN 集群，他们之间的延迟可以缩短很大一截。但这样一来，地域问题如何解决？ 比如有两位主播要连麦互动，一位在深圳，一位在背景，相隔千里，如何才能构建低延时且高质量的直播链路呢？

 腾讯云的解决方案是采用** RtmpAcc 加速节点**，它是我们专门为连麦场景所设立的超低延迟加速集群，在全国各大关键网络节点均有部署。这些加速节点全部由专线连接，唯一的职能便是为处于不同地域、不同运营商的主播，提供可靠而优质的低延时链路。
![](//mc.qcloudimg.com/static/img/323efdd148ffa623a34c6870a98a0b7e/image.png)
 
#### 2.3 播放器缓冲
- **延迟的原因：**
播放器的缓冲是多多少少都要有的，因为下行网络不可能均匀平滑不抖动。缓冲区越长，抗网络抖动的效果就越好，视频的观看体验也就越流畅，同时，这也意味着更大的延迟。常规解决方案中，我们一般设置 500ms 或者 1000ms 以上的播放器缓冲。

- **应对的思路：**
 在连麦场景中，这里就要激进一些，比如200ms的延迟相对适中。于此同时，常规开源解决方案的播放器一般不具备 **延迟修正** 能力，所以随着卡顿次数的增加，延迟也越积越多。在连麦场景下，延迟是不能容忍的，所以延迟修正不仅不可或缺，而且策略也要非常激进。

### 3. 回音消除 AEC
如果要做双向的语音通讯，回音消除是不可或缺的，我们从 RTMP SDK 1.8.2 开始，在 iOS 和 Android 两个平台引入了回音消除模块，从而避免主播在手机的喇叭里听到 1 秒前自己说话的声音。
![](//mc.qcloudimg.com/static/img/31fb2031789350bc88e886b75c03a02d/image.png)

从上图可以看出，AEC模块是躲在 RTMP SDK 里面的，所以在使用上您不需要额外的编程，只需要在 TXLivePushConfig 里把 enableAEC 开关打开即可。

## 对接攻略
以下介绍的是同一房间的连麦攻略，如要实现跨房间连麦，请参阅常见问题 - [如何实现跨房间连麦？](#2.-.E5.A6.82.E4.BD.95.E5.AE.9E.E7.8E.B0.E8.B7.A8.E6.88.BF.E9.97.B4.E8.BF.9E.E9.BA.A6.EF.BC.9F)

### step0. 更新 SDK 版本
RTMP SDK 1.8.2 开始才支持连麦功能，请到 [下载页](https://www.qcloud.com/document/product/454/7873) 更新最新版本的 RTMP SDK。同时，我们的 小直播 [DEMO](https://www.qcloud.com/document/product/454/6991) 也已经集成了这套解决方案的示例代码。

### step1. “大主播”推流
![](//mc.qcloudimg.com/static/img/779bb742c46a415b505cb8b21c6b2c59/image.png)

我们在 [iOS 推流](https://www.qcloud.com/document/product/454/7879) 和 [Android 推流](https://www.qcloud.com/document/product/454/7885) 中有详细介绍如何在主播端开启直播功能，这里您可以直接参考，流程上都是一样的。所以，如果您是第一次接触RTMP SDK，务必要先阅读一下基础推流功能的文档。

连麦场景下有三处差异需要您关注：
- **1.1 推流URL加参数**
在[如何获取推流地址中](https://www.qcloud.com/document/product/454/7915#.E5.90.8E.E5.8F.B0.E8.87.AA.E5.8A.A8.E6.8B.BC.E8.A3.85.EF.BC.9F)，我们详细介绍了推流地址的拼装规则，如果要做连麦，推流地址里面还要额外加一段参数：
![](//mc.qcloudimg.com/static/img/31d741e245bd77b3911d28eb2c216dc6/image.png)

 这段参数是告诉腾讯云，这场直播是支持连麦的。[session_id](#1.-session_id-.E4.BB.80.E4.B9.88.E9.AC.BC.EF.BC.9F) 的值可以是任意的 **<font color='red'>32 位整数</font>**，但要注意，两个不同房间的 session_id 不要相同，否则后台系统会乱掉。
 
- **1.2 TXLivePushConfig**
  + 开启回音消除 enableAEC 
 + 开启硬件加速 enableHWAcceleration 
 + 设置推流分辨率为 VIDEO_RESOLUTION_360_640 （秀场直播最流行的分辨率）
 + 设置推流的码率为 800kbps （斗鱼和映客比这要低一点）
 + 设置音频采样率为 <font color='red'>AUDIO_SAMPLE_RATE_48000</font> （不要用其它的）

 ``` 
 //先设置推流参数
 _txLivePush.config.enableAEC = YES;
 _txLivePush.config.enableHWAcceleration = YES;
 _txLivePush.config.videoResolution = VIDEO_RESOLUTION_320_480; // 秀场直播最流行的分辨率
 _txLivePush.config.videoResolution = 800; // 斗鱼和映客比这要低一点
 _txLivePush.config.videoResolution = AUDIO_SAMPLE_RATE_48000;  // 不要用其它的
 _txLivePush.config.audioChannels   = 1; // 单声道
 //之后再启动推流
 [_txLivePush startPush:rtmpUrl];
```

### step2. 请求连麦
这一步的目的是让“大主播”在交互上有决定权，同时也是让“小主播（们）”拿到低延时链路的“船票”（session_id）。
![](//mc.qcloudimg.com/static/img/8c22aa239260eb464e69ab5c1dacd87b/image.png)

如上图所示：观众 A 向主播请求 “我想跟你连麦”，主播选择同意或者拒绝。如果同意，主播的回应消息中一定要把 Step1.1 中的 session_id 带给 A。

在实现上，这里可以采用 C2C（Client To Client）消息通道，腾讯云 IM 通讯服务提供了 C2C 解决方案，您可以参考 [如何搭建聊天室](https://www.qcloud.com/document/product/454/7980) 了解 IM 服务的使用方案。

### step3. “小主播”推流
观众 A 如果得到“大主播”的恩准，就跃身成为“小主播”，接下来 TA 要开始推流，否则大主播看不到 TA 的影像。
![](//mc.qcloudimg.com/static/img/e65523468a3cdf617f2215b5a07c139a/image.png)

“小主播”推流的注意事项跟 Step1 中“大主播”推流的注意事项一样，也是两条：
- **3.1 推流URL加参数**
 + 推流地址的拼接方式参考 Step1.1 。
 + “小主播”的推流地址中的直播码要用自己的，**不要跟“大主播”的相同**，否则会被腾讯云判定为非法推流。
 + 对于同房间连麦场景，“小主播“的推流地址中的 session_id 建议使用“大主播”的 session_id。跨房间连麦场景中，由于主播都是先开始自主推流的，所以 session_id 推荐用直播码换算。
 
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
 _txLivePush.config.videoResolution = 300; // 码率太高是种浪费
 _txLivePush.config.videoResolution = AUDIO_SAMPLE_RATE_48000;  // 不要用其它的
 _txLivePush.config.audioChannels   = 1; // 单声道
 //之后再启动推流
 [_txLivePush startPush:rtmpUrl];
```


### step4. 打通加速链路
经过 Step1 - Step3 之后，“大主播”和“小主播（们）”就已经都在推流了，所以在观众端已经可以同时看到两路（及以上）的画面，但这样还远远不够，因为主播们无法相互沟通：

#### 4.1 “小主播”看“大主播”
“小主播（们）”不能再继续使用之前的 CDN 观看地址，而是需要**切换**成加速链路，以便能低延迟接收“大主播”的音视频流。
![](//mc.qcloudimg.com/static/img/a98470959a254737e790f06622b2c4aa/image.png)

#### 4.2 “大主播”看“小主播”
“大主播”也需要看到小主播（们）的画面，所以需要**新增**一条低延迟链路来接收“小主播（们）”的音视频流。
![](//mc.qcloudimg.com/static/img/e17f48dc39b0883cac8af03c39fe53f6/image.png)

#### 4.3 如何实现低延时链路？
不管是“大主播”还是“小主播”，低延时的播放链路都是可以用过 **TXLivePlayer** 来实现的，具体做法如下：
- **4.3.1 生成加速链路URL**
![](//mc.qcloudimg.com/static/img/57362a8f433c3d3b0eb944b365f3146d/image.png)
 + URL 必须选用 rtmp 播放协议 ，flv 是没有办法做到秒级延迟的。
 + session_id 必须是对方的，简言之，如果是“小主播（们）”这边拼装播放地址，session_id 就是“大主播”的。当然，如果大主播小主播都共用一个session_id，我们就不操心这事儿了。
 + 播放地址必须要加防盗链签名，签名方法参考 [推流防盗链的计算](https://www.qcloud.com/document/product/454/7915#.E9.98.B2.E7.9B.97.E9.93.BE.E7.9A.84.E8.AE.A1.E7.AE.97.EF.BC.9F)。因为几乎所有腾讯云的客户都配置了推流防盗链KEY，为了减少您的接入成本，可以直接使用推流防盗链KEY。

- **4.3.2 修改播放器参数**
 + startPlay 的 type 参数需要选用 1.8.2 新增的 **PLAY_TYPE_LINK_MIC**
 + TXLivePlayConfig 中开启回音消除 enableAEC
 + TXLivePlayConfig 中开启硬件加速 enableHWAcceleration
 + TXLivePlayConfig 中将播放模式设置为极速模式，缓冲区改为 200ms
 
 ``` 
 //修改播放器参数
 _txLivePlay.config.enableAEC = YES;              // 开启回音消除
 _txLivePlay.config.enableHWAcceleration = YES;   // 硬件解码
 _txLivePlay.config.bAutoAdjustCacheTime = YES;   // 极速模式 - 有明显的延迟修正表现
 _txLivePlay.config.minAutoAdjustCacheTime = 0.2; // 200ms
 _txLivePlay.config.maxAutoAdjustCacheTime = 0.2; // 200ms
 //之后再启动推流
 [_txLivePlay startPlay:rtmpUrl type:PLAY_TYPE_LINK_MIC];
```

> **<font color='red'>特别提醒</font>**：<font color='black'>加速链路不能用于普通观众端播放！！！</font>
>
>因为加速链路采用了核心节点的带宽，成本几倍于普通 CDN 带宽成本，所以只适用于主播间的实时音视频链路。
>同时，腾讯云限制了一个 session_id 下的加速链路的数量，目前最多为 3 路，后续逐步放开，但最多不会超过 8 路。

### step5. 观众端的处理
Step1 和 Step3 中有介绍如何让“大主播”和“小主播”使用自己的直播码推流，只要在能拿到两条流的直播码，就可以让所有观众看到多画面叠加（或拼接）的视频流，也就是连麦场景正式成立。

但是如何才能实现多画面叠加（或拼接）的视频流呢？这里有两种方案：

#### 5.1 客户端混流 
客户端混流的解决方案源自 RTMP SDK 1.8.2 开始支持的多实例播放，也就是可以并行的播放多个直播 URL， 视频 View 也可以相互叠加。

- **客户端混流的优势**
  + 由于观众端的表现由App自行控制，能够支持更灵活的界面排布
  
- **客户端混流的不足**
  + 下行数据是多路，所以带宽消耗要高于服务端混流。
  
- **LivePlayConfig设置**
在设置方面，观众端建议采用来自 CDN 集群的 FLV 地址进行播放，播放模式也尽量采用 1s 固定缓冲区的极速模式。
 ``` 
 //修改播放器参数
 _txLivePlay.config.enableAEC = NO;               // 观众端无需回音消除
 _txLivePlay.config.enableHWAcceleration = YES;   // 硬件解码
 _txLivePlay.config.bAutoAdjustCacheTime = YES;   // 极速模式 - 有明显的延迟修正表现
 _txLivePlay.config.minAutoAdjustCacheTime = 1;   // 1000ms
 _txLivePlay.config.maxAutoAdjustCacheTime = 1;   // 1000ms
 //之后再启动推流
 [_txLivePlay startPlay:flvUrl type:PLAY_TYPE_LIVE_FLV];
```

#### 5.2 服务端混流（Beta）
服务端混流是近期推出的一项试验性解决方案，目前外网已经可以支持，相比于客户端混流，服务端混流具有：
- **服务端混流的优势**
  + 混流在服务端处理，音画同步问题处理的更好。
  + 下行数据只有一路，所以对于高并发的直播场景，能有效降低带宽消耗。

- **服务端混流的不足**
  + 目前处于Beta阶段，还只支持 1v1 混流，而且稳定性还稍有不足。

- **如何启用服务端混流？**
  + 在 Step1.1 中，"大主播" mix 参数要补充 layer 和 t_id ：`mix=layer:b;session_id:1234;t_id:1`
	+ 在 Step3.1 中，"小主播" mix 参数要补充 layer 和 t_id ：`mix=layer:s;session_id:1234;t_id:1`
  + layer:b 是代表“大主播”， layer:s 代表“小主播”，t_id 代表混流模板（目前仅支持id为1的混流模板）
  + 如此操作之后，小主播一旦开始推流，大主播原来的直播流里就会出现一个右下角的小画面，不信您试试？


## 常见问题
### 1. session_id 什么鬼？
session_id 是房间号的概念，就像一群人开会，总要有个会议室一样，连麦的主播们也要有各自所属的房间号。

如果我们做的足够完美，是可以把主播的**推流直播码**直接用作房间号的，因为本来就是一个概念的东西，这样也可以省去您加参数的步骤。但由于常规直播和连麦系统两套后台系统的key值类型不同（一个是数字，一个是字符串），所以才用session_id来绕开兼容问题。
 
 > 塞翁失马，焉知非福。由于推流 URL 都是您的服务器拼装下发的，所以 session_id 怎么生成？要不要用后即废？哪些人能够获取？这些权限控制掌握在你的后台系统上也未尝不是个好事情。


### 2. 如何实现跨房间连麦？
同房间连麦场景中：观众向主播发起请求，在得到“大主播”的同意后，升级为“小主播”。
跨房间连麦场景中：两个房间的主播都正在推流，此时主播A向主播B直接发起连麦邀请，一般用于PK场景中。
但两者的对接流程基本上是一致的，只是些许有差异，我们来关注一下：

- **差异点 - step3 - “小主播”推流**
  + **同房间连麦**：“小主播”推流使用的 session_id 推荐跟“大主播”保持一致。
  + **跨房间连麦**：“小主播”推流使用的 session_id 是一开始推流就确定的，可以随意指定，只要不跟其它主播的冲突即可。如果直播码本来就是数字，那么推荐直接使用直播码。

- **差异点 - step4 - 打通加速链路**
  + **跨房间连麦**：“小主播” 和 “大主播” 的session_id是不一样，所以在拼装低延迟播放URL时，一定要使用对方的session_id，不要用自己的。 

- **差异点 - step5 -  观众端的处理**
 + **跨房间连麦**：目前不支持服务端混流。，只支持客户端混流。




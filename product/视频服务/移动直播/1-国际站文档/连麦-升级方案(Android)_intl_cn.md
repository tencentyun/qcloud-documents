# 腾讯视频云RTMP SDK使用文档-连麦-升级方案（Android） #

-----------------------------------------------------------------------------------------------------------------

本文主要介绍腾讯视频云连麦升级方案的对接方法，连麦旧方案的对接方法可以参考这里[Android视频连麦（旧方案）](https://cloud.tencent.com/document/product/454/8091)，如果您是首次使用视频连麦功能，强烈建议您直接使用连麦升级方案。

### 演示Demo
在详细介绍连麦升级方案的对接攻略之前，先介绍一下2.0.3版本引入的连麦演示Demo，以便您可以快速地体验一下连麦的效果。

![enter image description here](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/linkmic_demo_step.png)

假设用户A和用户B进行连麦，连麦演示Demo的使用方法是：

1. 用户A、用户B分别生成自己的推流地址和拉流地址；需要特别注意的是，**拉流地址里必须包括防盗链key：即必须包含bizid、txSecret和txTime三个参数**，具体生成方式请参考本文后面[加速拉流链路URL](https://cloud.tencent.com/document/product/454/8872#.E6.AD.A5.E9.AA.A4.E4.BA.8C.EF.BC.9A.E4.BA.92.E7.9B.B8.E6.8B.89.E6.B5.818)里的介绍；

```
推流地址A: rtmp://3891.livepush.myqcloud.com/live/3891_streamA?bizid=3891&txSecret=9d6e1a1ec1dde00dab718e5684ad53a3&txTime=5919D07F

拉流地址A: rtmp://3891.liveplay.myqcloud.com/live/3891_streamA?bizid=3891&txSecret=9d6e1a1ec1dde00dab718e5684ad53a3&txTime=5919D07F

推流地址B：rtmp://3891.livepush.myqcloud.com/live/3891_streamB?bizid=3891&txSecret=d37f5d7c6a3cd426105e57d6eb4900e8&txTime=5919D07F

拉流地址B：rtmp://3891.liveplay.myqcloud.com/live/3891_streamB?bizid=3891&txSecret=d37f5d7c6a3cd426105e57d6eb4900e8&txTime=5919D07F
```

2. 在连麦演示TAB界面，用户A、用户B分别扫描**自己的推流地址**，启动推流；可以点击右下角的"大主播"或者"小主播"按钮，模拟大主播或者小主播推流；
3. 在连麦演示TAB界面，用户A、用户B分别点击右上角的+按钮，扫描**对方的拉流地址**，添加一路拉流；
4. 经过步骤2和步骤3两步操作，用户A和用户B在推流的同时，互相拉取到了对方的视频流，也即在二者之间建立起了双向实时视频对话，具体效果如下图所示。

![enter image description here](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/linkmic_demo_example.png)

【特别说明】
- 步骤3中“扫描一个拉流地址，添加一路拉流”，必须保证拉流地址包含防盗链key；因为只有包含防盗链key，演示Demo才会使用本文后面介绍的加速拉流接口进行拉流播放，以降低视频时延，并做音频回声消除；
- 连麦演示Demo只用于在大、小主播之间建立双向实时视频对话，没有做视频混流，其它第三方观众看到的还是大主播一个人的视频画面；您在实际对接过程中，需要按照本文后面介绍的[视频混流方法](https://cloud.tencent.com/document/product/454/8872#.E6.AD.A5.E9.AA.A4.E4.B8.89.EF.BC.9A.E5.90.AF.E5.8A.A8.E6.B7.B7.E6.B5.8111)，对大、小主播做视频混流，才可以达到真正的连麦效果。

### 对接攻略

使用连麦升级方案，需要把SDK的版本更新到2.0.1以上版本；相比旧的连麦方案，升级后的方案能力更为强大，其主要特点有：

- 支持多人连麦，最多支持3个小主播同时和大主播进行视频连麦
- 可以自定义设置混流后小画面的位置
- 启动视频混流更加灵活，通过CGI调用的方式，可以把任意两路（最多支持四路）视频流混为一路视频


使用升级方案进行视频连麦，需要完成如下三步：

1.  **启动推流**：大主播推流，不必多说；小主播在启动推流之前，最好先向大主播发起连麦请求，收到大主播接受连麦的响应后，再启动推流，推流成功后，把自己的拉流地址发给大主播，以便大主播可以拉到小主播的视频流；
1.  **互相拉流**：使用RTMP SDK提供的加速拉流接口（可以大幅度降低时延），大、小主播互相拉取对方的视频流，这样就可以在大、小主播之间建立双向视频对话；
1.  **启动混流**：调用视频云提供的视频混流CGI，把小主播的视频叠加到大主播的视频流上面（包括音频），其它观众可以自动看到大、小主播的视频画面。

如果有多个小主播同时和大主播连麦：步骤2中，小主播之间也需要互相拉流，以便建立多向视频对话；步骤3中，需要调用混CGI，把多个小主播的视频叠加到大主播的视频流上。



### 步骤一：启动推流

在升级方案里，大、小主播启动推流时，都**不需要在推流地址的后面添加连麦参数**（旧方案里，大主播需添加连麦参数mix=layer:b;session_id:xxxx;t_id:1，小主播需添加连麦参数mix=layer:s;session_id:xxxx;t_id:1，以便启动服务端视频混流）；升级方案通过调用后台CGI的方式启动视频混流，使用更加灵活；

我们在文档[Android推流](https://cloud.tencent.com/document/product/454/7885)中有详细介绍如何在主播端开启直播推流功能，您可以直接参考，如果您是第一次接触RTMP SDK，务必要先阅读一下基础推流功能的文档。

需要注意的是连麦模式下推流有两点差异：一是需要开启回音消除，二是需要采用合理的调控策略来控制时延。对于这两点差异，其实您可以不用关心，我们强烈建议您使用SDK从1.9.2开始提供的视频质量设置接口 setVideoQuality ，视频质量有如下几个枚举值，每一个都对应了一组质量参数，比如视频分辨率、码率、帧率、是否开启回音消除等，这些参数是我们精心优化的，您可以放心使用。

```
/**
 * 视频质量定义
 */
public static final int VIDEO_QUALITY_STANDARD_DEFINITION       = 1;  //标清
public static final int VIDEO_QUALITY_HIGH_DEFINITION           = 2;  //高清
public static final int VIDEO_QUALITY_SUPER_DEFINITION          = 3;  //超清
public static final int VIDEO_QUALITY_LINKMIC_MAIN_PUBLISHER    = 4;  //大主播，连麦模式下使用
public static final int VIDEO_QUALITY_LINKMIC_SUB_PUBLISHER     = 5;  //小主播，连麦模式下使用
```


详细解释一下这几种画质

- VIDEO_QUALITY_STANDARD_DEFINITION：标清 - 采用 360 * 640 级别分辨率，码率会在 400kbps - 800kbps 之间自适应，如果主播的网络条件不理想，直播的画质会偏模糊，但总体卡顿率不会太高。采用软编码，软编码虽然更加耗电，但在运动画面的表现要优于硬编码。
- VIDEO_QUALITY_HIGH_DEFINITION ：高清 - 采用 540 * 960 级别分辨率，码率会锁定在 1000kbps，如果主播的网络条件不理想，直播画质不会有变化，但这段时间内会出现频繁的卡顿和跳帧。 采用软编码，软编码虽然更加耗电，但在运动画面的表现要优于硬编码。
- VIDEO_QUALITY_SUPER_DEFINITION：超清 - 采用 720 * 1280 级别分辨率，码率会锁定在 1500kbps，对主播的上行带宽要求比较高，适合观看端是大屏的业务场景。
- VIDEO_QUALITY_LINKMIC_MAIN_PUBLISHER：大主播 - 顾名思义，连麦中大主播使用，因为是观众的主画面，追求清晰一些的效果，所以分辨率会优先选择 540 * 960。
- VIDEO_QUALITY_LINKMIC_SUB_PUBLISHER：小主播 - 顾名思义，连麦中小主播使用，因为是小画面，画面追求流畅，分辨率采用 320 * 480， 码率 350kbps 固定。

【特别说明】

1. 如果是秀场直播，推荐使用【高清】，虽说“马上看壮士，月下观美人”是有这么一说，但是看完某椒就知道清晰有多么重要了。
2. 使用 setVideoQuality 之后，依然可以使用 TXLivePushConfig 设置画质，以最后一次的设置为准。
3. 如果您是手机端观看，那么一般不推荐使用【超清】选项，我们做过多组的画质主观评测，在小屏幕上观看几乎看不出差别。

#### 大主播推流
大主播启动推流， 请按照如下方式调用：

```
TXLivePushConfig config = new TXLivePushConfig();
config.setAudioSampleRate(48000); //音频采样率默认就是48K，不要设为其它值 
mLivePusher = new TXLivePusher(context);
mLivePusher.setPushListener(listener);
mLivePusher.setConfig(config);
mLivePusher.setVideoQuality(TXLiveConstants.VIDEO_QUALITY_HIGH_DEFINITION); //非连麦模式：高清
mLivePusher.startCameraPreview(txCloudVideoView);
mLivePusher.startPusher(pusherUrl);
```


如果有小主播和大主播连麦，也即**第一个小主播加入连麦**后，请您调用：

```
mLivePusher.setVideoQuality(TXLiveConstants.VIDEO_QUALITY_LINKMIC_MAIN_PUBLISHER); //连麦模式：大主播
```


如果没有小主播和大主播连麦，也即**最后一个小主播退出连麦**后，请您调用：

```
mLivePusher.setVideoQuality(TXLiveConstants.VIDEO_QUALITY_HIGH_DEFINITION); //非连麦模式：高清
```


通过调用接口setVideoQuality，SDK内部会自动选择最优的分辨率、帧率、码率及码率调控策略等视频质量参数。需要说明的是，如果没有小主播和大主播连麦，强烈不建议选择VIDEO_QUALITY_LINKMIC_MAIN_PUBLISHER。因为这种方式追求的是尽量降低时延，可能会影响流畅性；同时会开启回音消除，会有额外的性能损耗。

#### 小主播推流
小主播启动推流，请按照如下方式调用：

```
TXLivePushConfig config = new TXLivePushConfig();
config.setAudioSampleRate(48000); //音频采样率默认就是48K，不要设为其它值 
mLivePusher = new TXLivePusher(context);
mLivePusher.setPushListener(listener);
mLivePusher.setConfig(config);
mLivePusher.setVideoQuality(TXLiveConstants.VIDEO_QUALITY_LINKMIC_SUB_PUBLISHER);	//连麦模式：小主播
mLivePusher.startCameraPreview(txCloudVideoView);
mLivePusher.startPusher(pusherUrl);
```


通过调用接口setVideoQuality，选择VIDEO_QUALITY_LINKMIC_SUB_PUBLISHER，SDK内部会自动选择最优的分辨率、帧率、码率及码率调控策略等视频质量参数，同时会开启音频回音消除。

【特别说明】

- 小主播在启动推流之前，最好先向大主播发起连麦请求，收到大主播接受连麦的响应后，再启动推流；
- 小主播在推流成功之后，即收到开始推流的事件PUSH_EVT_PUSH_BEGIN后，要把自己的拉流地址发给大主播，以便大主播可以拉到小主播的视频流；如果是多人连麦，还要把自己的拉流地址扩散给其它小主播，以便小主播之间互相拉流；
- 小主播推流的目的，只是为了连麦，请不要把小主播的拉流地址加入到您App的直播列表里。

###  步骤二：互相拉流

连麦模式下，大、小主播之间互相拉流，必须使用SDK提供的加速拉流接口；在介绍加速拉流接口的使用方法之前，先说明一下，需要互相拉流的三种场景：

- 小主播在连麦之前，作为普通观众，通过普通拉流接口（文档[Android拉流](https://cloud.tencent.com/document/product/454/7886)）观看大主播的视频；小主播加入连麦后，必须通过加速拉流接口观看大主播的视频；小主播退出连麦后，必须切换为普通拉流接口观看大主播的视频。
- 大主播在连麦之前，不需要拉取视频流；连麦之后，需要通过加速拉流接口观看小主播的视频。
- 如果有多个小主播（目前最多支持三个）同时和大主播连麦：那么大主播需要通过加速拉流接口，拉取每一个小主播的视频流；小主播除了要拉取大主播的视频流，还需要拉取其它所有小主播的视频流。

下面，详细介绍一下加速拉流接口的使用方法：

#### 1. 生成加速拉流链路的 URL

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/RTMP加速拉流地址.png)

这里需要注意的有两点：

- URL 必须选用 rtmp 播放协议 ，flv 是没有办法做到秒级延迟的。
- 播放地址必须要加防盗链签名，签名方法参考[ 推流防盗链的计算](https://cloud.tencent.com/document/product/454/7915#.E9.98.B2.E7.9B.97.E9.93.BE.E7.9A.84.E8.AE.A1.E7.AE.97.EF.BC.9F)。因为几乎所有腾讯云的客户都配置了推流防盗链KEY，为了减少您的接入成本，可以直接使用推流防盗链KEY; 如果您接入腾讯云直播时设置了拉流防盗链KEY，那么请使用拉流防盗链KEY。

#### 2. 设置播放器参数

startPlay 的 type 参数需要选用 1.8.2 新增的 **PLAY_TYPE_LIVE_RTMP_ACC**

举例说明加速拉流接口的使用方法

```
String playUrl = "rtmp://8888.liveplay.myqcloud.com/live/8888_test?bizid=8888&txSecret=xxxx&txTime=xxx"; //加速拉流地址必须带防盗链key
TXLivePlayConfig playConfig = new TXLivePlayConfig();
mLivePlayer = new TXLivePlayer(context);
mLivePlayer.setConfig(playConfig);
mLivePlayer.setPlayListener(listener);
mLivePlayer.setPlayerView(mVideoView);
mLivePlayer.startPlay(playUrl, TXLivePlayer.PLAY_TYPE_LIVE_RTMP_ACC); //开始播放，type参数必须设置为PLAY_TYPE_LIVE_RTMP_ACC
```


【特别提醒】

加速链路不能用于普通观众端播放！！！因为加速链路采用了核心节点的带宽，成本几倍于普通 CDN 带宽成本，所以只适用于主播间的实时音视频链路。同时，腾讯云限制了每一条流通过加速拉流接口观看的链路数，目前最多为5路。

### 步骤三：启动混流

视频混流的目的，在于将一个或者多个（最多三个）小主播的视频画面叠加到大主播的视频流上（包括音频），从而使得普通观众可以看到小主播的视频画面。腾讯视频云通过对外提供 common API 的方式，来提供混流能力；你可以随时调用混流 CGI，来启动或者结束混流；并可以自定义设置混流的方式，即指定小画面相对于大画面的位置关系。

下面，详细介绍一下混流 CGI 的使用方法：

#### 1. 通过 HTTP 协议，请求这个 CGI

```
http://fcgi.video.qcloud.com/common_access
```


#### 2. 通过GET方式传递鉴权参数

```
http://fcgi.video.qcloud.com/common_access?cmd=appid&interface=Mix_StreamV2&t=t&sign=sign
```


- **cmd**：填写直播APPID，用于区分不同客户的身份
- **interface**：固定填写Mix_StreamV2
- **t（过期时间）**：UNIX时间戳，即从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数；这个字段表示的是请求过期时间，请您在获取当前时间（秒）的基础上加60秒偏移
- **sign（安全签名）**： sign = MD5(key + t) ，即把加密key 和 t 进行字符串拼接后，计算一下md5值。这里的key是您在腾讯云直播管理[控制台](https://console.cloud.tencent.com/live/livecodemanage)中设置的API鉴权key

举例说明安全签名**sign**的计算方法 

```
key = "40328529ca4381a80c6ecf2e6aa57438"                    //API鉴权key 
t = 1490858347                                              //t 过期时间
key + t = "40328529ca4381a80c6ecf2e6aa574381490858347"      //key 和 t 进行字符串拼接
sign = MD5（key + t） = "7f29ed83c61b77de1b0d66936fd4fd44"   //对拼接后的字符串计算MD5
```


#### 3. 通过POST方式传递混流参数

混流参数是json格式的字符串，用来指定对哪些视频流进行混流操作以及混流的方式，下面举例说明

```
{
    "timestamp":int(time.time()),           # UNIX时间戳，即从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数
    "eventId":int(time.time()),             # 混流事件ID，取时间戳即可，后台使用
    "interface":
    {
        "interfaceName":"Mix_StreamV2",	    # 固定取值"Mix_StreamV2"
        "para":
        {
            "app_id": appid,                # 填写直播APPID
            "interface": "mix_streamv2.start_mix_stream_advanced",  # 固定取值"mix_streamv2.start_mix_stream_advanced"
            "mix_stream_session_id" : "3891_denny1",                # 填大主播的流ID
            "output_stream_id": "3891_denny1",                      # 填大主播的流ID
            "input_stream_list":
            [
                # 大主播：背景画面
                {
                    "input_stream_id":"3891_denny1",    # 流ID
                    "layout_params":
                    {   
                        "image_layer": 1                # 图层标识号：大主播填 1 ;  小主播按照顺序填写2、3、4
                    }   
                },
                # 小主播1
                {
                    "input_stream_id":"3891_denny2",    # 流ID
                    "layout_params":
                    {   
                        "image_layer": 2,               # 图层标识号
                        "image_width": 160,             # 小主播画面宽度
                        "image_height": 240,            # 小主播画面高度
                        "location_x": 380,              # x偏移：相对于大主播背景画面左上角的横向偏移
                        "location_y": 630               # y偏移：相对于大主播背景画面左上角的纵向偏移
                    }   
                 },
                # 小主播2
                 {
                     "input_stream_id":"3891_denny3",
                     "layout_params":
                     {
                         "image_layer": 3,
                         "image_width": 160,
                         "image_height": 240,
                         "location_x": 380,
                         "location_y": 390
                     }
                 },
                # 小主播3
                 {
                     "input_stream_id":"3891_denny4",
                     "layout_params":
                     {
                         "image_layer": 4,
                         "image_width": 160,
                         "image_height": 240,
                         "location_x": 380,
                         "location_y": 150
                     }
                 }
            ]
        }
    }
}
```


详细解释一下混流参数

- 上面混流参数里，以#开始的内容是python格式的注释；
- 字段timestamp和eventId都取当前时间（秒）即可；
- 字段mix_stream_session_id和output_stream_id都填大主播的流ID；
- 字段input_stream_list是一个数组，包含了需要混流的视频流信息；这个数组里必须包含大主播的视频流，但视频流的数目不能超过4路，因为混流后台目前最多支持4路混流；
- 字段layout_params用于设置视频流排布参数；大主播的画面默认铺满整个屏幕，只需要将字段image_layer填写为1，不需要填写其它字段；image_layer是图层标识号，小主播请按照顺序，依次填写2、3或者4；
- 字段image_width、 image_height、 location_x、 location_y用来定义小画面相对于大画面的位置；需要注意的是，小画面的上、下、左、右四个位置都不能超过大画面的范围，即：location_x不能小于0，不能超过大画面的宽度；location_y不能小于0，不能超过大画面的高度； location_x + image_width之和不能超过大画面的宽度；location_y + image_height之和不能超过大画面的高度；


#### 4. CGI返回的是一段json格式的字符串，如下所示

```
{"code":0, "message":"Success!", "timestamp":1490079362}
```
    

- **code**: 错误码，0表示成功，其它表示失败
- **message**:错误描述信息
- **timestamp**:时间戳，取值与混流参数里的timestamp相同


关于启动视频混流的其它注意事项

- 混流CGI没有显式区分启动混流和结束混流，“是否需要混流”以及“把几路流混在一起”是由混流参数input_stream_list数组里视频流的数目决定的；如果视频流的数目大于1，就会启动混流；如果只有大主播一条视频流，就会结束混流；
- 鉴权参数建议在您App的后台服务端生成，因为基于保密性的考虑，API鉴权KEY不能放在前端App；混流参数建议您在大主播端生成，因为“有没有连麦（是否需要启动混流）”以及“有哪些小主播加入连麦（要对哪些视频流做混流操作）”，只有大主播最为清楚；混流CGI请求可以在后台服务端发起（需要把混流参数发送给后台，请后台代为发送混流请求），也可以在大主播端发起（需要向后台请求鉴权参数）；
- 启动混流之前必须确认大、小主播都已经推流成功了，也即必须在收到推流成功事件PUSH_EVT_PUSH_BEGIN之后调用混流CGI；否则会失败，CGI回包里code字段非0；
- 如果确认是在收到PUSH_EVT_PUSH_BEGIN事件之后调用的混流CGI，却仍然返回失败；这种情况下，可以采取重试策略，建议每2秒重试一次，最多重试5次；出现这种情况，是因为PUSH_EVT_PUSH_BEGIN事件，只是表示SDK成功地把第一个视频关键帧发送给服务器了，视频云后台流状态同步会有滞后。


###  与连麦旧方案的兼容方法

如果您是直接对接的连麦升级方案，则不存在与旧方案的兼容性问题，不需要关注下面介绍的内容。

如果您之前对接了连麦旧方案，请按照下面介绍的方式，解决与旧版本的兼容性问题。

连麦升级方案与旧方案的兼容性问题，是由于在升级方案里，大、小主播推流时，不需要在推流地址的后面添加连麦参数，这会导致如下两个兼容性问题：

#### 兼容性问题一
如果大主播使用的是新版本，小主播使用的是旧版本；那么小主播无法通过加速拉流接口拉取到大主播的低时延流，导致无法进行视频对话；

**解决办法**：新版本里的大主播启动推流时，请在推流地址的后面添加参数"&mix=session_id:xxxx"，请确保session_id的取值，与小主播（使用的是旧版本）连麦参数里的session_id相同。

#### 兼容性问题二
如果大主播使用的是旧版本，小主播使用的是新版本；那么大主播无法通过加速拉流接口拉取到小主播的低时延流，无法进行视频对话；同时无法启动后台视频混流，普通观众看不到小主播的画面；

**解决办法**：新版本里的小主播启动推流时，请按照原来的方式，在推流地址的后面添加连麦参数"mix=layer:s;session_id:xxxx;t_id:1",请确保session_id的取值，与大主播（使用的是旧版本）连麦参数里的session_id相同。
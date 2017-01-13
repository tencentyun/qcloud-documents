## 基础篇
目前常见的直播协议有三种：RTMP、 FLV 和 HLS。
目前常见的点播格式有三种：MP4、HLS和FLV。
![vod_video_protocol](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/vod_video_protocol.jpg)


影响画质的主要因素是三个：**分辨率**、**帧率**和**码率**。


这里说的**延迟**是主播 -> 观众的时间延迟，而**卡顿**指的是出现500ms以上的播放停滞。
如果是在完美的网络环境下，可以做到超低延迟下没有卡顿，但现实是国内的网络环境并不完美，数据在经过互联网传输时必然会有抖动和丢包，从而对播放端的流畅播放产生影响。
![tx_live_service_lag](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/tx_live_service_lag.jpg)

因此，为了缓解这些不稳定因素，云服务和终端APP都需要引入一些缓冲，但缓冲的加入就不可避免地引入了延迟。
所以，**延迟和流畅是一架天平的两端**，如果过分强调降低延迟，就会导致轻微的网络波动即产生明显的播放端卡顿。反推之，如果过分强调流畅，就意味着引入大量的延迟，一个典型的案例就是HLS协议，通过引入10-30秒的延迟来实现流畅的播放体验。
- **自动模式**：如果您不太确定您的主要场景是什么，可以选择这个模式。
>当把播放器中的 setAutoAdjustCache 开关打开，即为自动模式，在该模式下，播放器会根据当前网络情况，对延迟进行自动调节，默认情况下，播放器会在1s - 5s 这个区间内自动调节延迟大小（您也可以通过setMinCacheTime 和 setMaxCacheTime对默认值进行修改），以保证在足够流畅的情况下尽量降低观众跟主播端的延迟，确保良好的互动体验。

- **极速模式**：主要适用于**秀场直播**和**全民直播**等对延迟要求比较苛刻的场景。
> 我们所谓的极速模式，即（setMinCacheTime = setMaxCacheTime = 1s） ， 而您也发现了，自动模式跟极速模式的差异只是MaxCacheTime 有所不同 （极速模式的 MaxCacheTime 一般比较低，而自动模式的MaxCacheTime 则相对较高 ），这种灵活性主要得益于SDK内部的自动调控技术，可以在不引入卡顿的情况下自动修正延时大小，而MaxCacheTime 反应的就是调节速度：MaxCacheTime的值越大，调控速度会越发保守，当然卡顿概率就会越低。
 
- **流畅模式**：主要适用于**游戏直播**和**点播场景**等对延迟要求不是特别高的场景。
> 当把播放器中的 setAutoAdjustCache 开关关闭，即为流畅模式，在该模式下，播放器采取的处理策略跟Adobe FLASH内核的缓存出策略如出一辙：当视频出现卡顿后，会进入 loading 状态直到缓冲区蓄满，之后进入playing状态，直到下一次遭遇无法抵御的网络波动。默认情况下，缓冲大小为5s，您可以通过setCacheTime进行更改。
> 
> 在延迟要求不高的场景下，这种简单的模式会更加可靠，我们在视频云SDK中引入这种模式主要是很多采纳了很多优秀客户的建议，即希望在播放过程中有平滑的loading和playing状态切换。但采用极速模式时，对于低时延的追求会导致这种切换往往非常频繁进而引发loading闪烁。

- **0. ![diff](//mccdn.qcloud.com/static/img/1d093770d4b9bfaec5e15b01bdb65d00/image.png)
>这种情况下，您需要点击右上角的**编辑**按钮，勾选FLV协议前的复选框，从而开启FLV观看地址。
![conflict](//mccdn.qcloud.com/static/img/e8c4de29cb91419ba50146c0cacfd824/image.jpg)
后台是不是打水印了**

- **step4. 刚推流即播放**
腾讯云后台的流媒体处理流水线是需要一点时间做缓冲和预热的，所以如果刚开始推流，立刻点开播放，这时的测试数据并不是特别可靠，推荐您在推流后等15-30s再测试真实的延迟。

- **step5. 第三方推流器**
较低的延迟，我们只能确保在腾讯云一体化解决方案中能够达到理想的效果，如果您使用的是第三方推流软件，建议您先换成腾讯云RTMP SDK的推流Demo做个对比，排除一下这里引入问题的可能。



### 如何提取SDK输出的Log?
您可以通过调用TXLivePlayer或TxLivePush中的**setLogLevel**接口设置Log级别。
如果您使用的安卓手机，我们的Log存储在/sdcard/txRtmpLog目录下，您可以通过adb相关命令查看并提取Log文件：
![](//mccdn.qcloud.com/static/img/1a38cf482394d8e6ab678d44c4059a63/image.png)
如果您使用iPhone手机，我们的Log直接存储在Documents目录下，您可以通过itools工具导出Log文件：

## 集成篇

### 命名冲突（duplicate symbol）
在集成本SDK时常遇到的一种编译错误，因为一个进程中不能有重名函数（编译器会将函数编译成symbol），如果出现重复的，就会给链接器带来“选择困难症”。

如果您的APP之前使用过类似ffplay这样的播放器，请先将其从工程中移除掉。目前我们团队还没有实力去研发自己的H264软件编解码器，所以也是使用了ffmpeg这样的开源模块来实现H264视频流的编码和解码，只是修复了其中的一些bug而已。如果您的工程中之前就已经包含了它们，自然会带来命名冲突的问题。
![txc_rtmp_sdk_duplicated_symbol](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/txc_rtmp_sdk_duplicated_symbol.jpg)

一般IOS的工程会比较容易遇到这个问题，如果您APP原来就打包有ffmpeg而且确实无法放弃，这里的应对方案如下：
确保您的工程中的ffmpeg已经更新至最新版本（3.0.2）。
2. 检查一下Xcode工程设置中"Other Linker Flags"是否包含**-all_load**，如有请去掉。

这种方案的本质是让APP里链接两份ffmpeg，但是Xcode链接器没有办法做到聪明的可以判断出来两个库的精确调用关系，所以实际上APP内部的两个ffmpeg的调用关系是不可控的（有可能两个库之间的函数交错式调用）。

所以，<font color='red'>如果两个ffmpeg版本不一致，会出现莫名其妙的各种crash</font>，而且这种crash看堆栈一般都是崩溃在ffmpeg内部函数里。

### Android 出现程序崩溃（CRASH）
- **代码混淆原因**

- **工程配置原因**
```java
java.lang.UnsatisfiedLinkError: No implementation found for 
int[] com.tencent.rtmp.TXRtmpApi.getSDKVersion() 
(tried Java_com_tencent_rtmp_TXRtmpApi_getSDKVersion and Java_com_tencent_rtmp_TXRtmpApi_getSDKVersion)
```
解决方法就是检查一下工程配置，这里要特别说明一下，1.4.1 以及以前的版本，我们都是使用了aar作为sdk打包方案，这种android studio推荐的打包方案虽然感觉比较高大上，但实际兼容性并不好，所以在1.4.2版本开始，我们开始推行传统的jar解决方案，如果您现在拿到的是aar版本的sdk组件包，我建议您尝试一下jar版本的。
不少客户在APP中集成了不止一家的播放器，这里我们需要注意的是，目前国内少有互联网公司会自己研发H264编解码器，包括腾讯在内也是使用现在常见的ffmpeg等开源组件实现视频的软件编解码，所以编解码库的冲突非常普遍。如果您遇到各种百思不得解的运行冲突问题，可以考虑先临时把其它播放器屏蔽一下，看看是不是对稳定定位有所帮助。


### IOS 找不到函数定义（Undefined Symbols  ）
一般是工程配置问题，尤其是IOS下分多种指令架构，armv7, arm64, x86模拟器等等，另外检查下IOS工程的Link Binary With Libraries的配置，我们的SDK需要依赖的库如下（请参考demo工程的配置）：
![txc_rtmp_sdk_link_lib](//mccdn.qcloud.com/static/img/6605e78efb384799b9b4e1c6a5a7aac6/image.jpg)
如果出现如下错误：
请检查工程的c++库的配置：
![](//mccdn.qcloud.com/static/img/07665b7aa7f6495417bb8e2f850f3afa/image.jpg)
- **可能情况一**：


![](//mccdn.qcloud.com/static/img/64012a07f85259bb3246c40e1014dcb4/image.png)

step 1：确认播放端是否采用的是FLV 协议，RTMP协议由于本身是贯彻了大包拆小包的设计理念，所以数据包的拼接操作非常频繁，在海量并发的服务端，出现低概率数据包拼装错误不可能完全避免。所以我们不推荐采用RTMP作为直播的播放端协议。

step 2：请使用腾讯视频云的SDK DEMO验证一下是否同样存在这个问题，因为我们的DEMO有专业的团队测试验证过，如果也出现绿屏，说明云端问题确实比较明显。

step 3：如果出现大面积的花屏或者绿屏，并且推流端使用的是腾讯视频云SDK，可以检查一下推流端是否有切换视频分辨率的操作，按照规范操作，切换分辨率需要重新推流（或者至少向服务器补发sps 和 pps 信息，不过这个操作太专业了，您还是直接重启推流 stopPush& startPush 更加简单可靠一点）。

### 直播时出现黑屏&黑边
- **权限限制**：
>没有打开摄像头的权限，这时候一般会收到PUSH_ERR_OPEN_CAMERA_FAIL的事件，请检查摄像头权限，如果没有收到这个事件，请联系我们并告知机型&系统；另外需要特别注意的是Android 6.0的系统，摄像头的权限需要自行判断并启用摄像头权限，否则将出现黑屏
>
- **分辨率超标**：
>超过SDK支持的最大分辨率，SDK最大支持1920*1080的分辨率，请检查视频的分辨率
>
- **显示模式**：
>显示模式 setRenderMode 可能设置成了 RENDER_MODE_ADJUST_RESOLUTION ，但画面又不符合屏幕当前的宽高比，比如16：9 的画面在4：3的屏幕上显示。

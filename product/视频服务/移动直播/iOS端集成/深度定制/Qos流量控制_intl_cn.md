
## 背景说明
RTMP 推流质量对于观看体验非常关键，因为如果主播的推流质量不佳，那么所有观众看到的视频画面都是卡顿的，据统计，视频云客户群 80% 以上的直播间卡顿问题均是由于 RTMP 推流质量不佳导致的。

在众多的推流质量问题中，主播的上行网络不给力引发的问题又是最主要的，上行带宽不足会导致音视频数据在主播端堆积并丢弃，从而使观众端看到的视频画面出现卡顿甚至长时间卡死。

![](//mc.qcloudimg.com/static/img/3c10b3a268b4807a184b767b1cc4363c/image.png)

所以，优化主播上行卡顿问题能够有效地提升推流质量，进而提升观看端的质量，尤其在国内运营商普遍限制上行带宽的情况下。

但是网络问题不随人的意志为转移，主播家里买的 4Mbps 宽带套餐，不可能因为主播装一个 App 就让其变成 8Mbps，因此，我们只能采用顺势而为的做法 —— **主动适应上行网络的情况**。

## 快速对接
使用 TXLivePusher 的 setVideoQuality 接口的 参数即可开启 Qos 流控，开启 Qos 流控以后 SDK 会根据主播上行网络的好坏决定视频的清晰度。

![](//mc.qcloudimg.com/static/img/c52dc506047402db04ac285fa7520e65/image.png)

- **quality**
SDK 提供了六种基础档位，根据我们服务大多数客户的经验进行积累和配置。其中 STANDARD、HIGH、SUPER 适用于直播模式，MAIN_PUBLISHER 和 SUB_PUBLISHER 适用于连麦直播中的大小画面，VIDEOCHAT 用于实时音视频。

- **adjustBitrate**
是否开启 Qos 流量控制，开启后SDK 会根据主播上行网络的好坏自动调整视频码率。相应的代价就是，主播如果网络不好，画面会很模糊且有很多马赛克。

- **adjustResolution**
是否允许动态分辨率，开启后 SDK 会根据当前的视频码率选择相匹配的分辨率，这样能获得更好的清晰度。相应的代价就是，动态分辨率的直播流所录制下来的文件，在很多播放器上会有兼容性问题。

![](//mc.qcloudimg.com/static/img/07deb1e7e01daba3227175a0fcec1fa5/image.png)

## 精细校调
如果您觉得 setVideoQuality 里的默认参数无法满足您的需求，您可以通过 TXLivePushConfig 进行定制：

- **enableAutoBitrate**
是否开启码率自适应，也就是 Qos 流控，如果开启，开启后 SDK 会根据主播上行网络的好坏决定视频的码率。

- **autoAdjustStrategy**
在开启码率自适应以后才能设置，否则设置是无效的，autoAdjustStrategy支持如下四种策略：

| 策略名称 | 策略说明 |
|---------|---------|
| AUTO_ADJUST_BITRATE_STRATEGY_1 | 整个直播过程中不断地探测网速并相应地进行调整，适合秀场直播等场景。 | 
| AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_1 | 在调整码率的同时相应的调整分辨率，以保持码率和分辨率之间的平衡 | 
| AUTO_ADJUST_BITRATE_STRATEGY_2 | 开播的最初半分钟里快速探测网速，之后会尽量少地进行调整，适合手游场景。 | 
| AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_2 | 在调整码率的同时相应的调整分辨率，以保持码率和分辨率之间的平衡 | 

- **videoBitrateMin** ： 最低码率，在开启码率自适应以后才能设置，否则设置是无效。
- **videoBitrateMax**： 最高码率，在开启码率自适应以后才能设置，否则设置是无效。
- **videoBitratePIN** ： 初始码率，videoBitrateMin <= videoBitratePIN <= videoBitrateMax。


## 背景说明
RTMP 推流质量对于观看体验非常关键，因为如果主播的推流质量不佳，那么所有观众看到的视频画面都是卡顿的，据统计，视频云客户群 80% 以上的直播间卡顿问题均是由于 RTMP 推流质量不佳导致的。

![](//mc.qcloudimg.com/static/img/4bf231da79ec8e45bdc4c16c927da47f/image.png)

在众多的推流质量问题中，主播的上行网络不给力引发的问题又是最主要的，上行带宽不足会导致音视频数据在主播端堆积并丢弃，从而使观众端看到的视频画面出现卡顿甚至长时间卡死。

所以，优化主播上行卡顿问题能够有效地提升推流质量，进而提升观看端的质量，尤其在国内运营商普遍限制上行带宽的情况下。

但是网络问题不随人的意志为转移，主播家里买的 4Mbps 宽带套餐，不可能因为主播装一个 App 就让其变成 8Mbps，因此，我们只能采用顺势而为的做法 —— **主动适应上行网络的情况**。


## 可选方案
1.7.0 版本开始，RTMP SDK 提供了针对三种场景的推荐方案：

### 1. 秀场场景
- **场景特点**
秀场模式的分辨率一般采用  360\*640 的分辨率， 码率上相应的采用 800kbps ，该模式下我们一般更关注画面清晰度和声音流畅度。如果主播的网络遭遇波动，主动降低画质来确保流畅性未必是我们追求的效果。

 因为秀场模式的码率本来就不高，这个时候压低码率的收益非常有限，码率降得少了没什么实质性改善，码率降得多了，就必然会引入区域性的马赛克，同时会大幅牺牲画面色彩的丰富度。

- **流控方案**
针对上述场景特点，我们**推荐不要做流控**，当主播的网络遭遇波动时，RTMP SDK 会通过 **PUSH_WARNING_NET_BUSY** 事件通知给您的App。这个时候建议您通过 UI 上的提示，提醒一下主播自己现在接入的WiFi不太给力，是不是考虑坐的离路由器近一点？
```
TXLivePushConfig* _config;
_config.videoBitratePIN	  = 700;  // 700kbps
_config.enableAutoBitrate = NO;   //固定码率推流
_config.videoResolution   = VIDEO_RESOLUTION_TYPE_360_640;//设置推流分辨率
```

### 2. 手游直播
- **场景特点**
跟秀场模式不同，手游直播场景下的分辨率和码率都比较高，比如 540p 甚至 720p 的分辨率是非常常见的，码率也一般在 1.5Mbps 以上，有些画面变化幅度比较大的游戏（比如 TempleRun）的甚至要2.5Mbps以上的上行带宽才能扛得住。

 于此同时，手游直播的主播一般都更加职业和专注，倾向于会选择网络较好的场景进行长时间的直播，期间网络波动的情况更多的是偶发性的临时波动。

- **流控方案**
针对上述场景特点，我们推荐采用 **AUTO_ADJUST_BITRATE_STRATEGY_2** 策略自动调整码率，该方案的特点是快速探测，快速调整，比较适合大码率的手游直播场景。
```
TXLivePushConfig* _config;
_config.videoBitrateMin   = 500;//动态调整的最小码率
_config.videoBitrateMax   = 1000;//动态调整的最大码率
_config.videoBitratePIN   = 800;//刚开始进入的默认码率
_config.enableAutoBitrate = YES;//是否开启动态调整码率
_config.videoResolution   = VIDEO_RESOLUTION_TYPE_360_640;//默认分辨率 
_config.autoAdjustStrategy= AUTO_ADJUST_BITRATE_STRATEGY_2;
```

- **进阶应用**
每一数值的码率都有最适合的分辨率与之搭配，比如 600kbps 的码率配合 360p 的分辨率，不管是颜色还是清晰度都是挺不错的，但如果 600kbps 的码率要配合 720p 的分辨率，画面就会大大缩水，这是由于视频编码率通常要牺牲更多的画质来换取更高的分辨率。

 基于这个原因，在 720p 的分辨率场景下，如果简单的将码率从 1.5Mbps 降低到 500kbps，后果就是运动画面下的(720p - 500kbps) 的马赛克要远多于(360p - 500kbps) 。

 所以，对于高清场景的游戏推流，我们更推荐采用 **AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_2** ，它会在降低码率的同时，相应的调整分辨率，以保持码率和分辨率之间的最佳平衡点。
 ```
 TXLivePushConfig* _config;
 _config.videoBitrateMin      = 800;//动态调整的最小码率
 _config.videoBitrateMax      = 3000;//动态调整的最大码率
 _config.videoBitratePIN      = 1800;//刚开始进入的默认码率
 _config.enableAutoBitrate    = YES;//是否开启动态调整码率
 _config.videoResolution      = VIDEO_RESOLUTION_TYPE_720_1280;//默认分辨率 
_ config.autoAdjustStrategy  = AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_2;
```
 
 
### 3. 移动场景
- **场景特点**
移动场景是个很宽泛的概念，我们团队将带宽不稳定的场景统称为移动场景，该场景下，主播的上行网络会经常发生变动，这一段时间可能是1Mbps， 下一段时间可能就变成 300kbps了。

- **流控方案**
针对这种场景，我们推荐采用 **AUTO_ADJUST_BITRATE_STRATEGY_1**，该策略模式下会尽量让带宽跟着网络情况持续做适应性调整。带来的收益就是在带宽不稳定的情况下推流质量会灵活应对，当然，这也有代价，那就是当网络稳定的情况下，推流码率也会“很不安分”，相比于固定码率会带来更多的波动。
 ```
 TXLivePushConfig* _config;
 _config.videoBitrateMin   = 500;//动态调整的最小码率
 _config.videoBitrateMax   = 1000;//动态调整的最大码率
 _config.videoBitratePIN   = 800;//刚开始进入的默认码率
 _config.enableAutoBitrate = YES;//是否开启动态调整码率
 _config.videoResolution   = VIDEO_RESOLUTION_TYPE_360_640;//默认分辨率 
 _config.autoAdjustStrategy= AUTO_ADJUST_BITRATE_STRATEGY_1;
```

- **进阶应用**
同样的，**AUTO_ADJUST_BITRATE_STRATEGY_1** 也有一个进阶版本 **AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_1**，后者会根据当前码率选择最佳分辨率，适合初始分辨率比较高的场景。
 ```
 TXLivePushConfig* _config;
 _config.videoBitrateMin   = 800;//动态调整的最小码率
 _config.videoBitrateMax   = 3000;//动态调整的最大码率
 _config.videoBitratePIN   = 1800;//刚开始进入的默认码率
 _config.enableAutoBitrate = YES;//是否开启动态调整码率
 _config.videoResolution   = VIDEO_RESOLUTION_TYPE_720_1280;//默认分辨率 
 _config.autoAdjustStrategy= AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_2;
 ```




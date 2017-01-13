

针对上述场景特点，我们**推荐不要做流控**，当主播的网络遭遇波动时，RTMP SDK 会通过 **PUSH_WARNING_NET_BUSY** 事件通知给您的App。这个时候建议您通过 UI 上的提示，提醒一下主播自己现在接入的WiFi不太给力，是不是考虑坐的离路由器近一点？
_config.videoResolution   = VIDEO_RESOLUTION_TYPE_360_640;//设置推流分辨率

- **流控方案**
_config.videoResolution   = VIDEO_RESOLUTION_TYPE_360_640;//默认分辨率 
 _config.videoResolution      = VIDEO_RESOLUTION_TYPE_720_1280;//默认分辨率 
_ config.autoAdjustStrategy  = AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_2;
 _config.enableAutoBitrate = YES;//是否开启动态调整码率
 _config.videoResolution   = VIDEO_RESOLUTION_TYPE_720_1280;//默认分辨率 
 _config.autoAdjustStrategy= AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_2;

## 简介

SDK 的各项监控指标可以从 TXLivePushListener 和 TXLivePlayListener 的回调中获取。

## TXLivePushListener
 
### 1. 如何获取推流的状态数据？
TXLivePushListener 的 [onNetStatus](https://cloud.tencent.com/document/product/454/34757#onnetstatus) 回调，会每隔1秒 - 2秒会将 SDK 内部的状态指标同步出来，其中如下指标比较有意义：
![](https://main.qcloudimg.com/raw/fcd384fc96c9f1144df513cf7231641e.png)

|  推流状态                 |  含义说明                  |
| :------------------------  |  :------------------------ |
| NET_STATUS_CPU_USAGE     |当前进程的 CPU 使用率和本机总体的 CPU 使用率。|
| NET_STATUS_VIDEO_WIDTH  |当前视频的宽度，单位：像素值。    |
| NET_STATUS_VIDEO_HEIGHT|当前视频的高度，单位：像素值。    |
|    NET_STATUS_NET_SPEED     | 当前的发送速度，单位：kbps。|
|    NET_STATUS_VIDEO_BITRATE | 当前视频编码器输出的比特率，也就是编码器每秒生产了多少视频数据，单位：kbps。|
|    NET_STATUS_AUDIO_BITRATE | 当前音频编码器输出的比特率，也就是编码器每秒生产了多少音频数据，单位：kbps。|
|    NET_STATUS_VIDEO_FPS     | 当前视频帧率，也就是视频编码器每条生产了多少帧画面。|
|    NET_STATUS_VIDEO_CACHE    | 视频数据堆积情况，这个数字超过个位数，即说明当前上行带宽不足以消费掉已经生产的视频数据。|
|    NET_STATUS_AUDIO_CACHE    | 音频数据堆积情况，这个数字超过个位数，即说明当前上行带宽不足以消费掉已经生产的音频数据。|
|    NET_STATUS_VIDEO_DROP  |视频全局丢帧次数，为了避免延迟持续恶性堆积，SDK 在数据积压超过警戒线以后会主动丢帧，丢帧次数越多，说明网络问题越严重。|
|    NET_STATUS_AUDIO_DROP  |音频全局丢包次数，为了避免延迟持续恶性堆积，SDK 在数据积压超过警戒线以后会主动丢包，丢包次数越多，说明网络问题越严重。|
| NET_STATUS_SERVER_IP     | 连接的推流服务器的 IP。 |

### 2. 哪些状态指标有参考价值？

-  **BITRATE vs NET_SPEED**
BITRATE( = VIDEO_BITRATE + AUDIO_BITRATE ) 指的是编码器每秒产生了多少音视频数据要推出去，NET_SPEED 指的是每秒钟实际推出了多少数据。
 - 如果 BITRATE == NET_SPEED 的情况是常态，则推流质量会非常良好。
 - 如果 BITRATE >= NET_SPEED ，且这种情况的持续时间比较长，音视频数据会堆积在主播的手机上撑大 CACHE_SIZE 并最终被 SDK 丢弃形成 DROP_CNT 。

- **NET_STATUS_VIDEO_CACHE、 NET_STATUS_AUDIO_CACHE、NET_STATUS_VIDEO_DROP、NET_STATUS_AUDIO_DROP**
如果主播当前网络的上传速度不佳，就很容易出现 BITRATE ≥ NET_SPEED 的情况，此时音视频数据会在主播的手机上积压起来。如果积压的数据超过警戒阈值，SDK 会主动丢弃一些音视频数据。
 - NET_STATUS_VIDEO_CACHE 表示视频积压的帧数。
 - NET_STATUS_AUDIO_CACHE 表示音频积压的包数。
 - NET_STATUS_VIDEO_DROP 表示累计丢弃的视频帧数。
 - NET_STATUS_AUDIO_DROP 表示累计丢弃的音频包数。
 
![](https://main.qcloudimg.com/raw/8b603b473df5f4c75ede38de9f4161de.png)

- **CPU_USAGE**
 - 如果**系统 CPU 使用率**超过80%，音视频编码的稳定性会受到影响，可能导致画面和声音的随机卡顿。
 - 如果**系统 CPU 使用率**经常100%，会导致视频编码帧率不足，音频编码跟不上，必然导致画面和声音的严重卡顿。

>?很多客户会遇到的一个问题： App 在线下测试时性能表现极佳，但在 App 外发上线后，前排房间里的互动消息的滚屏和刷新会产生极大的 CPU 消耗导致直播画面卡顿严重。

- **SERVER_IP**
如果主播到 SERVER_IP 给出的 IP 地址的 ping 值很高（如超过500ms），那么推流质量一定无法保障。**就近接入**是我们腾讯云应该做好的事情，如您发现有这样的案例，请反馈给我们，我们的运维团队会持续调整和优化。

### 3. 如何看懂腾讯云推流图表？ 
在 [直播控制台 - 质量监控](https://console.cloud.tencent.com/live/livesdk) 您可以看到您所属账户里的直播间情况，以及每个直播间的推流质量数据：

- **主播端-应发速率-实发速率曲线图**
蓝色曲线代表 BITRATE 的统计曲线，即 SDK 产生的音视频数据，绿色曲线代表实际网络发出去多少。两条线重合度越高表示推流质量越好。

![](https://main.qcloudimg.com/raw/d2ad188df4ca9ca6bb192a74db9cb95d.png)

- **主播端-音视频数据堆积情况**
 + 如果曲线始终贴着0刻度线走，说明整个推流过程非常顺畅，一点都没有堆积。
 + 如果出现大于0的部分，说明当时有网络波动导致数据积压，有可能在播放端产生轻微卡顿和音画不同步的现象。
 + 如果堆积超出红色警戒线，说明已经产生了丢包，必然会在播放端产生卡顿和音画不同步的现象。

![](https://main.qcloudimg.com/raw/ce31d7b603a9a9719340c16b5e1b9471.png)

- **云端-应收视频时长-实收视频时长曲线**
这里是腾讯云服务端的统计图表，如果您不是使用腾讯云 SDK 推流，那么您将只能看到这个图表，前面两个（数据源来自 SDK）是看不到的。蓝绿两条线重合度越高，说明推流质量越好。

![](https://main.qcloudimg.com/raw/c24863a60618db266bb6eaaab6da1833.png)

## TXLivePlayListener

### 1. 如何获取播放的状态数据？
TXLivePlayListener 的 [onNetStatus](https://cloud.tencent.com/document/product/454/34773#onnetstatus) 回调，会每隔1秒 - 2秒会将 SDK 内部的状态指标同步出来，其中如下指标比较有意义：
![](https://main.qcloudimg.com/raw/7fca407dc1d3a6839fc69a850684caf0.png)

|  播放状态                 |  含义说明                  |
| :------------------------  |  :------------------------ |
| NET_STATUS_CPU_USAGE     | 当前瞬时 CPU 使用率。 |
| NET_STATUS_VIDEO_WIDTH  | 视频分辨率 - 宽。 |
| NET_STATUS_VIDEO_HEIGHT| 视频分辨率 - 高。 |
|    NET_STATUS_NET_SPEED     | 当前的网络的下载速度。 |
|    NET_STATUS_VIDEO_FPS     | 当前流媒体的视频帧率。    |
|    NET_STATUS_VIDEO_BITRATE | 当前流媒体的视频码率，单位：kbps。|
|    NET_STATUS_AUDIO_BITRATE | 当前流媒体的音频码率，单位：kbps。|
|    NET_STATUS_VIDEO_CACHE    | 视频播放缓冲区（jitterbuffer）大小，缓冲区越小越难以抵抗卡顿。|
|    NET_STATUS_AUDIO_CACHE    | 音频播放缓冲区（jitterbuffer）大小，缓冲区越小越难以抵抗卡顿。|
| NET_STATUS_SERVER_IP | 当前连接的服务器 IP。 |

### 2. 哪些状态指标有参考价值？
- **NET_STATUS_VIDEO_CACHE 、NET_STATUS_AUDIO_CACHE**
这两个指标用于衡量播放缓冲区（jitterbuffer）的大小：
 - 缓冲区越大，播放的延迟越高，但网络有波动时越不容易卡顿。
 - 缓冲区越小，播放的延迟越低，但下载速度稍有波动就可能引发卡顿。

TXLivePlayer 有三种模式用于控制播放缓冲区的大小，设置方法可以参考[【基础功能 - 直播拉流】](https://cloud.tencent.com/document/product/454/34920)的对接文档。

| 播放模式 | 卡顿率 | 延迟 | 使用场景 | 原理简述 |
|---------|---------|---------|---------|---------|
| 极速模式 | 较高 | 2s - 3s | 美女秀场 | 尽可能保证较低的播放缓冲区，进而减少延迟，适合1Mbps左右的低码率场景。|
| 流畅模式 | 较低 | >= 5s | 游戏直播 | 确保随时都有较大的播放缓冲区，通过牺牲延迟来应对大码率（2M左右）下的网络波动的影响。 |
| 自动模式 | 自适应 | 2s - 8s | 泛场景 | 缓冲区大小自动调节：网络越好，延迟越低；网络越差，延迟越高。 |




## What is "Instant Broadcasting"?

**Instant Broadcasting** is to make the time length between the start of video playback and the moment the first frame is displayed as short as possible to prevent viewers from waiting long. 
![](//mc.qcloudimg.com/static/img/9a1541e3d8f6796e8025b571d5267c7c/image.png)

This depends on optimized cloud services and player. In an LVB, a combination of Tencent's RTMP SDK and video cloud service allows you to open the first frame at a speed as high as about **200ms**, and even open it instantly if you has a good downstream bandwidth.

## How to Achieve Instant Broadcasting?
### Apps
To achieve instant broadcasting, you can use FLV playback protocol, which has a more stable structure than RTMP protocol, and [RTMP SDK](https://cloud.tencent.com/document/product/454/7873), which can help avoid:

**"Side effect" of instant broadcasting**.

>Instant broadcasting relies on the intelligent video buffering on cloud, which comes with a side effect - delay. Therefore, a good player should have both the ability to support instant broadcasting and an excellent delay control. Trading off delay control for instant broadcasting doesn't pay in some LVB scenarios with a high requirement for interactions, such as ShowTime LVB.
>
>Tencent Cloud RTMP SDK differentiates itself from others for its capability of allowing both instant broadcasting and a good delay control. 

### PC browsers
The video playback kernels on PC browsers usually use FLASH control (Chrome also supports MSE, but it has no obvious advantage over FLASH). FLASH player adopts a rigid **forced buffering** strategy, providing little room for optimization of video loading speed, which is unlikely to be kept within 1 second. This fact can be found on many video websites and LVB platforms when you're using a PC browser.

### Mobile browsers
Safari has a good support for HLS (m3u8) and even uses iPhone's hardware decoding chip to facilitate video playback. With DNS buffer, it can achieve an acceptable video loading speed, but this is only limited to iOS platform. The performance on Android depends on the player implementation on system browser, QQ browser or UC browser.


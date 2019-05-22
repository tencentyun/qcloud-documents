
## Background
RTMP push quality is crucial to the viewing experience. A poor push quality at VJ end can cause stutters at all the viewer ends. According to the statistics, over 80% of LVB stutters among Video Cloud customers are caused by a poor RTMP push quality.

Among the push quality issues, the biggest issue is caused by unsatisfactory upstream network at VJ end. Insufficient upstream bandwidth can make audio/video data build up and then be dropped at VJ end, thus leading to the stutters or even long freezing of video images at viewer end.

![](//mc.qcloudimg.com/static/img/3c10b3a268b4807a184b767b1cc4363c/image.png)

Therefore, dealing with the stutters of upstream network at VJ end can effectively improve the push quality, thus delivering a better viewing experience, especially in the domestic environment where upstream bandwidth is restricted by ISPs.

But network condition does not hinge on our will. If a VJ uses a 4-Mbps bandwidth plan at home, it is impossible to change it to 8Mbps just because the VJ installs a new App. Therefore, we can choose to**actively adapt to the upstream network**.

## Quick Interfacing
You can enable Qos traffic control by using the parameters of API setVideoQuality of TXLivePusher so that the SDK controls the video clarity depending on the the upstream network condition at VJ end.

![](//mc.qcloudimg.com/static/img/c52dc506047402db04ac285fa7520e65/image.png)

- **quality**
Six levels are provided in the SDK based on our experience in serving most of customers. STANDARD, HIGH, and SUPER apply to LVB; MAIN_PUBLISHER and SUB_PUBLISHER apply to primary and secondary images in joint broadcasting; and VIDEOCHAT is used for real-time audio and video.

- **adjustBitrate**
Whether to enable QoS traffic control. If it is enabled, the SDK automatically adjusts video bitrate based on the upstream network condition at VJ end. The disadvantage is that blurred screens and many mosaics may occur in case of a poor network on the VJ end.

- **adjustResolution**
Whether to allow dynamic resolution. If it is enabled, the SDK selects a resolution appropriate to the current video bitrate for a higher clarity. The disadvantage is that the files recorded from live streams with a dynamic resolution have compatibility issues on many players.

![](//mc.qcloudimg.com/static/img/07deb1e7e01daba3227175a0fcec1fa5/image.png)

## Fine Tuning
If the default parameters in setVideoQuality do not meet your needs, you can customize parameters via TXLivePushConfig:

- **enableAutoBitrate**
Whether to enable the self-adaption of bitrate, or Qos traffic control. If it is enabled, the SDK controls the video clarity based on the upstream network condition at VJ end.

- **autoAdjustStrategy**
Available only if the self-adaption of bitrate is enabled. autoAdjustStrategy supports the following four strategies:

| Strategy Name | Description |
|---------|---------|
| AUTO_ADJUST_BITRATE_STRATEGY_1 | Constantly monitor the network speed and adapt the bitrate to the network condition during LVB. It is suitable for live shows. | 
| AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_1 | Adjust the bitrate while adjusting the resolution accordingly to keep a balance between bitrate and resolution. | 
| AUTO_ADJUST_BITRATE_STRATEGY_2 | Quickly test the network speed within the first half minute of playback, then make adjustments to the minimum extent. It is suitable for mobile games. | 
| AUTO_ADJUST_BITRATE_RESOLUTION_STRATEGY_2 | Adjust the bitrate while adjusting the resolution accordingly to keep a balance between bitrate and resolution. | 

- **videoBitrateMin**: The minimum bitrate, which is available only after the self-adaption of bitrate is enabled.
- **videoBitrateMax**: The maximum bitrate, which is available only after the self-adaption of bitrate is enabled.
- **videoBitratePIN**: The original bitrate. videoBitrateMin <= videoBitratePIN <= videoBitrateMax.



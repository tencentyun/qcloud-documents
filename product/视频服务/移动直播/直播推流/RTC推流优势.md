为了提高在弱网下的推流效果，移动直播 SDK 在传统的 RTMP 协议推流的基础上增加了 RTC 协议的推流方式。本文档主要介绍不同档位弱网条件下两种协议的数据对比。效果可以参考下面的视频：
<video width="610" controls><source src="https://liteav.sdk.qcloud.com/doc/res/mlvb/picture/RTC_vs_RTMP.MP4">
  对不起，您的浏览器暂时不支持视频预览。
</video>
>? 推流教程请参见 [摄像头推流](https://cloud.tencent.com/document/product/454/56591)。

## 无损及弱网环境下的效果质量

### 测试场景
主播推流，观众通过 CDN 观看。在主播端进行各种弱网限制，观察观众播放的效果质量。本文档弱网环境只针对上行，下行网络为无损状态。

### 参数配置
为了避免受不同源的影响，使用 RTMP 和 RTC 推流时都固定使用 [V2TXLivePusher](https://cloud.tencent.com/document/product/454/56605) 推同一个本地视频。
视频参数：

| 参数类型 | 配置信息|
|---------|---------|
| 分辨率	| 720 × 1280 | 
| 码率	| 1800 kbps | 
| 帧率	| 15 | 

### 几种弱网场景下关键指标的对比
- **帧率**
![](https://qcloudimg.tencent-cloud.cn/raw/62878cd6195e3d9169362db59b8e270a.png)
>? 具体参数含义请参见 [附录：网络参数说明](#appendix1)。
- **卡顿率**
![](https://qcloudimg.tencent-cloud.cn/raw/2d9a13ce5a6b336844378d55122d52c4.png)
>? 具体参数含义请参见 [附录：网络参数说明](#appendix1)。

[](id:appendix1)
## 附录：网络参数说明
| 参数 | 说明 |
|---------|---------|
| 帧率 | 每秒钟渲染帧数 |
| 丢包率 | 50% 代表发送了10个数据包中会丢失5个 |
| 时延 | 200ms 时延代表 SDK 发送的包，会经过 200ms 后才被网络发送出去 |
| 限速 | 800kbps 代表每秒钟最多发送 800kb 的数据 |
| 卡顿率 | 渲染间隔大于 200ms 表示卡顿，卡顿率等于卡顿时间总和除以总播放时长 |

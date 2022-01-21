为了提高在弱网下的推流效果，移动直播 SDK 在传统的 RTMP 协议推流的基础上增加了 RTC（Real-Time Communication） 协议的推流方式。本文档主要介绍不同档位弱网条件下两种协议的数据对比。效果可以参考下面的视频：
<video width="610" controls><source src="https://sdk-liteav-1252463788.cos.ap-hongkong.myqcloud.com/doc/res/mlvb/picture/RTC_vs_RTMP.MP4">
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
| 分辨率	| 720 × 1080 | 
| 码率	| 1200Kbps | 
| 帧率	| 15 | 

### 极限网络抗性测试数据
极限网络抗性测试指的是在各种网络损伤环境下，测试 SDK 所能承受的最大网络损伤。

| 场景 | RTC | RTMP |
|---------|---------|---------|
| 可承受的最大丢包率 [Loss] | 55% | 30% |
| 可承受的最大网络延迟 [Delay] | 8000ms | 2000ms |
| 可流畅播放的最低带宽要求 | 500kbps | 1200kbps |

>? 具体损失指标及含义请参见 [附录1：音视频质量指标说明](#appendix1)。

### 几种弱网场景下关键指标的对比
- **帧率**
![](https://qcloudimg.tencent-cloud.cn/raw/c8c995ee6875a89e45904df69dde0de5.png)
- **卡顿率**
![](https://qcloudimg.tencent-cloud.cn/raw/7cd039799d9a9413ca638052da095f51.png)
>? 卡顿率由测试 Demo 统计得出，渲染间隔大于200毫秒视为卡顿，所有卡顿时间的总和除以总拉流时长则为卡顿率。

[](id:appendix1)
## 附录1：音视频网络损伤指标说明
| 网络损伤指标 | 说明 | 示例 |
|---------|---------|---------|
| Loss | 网络丢包 | 50% Loss 代表10个包中会丢5个包 |
| Delay | 代表延迟 | 200ms Delay 也就是 SDK 发送的包，会经过200ms后才被网络发送出去 |

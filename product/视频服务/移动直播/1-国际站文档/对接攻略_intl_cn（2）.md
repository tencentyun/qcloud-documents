## 整体流程
![](//mc.qcloudimg.com/static/img/2bbbdbba7baec530e40e05f15ea52fc0/image.gif)
1. 主播 A 正常推流直播，直播码为 streamA
2. 主播 B 正常推流直播，直播码为 streamB
3. 主播 B 向主播 A 请求连麦，并带上自己的推流地址 streamB
4. 主播 A 如果同意连麦，向主播 B 回应一下，于此同时，主播 A 拉取 streamB 的流进行播放（播放器设置为 PLAY_TYPE_LIVE_RTMP_ACC）
5. 主播 B 拉取 streamA 的流进行播放（播放器设置为 PLAY_TYPE_LIVE_RTMP_ACC）
6. 主播 A (或主播B) 根据需要通知服务器做一下混流，这样 CDN 的观众就能看到大小视频叠加的画面了。

## 整体对接
### 步骤一：主播 A 推流
主播 A 从您的业务后台获取推流防盗链地址 streamA，之后可以用 [TXLivePusher](https://cloud.tencent.com/document/product/454/7879) 进行推流。

在连麦开始前，推流的 setVideoQuality 要切换为 VIDEO_QUALITY_LINKMIC_MAIN_PUBLISHER。该模式中会开启回声抑制（AEC），避免连麦中有回音。

> setVideoQuality 支持推流中直接改变场景模式。

### 步骤二：主播 B 推流
主播 B 从您的业务后台获取推流防盗链地址 streamB，之后可以用 [TXLivePusher](https://cloud.tencent.com/document/product/454/7879) 进行推流。

在连麦开始前，推流的 setVideoQuality 要切换为 VIDEO_QUALITY_LINKMIC_SUB_PUBLISHER。该模式中会开启回声抑制（AEC），避免连麦中有回音。

> SUB_PUBLISHER 的分辨率和码率都要低于 MAIN_PUBLISHER，毕竟那么小的窗口，用很高的分辨率是浪费的。

### 步骤三：发起连麦请求
主播 B 向主播 A 发起连麦请求，请求可以由您的业务服务器中转，也可以使用腾讯云的 IM 云通讯解决方案。请求中要带上 主播 B 的推流直播码，否则主播 A 无法去播放主播 B 的视频流。

> 小直播源码中使用了腾讯云的  IM 云通讯解决方案实现了连麦请求的握手。

### 步骤四：主播 A 播放 streamB
主播 A 如果接受主播 B 的连麦请求，可以进行应答，这样主播 B 就知道连麦请求是否已经被同意了。

主播 A 此时需要使用 [TXLivePlayer](https://cloud.tencent.com/document/product/454/7880) 播放 streamB 的 **低延时** 地址，<font color='red'>特别注意</font>，这里不能播放普通的 CDN 观看地址。区别在于前者的延迟一般在 500ms 以内，而 CDN 的延迟一般在 2s 以上，CDN 地址只能给普通观众观看，不能用于主播之间的连麦。

所以，要得到 500ms 左右的低延迟播放效果，需要：

- **4.1 给播放地址加 [防盗链签名](https://cloud.tencent.com/document/product/454/9875)**
低延时链路使用的是腾讯云核心机房的BGP资源，需要有带防盗链签名的 rtmp-liveplay 地址才能访问，所以主播 A 和 主播 B 都要给播放地址加上防盗链签名（txTime 和 txSecret）才能低延迟播放，如下是一个正确的低延迟播放地址：
<table><tbody valign="middle"><tr><td height='80px'>rtmp://8888.liveplay.myqcloud.com/live/8888_streamB?bizid=8888&txSecret=xxxxx&txTime=5C2A3CFF</td></tr></tbody></table>

- **4.2 使用  [TXLivePlayer](https://cloud.tencent.com/document/product/454/7880) 的 PLAY_TYPE_LIVE_RTMP_ACC 播放模式**
LIVE_RTMP_ACC 的模式会开启播放器自带的精准延迟控制模块，该模式下的缓冲处理和音画同步技术相比于普通直播要求高很多。

### 步骤五：主播 B 播放 streamA
主播 B 在接到主播 A 同意连麦的请求后，可以开始播放 streamA 的 **低延时** 地址，同样需要：
- 给播放地址加上防盗链签名

- 使用  [TXLivePlayer](https://cloud.tencent.com/document/product/454/7880) 播放，并设置为 PLAY_TYPE_LIVE_RTMP_ACC 播放模式。

### 步骤六：云端混流
低延时链路使用的是腾讯云核心机房的BGP资源，如果用于普通观众观看，延迟是挺低的，但是费用也挺高的。所以，普通观众观看还是要使用普通的 CDN 地址。

腾讯云的云端混流技术，在于将一个或者多个（目前暂时支持到1+3）小主播的视频画面叠加到大主播的视频流上（包括音频混音），基于这种方案，您可以让普通观众在不改造播放器的情况下就能观看连麦直播。

具体使用方案可以参考 [云端混流 API](https://cloud.tencent.com/document/product/454/9850)。

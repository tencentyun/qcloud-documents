## 内容介绍

腾讯云实时音视频（TRTC）服务同时支持视频通话场景及直播两种场景。对于直播场景，您有两种选择：
1. 加入 TRTC 音视频房间进行观看，延迟更低、流畅性更好。但我们不推荐，因为该方案有两个明显的短板：
 - 按时长计费的价格方案较 CDN 直播服务要贵不少。
 - TRTC 单个房间的并发人数限制为 1000 人以内。

2. 使用 TRTC 的**旁路直播**功能，将 TRTC 音视频房间里的音视频流（经过混流转码）转推到腾讯云直播 CDN 上，从而获得低成本和高并发的观看能力。优势：
 - 带宽成本相对较低。
 - 支持超过1000人的大房间应用场景。

## 支持的平台

| iOS | Android | Mac OS | Windows | 微信小程序 | Chrome浏览器|
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|     ✔  |    ✔    |    ✔   |    ✔    |    ✖     |   ✖     |

## 如何开启旁路服务
在腾讯云实时音视频 [控制台](https://console.cloud.tencent.com/rav) 的**功能配置**页面里可以开启自动旁路推，开启此功能的前提是需要先开通腾讯云直播服务，可以在云直播 [控制台](https://console.cloud.tencent.com/live) 开通。
![](https://main.qcloudimg.com/raw/91672da223a6eb7c24e8c9891018ead1.png)

## 如何获取播放地址

假如一个 TRTC 房间里有三个用户，分别是 userA，userB 和 userC，那么现在一共有四路播放地址可以观看，分别是：
- userA 的播放地址：开启旁路服务后默认开启。
- userB 的播放地址：开启旁路服务后默认开启。
- userC 的播放地址：开启旁路服务后默认开启。
- ABC按照您指定的排版方式混合后的播放地址：需要您通过 `startCloudMixTranscoding` 和 `startPublishCDNStream` 接口手动开启。
![](https://main.qcloudimg.com/raw/96dc6cf35659f03d8ec9739f1fde2c5a.png)

### 独立画面的默认地址
房间里的每一路画面都配备一路对应的播放地址，画面内容相互独立，各路播放地址的计算规则如下：

播放地址的拼接规则如下：
```
rtmp://[bizid].liveplay.myqcloud.com/live/[bizid]_[streamid]
http://[bizid].liveplay.myqcloud.com/live/[bizid]_[streamid].flv
http://[bizid].liveplay.myqcloud.com/live/[bizid]_[streamid].m3u8
```
其中，streamid = MD5(房间号_用户名_流类型)
bizid： 的获取见文档前半部分
流类型：摄像头画面的流类型是 main，屏幕分享的流类型是 aux (有个例外，Web端目前屏幕分享的流类型也是 main)

假如：bizid = 8888， 房间号 = 12345，用户名 = rexchang， 用户当前使用了摄像头
那么：streamid = MD5(12345_rexchang_main) = 185e1a7b26423ca4470a99fa9d9b4b9b

所以，rexchang 这一路的腾讯云 CDN 观看地址是：
```
rtmp://8888.liveplay.myqcloud.com/live/8888_185e1a7b26423ca4470a99fa9d9b4b9b
http://8888.liveplay.myqcloud.com/live/8888_185e1a7b26423ca4470a99fa9d9b4b9b.flv
http://8888.liveplay.myqcloud.com/live/8888_185e1a7b26423ca4470a99fa9d9b4b9b.m3u8
```

### 混合画面的转推和播放

由于多路画面的混合需要您指定画面间的叠加方式，所以混合画面的播放地址并没有默认的，需要您按照如下三步进行获取。

#### step1：调用startPublishCDNStream进行转推

通过 TRTCCloud 的 `startPublishCDNStream` 可以将当前房间中的音视频流，转推到其参数 `TRTCPublishCDNParam` 指定的 url 上，该参数有如下字段需要您填写：

- **appid 和 bizid**
您可以在腾讯云实时音视频 [控制台](https://console.cloud.tencent.com/rav) 的**账号信息**页面看到这两个信息。
![](https://main.qcloudimg.com/raw/4bacb840b1ece10544f1f3414635fe7c.png)

 >! 如果您看到上述区域的数值为空，说明您还没有开通直播服务，在腾讯云直播[控制台](https://console.cloud.tencent.com/live)开通直播服务即可。

- **url**
RTMP 推流 URL 的获取，各家云服务商都有各自的方案，腾讯云的方案非常简单，您可以参考文档：[“快速获得推流地址”](https://cloud.tencent.com/document/product/267/7977) 或 [“后台自动拼装”](https://cloud.tencent.com/document/product/267/13457) 了解详情。

- **enableTranscoding**
设置为 **true** 才能开启多路画面的混合转码，否则只能转推当前用户的单路画面。

#### step2：调用 startCloudMixTranscoding 进行混流
如果开启混流转码，您需要调用 TRTCCloud 的 `startCloudMixTranscoding` 对各路画面的摆放位置以及最终的画面质量进行配置，这里的配置方法需要您参考文档：[云端混流转码](https://cloud.tencent.com/document/product/647/16827)。

 >! `startCloudMixTranscoding` 并不是在终端进行混流，而是将混流配置传输到云端，由云端进行混流和转码，所以不用担心这里的性能问题。

#### step3：拼装混合画面的播放地址
step1 中填写在 TRTCPublishCDNParam 里的 url 参数是推流用的 rtmp 推流 url，也就是只能用来推流不能用来播放，不过每一个推流url都有其对应的播放url。以腾讯云为例，您可以参考文档 [“直播码模式获取播放地址”](https://cloud.tencent.com/document/product/267/13484) 或 [“业务后台生成播放地址”](https://cloud.tencent.com/document/product/267/13485)，从而了解如何获取对应的播放URL。


## 如何播放

在各种播放地址中，我们推荐以 `http` 为前缀且以 `.flv` 为后缀的 **http-flv** 地址，该地址的播放具有时延低、秒开效果好且非常稳定可靠的特点。

播放器推荐使用已经打包在 TRTC SDK 里的 TXLivePlayer 播放器，该播放器的参考文档为：
- [TXLivePlayer(iOS)](https://cloud.tencent.com/document/product/454/7880)
- [TXLivePlayer(Android)](https://cloud.tencent.com/document/product/454/7886)
- [TXLivePlayer(Windows)](https://cloud.tencent.com/document/product/454/13676#.E6.92.AD.E6.94.BE.E5.8A.9F.E8.83.BD)

## 常见问题
- **1. 为什么房间里只有一个人的时候画面又卡又模糊?**
请将 `enterRoom` 中 TRTCAppScene 参数指定为 **TRTCAppSceneLIVE**，VideoCall 模式针对视频通话做了优化，所以在房间中只有一个用户时，画面会显得即卡又模糊。
 
- **2. 能不能转推到非腾讯云的CDN地址？**
支持，但目前尚需要手工配置白名单开启，如果需要开启此功能，请通过 400 电话或者工单联系我们。

- **3. 此服务是否收费？**
旁路推流到腾讯云直播CDN是不收取转推费用的，到其他云商CDN会收取一定的转推费用。





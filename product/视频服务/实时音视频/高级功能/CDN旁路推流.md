## 内容介绍
腾讯云实时音视频（TRTC）服务同时支持 **视频会议** 及 **在线直播** 两种场景：

#### 视频会议
所有人都可以直接加入 TRTC 房间进行观看，延迟更低、流畅性更好。但这种方案对于人数较多的直播场景并不适用，原因有二：
 - 按时长计费的价格方案较 CDN 直播服务要贵不少。
 - TRTC 单个房间的并发人数限制为 1000 人以内。

#### 在线直播
使用 TRTC 的**旁路直播**功能，将 TRTC 音视频房间里的音视频流（经过混流转码）转推到腾讯云直播 CDN 上，从而获得低成本和高并发的观看能力。优势：
- 带宽成本相对较低。
- 支持超过1000人的大房间应用场景。

本文主要介绍，如何使用 TRTCCloud 的 `startCloudMixTranscoding` 和 `startPublishCDNStream` 接口，实现多路画面混合并发布到 CDN 上，从而支持高并发低成本的直播需求。

## 支持的平台

| iOS | Android | Mac OS | Windows | 微信小程序 | Chrome浏览器|
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|     ✔  |    ✔    |    ✔   |    ✔    |    ✖     |   ✖     |

## 如何开启旁路服务
在腾讯云实时音视频 [控制台](https://console.cloud.tencent.com/rav) 的**功能配置**页面里可以开启自动旁路推，开启此功能的前提是需要先开通腾讯云直播服务，可以在云直播 [控制台](https://console.cloud.tencent.com/live) 开通。

![](https://main.qcloudimg.com/raw/91672da223a6eb7c24e8c9891018ead1.png)

## 如何获取播放地址

假如一个 TRTC 房间里有三个用户，分别是 userA，userB 和 userC，那么现在一共有四路播放地址可以观看，分别是：
- **userA** 的播放地址：开启旁路服务后默认开启，地址中只有 userA 的一路画面。

- **userB** 的播放地址：开启旁路服务后默认开启，地址中只有 userB 的一路画面。

- **userC** 的播放地址：开启旁路服务后默认开启，地址中只有 userC 的一路画面。

- **混合画面**：即将 userA、userB 和 userC 按照您指定的排版方式混合后的播放地址，非默认开启。

> ! 混合画面需要您通过 `startCloudMixTranscoding` 和 `startPublishCDNStream` 接口手动开启。

![](https://main.qcloudimg.com/raw/96dc6cf35659f03d8ec9739f1fde2c5a.png)

### 独立画面
房间里的每一路画面都配备一路对应的播放地址，其计算规则如下：
```
http://[bizid].liveplay.myqcloud.com/live/[bizid]_[streamid].flv
```
- streamid = MD5 (房间号\_用户名\_流类型)

- bizid： 一个直播服务相关的数字，您可以在腾讯云实时音视频 [控制台](https://console.cloud.tencent.com/rav) 的（账号信息>>直播信息）页面看到这两个信息。
![](https://main.qcloudimg.com/raw/4bacb840b1ece10544f1f3414635fe7c.png)

- 流类型：摄像头画面的流类型是 main，屏幕分享的流类型是 aux (有个例外，Web端目前屏幕分享的流类型也是 main)

```
假如，bizid = 8888， 房间号 = 12345，用户名 = userA， 用户当前使用了摄像头。

那么，streamid = MD5(12345_userA_main) = 8d0261436c375bb0dea901d86d7d70e8

所以，rexchang 这一路的腾讯云 CDN 观看地址（推荐 http-flv）是：

http://8888.liveplay.myqcloud.com/live/8888_8d0261436c375bb0dea901d86d7d70e8.flv
```

### 混合画面

由于多路画面的混合需要您指定画面间的叠加方式，所以混合画面并没有默认的播放地址，需要您按照如下两步进行获取。

#### step1: setMixTranscodingConfig() 多路画面混合成一路
如果开启混流转码，您需要调用 TRTCCloud 的 `startCloudMixTranscoding` 对各路画面的摆放位置以及最终的画面质量进行配置，这里的配置方法需要您参考文档：[云端混流转码](https://cloud.tencent.com/document/product/647/16827)。

> `setMixTranscodingConfig` 并不是在终端进行混流，而是将混流配置发送到云端，由云端进行混流和转码，所以不用担心这里的性能问题。

#### step2: startPublishCDNStream() 旁路转推到直播CDN

通过 TRTCCloud 的 `startPublishCDNStream` 可以将当前房间中的音视频流，转推到其参数 `TRTCPublishCDNParam` 指定的 url 上，该参数有如下字段需要您填写：

| 参数字段 | 参数说明 |
|:-------:|---------|
| appid | 您可以在腾讯云实时音视频 [控制台](https://console.cloud.tencent.com/rav) 的（账号信息>>直播信息）页面看到这两个信息。 |
| bizid | 您可以在腾讯云实时音视频 [控制台](https://console.cloud.tencent.com/rav) 的（账号信息>>直播信息）页面看到这两个信息。 |
| url | RTMP 推流 URL 的获取，各家云服务商都有各自的方案。腾讯云的方案非常简单：<br>您可以在云直播控制台中使用[地址生成器](https://console.cloud.tencent.com/live/livecodemanage)生成一个临时的推流URL，<br>也可以参考文档：[“如何自主拼装推流URL”](https://cloud.tencent.com/document/product/267/32720) 了解详情。 |

 >! 
 >1. 如果您看到 appid 和 bizid 数值为空，说明您还没有开通直播服务，在腾讯云直播 [控制台](https://console.cloud.tencent.com/live) 开通直播服务即可。
 >
 >2. 填写在 `TRTCPublishCDNParam` 里的 url 参数是推流 url （特点是以  rtmp:\\\\  打头），也就是只能用来推流不能用来播放，不过每一个推流url都有其对应的播放 url。以腾讯云为例，您可以参考文档 [“如何获取播放地址”](https://cloud.tencent.com/document/product/267/32733#.E5.A6.82.E4.BD.95.E8.8E.B7.E5.8F.96.E6.92.AD.E6.94.BE.E5.9C.B0.E5.9D.80) ，从而了解如何获取对应的播放URL。


## 如何播放

在各种播放地址中，我们推荐以 `http` 为前缀且以 `.flv` 为后缀的 **http-flv** 地址，该地址的播放具有时延低、秒开效果好且非常稳定可靠的特点。

播放器推荐使用已经打包在 TRTC SDK 里的 TXLivePlayer 播放器，该播放器的参考文档为：
- [TXLivePlayer(iOS)](https://cloud.tencent.com/document/product/454/7880)
- [TXLivePlayer(Android)](https://cloud.tencent.com/document/product/454/7886)
- [TXLivePlayer(Windows)](https://cloud.tencent.com/document/product/454/13676#.E6.92.AD.E6.94.BE.E5.8A.9F.E8.83.BD)

## 常见问题
- **1. 为什么房间里只有一个人的时候画面又卡又模糊?**
请将 `enterRoom` 中 TRTCAppScene 参数指定为 **TRTCAppSceneLIVE**，VideoCall 模式针对视频通话做了优化，所以在房间中只有一个用户时，画面会保持较低的码率和帧率以节省用户的网络流量，因此看起来会感觉又卡又模糊。
 
- **2. 能不能转推到非腾讯云的CDN地址？**
支持，但目前尚需要手工配置白名单开启，如果需要开启此功能，请通过 400 电话或者工单联系我们。

- **3. 此服务是否收费？**
旁路推流到腾讯云直播CDN是不收取转推费用的，到其他云商CDN会收取一定的转推费用。





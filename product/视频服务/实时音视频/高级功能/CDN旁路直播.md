基于 UDP 传输协议的 TRTC 服务，可以通过协议转换将音视频流对接到标准的直播 CDN 系统上，这个过程我们称之为“旁路推流”或者“旁路直播”。

您可以在 TRTC 控制台中开启旁路直播功能，功能开启后，您会自动获取一个 TRTC 房间中的各路音视频流。同时您也可以通过 TRTCCloud 中提供的 **setMixTranscodingConfig** 接口，启动云端混流转码，这样就可以将多路画面混合到一路直播流上，如下图所示：
![](https://main.qcloudimg.com/raw/bc9a947800ae8648951a9def71114ca9.gif)

下面主要介绍如何在腾讯云直播 CDN 系统上，通过标准的 **http + flv** 协议，观看 TRTC 房间里的各路音视频流。
## 平台支持

| iOS | Android | Mac OS | Windows | 微信小程序 | Chrome 浏览器|
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|     ✔  |    ✔    |    ✔   |    ✔    |    ✔     |   ✔     |

## 功能体验
我们在实时音视频 [DEMO](https://cloud.tencent.com/document/product/647/17021) 中加入了旁路直播功能，您可以在视频通话的过程中单击“更多功能”按钮找到该功能的体验入口（播放器 TXLivePlayer 的下载地址在 [移动直播页面](https://cloud.tencent.com/document/product/454/6555)）。
![](https://main.qcloudimg.com/raw/1d663f77c71bee9914b60609edaf1fef.jpg)


## 应用场景
基于旁路直播特性，我们可以实现主流直播平台常见的主播连麦功能：
1. 主播通过 `enterRoom()`创建一个 TRTC 音视频房间。
2. 如果当前的账号已经开启了“旁路直播”功能，即可获得该房间的一路直播 CDN 播放地址（http - flv 协议）。
3. 观众可以通过 TXLivePlayer 观看该路（http - flv 协议）直播地址。如果设置极速模式，延时通常为2s - 3s。
4. 当有观众通过 `enterRoom()`发起连麦，或者有其他主播通过`connectOtherRoom()` 发起 PK 后，即可通过 `setMixTranscodingConfig()` 启动云端混流，这样原来的 CDN 播放地址就会从单一的一路视频变成混合视频。
5. 当连麦结束后，主播可以再次调用 `setMixTranscodingConfig()` 关闭混流，这样 CDN 播放地址又会恢复成单路画面。

## 如何使用

### step1: 开通服务

在腾讯云实时音视频 [控制台](https://console.cloud.tencent.com/rav) 的**功能配置**页面里可以开启“自动旁路直播”功能。开启此功能的前提是需要先开通腾讯 [云直播](https://console.cloud.tencent.com/live) 服务。
![](https://main.qcloudimg.com/raw/91672da223a6eb7c24e8c9891018ead1.png)

### step2: 独立画面

开启旁路直播功能后， TRTC 房间里的每一路画面都配备一路对应的播放地址，其计算规则如下：
```
http://[bizid].liveplay.myqcloud.com/live/[bizid]_[streamid].flv
```
- streamid = MD5 (房间号\_用户名\_流类型)。
- bizid： 一个与直播服务相关的数字，请在 [实时音视频控制台](https://console.cloud.tencent.com/rav) 选择已经创建的应用，单击【帐号信息】后，在“直播信息”中获取。
![](https://main.qcloudimg.com/raw/4bacb840b1ece10544f1f3414635fe7c.png)
- 流类型：摄像头画面的流类型是 main，屏幕分享的流类型是 aux。
	>!Web 端目前屏幕分享的流类型也是 main。

您可以参照下面的计算示例来计算您的**直播流地址**：
```
例如 bizid = 8888， 房间号 = 12345，用户名 = userA， 用户当前使用了摄像头。

那么 streamid = MD5(12345_userA_main) = 8d0261436c375bb0dea901d86d7d70e8

所以 userA 这一路的腾讯云 CDN 观看地址（推荐 http - flv）是：

http://8888.liveplay.myqcloud.com/live/8888_8d0261436c375bb0dea901d86d7d70e8.flv
```

### step3: 混合画面

如果您想要获得混合后的直播画面，需要调用 TRTCCloud 的 `setMixTranscodingConfig` 接口启动云端混流转码，该接口的参数 `TRTCTranscodingConfig` 可用于配置：
 - 各个子画面的摆放位置和大小。
 - 混合画面的画面质量和编码参数。

详细配置方法请参考 [云端混流转码](https://cloud.tencent.com/document/product/647/16827)。
>! `setMixTranscodingConfig` 并不是在终端进行混流，而是将混流配置发送到云端，并在云端服务器进行混流和转码。由于混流和转码都需要对原来的音视频数据进行解码和二次编码，所以需要更长的处理时间。因此，混合画面的实际观看时延要比独立画面的多出1 - 2秒。

### step4: 对接播放

我们推荐以 `http` 为前缀且以 `.flv` 为后缀的 **http - flv** 地址，该地址的播放具有时延低、秒开效果好且稳定可靠的特点。播放器推荐使用已经打包在 TRTC SDK 里的 TXLivePlayer 播放器，该播放器的参考文档为：
- [TXLivePlayer(iOS)](https://cloud.tencent.com/document/product/454/7880)
- [TXLivePlayer(Android)](https://cloud.tencent.com/document/product/454/7886)
- [TXLivePlayer(Windows)](https://cloud.tencent.com/document/product/454/13676#.E6.92.AD.E6.94.BE.E5.8A.9F.E8.83.BD)

### step5: 优化延时

开启旁路直播后的 http - flv 地址，由于经过了直播 CDN 的扩散和分发，观看时延肯定要比直接在 TRTC 直播间里的通话时延要高。那么具体时延是多少呢？按照目前腾讯云的直播 CDN 技术，如果配合 TXLivePlayer 播放器，可以达到下表中的延时标准：

| 旁路流类型 | TXLivePlayer 的播放模式 |  平均延时 |
|:-------:|:-------:|:--------:|
| 独立画面 | 极速模式（推荐） | **2s - 3s** |
| 独立画面 | 流畅模式 | >= 5s |
| 混合画面 | 极速模式（推荐） | **4s - 5s** |
| 混合画面 | 混合模式 | >= 7s |

![](https://main.qcloudimg.com/raw/c34bc689fc4783829563860c94cbc9ca.jpg)
如果您在实测中看到的延时比上表中的要大，可以按照如下指引来优化延时：

- **使用 TRTC SDK 自带的 TXLivePlayer**
如果使用普通的 ijkplayer 或者 ffmpeg 播放这些直播流地址，时延一般是不可控的，因为他们都是基于 ffmpeg 的内核包装出的播放器，缺乏延时调控的能力。TXLivePlayer 有一个自研的播放引擎，具备延时调控的能力。

- **设置 TXLivePlayer 的播放模式为极速模式**
可以通过设置 TXLivePlayerConfig 的三个参数来实现极速模式，以 [iOS](https://cloud.tencent.com/document/product/454/7880#Delay) 为例，设置代码如下：

```
// 设置 TXLivePlayer 的播放模式为极速模式
TXLivePlayerConfig * config = [[TXLivePlayerConfig alloc] init];
config.bAutoAdjustCacheTime = YES;
config.minAutoAdjustCacheTime = 1; // 最小缓冲1s
config.maxAutoAdjustCacheTime = 1; // 最大缓冲1s
[player setConfig:config];

// 启动直播播放
```

## 常见问题
**为什么房间里只有一个人的时候画面又卡又模糊?**
请将 `enterRoom` 中 TRTCAppScene 参数指定为 **TRTCAppSceneLIVE**，VideoCall 模式针对视频通话做了优化，所以在房间中只有一个用户时，画面会保持较低的码率和帧率以节省用户的网络流量，因此看起来会感觉又卡又模糊。
 
 




## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | &#10003;  | -  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。

## 适用场景

CDN 直播观看，也叫 “CDN 旁路直播”，由于 TRTC 采用 UDP 协议进行传输音视频数据，而标准直播 CDN 则采用的 RTMP\HLS\FLV 等协议进行数据传输，所以需要将 TRTC 中的音视频数据**旁路**到直播 CDN 中，才能在让观众通过直播 CDN 进行观看。

给 TRTC 对接 CDN 观看，一般被用于解决如下两类问题：
- **问题一：超高并发观看**
TRTC 的低延时观看能力，单房间支持的最大人数上限为10万人。CDN 观看虽然延迟要高一些，但支持10万人以上的并发观看，且 CDN 的计费价格更加便宜。
- **问题二：移动端网页播放**
TRTC 虽然支持 WebRTC 协议接入，但主要用于 Chrome 桌面版浏览器，移动端浏览器的兼容性非常不理想，尤其是 Android 手机浏览器对 WebRTC 的支持普遍都很差。所以如果希望通过 Web 页面在移动端分享直播内容，还是推荐使用 HLS(m3u8) 播放协议，这也就需要借助直播 CDN 的能力来支持 HLS 协议。


## 原理解析
腾讯云会使用一批旁路转码集群，将音视频通话 TRTC 中的音视频数据旁路到直播 CDN 系统中，该集群负责将音视频通话 TRTC 所使用的 UDP 协议转换为标准的直播 RTMP 协议。
[](id:directCDN)
**单路画面的旁路直播**
当音视频通话 TRTC 房间中只有一个主播时，TRTC 的旁路推流跟标准的 RTMP 协议直推功能相同，不过 TRTC 的 UDP 相比于 RTMP 有更强大的弱网络抗性。
![](https://main.qcloudimg.com/raw/b682b1493a81bc8a53aea6a07f375ba2.gif)

[](id:mixCDN)
**混合画面的旁路直播**
音视频通话TRTC 最擅长的领域就是音视频互动连麦，如果一个房间里同时有多个主播，而 CDN 观看端只希望拉取一路音视频画面，就需要使用 [云端混流服务](https://cloud.tencent.com/document/product/647/16827) 将多路画面合并成一路，其原理如下图所示：
![](https://main.qcloudimg.com/raw/f2feaaaac176bb4fe7dd1c318490f9e1.gif)


<dx-alert infotype="explain" title="<b>为什么不直接播放多路 CDN 画面？</b>">
播放多路 CDN 画面很难解决多路画面的延迟对齐问题，同时拉取多路画面所消耗的下载流量也比单独画面要多，所以业内普遍采用云端混流方案。
</dx-alert>

## 前提条件
已开通腾讯 [云直播](https://console.cloud.tencent.com/live) 服务。应国家相关部门的要求，直播播放必须配置播放域名，具体操作请参考 [添加自有域名](https://cloud.tencent.com/document/product/267/20381)。

## 使用步骤

[](id:step1)
### 步骤1：开启旁路推流功能

1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/trtc)。
2. 在左侧导航栏选择【应用管理】，单击目标应用所在行的【功能配置】。
3. 在【旁路推流配置】中，单击【启用旁路推流】右侧的![](https://main.qcloudimg.com/raw/5f58afe211aa033037e5c0b793023b49.png)，在弹出的【开启旁路推流功能】对话框中，单击【开启旁路推流功能】即可开通。


[](id:step2)
### 步骤2：配置播放域名并完成 CNAME
1. 登录 [云直播控制台](https://console.cloud.tencent.com/live/)。
2. 在左侧导航栏选择【域名管理】，您会看到在您的域名列表新增了一个推流域名，格式为 `xxxxx.livepush.myqcloud.com`，其中 xxxxx 是一个数字，叫做 bizid，您可以在实时音视频控制台 >【[应用管理](https://console.cloud.tencent.com/trtc/app)】>【应用信息】中查找到 bizid 信息。
3. 单击【添加域名】，输入您已经备案过的播放域名，选择域名类型为【播放域名】，选择加速区域（默认为【中国大陆】），单击【确定】即可。
4. 域名添加成功后，系统会为您自动分配一个 CNAME 域名（以`.liveplay.myqcloud.com`为后缀）。CNAME 域名不能直接访问，您需要在域名服务提供商处完成 CNAME 配置，配置生效后，即可享受云直播服务。具体操作请参见 [CNAME 配置](https://cloud.tencent.com/document/product/267/19908)。

![](https://main.qcloudimg.com/raw/97b24ee2a758b311ba8dea23db04c3ae.png)

>! **不需要添加推流域名**，在 [步骤1](#step1) 中开启旁路直播功能后，腾讯云会默认在您的云直播控制台中增加一个格式为  `xxxxx.livepush.myqcloud.com` 的推流域名，该域名为腾讯云直播服务和 TRTC 服务之间约定的一个默认推流域名，暂时不支持修改。

[](id:step3)
### 步骤3：关联 TRTC 的音视频流到直播 streamId
开启旁路推流功能后， TRTC 房间里的每一路画面都配备一路对应的播放地址，该地址的格式如下：
```
http://播放域名/live/[streamId].flv
```
地址中的 streamId 可以在直播中唯一标识一条直播流，您可以自己指定 streamId，也可以使用系统默认生成的。

#### 方式一：自定义指定 streamId
您可以在调用 `TRTCCloud` 的 `enterRoom` 函数时，通过其参数 `TRTCParams` 中的 `streamId` 参数指定直播流 ID。
以 iOS 端的 Objective-C 代码为例：

```Objective-C
TRTCCloud *trtcCloud = [TRTCCloud sharedInstance];
TRTCParams *param = [[TRTCParams alloc] init];
param.sdkAppId = 1400000123;     // TRTC 的 SDKAppID，创建应用后可获得
param.roomId   = 1001;           // 房间号
param.userId   = @"rexchang";    // 用户名
param.userSig  = @"xxxxxxxx";    // 登录签名
param.role     = TRTCRoleAnchor; // 角色：主播
param.streamId = @"stream1001";  // 流 ID
[trtcCloud enterRoom:params appScene:TRTCAppSceneLIVE]; // 请使用 LIVE 模式
```
userSig 的计算方法请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/1449/58939)。

#### 方式二：系统指定 streamId
开启自动旁路推流后，如果您没有自定义指定 streamId，系统会默认为您生成一个缺省的 streamId，生成规则如下：

- **拼装 streamId 用到的字段**
  - SDKAppID：您可以在 [控制台](https://console.cloud.tencent.com/trtc/app) >【应用管理】>【应用信息】中查找到。
  - bizid：您可以在 [控制台](https://console.cloud.tencent.com/trtc/app) >【应用管理】>【应用信息】中查找到。
  - roomId：由您在 `enterRoom` 函数的参数 `TRTCParams` 中指定。
  - userId：由您在 `enterRoom` 函数的参数 `TRTCParams` 中指定。
  - streamType： 摄像头画面为 main，屏幕分享为 aux （WebRTC 由于同时只支持一路上行，因此 WebRTC 上屏幕分享的流类型是 main）。

- **拼装 streamId 的计算规则**
 <table>
<tr>
<th>拼装</th>
<th>2020年01月09日及此后新建的应用</th>
<th>2020年01月09日前创建且使用过的应用</th>
</tr>
<tr>
<td>拼装规则</td>
<td>streamId = urlencode(sdkAppId_roomId_userId_streamType)</td>
<td>StreamId = bizid_MD5(roomId_userId_streamType)</td>
</tr>
<tr>
<td>计算样例</td>
<td>例如：sdkAppId = 12345678，roomId = 12345，userId = userA，用户当前使用了摄像头。<br>那么：streamId = 12345678_12345_userA_main</td>
<td>例如：bizid = 1234，roomId = 12345，userId = userA，用户当前使用了摄像头。<br>那么：streamId = 1234_MD5(12345_userA_main) = 1234_8D0261436C375BB0DEA901D86D7D70E8</td>
</tr>
</table>


[](id:step4)
### 步骤4：控制多路画面的混合方案

如果您想要获得混合后的直播画面，需要调用 TRTCCloud 的 `setMixTranscodingConfig` 接口启动云端混流转码，该接口的参数 `TRTCTranscodingConfig` 可用于配置：
 - 各个子画面的摆放位置和大小。
 - 混合画面的画面质量和编码参数。

画面布局的详细配置方法请参考 [云端混流转码](https://cloud.tencent.com/document/product/647/16827)，整个流程所涉及的各模块关系可以参考 [原理解析](#mixCDN)。

>! `setMixTranscodingConfig` 并不是在终端进行混流，而是将混流配置发送到云端，并在云端服务器进行混流和转码。由于混流和转码都需要对原来的音视频数据进行解码和二次编码，所以需要更长的处理时间。因此，混合画面的实际观看时延要比独立画面的多出1s - 2s。

[](id:step5)
### 步骤5：获取播放地址并对接播放
当您通过 [步骤2](#step2) 配置完播放域名和 [步骤3](#step3) 完成 streamId 的映射后，即可得到直播的播放地址。播放地址的标准格式为：
```
http://播放域名/live/[streamId].flv
```

例如，您的播放域名为`live.myhost.com`，您将房间（1001）中的用户 userA 的直播流 ID 通过进房参数指定为 `streamId = "streamd1001"`。
则您可以得到三路播放地址：
```
 rtmp 协议的播放地址：rtmp://live.myhost.com/live/streamd1001
 flv 协议的播放地址：http://live.myhost.com/live/streamd1001.flv
 hls 协议的播放地址：http://live.myhost.com/live/streamd1001.m3u8
```

我们推荐以 `http` 为前缀且以 `.flv` 为后缀的 **http - flv** 地址，该地址的播放具有时延低、秒开效果好且稳定可靠的特点。
播放器选择方面推荐参考如下表格中的指引的方案：

| 所属平台    | 对接文档 | API 概览 | 支持的格式 |
| ----------- | ----------- | ----------- | ----------- |
| iOS App     | [接入指引](https://cloud.tencent.com/document/product/1449/57068) | [TXLivePlayer(iOS)](https://cloud.tencent.com/document/product/1449/57170) | 推荐 FLV                                                     |
| Android App | [接入指引](https://cloud.tencent.com/document/product/1449/57069) | [TXLivePlayer(Android)](https://cloud.tencent.com/document/product/1449/57172) | 推荐 FLV                                                     |
| Web 浏览器  | [接入指引](https://cloud.tencent.com/document/product/1449/57070) | [TXLivePusher](https://cloud.tencent.com/document/product/1449/57173) | 桌面端 Chrome 浏览器支持 FLV <br> Mac 端 Safari和移动端手机浏览器仅支持 HLS |
| 微信小程序  | [接入指引](https://cloud.tencent.com/document/product/1449/57071) | [&lt;live-player&gt; 标签](https://cloud.tencent.com/document/product/1449/58919) | 推荐 FLV                                                     |




[](id:step6)
### 步骤6：优化播放延时

开启旁路直播后的 http - flv 地址，由于经过了直播 CDN 的扩散和分发，观看时延肯定要比直接在 TRTC 直播间里的通话时延要高。
按照目前腾讯云的直播 CDN 技术，如果配合 TXLivePlayer 播放器，可以达到下表中的延时标准：

| 旁路流类型 | TXLivePlayer 的播放模式 |  平均延时 |  实测效果 |
|:-------:|:-------:|:--------:|:---------:|
| 独立画面 | 极速模式（推荐） | **2s - 3s** | 下图中左侧对比图（橙色）|
| 混合画面 | 极速模式（推荐） | **4s - 5s** | 下图中右侧对比图（蓝色）|

下图中的实测效果，采用了同样的一组手机，左侧 iPhone 6s 使用了 TRTC SDK 进行直播，右侧的小米6 使用 TXLivePlayer 播放器播放 FLV 协议的直播流。
![](https://main.qcloudimg.com/raw/98cf3ebc48875d831ef0bd138f7a3cb5.jpg)

如果您在实测中延时比上表中的更大，可以按照如下指引优化延时：

- **使用 TRTC SDK 自带的 TXLivePlayer**
普通的 ijkplayer 或者 ffmpeg 基于 ffmpeg 的内核包装出的播放器，缺乏延时调控的能力，如果使用该类播放器播放上述直播流地址，时延一般不可控。TXLivePlayer 有一个自研的播放引擎，具备延时调控的能力。

- **设置 TXLivePlayer 的播放模式为极速模式**
可以通过设置 TXLivePlayerConfig 的三个参数来实现极速模式，以 [iOS](https://cloud.tencent.com/document/product/1449/57068#delay) 为例。
以 iOS 端的 Objective-C 代码为例：
```
 // 设置 TXLivePlayer 的播放模式为极速模式
    TXLivePlayerConfig * config = [[TXLivePlayerConfig alloc] init];
    config.bAutoAdjustCacheTime = YES;
    config.minAutoAdjustCacheTime = 1; // 最小缓冲1s
    config.maxAutoAdjustCacheTime = 1; // 最大缓冲1s
    [player setConfig:config];
    // 启动直播播放
```

[](id:expense)
## 相关费用

实现 CDN 直播观看的费用包括**观看费用**和**转码费用**，观看费用为基础费用，转码费用仅在启用 [多路画面混合](#mixCDN) 时才会收取。

>!本文中的价格为示例，仅供参考。若价格与实际不符，请以 [云直播 > 标准直播](https://cloud.tencent.com/document/product/267/2818) 的计费说明为准。

### 观看费用：通过直播 CDN 观看时产生的费用

通过直播 CDN 观看时，**云直播**将向您收取因观看产生的下行流量/带宽费用，可以根据实际需要选择适合自己的计费方式，默认采用流量计费，详情请参见 [云直播 > 标准直播 > 流量带宽](https://cloud.tencent.com/document/product/267/34175#.E6.B5.81.E9.87.8F.E5.B8.A6.E5.AE.BD) 计费说明。


### 转码费用：启用多路画面混合时收取
如果您启用了 [多路画面混合](#mixCDN) ，混流需要进行解码和编码，因此会产生额外的混流转码费用。混流转码根据分辨率大小和转码时长进行计费，主播用的分辨率越高，连麦时间（通常在连麦场景才需要混流转码）越长，费用越高，详情请参见 [云直播 > 直播转码](https://cloud.tencent.com/document/product/267/39889) 计费说明。

<dx-alert infotype="explain" title="示例：">
您通过 [setVideoEncodrParam()](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloudDef__ios.html#interfaceTRTCVideoEncParam) 设置主播的码率（videoBitrate）为1500kbps，分辨率为720P。如果有一位主播跟观众连麦了1个小时，连麦期间开启了 [多路画面混合](#mixCDN) ，那么产生的转码费用为 `0.0325元/分钟 × 60分钟 = 1.95元`。
</dx-alert>



## 常见问题
**为什么房间里只有一个人时画面又卡又模糊?**
请将 `enterRoom` 中 TRTCAppScene 参数指定为 **TRTCAppSceneLIVE**。
VideoCall 模式针对视频通话做了优化，所以在房间中只有一个用户时，画面会保持较低的码率和帧率以节省用户的网络流量，看起来会感觉又卡又模糊。

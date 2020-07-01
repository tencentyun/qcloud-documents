基于 UDP 传输协议的 TRTC 服务，可以通过协议转换将音视频流对接到标准的直播 CDN 系统上，这个过程我们称之为“旁路推流”或者“旁路直播”。
您可以在 TRTC 控制台中开启旁路直播功能，功能开启后，您会自动获取一个 TRTC 房间中的各路音视频流。同时您也可以通过 TRTCCloud 中提供的 **setMixTranscodingConfig** 接口，启动云端混流转码，这样就可以将多路画面混合到一路直播流上，如下图所示：
![](https://main.qcloudimg.com/raw/bc9a947800ae8648951a9def71114ca9.gif)

下面主要介绍如何在腾讯云直播 CDN 系统上，通过标准的 **http + flv** 协议，观看 TRTC 房间里的各路音视频流。


## Demo
我们在实时音视频 [Demo](https://cloud.tencent.com/document/product/647/17021) 中加入了旁路直播功能，您可以在视频通话的过程中单击【更多功能】找到该功能的体验入口（播放器 TXLivePlayer 的下载地址在 [移动直播页面](https://cloud.tencent.com/document/product/454/6555)）。
![](https://main.qcloudimg.com/raw/3d237e98f64184ad22b7493c10951223.jpg)

## 示例代码

| 所属平台 | 计算 CDN 观看地址 | 设置云端混流参数 |
|---------|---------|---------|
| iOS | 文件：[TRTCCloudManager.m](https://github.com/tencentyun/TRTCSDK/blob/master/iOS/TRTCDemo/TRTC/Settings/SDKManager/Feature/TRTCCloudManager.m) <br>函数：getCdnUrlOfUser() | 文件：[TRTCCloudManager.m](https://github.com/tencentyun/TRTCSDK/blob/master/iOS/TRTCDemo/TRTC/Settings/SDKManager/Feature/TRTCCloudManager.m)<br>函数：updateCloudMixtureParams() |
| Android | 文件：[CdnPlayManager.java](https://github.com/tencentyun/TRTCSDK/blob/master/Android/TRTCDemo/trtc/src/main/java/com/tencent/liteav/demo/trtc/sdkadapter/cdn/CdnPlayManager.java)<br>函数：initPlayUrl() | 文件：[TRTCRemoteUserManager.java](https://github.com/tencentyun/TRTCSDK/blob/master/Android/TRTCDemo/trtc/src/main/java/com/tencent/liteav/demo/trtc/sdkadapter/remoteuser/TRTCRemoteUserManager.java)<br>函数：updateCloudMixtureParams() |
| Windows（C++） |  文件：[TRTCSettingViewController.cpp](https://github.com/tencentyun/TRTCSDK/blob/master/Windows/DuilibDemo/TRTCSettingViewController.cpp)<br>函数：NotifyOtherTab | 文件：[TRTCCloudCore.cpp](https://github.com/tencentyun/TRTCSDK/blob/master/Windows/DuilibDemo/sdkinterface/TRTCCloudCore.cpp)<br>函数：updateMixTranCodeInfo() |
| Windows（C#） |  文件：[TRTCMainForm.cs](https://github.com/tencentyun/TRTCSDK/blob/master/Windows/CSharpDemo/TRTCMainForm.cs)<br>函数：OnShareUrlLabelClick| 文件：[TRTCMainForm.cs](https://github.com/tencentyun/TRTCSDK/blob/master/Windows/CSharpDemo/TRTCMainForm.cs)<br>函数：UpdateMixTranCodeInfo() |
| Mac |  暂无 | 文件：[TRTCMainWindowController.m](https://github.com/tencentyun/TRTCSDK/blob/master/Mac/TRTCDemo/TRTC/TRTCMainWindowController.m)<br>函数：updateCloudMixtureParams() |

## 应用场景
基于旁路直播特性，我们可以实现主流直播平台常见的主播连麦和直播 PK 功能：

1. 主播通过 TRTCCloud 中的 `enterRoom()` 接口，可创建一个 TRTC 房间，通过  `connectOtherRoom()` 接口可跟其他房间的主播进行实时视频连麦 PK。当前账号开启了“旁路直播”功能后，可获得该房间对应的一路直播 CDN 地址（推荐：http - flv 协议，秒开效果好）。
2. 观众通过 TXLivePlayer 播放器可观看该路 CDN 地址，也可通过 TRTCCloud 中的 `enterRoom()` 接口进入主播当前的 TRTC 房间，跟主播进行实时视频连麦互动。
4. 主播进入连麦或者 PK 状态后，通过 TRTCCloud 中的 `setMixTranscodingConfig()` 接口，可通知云端进行视频混流（即将多路视频画面混合成一路），使原 CDN 地址中的视频画面从单人画面变成多人混合画面。过程中，一直观看的观众无需切换直播 CDN 地址。
5. 当连麦结束后，主播可以再次调用 `setMixTranscodingConfig()` 接口关闭混流，将 CDN 地址中的视频画面恢复为单人画面。

## 前提条件
已开通腾讯 [云直播](https://console.cloud.tencent.com/live) 服务。应国家相关部门的要求，直播播放必须配置播放域名，具体操作请参考 [添加自有域名](https://cloud.tencent.com/document/product/267/20381)。

## 使用步骤

### 步骤1：开通服务

1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/rav)。
2. 在左侧导航栏选择【应用管理】，单击目标应用所在行的【功能配置】。
3. 单击【启动自动旁路直播】右侧的<img src="https://main.qcloudimg.com/raw/8f08eba741586e96dbe3b30c6804e9b6.png"  style="margin:0;">，在弹出的【开启自动旁路直播】对话框中，单击【确定】。
4. 在弹出的【选择旁路直播类型】对话框中，选择合适的直播类型，单击【确定】保存设置。

### 步骤2：独立画面

开启旁路直播功能后， TRTC 房间里的每一路画面都配备一路对应的播放地址，该地址的格式如下：
```
http://播放域名/live/[StreamId].flv
```
其中 `播放域名`、`StreamId` 都是需要您填写的部分，具体的填写规则如下：
- 流类型：一般情况下，摄像头画面的流类型是 main，屏幕分享的流类型是 aux。
 >!WebRTC 端同时只支持一路上行，因此 WebRTC 上屏幕分享的流类型是 main。
 >
- StreamId 计算方法：
 - 2020年01月09日及此后新建的应用，或此前已创建但从未使用过的应用，`StreamId = urlencode(SDKAppID_房间号_userId_流类型)`，即由`SDKAppID_房间号_userId_流类型`计算的流 ID 经过 URL 编码而成。
 - 2020年01月09日前创建且使用过的应用，`StreamId = bizid_MD5(房间号_userId_流类型)`
- SDKAppID：请在 [实时音视频控制台](https://console.cloud.tencent.com/trtc/app) 选择已经创建的应用，在“应用信息”中获取。 
 ![](https://main.qcloudimg.com/raw/5d54378547d8bb38c60ae153039da196.png)

我们通过如下示例来详细地展示 StreamId 的计算过程，您可以参照该示例来计算您自己的 CDN 播放地址：
>?本文以2020年01月09日创建的应用计算 StreamId 为例。
>
```
例如，SDKAppID = 12345678，进行旁路直播的房间号 = 12345、userId = userA，使用摄像头画面。

1. StreamId = urlencode(12345678_12345_userA_main) = 12345678_12345_userA_main
2. 拼接后 userA 这一路的腾讯云 CDN 观看地址为：
 flv 协议：http://播放域名/live/12345678_12345_userA_main.flv
 hls 协议：http://播放域名/live/12345678_12345_userA_main.m3u8
```


### 步骤3：混合画面

如果您想要获得混合后的直播画面，需要调用 TRTCCloud 的 `setMixTranscodingConfig` 接口启动云端混流转码，该接口的参数 `TRTCTranscodingConfig` 可用于配置：
 - 各个子画面的摆放位置和大小。
 - 混合画面的画面质量和编码参数。

详细配置方法请参考 [云端混流转码](https://cloud.tencent.com/document/product/647/16827)。
>! `setMixTranscodingConfig` 并不是在终端进行混流，而是将混流配置发送到云端，并在云端服务器进行混流和转码。由于混流和转码都需要对原来的音视频数据进行解码和二次编码，所以需要更长的处理时间。因此，混合画面的实际观看时延要比独立画面的多出1s - 2s。

### 步骤4：对接播放

我们推荐以 `http` 为前缀且以 `.flv` 为后缀的 **http - flv** 地址，该地址的播放具有时延低、秒开效果好且稳定可靠的特点。播放器推荐使用已经打包在 TRTC SDK 里的 TXLivePlayer 播放器，该播放器的参考文档为：
- [TXLivePlayer(iOS)](https://cloud.tencent.com/document/product/454/7880)
- [TXLivePlayer(Android)](https://cloud.tencent.com/document/product/454/7886)


### 步骤5：优化延时

开启旁路直播后的 http - flv 地址，由于经过了直播 CDN 的扩散和分发，观看时延肯定要比直接在 TRTC 直播间里的通话时延要高。那么具体时延是多少呢？按照目前腾讯云的直播 CDN 技术，如果配合 TXLivePlayer 播放器，可以达到下表中的延时标准：

| 旁路流类型 | TXLivePlayer 的播放模式 |  平均延时 |
|:-------:|:-------:|:--------:|
| 独立画面 | 极速模式（推荐） | **2s - 3s** |
| 混合画面 | 极速模式（推荐） | **4s - 5s** |

![](https://main.qcloudimg.com/raw/63c4fbd1ddc006f660c4d1f13ae1b076.jpg)

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
**为什么房间里只有一个人时画面又卡又模糊?**
请将 `enterRoom` 中 TRTCAppScene 参数指定为 **TRTCAppSceneLIVE**，VideoCall 模式针对视频通话做了优化，所以在房间中只有一个用户时，画面会保持较低的码率和帧率以节省用户的网络流量，看起来会感觉又卡又模糊。

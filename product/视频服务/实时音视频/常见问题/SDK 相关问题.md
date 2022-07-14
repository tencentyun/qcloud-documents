### 实时音视频 TRTC 可以与 iLiveSDK 通信吗？
不可以，建议更新 iLiveSDK 方案到 TRTC ，具体操作请参考 [iLiveSDK 迁移方案](https://cloud.tencent.com/document/product/647/32281)。

### 实时音视频的小程序端、桌面浏览器端、PC 端是不是同步的？
是的，实时音视频支持全平台互通。

### 实时音视频在小程序端创建了一个房间，手机端（Andriod/iOS）能否进入该房间？
可以，实时音视频支持全平台互通。

### TRTC SDK 是否支持 iOS 后台运行？
支持，您只需选中当前工程项目，在 **Capabilities** 下的设置  **Background Modes** 为 **ON**，并勾选 **Audio，AirPlay and Picture in Picture**即可实现后台运行，详情如下图所示：
![](https://main.qcloudimg.com/raw/d960dfec88388936abce2d4cb77ac766.jpg)

### 如何创建房间？
房间是由腾讯云后台在客户端进房时自动创建的，您无需手动创建房间，只需调用客户端的相关接口“进入房间”即可：
- [iOS & Mac > enterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__ios.html#a96152963bf6ac4bc10f1b67155e04f8d)
- [Android > enterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__TRTCCloud__android.html#abfc1841af52e8f6a5f239a846a1e5d5c)
- [Windows（C++） > enterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__cplusplus.html#ac73c4ad51eda05cd2bcec820c847e84f)
- [Windows（C#） > enterRoom](https://liteav.sdk.qcloud.com/doc/api/zh-cn/group__ITRTCCloud__csharp.html#a28b2d3ec27af8c9bfd5cf687dd8e002b)
- [Electron > enterRoom](https://web.sdk.qcloud.com/trtc/electron/doc/zh-cn/trtc_electron_sdk/TRTCCloud.html#enterRoom)
- [桌面浏览器 > join](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/Client.html#join)
- [小程序 > enterRoom](https://cloud.tencent.com/document/product/647/17018#enterroom(params))

### 小程序端集成实时音视频 SDK 前需要做哪些准备工作？

1. 创建腾讯云实时音视频应用，购买相应的套餐，并获取到 SDKAppID 和密钥信息。
2. 小程序服务器域名配置。
3. 开通小程序类目与推拉流标签权限。
   出于政策和合规的考虑，微信暂未放开所有小程序对实时音视频功能（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签）的支持：
   - 小程序推拉流标签不支持个人小程序，只支持企业类小程序。
   - 小程序推拉流标签使用权限暂时只开放给有限 [类目](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。
   - 符合类目要求的小程序，需要在【[微信公众平台](https://mp.weixin.qq.com)】>【开发】>【接口设置】中自助开通该组件权限，如下图所示：
     ![](https://main.qcloudimg.com/raw/ad87091aaae2db6ad412136297886c15.png)

更多详情请参见 [跑通Demo(小程序)](https://cloud.tencent.com/document/product/647/32399) 和 [快速集成(小程序)](https://cloud.tencent.com/document/product/647/32183)。

### 实时音视频小程序端运行出错，该如何排查？

1. 请检查开通的小程序类目是否正确，&lt;live-pusher&gt; 和 &lt;live-player&gt; 标签是否已开启。
2. 请确认已将 [小程序域名白名单](https://cloud.tencent.com/document/product/647/34399#.E5.BE.AE.E4.BF.A1.E5.B0.8F.E7.A8.8B.E5.BA.8F) 添加到小程序 request 合法域名，或已开启调试模式。
3. 请重新解压小程序端 Demo 直接运行，若运行正常，建议参考 [快速集成(小程序)](https://cloud.tencent.com/document/product/647/32183) 重新集成 SDK。
4. 若问题依然存在，可以登录 [微信小程序开发者社区](https://developers.weixin.qq.com/community/develop/question) 查找相关资料，也可以 [提交工单](https://console.cloud.tencent.com/workorder/category) 或致电 95716 联系我们。

### 实时音视频小程序端进入多人音视频看不到画面，该如何处理？
1. 请使用手机真机运行，微信开发者工具内部的模拟器目前暂不支持直接运行。
2. 请通过 wx.getSystemInfo 查询小程序基础库版本，小程序基础库最低版本要求为2.10.0。
3. 请确认小程序所属的类目，由于监管要求，小程序推拉流标签使用权限暂时只开放给有限 [类目](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。

如有更多需求，或希望深度合作，可以 [提交工单](https://console.cloud.tencent.com/workorder/category) 或致电95716联系我们。

### &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签使用及错误码参考：
-  [live-pusher 错误码](https://mp.weixin.qq.com/debug/wxadoc/dev/component/live-pusher.html) 
-  [live-player 错误码](https://mp.weixin.qq.com/debug/wxadoc/dev/component/live-player.html) 
- [livePusherContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.html)
- [livePlayerContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.html)

### 调试时为什么要开启调试模式？
开启调试后，可以略过把“request 合法域名”加入小程序白名单的操作，避免遇到登录失败，通话无法连接的问题。

### 实时音视频小程序端如果需要上线或者部署正式环境怎么办？
1. 请申请域名并做好备案工作。
2. 请将服务端代码部署到申请的服务器上。
3. 请将推流域名及 IM 域名配置到小程序控制台 request 合法域名里面：
   - https://official.opensso.tencent-cloud.com
   - https://yun.tim.qq.com
   - https://cloud.tencent.com
   - https://webim.tim.qq.com

### 使用组件内置模板不符合预期是什么原因？
目前我们的组件仅支持在同层模式下使用（微信已全量支持同层模式），如果使用不符合预期，请您检查 app.json 下是否有`"renderingMode": "seperated" `配置，此配置会强制开启非同层模式，导致内置模板样式失效。

### 小程序端为什么会出现黑屏/画面卡住？

您可以检查小程序 Demo 左下方的控制面板，打开【调试模式】即可在界面上看到详细的推拉流信息，如果没有推拉流信息则表示未成功进房或 live-pusher，live-player 创建失败。
![](https://main.qcloudimg.com/raw/b370373d41217c2c0efca37ab87cc94a.jpg)


| 参数          | 含义                                                         |
| ------------- | ------------------------------------------------------------ |
| appVersion    | 微信版本号                                                   |
| libVersion    | 基础库版本号                                                 |
| template      | trtc-room 组件的 template                                      |
| debug         | 是否开启推拉流的 debug 信息                                    |
| userID        | 生成的用户 ID                                                 |
| roomID        | 房间号                                                       |
| camera        | 是否开启摄像头                                               |
| mic           | 是否开启麦克风                                               |
| switch camera | 摄像头位置（front / back）                                       |
| Room          | 进房，退房，退房并返回上一界面操作                           |
| user count    | 房间内人数以及 user 信息<br/>userID：用户 ID<br/>mainV：该用户是否有主路视频<br/>mainA：该用户是否有主路音频<br/>auxV：该用户是否有辅路视频 |
| stream count  | 房间内流的数量以及流信息<br/>userID：用户 ID<br/>SubV：是否订阅此路流的视频<br />SubA：是否订阅此路流的音频 |

### 运行桌面浏览器端 SDK 时，出现错误：“RtcError: no valid ice candidate found”该如何处理？

出现该错误说明 TRTC 桌面浏览器 SDK 在 STUN 打洞失败，请检查防火墙配置。TRTC 桌面浏览器 SDK 依赖以下端口进行数据传输，请将其加入防火墙白名单，配置完成后，您可以通过访问并体验 [官网 Demo](https://web.sdk.qcloud.com/trtc/webrtc/demo/api-sample/basic-rtc.html) 检查配置是否生效。

具体请参见 [应对防火墙限制相关](https://cloud.tencent.com/document/product/647/34399)。

### 出现客户端错误："RtcError: ICE/DTLS Transport connection failed" 或 “RtcError: DTLS Transport connection timeout”该如何处理？
出现该错误说明 TRTC 桌面浏览器 SDK 在建立媒体传输通道时失败，请检查防火墙配置。TRTC 桌面浏览器 SDK 依赖以下端口进行数据传输，请将其加入防火墙白名单，配置完成后，您可以通过访问并体验 [官网 Demo](https://web.sdk.qcloud.com/trtc/webrtc/demo/api-sample/basic-rtc.html) 检查配置是否生效。

具体请参见 [应对防火墙限制相关](https://cloud.tencent.com/document/product/647/34399)。


### 出现10006 error 该如何处理？
如果出现"Join room failed result: 10006 error: service is suspended,if charge is overdue,renew it"，请确认您的实时音视频应用的服务状态是否为可用状态。
登录 [实时音视频控制台](https://console.cloud.tencent.com/rav)，单击您创建的应用，单击【帐号信息】，在帐号信息面板即可确认服务状态。
![](https://main.qcloudimg.com/raw/13c9b520ea333804cffb4e2c4273fced.png)


### 实时音视频桌面浏览器端的截图功能如何实现？
截图功能使用的是实例 HTMLVideoElement 中的 HTMLVideoElement.takeSnapshot。
``` 
/*
 * params:
 *   DeviceObject device
 * return:
 *   null
 */
    var video = document.getElementById(""video"")
    video.takeSnapshot(function(data){
        var img = document.createElement('img');
        img.src = data;
        $(""#some_div_id"").append( img );
    });
```


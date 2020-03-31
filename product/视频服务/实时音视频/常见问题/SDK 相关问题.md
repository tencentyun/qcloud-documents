

### 实时音视频可以与互动直播 SDK 通信吗？

可以，只需 SDKAppID 一致且房间号一致即可。

### 实时音视频的小程序端、Web 端、PC 端是不是同步的？
是的，实时音视频支持全平台互通。

### 实时音视频在小程序端创建了一个房间，手机端（Andriod/iOS）能否进入该房间？
能进入，实时音视频支持全平台互通。

### TRTC SDK 是否支持 iOS 后台运行？
支持，您只需选中当前工程项目，在 **Capabilities** 下的设置  **Background Modes** 为 **ON**，并勾选 **Audio，AirPlay and Picture in Picture** 即可实现后台运行，详情如下图所示：
![](https://main.qcloudimg.com/raw/d960dfec88388936abce2d4cb77ac766.jpg)

### 小程序端集成实时音视频 SDK 前需要做哪些准备工作？

- 创建腾讯云实时音视频应用，购买相应的套餐，并获取到 SDKAppID。
- 获取私钥文件。
- 小程序服务器域名配置。
- 开通小程序类目与推拉流标签权限。
 出于政策和合规的考虑，微信暂未放开所有小程序对实时音视频功能（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签）的支持：
 - 小程序推拉流标签不支持个人小程序，只支持企业类小程序。
 - 小程序推拉流标签使用权限暂时只开放给有限 [类目](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。
 - 符合类目要求的小程序，需要在【[微信公众平台](https://mp.weixin.qq.com)】>【开发】>【接口设置】中自助开通该组件权限，如下图所示：
 ![](https://main.qcloudimg.com/raw/ad87091aaae2db6ad412136297886c15.png)

更多详情请参见 [跑通Demo(小程序)](https://cloud.tencent.com/document/product/647/32399) 和 [快速集成(小程序)](https://cloud.tencent.com/document/product/647/32183)。

### 实时音视频小程序端运行出错，该如何排查？

- 请检查开通的小程序类目是否正确，&lt;live-pusher&gt; 和 &lt;live-player&gt; 标签是否已开启。
- 请修改 wxlite/config.js 中的 URL，使用默认的官方 Demo 后台`_https://room.qcloud.com_`，直接运行小程序。
- 请重新解压小程序端 Demo 直接运行，若运行正常，建议参考 [快速集成(小程序)](https://cloud.tencent.com/document/product/647/32183) 重新集成 SDK。
- 若问题依然存在，可以 [提交工单](https://console.cloud.tencent.com/workorder/category) 或致电95716联系我们。

### 实时音视频小程序端进入多人音视频看不到画面，该如何处理？
- 请使用手机真机运行，微信开发者工具内部的模拟器目前暂不支持直接运行。
- 请通过 wx.getSystemInfo 查询小程序基础库版本，小程序基础库最低版本要求为2.10.0。
- 请确认小程序所属的类目，由于监管要求，小程序推拉流标签使用权限暂时只开放给有限 [类目](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。
- 如有更多需求，或希望深度合作，可以 [提交工单](https://console.cloud.tencent.com/workorder/category) 或致电95716联系我们。

### &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签使用及错误码参考：
- [live-pusher&错误码](https://mp.weixin.qq.com/debug/wxadoc/dev/component/live-pusher.html)
- [live-player&错误码](https://mp.weixin.qq.com/debug/wxadoc/dev/component/live-player.html)
- [livePusherContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePusherContext.html)
- [livePlayerContext](https://developers.weixin.qq.com/miniprogram/dev/api/media/live/LivePlayerContext.html)


### 调试时为什么要开启调试模式？

开启调试后，可以略过把“request 合法域名”加入小程序白名单的操作，避免遇到登录失败，通话无法连接的问题。

### 实时音视频小程序端如果需要上线或者部署正式环境怎么办？
- 请申请域名并做备案。
- 请将服务端代码部署到申请的服务器上。
- 请将推流域名及 IM 域名配置到小程序控制台 request 合法域名里面：
<table>
<tr>
<th>域名</th>
<th>说明</th>
</tr>
<tr>
<td><code>https://cloud.tencent.com</code></td>
<td>推流域名</td>
</tr>
<tr>
<td><code>https://webim.tim.qq.com</code></td>
<td>IM 业务域名</td>
</tr>
<tr>
<td><code>https://yun.tim.qq.com</code></td>
<td>IM 业务域名</td>
</tr>
<tr>
<td><code>https://pingtas.qq.com</code></td>
<td>IM 业务域名</td>
</tr>
</table>

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
| stream count  | 房间内流的数量以及流信息<br/>userID用户 ID<br/>SubV：是否订阅此路流的视频<br />SubA：是否订阅此路流的音频 |

### 运行 Web 端时，出现客户端错误：“RtcError: no valid ice candidate found”该如何处理？
出现该错误说明 TRTC Web SDK 在 STUN 打洞失败，请检查防火墙配置。TRTC Web SDK 依赖以下端口进行数据传输，请将其加入防火墙白名单，配置完成后，您可以通过访问并体验 [官网 Demo](https://trtc-1252463788.file.myqcloud.com/web/demo/official-demo/index.html) 检查配置是否生效。
 - TCP 端口：8687
 - UDP 端口：8000，8800，843，443
 - 域名：qcloud.rtc.qq.com

### 出现客户端错误："RtcError: ICE/DTLS Transport connection failed" 或 “RtcError: DTLS Transport connection timeout”该如何处理？
出现该错误说明 TRTC Web SDK 在建立媒体传输通道时失败，请检查防火墙配置。TRTC Web SDK 依赖以下端口进行数据传输，请将其加入防火墙白名单，配置完成后，您可以通过访问并体验 [官网 Demo](https://trtc-1252463788.file.myqcloud.com/web/demo/official-demo/index.html) 检查配置是否生效。
 - TCP 端口：8687
 - UDP 端口：8000，8800，843，443
 - 域名：qcloud.rtc.qq.com


### 出现10006 error 该如何处理？
如果出现"Join room failed result: 10006 error: service is suspended,if charge is overdue,renew it"，请确认您的实时音视频应用的服务状态是否为可用状态。
登录 [实时音视频控制台](https://console.cloud.tencent.com/rav)，单击您创建的应用，单击【帐号信息】，在帐号信息面板即可确认服务状态。
![](https://main.qcloudimg.com/raw/13c9b520ea333804cffb4e2c4273fced.png)


### 实时音视频 Web 端的截图功能如何实现？
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


快直播（LEB）是标准直播在超低延迟播放场景下的延伸，比传统直播协议延迟更低，为观众提供毫秒级的极致**直播观看**体验。
在您使用快直播服务前，建议您提前阅读 [快直播服务费用](https://cloud.tencent.com/document/product/267/39136)，清楚收费项目和价格，避免产生误解。

> ! 由于快直播使用的是 WebRTC 协议的低延迟特性，默认不支持 B 帧且音频编解码方式为 opus 编解码。为了保证快直播流可播放，当推流时带 B 帧或音频编码非 opus 编码时，云直播后台会自动发起转码去B帧并转码为 opus 编码，从而产生 [标准转码费用](https://cloud.tencent.com/document/product/267/39889)。

[](id:app)
## App 接入
### 接入说明
iOS、Android 上的应用可以通过集成移动直播 SDK 来实现 App 端上的直播推流/播放功能。

- **App 端直播推流**：支持采集摄像头画面或者采集手机界面，通过 RTMP 协议快速推流到云直播服务上，详情请参见 [摄像头推流](https://cloud.tencent.com/document/product/454/56591) 和 [录屏推流](https://cloud.tencent.com/document/product/454/56594)。
- **App 端直播播放**：支持 WebRTC 播放协议，配合快直播服务快速打造低延迟直播体验，详情请参见 [快直播拉流](https://cloud.tencent.com/document/product/454/55880)。

>? 移动直播 SDK 借助云直播、即时通信 IM、TRTC 等服务实现了多人音视频低延迟互联互通，可以实现多人连麦的互动效果，不参与连麦的观众仍通过直播服务观看，详情请参见 [直播连麦互动](https://cloud.tencent.com/document/product/454/52751)。

### Demo 体验
视频云工具包是腾讯云开源的一套完整的音视频服务解决方案，您可通过视频云工具包体验快直播毫秒级低延迟拉流能力。
<table>
  <tr>
    <th><div align="center">开发端</div></th>
    <th><div align="center">体验安装</div></th>
    <th><div align="center">推流演示（Android）</div></th>
    <th><div align="center">播放演示（Android）</div></th>
  </tr>
  <tr>
    <td >Android</td>
    <td style="text-align:center"><img width="150" src="https://main.qcloudimg.com/raw/6790ddaf4ffe4afd0ceb96b309a16496.png"> </td>
    <td rowspan="2">
      <div align="center">
        <img  width="200" src="https://sdk-liteav-1252463788.cos.ap-hongkong.myqcloud.com/doc/res/mlvb/picture/push.gif"/>
      </div>
    </td>
    <td rowspan="2">
      <div align="center">
        <img  width="200"  src="https://sdk-liteav-1252463788.cos.ap-hongkong.myqcloud.com/doc/res/mlvb/picture/pull.gif"/>
      </div>
    </td>
  </tr>
  <tr>
      <td >iOS</td>
    <td style="text-align:center"><img src="https://main.qcloudimg.com/raw/12c7da97cc910eda673cb19b66fc7cb3.png" width="150"></td>
  </tr>
</table>



[](id:web)
## Web 接入
### 接入说明
若您有网站需要进行直播推流和播放，推荐您使用以下方式进行接入：

- **Web 端直播推流**：基于浏览器通用的 WebRTC 标准进行设计和封装，通过引入代码片段就能实现在浏览器中进行直播推流，详情请参见 [WebRTC 推流](https://cloud.tencent.com/document/product/267/56505)。
> ! 
> - WebRTC 推流时音频编码方式为 opus 编码，若使用标准直播的播放协议（RTMP、FLV、HLS）进行播放时，为保证能正常观看，云直播后台会自动发起音频转码转为 aac 编码，从而会产生音频转码费用，详情请参见[音频转码费用说明](https://cloud.tencent.com/document/product/267/39889#a_trans)。（若只使用快直播则不会发起音频转码）
> - 使用 WebRTC 协议推流，每个推流域名默认限制**100路并发**推流数，如您需要超过此推流限制，可通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 的方式联系我们进行申请。
- **Web 端直播播放**：推荐您选用播放器 SDK 的 [TCPlayerLite](https://cloud.tencent.com/document/product/454/7503) ，支持在手机浏览器和 PC 浏览器上播放**快直播 WebRTC 协议**直播流，相比传统的直播协议延迟更低，为观众提供毫秒级的极致直播观看体验。
> ! 在不支持 WebRTC 的浏览器环境，传入播放器的 WebRTC 地址会自动进行协议转换来更好的支持媒体播放，在移动端浏览器会默认转换为 HLS，PC 端浏览器默认转换为 FLV。

### Demo 体验

- **Web 端直播推流**：可通过 **云直播控制台**>[Web 推流工具](https://console.cloud.tencent.com/live/tools/webpush) 进行测试 Web 端推流功能。
<img src="https://main.qcloudimg.com/raw/a47e0c7d8b40f94c13339265034b188a.png" width=600>
- **Web 端直播拉流**：可通过 [WebRTC Live Demo](https://tcplayer.vcube.tencent.com/webrtc-demo/index.html) 工具进行播放体验。
>?
>- Web 端直播推流和拉流均使用标准 WebRTC 协议，Web 端推流时不包含 B帧 ，且音频编码为 OPUS 音频格式，所以不会产生音频转码及去 B 帧转码费用。
>- WebRTC Live Demo 支持多清晰度功能，可在云直播控制台 **功能配置**>[**直播转码**](https://console.cloud.tencent.com/live/config/transcode) 配置高清-HD、标清-SD 的转码模板，将带有转码模板的 WebRTC 流地址填入 Demo 中对应的栏目后测试播放（如不需要测试此功能则只需要在 Demo 中填入一条 WebRTC 原始流即可）。
>- 直播转码操作指引及转码计费内容，请参见文档 [直播转码](https://cloud.tencent.com/document/product/267/20385)。
>
<img src="https://main.qcloudimg.com/raw/1f871aa2d45e2d3529cee8a98ef24673.png" width=600>

[](id:obs)
## OBS WebRTC 协议推流接入
WebRTC 协议推流主要用于视频云的快直播（超低延迟直播）推流，负责将采集的音视频画面或者视频文件通过 WebRTC 协议推送到直播服务器。下述内容主要介绍如何使用 OBS 工具，实现 webRTC 协议推流功能。

### 注意事项
- 目前对 OBS 的版本要求在26版本或版本以上。
- WebRTC 协议推流目前针对 OBS 只有 Windows 端的插件，想要实现在 mac 上进行 WebRTC 推流，可以使用 [Web接入](https://cloud.tencent.com/document/product/267/59017#web-.E6.8E.A5.E5.85.A5)。

[](id:set)
### 配置 OBS 插件
1. **配置插件数据**。
下载 [OBS 插件](https://mediacloud-76607.gzc.vod.tencent-cloud.com/TOBSWebRTC/Release/tencent_webrtc_plugin_20210628.zip)，把 data 文件里面的两个 `services.json` 和 `package.json` 文件，挪动到对应的 **obs-studio** > **rtmp-service** > **data** 目录进行覆盖。（`obs-studio` 默认安装在 C 盘，对应的目录为：`C:\Program Files\obs-studio\data\obs-plugins\rtmp-services`，请根据您的实际情况进行配置。）
![](https://main.qcloudimg.com/raw/03859054448cb140d31f2a57a60d82aa.png)  
2. **配置插件动态库**。
将 `obs-plugins\64bit` 中的 dll 和 pdb 文件，挪动到对应的 **obs-studio** > **obs-plugins** > **64bit** 目录下。（`obs-studio` 默认安装在 C 盘，对应的目录为：`C:\Program Files\obs-studio\obs-plugins\64bit`，请根据您的实际情况进行配置。）
![](https://main.qcloudimg.com/raw/0384bd8ebe63704fdb306a0620124ebf.png)   

[](id:push)
### 配置推流链接
[](id:push)
1. **生成 WebRTC 推流地址**。
	1. 登录腾讯云直播控制台，在 **直播工具箱**>**[地址生成器](https://console.cloud.tencent.com/live/addrgenerator/addrgenerator)** 生成推流地址，具体操作请参见 [地址生成器](https://cloud.tencent.com/document/product/267/35257)。
	2. 把生成的 `rtmp` 前缀修改成 `webrtc`，具体使用说明请参见 [自主拼装直播 URL](https://cloud.tencent.com/document/product/267/32720)。
	![](https://main.qcloudimg.com/raw/34924378812d1a36f04cfe1a2180e7a0.png)    
2. **配置 OBS 推流服务**。[](id:set_obs)
	1. 打开 OBS，您可通过底部工具栏的 **控件**>**设置** 按钮进入设置界面。
	2. 单击 **推流** 进入流设置页签，选择服务类型为 `Tenent webrtc`，服务器为 `Default`，串流密钥中输入之前生成的 [WebRTC 推流地址](#push)，并在后面拼接上 `&stopstream_api=https://webrtcpush.myqcloud.com/webrtc/v1/stopstream`。
	**串流密钥示例：**
```
webrtc://domain/AppName/StreamName?txSecret=xxx&txTime=xxx &stopstream_api=https://webrtcpush.myqcloud.com/webrtc/v1/stopstream 
```
如下图：
![](https://main.qcloudimg.com/raw/5c33acc958da82c01127ba2d4575ce1e.png)     

[](id:play)
### 快直播拉流播放
集成快直播 SDK 进行拉流播放，具体请参见 [快直播拉流](https://cloud.tencent.com/document/product/454/56879)。

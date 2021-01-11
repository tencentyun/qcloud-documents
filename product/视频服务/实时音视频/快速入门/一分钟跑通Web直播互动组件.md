[TWebLive](https://trtc.qcloud.com/tweblive/index.html#/) 即腾讯云 Web 直播互动组件，是腾讯云团队提供的一个新的 [SDK](https://www.npmjs.com/package/tweblive)，集成了 [腾讯云实时音视频 TRTC](https://cloud.tencent.com/product/trtc/)、[腾讯云即时通信 IM](https://cloud.tencent.com/product/im)、[腾讯云超级播放器 TCPlayer](https://cloud.tencent.com/document/product/454/7503)，覆盖了 Web 直播互动场景常见的功能（推流、开/关麦、开/关摄像头、微信分享观看、聊天点赞等），并封装了简单易用的 [API](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tweblive/TWebLive.html)，接入后可快速实现 Web 端推流、拉流以及实时聊天互动功能。

## 效果展示
![](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tweblivedemo/doc-assets/demo-official-website.gif)

## 组件优势

开发者接入此 SDK，可彻底替代 flash 推流方案，极大地降低 Web 推流、Web 低延时观看、CDN 观看以及实时聊天互动（或弹幕）的实现复杂度和时间成本，下面我们通过举例来进行说明。

<dx-tabs>
::: 推流
当需要推流时，创建 Pusher（推流）对象，最简单的推流仅需3步：
<dx-codeblock>
::: html html
<div id="pusherView" style="width:100%; height:auto;"></div>
<script>
// 1、创建 Pusher（推流）对象
let pusher = TWebLive.createPusher({ userID: 'your userID' });

// 2、设置渲染界面，且从麦克风采集音频，从摄像头采集视频（默认720p）
pusher.setRenderView({
  elementID: 'pusherView',
  audio: true,
  video: true
}).then(() => {
  // 3、填入 sdkappid roomid 等信息，推流
  // url 必须以 `room://` 开头
  let url = `room://sdkappid=${SDKAppID}&roomid=${roomID}&userid=${userID}&usersig=${userSig}&livedomainname=${liveDomainName}&streamid=${streamID}`;
  pusher.startPush(url).then(() => {
    console.log('pusher | startPush | ok');
  });
}).catch(error => {
  console.error('pusher | setRenderView | failed', error);
});
</script>
:::
</dx-codeblock>
:::
::: 拉流
当需要拉流播放时，创建 Player（播放器）对象，最简单的拉流仅需3步：

<dx-codeblock>
::: html html
<div id="playerView" style="width:100%; height:auto;"></div>
<script>
// 1、创建 Player（播放器）对象
let player = TWebLive.createPlayer();

// 2、设置渲染界面
player.setRenderView({ elementID: 'playerView' });

// 3、填入 flv hls 地址等信息，拉 CDN 流播放，此时 url 必须以 `https://` 开头
// 或 填入 sdkappid roomid 等信息，拉 WebRTC 低延时流播放，此时 url 必须以 `room://` 开头
let url = 'https://'
  + 'flv=https://200002949.vod.myqcloud.com/200002949_b6ffc.f0.flv' + '&' // 请替换成实际可用的播放地址
  + 'hls=https://200002949.vod.myqcloud.com/200002949_b6ffc.f0.m3u8' // 请替换成实际可用的播放地址

// let url = `room://sdkappid=${SDKAppID}&roomid=${roomID}&userid=${userID}&usersig=${userSig}`;
player.startPlay(url).then(() => {
  console.log('player | startPlay | ok');
}).catch((error) => {
  console.error('player | startPlay | failed', error);
});
</script>
:::
</dx-codeblock>
:::
::: 直播互动
当主播和观众需要聊天互动时，创建 IM（即时通信）对象，最简单的消息收发仅需3步：

<dx-codeblock>
::: javascript javascript
// 1、创建 IM（即时通信）对象并监听事件
let im = TWebLive.createIM({
  SDKAppID: 0 // 接入时需要将0替换为您的即时通信应用的 SDKAppID
});
// 监听 IM_READY IM_TEXT_MESSAGE_RECEIVED 等事件
let onIMReady = function(event) {
  im.sendTextMessage({ roomID: 'your roomID', text: 'hello from TWebLive' });
};
let onTextMessageReceived = function(event) {
  event.data.forEach(function(message) {
    console.log((message.from || message.nick) + ' : ', message.payload.text);
  });
};
// 接入侧监听此事件，然后可调用 SDK 发送消息等
im.on(TWebLive.EVENT.IM_READY, onIMReady);
// 收到文本消息，上屏
im.on(TWebLive.EVENT.IM_TEXT_MESSAGE_RECEIVED, onTextMessageReceived);

// 2、登录
im.login({userID: 'your userID', userSig: 'your userSig'}).then((imResponse) => {
  console.log(imResponse.data); // 登录成功
  if (imResponse.data.repeatLogin === true) {
    // 标识账号已登录，本次登录操作为重复登录
    console.log(imResponse.data.errorInfo);
  }
}).catch((imError) => {
  console.warn('im | login | failed', imError); // 登录失败的相关信息
});

// 3、加入直播间
im.enterRoom('your roomID').then((imResponse) => {
  switch (imResponse.data.status) {
    case TWebLive.TYPES.ENTER_ROOM_SUCCESS: // 加入直播间成功
      break;
    case TWebLive.TYPES.ALREADY_IN_ROOM: // 已经在直播间内
      break;
    default:
      break;
  }
}).catch((imError) => {
  console.warn('im | enterRoom | failed', imError); // 加入直播间失败的相关信息
});
:::
</dx-codeblock>
:::
</dx-tabs>

>? 为了进一步降低开发者的开发和人力成本，我们在 TWebLive SDK 的基础上，提供了同时适配 PC 和移动端浏览器的 [Demo](https://github.com/tencentyun/TWebLive)，并开源到了 Github。开发者 fork&clone 项目到本地，稍作修改即可把 Demo 跑起来，或者集成到自己的项目部署上线。

## 接入使用
### 注意事项
- 实时音视频应用与 IM 应用的 SDKAppID 一致，才能复用账号与鉴权。
- IM 应用针对文本消息，提供基础版本的安全打击能力，如果希望使用自定义不雅词功能，可以单击【升级】或在[【购买页】](https://buy.cloud.tencent.com/avc?position=1400399435)购买 [安全打击 - 专业版服务](https://cloud.tencent.com/document/product/269/11673#.E5.A2.9E.E5.80.BC.E6.9C.8D.E5.8A.A1.E8.B5.84.E8.B4.B9.3Ca-id.3D.22zz.22.3E.3C.2Fa.3E)。
- 本地计算 UserSig 的方式仅用于本地开发调试，请勿直接发布到线上，一旦 SECRETKEY 泄露，攻击者就可以盗用您的腾讯云流量。
- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。


[](id:step1)
### 步骤1：创建应用
<dx-tabs>
::: 基于TRTC
1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/trtc)。
2. 进入[【应用管理】](https://console.cloud.tencent.com/trtc/app)，单击【创建应用】，输入应用名称，单击【确定】创建一个实时音视频应用。
![](https://main.qcloudimg.com/raw/9a6003b3b96e7219d0718fde3cf83297.png)
>? 创建成功后， [即时通信 IM 控制台](https://console.cloud.tencent.com/im) 会同时自动创建 `SDKAppID` 相同的 IM 应用。
:::
::: 基于IM
1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)。
2. 单击【+添加新应用】，在【创建应用】对话框中输入您的应用名称，单击【确定】即可成功创建应用。
![](https://main.qcloudimg.com/raw/e6ec81c001d911f8d8295939610f97b6.png)
:::
</dx-tabs>

[](id:step2)
### 步骤2：获取 SDKAppID 及密钥
<dx-tabs>
::: 基于TRTC
1. 在 [应用列表](https://console.cloud.tencent.com/trtc/app) 里，选择目标应用，单击右侧的【应用信息】进入详情页。
3. 查看【应用信息】模块，单击复制按钮，记录 SDKAppID 信息。
![](https://main.qcloudimg.com/raw/33807f21a5591c4bde5e58911126d908.png)
4. 选择【快速上手】页签，查看【第二步 获取签发UserSig的密钥】标签，单击【复制密钥】。
![](https://main.qcloudimg.com/raw/ad738c0b26ac45afe404a013c4c280ab.png)

>? 若您需要开启 CDN 直播观看，可执行以下步骤：
>1. 在【应用管理】>【功能配置】中 [开启自动旁路推流](https://cloud.tencent.com/document/product/647/50768#open_bypass)。开启旁路推流功能后，TRTC 房间里的每一路画面都配备一路对应的播放地址。
![](https://main.qcloudimg.com/raw/b9846f4a7f5ce1e39b3450963e872c90.png)
>2. 在 [腾讯云直播控制台](https://console.cloud.tencent.com/live/) 配置播放域名并完成 CNAME 配置，详细操作请参见 [实现 CDN 直播观看](https://cloud.tencent.com/document/product/647/16826#.E4.BD.BF.E7.94.A8.E6.AD.A5.E9.AA.A4) 文档。
:::
::: 基于IM
应用创建完成后，可在控制台总览页查看新建应用的状态、业务版本、`SDKAppID`、创建时间以及到期时间。
1. 找到已创建的应用，单击目标应用卡片，进入应用的基础配置页面。
2. 在【基本信息】区域：
	- 单击复制按钮，记录 SDKAppID 信息。
	- 单击【显示密钥】，单击【复制】记录密钥信息。
![](https://main.qcloudimg.com/raw/e738005b56e826a4650e6e2862d617f0.png)
>!密钥信息为敏感信息，请妥善保管密钥信息，谨防泄露。
3. 查看【开通腾讯事实音视频服务】模块，单击【立即开通】，在弹框中单击【确认】开通腾讯云实时音视频服务。
![](https://main.qcloudimg.com/raw/3ebdce6918c5cc4c242161dd7e2e3a49.png)
:::
</dx-tabs>

>!
>- 本地计算 UserSig 的方式仅用于本地开发调试，请勿直接发布到线上，一旦您的 `SECRETKEY` 泄露，攻击者就可以盗用您的腾讯云流量。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。


[](id:step3)
### 步骤3：下载并配置 Demo 源码

1. 下载 [腾讯云 Web 直播互动组件 Demo 工程](https://github.com/tencentyun/TWebLive)。
2. 打开 `TWebLive/dist/debug/GenerateTestUserSig.js` 文件，并设置相关参数：<ul style="margin:0">
<li/>SDKAPPID：请设置为 <a href="#step2">步骤1</a> 中获取的实际应用 SDKAppID。
 <li/>SECRETKEY：请设置为 <a href="#step2">步骤2</a> 中获取的实际密钥信息。
 <li/>PLAYDOMAIN：CDN观看，配置播放域名。（如果不需要 CDN 直播观看，可略过此配置。）
 </ul>
 <img src="https://main.qcloudimg.com/raw/1f5dc0239e9c26d04ca905656e8bb854.png"/>
3. 集成 Demo 源码：
<dx-tabs>
::: 通过npm包安装
1. 在项目中通过 npm 安装最新版本的 `tim-js-sdk`、`trtc-js-sdk`、`tweblive`。
```javascript
npm install tim-js-sdk --save
npm install trtc-js-sdk --save
npm install tweblive --save
```
>? 如果项目已经集成有 `tim-js-sdk` 或 `trtc-js-sdk`，直接将其升级到最新版本即可。
2. 在项目中引入 tweblive。
```javascript
import TWebLive from 'tweblive'
Vue.prototype.TWebLive = TWebLive
```
:::
::: 通过script标签外链
如果需要通过 script 标签外链的方式引入，需要将 `tim-js.js`、`trtc.js`、`tweblive.js` 拷贝至项目中，按顺序引入。
```javascript
<script src="./trtc.js"></script>
<script src="./tim-js.js"></script>
<script src="./tweblive.js"></script>
```
:::
</dx-tabs>


[](id:step4)
### 步骤4：运行 Demo

使用 Chrome 浏览器打开 `dist` 目录下的 `index.html` 文件即可运行 Demo。
>!
>- 一般情况下体验 Demo 需要部署至服务器，通过 `https://域名/xxx` 访问，或者直接在本地搭建服务器，通过 `localhost:端口`访问。
>- 目前桌面端 Chrome 浏览器支持 TRTC 桌面浏览器 SDK 的相关特性比较完整，因此建议使用 Chrome 浏览器进行体验。
>- TWebLive 需要使用摄像头和麦克风采集音视频，在体验过程中您可能会收到来自 Chrome 浏览器的相关提示，单击【允许】。
![](https://main.qcloudimg.com/raw/1a2c1e7036720b11f921f8ee1829762a.png)



## 架构与平台支持
###  TWebLive 架构设计
![](https://main.qcloudimg.com/raw/503229b90d3714e5340e7c860ee50a8d.png)

### 支持平台
Web 推流和 Web 低延时观看用到了 WebRTC 技术。而 WebRTC 技术是由 Google 最先提出的，目前主要在桌面版 Chrome 浏览器、桌面版 Edge 浏览器、桌面版 Firefox 浏览器、桌面版 Safari 浏览器以及移动版的 Safari 浏览器上有较为完整的支持，其他平台（例如 Android 平台的浏览器）支持情况均比较差。

- 在移动端推荐使用 [小程序](https://cloud.tencent.com/document/product/647/32399) 解决方案，微信和手机 QQ 小程序均已支持，都是由各平台的 Native 技术实现，音视频性能更好，且针对主流手机品牌进行了定向适配。
- 如果您的应用场景主要为教育场景，那么教师端推荐使用稳定性更好的 [Electron](https://cloud.tencent.com/document/product/647/38549) 解决方案，支持大小双路画面，更灵活的屏幕分享方案以及更强大的弱网络恢复能力。

|  操作系统   |          浏览器类型          | 浏览器最低版本要求 | 接收（播放） | 发送（上麦） |
| :---------: | :--------------------------: | :----------------: | :----------: | :----------: |
|   Mac OS    |     桌面版 Safari 浏览器     |        11+         |     支持     |     支持     |
|   Mac OS    |     桌面版 Chrome 浏览器     |        56+         |     支持     |     支持     |
|   Mac OS    |    桌面版 Firefox 浏览器     |        56+         |     支持     |     支持     |
|   Mac OS    |      桌面版 Edge 浏览器      |        80+         |     支持     |     支持     |
|   Windows   |     桌面版 Chrome 浏览器     |        56+         |     支持     |     支持     |
|   Windows   | 桌面版 QQ 浏览器（极速内核） |       10.4+        |     支持     |     支持     |
|   Windows   |    桌面版 Firefox 浏览器     |        56+         |     支持     |     支持     |
|   Windows   |      桌面版 Edge 浏览器      |        80+         |     支持     |     支持     |
| iOS 11.1.2+ |     移动版 Safari 浏览器     |        11+         |     支持     |     支持     |
| iOS 12.1.4+ |         微信内嵌网页         |         -          |     支持     |    不支持    |
|   Android   |       移动版 QQ 浏览器       |         -          |    不支持    |    不支持    |
|   Android   |       移动版 UC 浏览器       |         -          |    不支持    |    不支持    |
|   Android   |   微信内嵌网页（TBS 内核）   |         -          |     支持     |     支持     |
|   Android   |  微信内嵌网页（XWEB 内核）   |         -          |     支持     |    不支持    |

>! 由于 H.264 版权限制，华为系统的 Chrome 浏览器和以 Chrome WebView 为内核的浏览器均不支持 TRTC 桌面浏览器端 SDK 的正常运行。


## 常见问题
<dx-accordion>
::: 1.\s查看密钥时只能获取公钥和私钥信息，要如何获取密钥？
TRTC SDK 6.6 版本（2019年08月）开始启用新的签名算法 HMAC-SHA256。在此之前已创建的应用，需要先升级签名算法才能获取新的加密密钥。
:::
::: 2.\s出现客户端错误：“RtcError:\sno\svalid\sice\scandidate\sfound”该如何处理？
出现该错误说明 TRTC 桌面浏览器 SDK 在 STUN 打洞失败，请根据环境要求检查防火墙配置。
:::
::: 3.\s出现客户端错误：“RtcError:\sICE/DTLS\sTransport\sconnection\sfailed”或\s“RtcError:\sDTLS\sTransport\sconnection\stimeout”该如何处理？
出现该错误说明 TRTC 桌面浏览器 SDK 在 STUN 打洞失败，请根据环境要求检查防火墙配置。
:::
::: 4.\s出现10006\serror\s该如何处理？
如果出现 `"Join room failed result: 10006 error: service is suspended,if charge is overdue,renew it"`。请登录 [实时音视频控制台](https://console.cloud.tencent.com/rav)，单击您创建的应用，单击【帐号信息】，在帐号信息面板请确认您的实时音视频应用的服务状态是否为可用状态。
![](https://main.qcloudimg.com/raw/13c9b520ea333804cffb4e2c4273fced.png)
:::
</dx-accordion>



## 结语

本文为您介绍了腾讯云新的 Web 直播互动组件：TWebLive，通过接入此 SDK，开发者可以快速轻便地实现 Web 推流、Web 低延时观看、CDN 观看以及实时聊天互动（或弹幕）等功能，能够很好替换传统的 flash 推流方案。

同时，提供详细的接入方案和 [在线 Demo](https://trtc.qcloud.com/tweblive/index.html#/) 供您体验。目前 TWebLive 在主流的桌面浏览器上也有较好的支持，在移动端支持小程序的解决方案。

后续，我们会提供更全方位的直播功能服务，例如：推流端支持屏幕分享、图片消息互动、观众端多线路观看（WebRTC 低延时线路和 CDN 线路）、主播观众连麦互动等功能。

参考资料：

- [TWebLive 接口手册](https://webim-1252463788.cos.ap-shanghai.myqcloud.com/tweblive/TWebLive.html)
- [在线 Demo](https://trtc.qcloud.com/tweblive/index.html#/)

## 相关文档

[折扣活动](https://cloud.tencent.com/document/product/269/46181)

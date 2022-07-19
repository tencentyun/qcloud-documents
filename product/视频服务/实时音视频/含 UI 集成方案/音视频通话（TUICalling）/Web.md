## 组件介绍
TUICalling 组件是一个开源的音视频组件，帮助您快速在您的桌面浏览器中集成**视频通话**功能，非常适合用于在线问诊，在线客服，远程理赔等场景中。
>?TUIKit 系列组件同时使用了腾讯云 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 两个基础 PaaS 服务，开通实时音视频后会同步开通即时通信 IM 服务。即时通信 IM 服务详细计费规则请参见 [即时通信 - 价格说明](https://cloud.tencent.com/document/product/269/11673)，TRTC 开通会默认关联开通 IM SDK 的体验版，仅支持100个 DAU。

![](https://qcloudimg.tencent-cloud.cn/raw/425c82df7e228557567fc491b7bb1084.png)

#### 其它平台
除了 Web 版的 TUICalling，我们同时也推出了 Android、iOS、小程序、Flutter、Uniapp 等平台的源代码，其中 Android、iOS 版本的 TUICalling 支持“来电提醒”功能。

>?
>- **除了 Web 版的 TUICalling，我们同时也推出了 Android、iOS、小程序、Flutter、Uniapp 等平台的源代码，其中 Android、iOS 版本的 TUICalling 支持“来电提醒”功能。** 
>- 如果您有任何咨询或建议，可以加入 QQ 群 **592465424** 一起交流。

## 组件集成
[](id:step1)
### 步骤一：获取 SdkAppId 和签名密钥
- 如果您还没有腾讯云账号，请注册一个腾讯云账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。然后跳转到 TRTC  管理控制台中的[应用管理](https://console.cloud.tencent.com/trtc/app)界面。
- 如果您的应用列表为空，可以点击**创建应用**按钮创建一个新的应用，之后单击**应用信息**，打开该应用管理界面。在该界面中寻找**快速上手**页签，就能够看到如下界面：
 <img src="https://qcloudimg.tencent-cloud.cn/raw/22d68577a7a54cc7cc7df2f078ffbff3.png" width="700">
- **SDKAppID**：TRTC 的应用 ID，用于业务隔离，即不同的 SDKAppID 的通话彼此不能互通；
- **Secretkey**：TRTC 的应用密钥，需要和 SDKAppID 配对使用，用于签出合法使用 TRTC 服务的鉴权用票据 UserSig，我们会在接下来的步骤五中用到这个 Key。

[](id:step2)
### 步骤二：下载并集成 TRTCCalling 组件
单击进入 [Github](https://github.com/tencentyun/TUICalling) ，选择克隆/下载代码，可参考 Web 目录下的实现。

>?
>- 从v0.6.0起，需要手动安装依赖 [trtc-js-sdk](https://www.npmjs.com/package/trtc-js-sdk) 和 [tim-js-sdk](https://www.npmjs.com/package/tim-js-sdk) 以及 [tsignaling](https://www.npmjs.com/package/tsignaling)。
>- 为了减小 trtc-calling-js.js 的体积，避免和接入侧已使用的 trtc-js-sdk 和 tim-js-sdk 以及 tsignaling 发生版本冲突，trtc-calling-js.js 将 trtc-js-sdk，tim-js-sdk，tsignaling 打包为外部依赖，在使用前您需要手动安装。

<dx-codeblock>
::: javascript javascript
// npm 方式安装
  npm install trtc-js-sdk --save

  npm install tim-js-sdk --save

  npm install tsignaling --save

  npm install trtc-calling-js --save
:::
</dx-codeblock>

<dx-codeblock>
::: html html
// 如果您需要通过 script 方式使用 trtc-calling-js，需要按顺序引入以下资源

<script src="./trtc.js"></script>
<script src="./tim-js.js"></script>
<script src="./tsignaling.js"></script>
<script src="./trtc-calling-js.js"></script>
:::
</dx-codeblock>

[](id:step3)
### 步骤三：创建 TRTCCalling 对象
创建 TRTCCalling 对象，并将 SDKAppID 参数设置为您自己的 SDKAppID。
```javascript
// 可参考 Web/src/trtc-calling/index.js
import TRTCCalling from 'trtc-calling-js';

let options = {
	SDKAppID: 0, // 接入时需要将0替换为您的 SDKAppID
	// 从v0.10.2起，新增 tim 参数
	// tim 参数适用于业务中已存在 TIM 实例，为保证 TIM 实例唯一性
	tim: tim
};
const trtcCalling = new TRTCCalling(options);
```

[](id:step4)
### 步骤四：进行登录与事件监听
```javascript
// 可参考 Web/src/components/login/index.vue
trtcCalling.login({
	userID,
	userSig,
});

// 可参考 Web/src/App.vue

export default {
	name: "App",
	components: {
	},
	async created() {
		this.initListener();
	},
	data() {
		return {};
	},
	destroyed() {
		this.removeListener();
	},
	methods: {
		initListener: function() {
			// 远端用户呼叫
			trtcCalling.on(trtcCalling.EVENT.INVITED, this.handleNewInvitationReceived);
			// 远端用户接听
			trtcCalling.on(trtcCalling.EVENT.USER_ACCEPT, this.handleUserAccept);
			// 远端用户拒绝
			trtcCalling.on(trtcCalling.EVENT.REJECT, this.handleInviteeReject);
			// ...
		},
		removeListener: function() {
			trtcCalling.off(trtcCalling.EVENT.INVITED, this.handleNewInvitationReceived);
			trtcCalling.off(trtcCalling.EVENT.USER_ACCEPT, this.handleUserAccept);
			trtcCalling.off(trtcCalling.EVENT.REJECT, this.handleInviteeReject);
		},
		handleNewInvitationReceived: async function(payload) {
		},
		handleUserAccept: function() {
		},
		handleInviteeReject: function() {
		}
	}
}
```

[](id:step5)
### 步骤五：实现 1v1 通话
- **主叫方：呼叫某个用户**
```javascript
// 可参考 Web/src/components/video-call/index.vue 或 Web/src/components/audio-call/index.vue
trtcCalling.call({
  userID,  //用户 ID
  type: 2, //通话类型，0-未知， 1-语音通话，2-视频通话
  timeout  //邀请超时时间, 单位 s(秒)
});
```
- **被叫方：接听新的呼叫**
```javascript
// 可参考 Web/src/App.vue handleAcceptCall 方法
// 接听
trtcCalling.accept();
// 拒绝
trtcCalling.reject()
```
- **展示远端的视频画面**
```javascript
trtcCalling.startRemoteView({
  userID, //远端用户 ID
  videoViewDomID //该用户数据将渲染到该 DOM ID 节点里
})
```
- **展示本地的预览画面**
```javascript
trtcCalling.startLocalView({
  userID, //本地用户 ID
  videoViewDomID //该用户数据将渲染到该 DOM ID 节点里
})
```
- **挂断**
```javascript
trtcCalling.hangup()
```

## 常见问题

### 为什么拨打不通，或者被踢下线？
组件暂不支持多实例登入，不支持**离线推送信令**功能，请您确认登入账号的唯一性。
> ?
> - **多实例**：一个 UserID 重复登入，或在不同端登入，将会引起信令的混乱。
> - **离线推送**：实例在线才能接收消息，实例离线时接收到的信令不会在上线后重新推送。

### 对于环境有哪些要求?
请使用最新版本的 Chrome 浏览器。目前桌面端 Chrome 浏览器支持 TRTC Web SDK 的相关特性比较完整，因此建议使用 Chrome 浏览器进行体验。

TRTCCalling 依赖以下端口进行数据传输，请将其加入防火墙白名单，配置完成后，您可以通过访问并体验 [官网 Demo](https://web.sdk.qcloud.com/component/trtccalling/demo/web/latest/index.html) 检查配置是否生效。
- **TCP 端口**：8687
- **UDP 端口**：8000，8080，8800，843，443，16285
- **域名**：qcloud.rtc.qq.com，具体请参见 [应对防火墙限制相关](https://cloud.tencent.com/document/product/647/34399)。
- **平台支持**：目前该方案支持如下平台
<table>
<thead><tr><th>操作系统</th><th>浏览器类型</th><th>浏览器最低版本要求</th></tr></thead>
<tbody><tr>
<td>Mac OS</td>
<td>桌面版 Safari 浏览器</td>
<td>11+</td>
</tr><tr>
<td>Mac OS</td>
<td>桌面版 Chrome 浏览器</td>
<td>56+</td>
</tr><tr>
<td>Mac OS</td>
<td>桌面版 Firefox 浏览器</td>
<td>56+</td>
</tr><tr>
<td>Mac OS</td>
<td>桌面版 Edge 浏览器</td>
<td>80+</td>
</tr><tr>
<td>Windows</td>
<td>桌面版 Chrome 浏览器</td>
<td>56+</td>
</tr><tr>
<td>Windows</td>
<td>桌面版 QQ 浏览器（极速内核）</td>
<td>10.4+</td>
</tr><tr>
<td>Windows</td>
<td>桌面版 Firefox 浏览器</td>
<td>56+</td>
</tr><tr>
<td>Windows</td>
<td>桌面版 Edge 浏览器</td>
<td>80+</td>
</tr>
</tbody></table>
>? 详细兼容性查询，具体请参见 [浏览器支持情况](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-05-info-browser.html)。同时，您可通过 [TRTC 检测页面](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) 在线检测。
- **URL 域名协议限制**：
<table>
<thead><tr><th>应用场景</th><th>协议</th><th>接收（播放）</th><th>发送（上麦）</th><th>屏幕分享</th><th>备注</th></tr></thead>
<tbody><tr>
<td>生产环境</td>
<td>HTTPS 协议</td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
<td>推荐</td>
</tr><tr>
<td>生产环境</td>
<td>HTTP 协议</td>
<td>支持</td>
<td>不支持</td>
<td>不支持</td>
<td>-</td>
</tr><tr>
<td>本地开发环境</td>
<td>http://localhost</td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
<td>推荐</td>
</tr><tr>
<td>本地开发环境</td>
<td>http://127.0.0.1</td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
<td>-</td>
</tr><tr>
<td>本地开发环境</td>
<td>http://[本机IP]</td>
<td>支持</td>
<td>不支持</td>
<td>不支持</td>
<td>-</td>
</tr><tr>
<td>本地开发环境</td>
<td align="left">file:///</td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
<td>-</td>
</tr>
</tbody></table>

## 相关文档
- [TUICalling Demo 源码](https://github.com/tencentyun/TUICalling)
- [TRTCCalling API 文档](https://web.sdk.qcloud.com/component/trtccalling/doc/web/zh-cn/TRTCCalling.html)
- [TRTCCalling Web 端相关问题](https://cloud.tencent.com/document/product/647/62484)

## TUICallEngine 说明 
TUICallEngine(无 UI 接口) 是一个开源的音视频组件，仅包含通话业务相关的逻辑 API，适用于 UI 定制性较高的场景，帮助您快速在您的桌面浏览器中集成**视频通话**功能，非常适合用于在线问诊，在线客服，远程理赔等场景中。


## 接入准备

腾讯云 TUICallEngine SDK 接入前，您需要：

- 在 [云通信控制台](https://console.cloud.tencent.com/im) 中创建一个云通信应用，并取得 SDKAppID。
- 在 [云通信控制台-基本配置](https://console.cloud.tencent.com/im-detail) 中，选择创建好的云通信应用，开通腾讯实时音视频服务。
  ![](https://qcloudimg.tencent-cloud.cn/raw/b0eb86680b0ecacd1e5ce4424e66252e.png)
	- **SDKAppID**：IM 的应用 ID，用于业务隔离，即不同的 SDKAppID 的通话彼此不能互通。
	- **Secretkey**：IM 的应用密钥，需要和 SDKAppID 配对使用，用于签出合法使用 IM 服务的鉴权用票据 UserSig，我们会在接下来的 [步骤五](TODO: 文档缺少步骤5) 中用到这个 Key。
  

## 接入示例
通过集成 TUICallEngine，您可以通过对方 userId 直接拨打一个 1v1 通话，也可以以 C2C 的方式实现群组通话。

[](id:step1)
### 步骤一：导入 SDK 到项目中
需要手动安装依赖 [trtc-js-sdk](https://www.npmjs.com/package/trtc-js-sdk) 和 [tim-js-sdk](https://www.npmjs.com/package/tim-js-sdk) 以及 [tsignaling](https://www.npmjs.com/package/tsignaling)。
- **NPM 集成**[](id:NPM)
```javascript
// 为了减小 tuicallengine.js 的体积，避免和接入侧已使用的 trtc-js-sdk 和 tim-js-sdk 以及 tsignaling 发生版本冲突
// trtc-js-sdk 和 tim-js-sdk 以及 tsignaling 不再被打包到 tuicallengine.js，在使用前您需要手动安装依赖。

npm i trtc-js-sdk --save
npm i tim-js-sdk --save
npm i tsignaling --save
npm i tuicall-engine-webrtc --save

import { TUICallEngine, TUICallEvent, TUICAllType } from "tuicall-engine-webrtc"
```
- **Script 集成**[](id:Script)
```javascript
// 如果您通过 script 方式使用 trtc-calling-js，需要按顺序先手动引入 trtc.js
<script src="./trtc.js"></script>

// 接着手动引入 tim-js.js
<script src="./tim-js.js"></script>

// 然后手动引入 tsignaling.js
<script src="./tsignaling.js"></script>

// 最后再手动引入 tuicallengine.js
<script src="./tuicall-engine-webrtc.js"></script>

const { TUICallEngine, TUICallEvent, TUICAllType } = window['tuicall-engine-webrtc']
```

[](id:step2)
### 步骤二：创建 TUICallEngine 对象
```javascript
let options = {
  SDKAppID: 0, // 接入时需要将0替换为您的云通信应用的 SDKAppID
  // tim 参数适用于业务中已存在 TIM 实例，为保证 TIM 实例唯一性
  tim: tim
};
let tuiCallEngine = TUICallEngine.createInstance(options);
```

[](id:step3)
### 步骤三：进行登录与事件监听
```javascript
tuiCallEngine.login({
    userID,
    userSig,
});
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
            tuiCallEngine.on(TUICallEvent.INVITED, this.handleNewInvitationReceived);
            // 远端用户接听
            tuiCallEngine.on(TUICallEvent.USER_ACCEPT, this.handleUserAccept);
            // 远端用户拒绝
            tuiCallEngine.on(TUICallEvent.REJECT, this.handleInviteeReject);
            // ...
        },
        removeListener: function() {
            tuiCallEngine.off(TUICallEvent.INVITED, this.handleNewInvitationReceived);
            tuiCallEngine.off(TUICallEvent.USER_ACCEPT, this.handleUserAccept);
            tuiCallEngine.off(TUICallEvent.REJECT, this.handleInviteeReject);
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

[](id:step4)
### 步骤四：实现 1v1 通话
- 主叫方：呼叫某个用户
```javascript
tuiCallEngine.call({
		userID,  //用户 ID
		type: 2, //通话类型，0-未知， 1-语音通话，2-视频通话
		timeout  //邀请超时时间, 单位 s(秒)
});
```
- 被叫方：接听新的呼叫
```javascript
// 接听
tuiCallEngine.accept();
// 拒绝
tuiCallEngine.reject()
```
- 展示远端的视频画面
```javascript
tuiCallEngine.startRemoteView({
		userID, //远端用户 ID
		videoViewDomID //该用户数据将渲染到该 DOM ID 节点里
})
```
- 展示本地的预览画面
```javascript
tuiCallEngine.startLocalView({
		userID, //本地用户 ID
		videoViewDomID //该用户数据将渲染到该 DOM ID 节点里
})
```
- 挂断
```javascript
tuiCallEngine.hangup()
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
- **域名**：qcloud.rtc.qq.com，具体请参见 [应对防火墙限制相关](https://cloud.tencent.com/document/product/647/34399)
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

- [TUICallEngine API 文档](https://web.sdk.qcloud.com/component/trtccalling/doc/web/zh-cn/TRTCCalling.html)
- [TUICallEngine Web 端相关问题](https://cloud.tencent.com/document/product/647/62484)
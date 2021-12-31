本文介绍如何实现一套可以在浏览器上运行的语音通话解决方案，文章分成两个部分：
- 第一部分：介绍如何开通服务并跑通我们提供的演示 Demo。
- 第二部分：介绍如何使用 TRTCCalling 组件快速搭建自己的语音通话功能。

## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | -  | &#10003;  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。


## 环境要求
请使用最新版本的 Chrome 浏览器。目前桌面端 Chrome 浏览器支持 TRTC Web SDK 的相关特性比较完整，因此建议使用 Chrome 浏览器进行体验。

TRTCCalling 依赖以下端口进行数据传输，请将其加入防火墙白名单，配置完成后，您可以通过访问并体验 [官网 Demo](https://web.sdk.qcloud.com/component/trtccalling/demo/web/latest/index.html) 检查配置是否生效。
  - TCP 端口：8687
  - UDP 端口：8000，8080，8800，843，443，16285
  - 域名：qcloud.rtc.qq.com
具体请参见 [应对防火墙限制相关](https://cloud.tencent.com/document/product/647/34399)。

## 平台支持
目前该方案支持如下平台：

| 操作系统 |          浏览器类型          | 浏览器最低版本要求 |
| :------: | :--------------------------: | :----------------: |
|  Mac OS  |     桌面版 Safari 浏览器     |        11+         |
|  Mac OS  |     桌面版 Chrome 浏览器     |        56+         |
|  Mac OS  |    桌面版 Firefox 浏览器     |        56+         |
|  Mac OS  |      桌面版 Edge 浏览器      |        80+         |
| Windows  |     桌面版 Chrome 浏览器     |        56+         |
| Windows  | 桌面版 QQ 浏览器（极速内核） |       10.4+        |
| Windows  |    桌面版 Firefox 浏览器     |        56+         |
| Windows  |      桌面版 Edge 浏览器      |        80+         |

>? 详细兼容性查询，具体请参见 [浏览器支持情况](https://web.sdk.qcloud.com/trtc/webrtc/doc/zh-cn/tutorial-05-info-browser.html)。同时，您可通过 [TRTC 检测页面](https://web.sdk.qcloud.com/trtc/webrtc/demo/detect/index.html) 在线检测。


## URL 域名协议限制
| 应用场景     | 协议             | 接收（播放） | 发送（上麦） | 屏幕分享 | 备注 |
| ------------ | :--------------- | :----------- | ------------ | -------- | ---- |
| 生产环境     | HTTPS 协议        | 支持         | 支持         | 支持     | 推荐 |
| 生产环境     | HTTP 协议         | 支持         | 不支持       | 不支持   |   -   |
| 本地开发环境 | http://localhost | 支持         | 支持         | 支持     | 推荐 |
| 本地开发环境 | http://127.0.0.1 | 支持         | 支持         | 支持     |   -   |
| 本地开发环境 | http://[本机IP]  | 支持         | 不支持       | 不支持   |   -   |
| 本地开发环境 | file:///         | 支持         | 支持         | 支持     |  -    |

## 跑通测试 Demo

[](id:step1)
### 步骤1：创建新的应用
1. [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 实名认证。
2. 登录实时音视频控制台，选择 **开发辅助>[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)**。
3. 输入应用名称，例如 `TestTRTC` ，单击 **创建**。

[](id:step2)
### 步骤2：下载 SDK 和 Demo 源码
1. 根据实际业务需求下载 SDK 及配套的 Demo 源码。
2. 下载完成后，单击 **已下载，下一步**。
![](https://main.qcloudimg.com/raw/a4f5a2ac1f49d67b4c6968d8b22cdeb0.png)

[](id:step3)
### 步骤3：配置 Demo 工程文件
1. 进入修改配置页，根据您下载的源码包，选择相应的开发环境。
2. 找到并打开 `Web/js/debug/GenerateTestUserSig.js` 文件。
3. 设置 `GenerateTestUserSig.js` 文件中的相关参数：
  <ul><li>SDKAPPID：默认为0，请设置为实际的 SDKAppID。</li>
  <li>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</li></ul> 
  <img src="https://main.qcloudimg.com/raw/99c0bf40a7b6267c5c398336a97f3335.png">
4. 粘贴完成后，单击 **已复制粘贴，下一步** 即创建成功。
5. 编译完成后，单击 **回到控制台概览** 即可。


>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

[](id:step4)
### 步骤4：运行 Demo
1. 在 Demo 目录下依次输入如下命令：
```
npm install
npm run serve
```
2. 启动 Chrome 浏览器中打开链接 `http://localhost:8080/` ，如果一切正常，Demo 运行界面如图所示：
![](https://main.qcloudimg.com/raw/03cc2aa792a0f885fe070eb86ada4ce4.png)
3. 输入用户 userid，单击 **登录**，并选择 **语音通话**：
![](https://main.qcloudimg.com/raw/c1243956fe79d1361f3f0329e85f41d9.png)
4. 输入呼叫用户 userid，单击 **呼叫**：
![](https://main.qcloudimg.com/raw/cdb27d63a75c83e99452923d5da05999.png)
5. 即可进行语音通话：
![](https://main.qcloudimg.com/raw/37f1e43114ea2ab6dc4b419d60002d09.png)


## 搭建自己的语音通话
### 步骤1：集成 TRTCCalling 组件
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

### 步骤2：创建 TRTCCalling 对象
创建 TRTCCalling 对象，并将 SDKAppID 参数设置为您自己的 SDKAppID。
```javascript
import TRTCCalling from 'trtc-calling-js';


let options = {
  SDKAppID: 0, // 接入时需要将0替换为您的 SDKAppID
  // 从v0.10.2起，新增 tim 参数
  // tim 参数适用于业务中已存在 TIM 实例，为保证 TIM 实例唯一性
  tim: tim
};
const trtcCalling = new TRTCCalling(options);
```

### 步骤3：完成登录
```javascript
trtcCalling.login({
  userID,
  userSig,
});
```

### 步骤4：实现 1v1 通话
- **主叫方：呼叫某个用户**
```javascript
trtcCalling.call({
  userID,  //用户 ID
  type: 1, //通话类型，0-未知， 1-语音通话，2-视频通话
  timeout  //邀请超时时间, 单位 s(秒)
});
```
- **被叫方：接听新的呼叫**
```javascript
// 接听
trtcCalling.accept();
//拒绝
trtcCalling.reject()
```
- **挂断**
```javascript
trtcCalling.hangup()
```

## 常见问题

#### 为什么拨打不通，或者被踢下线？
组件暂不支持多实例登入，不支持**离线推送信令**功能，请您确认登入账号的唯一性。
> ?
> - **多实例**：一个 UserID 重复登入，或在不同端登入，将会引起信令的混乱。
> - **离线推送**：实例在线才能接收消息，实例离线时接收到的信令不会在上线后重新推送。
更多常见问题，请参见 [TRTCCalling Web 相关问题](https://cloud.tencent.com/document/product/647/62484)。

## 技术咨询[](id:QQ)

了解更多详情您可以 QQ 咨询：646165204 <dx-tag-link link="#QQ" tag="技术支持"></dx-tag-link>


## 参考文档
- [TRTCCalling web 官网体验](https://web.sdk.qcloud.com/component/trtccalling/demo/web/latest/index.html#/login)
- [TRTCCalling npm](https://www.npmjs.com/package/trtc-calling-js)
- [TRTCCalling web demo 源码](https://github.com/tencentyun/TRTCSDK/tree/master/Web/TRTCScenesDemo/trtc-calling-web)
- [TRTCCalling web API](https://web.sdk.qcloud.com/component/trtccalling/doc/web/zh-cn/TRTCCalling.html)
- [TRTCCalling web 相关问题](https://cloud.tencent.com/document/product/647/62484)

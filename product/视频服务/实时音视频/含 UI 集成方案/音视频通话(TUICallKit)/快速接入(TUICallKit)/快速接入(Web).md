
本文将介绍如何用最短的时间完成帮助您快速在桌面浏览器中集成**视频通话**功能，跟随本文档，您将在最终得到一个完整的视频通话功能。

## 环境准备
[](id:bversion)
### 1. 对浏览器版本要求
请使用最新版本的 Chrome 浏览器进行体验，本文档中所对接的组件对当前主流的桌面浏览器的支持情况如下：
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


### 2. 对网络环境的要求

在使用 TUICallKit 时，用户可能因防火墙限制导致无法正常进行音视频通话，请参考 [应对防火墙限制相关](https://cloud.tencent.com/document/product/647/34399) 将相应端口及域名添加至防火墙白名单中。

### 3. 对网站域名协议的要求
出于对用户安全、隐私等问题的考虑，浏览器限制网页在 HTTPS 协议下才能正常使用本文档中所对接组件的全部功能。为确保生产环境中的用户能够顺畅体验产品功能，请将您的网站部署在 **https://** 协议的域名下。
>! 本地开发可以通过 `http://localhost` 或者 `file://` 协议进行访问。

URL 域名及协议支持情况请参考如下表格：

<table>
<thead><tr><th>应用场景</th><th>协议</th><th>接收（播放）</th><th>发送（推流）</th><th>屏幕分享</th><th>备注</th></tr></thead>
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
<td>本地调试环境</td>
<td>http://localhost</td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
<td>推荐</td>
</tr><tr>
<td>本地调试环境</td>
<td>http://127.0.0.1</td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
<td>-</td>
</tr><tr>
<td>本地调试环境</td>
<td>http://[本机IP]</td>
<td>支持</td>
<td>不支持</td>
<td>不支持</td>
<td>-</td>
</tr><tr>
<td>本地调试环境</td>
<td align="left">file:///</td>
<td>支持</td>
<td>支持</td>
<td>支持</td>
<td>-</td>
</tr>
</tbody></table>


[](id:step1)
##  步骤一：开通服务

TUICallKit 是基于腾讯云 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 和 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 两项付费 PaaS 服务构建出的音视频通信组件。您可以按照如下步骤开通相关的服务并体验 7 天的免费试用服务：

1. 登录到 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)，单击**创建新应用**，在弹出的对话框中输入您的应用名称，并单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/1105c3c339be4f71d72800fe2839b113.png)
2. 单击刚刚创建出的应用，进入**基本配置**页面，并在页面的右下角找到**开通腾讯实时音视频服务**功能区，单击**免费体验**即可开通 TUICallKit 的 7 天免费试用服务。如果需要正式应用上线，可以单击 [**前往加购**](https://buy.cloud.tencent.com/avc) 即可进入购买页面。
<img width="640" src="https://qcloudimg.tencent-cloud.cn/raw/99a6a70e64f6877bad9406705cbf7be1.png">
>? IM 音视频通话能力针对不同的业务需求提供了差异化的付费版本供您选择，您可以在 [IM 购买页](https://buy.cloud.tencent.com/avc) 了解包含功能并选购您适合的版本。
3. 在同一页面找到 **SDKAppID** 和**密钥**并记录下来，它们会在后续中被用到。
![](https://qcloudimg.tencent-cloud.cn/raw/e435332cda8d9ec7fea21bd95f7a0cba.png)
    - SDKAppID：IM 的应用 ID，用于业务隔离，即不同的 SDKAppID 的通话彼此不能互通；
    - SecretKey：IM 的应用密钥，需要和 SDKAppID 配对使用，用于签出合法使用 IM 服务的鉴权用票据 UserSig，我们会在接下来的步骤五中用到这个 Key。

<dx-alert infotype="alarm" title="<b>友情提示：</b>">
单击**免费体验**以后，部分之前使用过 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 服务的用户会提示：
```
[-100013]:TRTC service is  suspended. Please check if the package balance is 0 or the Tencent Cloud accountis in arrears
```
因为新的 IM 音视频通话能力是整合了腾讯云[实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 两个基础的 PaaS 服务，所以当 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 的免费额度（10000分钟）已经过期或者耗尽，就会导致开通此项服务失败，这里您可以单击 [TRTC 控制台](https://console.cloud.tencent.com/trtc/app)，找到对应 SDKAppID 的应用管理页，示例如图，开通后付费功能后，再次**启用应用**即可正常体验音视频通话能力。
<img width=800px src="https://qcloudimg.tencent-cloud.cn/raw/f74a13a7170cf8894195a1cae6c2f153.png" />
</dx-alert>


[](id:step2)
## 步骤二：下载并导入 SDK 到项目中
要实现视频通话功能，您需要集成腾讯云的几个 web sdk 组件（trtc、im、tsignaling、tuicall-engine-web），您可以使用如下两种集成方式中的任何一种：

### 集成方式一：NPM 集成

安装依赖地址： 
- [trtc-js-sdk](https://www.npmjs.com/package/trtc-js-sdk) 
- [tim-js-sdk](https://www.npmjs.com/package/tim-js-sdk) 
- [tsignaling](https://www.npmjs.com/package/tsignaling)
- [tuicall-engine-webrtc](https://www.npmjs.com/package/tuicall-engine-webrtc)

```javascript
npm i trtc-js-sdk --save
npm i tim-js-sdk --save
npm i tsignaling --save
npm i tuicall-engine-webrtc --save

import { TUICallEngine, TUICallEvent } from "tuicall-engine-webrtc"
```
### 集成方式二：Script 集成

Script 下载地址：
- [trtc-js-sdk](https://web.sdk.qcloud.com/component/trtccalling/download/trtc-js-sdk.zip) 
- [tim-js-sdk](https://web.sdk.qcloud.com/component/trtccalling/download/tim-js-sdk.zip) 
- [tsignaling](https://web.sdk.qcloud.com/component/trtccalling/download/tsignaling.zip)
- [tuicall-engine-webrtc](https://web.sdk.qcloud.com/component/trtccalling/download/tuicall-engine-webrtc.zip)

```javascript
// 如果您通过 script 方式使用 tuicall-engine-webrtc.js，需要按顺序先手动引入 trtc.js
<script src="./trtc.js"></script>

// 接着手动引入 tim-js.js
<script src="./tim-js.js"></script>

// 然后手动引入 tsignaling.js
<script src="./tsignaling.js"></script>

// 最后再手动引入 tuicall-engine-webrtc.js
<script src="./tuicall-engine-webrtc.js"></script>

const { TUICallEngine, TUICallEvent } = window['tuicall-engine-webrtc'];
```

[](id:step3)
## 步骤三：创建 TUICallEngine 对象
TUICallEngine 是完成音视频通话的核心组件，我们需要先创建出该组件的一个对象。
在创建组件时，有两个关键参数需要您注意：
- **SDKAppID**：您会在[步骤一](#step1) 中的最后一步找到这个数字。
- **tim**：本文档中的组件依赖腾讯云 tim 组件完成消息通信功能，如果您的项目中已经使用了腾讯云的 tim 组件，为了避免重复登录导致的状态混乱问题，可以将您的项目中已经创建出来的 tim 组件实例通过该参数传递给 TUICallEngine 组件。如果项目中没有 tim 组件实例，传空值即可。

```javascript
let options = {
    SDKAppID: 0, // 接入时需要将 0 替换为您的云通信应用的 SDKAppID
    tim: null     // tim 参数适用于业务中已存在 TIM 实例，为保证 TIM 实例唯一性
};
let tuiCallEngine = TUICallEngine.createInstance(options);
```


[](id:step4)
## 步骤四：登录组件
获得 TUICallEngine 组件实例后，还需要完成组件的登录，才能发起视频通话功能：

```javascript
tuiCallEngine.login({  
    userID: "jane",
    userSig: "xxxxx",
}).then( res => {
    // success
}).catch( error => {
    console.warn('login error:', error);
});
```
**参数说明**：
这里详细介绍一下 login 的关键参数：
- userID：当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。
- userSig：使用步骤一中获取的 SecretKey 对 SDKAppID、userID 等信息进行加密，就可以得到 UserSig，它是一个鉴权用的票据，用于腾讯云识别当前用户是否能够使用 TRTC 的服务。您可以通过控制台中的 [**辅助工具**](https://console.cloud.tencent.com/im/tool-usersig) 生成一个临时可用的 UserSig。
- 更多信息请参见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。

> ! 这个步骤也是目前我们收到的反馈最多的步骤，常遇到的问题有如下几个：
> 1. SDKAppID 设置错误，国内站的 SDKAppID 一般是以 140 开头的 10 位整数。
> 2. UserSig 被错配成了加密密钥（SecretKey），UserSig 是用 SecretKey 把 SDKAppID、UserID 以及过期时间等信息加密得来的，而不是直接把 SecretKey 配置成 UserSig。
> 3. UserID 被设置成 “1”、“123”、“111” 等简单字符串，由于 **TRTC 不支持同一个 UserID 多端登录**，所以在多人协作开发时，形如 “1”、“123”、“111” 这样的 UserID 很容易被您的同事占用，导致登录失败，因此我们建议您在调试的时候设置一些辨识度高的 UserID。

>! Github 中的示例代码使用了 genTestUserSig 函数在本地计算 userSig 是为了更快地让您跑通当前的接入流程，但该方案会将您的 SecretKey 暴露在 Web 的代码当中，这并不利于您后续升级和保护您的 SecretKey，所以我们强烈建议您将 UserSig 的计算逻辑放在服务端进行，并由 Web 在每次使用 TUICallKit 组件时向您的服务器请求实时计算出的 UserSig。

[](id:step5)
## 步骤五：拨打视频通话
**1对1视频通话**：您可以调用 TUICallEngine 中的 **call** 接口拨打1对1视频通话。
```javascript
tuiCallEngine.call({
    userID: "xxx",  // 用户 ID
    type: 2, // 通话类型，0-未知， 1-语音通话，2-视频通话
}).then( res => {
    // success
}).catch( error => {
    console.warn('call error:', error);
});
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userID | String | 被邀请方 userID|
| type | Number | 0-未知， 1-语音通话，2-视频通话|

**群内多人通话**：您可以调用 TUICallEngine 中的 **groupCall** 接口，在群内发起多人音视频通话。
```javascript
tuiCallEngine.groupCall({
    userIDList: ['user1', 'user2'], 
    type: 1, 
    groupID: 'IM群组 ID'
}).then( res => {
    // success
}).catch( error => {
    console.warn('groupCall error:', error);
});
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| userIDList | Array | 邀请列表 |
| type | Number | 0-未知， 1-语音通话，2-视频通话 |
| groupID | String | IM 群组 ID |

>? 
>1. 群组的创建详见：[ IM 群组管理](https://cloud.tencent.com/document/product/269/75394#.E5.88.9B.E5.BB.BA.E7.BE.A4.E7.BB.84) ，或者您也可以直接使用 [IM TUIKit](https://cloud.tencent.com/document/product/269/37059)，一站式集成聊天、通话等场景。
>2. TUICallKit 目前还不支持发起非群组的多人视频通话，如果您有此类需求，欢迎反馈： [TUICallEngine 需求收集表](https://wj.qq.com/s2/10622244/b9ae/)。

[](id:step6)
## 步骤六：接听通话
通过 TUICallEngine 中的 **on** 接口，可以监听通话相关的事件，并绑定对应的处理函数：
```javascript
tuiCallEngine.on(TUICallEvent.INVITED, () => {   
    // 收到视频通话的邀请
});     
tuiCallEngine.on(TUICallEvent.USER_ACCEPT, () => { 
    // 对方接听了您发出的通话邀请
}); 
tuiCallEngine.on(TUICallEvent.REJECT, () => {
    // 对方拒绝了您发出的通话邀请
});      
```

当收到了视频通话邀请之后，您可以调用 TUICallEngine 中的 **accept** 接口来接听通话消息。 
```javascript
// 接听通话
tuiCallEngine.accept().then( res => {
    // success
}).catch( error => {
    console.warn('accept error:', error);
});      
```

[](id:step7)
## 步骤七：显示视频画面
您可以通过 TUICallEngine 中的 **startLocalView** 接口来显示本地的摄像头画面，示例代码如下：
```javascript
// 本地视频画面
tuiCallEngine.startLocalView({
    userID: "xxx", // 本地用户的 userID
    videoViewDomID: "local-xxx" // 用于显示摄像头画面的 DOM 节点
}).then( res => {
    // success
}).catch( error => {
    console.warn('startLocalView error:', error);
})
```

您可以通过 TUICallEngine 中的 **startRemoteView** 接口来显示远端的视频画面，但请在收到 `TUICallEvent.USER_ENTER` 事件后再调用 **startRemoteView** 比较合适：
```javascript
tuiCallEngine.on(TUICallEvent.USER_ENTER, () => {
    // 远端视频画面
    tuiCallEngine.startRemoteView({
        userID: "xxx", // 远端用户 ID
        videoViewDomID: "remote-xxx" // 用于显示对方视频画面的 DOM 节点
    }).then( res => {
        // success
    }).catch( error => {
        console.warn('startRemoteView error:', error);
    })
})
```

[](id:step8)
## 步骤八：更多特性

### 1. 设置昵称&头像
如果您需要自定义昵称或头像，可以使用该接口进行更新。
```javascript
tuiCallEngine.setSelfInfo({
    nickName: 'video', 
    avatar: 'http(s)://url/to/image.jpg'
}).then( res => {
    // success
}).catch( error => {
    console.warn('setSelfInfo error:', error);
});
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| nickName | String | 要设置的用户昵称 |
| avatar | String | 头像链接 |

> ! 因为用户隐私限制，非好友之间的通话，被叫的昵称和头像更新可能会有延迟，一次通话成功后就会顺利更新。


### 2. 切换摄像头和麦克风设备
如果您需要切换摄像头（麦克风）为外接摄像头或其他，可通过该接口实现。
```javascript
let cameras = [];
// 获取摄像头列表
tuiCallEngine.getDeviceList('camera').then( devices => {  
    cameras = devices;
}).catch(error => {
    console.warn('getDeviceList error:', error);
});
// 切换设备
tuiCallEngine.switchDevice({
    deviceType: 'video', 
    deviceId: cameras[0].deviceId
}).then( res => {
    // success
}).catch( error => {
    console.warn('switchDevice error:', error);
});
```

| 参数 | 类型 | 含义 |
|-----|-----|-----|
| deviceType | string |  video-摄像头，audio-麦克风|
| deviceId | string | 需要切换的设备 ID|


### 3. 设置视频画面的质量
如果您需要调整视频画面的质量，可以调用 TUICallEngine 中的 **setVideoQuality** 接口来实现：
```javascript
const profile = '720p';
tuiCallEngine.setVideoQuality(profile).then( res => {
    // success
}).catch( error => {
    console.warn('setVideoQuality error:', error);
});
```

|视频 Profile | 分辨率（宽 x 高）|
|-----|-----|
|480p|640 x 480|
|720p|1280 x 720|
|1080p|1920 x 1080|


>! 该方法需在 call、groupCall、accept 之前设置，之后设置不生效。

## 相关链接
- [Github Demo 地址](https://github.com/tencentyun/TUICalling)
- [Web 端常见问题](https://cloud.tencent.com/document/product/647/78769)
- [TUICallEngine API 概览](https://cloud.tencent.com/document/product/647/78756)
- [TUICallEngine API 文档](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/TUICallEngine.html)

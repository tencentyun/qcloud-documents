
本文将介绍如何用最短的时间完成帮助您快速在桌面浏览器中集成**视频通话**功能，跟随本文档，您将在最终得到一个完整的视频通话功能。

## 环境准备
请使用最新版本的 Chrome 浏览器。目前桌面端 Chrome 浏览器支持 TRTC Web SDK 的相关特性比较完整，因此建议使用 Chrome 浏览器进行体验。

TUICallEngine 依赖以下端口进行数据传输，请将其加入防火墙白名单。

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


[](id:step1)
##  步骤一：开通服务

TUICallKit 是基于腾讯云 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 和 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 两项付费 PaaS 服务构建出的音视频通信组件。您可以按照如下步骤开通相关的服务并体验 7 天的免费试用服务：

1. 登录到 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)，单击**创建新应用**，在弹出的对话框中输入您的应用名称，并单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/1105c3c339be4f71d72800fe2839b113.png)
2. 单击刚刚创建出的应用，进入**基本配置**页面，并在页面的右下角找到**开通腾讯实时音视频服务**功能区，单击**免费体验**即可开通 TUICallKit 的 7 天免费试用服务。
![](https://qcloudimg.tencent-cloud.cn/raw/667633f7addfd0c589bb086b1fc17d30.png)
1. 在同一页面找到 **SDKAppID** 和**密钥**并记录下来，它们会在后续中被用到。
![](https://qcloudimg.tencent-cloud.cn/raw/e435332cda8d9ec7fea21bd95f7a0cba.png)
    - SDKAppID：IM 的应用 ID，用于业务隔离，即不同的 SDKAppID 的通话彼此不能互通；
    - Secretkey：IM 的应用密钥，需要和 SDKAppID 配对使用，用于签出合法使用 IM 服务的鉴权用票据 UserSig，我们会在接下来的步骤五中用到这个 Key。


[](id:step2)
## 步骤二：下载并导入 SDK 到项目中
通过集成 TUICallEngine，您可以通过对方 userID 直接拨打一个 1v1 通话，也可以实现群内通话。

### NPM 集成

安装依赖地址： 
- [trtc-js-sdk](https://www.npmjs.com/package/trtc-js-sdk) 
- [tim-js-sdk](https://www.npmjs.com/package/tim-js-sdk) 
- [tsignaling](https://www.npmjs.com/package/tsignaling)
- [tuicall-engine-web](https://www.npmjs.com/package/tuicall-engine-web)

```javascript
npm i trtc-js-sdk --save
npm i tim-js-sdk --save
npm i tsignaling --save
npm i tuicall-engine-web --save

import { TUICallEngine, TUICallEvent } from "tuicall-engine-web"
```
### Script 集成

下载地址：
- [trtc-js-sdk](https://web.sdk.qcloud.com/component/trtccalling/download/trtc-js-sdk.zip) 
- [tim-js-sdk](https://web.sdk.qcloud.com/component/trtccalling/download/tim-js-sdk.zip) 
- [tsignaling](https://web.sdk.qcloud.com/component/trtccalling/download/tsignaling.zip)
- [tuicall-engine-web](https://web.sdk.qcloud.com/component/trtccalling/download/tuicall-engine-web.zip)

```javascript
// 如果您通过 script 方式使用 tuicall-engine-web.js，需要按顺序先手动引入 trtc.js
<script src="./trtc.js"></script>

// 接着手动引入 tim-js.js
<script src="./tim-js.js"></script>

// 然后手动引入 tsignaling.js
<script src="./tsignaling.js"></script>

// 最后再手动引入 tuicall-engine-web.js
<script src="./tuicall-engine-web.js"></script>

const { TUICallEngine, TUICallEvent } = window['tuicall-engine-web']
```

[](id:step3)
## 步骤三：创建 TUICallEngine 对象
```javascript
let options = {
  SDKAppID: 0, // 接入时需要将 0 替换为您的云通信应用的 SDKAppID
  tim: tim     // tim 参数适用于业务中已存在 TIM 实例，为保证 TIM 实例唯一性
};
let tuiCallEngine = TUICallEngine.createInstance(options);
```
**参数说明**：
- SDKAppID：在步骤一中的最后一步中您已经获取到，这里不再赘述。
- tim：非必填项，若您没有，将会由内部代码自动创建。

[](id:step4)
## 步骤四：登录
```javascript
tuiCallEngine.login({  // 登陆事件
    userID: "xxx",
    userSig: "xxx",
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
> 1. SDKAppID 设置错误，国内站的 SDKAppID 一般是以140开头的10位整数；
> 2. UserSig 被错配成了加密密钥（Secretkey），UserSig 是用 SecretKey 把 SDKAppID、UserID 以及过期时间等信息加密得来的，而不是直接把 Secretkey 配置成 UserSig。
> 3. UserID 被设置成“1”、“123”、“111”等简单字符串，由于 **TRTC 不支持同一个 UserID 多端登录**，所以在多人协作开发时，形如 “1”、“123”、“111” 这样的 UserID 很容易被您的同事占用，导致登录失败，因此我们建议您在调试的时候设置一些辨识度高的 UserID。

>! Github 中的示例代码使用了 genTestUserSig 函数在本地计算 userSig 是为了更快地让您跑通当前的接入流程，但该方案会将您的 SecretKey 暴露在 Web 的代码当中，这并不利于您后续升级和保护您的 SecretKey，所以我们强烈建议您将 UserSig 的计算逻辑放在服务端进行，并由 Web 在每次使用 TUICallKit 组件时向您的服务器请求实时计算出的 UserSig。

[](id:step5)
## 步骤五：事件监听

```javascript
// 绑定事件
tuiCallEngine.on(TUICallEvent.INVITED, () => {    // 呼叫远端用户
    // 处理监听到 INVITED 事件的回调
    // ...
});     
tuiCallEngine.on(TUICallEvent.USER_ACCEPT, () => { // 远端用户接听
    // 处理监听到 USER_ACCEPT 事件的回调
    // ...
}); 
tuiCallEngine.on(TUICallEvent.REJECT, () => {      // 远端用户拒绝
    // 处理监听到 REJECT 事件的回调
    // ...
});      
// ...
```

[](id:step6)
## 步骤六：实现 1v1 通话
- 主叫方：呼叫某个用户
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


- 被叫方：接听新的呼叫
    ```javascript
    // 接听通话
    tuiCallEngine.accept().then( res => {
        // success
    }).catch( error => {
        console.warn('accept error:', error);
    });
    ```
- 展示视频画面
  
  展示视频画面需要在监听到 `USER_ENTER`事件后处理。
    ```javascript
    tuiCallEngine.on(TUICallEvent.USER_ENTER, () => {
        // 远端视频画面
        tuiCallEngine.startRemoteView({
            userID: "xxx", // 远端用户 ID
            videoViewDomID: "remote-xxx" // 该用户数据将渲染到该 DOM ID 节点里
        }).then( res => {
            // success
        }).catch( error => {
            console.warn('startRemoteView error:', error);
        });
        // 本地视频画面
        tuiCallEngine.startLocalView({
            userID: "xxx", // 本地用户 ID
            videoViewDomID: "local-xxx" // 该用户数据将渲染到该 DOM ID 节点里
        }).then( res => {
            // success
        }).catch( error => {
            console.warn('startLocalView error:', error);
        });
    }); 
    ```
    | 参数 | 类型 | 含义 |
    |-----|-----|-----|
    | userID | String | 用户 ID|
    | videoViewDomID | String | 该用户数据将渲染到该 DOM ID 节点里|

- 挂断
    ```javascript
    tuiCallEngine.hangup().then( res => {
        // success
    }).catch( error => {
        console.warn('hangup error:', error);
    });
    ```


[](id:step7)
## 步骤七：更多特性

### 一. 设置昵称&头像
如果您需要自定义昵称或头像，可以使用该接口进行更新。
```javascript
tuiCallEngine.setSelfInfo({
  nickName: 'video', 
  avatar:'http(s)://url/to/image.jpg'
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

### 二. 群内视频通话
通过调用 groupCall 接口并指定通话类型和被叫方的 userID，就可以发起群内的视频或语音通话。
```javascript
tuiCallEngine.groupCall({
  userIDList: ['user1', 'user2'], 
  type: 1, 
  groupID: 'IM群组 ID', 
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
>2. TUICallKit 目前还不支持发起非群组的多人视频通话，如果您有此类需求，欢迎反馈： [TUICallEngine 需求收集表]()。

### 三. 切换摄像头和麦克风设备
如果您需要切换摄像头（麦克风）为外接摄像头或其他，可通过该接口实现。
```javascript
let cameras = [];
// 获取摄像头列表
tuiCallEngine.getDeviceList('camera').then((devices)=>{  
 cameras = devices;
}).catch(error => {
  console.warn('getDeviceList error:', error)
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
| deviceId | string | 需要切换的设备ID|


### 四. 设置视频质量
如果您需要设置视频质量，使视频更加流畅，可通过该接口实现。


```javascript
const profile = '720p';
tuiCallEngine.setVideoQuality(profile)
.then( res => {
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
- [Web 端常见问题](https://tcloud-doc.isd.com/document/product/647/78769)
- [TUICallEngine API 概览](https://tcloud-doc.isd.com/document/product/647/78756)
- [TUICallEngine API 文档](https://web.sdk.qcloud.com/component/trtccalling/doc/TUICallEngine/web/TUICallEngine.html)
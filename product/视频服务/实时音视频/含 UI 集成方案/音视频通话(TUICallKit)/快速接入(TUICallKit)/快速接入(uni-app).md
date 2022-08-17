本文将介绍如何用最短的时间完成 TUICallKit 组件的接入，跟随本文档，您将在一个小时的时间内完成如下几个关键步骤，并最终得到一个包含完备 UI 界面的视频通话功能。

## 环境准备
- 建议使用最新的 HBuilderX 编辑器 。
- iOS 9.0 或以上版本且支持音视频的 iOS 设备，暂不支持模拟器。
- Android 版本不低于 4.1 且支持音视频的 Android 设备，暂不支持模拟器。如果为真机，请开启**允许调试**选项。最低兼容 Android 4.1（SDK API Level 16），建议使用 Android 5.0 （SDK API Level 21）及以上版本。
- iOS/Android 设备已经连接到 Internet。

[](id:step1)
## 步骤一：开通服务
TUICallKit 是基于腾讯云 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 和 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 两项付费 PaaS 服务构建出的音视频通信组件。您可以按照如下步骤开通相关的服务并体验 7 天的免费试用服务。

1. 登录到 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)，单击**创建新应用**，在弹出的对话框中输入您的应用名称，并单击**确定**。
<img width="640" src="https://qcloudimg.tencent-cloud.cn/raw/1105c3c339be4f71d72800fe2839b113.png">
2. 单击刚刚创建出的应用，进入**基本配置**页面，并在页面的右下角找到**开通腾讯实时音视频服务**功能区，单击**免费体验**即可开通 TUICallKit 的 7 天免费试用服务。如果需要正式应用上线，可以单击 [**前往加购**](https://buy.cloud.tencent.com/avc) 即可进入购买页面。
<img width="640" src="https://qcloudimg.tencent-cloud.cn/raw/99a6a70e64f6877bad9406705cbf7be1.png">
>? IM 音视频通话能力针对不同的业务需求提供了差异化的付费版本供您选择，您可以在 [IM 购买页](https://buy.cloud.tencent.com/avc) 了解包含功能并选购您适合的版本。
3. 在同一页面找到 **SDKAppID** 和**密钥**并记录下来，它们会在后续的 [步骤四：登录 TUI 组件](#step4) 中被用到。
<img width="640" src="https://qcloudimg.tencent-cloud.cn/raw/e435332cda8d9ec7fea21bd95f7a0cba.png">

<dx-alert infotype="alarm" title="<b>友情提示：</b>">
单击**免费体验**以后，部分之前使用过 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 服务的用户会提示：
```
[-100013]:TRTC service is  suspended. Please check if the package balance is 0 or the Tencent Cloud accountis in arrears
```
因为新的 IM 音视频通话能力是整合了腾讯云[实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 和 [即时通信 IM](https://cloud.tencent.com/document/product/269/42440) 两个基础的 PaaS 服务，所以当 [实时音视频 TRTC](https://cloud.tencent.com/document/product/647/16788) 的免费额度（10000分钟）已经过期或者耗尽，就会导致开通此项服务失败，这里您可以单击 [TRTC 控制台](https://console.cloud.tencent.com/trtc/app)，找到对应 SDKAppID 的应用管理页，示例如图，开通后付费功能后，再次**启用应用**即可正常体验音视频通话能力。
<img width=800px src="https://qcloudimg.tencent-cloud.cn/raw/f74a13a7170cf8894195a1cae6c2f153.png" />
</dx-alert>

[](id:step2)
## 步骤二：导入插件 
1. **购买 uni-app 原生插件**
登录 [uni 原生插件市场](https://ext.dcloud.net.cn/plugin?id=9035)，在插件详情页中购买（免费插件也可以在插件市场0元购）。购买后才能够云端打包使用插件。**购买插件时请选择正确的 appid，以及绑定正确包名**。
![](https://qcloudimg.tencent-cloud.cn/raw/d270d9298975ee829ae9c8c405530765.png)
2. 使用自定义基座打包 uni 原生插件 （**请使用真机运行自定义基座**）
使用 uni 原生插件必须先提交云端打包才能生效，购买插件后在应用的 `manifest.json` 页面的 **App原生插件配置** 项下单击**选择云端插件**，选择**腾讯云原生音视频插件**。
![](https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/TencentCloud-TUICallKit.png)
直接云端打包后无法打 log，无法排查问题，需要自定义基座调试原生插件。
>! 
>- 自定义基座不是正式版，真正发布时，需要再打正式包。使用自定义基座是无法正常升级替换 APK 的。
>- 请尽量不要使用本地插件，插件包超过自定义基座的限制，可能导致调试收费。


[](id:step3)
## 步骤三：在 vue 页面中引入原生插件
使用 `uni.requireNativePlugin` 的 API 在 vue 页面中引入原生插件，参数为插件的 ID。
```javascript
const TUICallKit = uni.requireNativePlugin('TencentCloud-TUICallKit');
```

[](id:step4)
## 步骤四：登录 TUI 组件
在您的项目中添加如下代码，完成 TUICallKit 组件的登录。这个步骤异常关键，因为只有在登录成功后才能正常使用 TUICallKit 的各项功能，故请您耐心检查相关参数是否配置正确。
```javascript
const options = {
  SDKAppID: 0,
  userID: 'your userID',
  userSig: 'your userSig',
};
TUICallKit.login(options, (res) => {
  if (res.code === 0) {
    console.log('login success');
  } else {
    console.log(`login failed, error message = ${res.msg}`);
  }
});
```

**参数说明**
这里详细介绍一下 login 函数中所需要用到的几个关键参数：
- **SDKAppID**：在 [步骤一](#step1) 中的最后一步中您已经获取到，这里不再赘述。
- **userID**：当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。
- **userSig**：使用 [步骤一](#step1) 中获取的 SecretKey 对 SDKAppID、userID 等信息进行加密，就可以得到 userSig，它是一个鉴权用的票据，用于腾讯云识别当前用户是否能够使用 TRTC 的服务。您可以通过控制台中的 [**辅助工具**](https://console.cloud.tencent.com/im/tool-usersig) 生成一个临时可用的 userSig。
- 更多信息请参见 [如何计算及使用 userSig](https://cloud.tencent.com/document/product/647/17275)。

> !
- **这个步骤也是目前我们收到的开发者反馈最多的步骤，常见问题如下**：
 - sdkAppId 设置错误，国内站的 SDKAppID 一般是以140开头的10位整数。
 - userSig 被错配成了加密密钥（Secretkey），userSig 是用 SecretKey 把 sdkAppId、userId 以及过期时间等信息加密得来的，而不是直接把 Secretkey 配置成 userSig。
 - userId 被设置成“1”、“123”、“111”等简单字符串，由于 **TRTC 不支持同一个 UserID 多端登录**，所以在多人协作开发时，形如 “1”、“123”、“111” 这样的 userId 很容易被您的同事占用，导致登录失败，因此我们建议您在调试的时候设置一些辨识度高的 userId。
- Github 中的示例代码使用了 genTestUserSig 函数在本地计算 userSig 是为了更快地让您跑通当前的接入流程，但该方案会将您的 SecretKey 暴露在 App 的代码当中，这并不利于您后续升级和保护您的 SecretKey，所以我们强烈建议您将 userSig 的计算逻辑放在服务端进行，并由 App 在每次使用 TUICallKit 组件时向您的服务器请求实时计算出的 userSig。


[](id:step5)
## 步骤五：拨打通话
### 1对1视频通话
通过调用 TUICallKit 的 call 函数并指定通话类型和被叫方的 userID，就可以发起语音或者视频通话。
```javascript
const options = {
  userID: 'chard',
  callMediaType: 1, // 语音通话(callMediaType = 1)、视频通话(callMediaType = 2)
};
TUICallKit.call(options, (res) => {
  if (res.code === 0) {
    console.log('call success');
  } else {
    console.log(`call failed, error message = ${res.msg}`);
  }
});
```

### 群内视频通话
通过调用 TUICallKit 的 groupCall 函数并指定通话类型和被叫方的 userID，就可以发起群内的视频或语音通话。
```javascript
const options = {
  groupID: 'myGroup',
  userIDList: ['chard', 'linda', 'rg'],
  callMediaType: 1, // 语音通话(callMediaType = 1)、视频通话(callMediaType = 2)
};
TUICallKit.groupCall(options, (res) => {
  if (res.code === 0) {
    console.log('groupCall success');
  } else {
    console.log(`groupCall failed, error message = ${res.msg}`);
  }
});
```

[](id:step6)
## 步骤六：接听通话
收到来电请求后，TUICallKit 组件会自动唤起来电提醒的接听界面。

[](id:step7)
## 步骤七：更多特性
### 一、设置昵称&头像
如果您需要自定义昵称或头像，可以使用如下接口进行更新。
```javascript
const options = {
  nickName: '',
  avatar: ''
}
TUICallKit.setSelfInfo(options, (res) => {
  if (res.code === 0) {
    console.log('setSelfInfo success');
  } else {
    console.log(`setSelfInfo failed, error message = ${res.msg}`);
  }
});
```
> ! 因为用户隐私限制，非好友之间的通话，被叫的昵称和头像更新可能会有延迟，一次通话成功后就会顺利更新。

### 二、悬浮窗功能
如果您的业务需要开启悬浮窗功能，您可以在 TUICallKit 组件初始化时调用以下接口开启该功能。
```javascript
const enable = true;
TUICallKit.enableFloatWindow(enable);
```

### 三、通话状态监听
如果您的业务需要 **监听通话的状态**，例如：异常、通话开始、结束等，可以监听以下事件：
```javascript
const TUICallingEvent = uni.requireNativePlugin('globalEvent');
TUICallingEvent.addEventListener('onError', (res) => {
  console.log('onError', JSON.stringify(res));
});
TUICallingEvent.addEventListener('onCallReceived', (res) => {
  console.log('onCallReceived', JSON.stringify(res));
});
TUICallingEvent.addEventListener('onCallCancelled', (res) => {
  console.log('onCallCancelled', res);
});
TUICallingEvent.addEventListener('onCallBegin', (res) => {
  console.log('onCallBegin', JSON.stringify(res));
});
TUICallingEvent.addEventListener('onCallEnd', (res) => {
  console.log('onCallEnd', JSON.stringify(res));
});
```

### 四、自定义铃音
如果您需要自定义来电铃音，可以通过如下接口进行设置。
```javascript
const filePath = './**';
TUICallKit.setCallingBell(filePath, (res) => {
  if (res.code === 0) {
    console.log('setCallingBell success');
  } else {
    console.log(`setCallingBell failed, error message = ${res.msg}`);
  }
});
```

[](id:step8)
## 步骤八：本地调试和发布
 使用自定义基座开发调试 [TencentCloud-TUICallKit 插件](https://ext.dcloud.net.cn/plugin?id=9035) 后，不可直接将自定义基座 APK 作为正式版发布。
 应该重新提交云端打包（不能勾选“**自定义基座**”）生成正式版本。

## 实现案例
我们提供了**在线客服场景**的相关源码，建议您 [下载](https://ext.dcloud.net.cn/plugin?id=721) 并集成体验。该场景提供了示例客服群 + 示例好友的基础模板，实现功能包括：
- 支持发送文本消息、图片消息、语音消息、视频消息等常见消息。
- 支持双人语音、视频通话功能
- 支持创建群聊会话、群成员管理等。

<table>
<thead>
<tr>
<th style="text-align:center">Android 演示</th>
<th style="text-align:center">iOS 演示</th>
</tr>
</thead>
<tbody><tr>
<td ><img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/android-uniapp.gif"></td>
<td ><img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/ios-uniapp.gif"></td>
</tr>
</tbody></table>

## 技术咨询
了解更多详情您可 QQ 咨询：**309869925** (技术交流群)

## 相关文档
- [uni-app 原生音视频插件示例](https://github.com/tencentyun/TIMSDK/tree/master/uni-app/TUICallKit/TUICallKit-app)
- [uni-app TUIKit 源码](https://github.com/tencentyun/TIMSDK/tree/master/uni-app)
- [一分钟跑通 Demo (uni-app)](https://cloud.tencent.com/document/product/269/64506)
- [快速集成 uni-app TUIKit](https://cloud.tencent.com/document/product/269/64507)
- [TencentCloud-TUICallKit 插件](https://ext.dcloud.net.cn/plugin?id=9035)

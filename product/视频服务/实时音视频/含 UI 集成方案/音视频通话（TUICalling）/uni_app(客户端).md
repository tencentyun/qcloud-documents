## 组件介绍

TUICalling 插件是**腾讯云官方推出**的基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的插件，支持双人和多人音视频通话。插件提供了全套定制 UI，开发者仅需两个 API 可集成实现通话功能。TUICalling 同时支持 iOS、Web、小程序、Flutter、UniApp 等平台，基本功能如下图所示：
<table>
<tr><th>双人视频通话演示</th><th>多人视频通话演示</th>
 </tr>
<tr>
<td><img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-calling-call.gif"/ ></td>
<td><img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-calling-group.gif" ></td>
</tr>
</table>

## 组件集成

### 步骤一：导入插件 
1. **购买 uni-app 原生插件**：
登录 [uni 原生插件市场](https://ext.dcloud.net.cn/plugin?id=7097)，在插件详情页中购买（免费插件也可以在插件市场0元购）。购买后才能够云端打包使用插件。**购买插件时请选择正确的 appid，以及绑定正确包名**。
![](https://qcloudimg.tencent-cloud.cn/raw/d270d9298975ee829ae9c8c405530765.png)
2. 使用自定义基座打包 uni 原生插件 （**请使用真机运行自定义基座**）。
使用 uni 原生插件必须先提交云端打包才能生效，购买插件后在应用的 `manifest.json` 页面的 **App原生插件配置** 项下单击**选择云端插件**，选择**腾讯云原生音视频插件**。
![](https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-app-21.png)
直接云端打包后无法打 log，无法排查问题，需要自定义基座调试原生插件。

>!
>- 自定义基座不是正式版，真正发布时，需要再打正式包。使用自定义基座是无法正常升级替换 APK 的。
>- 请尽量不要使用本地插件，插件包超过自定义基座的限制，可能导致调试收费


### 步骤二：在 vue 页面中引入原生插件
使用 `uni.requireNativePlugin` 的 API 在 vue 页面中引入原生插件，参数为插件的 ID。
```javascript
const TUICalling = uni.requireNativePlugin("TUICallingUniPlugin-TUICallingModule");
```

### 步骤三：获取 SdkAppId 和签名密钥
- **SDKAppID**：**TRTC 应用 ID**，如果您未开通腾讯云 TRTC 服务，可进入 [腾讯云实时音视频控制台](https://console.cloud.tencent.com/trtc/app)，创建一个新的 TRTC 应用后，单击**应用信息**，SDKAppID 信息如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/3d6ebfa2a1e4ae5d3af3ecd564fb1463.png)
- **SecretKey**：**TRTC 应用密钥**，和 SDKAppId 对应，进入 [TRTC 应用管理](https://console.cloud.tencent.com/trtc/app) 后，SecretKey 信息如上图所示。
- **userId**：当前用户的 ID，字符串类型，长度不超过32字节，不支持使用特殊字符，建议使用英文或数字，可结合业务实际账号体系自行设置。
- **userSig**：根据 SDKAppId、userId，Secretkey 等信息计算得到的安全保护签名，您可以单击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的 UserSig，也可以参照我们的 [TUICalling示例工程](https://github.com/TencentCloud/TIMSDK/blob/master/uni-app/TUICalling/TUICalling-app/debug/GenerateTestUserSig.js)自行计算，更多信息见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。

### 步骤四：在 vue 页面中实现功能
1. 登录并填写您的应用 sdkAppID 等信息。
```javascript
TUICalling.login({
sdkAppID: 0, 
userID: 'your userID',
userSig: 'your userSig'
})
```

2. 发起音视频通话。
	- 发起双人通话：
```javascript
TUICalling.call({ userID: 'user1', type: 1 })
```
	- 发起群通话：
```javascript
TUICalling.groupCall({ userIDList: ['user1'，'user2'], type: 1 })
```
3. 登出。
```javascript
TUICalling.logout()
```

### 步骤五：本地调试和发布
 使用自定义基座开发调试 [uni-app 原生插件](https://ask.dcloud.net.cn/article/35412) 后，不可直接将自定义基座 APK 作为正式版发布。
 应该重新提交云端打包（不能勾选“**自定义基座**”）生成正式版本。

## 实现案例
我们提供了**在线客服场景**的相关源码，建议您 [下载](https://github.com/tencentyun/TIMSDK/tree/master/uni-app/TUIKit) 并集成体验。该场景提供了示例客服群 + 示例好友的基础模板，实现功能包括：
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
- [uni-app 原生音视频插件示例](https://github.com/tencentyun/TIMSDK/tree/master/uni-app/TUICalling/TUICalling-app)
- [uni-app TUIKit 源码](https://github.com/tencentyun/TIMSDK/tree/master/uni-app)
- [一分钟跑通 Demo (uni-app)](https://cloud.tencent.com/document/product/269/64506)
- [快速集成 uni-app TUIKit](https://cloud.tencent.com/document/product/269/64507)


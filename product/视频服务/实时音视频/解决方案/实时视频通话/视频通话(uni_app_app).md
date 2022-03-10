TUICalling 插件是**腾讯云官方推出**的基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的插件，支持双人和多人音视频通话。插件提供了全套定制 UI，开发者仅需两个 API 可集成实现通话功能。

## 效果展示
<table>
<tr><th>双人视频通话演示</th><th>多人视频通话演示</th>
 </tr>
<tr>
<td><img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-calling-call.gif"/ ></td>
<td><img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-calling-group.gif" ></td>
</tr>
</table>

## 应用场景
在线客服、在线面试、企业在线沟通、在线问诊、音视频社交等。

## 实现架构和支持平台
<img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-calling.png" height = "400"/>

## 支持平台
**Android** 和 **iOS** 端均支持。

## 快速跑通
[](id:run.step1)
### 步骤一：注册并创建 uni-app 账号
搭建 App 开发环境步骤如下：
1. 下载 [HBuilderX 编辑器 ](https://www.dcloud.io/hbuilderx.html)。
>!项目中 HBuilderX 目前使用的最新版本，如果此前下载过 HBuilderX，为保证开发环境统一请更新到最新版本。
2. [DCloud 开发者中心注册](https://dev.dcloud.net.cn/) 之后登录 HBuilderX 编辑器。

[](id:run.step2)
### 步骤二：创建应用并开通腾讯云服务
<dx-tabs>
::: 方式1：基于实时音视频
#### 步骤1：创建实时音视频 TRTC 应用
1. [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2Fdocument%2Fproduct%2F647%2F49327) 并开通 [实时音视频](https://console.cloud.tencent.com/trtc) 和 [即时通信](https://console.cloud.tencent.com/im) 服务。
2. 在 [实时音视频控制台](https://console.cloud.tencent.com/trtc) 单击 **应用管理 > 创建应用** 创建新应用。
   ![创建应用](https://main.qcloudimg.com/raw/34f87b8c0a817d8d3e49baac5b82a1fa.png)

#### 步骤2：获取 TRTC 密钥信息

1. 在 **应用管理 > 应用信息** 中获取 SDKAppID 信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/f7915fbbeb48518c2b25a413960f3432.png)
2. 在 **应用管理 > 快速上手** 中获取应用的 secretKey 信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/06d38bbdbaf43e1f2b444edae00019fa.png)

>?
>
>- 首次创建实时音视频应用的腾讯云账号，可获赠一个10000分钟的音视频资源免费试用包。
>- 创建实时音视频应用之后会自动创建一个 SDKAppID 相同的即时通信 IM 应用，可在 [即时通信控制台](https://console.cloud.tencent.com/im) 配置该应用的套餐信息。

:::
::: 方式2：基于即时通信\sIM
#### 步骤1：创建即时通信 IM 应用
1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)，单击 **创建新应用** 将弹出对话框。
![](https://qcloudimg.tencent-cloud.cn/raw/d40aa2432418dd6ea253dd3e6ffc06a6.png)
2. 输入您的应用名称，单击 **确认** 即可完成创建。
![](https://qcloudimg.tencent-cloud.cn/raw/7c09422c6ccf076e4eef814ae0c53dcc.png)
3. 在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) 总览页面查看新建应用的状态、业务版本、SDKAppID、创建时间以及到期时间。请记录 SDKAppID 信息。
4. 单击您已创建的 IM 应用，进入应用详情页完成登录设置：
	1.  在 **功能配置** > **登录与消息**页面，单击 **登录设置** 右侧的 **编辑**。
	2.  在弹出的登录设置对话框中，选择多端登录类型，设置 Web 端以及其他平台实例同时在线数量。
>!旗舰版选择多平台登录时，Web 端可同时在线个数最多为10个。Android、iPhone、iPad、Windows、Mac 平台可同时在线设备个数最多为3个。
>
![](https://qcloudimg.tencent-cloud.cn/raw/f9b9270f5c69d51390d391b370d36501.png)
	3. 单击 **确定** 保存设置。
>!请务必开启多终端。

#### 步骤2：获取 IM 密钥并开通实时音视频服务
1. 在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) 总览页单击您创建完成的即时通信 IM 应用，随即跳转至该应用的基础配置页。在 **基本信息** 区域，单击 **显示密钥**，复制并保存密钥信息。
![](https://main.qcloudimg.com/raw/030440f94a14cd031476ce815ed8e2bc.png)
>!请妥善保管密钥信息，谨防泄露。
2. 在该应用的基础配置页，开通腾讯云实时音视频服务。
![](https://main.qcloudimg.com/raw/1c2ce5008dad434d9206aabf0c07fd04.png)
:::
</dx-tabs>

[](id:run.step3)
### 步骤三：下载并配置 TUICalling 源码
1. 根据您的实际业务需求，下载 SDK 及配套的 [Demo 源码](https://gitee.com/cloudtencent/TIMSDK/tree/master/uni-app/TUICalling)。
```
# 命令行执行
git clone https://gitee.com/cloudtencent/TIMSDK

# 进入 uni-app TUICalling 项目
cd TIMSDK/uni-app/TUICalling/TUICalling-app
```
2. 将 uni-app 中 TUICalling 工程文件，导入自己的 HBuilderX 工程。具体请参见官方文档 [uni-app 开发](https://uniapp.dcloud.io/quickstart-hx)。
3. 设置 GenerateTestUserSig 文件中的相关参数。
	- 找到并打开 `debug/GenerateTestUserSig.js` 文件。
	- 设置 `GenerateTestUserSig.js` 文件中的相关参数。
		<ul><li>SDKAPPID：默认为0，请设置为实际的 SDKAppID。</li>
		<li>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</li></ul> 
<img src="https://main.qcloudimg.com/raw/575902219de19b4f2d4595673fa755d4.png">

>!
>- 本文提到的生成 `UserSig` 的方案是在客户端代码中配置 `SECRETKEY`，该方法中 `SECRETKEY` 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 uni-app 和功能调试**。
>- 正确的 `UserSig` 签发方式是将 `UserSig` 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 `UserSig` 时由您的 App 向业务服务器发起请求获取动态 `UserSig`。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

[](id:run.step4)
### 步骤四：导入插件 
1. **购买 uni-app 原生插件**：
登录 [uni 原生插件市场](https://ext.dcloud.net.cn/plugin?id=7097)，在插件详情页中购买（免费插件也可以在插件市场0元购）。购买后才能够云端打包使用插件。**购买插件时请选择正确的 appid，以及绑定正确包名**。
![](https://qcloudimg.tencent-cloud.cn/raw/d270d9298975ee829ae9c8c405530765.png)
2. 使用自定义基座打包 uni 原生插件 （**请使用真机运行自定义基座**）。
使用 uni 原生插件必须先提交云端打包才能生效，购买插件后在应用的 `manifest.json` 页面的 **App原生插件配置** 项下单击**选择云端插件**，选择需要打包的插件。
![](https://img-cdn-tc.dcloud.net.cn/uploads/article/20190416/1b5297e695ad1536ddafe3c834e9c297.png)
直接云端打包后无法打 log，不利于排错，所以一般先打一个自定义基座，把需要的原生插件打到真机运行基座里，然后在本地写代码调用调试。

>!
>- 自定义基座不是正式版，真正发布时，需要再打正式包。使用自定义基座是无法正常升级替换 APK 的。
>- 请尽量不要使用本地插件，插件包超过自定义基座的限制，可能导致调试收费

[](id:run.step5)
### 步骤五：编译运行
具体操作请参见 [uni-app 运行](https://uniapp.dcloud.io/quickstart-hx?id=%e8%bf%90%e8%a1%8cuni-app)。

[](id:run.step6)
### 步骤六：打包发布
使用自定义基座开发调试 uni-app 原生插件后，不可直接将自定义基座 APK 作为正式版发布。
应该重新提交云端打包（不能勾选“**自定义基座**”）生成正式版本。

[](id:integrated)
## 集成方法
[](id:in_step1)
### 步骤一：购买并将原生插件导入自己的项目
1. 购买并将 [原生插件](https://ext.dcloud.net.cn/plugin?id=7097)。
2. 将原生插件导入自己的项目中，具体使用方法请参见 [原生插件使用指南](https://ask.dcloud.net.cn/article/35412)。

[](id:in_step2)
### 步骤二：在 vue 页面中引入原生插件
使用 `uni.requireNativePlugin` 的 API 在 vue 页面中引入原生插件，参数为插件的 ID。
```javascript
const TUICalling = uni.requireNativePlugin("TUICallingUniPlugin-TUICallingModule");
```

[](id:in_step3)
### 步骤三：在 vue 页面中实现功能
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
TUICalling.call({userID: 'user1', type: 1})
```
	- 发起群通话：
```javascript
TUICalling.groupCall({userIDList: ['user1'，'user2'], type: 1})
```
3. 登出。
```javascript
TUICalling.logout()
```

[](id:in_step4)
### 步骤四：本地调试和发布
 使用自定义基座开发调试 [uni-app 原生插件](https://ask.dcloud.net.cn/article/35412) 后，不可直接将自定义基座 APK 作为正式版发布。
 应该重新提交云端打包（不能勾选“**自定义基座**”）生成正式版本。

## 实现案例
我们提供了**在线客服场景**的相关源码，建议您 [下载](https://github.com/tencentyun/TIMSDK/tree/master/uni-app/TUIKit) 并集成体验。该场景提供了示例客服群 + 示例好友的基础模板，实现功能包括：
- 支持发送文本消息、图片消息、语音消息、视频消息等常见消息。
- 支持双人语音、视频通话功能
- 支持创建群聊会话、群成员管理等。

| Android 演示| iOS 演示 |
| :-----| ----: |
| <img  src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/android-uniapp.gif">|<img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/ios-uniapp.gif">|

## 技术咨询

了解更多详情您可 QQ 咨询：309869925 (技术交流群)

## 相关文档
- [uni-app 原生音视频插件示例](https://github.com/tencentyun/TIMSDK/tree/master/uni-app/TUICalling/TUICalling-app)
- [uni-app TUIKit 源码](https://github.com/tencentyun/TIMSDK/tree/master/uni-app)
- [一分钟跑通 Demo (uni-app)](https://cloud.tencent.com/document/product/269/64506)
- [快速集成 uni-app TUIKit](https://cloud.tencent.com/document/product/269/64507)


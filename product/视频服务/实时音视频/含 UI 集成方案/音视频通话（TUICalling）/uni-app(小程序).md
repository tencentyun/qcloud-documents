TUICalling 小程序组件是基于腾讯云实时音视频（TRTC）和腾讯云信令 SDK（TSignalling）组合而成，支持1V1，多人场景下的视频通话。

## 效果展示

<img src="https://qcloudimg.tencent-cloud.cn/raw/80d21c47a70a9862c637c9a2bf8d58d5.png">


## 应用场景
在线客服、在线面试、企业在线沟通、在线问诊、音视频社交等。

## 环境要求
- 微信 App iOS 最低版本要求：7.0.9。
- 微信 App Android 最低版本要求：7.0.8。
- 小程序基础库最低版本要求：2.10.0。
- 由于微信开发者工具不支持原生组件（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签），需要在真机上进行运行体验。
- 由于小程序测试号不具备 &lt;live-pusher&gt; 和 &lt;live-player&gt; 的使用权限，需要申请常规小程序账号进行开发。

## 前提条件
1. 您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. **开通小程序类目与推拉流标签权限（如不开通则无法正常使用）**。
出于政策和合规的考虑，微信暂未放开所有小程序对实时音视频功能（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签）的支持：
 - 小程序推拉流标签不支持个人小程序，只支持企业类小程序。
 - 小程序推拉流标签使用权限暂时只开放给有限 [类目](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。
 - 符合类目要求的小程序，需要在 **[微信公众平台](https://mp.weixin.qq.com)** > **开发** > **开发管理** > **接口设置** 中自助开通该组件权限，如下图所示：
![](https://main.qcloudimg.com/raw/dc6d3c9102bd81443cb27b9810c8e981.png)

[](id:run)
## 快速跑通
[](id:run.step1)
### 步骤一：注册并创建 uni-app 账号

搭建 App 开发环境：
1. 下载 [HBuilderX 编辑器 ](https://www.dcloud.io/hbuilderx.html)。
>!项目中 HBuilderX 目前使用的最新版本，如果此前下载过 HBuilderX，为保证开发环境统一请更新到最新版本。
2. 进入 [DCloud 开发者中心注册](https://dev.dcloud.net.cn/)，登录 HBuilderX 编辑器。

### 步骤二：创建应用并开通腾讯云服务
1. **创建即时通信 IM 应用：**
	1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im)，单击 **创建新应用** 将弹出对话框。
		 ![](https://main.qcloudimg.com/raw/c8d1dc415801404e30e49ddd4e0c0c13.png)
	2. 输入您的应用名称，单击 **确认** 即可完成创建。
		 ![](https://main.qcloudimg.com/raw/496cdc614f7a9d904cb462bd4d1e7120.png)
	3. 您可在 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) 总览页面查看新建应用的状态、业务版本、SDKAppID、创建时间以及到期时间。请记录 SDKAppID 信息。
2. **获取 IM 密钥并开通实时音视频服务：**
	1. 在 [即时通讯 IM 控制台](https://console.cloud.tencent.com/im) 总览页单击您创建完成的即时通信 IM 应用，随即跳转至该应用的基础配置页。在 **基本信息** 区域，单击 **显示密钥**，复制并保存密钥信息。
	![](https://main.qcloudimg.com/raw/030440f94a14cd031476ce815ed8e2bc.png)
>!请妥善保管密钥信息，谨防泄露。
	2. 在该应用的基础配置页，开通腾讯云实时音视频服务。
	![](https://main.qcloudimg.com/raw/1c2ce5008dad434d9206aabf0c07fd04.png)

[](id:run.step3)
### 步骤三：下载并配置 TUICalling 源码

1. 根据您的实际业务需求，下载 SDK 及配套的 [Demo 源码](https://gitee.com/cloudtencent/TIMSDK/tree/master/uni-app/TUICalling-miniprogram)。
```javascript
# 命令行执行
git clone https://gitee.com/cloudtencent/TIMSDK

# 进入 uni-app TUICalling 项目
cd TIMSDK/uni-app/TUICalling-miniprogram

# 安装依赖
npm install
```
2. 将 uni-app 中 TUICalling 工程文件，导入自己的 HBuilderX 工程。具体操作请参见 [uni-app 开发](https://uniapp.dcloud.io/quickstart-hx)。
3. 设置 GenerateTestUserSig 文件中的相关参数。
	- 找到并打开 `debug/GenerateTestUserSig.js` 文件。
	- 设置 `GenerateTestUserSig.js` 文件中的相关参数。
  <ul><li>SDKAPPID：默认为0，请设置为实际的 SDKAppID。</li>
  <li>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</li></ul> 
  <img src="https://main.qcloudimg.com/raw/575902219de19b4f2d4595673fa755d4.png">
>! 
>- 本文提到的生成 `UserSig` 的方案是在客户端代码中配置 `SECRETKEY`，该方法中 `SECRETKEY` 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 uni-app 和功能调试**。
>- 正确的 `UserSig` 签发方式是将 `UserSig` 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 `UserSig` 时由您的 App 向业务服务器发起请求获取动态 `UserSig`。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275)。

[](id:run.step4)
### 步骤四：编译运行
具体操作，请参见 [uni-app 运行](https://uniapp.dcloud.io/quickstart-hx?id=%e8%bf%90%e8%a1%8cuni-app)。

[](id:run.step4)
###  步骤五：打包发布
具体操作，请参见 [uni-app 打包](https://uniapp.dcloud.io/quickstart-hx?id=%e5%8f%91%e5%b8%83uni-app)。

[](id:integrated)
## 集成方法
[](id:in.step1)
### 步骤一：集成 TUICalling 组件
1. **把组件文件放在 wxcomponents 中：**
	1. 从 [GitHub](https://github.com/tencentyun/TIMSDK/tree/master) 下载 uni-app TUIKit 源码 [Demo 源码](https://gitee.com/cloudtencent/TIMSDK/tree/master/uni-app/TUICalling-miniprogram)。
```javascript
# 命令行执行
git clone https://gitee.com/cloudtencent/TIMSDK

# 进入 uni-app TUICalling 项目
cd TIMSDK/uni-app/TUICalling-miniprogram

# 安装依赖
npm install
```
	2. 将项目中的 wxcomponents 中的 TUICalling 组件复制到自己项目的 wxcomponents 中。如果没有 wxcomponents文件，请将 wxcomponents 复制到自己的项目中。
<img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-calling-wx-1.png" width = "400"/>
2.  **pages 配置组件：**
在 `pages.json` 文件中，呼叫音视频页面配置组件。
```json
{
	"usingComponents": {
		"tuicalling": "/wxcomponents/TUICalling/TUICalling"
	}
}
```
>!组件名称均是小写字母。
3. **在页面的 xml 中引入组件：**
```xml
<tuicalling
	ref="TUICalling" 
	id="TUICalling-component" 
	:config="config">
</tuicalling>
```
>!组件的名称要与 page.json 中的保持一致，组件名称均是小写字母。
4. **填写 TIM 实例（如果您没有创建 TIM 实例，可忽略）**：
在 `app.vue` 中，如果您已创建了 TIM，请将 TIM 实例挂载在 wx 上，且不可以修改 wx.$TIM。
>!
>- TIM 参数适用于业务中已存在 TIM 实例，为保证 TIM 实例唯一性。
>- 填写后，不可以修改 wx.$TIM（修改变量可能导致 TUICalling 组件无法正常使用）。
>
![](https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-calling-wx-2.png)
5. **填写 config 配置信息：**
```javascript
config = {
  sdkAppID: 0, // 开通实时音视频服务创建应用后分配的 SDKAppID
  userID: 'user0', // 用户 ID，可以由您的帐号系统指定
  userSig: 'xxxxxxxxxxxx', // 身份签名，相当于登录密码的作用
  type: 2, // 通话模式
}
```

[](id:in.step2)
### 步骤二：初始化 TUICalling 组件
```javascript
  // 将初始化后到 TUICalling 实例注册到 this.TUICalling。
  this.TUICalling = this.$refs.TUICalling;
  // 初始化 TUICalling
  this.$nextTick(() => {
  	this.TUICalling.init()
  })
```

[](id:in.step3)
### 步骤三： 进行通话
- **双人通话**
```javascript
this.TUICalling.call({ userID: 'user1', type:2})
```
- **多人通话**
```javascript
this.TUICalling.groupCall({userIDList: ['user1','user2'], type: 2})
```

[](id:in.step4)
### 步骤四： 回收 TUICalling

```javascript
// 回收 TUICalling
this.TUICalling.destroyed()
```

## 实现案例
我们提供了**在线客服场景**的相关源码，建议您 [下载](https://github.com/tencentyun/TIMSDK/tree/master/uni-app/TUIKit) 并集成体验。该场景提供了示例客服群 + 示例好友的基础模板，实现功能包括：
- 支持发送文本消息、图片消息、语音消息、视频消息等常见消息。
- 支持双人语音、视频通话功能
- 支持创建群聊会话、群成员管理等。

| Android 演示| iOS 演示 |
| :-----| ----: |
| <img  src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/android-uniapp.gif">|<img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/ios-uniapp.gif">|

## 技术咨询

了解更多详情您可 QQ 咨询：
- **309869925** (uniapp 技术交流群)
- **646165204** （TUICalling 技术交流群)

## 参考文档
- [小程序音视频 TUICalling 组件源码](https://github.com/tencentyun/TIMSDK/tree/master/uni-app/TUIKit/uni-app/TUICalling-miniprogram)
- [TUICalling API](https://cloud.tencent.com/document/product/647/49380)
- [小程序端相关问题](https://cloud.tencent.com/document/product/647/45532)

## 常见问题
### 调试中出现以下错误怎么办？
- **错误1：**
<img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-calling-wx-3.png"/>
解决方法：请勾选开发者工具中的增强编译，再调试。
- **错误2：**
![](https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-calling-wx-4.png)
解决方法：请在 `manifest.json` 的文件中填写小程序 APPID。

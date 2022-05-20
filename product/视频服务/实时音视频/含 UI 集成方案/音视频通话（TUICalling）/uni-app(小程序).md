## 组件介绍

TUICalling 小程序组件是基于腾讯云实时音视频（TRTC）和腾讯云信令 SDK（TSignalling）组合而成，支持1V1，多人场景下的视频通话。TUICalling 同时支持 iOS、Web、小程序、Flutter、UniApp 等平台，基本功能如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/80d21c47a70a9862c637c9a2bf8d58d5.png" width=600>

## 环境要求
- 微信 App iOS 最低版本要求：7.0.9。
- 微信 App Android 最低版本要求：7.0.8。
- 小程序基础库最低版本要求：2.10.0。
- 由于微信开发者工具不支持原生组件（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签），需要在真机上进行运行体验。
- 由于小程序测试号不具备 &lt;live-pusher&gt; 和 &lt;live-player&gt; 的使用权限，需要申请常规小程序账号进行开发。

## 组件集成
## 步骤一：开通小程序权限
1. 您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. **开通小程序类目与推拉流标签权限（如不开通则无法正常使用）**。
出于政策和合规的考虑，微信暂未放开所有小程序对实时音视频功能（即 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签）的支持：
 - 小程序推拉流标签不支持个人小程序，只支持企业类小程序。
 - 小程序推拉流标签使用权限暂时只开放给有限 [类目](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher.html)。
 - 符合类目要求的小程序，需要在 **[微信公众平台](https://mp.weixin.qq.com)** > **开发** > **开发管理** > **接口设置** 中自助开通该组件权限，如下图所示：
![](https://main.qcloudimg.com/raw/dc6d3c9102bd81443cb27b9810c8e981.png)

### 步骤二：下载并集成 TUICalling 组件

1. 根据您的实际业务需求，下载 [TUICalling 组件](https://github.com/TencentCloud/TIMSDK/tree/master/uni-app/TUICalling/TUICalling-miniprogram)。
```javascript
# 命令行执行
git clone https://gitee.com/cloudtencent/TIMSDK

# 进入 uni-app TUICalling 项目
cd TIMSDK/uni-app/TUICalling/TUICalling-miniprogram
```
2. 将项目中的 wxcomponents 中的 TUICalling 组件复制到自己项目的 wxcomponents 中。如果没有 wxcomponents文件，请将 wxcomponents 复制到自己的项目中。<br>
<img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-calling-wx-1.png" width = "400"/>

### 步骤三：获取 SDKAppID 和签名密钥

- **SDKAppID**：**TRTC 应用ID**，如果您未开通腾讯云 TRTC 服务，可进入 [腾讯云实时音视频控制台](https://console.cloud.tencent.com/trtc/app)，创建一个新的 TRTC 应用后，单击**应用信息**，SDKAppID 信息如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/3d6ebfa2a1e4ae5d3af3ecd564fb1463.png)
- **SecretKey**：**TRTC 应用密钥**，和 SDKAppId 对应，进入 [TRTC 应用管理](https://console.cloud.tencent.com/trtc/app) 后，SecretKey 信息如上图所示。
- **userId**：当前用户的 ID，字符串类型，长度不超过32字节，不支持使用特殊字符，建议使用英文或数字，可结合业务实际账号体系自行设置。
- **userSig**：根据 SDKAppId、userId，Secretkey 等信息计算得到的安全保护签名，您可以单击 [这里](https://console.cloud.tencent.com/trtc/usersigtool) 直接在线生成一个调试的 UserSig，也可以参照我们的 [TUICalling示例工程](https://github.com/TencentCloud/TIMSDK/blob/master/uni-app/TUICalling/TUICalling-miniprogram/debug/GenerateTestUserSig.js)自行计算，更多信息见 [如何计算及使用 UserSig](https://cloud.tencent.com/document/product/647/17275)。

### 步骤四：创建并配置组件

1.  **pages 配置组件：**
在 `pages.json` 文件中，呼叫音视频页面配置组件。
```json
{
	"usingComponents": {
		"tuicalling": "/wxcomponents/TUICalling/TUICalling"
	}
}
```
>!组件名称均是小写字母。
2. **在页面的 xml 中引入组件：**
```xml
<tuicalling
	ref="TUICalling" 
	id="TUICalling-component" 
	:config="config">
</tuicalling>
```
>!组件的名称要与 page.json 中的保持一致，组件名称均是小写字母。
3. **填写 TIM 实例（如果您没有创建 TIM 实例，可忽略）**：
在 `app.vue` 中，如果您已创建了 TIM，请将 TIM 实例挂载在 wx 上，且不可以修改 wx.$TIM。
>!
>- TIM 参数适用于业务中已存在 TIM 实例，为保证 TIM 实例唯一性。
>- 填写后，不可以修改 wx.$TIM（修改变量可能导致 TUICalling 组件无法正常使用）。
>
![](https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-calling-wx-2.png)
4. **填写 config 配置信息：**
```javascript
config = {
  sdkAppID: 0, // 开通实时音视频服务创建应用后分配的 SDKAppID
  userID: 'user0', // 用户 ID，可以由您的帐号系统指定
  userSig: 'xxxxxxxxxxxx', // 身份签名，相当于登录密码的作用
  type: 2, // 通话模式
}
```

### 步骤五：初始化 TUICalling 组件
```javascript
  // 将初始化后到 TUICalling 实例注册到 this.TUICalling。
  this.TUICalling = this.$refs.TUICalling;
  // 初始化 TUICalling
  this.$nextTick(() => {
  	this.TUICalling.init()
  })
```

[](id:in.step3)
### 步骤六： 进行通话
- **双人通话**
```javascript
this.TUICalling.call({ userID: 'user1', type:2 })
```
- **多人通话**
```javascript
this.TUICalling.groupCall({ userIDList: ['user1','user2'], type: 2 })
```

[](id:in.step4)
### 步骤七： 回收 TUICalling

```javascript
// 回收 TUICalling
this.TUICalling.destroyed()
```

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
<td><img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/android-uniapp.gif"></td>
<td><img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/ios-uniapp.gif"></td>
</tr>
</tbody></table>

## 技术咨询

了解更多详情您可 QQ 咨询：
- **309869925** (uni-app 技术交流群)
- **646165204** （TUICalling 技术交流群)

## 参考文档
- [小程序音视频 TUICalling 组件源码](https://github.com/TencentCloud/TIMSDK/tree/master/uni-app/TUICalling/TUICalling-miniprogram)
- [集成 TUICalling (小程序)](https://cloud.tencent.com/document/product/647/49379)
- [小程序端相关问题](https://cloud.tencent.com/document/product/647/45532)

## 常见问题
### 调试中出现以下错误怎么办？
- **错误1：**
<img src="https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-calling-wx-3.png"/>
解决方法：请勾选开发者工具中的增强编译，再调试。
- **错误2：**
![](https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uni-calling-wx-4.png)
解决方法：请在 `manifest.json` 的文件中填写小程序 APPID。

本文主要介绍如何快速运行腾讯云 TRTC Demo（uni-app）。
- [uni-app 插件](https://ext.dcloud.net.cn/plugin?id=7774)
- [API 文档](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#enterRoom)
- [GitHub](https://github.com/LiteAVSDK/TRTC_UniApp)

## 环境要求
- 建议使用最新的 [HBuilderX 编辑器 ](https://www.dcloud.io/hbuilderx.html)。
- iOS 9.0 或以上版本且支持音视频的 iOS 设备，暂不支持模拟器。
- Android 版本不低于 4.1 且支持音视频的 Android 设备，暂不支持模拟器。如果为真机，请开启“允许调试”选项。
- iOS/Android 设备已经连接到 Internet。

## 前提条件
1. 您已 [注册腾讯云](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2Fdocument%2Fproduct%2F647%2F49327) 账号，并完成实名认证
2. [DCloud 开发者中心注册](https://dev.dcloud.net.cn/) 之后登录 HBuilderX 编辑器。

## 操作步骤
[](id:step1)
### 步骤1：创建实时音视频 TRTC 应用
1. [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2Fdocument%2Fproduct%2F647%2F49327) 并开通 [实时音视频](https://console.cloud.tencent.com/trtc)
2. 在 [实时音视频控制台](https://console.cloud.tencent.com/trtc) 单击 **应用管理 > 创建应用** 创建新应用。
  ![创建应用](https://main.qcloudimg.com/raw/34f87b8c0a817d8d3e49baac5b82a1fa.png)

[](id:step2)
#### 步骤2：获取 TRTC 密钥信息
1. 在 **应用管理 > 应用信息** 中获取 SDKAppID 信息。
  ![](https://qcloudimg.tencent-cloud.cn/raw/f7915fbbeb48518c2b25a413960f3432.png)
2. 在 **应用管理 > 快速上手** 中获取应用的 secretKey 信息。
  ![](https://qcloudimg.tencent-cloud.cn/raw/06d38bbdbaf43e1f2b444edae00019fa.png)

[](id:step3)
### 步骤3：下载 Api-Example
- 从 GitHub 获取
```
git clone https://github.com/LiteAVSDK/TRTC_UniApp.git
```
- [直接下载](https://web.sdk.qcloud.com/trtc/uniapp/download/Api-Example.zip)

[](id:step4)
### 步骤4：配置 Api-Example 工程文件
1. 根据您下载的源码包，进入修改配置页。
2. 找到并打开 `./debug/GenerateTestUserSig.js` 文件。
3. 设置 GenerateTestUserSig.js 文件中的相关参数：
  1. SDKAPPID：默认为0，请设置为实际的 SDKAppID。
  2. SECRETKEY：默认为空字符串，请设置为实际的密钥信息。
![](https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/config.png)
   
> !
> - 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此该方法仅适合本地跑通 Demo 和功能调试。
> - 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275)。

### 步骤5：运行
1. **制作自定义调试基座**
> ? uni-app 官方教程请参见 [什么是自定义调试基座及使用说明](https://ask.dcloud.net.cn/article/35115)。
> 
	1. 选择 **运行** >  **运行到手机或模拟器** > **制作自定义调试基座** 菜单。
		 ![](https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uniapp-customBase.png)
	2. 在弹出的界面中，参考 `uni-app` 教程，填写相关信息，并单击 **打包** 进行云打包。
		 ![](https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uniapp-package.png)
2. **切换运行基座为自定义调试基座**
在自定义调试基座选择 **运行** > **运行到手机或模拟器** > **运行基座选择** > **自定义调试基座** 菜单。
![](https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uniapp-selectCustomBase.png)
3. **运行**
在 **运行** > **运行到手机或模拟器** 菜单，选择自己的设备，并运行。

## 常见问题
### 1.【官方】腾讯云实时音视频 SDK 和 【官方】腾讯云原生音视频插件的区别？
- [【官方】腾讯云实时音视频 SDK](https://ext.dcloud.net.cn/plugin?id=7774) 就是 `TRTC SDK`。[【官方】腾讯云原生音视频插件](https://ext.dcloud.net.cn/plugin?id=7097) 就是 `TUICalling`。
- `TRTC SDK` 是音视频基础能力，无 UI 和逻辑。适用于比较复杂的场景，或者定制化比较强的场景。用现有的 `TUICalling` 无法满足的需求，就可以使用 `TRTC SDK` 自己搭建。
- `TUICalling` 插件包含 UI 和逻辑，专用于 1V1、多人音视频通话场景，接入简单。

### 2. 【官方】腾讯云实时音视频 SDK 支持小程序吗？
建议请参见 [TRTCSimpleDemoUniApp](https://github.com/LiteAVSDK/Live_WXMini/tree/main/TRTCSimpleDemoUniApp)。

### 3. 实例里面 app.vue 中的 aegis-weex-sdk 有什么用？
[Demo](https://web.sdk.qcloud.com/trtc/uniapp/download/Api-Example.zip) 里的 `aegis-weex-sdk` 主要是用来对 Demo 做性能监控统计。

### 4. 创建实例 this.trtcCloud = TrtcCloud.createInstance(); 和 this.trtcCloud = new TrtcCloud(); 有什么区别？
创建 trtcCloud 单例，只能通过 [`TrtcCloud.createInstance()`](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#.createInstance) 实例化一个 TrtcCloud 对象

### 5. startRemoteView 在什么时候调用？
建议在 [onUserVideoAvailable](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TRTCCallback.html#event:onUserVideoAvailable) 事件回调中调用 [startRemoteView](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#stopLocalPreview)。

### 6. 本地预览如何自定义样式？
建议通过 view 包裹 `trtc-local-view、trtc-remote-view`。然后设置 view 的样式即可

### 7. startLocalPreview 不传 viewId 可以吗？
[startLocalPreview](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#startLocalPreview) **可以不传** viewId。但是页面需要有 trtc-local-view 组件，并且它的 viewId 绑定的是本地用户 ID。

### 8. startLocalPreview 报 -2 错误？
- 错误原因：没有实例化本地预览的 view。
- 解决方案：
	- 首先必须是 .nvue 文件，[详见](https://nativesupport.dcloud.net.cn/NativePlugin/course/ios)。
	- 页面必须使用 `trtc-local-view` 并且绑定了 viewId。

### 9. [【官方】腾讯云实时音视频 SDK](https://ext.dcloud.net.cn/plugin?id=7774) 和 [livepusher](https://nativesupport.dcloud.net.cn/AppDocs/usemodule/androidModuleConfig/android_Library) 推流模块同时使用，打包冲突
 [uni-app 官网文档介绍](https://nativesupport.dcloud.net.cn/AppDocs/usemodule/androidModuleConfig/android_Library) 第三方 SDK 使用 LiteAVSDK（weex_livepusher-release.aar）做直播推流，和 [【官方】腾讯云实时音视频 SDK](https://ext.dcloud.net.cn/plugin?id=7774) 使用的 LiteAVSDK_TRTC 类冲突。和 uni-app 技术沟通后，对方反馈不清楚 SDK 属于那个版本类型，因此 uni-app 他们无法对 livepusher 进行升级。

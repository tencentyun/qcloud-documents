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
- 您已 [注册腾讯云](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2Fdocument%2Fproduct%2F647%2F49327) 账号，并完成实名认证。
- 进入 [DCloud 开发者中心注册](https://dev.dcloud.net.cn/) 之后登录 HBuilderX 编辑器。

## 操作步骤
### 步骤1：创建实时音视频 TRTC 应用
1. [注册腾讯云账号](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2Fdocument%2Fproduct%2F647%2F49327) 并开通 [实时音视频](https://console.cloud.tencent.com/trtc)。
2. 在 [实时音视频控制台](https://console.cloud.tencent.com/trtc) 单击 **应用管理 > 创建应用** 创建新应用。
![](https://qcloudimg.tencent-cloud.cn/raw/dbf33c047c4af90aeb20f2b4b01988c2.png)

### 步骤2：获取 TRTC 密钥信息
1. 在 **应用管理 > 应用信息** 中获取 SDKAppID 信息。
  ![](https://qcloudimg.tencent-cloud.cn/raw/f7915fbbeb48518c2b25a413960f3432.png)
2. 在 **应用管理 > 快速上手** 中获取应用的 secretKey 信息。
  ![](https://qcloudimg.tencent-cloud.cn/raw/06d38bbdbaf43e1f2b444edae00019fa.png)

### 步骤3：下载 API-Example
支持以下两种方式：
- 从 GitHub 获取：
```
git clone https://github.com/LiteAVSDK/TRTC_UniApp.git
```
- 单击 [直接下载](https://web.sdk.qcloud.com/trtc/uniapp/download/Api-Example.zip)。

### 步骤4：配置 Api-Example 工程文件
1. 根据您下载的源码包，进入修改配置页。
2. 找到并打开 `./debug/GenerateTestUserSig.js` 文件。
3. 设置 GenerateTestUserSig.js 文件中的相关参数：
  1. SDKAPPID：默认为0，请设置为实际的 SDKAppID。
  2. SECRETKEY：默认为空字符串，请设置为实际的密钥信息。
![](https://qcloudimg.tencent-cloud.cn/raw/f11a79f38f1479ba643752d8d9f3e3d4.png)
   
> !本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此该方法仅适合本地跑通 Demo 和功能调试。
> !正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 服务端生成 UserSig。

### 步骤5：运行
1. **制作自定义调试基座**
> ? uni-app 官方教程请参见 [什么是自定义调试基座及使用说明](https://ask.dcloud.net.cn/article/35115)。
> 
	1. 选择**运行** >  **运行到手机或模拟器** > **制作自定义调试基座**菜单。
	![](https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uniapp-customBase.png)
	2. 在弹出的界面中，参考 `uni-app` 教程，填写相关信息，并单击**打包**进行云打包。
   ![](https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uniapp-package.png)
2. **切换运行基座为自定义调试基座**
在自定义调试基座选择**运行** > **运行到手机或模拟器** > **运行基座选择** > **自定义调试基座**菜单。
![](https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uniapp-selectCustomBase.png)
3. **运行**
在 **运行** > **运行到手机或模拟器**菜单中，选择自己的设备，并运行。

## 常见问题
### 【官方】腾讯云实时音视频SDK 和 【官方】腾讯云原生音视频插件的区别？
1.  [【官方】腾讯云实时音视频SDK](https://ext.dcloud.net.cn/plugin?id=7774) 就是 `TRTC SDK`，[【官方】腾讯云原生音视频插件](https://ext.dcloud.net.cn/plugin?id=7097) 就是 `TUICalling`。
2. `TRTC SDK` 是音视频基础能力，无 UI 和逻辑。适用于比较复杂的场景，或者定制化比较强的场景。用现有的 `TUICalling` 无法满足的需求，就可以使用 `TRTC SDK` 自己搭建。
3. `TUICalling` 插件包含 UI 和逻辑，专用于 1V1、多人音视频通话场景，接入简单。

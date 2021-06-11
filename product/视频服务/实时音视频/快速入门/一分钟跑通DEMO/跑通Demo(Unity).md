这个示例项目演示了如何在 Unity 中快速集成 TRTC SDK，实现在游戏中的音视频通话。

在这个示例项目中包含了以下功能：
- 加入通话和离开通话。
- 自定义视频渲染。
- 设备管理、音乐特效和人声特效。

>?
>- 具体 API 功能参数说明，请参见 [Unity API 概览](https://cloud.tencent.com/document/product/647/55158)。
- 更多项目接入问题，请接入 QQ 群（764231117）咨询。

## 运行环境要求
- Unity 建议版本： 2020.2.1f1c1。
- 目前支持 Android、iOS、Windows、Mac(Mac 还在内测中)平台。
- 需要包含 `Android Build Support`、`iOS Build Support`、`Winodows Build Support` 和 `MacOs Build Support` 模块。
- 其中 iOS 端开发还需要：
  - Xcode 11.0及以上版本。
  - 请确保您的项目已设置有效的开发者签名。

## 运行示例程序
[](id:step1)
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择【开发辅助】>【[快速跑通Demo](https://console.cloud.tencent.com/trtc/quickstart)】。
2. 单击【立即开始】，输入应用名称，例如 `TestTRTC`，单击【创建应用】。
![](https://main.qcloudimg.com/raw/7178fb5203b8c1ad9eb4a3b7a3c008d7.png)

[](id:step2)
### 步骤2：下载 SDK 与源码
1. 根据您的实际业务需求，下载 SDK 及配套的 [Demo 源码](https://tccweb-1258344699.cos.ap-nanjing.myqcloud.com/sdk/trtc/unity/TRTCUnitySDK.zip)。
2. 下载完成后，单击【已下载，下一步】。（可直接用 Unity 打开本项目；如果想直接用 SDK 文件，也可把 SDK 包中的 `TRTCUnitySDK/Assets/TRTCSDK/SDK` 文件夹拷贝到您项目中的 Assets 目录下。）
![](https://main.qcloudimg.com/raw/a452f35ef0efe73124b301084e1a77f4.png)
3. 找到并打开 `Assets/TRTCSDK/Demo/Tools/GenerateTestUserSig.cs` 文件。
4. 设置 `GenerateTestUserSig.cs` 文件中的相关参数：
  <ul><li>SDKAPPID：默认为0，请设置为实际的 SDKAppID。</li>
  <li>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</li></ul> 
	<img src="https://main.qcloudimg.com/raw/4dad4541a4a0d400441e9cd75c07ba1e.png"/>

[](id:step3)
### 步骤3：编译运行
<dx-tabs>
::: Android\s平台
1. 配置 Unity Editor，单击【File】>【Build Setting】，切换至 Android。
![](https://main.qcloudimg.com/raw/4464eb891829e3505a59c8ec00cc2414.png)
2. 连接 Android 真机，单击【 Build And Run】，Demo 就能跑起来。
3. 接口测试，需要先点击调用 enterRoom ，然后自行测试其他相关，数据展示窗口显示点击调用成功，另外一个窗口显示回调信息。
:::
::: iOS\s平台
1. 配置 Unity Editor，单击【File】>【Build Setting】，切换至 iOS。
![](https://main.qcloudimg.com/raw/3a0ef43000fe53e8e7ff58b6cc243785.png)
2. 连接 iPhone 真机，单击【Build And Run】，需要选择一个新的目录存放编译出来的 iOS 工程，等待编译完成，会有新窗口弹出 Xcode 工程。
:::
::: Windows\s平台
1. 配置 Unity Editor，单击【File】>【Build Setting】，切换至 `PC, Mac & Linux Standalone`，Target Platform 选择 Windows。
![](https://main.qcloudimg.com/raw/580764f661c06cf71c4952727c409c5e.png)
2. 单击【 Build And Run】，Demo 就能跑起来。
:::
::: macOS\s平台
1. 配置 Unity Editor，单击【File】>【Build Setting】，切换至 `PC, Mac & Linux Standalone`，Target Platform 选择 macOS。
![](https://main.qcloudimg.com/raw/6f3f9c21aa9eeadd7a4e3be377b2a6b3.png)
2. 单击【 Build And Run】，Demo 就能跑起来。
3. 使用 Unity Editor 模拟器运行，先要安装 `Device Simulator Package`。
4. 单击【Window】>【General】>【Device Simulator】
![](https://main.qcloudimg.com/raw/79f707b89553528956a888f48b4d4d6d.png)
:::
</dx-tabs>


[](id:demo)
## Demo示例
Demo 里面包含了已上线的大部分 API，可以测试和作为调用参考，API 文档参见 [SDK API（Unity）](https://cloud.tencent.com/document/product/647/55158)。
>? UI 可能会有部分调整更新，请以最新版为准。

![](https://main.qcloudimg.com/raw/2ce3ab51c6fdc843c1e8b086b55840c0.png)

## 目录结构
```
├─Assets
├── Editor                        // Unity 编辑器脚本
│   ├── BuildScript.cs            // Unity 编辑器build菜单
│   ├── IosPostProcess.cs         // Unity 编辑器构建ios应用脚本
├── Plugins
│   ├── Android                   
│   │   ├── AndroidManifest.xml   //Android应用配置文件
├── StreamingAssets               // Unity Demo 音视频流文件
├── TRTCSDK
    ├── Demo                      // Unity 示例 Demo
    ├── SDK                       // TRTC Unity SDK
        ├── Implement             // TRTC Unity SDK 实现
        ├── Include               // TRTC Unity SDK 头文件
        └── Plugins               // TRTC Unity SDK 不同平台底层实现
            
```

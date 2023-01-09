本文主要介绍如何快速地将腾讯云即时通信 IM SDK 集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。

## 环境要求

| 平台    | 版本                                                         |
| ------- | ------------------------------------------------------------ |
| Unity   | 2019.4.15f1 及以上版本。                                     |
| Android | Android Studio 3.5及以上版本，App 要求 Android 4.1及以上版本设备。 |
| iOS     | Xcode 11.0及以上版本，请确保您的项目已设置有效的开发者签名。 |

## UPM 集成（推荐）

1. 修改 manifest.json 文件：
![](https://qcloudimg.tencent-cloud.cn/raw/881d625bf3ee2e736db22762e8763c18.png)
2. 修改如下：
```json
   {
     "dependencies":{
       "com.tencent.imsdk.unity":"https://github.com/TencentCloud/chat-sdk-unity.git#unity"
     }
   }
```
3. 在 Unity Editor 中打开项目，等候依赖加载完毕，确认Tencent Cloud IM 已经加载完成。
![img](https://qcloudimg.tencent-cloud.cn/raw/d98dfb17bbee6c0319e370de6f2ba9dd.jpg)
4. 该步骤为测试环节，您可下载 [IM_Api_Example](https://github.com/TencentCloud/tc-chat-sdk-unity/tree/main/Assets/IM_Api_Example)，解压后放入您的项目内。
   <img src="https://qcloudimg.tencent-cloud.cn/raw/7c7e35b688673c3bca02b95f6ca74e4a.png" width="70%">
    > ?IM_Api_Example 是我们提供的用来测试 SDK 接口回调数据的 Demo，您也可以在项目开发早期通过调用我们提供的接口来对您的应用进行操作。

    将 `IM_Api_Example/Assets` 文件夹下所有场景拖入 `Build Settings`，并保证 `Main` 场景的顺序在第一位。
    <img src="https://qcloudimg.tencent-cloud.cn/raw/b4235594ea96e60960a31f8c7e7edd67.jpg" width="35%">

    双击位于 `IM_Api_Example/Assets` 下的 Main Scene 来启动 Demo，您可以在这里选择语言。
    <img src="https://qcloudimg.tencent-cloud.cn/raw/16d9c669d4c5b4932490452ec421ca89.jpg" width="35%">

    单击 Header 右侧的 ![](https://qcloudimg.tencent-cloud.cn/raw/471e34746e4accceea25945e12223000.png) 并填写相应信息。
    <img src="https://qcloudimg.tencent-cloud.cn/raw/5b5641156812d46d7e03218e856385a8.jpg" width="35%">

    分别单击基础模块内的 InitSDK & Login 完成初始化和登录，接下来您可以自由调用 Api Example 里提供的接口。
    <img src="https://qcloudimg.tencent-cloud.cn/raw/4b5cff4c369a770f980b16a017f6d329.jpg" width="23%"> <img src="https://qcloudimg.tencent-cloud.cn/raw/a2d0dfab936904bf8703ef8240656ab6.jpg" width="23%"> <img src="https://qcloudimg.tencent-cloud.cn/raw/cc01b9a6b752f26b056d04f346bc1056.jpg" width="23%">

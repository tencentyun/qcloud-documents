本文主要介绍如何快速地将腾讯云 TRTC uni-app SDK 集成到您的项目中。
## 准备工作
集成 TRTC uni-app SDK 之前需要了解的事项。

## 开发环境要求
- 建议使用最新的 HBuilderX 编辑器 。
- iOS 9.0 或以上版本且支持音视频的 iOS 设备，暂不支持模拟器。
- Android 版本不低于 4.1 且支持音视频的 Android 设备，暂不支持模拟器。如果为真机，请开启**允许调试**选项。
- iOS/Android 设备已经连接到 Internet。

## 导入 SDK
uni-app 音视频 SDK 已发布到 [GitHub](https://github.com/LiteAVSDK/TRTC_UniApp)，可以到 [GitHub](https://github.com/LiteAVSDK/TRTC_UniApp) 下载或 [直接下载](https://web.sdk.qcloud.com/trtc/uniapp/download/TrtcCloud.zip) SDK。对应的插件 [**官方**腾讯云实时音视频SDK](https://ext.dcloud.net.cn/plugin?id=7774) 已发布到插件市场。

1. [直接下载](https://web.sdk.qcloud.com/trtc/uniapp/download/TrtcCloud.zip)，获取 TrtcCloud。然后将 TrtcCloud 放到自己 uni-app 的项目中，例如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/e45490acb915b807a21297e13f73a3ed.png)
```javascript
import TrtcCloud from "@/TrtcCloud/lib/index"; // 将 TrtcCloud 引入到代码中
```
2. **购买 uni-app SDK 插件**：
   登录 [uni 原生插件市场](https://ext.dcloud.net.cn/plugin?id=7774)，在插件详情页中购买（免费插件也可以在插件市场 0 元购）。购买后才能够云端打包使用插件。**购买插件时请选择正确的 appid，以及绑定正确包名**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/d270d9298975ee829ae9c8c405530765.png)
3. 使用自定义基座打包 uni 原生插件（请使用真机运行自定义基座）
   ![](https://web.sdk.qcloud.com/component/TUIKit/assets/uni-app/uniapp-selectCustomBase.png)

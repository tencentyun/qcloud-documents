本文主要介绍如何快速地将腾讯云 TRTC SDK（uni-app）集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。
- [uni-app 插件](https://ext.dcloud.net.cn/plugin?id=7774)
- [API 文档](https://web.sdk.qcloud.com/trtc/uniapp/doc/zh-cn/TrtcCloud.html#enterRoom)
- [GitHub](https://github.com/LiteAVSDK/TRTC_UniApp)

## 环境要求
- 建议使用最新的 [HBuilderX 编辑器 ](https://www.dcloud.io/hbuilderx.html)。
- iOS 9.0 或以上版本且支持音视频的 iOS 设备，暂不支持模拟器。
- Android 版本不低于 4.1 且支持音视频的 Android 设备，暂不支持模拟器。如果为真机，请开启**允许调试**选项。
- iOS/Android 设备已经连接到 Internet。

## 前提条件
1. 您已 [注册腾讯云](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2Fdocument%2Fproduct%2F647%2F49327) 账号，并完成实名认证
2. [DCloud 开发者中心注册](https://dev.dcloud.net.cn/) 之后登录 HBuilderX 编辑器。

## 集成 SDK
uni-app 音视频 SDK 已发布到 [GitHub](https://github.com/LiteAVSDK/TRTC_UniApp)，可以到 [GitHub](https://github.com/LiteAVSDK/TRTC_UniApp) 下载或 [直接下载](https://web.sdk.qcloud.com/trtc/uniapp/download/TrtcCloud.zip) SDK。对应的插件 [【官方】腾讯云实时音视频SDK](https://ext.dcloud.net.cn/plugin?id=7774) 已发布到插件市场。
下载 SDK 中的 TrtcCloud 代码：
1. [直接下载](https://web.sdk.qcloud.com/trtc/uniapp/download/Api-Example.zip) SDK，获取 TrtcCloud，并引入工程。
```
import TrtcCloud from "@/TrtcCloud/lib/index";
```
2. **购买 uni-app SDK 插件**：
登录 [uni 原生插件市场](https://ext.dcloud.net.cn/plugin?id=7774)，在插件详情页中购买（免费插件也可以在插件市场 0 元购）。购买后才能够云端打包使用插件。**购买插件时请选择正确的 appid，以及绑定正确包名**。
3. 使用自定义基座打包 uni 原生插件 （请使用真机运行自定义基座）。

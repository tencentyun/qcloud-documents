腾讯云云游戏提供 Web 端和 Android 端的 SDK，本文主要为您提供 SDK 安装包下载及腾讯云云游戏 SDK 的时序图说明。

### 云游戏 SDK 下载

| SDK         | 所属平台   | ZIP 包                                                       | SDK 说明                                                     |
| ----------- | ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| JS SDK      | 桌面浏览器 | [DOWNLOAD](https://ex.cloud-gaming.myqcloud.com/cloud_gaming_web_sdk/tcg-sdk/latest/index.js) | [DOC](https://cloud.tencent.com/document/product/1162/46134) |
| Android SDK | Android    | [DOWNLOAD](https://recorder-10018504.cos.ap-shanghai.myqcloud.com/1.1.2/tcgsdk_v1.1.2.107_202012291751.zip) | [DOC](https://cloud.tencent.com/document/product/1162/47434) |


### 云游戏 JS SDK 时序图

![](https://main.qcloudimg.com/raw/bd9d347d6b38a6587854119ac57d9799.png)
**其中：**

| 时序角色       | 对应           |
| ---------- | -------------- |
| page       | 用户网页       |
| tcgsdk.js  | 当前使用的云游戏 SDK         |
| app_server | 用户业务服务器 |
| cloud_api  | 腾讯云 API     |

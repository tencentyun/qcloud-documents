
本文主要介绍如何快速运行腾讯云 MLVB-API-Example（iOS）。

## 环境要求
- Xcode 9.0+。
- iOS 9.0 以上的 iPhone 或者 iPad 真机。
- 项目已配置有效的开发者签名。

## 前提条件
您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤
[](id:step1)
### 步骤1：下载 SDK 和 MLVB-API-Example 源码
1. 根据实际业务需求 [下载](https://cloud.tencent.com/document/product/454/7873) 相应的压缩包，这里以 [Professional](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Professional_iOS_latest.zip) 为例。
2. 下载完成后，解压。<br>
<img src="https://main.qcloudimg.com/raw/e0d2391f4e5bd316ac702e7980393584.png" width=300px>

[](id:step2)
### 步骤2：配置 License

1. 登录云直播控制台，在左侧菜单中选择 **直播SDK** > [**License管理**](https://console.cloud.tencent.com/live/license)，单击 **创建测试License**。 
![#500px](https://main.qcloudimg.com/raw/a623b59b4989ef4d713fc5a2e13927c1.png)
2. 根据实际需求填写 `App Name`、`Package Name` 和 `Bundle ID`，勾选功能模块 **直播推流**，单击 **确定**。
<img src="https://main.qcloudimg.com/raw/b471d5f1b85b292de034fde0a5b6650f.png" width=600px>
3. License 成功创建后，页面会显示生成的 License 信息。
<img src="https://main.qcloudimg.com/raw/53635bb1119911b9a17bea79ab327283.png" width=600px>
4. 打开 `LiteAVSDK_Professional_iOS_版本号/MLVB-API-Example-OC/Debug/GenerateTestUserSig.h` 文件。
设置 `GenerateTestUserSig.h` 文件中的相关参数：
- LICENSEURL：默认为空，请设置为您的下载 Licence url。
- LICENSEURLKEY：默认为空，请设置为您的下载 Licence key。
<img src="https://main.qcloudimg.com/raw/bcf6f24c3f6e480106479d47dd335b93.png" width=600px>


[](id:step3)
### 步骤3：配置推流/播放能力
1. 已在 [域名注册](https://dnspod.cloud.tencent.com/?from=qcloudProductDns) 申请域名，并备案成功。
2. 已在 **云直播控制台** > **[域名管理](https://console.cloud.tencent.com/live/domainmanage)** 中添加推流/播放域名，具体操作请参见 [添加自有域名](https://cloud.tencent.com/document/product/267/20381)。
3. 成功 [配置域名 CNAME](https://cloud.tencent.com/document/product/267/19908)。
4. 配置好推流/播放域名后，在推流/播放域名的 **基本信息** 页面可以获得 `CNAME` 和 `API Key` 两个信息
<img src="https://main.qcloudimg.com/raw/479d9da3f5da8068431beb796609d932.png" width=500px>
5. 打开 `LiteAVSDK_Professional_iOS_版本号/MLVB-API-Example-OC/Debug/App/Common/LiveUrl.m` 文件。
设置 `LiveUrl.` 文件中的相关参数：
  - generateRtmpPushUrl 中推流地址请设置为您的推流域名的 `CNAME`。
  - generateRtmpPlayUrl 中拉流地址请设置为您的播放域名的 `CNAME`。
  - KEY：非必需，用于生成 txSecret 等鉴权信息，具体计算请参见 [推拉流 URL](https://cloud.tencent.com/document/product/454/7915)。

[](id:step4)
### 步骤4：配置 RTC 推流能力（可选）
- 如果您有连麦的需求，可以参考 [RTC 推拉流](https://cloud.tencent.com/document/product/454/60979) 来配置 Demo 并拼接推流/拉流 URL。
- 如果您没有连麦的需求，仅需修复文件 `LiteAVSDK_Professional_iOS_版本号/MLVB-API-Example-OC/Debug/GenerateTestUserSig.h` 的 `SDKAPPID` 编译错误即可。

[](id:step5)
### 步骤5：编译运行
使用 Xcode（9.0及以上的版本）打开源码工程 `MLVB-API-Example-OC`，单击 **运行** 即可。
<img src="https://main.qcloudimg.com/raw/a6534c832fa80b8c818a7320873e5e1c.png" width=300px>

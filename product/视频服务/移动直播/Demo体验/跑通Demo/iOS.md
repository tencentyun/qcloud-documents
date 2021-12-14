
本文主要介绍如何快速运行腾讯云 MLVB-API-Example（iOS）。

## 环境要求
- Xcode 9.0+。
- iOS 9.0 以上的 iPhone 或者 iPad 真机。
- 项目已配置有效的开发者签名。

## 前提条件
您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤
[](id:step1)
### 步骤一：下载 SDK 和 MLVB-API-Example 源码
1. 根据实际业务需求 [下载](https://cloud.tencent.com/document/product/454/7873) 相应的压缩包，这里以 [Professional](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_Professional_iOS_latest.zip) 为例。
2. 下载完成后，解压。<br>
<img src="https://main.qcloudimg.com/raw/e0d2391f4e5bd316ac702e7980393584.png" width=300px>
>!源码也可以从 [Github](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/MLVB-API-Example-OC) 获得。

[](id:step2)
### 步骤二：配置 License

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
### 步骤三：配置推流/播放能力
1. 已在 [域名注册](https://dnspod.cloud.tencent.com/?from=qcloudProductDns) 申请域名，并备案成功。
2. 已在 **云直播控制台** > **[域名管理](https://console.cloud.tencent.com/live/domainmanage)** 中添加推流/播放域名，具体操作请参见 [添加自有域名](https://cloud.tencent.com/document/product/267/20381)。
3. 成功 [配置域名 CNAME](https://cloud.tencent.com/document/product/267/19908)。
4. 配置好推流/播放域名后，在推流/播放域名的 **基本信息** 页面可以获得 `CNAME` 和 `API Key` 两个信息。
<img src="https://main.qcloudimg.com/raw/479d9da3f5da8068431beb796609d932.png" width=500px>
5. 打开 `LiteAVSDK_Professional_iOS_版本号/MLVB-API-Example-OC/Debug/GenerateTestUserSig.h` 文件。
设置 `GenerateTestUserSig.h` 文件中的相关参数：
  - PUSH_DOMAIN 中推流地址请设置为您的推流域名的 `CNAME`。
  - PLAY_DOMAIN 中拉流地址请设置为您的播放域名的 `CNAME`。
  - LIVE_URL_KEY：非必需，用于生成 txSecret 等鉴权信息，具体计算请参见 [推拉流 URL](https://cloud.tencent.com/document/product/454/7915)。

[](id:step4)
### 步骤四：配置连麦或 PK 能力
[](id:step41)
#### 服务开通 
使用连麦或 PK 能力前，需先开通腾讯云 [**实时音视频**](https://cloud.tencent.com/document/product/647) 服务，具体步骤如下：
1. 登录实时音视频控制台，选择 **[应用管理](https://console.cloud.tencent.com/trtc/app)**。
2. 单击 **创建应用**，输入应用名称，例如 `V2Demo`，单击 **确定**。
3. 创建成功后，单击应用列表中 **应用名称** 为 `V2Demo` 这行右侧的 **应用信息**，查看应用对应的 `SDKAppID` 信息。
![](https://main.qcloudimg.com/raw/10e6a9395d2ebc19825d1183d5bef8f1.png)
4. 单击 **开发辅助** > **快速跑通Demo**，选中 **选择已有应用**，在下拉列表中选择 `V2Demo`，单击 **创建**。
<img src="https://main.qcloudimg.com/raw/105c7afd43f689e6f4db64bb737e6d9a.png" width=528>
5. 在创建成功后的页面，单击 **已下载，下一步**。
6. 在 **修改配置** 页面可以记录出现的 **密钥**，下文中将会替换 `SECRETKEY`，计算出 `UserSig`。
<img src="https://main.qcloudimg.com/raw/88ac7e12dfe38069ea7dc155d09e13af.png" width=528>
> !
> - 本文提到的生成 UserSig 的方案是在客户端代码中配置 UserSig，该UserSig 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此 **该方法仅适合本地跑通 Demo 和功能调试**。
> - 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。
7. 若您的播放端需要进行 CDN 播放，则需要在 [**应用管理**](https://console.cloud.tencent.com/trtc/app) 中选择 `V2Demo` 行右侧的 **应用信息**，选择 **功能配置** 页，开启 **旁路推流** 功能。
![](https://main.qcloudimg.com/raw/0dbafd4ba41100d7d2f50038b9232ceb.png)
>? 
>- 旁路推流的方式默认选择 `指定流旁路` 即可，对于 V2TXLivePusher 两种方式没有区别。

[](id:step42)
#### 配置推流参数
1. 找到并打开 `LiteAVSDK_Professional_iOS_版本号/MLVB-API-Example-OC/Debug/GenerateTestUserSig.h` 文件。
2. 根据上面  [服务开通](#step41) 设置  [GenerateTestUserSig.h](https://github.com/tencentyun/MLVBSDK/blob/master/iOS/MLVB-API-Example/Debug/GenerateTestUserSig.h)  文件中的相关参数：
 - SDKAppID：默认为 0 ，请设置为实际的 SDKAppID。
 - SECRETKEY：默认为空 ，请设置为实际的密钥信息。
 <img src="https://main.qcloudimg.com/raw/861170156910720be7ba980bcb625ceb.png" width=700px>

[](id:step43)
#### 推流 URL 字段说明
具体的推拉流 URL 字符串，需要开发者按照对应的协议自行拼接，拼装方案请参见 [推拉流 URL](https://cloud.tencent.com/document/product/454/7915#rtc)。Demo 中已经拼接好，运行后即可播放。

[](id:step5)
### 步骤五：编译运行
使用 Xcode（9.0及以上的版本）打开源码工程 `MLVB-API-Example-OC`，单击 **运行** 即可。
<img src="https://main.qcloudimg.com/raw/a6534c832fa80b8c818a7320873e5e1c.png" width=300px>

本文主要介绍如何快速运行腾讯云 TRTC-API-Example（Electron）。

## 前提条件
您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤
[](id:step1)
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择**开发辅助** > [**快速跑通Demo**](https://console.cloud.tencent.com/trtc/quickstart)。
2. 单击**新建应用**输入应用名称，例如 `TestTRTC`；若您已创建应用可单击**选择已有应用**。
3. 根据实际业务需求添加或编辑标签，单击**创建**。
![](https://main.qcloudimg.com/raw/f04d288ed091c98a5e8056eb86fb49e8.png)
>?
>- 应用名称只能包含数字、中英文字符和下划线，长度不能超过15个字符。
>- 标签用于标识和组织您在腾讯云的各种资源。例如：企业可能有多个业务部门，每个部门有1个或多个 TRTC 应用，这时，企业可以通过给 TRTC 应用添加标签来标记部门信息。标签并非必选项，您可根据实际业务需求添加或编辑。

[](id:step2)
### 步骤2：下载 SDK 和 TRTC-API-Example 源码

1. TRTC-API-Example 源码。
```shell script
git clone https://github.com/tencentyun/TRTCSDK
cd Electron/TRTC-API-Example
```

[](id:step3)
### 步骤3：配置 TRTC-API-Example 工程文件

1. 找到并打开 `Electron/TRTC-API-Example/assets/debug/gen-test-user-sig.js` 文件。
3. 设置 `gen-test-user-sig.js` 文件中的相关参数：
	<ul><li/>SDKAPPID：默认为 0 ，请设置为实际的 SDKAppID。
	<li/>SECRETKEY：默认为 '' ，请设置为实际的密钥信息。</ul>
	<img src="https://qcloudimg.tencent-cloud.cn/raw/a8b896a1d9a3f4527a687f34c0987b80.png">

>!
>- 本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 TRTC-API-Example 和功能调试**。
>- 正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

### 步骤4：编译运行
```shell
npm install
cd src/app/render/main-page
npm install

cd ../../..
npm run start
```

## 常见问题
### 1. 查看密钥时只能获取公钥和私钥信息，该如何获取密钥？
TRTC SDK 6.6 版本（2019年08月）开始启用新的签名算法 HMAC-SHA256。在此之前已创建的应用，需要先升级签名算法才能获取新的加密密钥。如不升级，您也可以继续使用 [老版本算法 ECDSA-SHA256](https://cloud.tencent.com/document/product/647/17275#Old)，如已升级，您按需切换为新旧算法。

升级/切换操作：
 1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/trtc)。
 2. 在左侧导航栏选择**应用管理**，单击目标应用所在行的**应用信息**。
 3. 选择**快速上手**页签，单击**第二步 获取签发UserSig的密钥**区域的 **HMAC-SHA256**。
  - 切换回老版本算法 ECDSA-SHA256：
![](https://qcloudimg.tencent-cloud.cn/raw/ba76b709e17c100798810e38c94c9f9d.png)
  - 切换为新版本算法 HMAC-SHA256：
![](https://qcloudimg.tencent-cloud.cn/raw/73d25cffe81af56353db4a874255f1bc.png)

### 2. 防火墙有什么限制？
由于 SDK 使用 UDP 协议进行音视频传输，所以在对 UDP 有拦截的办公网络下无法使用。如遇到类似问题，请参见 [应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399) 排查并解决。

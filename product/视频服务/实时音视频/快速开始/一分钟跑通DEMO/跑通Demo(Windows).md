本文主要介绍如何快速地跑通腾讯云 TRTC Demo ，您只需参考如下步骤依次执行即可。

## 步骤1：创建应用
1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/rav) ，单击【创建应用】。
2. 输入应用名称等相关信息，单击【确定】。
 应用创建完成后，自动生成一个应用标识 SDKAppID。
3. 记录 SDKAppID 信息。
![](https://main.qcloudimg.com/raw/a29e87152fb3771e44c0f812551a10ba.png)

## 步骤2：下载 SDK 和 Demo 源码
1. 单击应用卡片，进入【快速上手】页面。
2. 单击【第一步 下载SDK+配套demo源码】区域的【Windows(V2)】，跳转至 Github 并选择下载对应的 SDK 和 Demo 源码。
>?如果您当前网络访问 Github 较慢，您可以在 [项目首页](https://github.com/tencentyun/TRTCSDK) 通过分流下载地址下载相关资源。
>
![](https://main.qcloudimg.com/raw/6e78a94d6c9ce1b987f2bdbb44cd80a8.png)

## 步骤3：获取加密密钥
1. 单击【第二步 获取签发UserSig的密钥】区域的【查看密钥】，即可获取用于计算 UserSig 的加密密钥。
2. 单击【复制密钥】，将密钥拷贝到剪贴板中。
 ![](https://main.qcloudimg.com/raw/d0b780f7b28833533e12807d1b11d8be.png)

<h2 id="CopyKey"> 步骤4：配置 Demo 工程 </h2>
 Demo 源码工程中的`GenerateTestUserSig`文件可以通过 HMAC-SHA256 算法在本地计算 UserSig，用于快速跑通 Demo。您只需手动设置 SDKAppID（应用 SDKAppID）和 SECRETKEY（密钥信息）这两个成员变量的取值即可，如下图所示： 
 
![](https://main.qcloudimg.com/raw/d326435f91c68b3f4dd89f74b2c92d9d.jpg)


## 步骤5：编译运行
- C++版：使用 Visual Stuido（建议 VS2015）打开源码目录下的`MFCDemo\TRTCMfcDemo.vcxproj`工程文件，编译并运行 Demo 工程。

- C#版：使用 Visual Stuido（建议 VS2015）打开源码目录下的`CSharpDemo\TRTCCSharpDemo.csproj`工程文件，编译并运行 Demo 工程。

## 常见问题

### 1. 开发环境有什么要求？

C++ 版：

- 操作系统： Microsoft Windows 7+
- 开发环境：Microsoft Visual Studio 2015 +

C# 版：

- 操作系统： Microsoft Windows 7+
- 开发环境：Microsoft Visual Studio 2015 +
- 开发框架：.Net Framework 4.0+

### 2. 两台手机同时运行 Demo，为什么看不到彼此的画面？
请确保两台手机在运行 Demo 时使用的是不同的 UserID，TRTC 不支持同一个 UserID （除非 SDKAppID 不同）在两个终端同时使用。
![](https://main.qcloudimg.com/raw/c7b1589e1a637cf502c6728f3c3c4f99.png)

### 3. 防火墙有什么限制？
由于 SDK 使用 UDP 协议进行音视频传输，因此在对 UDP 有拦截的办公网络下无法使用。如遇类似问题，请参考 [应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399) 添加防火墙白名单。

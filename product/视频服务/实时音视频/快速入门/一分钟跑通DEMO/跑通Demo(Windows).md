本文主要介绍如何快速运行腾讯云 TRTC Demo（Windows）。

## 环境要求
**Windows（C++）开发环境**
- Microsoft Visual Studio 2015及以上版本，推荐使用 Microsoft Visual Studio 2015 
- Windows SDK 8.0及以上版本，推荐使用 Windows SDK 8.1

**Windows（C#）开发环境**
- Microsoft Visual Studio 2015及以上版本，推荐使用 Microsoft Visual Studio 2017
- .Net Framework 4.0及以上版本，推荐使用 .Net Framework 4.0

## 操作步骤
<span id="step1"></span>
### 步骤1：创建新的应用
1. 登录 [实时音视频控制台](https://console.cloud.tencent.com/rav)，单击【创建应用】。
 如果您已有应用，请记录其 SDKAppID 然后直接 [下载 SDK 和 Demo 源码](#step2)。否则，继续执行下一步。
2. 填写新建应用的应用名称等信息，单击【确定】。
 应用创建完成后，自动生成一个应用标识 SDKAppID，请记录 SDKAppID 信息。
 ![](https://main.qcloudimg.com/raw/1acc030cfc47e32bc36873c9a494b88a.png)

<span id="step2"></span>
### 步骤2：下载并解压 SDK 和 Demo 源码
>?如果您的网络环境访问 Github 过慢，建议通过**方法1**下载 SDK 和配套 Demo 源码。

**方法1**
下载 Windows 端 [SDK 和 Demo 源码](http://liteavsdk-1252463788.cosgz.myqcloud.com/TXLiteAVSDK_TRTC_Win_latest.zip)。


**方法2**
1. 单击应用卡片，进入【快速上手】页面。
2. 单击【第一步 下载SDK+配套demo源码】区域的【Windows(V2)】跳转至 [Github](https://github.com/tencentyun/TRTCSDK)（或直接访问 [Gitee](https://gitee.com/cloudtencent/TRTCSDK)），下载并解压相关 Demo 源码。
 ![](https://main.qcloudimg.com/raw/1bc8fdb853ab6b8bdf5b398c6efa1623.png)
3. 下载并解压 [SDK](https://github.com/tencentyun/TRTCSDK/tree/master/Windows/SDK) 源码。
4. 将解压 SDK 源码所得`SDK`目录下的所有文件复制并替换至 Demo 源码的`Windows/SDK`目录中。

<span id="step3"></span>
### 步骤3：查看并拷贝加密密钥
1. 单击【第二步 获取签发UserSig的密钥】区域的【查看密钥】，即可获取用于计算 UserSig 的加密密钥。
2. 单击【复制密钥】，将密钥拷贝到剪贴板中。
 ![](https://main.qcloudimg.com/raw/d0b780f7b28833533e12807d1b11d8be.png)

<h3 id="CopyKey">步骤4：配置 Demo 工程文件</h3>
 Demo 源码工程中的`GenerateTestUserSig`文件可以通过 HMAC-SHA256 算法在本地计算 UserSig，用于快速跑通 Demo。

1. 在 [步骤2](#step2) 中解压的 Demo 源码包目录中，找到并打开 `GenerateTestUserSig`文件。
  <table>
     <tr>
         <th nowrap="nowrap">适用平台</th>  
         <th nowrap="nowrap">文件相对路径</th>  
     </tr>
	 <tr>      
         <td>Windows(C++)</td>   
	     <td>Windows/DuilibDemo/GenerateTestUserSig.h</td>   
     </tr> 
	 <tr>
	     <td>Windows(C#)</td>   
	     <td>Windows/CSharpDemo/GenerateTestUserSig.cs</td>
     </tr> 
</table>
2. 设置`GenerateTestUserSig`文件中的相关参数，下图以 Windows(C++) 为例作为参考：
  - SDKAppID：请设置为 [步骤1](#step1) 中获取的实际 SDKAppID。
  - SECRETKEY：请设置为 [步骤3](#step3) 中获取的实际密钥信息。
    ![](https://main.qcloudimg.com/raw/c8dd14631e8f976944376ba58e9c1079.png)

>!本文提到的生成 UserSig 的方案是在客户端代码中配置 SECRETKEY，该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](https://cloud.tencent.com/document/product/647/17275#Server)。

### 步骤5：编译运行
- **Windows（C++）**
使用 Visual Stuido（建议 VS2015）打开源码目录下的`DuilibDemo\TRTCDuilibDemo.sln`工程文件，推荐选择 Release/X86 构建平台，编译并运行 Demo 工程即可。

- **Windows（C#）**
使用 Visual Stuido（建议 VS2017）打开源码目录下的`CSharpDemo\TRTCCSharpDemo.sln`工程文件，推荐选择 Release/X86 构建平台，编译并运行 Demo 工程即可。

## 常见问题

### 1. 查看密钥时只能获取公钥和私钥信息，要如何获取密钥？
TRTC SDK 6.6 版本（2019年08月）开始启用新的签名算法 HMAC-SHA256。在此之前已创建的应用，需要先单击【第二步 获取签发UserSig的密钥】区域的【点此升级】升级签名算法才能获取新的加密密钥。如不升级，您也可以继续使用 [老版本算法](https://cloud.tencent.com/document/product/647/17275#.E8.80.81.E7.89.88.E6.9C.AC.E7.AE.97.E6.B3.95) ECDSA-SHA256。

### 2. 两台手机同时运行 Demo，为什么看不到彼此的画面？
请确保两台手机在运行 Demo 时使用的是不同的 UserID，TRTC 不支持同一个 UserID （除非 SDKAppID 不同）在两个终端同时使用。
![](https://main.qcloudimg.com/raw/c7b1589e1a637cf502c6728f3c3c4f99.png)

### 3. 防火墙有什么限制？
由于 SDK 使用 UDP 协议进行音视频传输，所以对 UDP 有拦截的办公网络下无法使用，如遇到类似问题，请参考文档：[应对公司防火墙限制](https://cloud.tencent.com/document/product/647/34399)。

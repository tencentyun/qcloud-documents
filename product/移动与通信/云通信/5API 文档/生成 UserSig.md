本文将指导您如何生成 UserSig。

## 获取密钥 

1. 登录云通信 IM [控制台](https://console.cloud.tencent.com/avc)。
 >?如果您还没有应用，请先 [创建应用](https://cloud.tencent.com/document/product/269/3794#.E6.8E.A5.E5.85.A5.E6.AD.A5.E9.AA.A4)，然后执行 [步骤2](#step2)。
<span id="step2"></span>
2. 单击目标应用所在行的【应用配置】，进入应用详情页面。
3. 单击**帐号体系集成**右侧的【编辑】，配置**帐号管理员**信息，单击【保存】。
 ![](https://main.qcloudimg.com/raw/2ad153a77fe6f838633d23a0c6a4dde1.png)
4. 单击【查看密钥】，拷贝并保存密钥信息。
 >!请妥善保管密钥信息，谨防泄露。

## 客户端计算 UserSig
IM SDK 示例代码中提供的 `GenerateTestUserSig`的开源模块可以帮忙您快速生成 UserSig。您只需设置 SDKAPPID（应用 SDKAppID）、EXPIRETIME（UserSig 过期时间）和 SECRETKEY（密钥信息）三个成员变量的取值，然后调用 genTestUserSig() 函数即可快速获取 UserSig。
为了简化实现过程，我们提供了下列语言或平台的 UserSig 计算源码，您可以直接下载并集成到您的客户端。

|语言版本|适用平台|源码位置|
|---|---|---|
|Objective-C|Android|[Github](https://github.com/tencentyun/TIMSDK/tree/master/iOS/TUIKitDemo/TUIKitDemo/Debug/GenerateTestUserSig.h)|
|Java|Android|[Github](https://github.com/tencentyun/TIMSDK/tree/master/Android/app/src/main/java/com/tencent/qcloud/tim/demo/debug/GenerateTestUserSig.java)|
|C++|Windows|[Github](https://github.com/tencentyun/TIMSDK/blob/master/cross-platform/Windows/IMApp/IMApp/TestUserSigGenerator.cpp)|

>!该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>**正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。**更多详情请参见 [服务端生成 UserSig](#GeneratingdynamicUserSig)。

<span id="GeneratingdynamicUserSig"></span>
## 服务端计算 UserSig
采用服务端计算 UserSig，可以最大限度地保障计算 UserSig 所用的密钥信息不被泄露。您只需将计算代码部署在您的服务器上，并提供面向 App 的服务端接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。
为了简化实现过程，我们提供了下列语言或平台的 UserSig 计算源码，您可以直接下载并集成到您的服务端。

| 语言版本 | 关键函数 | 下载链接 |
|---------|---------|---------|
| Java | [genSig](https://github.com/tencentyun/tls-sig-api-v2-java/blob/master/src/main/java/com/tencentyun/TLSSigAPIv2.java) | [Github](https://github.com/tencentyun/tls-sig-api-v2-java)|
| GO | [GenSig](https://github.com/tencentyun/tls-sig-api-v2-golang/blob/master/tencentyun/TLSSigAPI.go) | [Github](https://github.com/tencentyun/tls-sig-api-v2-golang)|
| PHP | [genSig](https://github.com/tencentyun/tls-sig-api-v2-php/blob/master/src/TLSSigAPIv2.php) | [Github](https://github.com/tencentyun/tls-sig-api-v2-php)|
| Node.js | [genSig](https://github.com/tencentyun/tls-sig-api-v2-node/blob/master/TLSSigAPIv2.js) | [Github](https://github.com/tencentyun/tls-sig-api-v2-node)|
| Python | [gen_sig](https://github.com/tencentyun/tls-sig-api-v2-python/blob/master/TLSSigAPIv2.py) | [Github](https://github.com/tencentyun/tls-sig-api-v2-python)|
| C# | [GenSig](https://github.com/tencentyun/tls-sig-api-v2-cs/blob/master/tls-sig-api-v2-cs/TLSSigAPIv2.cs) | [Github](https://github.com/tencentyun/tls-sig-api-v2-cs)|


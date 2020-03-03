UserSig 是用户登录即时通信 IM 的密码，其本质是对 UserID 等信息加密后得到的密文，本文将指导您如何生成 UserSig。

## 获取密钥 

1. 登录即时通信 IM [控制台](https://console.cloud.tencent.com/im)。
 >?如果您还没有应用，请先 [创建应用](https://cloud.tencent.com/document/product/269/36838#step1)，然后执行 [步骤2](#step2)。
<span id="step2"></span>
2. 单击目标应用卡片，进入应用的基础配置页面。
3. 在【基本信息】区域，单击【密钥】右侧的【显示密钥】。
4. 单击【复制】即可复制并储存密钥信息。
 >!请妥善保管密钥信息，谨防泄露。

## 客户端计算 UserSig
IM SDK 示例代码中提供的`GenerateTestUserSig`的开源模块可以帮忙您快速生成 UserSig。您只需设置 SDKAPPID（应用 SDKAppID）、EXPIRETIME（UserSig 过期时间）和 SECRETKEY（密钥信息）三个成员变量的取值，然后调用 genTestUserSig() 函数即可快速获取 UserSig。
为了简化实现过程，我们提供了下列语言或平台的 UserSig 计算源码，您可以直接下载并集成到您的客户端。

| 编程语言 | 所属平台 | GenerateTestUserSig 源代码 |
| :---: | :---: | :---: |
| Java | Android | [GenerateTestUserSig.java](https://github.com/tencentyun/TIMSDK/blob/master/Android/app/src/main/java/com/tencent/qcloud/tim/demo/signature/GenerateTestUserSig.java)  |
| Objective-C | iOS | [GenerateTestUserSig.h](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKitDemo/TUIKitDemo/Debug/GenerateTestUserSig.h) | 
|Objective-C | Mac | [GenerateTestUserSig.h](https://github.com/tencentyun/TIMSDK/blob/master/Mac/TUIKitDemo/TUIKitDemo/Debug/GenerateTestUserSig.h) |
| C++ | Windows | [GenerateTestUserSig.h](https://github.com/tencentyun/TIMSDK/blob/master/cross-platform/Windows/IMApp/IMApp/GenerateTestUserSig.h) |
| Javascript | Web | [GenerateTestUserSig.js](https://github.com/tencentyun/TIMSDK/blob/master/H5/dist/debug/GenerateTestUserSig.js) |
| Javascript | 小程序 | [GenerateTestUserSig.js](https://github.com/tencentyun/TIMSDK/blob/master/WXMini/dist/wx/debug/GenerateTestUserSig.js) | 

>!该方法中 SECRETKEY 很容易被反编译逆向破解，一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量，因此**该方法仅适合本地跑通 Demo 和功能调试**。
>正确的 UserSig 签发方式是将 UserSig 的计算代码集成到您的服务端，并提供面向 App 的接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。更多详情请参见 [服务端生成 UserSig](#GeneratingdynamicUserSig)。

<span id="GeneratingdynamicUserSig"></span>
## 服务端计算 UserSig
采用服务端计算 UserSig，可以最大限度地保障计算 UserSig 所用的密钥信息不被泄露。您只需将计算代码部署在您的服务器上，并提供面向 App 的服务端接口，在需要 UserSig 时由您的 App 向业务服务器发起请求获取动态 UserSig。
为了简化实现过程，我们提供了下列语言或平台的 UserSig 计算源码，您可以直接下载并集成到您的服务端。

| 语言版本 | 关键函数 | 下载链接 |
|---------|---------|---------|
| Java | HMAC-SHA256 | [genSig](https://github.com/tencentyun/tls-sig-api-v2-java/blob/master/src/main/java/com/tencentyun/TLSSigAPIv2.java)  | [Github](https://github.com/tencentyun/tls-sig-api-v2-java)|
| GO | HMAC-SHA256 | [GenSig](https://github.com/tencentyun/tls-sig-api-v2-golang/blob/master/tencentyun/TLSSigAPI.go) | [Github](https://github.com/tencentyun/tls-sig-api-v2-golang)|
| PHP | HMAC-SHA256 | [genSig](https://github.com/tencentyun/tls-sig-api-v2-php/blob/master/src/TLSSigAPIv2.php) | [Github](https://github.com/tencentyun/tls-sig-api-v2-php)|
| Nodejs | HMAC-SHA256 | [genSig](https://github.com/tencentyun/tls-sig-api-v2-node/blob/master/TLSSigAPIv2.js) | [Github](https://github.com/tencentyun/tls-sig-api-v2-node)|
| Python | HMAC-SHA256 | [gen_sig](https://github.com/tencentyun/tls-sig-api-v2-python/blob/master/TLSSigAPIv2.py) | [Github](https://github.com/tencentyun/tls-sig-api-v2-python)|
| C# | HMAC-SHA256 | [GenSig](https://github.com/tencentyun/tls-sig-api-v2-cs/blob/master/tls-sig-api-v2-cs/TLSSigAPIv2.cs) | [Github](https://github.com/tencentyun/tls-sig-api-v2-cs)|
| C++ | HMAC-SHA256 | [gen_sig](https://github.com/tencentyun/tls-sig-api-v2-cpp)|


<span id="ECDSA-SHA256"></span>
## 老版本算法

为了简化签名计算难度，方便客户更快速地使用腾讯云服务，即时通信 IM 服务自2019.07.19开始启用新的签名算法，从之前的 ECDSA-SHA256 升级为 HMAC-SHA256。 2019.07.19以后创建的 SDKAppID 均会采用新的 HMAC-SHA256 算法。

如果您的 SDKAppID 是2019.07.19之前创建的，建议升级为 [HMAC-SHA256 算法](#GeneratingdynamicUserSig)。您也可以继续使用老版本的签名算法，ECDSA-SHA256 算法的源码下载链接如下：

| 语言版本 | 签名算法 | 下载链接 |
|:---------:|:---------:|:---------:|
| Java | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api-java)|
| GO | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api-golang)|
| PHP | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api-php)|
| Nodejs | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api-node)|
| Python | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api-python)|
| C# | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api-cs)|
| C++ | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api)|

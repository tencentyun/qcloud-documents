<h2 id="UserSig"> UserSig 介绍 </h2>

UserSig 是腾讯云设计的一种安全保护签名，目的是为了阻止恶意攻击者盗用您的云服务使用权。

目前，腾讯云的移动直播（MLVB）、实时音视频（TRTC）以及云通信（IM）等服务都采用了该套安全保护机制。要使用这些服务，您都需要在相应 SDK 的初始化或登录函数中提供 SDKAppID、UserID 和 UserSig 三个关键信息。

其中 SDKAppID 用于标识您的应用，UserID 用于标识您的用户，而 UserSig 则是基于前两者计算出的安全签名，它由 **HMAC SHA256** 加密算法计算得出。只要攻击者不能伪造 UserSig，就无法盗用您的云服务流量。

UserSig 的计算原理如下所示，其本质就是对 SDKAppID、UserID 和 ExpireTime 等关键信息进行了一次哈希加密：

```Cpp
//UserSig 计算公式，其中 secretkey 为计算 usersig 用的加密密钥

usersig = hmacsha256(secretkey, (userid + sdkappid + currtime + expire + 
                                 base64(userid + sdkappid + currtime + expire)))
```

<h2 id="Key">密钥获取</h2>

访问实时音视频 [控制台](https://console.cloud.tencent.com/rav) 可以查询计算 UserSig 用的密钥，方法如下：
1. 选择一个应用并进入详情页面，如果还没有应用就创建一个。
2. 进入**快速上手**页面，在右侧找到【查看密钥】按钮，单击即可获得加密密钥。

![](https://main.qcloudimg.com/raw/6b862c1c2d3534d06729d50540426bd5.png)

<h2 id="Client">客户端计算</h2>

我们在 IM SDK 的示例代码中提供了一个叫做`GenerateTestUserSig`的开源模块，您只需要将其中的 SDKAPPID、EXPIRETIME 和 SECRETKEY 三个成员变量修改成您自己的配置，就可以调用`genTestUserSig()`函数获取计算好的 UserSig，从而快速跑通 SDK 的相关功能：

| 语言版本 |  适用平台 | 源码位置 |
|:---------:|:---------:|:---------:|
| Objective-C | iOS  | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/iOS/Demo/TXLiteAVDemo/LVB/LiveRoom/Debug/GenerateTestUserSig.h)|
| Java | Android  | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/Android/Demo/app/src/main/java/com/tencent/liteav/demo/lvb/liveroom/debug/GenerateTestUserSig.java) |
| Javascript | 小程序 | [Github](https://github.com/tencentyun/MLVBSDK/tree/master/WXMini/pages/mlvb-live-room-demo/debug/GenerateTestUserSig.js)|

![](https://main.qcloudimg.com/raw/1dccb5267535b85cc1d342101dbd5224.png)


>! 该方案仅适用于调试，如果产品要正式上线，**不推荐**采用这种方案，因为客户端代码（尤其是 Web 端）中的 SECRETKEY 很容易被反编译逆向破解。一旦您的密钥泄露，攻击者就可以盗用您的腾讯云流量。
>
>正确的做法是将 UserSig 的计算代码放在您的业务服务器上，然后由您的 App 在需要的时候向您的服务器获取实时算出的 UserSig。

<h2 id="Server">服务端计算</h2>

采用服务端计算 UserSig 的方案，可以最大限度地保障计算 UserSig 用的密钥不被泄露，因为攻破一台服务器的难度要高于逆向一款 App。具体的做法如下：

1. 您的 App 在调用 SDK 的初始化函数之前，首先要向您的服务器请求 UserSig。
2. 您的服务器根据 SDKAppID 和 UserID 计算 UserSig，计算源码见文档前半部分。
3. 服务器将计算好的 UserSig 返回给您的 App。
4. 您的 App 将获得的 UserSig 通过特定 API 传递给 SDK。
5. SDK 将 SDKAppID + UserID + UserSig 提交给腾讯云服务器进行校验。
6. 腾讯云校验 UserSig，确认合法性。
7. 校验通过后，会向 TRTCSDK 提供实时音视频服务。

![](https://main.qcloudimg.com/raw/60c419d6b977fa3cc158c57c8f3f7315.png)

为了简化您的实现过程，我们提供了多个语言版本的 UserSig 计算源代码：

| 语言版本 | 签名算法 | 关键函数 | 下载链接 |
|:---------:|:---------:|:---------:|:---------:|
| Java | HMAC-SHA256 | [genSig](https://github.com/tencentyun/tls-sig-api-v2-java/blob/master/src/main/java/com/tencentyun/TLSSigAPIv2.java)  | [Github](https://github.com/tencentyun/tls-sig-api-v2-java)|
| GO | HMAC-SHA256 | [GenSig](https://github.com/tencentyun/tls-sig-api-v2-golang/blob/master/tencentyun/TLSSigAPI.go) | [Github](https://github.com/tencentyun/tls-sig-api-v2-golang)|
| PHP | HMAC-SHA256 | [genSig](https://github.com/tencentyun/tls-sig-api-v2-php/blob/master/src/TLSSigAPIv2.php) | [Github](https://github.com/tencentyun/tls-sig-api-v2-php)|
| Nodejs | HMAC-SHA256 | [genSig](https://github.com/tencentyun/tls-sig-api-v2-node/blob/master/TLSSigAPIv2.js) | [Github](https://github.com/tencentyun/tls-sig-api-v2-node)|
| Python | HMAC-SHA256 | [gen_sig](https://github.com/tencentyun/tls-sig-api-v2-python/blob/master/TLSSigAPIv2.py) | [Github](https://github.com/tencentyun/tls-sig-api-v2-python)|
| C# | HMAC-SHA256 | [GenSig](https://github.com/tencentyun/tls-sig-api-v2-cs/blob/master/tls-sig-api-v2-cs/TLSSigAPIv2.cs) | [Github](https://github.com/tencentyun/tls-sig-api-v2-cs)|


## 老版本算法

为了简化签名计算难度，方便客户更快速地使用腾讯云服务，即时通信 IM 服务自2019-08-06开始启用新的签名算法，从之前的 ECDSA-SHA256 升级为 HMAC-SHA256，也就是从2019-08-06之后创建的 SDKAppID 均会采用新的 HMAC-SHA256 算法。

如果您的 SDKAppID 是2019-07-19之前创建的，可以继续使用老版本的签名算法，算法的源码下载链接如下：

| 语言版本 | 签名算法 | 下载链接 |
|:---------:|:---------:|:---------:|
| Objective-C | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api-oc)|
| Java | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api-java)|
| C++ | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api)|
| GO | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api-golang)|
| PHP | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api-php)|
| Nodejs | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api-node)|
| C# | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api-cs)|
| Python | ECDSA-SHA256 | [Github](https://github.com/tencentyun/tls-sig-api-python)|






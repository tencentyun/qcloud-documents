移动直播中使用的 TIM 云通信组件和 MLVBLiveRoom 组件会用到 UserSig。UserSig 本质是一种签名，类似直播推流地址里的防盗链签名，只不过 UserSig 的计算方式比防盗链签名要复杂一些。

本文主要介绍 UserSig 在移动直播服务中的作用以及计算方法。

<h2 id="UserSig"> UserSig 介绍 </h2>

UserSig 是腾讯云 MLVBLiveRoom 组件和云通信 TIMSDK 会用到的一种“签名”，计算方法是对 SDKAppID、UserID 和过期时间进行非对称签名，签名算法为 ECDSA，下图展示了 UserSig 的原理。

![](https://main.qcloudimg.com/raw/dd87ed980127527e5b4b8023aa7170a7.png)

1. 您的 App 在使用 MLVBLiveRoom 组件（该组件内部会使用 TIM 云通信服务）之前，首先要向您的服务器请求 UserSig。
2. 您的服务器根据（SDKAppID + UserID）计算 UserSig，计算方法和源代码见文章下半部分。
3. 服务器将计算好的 UserSig 返回给你的 App。
4. 您的 App 将获得的 UserSig 通过接口函数（MLVBLiveRoom#login）传递给 MLVBLiveRoom 组件。
5. MLVBLiveRoom 将（SDKAppID + UserID + UserSig）提交给腾讯云服务器进行校验。
6. 腾讯云校验 UserSig，确认合法性。
7. 校验通过后，会向 MLVBLiveRoom 提供其所需的音视频、连麦和云通信服务。

<h2 id="PrivateKey"> 下载签名私钥 (PrivateKey) </h2>

首先进入【直播控制台】=>【直播SDK】=>【[应用管理](https://console.cloud.tencent.com/live/license/appmanage)】页面，如果还没有应用，就先创建一个，如果已经有应用存在，则可以点击**管理**入口，在**应用管理**页卡上，就可以看到公私钥的下载链接，如下图：

![](https://main.qcloudimg.com/raw/fa021e482fa0e89cc0030913057fb714.png)

点击**下载公私钥**链接，即可获得一个叫做 `authkeys.txt` 的文本文件，其中，下图中红框圈出的部分就是**私钥**了，它可以配合 SHA256withECDSA 算法计算出合法的 UserSig。

![](https://main.qcloudimg.com/raw/398091b0beb19a9e13c0b6d9af518c08.png)

<h2 id="Generate"> 生成 UserSig </h2>

UserSig 的计算过程，就是对 SDKAppID、UserID、过期时间等几个关键值进行非对称签名，我们准备了各个平台的示例代码，您可以直接下载后集成到你的服务器上。

| 语言版本 | 关键函数 | 下载链接 |
|:---------:|:---------:|:---------:|
| Java | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-java)|
| GO | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-golang)|
| PHP | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-php)|
| Nodejs | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-node)|
| C++ | `gen_sig` | [Github](https://github.com/tencentyun/tls-sig-api)|
| C# | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-cs)|
| Python | `gen_sig` | [Github](https://github.com/tencentyun/tls-sig-api-python)|

>! 您也可以在客户端计算 UserSig，但这就意味着您要在客户端的代码里写死 PrivateKey，这很容易导致 PrivateKey 的泄露。为了您的账号安全，我们不推荐您这样做，最安全的做法是将计算代码放在您的服务器上，这样就很大程度上避免了客户端被破解导致的 PrivateKey 泄露风险。


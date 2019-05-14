本文主要介绍 UserSig 的作用和生成方法。为了避免有恶意攻击者盗用您的通话时长，腾讯云实时音视频服务（TRTC）需要您正确的生成 UserSig 才能使用。

<h2 id="UserSig"> UserSig 介绍 </h2>

UserSig 是腾讯云实时音视频服务（TRTC）会用到的一种“签名”，计算方法是对 SDKAppID、UserID 和过期时间进行非对称签名，签名算法为 ECDSA，下图展示了 UserSig 的原理。

![](https://main.qcloudimg.com/raw/dd87ed980127527e5b4b8023aa7170a7.png)

1. 您的 App 在使用 TRTCSDK 之前，首先要向您的服务器请求 UserSig。
2. 您的服务器根据 SDKAppID + UserID 计算 UserSig，计算方法和源代码见文章下半部分。
3. 服务器将计算好的 UserSig 返回给您的 App。
4. 您的 App 将获得的 UserSig 通过接口函数（TRTCCloud#enterRoom）传递给 TRTCSDK。
5. TRTCSDK 将 SDKAppID + UserID + UserSig 提交给腾讯云服务器进行校验。
6. 腾讯云校验 UserSig，确认合法性。
7. 校验通过后，会向 TRTCSDK 提供实时音视频服务。

<h2 id="PrivateKey"> 下载签名私钥 (PrivateKey) </h2>

进入腾讯云实时音视频 [控制台](https://console.cloud.tencent.com/rav)，创建一个应用，单击应用名称进入应用详情页面，即可以获得签名用的私钥下载链接：

![](https://main.qcloudimg.com/raw/8d4b35085f3e774d70f403f92d273d4b.png)

单击【点击下载公私钥】，会得到 **keys.zip** 的压缩文件，解压后会生成 **private_key** 和 **public_key** 两个文件，其中 **private_key** 就是我们需要的私钥文件。

![](https://main.qcloudimg.com/raw/9df4f826d9ccc9c3d1a3ab1021f99dfb.png)

<h2 id="GetForDebug"> 控制台生成 </h2>

在应用详情页面，将私钥文件内容拷贝到第三步即“**生成 Demo 配置文件内容**”的输入框中，再单击【生成Demo配置文件内容】，即可生成一个 JSON 文件，文件中有一组或多组 userid 和 usersig。

![](https://main.qcloudimg.com/raw/5de8161bb72b2e19ebdb24ef6056751c.png)

这一批 userid 和 usersig 可以直接在我们提供的 Demo 中使用，便于您快速开始测试及调试。

<h2 id="Generate"> 生成 UserSig </h2>

UserSig 的计算过程，就是对 SDKAppID、UserID 及过期时间等几个关键值进行非对称签名，我们准备了各个平台的示例代码，您可以直接下载后集成到自己的服务器上。

| 语言版本 | 关键函数 | 下载链接 |
|:---------:|:---------:|:---------:|
| Java | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-java)|
| GO | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-golang)|
| PHP | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-php)|
| Nodejs | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-node)|
| C++ | `gen_sig` | [Github](https://github.com/tencentyun/tls-sig-api)|
| C# | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-cs)|
| Python | `gen_sig` | [Github](https://github.com/tencentyun/tls-sig-api-python)|

>! 您也可以在客户端计算 UserSig，但需要您在客户端的代码里写死 PrivateKey，这很容易导致 PrivateKey 泄露。为了您的账号安全，我们不推荐这种方法。最安全的方法是将计算代码放在您自己的服务器上，这样可以避免客户端被破解导致 PrivateKey 泄露的风险。


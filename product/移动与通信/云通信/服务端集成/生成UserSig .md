<h2 id="Generate"> 生成 UserSig </h2

<h3 id="PrivateKey"> 下载签名用的私钥 </h3>

进入腾讯云通信 [控制台](https://console.cloud.tencent.com/avc)，如果还没有应用就创建一个，之后进入**应用配置**页面，在既可以获得签名用的私钥下载链接：

![](https://main.qcloudimg.com/raw/e3ce0ef527d2d4f8d0b3a0f69cefa78e.png)

点击下载，会得到一个叫做 **keys.zip** 的压缩文件，解压后会获得一个叫做 **private_key** 和一个叫做 **public_key** 的文件，其中 **private_key** 就是我们所需要的私钥文件。

![](https://main.qcloudimg.com/raw/95875a7baca63c21103bc6cd6dac0279.png)

<h3 id="GetForDebug"> 控制台手工生成 </h3>

在 **应用配置** 页面，将私钥文件拷贝到 **开发辅助工具** 下的的文本框中，再点击**生成**按钮，即可获得一个签名文件即UserSig。

![](https://main.qcloudimg.com/raw/bddde13761941c5b1919d35d75174694.png)

生成的SdkAppid、Identifier和UserSig可以直接用在我们提供的 Demo 中，便于您快速开始测试和调试。但真正要线上使用，肯定不适合采用这种做法，而是推荐采用下面介绍的服务端方案。

<h3 id="GetFromServer"> 服务器自动计算</h3>

#### 计算原理

- 将计算代码部署在您的服务器上，并提供面向 App 的服务端接口。
- 使用上面提到的 private_key 对 SdkAppid、identifier 和 expire（签名过期时间）进行实时非对称加密，并将计算结果返回给 App。
- 如果出现 private_key 泄露的问题，可以通过 400 电话联系我们进行更换。

```
  UserSig = 非对称加密（private_key, sdkappid, identifier, expire）
```

#### 源码下载

我们提供了 java、php 和 nodejs 三个版本的 UserSig 计算代码，您可以直接下载并集成到您的服务端。

| 语言版本 | 关键函数 | 下载链接 |
|:---------:|:---------:|:---------:|
| java | `genUserSig` | [Github](https://github.com/TencentVideoCloudMLVBDev/usersig_server_source/tree/master/java)|
| php | `genUserSig` | [Github](https://github.com/TencentVideoCloudMLVBDev/usersig_server_source/tree/master/php)|
| nodejs | `genUserSig` | [Github](https://github.com/TencentVideoCloudMLVBDev/usersig_server_source/tree/master/nodejs)|








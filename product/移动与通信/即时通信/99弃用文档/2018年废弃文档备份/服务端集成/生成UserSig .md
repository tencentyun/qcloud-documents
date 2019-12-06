## UserSig 生成指引

### 下载签名用的私钥 

进入腾讯云通信 [控制台](https://console.cloud.tencent.com/avc)，如果还没有应用，请新创建一个应用。进入**应用配置**页面，既可以获得签名用的私钥下载链接：

![](https://main.qcloudimg.com/raw/e3ce0ef527d2d4f8d0b3a0f69cefa78e.png)

点击下载，会得到一个叫做 **keys.zip** 的压缩文件，解压后会获得一个叫 **private_key** 和一个叫 **public_key** 的文件，其中 **private_key** 就是我们所需要的私钥文件。

![](https://main.qcloudimg.com/raw/95875a7baca63c21103bc6cd6dac0279.png)

### 控制台手工生成 UserSig

在 **应用配置** 页面，将私钥文件内容拷贝到 **开发辅助工具** 下的的文本框中，指定用户名，点击**生成**按钮，即可获得该云通信应用指定用户名的 UserSig。

![](https://main.qcloudimg.com/raw/39f858a08717d90aba5ebc1ee7f32348.png)

Identifier 和 UserSig 可以直接用在我们提供的 Demo 中，便于您快速测试和调试。
>!
> 真正要线上使用，不能采用这种做法，会有极大的安全隐患，需要使用下文介绍的服务端方案。

### 服务器生成 UserSig

#### 生成原理

- 将生成代码部署在您的服务器上，并提供面向 App 的服务端接口。
- 使用上文提到的 private_key 对 SdkAppid、Identifier 和 Expire（签名过期时间）进行非对称加密运算，并将计算结果返回给 App。
- 如果出现 private_key 泄露的情况，请[提交工单](/document/product/269/3916#.E4.BF.AE.E6.94.B9.E6.AF.8F.E6.97.A5.E5.88.9B.E5.BB.BA.E7.BE.A4.E7.BB.84.E9.85.8D.E9.A2.9D)进行更换。

```
  UserSig = 非对称加密（private_key, SdkAppid, Identifier, Expire）
```

#### 源码下载

我们提供了 java、php 和 nodejs 三个版本的 UserSig 生成代码，您可以直接下载并集成到您的服务端。

| 语言版本 | 关键函数 | 下载链接 |
|:---------:|:---------:|:---------:|
| java | `genUserSig` | [Github](https://github.com/TencentVideoCloudMLVBDev/usersig_server_source/tree/master/java)|
| php | `genUserSig` | [Github](https://github.com/TencentVideoCloudMLVBDev/usersig_server_source/tree/master/php)|
| nodejs | `genUserSig` | [Github](https://github.com/TencentVideoCloudMLVBDev/usersig_server_source/tree/master/nodejs)|








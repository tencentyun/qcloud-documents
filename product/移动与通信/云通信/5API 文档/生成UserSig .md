## UserSig 生成指引

### 下载签名用的私钥 

登录云通信 [控制台](https://console.cloud.tencent.com/avc)，如果您还没有应用，请新创建一个应用，完成新建应用后获得应用的 SdkAppId，单击对应 SdkAppId 的应用配置链接，在应用详情页，找到当前页面的**帐号体系集成**部分，单击**编辑**链接，配置**账号管理员**信息，然后单击【保存】，即可看到【下载公私钥】按钮：
![](https://main.qcloudimg.com/raw/e3ce0ef527d2d4f8d0b3a0f69cefa78e.png)

单击【下载公私钥】按钮，会得到一个 **keys.zip** 的压缩文件，解压后会获得一个 **private_key** 和一个 **public_key** 的文件，其中 **private_key** 就是我们所需要的私钥文件。
![](https://main.qcloudimg.com/raw/95875a7baca63c21103bc6cd6dac0279.png)

### 控制台手工生成 UserSig

在 **应用配置** 页面，将私钥文件内容拷贝到 **开发辅助工具** 下的的文本框中，指定用户名，单击**生成**按钮，即可获得该云通信应用指定用户名的 UserSig。
![](https://main.qcloudimg.com/raw/39f858a08717d90aba5ebc1ee7f32348.png)

Identifier 和 UserSig 可以直接用在我们提供的 Demo 中，便于您快速测试和调试。
>!真正要线上使用，不能采用这种做法，会有极大的安全隐患，需要使用下文介绍的服务器生成 UserSig 方案。


### 服务器生成 UserSig
#### 生成原理

- 将生成代码部署在您的服务器上，并提供面向 App 的服务端接口。
- 使用上文提到的 private_key 对 SdkAppid、Identifier 和 Expire（签名过期时间）进行非对称加密运算，并将计算结果返回给 App。
- 如果出现 private_key 泄露的情况，请根据 [云通信配置变更需求工单](https://cloud.tencent.com/document/product/269/3916#.E4.BF.AE.E6.94.B9.E6.AF.8F.E6.97.A5.E5.88.9B.E5.BB.BA.E7.BE.A4.E7.BB.84.E9.85.8D.E9.A2.9D) 模版给我们 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=29&level2_id=40&source=0&data_title=%E4%BA%91%E9%80%9A%E4%BF%A1%20%20IM&step=1) 进行更换。

```
  UserSig = 非对称加密（private_key, SdkAppid, Identifier, Expire）
```

#### 源码下载

我们提供了 Java、PHP 和 Nodejs 三个版本的 UserSig 生成代码，您可以直接下载并集成到您的服务端。

| 语言版本 | 关键函数 | 下载链接 |
|:---------:|:---------:|:---------:|
| java | `genUserSig` | [Github](https://github.com/TencentVideoCloudMLVBDev/usersig_server_source/tree/master/java)|
| php | `genUserSig` | [Github](https://github.com/TencentVideoCloudMLVBDev/usersig_server_source/tree/master/php)|
| nodejs | `genUserSig` | [Github](https://github.com/TencentVideoCloudMLVBDev/usersig_server_source/tree/master/nodejs)|








本文将指导您如何生成 UserSig。
## 下载签名用的私钥 

1. 登录云通信 IM [控制台](https://console.cloud.tencent.com/avc)。
 >?如果您还没有应用，请先 [创建应用](https://cloud.tencent.com/document/product/269/3794#.E6.8E.A5.E5.85.A5.E6.AD.A5.E9.AA.A4)，然后执行 [步骤2](#step2)。
<span id="step2"></span>
2. 单击目标应用所在行的【应用配置】，进入应用详情页面。
 ![](https://main.qcloudimg.com/raw/e41602a50754be9d478b9db84c0bcff2.png)
3. 单击**帐号体系集成**右侧的【编辑】，配置**帐号管理员**信息，单击【保存】。
 ![](https://main.qcloudimg.com/raw/2ad153a77fe6f838633d23a0c6a4dde1.png)
4. 单击【下载公私钥】，保存 **keys.zip** 压缩文件。
 ![](https://main.qcloudimg.com/raw/c44938b9268d0ef76c68b8bf61689219.png)
5. 解压 **keys.zip**文件 ，获得 **private_key.txt** 和 **public_key.txt** 文件，其中 **private_key.txt** 即为私钥文件。
 ![](https://main.qcloudimg.com/raw/ec89f5bb93d57de1acffa4e15786da11.png)

## 控制台手动生成 UserSig
1. 登录云通信 [控制台](https://console.cloud.tencent.com/avc)。
 >?如果您还没有应用，请先 [创建应用](https://cloud.tencent.com/document/product/269/3794#.E6.8E.A5.E5.85.A5.E6.AD.A5.E9.AA.A4)，然后执行 [步骤2](#step2)。
<span id="step2"></span>
2. 单击目标应用所在行的【应用配置】，进入应用详情页面。
 ![](https://main.qcloudimg.com/raw/13e78d26c8b813e8d54f257f31384668.png)
3. 选择【开发辅助工具】页签，填写【用户名（UserID）】，拷贝私钥文件内容至【私钥（PrivateKey）】文本框中，单击【生成签名】，在【签名（UserSig）】文本框中即可获得该云通信应用指定用户名的 UserSig。
 ![](https://main.qcloudimg.com/raw/f491ffbd8dc3c0e8659288d27152c847.png)

UserID 和 UserSig 可以直接用在我们提供的 Demo 中，便于您快速测试和调试。

>!真正需要线上使用时，不能采用控制台手动生成 UserSig 方案，会有极大的安全隐患，建议使用下文介绍的服务器生成 UserSig 方案。

## 服务器生成 UserSig
### 生成原理

- 将生成代码部署在您的服务器上，并提供面向 App 的服务端接口。
- 使用上文提到的 private_key 对 SDKAppID、Identifier 和 Expire（签名过期时间）进行非对称加密运算，并将计算结果返回给 App。
- 如果出现 private_key 泄露的情况，请 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=29&level2_id=40&source=0&data_title=%E4%BA%91%E9%80%9A%E4%BF%A1%20%20IM&step=1) 申请更换。

```
  UserSig = 非对称加密（private_key, SdkAppid, Identifier, Expire）
```

### 源码下载

我们提供了下列语言或平台的 UserSig 生成代码，您可以直接下载并集成到您的服务端。

| 语言版本 | 关键函数 | 下载链接 |
|---------|---------|---------|
| Java | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-java)|
| GO | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-golang)|
| PHP | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-php)|
| C# | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-cs)|
| Nodejs | `genSig` | [Github](https://github.com/tencentyun/tls-sig-api-node)|
| C++ | `gen_sig` | [Github](https://github.com/tencentyun/tls-sig-api)|
| Python | `gen_sig` | [Github](https://github.com/tencentyun/tls-sig-api-python)|


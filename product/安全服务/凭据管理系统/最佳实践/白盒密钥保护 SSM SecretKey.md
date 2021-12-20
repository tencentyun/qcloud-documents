## 背景
调用凭据管理系统（SSM）服务时，将会使用到腾讯云账号的 SecretKey 作为身份的认证，其中大部分用户直接以 SecretKey 的明文形式存储，例如明文暴露在代码中、放置在配置中心、上传至 Git 等方式，风险系数极大。

为了能保障端到端的全链路数据安全，防止 SecretKey 的明文泄露，可以结合密钥管理系统（KMS）的白盒密钥解决方案，以密文的形式来存储 SecretKey。

在白盒密钥管理解决方案中，将密钥和算法进行融合，有效的将密钥隐藏起来，大大增加密钥被嗅探、被破解的难度，从而保护密钥这一极其敏感的信息，提升端到端全链路的安全性。

## 操作流程
![](https://qcloudimg.tencent-cloud.cn/raw/68c39f2d1a322e70877f893a5cd8f641.png)
#### 步骤1：创建 SSM 凭据对象
a. 用户在凭据管理系统 SSM 中创建一个凭据对象，关于创建凭据，详情请参见 [创建凭据](https://cloud.tencent.com/document/product/1140/40865)。

#### 步骤2：白盒密钥加密
b. 用户使用密钥管理系统 KMS 的白盒密钥对 SecretKey 进行加密，具体操作步骤如下所示。
 &nbsp;&nbsp;i. [创建白盒密钥 ](https://cloud.tencent.com/document/product/573/54236#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E5.88.9B.E5.BB.BA.E7.99.BD.E7.9B.92.E5.AF.86.E9.92.A5)。
   &nbsp;&nbsp;ii. [控制台获取 API SecretKey](https://cloud.tencent.com/document/product/573/54236#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E6.8E.A7.E5.88.B6.E5.8F.B0.E8.8E.B7.E5.8F.96-api-secretkey)。
   &nbsp;&nbsp;iii. [使用白盒密钥加密 API SecretKey](https://cloud.tencent.com/document/product/573/54236#.E6.AD.A5.E9.AA.A44.EF.BC.9A.E4.BD.BF.E7.94.A8.E7.99.BD.E7.9B.92.E5.AF.86.E9.92.A5.E5.8A.A0.E5.AF.86-api-secretkey)。
 
c. 加密完成后，获取对应的密文和初始化向量，并下载解密密钥和解密 SDK 文件。
>?白盒加密的整体操作，详情请参见 [使用 KMS 白盒密钥保护 SecretKey 最佳实践](https://cloud.tencent.com/document/product/573/54236) 。
>
d. 部署白盒解密 SDK。

#### 步骤3：应用系统需要访问 SSM，获取凭据明文
e. 首先在业务逻辑中调用白盒 SDK 的解密函数，获取到 SecretKey 的明文，接口详情请参见 [白盒密钥解密代码示例](https://cloud.tencent.com/document/product/573/54237)。
f. 应用系统通过白盒解密接口所返回的 SecretKey 明文，再向凭据管理系统 SSM 请求访问凭据，接口详情请参见 [获取凭据明文](https://cloud.tencent.com/document/product/1140/40522)。 
>! 白盒解密的整个过程是在本地内存中运行的，不依赖于网络和外部的服务。

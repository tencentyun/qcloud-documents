## 背景
调用凭据管理系统（SSM）服务时，将会使用到腾讯云账号的 SecretKey 作为身份的认证，其中大部分用户直接以 SecretKey 的明文形式存储，例如明文暴露在代码中、放置在配置中心、上传至 Git 等等方式，风险系数极大。

为了能保障端到端的全链路数据安全，防止 SecretKey 的明文泄露，可以结合密钥管理系统（KMS）的白盒密钥解决方案，以密文的形式来存储 SecretKey。

在白盒密钥管理解决方案中，将密钥和算法进行融合，有效的将密钥隐藏起来，大大增加密钥被嗅探、被破解的难度，从而保护密钥这一极其敏感的信息，提升端到端全链路的安全性。

## 操作流程
![](https://qcloudimg.tencent-cloud.cn/raw/7740e927a8a436b0415854b47dfc0201.png)
1. 用户在凭据管理系统（SSM）中创建一个凭据对象，关于创建凭据，详情请参见 [创建凭据](https://cloud.tencent.com/document/product/1140/40865)。
2. 用户使用密钥管理系统（KMS）的白盒密钥对 SecretKey 进行加密：
 - 具体步骤： 创建白盒密钥 → 获取 SecretKey →  使用白盒密钥加密 SecretKey →  获取密文+初始化向量，下载解密密钥+解密 SDK 文件 
 - 白盒加密的整体操作，详情请参见 [使用 KMS 白盒密钥保护 SecretKey 最佳实践](https://cloud.tencent.com/document/product/573/54236) 。
3. 当应用系统需要访问 SSM 时：
 - 首先在业务逻辑中调用白盒 SDK 的解密函数，获取到 SecretKey 的明文，接口详情请参见 [白盒密钥解密代码示例](https://cloud.tencent.com/document/product/573/54237)。
 - 应用系统通过白盒解密接口所返回的 SecretKey 明文，再向凭据管理系统 SSM 请求访问凭据，接口详情请参见 [获取凭据明文](https://cloud.tencent.com/document/product/1140/40522)。 

>! 白盒解密的整个过程是在本地内存中运行的，不依赖于网络和外部的服务。

根据 CA/Browser Forum 规定，**自2021年06月01日起**，将强制要求使用密钥长度至少为3072位来颁发新的（新申请/重颁发/续签）代码签名证书。

根据上述规定，腾讯云 DigiCert 和 GlobalSign 品牌代码签名证书将有如下变更：
 
### DigiCert
**更新时间：2021年5月28日**
- 2021年5月28日之后，DigiCert 品牌所颁发（新申请/续费/重颁发）的代码签名证书，RSA 算法的密钥长度大于或等于3072位。
- 2021年5月28日之后，DigiCert 品牌所颁发（新申请/续费/重颁发）的 EV 代码签名证书，USB 令牌（Token）或 HSM 支持3072位密钥。

>?变更前，USB 令牌（Token）或 HSM 只支持2048位。

代码签名证书链变更如下：
- **RSA**：DigiCert Trusted G4 Code Signing RSA4096 SHA384 2021 CA1 变更为 DigiCert Trusted Root G4
- **ECC**：DigiCert Global G3 Code Signing ECC SHA384 2021 CA1 变更为 DigiCert Global Root G3


### GlobalSign
**更新时间：2021年5月31日**
- 2021年5月31日之后，GlobalSign 品牌所颁发（新申请/续费/重颁发）的代码签名证书，RSA 算法的密钥长度大于或等于4096位。
- 2021年5月31日之后，GlobalSign 品牌所颁发（新申请/续费/重颁发）的 EV 代码签名证书，USB 令牌（Token）或 HSM 支持4096位密钥。

>?
>- 由于时间戳服务是代码签名长期有效的重要组成部分，因此时间戳 URL 也做了相应更新，迁移至新 R6 代码签名时间戳 `URL(timestamp.globalsign.com/tsa/r6advanced1)`，旧版 `R3 TSA URL(rfc3161timestamp.globalsign.com/advanced)` 已被弃用，并将时间戳服务的加密长度从2048位更改为3072位密钥。
>- 如您的代码签名不使用时间戳服务，则在 Windows 中尝试加载运行已经过期证书的 Active-X 控件时会收到警告提示 “为帮助保护您的安全，IE 已经停止从此站点安装 ActiveX 控件到您的计算机”。即对于未添加时间戳服务的代码签名，签名证书过期后对签名有效性验证的处理方式将等同于未签名的代码。
因此，当您在进行代码签名操作时，为保持签名机的网络通畅，请在您的代码添加签名时间戳服务。
>- 变更后对已颁发的代码签名证书无影响，您可放心使用。

根据 CA /B论坛（CA/Browser Forum）规定，**自2021年06月01日起**，将强制要求使用至少 3072 位的密钥长度来颁发新的（新申请/重颁发/续签）代码签名证书。

根据上述规定腾讯云 DigiCert 和 GlobalSign 品牌代码签名证书将有如下变更：
 
### DigiCert
**更新时间：2021年5月28日**
- 2021.5.28之后，DigiCert 品牌所颁发(新申请/续费/重颁发)的代码签名证书，RSA算法的密钥强度大于或等于 3072 位。
- 2021.5.28之后，EV代码签名支持 3072 位的 USB 令牌（Token）或 HSM。

>变更前，USB令牌（Token）或 HSM 只支持 2048 位。

代码签名证书链变更如下：
- RSA：
DigiCert Trusted G4 Code Signing RSA4096 SHA384 2021 CA1 变更为 DigiCert Trusted Root G4
- ECC：
DigiCert Global G3 Code Signing ECC SHA384 2021 CA1   变更为 DigiCert Global Root G3


### GlobalSign
**更新时间：2021年5月31日**
- 2021.5.31之后，新颁发(新申请/续费/重颁发)的代码签名证书，RSA算法的密钥强度大于或等于 4096 位。
- 2021.5.31之后，新颁发(新申请/续费/重颁发)的 EV 代码签名证书 USB 令牌（Token）或 HSM 支持 4096 位密钥。

>?
>- 由于时间戳服务是代码签名长期有效的重要组成部分，因此时间戳 URL 也做了更新，迁移到了新 R6 代码签名时间戳 `URL(timestamp.globalsign.com / tsa / r6advanced1) `，旧版 `R3 TSA URL(rfc3161timestamp.globalsign.com /advanced)` 已被弃用。并将密钥长度从 2048 位更改为 3072 位密钥。
>- 变更后对已颁发的代码签名证书无影响，您可放心使用。
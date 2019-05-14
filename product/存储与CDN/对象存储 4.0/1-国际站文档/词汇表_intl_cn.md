### APPID
APPID 是腾讯云账户的账户标识之一，用于关联云资源。在用户成功申请腾讯云账户后，系统自动为用户分配一个 APPID，一个 APPID 下可以创建多个项目。可通过 [腾讯云控制台](https://console.cloud.tencent.com/developer) 【账号信息】查看 APPID。
### 存储桶
存储桶即 Bucket ，在 COS 中用于存储对象。一个存储桶中可以存储多个对象。更多详细信息，请参阅 [存储桶概述](https://cloud.tencent.com/document/product/436/6244)。
### 对象
对象即 Object，COS 中存储的基本单元。更多详细信息，请参阅 [对象概述](https://cloud.tencent.com/document/product/436/6254)。
### SecretId 
SecretId & SecretKey 合称为云 API 密钥，是用户访问腾讯云 API 进行身份验证时需要用到的安全凭证。SecretId 用于标识 API 调用者身份。一个 APPID 可以创建多个云 API 密钥，若用户还没有云 API 密钥，则需要在 [云 API 密钥控制台](https://console.cloud.tencent.com/capi) 新建，否则就无法调用云 API 接口。
### SecretKey
SecretId & SecretKey 合称为云 API 密钥，是用户访问腾讯云 API 进行身份验证时需要用到的安全凭证。SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。一个 APPID 可以创建多个云 API 密钥，若用户还没有云 API 密钥，则需要在 [云 API 密钥控制台](https://console.cloud.tencent.com/capi) 新建，否则就无法调用云 API 接口。

### 项目
项目为一个虚拟概念，用户可以在一个账户下面建立多个项目，每个项目中管理不同的资源。用户可以从控制台访问 [项目管理](https://console.cloud.tencent.com/project)。

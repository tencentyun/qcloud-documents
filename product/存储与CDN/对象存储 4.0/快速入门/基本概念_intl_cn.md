想要充分利用 COS，您需要了解一些相关的基本概念和术语。
### 存储桶
存储桶即 Bucket ，在 COS 中用于存储对象。一个存储桶中可以存储多个对象。更多详细信息，请参阅 [存储桶管理](https://cloud.tencent.com/document/product/436/6244)。
### 对象
对象即 Object，COS 中存储的基本单元。更多详细信息，请参阅 [对象管理](https://cloud.tencent.com/document/product/436/6254)。
### 地域
地域即 Region，表示 COS 的数据中心所在的地域。用户可以根据费用、请求来源等综合选择数据存储的地域。建议根据自己的业务场景选择就近的地域存储，可以提高对象上传、下载速度。详细请参阅 [COS 的可用地域](https://cloud.tencent.com/document/product/436/6224)。
地域是在创建存储桶的时候指定的，一旦指定之后就不允许更改。该存储桶下所有的对象都存储在对应的数据中心，目前不支持对象级别的地域设置。
### APPID
APPID 是腾讯云账户的账户标识之一，用于关联云资源。在用户成功申请腾讯云账户后，系统自动为用户分配一个 APPID，一个 APPID 下可以创建多个项目。可通过 [腾讯云控制台](https://console.cloud.tencent.com/developer) 【账号信息】查看 APPID。
### 项目
项目为一个虚拟概念，用户可以在一个账户下面建立多个项目，每个项目中管理不同的资源。用户可以从控制台访问 [项目管理](https://console.cloud.tencent.com/project)。
### SecretId 
SecretId & SecretKey 合称为云 API 密钥，是用户访问腾讯云 API 进行身份验证时需要用到的安全凭证。SecretId 用于标识 API 调用者身份。一个 APPID 可以创建多个云 API 密钥，若用户还没有云 API 密钥，则需要在 [云 API 密钥控制台](https://console.cloud.tencent.com/capi) 新建，否则就无法调用云 API 接口。
### SecretKey
SecretId & SecretKey 合称为云 API 密钥，是用户访问腾讯云 API 进行身份验证时需要用到的安全凭证。SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。一个 APPID 可以创建多个云 API 密钥，若用户还没有云 API 密钥，则需要在 [云 API 密钥控制台](https://console.cloud.tencent.com/capi) 新建，否则就无法调用云 API 接口。
### 默认访问地址
默认访问地址由 APPID、存储桶名、COS 地域标识和对象名组成，通过默认访问域名可寻址 COS 中唯一对应的对象。更多信息请参阅 [域名管理](https://cloud.tencent.com/document/product/436/6252)。

### CDN 加速访问地址
CDN 加速访问地址由 APPID、存储桶名、CDN 加速标识以及对象名组成，通过该地址可寻址 COS 中唯一对应的地址。
CDN 加速访问地址通过 CDN 节点中转文件实现加速访问，更多信息请参阅 [域名管理](https://cloud.tencent.com/document/product/436/6252)。

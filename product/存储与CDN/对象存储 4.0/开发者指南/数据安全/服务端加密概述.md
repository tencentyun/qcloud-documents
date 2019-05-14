## 概述

对象存储 COS 在数据写入数据中心内的磁盘之前，支持在对象级别上应用数据加密的保护策略，并在访问数据时自动解密。加密和解密这一操作过程都是在服务端完成，这种服务端加密功能可以有效保护静态数据。

>!
> - 服务端加密功能目前仅支持北京、上海、广州地域。
> - 访问加密对象与访问未加密的对象在体验上并无差别，但前提是用户已拥有对对象的访问权限。
> - 服务端加密仅加密对象数据而不加密对象元数据，而且使用服务端加密的对象必须使用有效签名访问，不可被匿名用户访问。

## 适用场景

- **私密数据存储场景：**对于私密数据的存储，服务端加密可以对存储的数据进行加密，保证用户的隐私，用户访问时会自动解密。
- **私密数据传输场景：**对于私密数据的传输，COS 提供用 HTTPS 部署 SSL 证书实现加密的功能，在传输链路层上建立加密层，确保数据在传输过程中不会被窃取及篡改。

## 加密方式
COS 支持三种不同的服务端加密方式：SSE-COS、SSE-KMS 和 SSE-C。用户可以自行选择合适的加密方式对存放到 COS 中的数据进行加密。

### SSE-COS 加密
SSE-COS：即 COS 托管密钥的服务端加密。由腾讯云 COS 托管主密钥和管理数据。用户通过 COS 直接对数据进行管理和加密。SSE-COS 采用了多因素强加密，确保使用唯一的密钥加密每个对象，同时采用256位高级加密标准（即 AES-256）来加密数据，并且会通过定期轮换的主密钥来对密钥本身进行加密。

>!
>- 当使用 POST 操作上传对象时，需在表单字段中提供相同的信息，而不是提供 x-cos-server-side-encryption 头部。详情请参阅 [POST Object](https://cloud.tencent.com/document/product/436/14690)。
>- 对于使用预签名 URL 上传的对象，则无法使用 SSE-COS 加密。只能使用 COS 控制台或 HTTP 请求头部指定服务端加密。

#### 使用对象存储控制台
用户可以参阅 [设置对象加密](https://cloud.tencent.com/document/product/436/33366) 控制台文档，了解如何通过控制台对对象进行加密。

#### 使用 REST API

>!
>- 在列出存储桶中对象时，列表会返回所有对象的列表，无论对象是否加密。
>- 当使用 POST 操作上传对象时，请在表单字段中提供相同的信息，而不是提供该请求头部，详情请参阅 [POST Object](https://cloud.tencent.com/document/product/436/14690)。

COS 提供 REST API 与服务端加密相关的接口，在创建对象时可以通过提供 x-cos-server-side-encryption 头部来请求服务端加密。当用户执行以下 PUT、分块上传和 Copy 操作时，需要提供 x-cos-server-side-encryption 头部。当使用 POST 操作上传对象时，请在表单字段中提供相同的信息，不需提供该请求头部，详情请参阅 [POST Object](https://cloud.tencent.com/document/product/436/14690)。以下操作支持此头部：

- [PUT Object](https://cloud.tencent.com/document/product/436/7749)
- [Initiate Multipart Upload](https://cloud.tencent.com/document/product/436/7746)
- [PUT Object - Copy](https://cloud.tencent.com/document/product/436/10881)

### SSE-KMS 加密
SSE-KMS：即腾讯云 KMS 托管密钥的服务端加密。由腾讯云 KMS 管理数据密钥，用户管理腾讯云 KMS 中的主密钥。腾讯云 KMS 提供两种主密钥类型，一种普通密钥类型，另一种为量子密钥类型，分别满足用户的不同需求，详情请参阅 [密钥管理服务 KMS](https://cloud.tencent.com/document/product/573)。

#### 使用对象存储控制台
用户可以参阅 [设置对象加密](https://cloud.tencent.com/document/product/436/33366) 控制台文档，了解如何通过控制台对对象进行加密。

#### 使用 REST API
当用户执行以下 PUT、分块上传、POST 和 Copy 操作时，需要提供 x-cos-server-side-encryption 头部，以下操作支持此头部：

- [PUT Object](https://cloud.tencent.com/document/product/436/7749)
- [Initiate Multipart Upload](https://cloud.tencent.com/document/product/436/7746)
- [POST Object](https://cloud.tencent.com/document/product/436/14690)
- [PUT Object - Copy](https://cloud.tencent.com/document/product/436/10881)


### SSE-C 加密

SSE-C：即用户自定义密钥的服务端加密。加密密钥由用户自己提供，用户在上传对象时，COS 将使用用户提供的加密密钥对用户的数据进行 AES-256 加密。

>!
>- COS 不存储用户提供的加密密钥，而是存储加密密钥添加了随机数据的 HMAC 值，该值用于验证用户访问对象的请求。COS 无法使用随机数据的 HMAC 值来推导出加密密钥的值或解密加密对象的内容。因此，如果用户丢失了加密密钥，则无法再次获取到该对象。
>- SSE-C 仅能通过 API 进行使用，不支持控制台操作。

#### 使用 REST API
当用户执行以下 GET、HEAD、 PUT、POST 和分块上传操作时，需要提供 x-cos-server-side-encryption 头部，以下操作支持此头部：

- [GET Object](https://cloud.tencent.com/document/product/436/7753)
- [HEAD Object](https://cloud.tencent.com/document/product/436/7745)
- [PUT Object](https://cloud.tencent.com/document/product/436/7749)
- [Initiate Multipart Upload](https://cloud.tencent.com/document/product/436/7746)
- [Upload Part](https://cloud.tencent.com/document/product/436/7750)
- [POST Object](https://cloud.tencent.com/document/product/436/14690)
- [PUT Object - Copy](https://cloud.tencent.com/document/product/436/10881)


如果需要对上传的对象进行加密，我们支持以下加密方式。

#### 使用 COS 托管加密密钥的服务端加密（SSE-COS）保护数据

由腾讯云 COS 托管主密钥和管理数据。COS 会帮助您在数据写入数据中心时自动加密，并在您取用该数据时自动解密。目前支持使用 COS 主密钥对数据进行 AES-256 加密。

SDK 通过调用 `put_object` 来完成，

[//]: # (.cssg-snippet-put-object-sse)
```py
response = client.put_object(
    Bucket='examplebucket-1250000000',
    Body=b'bytes'|file,
    Key='exampleobject',
    ServerSideEncryption='AES256'
)
```

#### 使用客户提供的加密密钥的服务端加密 （SSE-C）保护数据

加密密钥由用户自己提供，用户在上传对象时，COS 将使用用户提供的加密密钥对用户的数据进行 AES-256 加密。SDK 通过调用 `put_object` 方法来完成。

> !
>- 该加密所运行的服务需要使用 HTTPS 请求。
>- customerKey：用户提供的密钥，传入一个32字节的字符串，支持数字、字母、字符的组合，不支持中文。
>- 如果上传的源文件调用了该方法，那么在使用 GET（下载）、HEAD（查询）时对源对象操作的时候也要调用该方法。

[//]: # (.cssg-snippet-put-object-sse-c)
```py
response = client.put_object(
    Bucket='examplebucket-1250000000',
    Body=b'bytes'|file,
    Key='exampleobject',
    SSECustomerAlgorithm='AES256',
    SSECustomerKey='string', // 客户端密钥的 base64 编码字符串
    SSECustomerKeyMD5='string' // 客户端密钥的 md5 字符串
)
```

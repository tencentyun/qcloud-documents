
如果需要对上传的对象进行加密，我们支持以下加密方式。

#### 使用 COS 托管加密密钥的服务端加密（SSE-COS）保护数据

由腾讯云 COS 托管主密钥和管理数据。COS 会帮助您在数据写入数据中心时自动加密，并在您取用该数据时自动解密。目前支持使用 COS 主密钥对数据进行 AES-256 加密。

JavaScript SDK 通过调用 API 时传入 `ServerSideEncryption` 参数完成。

[//]: # (.cssg-snippet-put-object-sse)
```js
cos.putObject({
    Bucket: 'examplebucket-1250000000', /* 必须 */
    Region: 'ap-beijing',    /* 必须 */
    Key: 'picture.jpg',              /* 必须 */
    Body: 'hello!',
    ServerSideEncryption: 'AES-256',
}, function(err, data) {
    console.log(err || data);
});
```

#### 使用客户提供的加密密钥的服务端加密 （SSE-C）保护数据

加密密钥由用户自己提供，用户在上传对象时，COS 将使用用户提供的加密密钥对用户的数据进行 AES-256 加密。JavaScript SDK 通过调用 API 时传入 `SSECustomerKey` 参数完成。

> !
>- 该加密所运行的服务需要使用 HTTPS 请求。
>- customerKey：用户提供的密钥，传入一个32字节的字符串的base64编码，字符串支持数字、字母、字符的组合，不支持中文。
>- 如果上传源文件（putObject）使用了该参数，那么在使用 headObject（查询）、getObject（下载）、multipartInit（初始化分块上传）、multipartUpload（上传分块）、putObjectCopy（复制）时对源对象操作的时候也要调用该方法。

[//]: # (.cssg-snippet-put-object-sse-c)
```js
cos.putObject({
    Bucket: 'examplebucket-1250000000', /* 必须 */
    Region: 'ap-beijing',    /* 必须 */
    Key: 'picture.jpg',              /* 必须 */
    Body: 'hello!',
    SSECustomerKey: 'MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY',
}, function(err, data) {
    console.log(err || data);
});
```

## 描述

此篇文档将为您介绍在使用 API 时候会使用到的公共请求头部（Request Header），下文提到的头部会在之后的具体 API 文档中不再赘述。

##  请求头部列表

| Header名称           | 描述                                       | 类型     | 必选   |
| ------------------ | ---------------------------------------- | ------ | ---- |
| Authorization      | 携带鉴权信息， 用以验证请求合法性的签名信息。针对公有读的文件，无需携带此头部。 | String | 否    |
| Content-Length     | RFC 2616 中定义的 HTTP 请求内容长度（字节），常用于 PUT 类型的 API 的操作。 | String | 否    |
| Content-Type       | RFC 2616 中定义的 HTTP 请求内容类型（MIME），例如 text/plain。同时可以设置 charset 属性，避免客户端下载文件后使用默认编码方式打开文件导致乱码。 | String | 否   |
| Content-MD5        | RFC 1864 中定义的经过 Base64 编码的 128-bit 内容 MD5 校验值。此头部用来校验文件内容是否发生变化。 | String | 否    |
| Date               | RFC 1123 中定义的 GMT 时间，例如 Wed, 30 Mar. 2016 23:00:00 GMT。 | String | 否    |
| Expect             | 当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容。该选项可以被用于验证头部是否有效，而无需发送数据内容。<br />有效值：100-continue。 | String | 否    |
| Host               | 请求的主机，形式为 &lt;BucketName&gt;-&lt;APPID&gt;.cos.&lt;Region&gt;.myqcloud.com | String | 是    |
|Cache-Control|	RFC 2616 中定义的缓存策略，将作为 Object 元数据保存| String|否
|x-cos-security-token |使用临时安全凭证时需要传入的安全令牌字段，请查看 [临时安全凭证的相关说明](https://cloud.tencent.com/document/product/436/31315#.E4.B8.B4.E6.97.B6.E5.AE.89.E5.85.A8.E5.87.AD.E8.AF.81)。|  String  | 否

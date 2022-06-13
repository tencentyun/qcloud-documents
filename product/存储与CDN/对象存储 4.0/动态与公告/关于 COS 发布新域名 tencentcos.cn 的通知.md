2022年7月25日，对象存储（Cloud Object Storage，COS）将正式发布新域名 tencentcos.cn，旧域名 myqcloud.com 支持继续使用，但不支持 COS 后续的新增特性与功能。新域名具有更高的安全性和稳定性，建议用户优先使用新域名 tencentcos.cn。


>! 旧域名 myqcloud.com 支持继续使用，旧域名的原有特性仍然不受影响，但不再支持 COS 后续的新增特性。
>

新域名 tencentcos.cn 主要有以下几点变化：

**1. 统一使用 tencentcos.cn 后缀**

以默认存储桶域名为例，新域名形如：&lt;BucketName-APPID&gt;.cos.&lt;Region&gt;.tencentcos.cn。

**2. 提供内网域名**

新域名提供独立的内网域名，仅支持在内网环境访问，外网环境会访问失败，可用于避免外网流量产生。

以默认存储桶域名为例，新域名的内网域名形如：&lt;BucketName-APPID&gt;.cos-internal.&lt;Region&gt;.tencentcos.cn。

**3. 支持 tencentcos.cn 的域名**
除内网域名外，新域名均支持内外网智能解析，会根据访问环境自动切换内外网。

| 域名   |  示例              |
| -------------- | ---------------- |
| 默认存储桶域名 | &lt;BucketName-APPID&gt;.cos.&lt;Region&gt;.tencentcos.cn
| 默认存储桶域名(内网) | &lt;BucketName-APPID&gt;.cos-internal.&lt;Region&gt;.tencentcos.cn  |
| 全球加速域名 | &lt;BucketName-APPID&gt;.cos.accelerate.tencentcos.cn  |
| 全球加速域名(内网) | &lt;BucketName-APPID&gt;.cos-internal.accelerate.tencentcos.cn  |
| 静态网站域名 | &lt;BucketName-APPID&gt;.cos-website.&lt;Region&gt;.tencentcos.cn  |
| 静态网站域名(内网) | &lt;BucketName-APPID&gt;.cos-website-internal.&lt;Region&gt;.tencentcos.cn  |   

2022年3月15日，对象存储（Cloud Object Storage，COS）将正式发布新域名 tencentcos.cn，旧域名 myqcloud.com 可以继续使用，但不会支持后续 COS 的新增特性与功能。新域名具有更高的安全性和稳定性，建议用户优先使用新域名 tencentcos.cn。


>! 旧域名 myqcloud.com 支持继续使用，旧域名的原有特性（例如内外网智能解析）仍然不受影响，但不再支持后续新增特性。
>

新域名 tencentcos.cn 主要有以下几点变化：

**1. 统一使用 tencentcos.cn 后缀**

以默认存储桶域名为例，

- 旧域名形如：&lt;BucketName-APPID&gt;.cos.&lt;Region&gt;.myqcloud.com
- 新域名形如：&lt;BucketName-APPID&gt;.cos.&lt;Region&gt;.tencentcos.cn

**2. 区分内外网域名**

旧域名不区分内、外网域名，以默认存储桶域名为例，域名形式统一使用：&lt;BucketName-APPID&gt;.cos.&lt;Region&gt;.myqcloud.com。

新域名区分内、外网域名，以默认存储桶域名为例，域名形式如下：

- 新域名外网域名：&lt;BucketName-APPID&gt;.cos.&lt;Region&gt;.tencentcos.cn
- 新域名内网域名：&lt;BucketName-APPID&gt;.cos-internal.&lt;Region&gt;.tencentcos.cn


新旧域名的对比情况如下：

| 域名类型   | 旧域名                    | 新域名                |
| -------------- | ---------------------------------- | ---------------- |
| 默认存储桶域名 | &lt;BucketName-APPID&gt;.cos.&lt;Region&gt;.myqcloud.com，不区分内、外网域名。 | <ul  style="margin: 0;"><li>外网域名：&lt;BucketName-APPID&gt;.cos.&lt;Region&gt;.tencentcos.cn </li><li>内网域名：&lt;BucketName-APPID&gt;.cos-internal.&lt;Region&gt;.tencentcos.cn  </li></ul>     |   
| 全球加速域名 | &lt;BucketName-APPID&gt;.cos.accelerate.myqcloud.com，不区分内、外网域名。   |  <ul  style="margin: 0;"><li>外网域名：&lt;BucketName-APPID&gt;.cos.accelerate.tencentcos.cn </li><li>内网域名：&lt;BucketName-APPID&gt;.cos-internal.accelerate.tencentcos.cn </li></ul>              |   
| 静态网站域名 |&lt;BucketName-APPID&gt;.cos-website.&lt;Region&gt;.myqcloud.com，不区分内、外网域名。 | <ul  style="margin: 0;"><li>外网域名：&lt;BucketName-APPID&gt;.cos-website.&lt;Region&gt;.tencentcos.cn </li><li>内网域名：&lt;BucketName-APPID&gt;.cos-website-internal.&lt;Region&gt;.tencentcos.cn</li></ul> |       



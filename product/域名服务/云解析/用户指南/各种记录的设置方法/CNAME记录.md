### 什么情况下会用到CNAME记录？

如果需要将域名指向另一个域名，再由另一个域名提供ip地址，就需要添加CNAME记录；
最常用到CNAME的场景包括做CDN、做企业邮局。

### CNAME记录的添加方式

![](https://mccdn.qcloud.com/static/img/c9a251b3b52d06f8a44d076e12f75b5b/CName-1.png)

![](https://mccdn.qcloud.com/static/img/e38225a498ababb41f8215119726a27a/CName-2.png)

1. 主机记录处填子域名（比如需要添加 www.123.com 的解析，只需要在主机记录处填写www即可；如果只是想添加123.com的解析，主机记录直接留空，系统会自动填一个“@”到输入框内，@的CNAME会影响到MX记录的正常解析，添加时慎重考虑）。

2. 记录类型为CNAME。

3. 线路类型（默认为必填项，否则会导致部分用户无法解析；在上图中，默认的作用为：除了联通用户之外的所有用户，都会指向1.com）。

4. 记录值为CNAME指向的域名，只可以填写域名。
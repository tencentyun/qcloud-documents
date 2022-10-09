WordPress 是一种使用 PHP 语言开发的平台，用户可以在支持 PHP 和 MySQL 数据库的服务器上架设 WordPress。可以搭建独立博客，也可以作为内容管理系统（CMS），或者是用来构建门户网站。

虽然 WordPress 已经占据全球 Web 的45%以上的份额，但拥有丰富强大功能的同时也造成了程序本身过于臃肿的问题，在服务器带宽不足、配置低的情况下，图片、视频等大型媒体文件会严重拖慢网站访问速度。此时我们可以使用腾讯云对象存储来存放网站中的图片、视频或者其他静态文件，减轻服务器压力，提高网站访问速度，示意图如下：
![](https://qcloudimg.tencent-cloud.cn/raw/67c6850cad068b091609766ee70cdb14.png)
## 创建存储桶
首先登陆腾讯云对象存储控制台新建一个存储桶，存储桶就是存放文件的容器。
![](https://qcloudimg.tencent-cloud.cn/raw/cb465036f339785391888bae4d72f37f.jpeg)
- 存储痛地域根据实际情况选择，越靠近用户体验越好。
- 访问权限可以选择**私有读写**通过鉴权访问文件，或者**公有读私有写**配合黑白名单、refer 头控制访问。
其他配置可以暂时选择默认选项。

创建好存储桶后进入WordPress网站后台，安装腾讯云对象存储（COS）插件。该插件基于腾讯云对象存储 COS，将网站静态资源与后台应用分离，用户访问网页的请求由应用后台响应，并直接返回动态html内容，减轻服务器带宽和存储压力；静态资源存放在 COS 上，和云服务器内网高速互通，不仅访问速度快，相较磁盘存储成本更低。并且可配合内容分发网络 [CDN](https://cloud.tencent.com/product/cdn?from=10680) 进一步提升用户访问静态资源的速度，让你的网站速度更快一步。
![](https://qcloudimg.tencent-cloud.cn/raw/27bbcdb2f8ddaf8f3b9943dc64175813.jpeg)
安装好后启用插件，在腾讯云设置（全局）中填入密钥。

## 获取 API 密钥管理
在腾讯云访问管理控制台获取 API 密钥管理。
![](https://qcloudimg.tencent-cloud.cn/raw/0b327756b85c6aee1cbefe44a583b5b7.png)
依次填入地域、空间名称、访问域名，建议开启自动重命名。
![](https://qcloudimg.tencent-cloud.cn/raw/ece4de06a25c3b8ca4933216eaa43009.jpeg)
![](https://qcloudimg.tencent-cloud.cn/raw/c83918fe0f38a4e31d71f67057ed43e7.jpeg)
![](https://qcloudimg.tencent-cloud.cn/raw/0bcf04101f32790125e7a6cfbe4eb77b.jpeg)
单击**保存配置**，提示保存成功即可。
![](https://qcloudimg.tencent-cloud.cn/raw/8c313f895ba06b6d9f26497d15eedae6.png)
然后单击附件同步，等待插件将文件同步到 COS 桶中。
![](https://qcloudimg.tencent-cloud.cn/raw/76f9bd3a4af4898c4c852dc9a61b8c27.png)
同步完成后点击**一键替换**，将网站内容中所有静态文件地址替换为腾讯云 COS 文件地址。

访问网站[ 48zhai.cn](https://48zhai.cn/) 发现缺失了部分图片。
![](https://qcloudimg.tencent-cloud.cn/raw/c5312338585b2edf0bb853fa2556cf69.png)
查看控制台发现部分图片404了，通过状态码结合 xml 返回的错误信息可以知道存储桶中没有该文件，可能是同步未完成。
![](https://qcloudimg.tencent-cloud.cn/raw/a7f47727e2cf0deb7938d9a8622e4de9.png)
等待同步完成后再次点击替换，完成后通过控制台看到文件地址都已经改为 COS 默认域名。
![](https://qcloudimg.tencent-cloud.cn/raw/ac3e5a402af4e7ccc617f004d0bef7f9.png)
如果你觉得这个域名太长不美观，你可以为每个 COS 存储桶添加一个或多个自定义域名，你添加的自定义域名需要解析到腾讯云对象存储提供的 CNAME上，同时如果需要对资源开启 HTTPS 访问还需要上传相关域名的证书文件。
![](https://qcloudimg.tencent-cloud.cn/raw/4694358e382050810038bcb8686e882e.png)
如果你认为访问存储桶内的资源速度不理想或者延迟过大，你也可以对存储桶开启 CDN 加速，并且添加加速域名，同样的需要添加解析和上传证书文件，并等待 CDN 生效。
![](https://qcloudimg.tencent-cloud.cn/raw/b12efebddb1c253601f358caf9293074.png)
使用 COS 的时候你可以在安全管理下配置防盗链设置白名单，防止 COS 流量被盗刷。
![](https://qcloudimg.tencent-cloud.cn/raw/219774d398ab0b8036c29c7941f483fc.png)
验证规则是否生效，图片在网站中可以正常显示，直接访问触发了防盗链规则。
![](https://qcloudimg.tencent-cloud.cn/raw/ba26de1d14e906459eb163379e6eeebc.png)
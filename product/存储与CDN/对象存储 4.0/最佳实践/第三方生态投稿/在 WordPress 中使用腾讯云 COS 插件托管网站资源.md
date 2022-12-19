WordPress 是一种使用 PHP 语言开发的平台，用户可以在支持 PHP 和 MySQL 数据库的服务器上架设 WordPress。可以搭建独立博客，也可以作为内容管理系统（CMS），或者是用来构建门户网站。

虽然 WordPress 已经占据全球 Web 的45%以上的份额，但拥有丰富强大功能的同时也造成了程序本身过于臃肿的问题。在服务器带宽不足、配置低的情况下，图片、视频等大型媒体文件会严重拖慢网站访问速度。

此时我们可以使用腾讯云对象存储来存放网站中的图片、视频或者其他静态文件，从而减轻服务器压力，提高网站访问速度，示意图如下：

![](https://qcloudimg.tencent-cloud.cn/raw/67c6850cad068b091609766ee70cdb14.png)
## 操作步骤
### 创建存储桶
1. 首先登录 [腾讯云-对象存储控制台](https://console.cloud.tencent.com/cos/bucket) 新建一个存储桶，存储桶就是存放文件的容器。
![](https://qcloudimg.tencent-cloud.cn/raw/133b5a93ec49951076a7779094ae399c.png)

 - 存储桶**所属地域**根据实际情况选择，越靠近用户体验越好。
 - **访问权限**可以选择**私有读写**通过鉴权访问文件，或者**公有读私有写**配合黑白名单、refer 头控制访问。
 - 其他配置可以暂时选择默认选项。

2. 创建好存储桶后，进入 WordPress 网站后台，安装**腾讯云对象存储（COS）**插件。该插件基于腾讯云对象存储 COS，将网站静态资源与后台应用分离，用户访问网页的请求由应用后台响应，并直接返回动态 HTML 内容，减轻服务器带宽和存储压力。
静态资源存放在 COS 上，和云服务器内网高速互通，不仅访问速度快，相较磁盘存储成本更低。并且可配合内容分发网络 [CDN](https://cloud.tencent.com/product/cdn?from=10680) 进一步提升用户访问静态资源的速度，让您的网站速度更快一步。
![](https://qcloudimg.tencent-cloud.cn/raw/27bbcdb2f8ddaf8f3b9943dc64175813.jpeg)
安装好后启用插件，在**腾讯云设置（全局）**中填入密钥。

### 获取 API 密钥管理
1. 在腾讯云访问管理控制台获取 [API 密钥管理](https://console.cloud.tencent.com/cam/capi)。
![](https://qcloudimg.tencent-cloud.cn/raw/0b327756b85c6aee1cbefe44a583b5b7.png)

<span id="Request"></span>
2. 依次填入**所属地域**、**空间名称**、**访问域名**，建议开启**自动重命名**。
![](https://qcloudimg.tencent-cloud.cn/raw/b69ca4f0e6a082865bf2f9f4d5cf23e8.jpeg)
![](https://qcloudimg.tencent-cloud.cn/raw/c83918fe0f38a4e31d71f67057ed43e7.jpeg)
![](https://qcloudimg.tencent-cloud.cn/raw/25ee2c96c7d21de653914d4a381044bc.jpeg)

<span id="Request"></span>
3. 单击**保存配置**，提示“保存成功”即可。
![](https://qcloudimg.tencent-cloud.cn/raw/8c313f895ba06b6d9f26497d15eedae6.png)

<span id="Request"></span>
4. 单击**附件同步**，等待插件将文件同步到 COS 桶中。
![](https://qcloudimg.tencent-cloud.cn/raw/2f31a63eaeaf170a558f32f92cecec68.png)

<span id="Request"></span>
5. 同步完成后单击**一键替换**，将网站内容中所有静态文件地址替换为腾讯云 COS 文件地址。

<span id="Request"></span>
6. 访问网站[ 48zhai.cn](https://48zhai.cn/) 发现缺失了部分图片。
![](https://qcloudimg.tencent-cloud.cn/raw/036f832151007f61973d9ef262fd799e.png)

<span id="Request"></span>
7. 查看控制台发现部分图片404了，通过状态码结合 xml 返回的错误信息，可以知道存储桶中没有该文件，可能是同步未完成。
![](https://qcloudimg.tencent-cloud.cn/raw/a7f47727e2cf0deb7938d9a8622e4de9.png)

<span id="Request"></span>
8. 等待同步完成后，再次点击**替换**，完成后，通过控制台可以看到文件地址都已经改为 COS 默认域名。
![](https://qcloudimg.tencent-cloud.cn/raw/140a634ecb5319d5b15676f3f1fee791.png)

<span id="Request"></span>
9. 如果您觉得这个域名太长不美观，您可以为每个 COS 存储桶添加一个或多个**自定义源站域名**，您添加的**自定义源站域名**需要解析到腾讯云对象存储提供的 CNAME 上。同时，如果需要对资源开启 HTTPS 访问，还需要上传相关域名的证书文件。
![](https://qcloudimg.tencent-cloud.cn/raw/4694358e382050810038bcb8686e882e.png)

<span id="Request"></span>
10. 如果您认为访问存储桶内的资源速度不理想或者延迟过大，您也可以对存储桶开启 CDN 加速，并且添加**自定义 CDN 加速域名**，同样的需要添加解析和上传证书文件，并等待 CDN 生效。
![](https://qcloudimg.tencent-cloud.cn/raw/b12efebddb1c253601f358caf9293074.png)

<span id="Request"></span>
11. 使用 COS 的时候，您可以在安全管理下配置**防盗链设置白名单**，防止 COS 流量被盗刷。
![](https://qcloudimg.tencent-cloud.cn/raw/219774d398ab0b8036c29c7941f483fc.png)

<span id="Request"></span>
12. 验证规则是否生效，图片在网站中可以正常显示，直接访问触发了防盗链规则。

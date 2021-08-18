本文详细描述了通过 COS 控制台实现 CDN 加速 COS 的整体操作流程和具体的操作方法。

## 前提条件
1. 完成腾讯云账号注册、实名认证。
2. 开启 CDN 服务，详情请参见 [CDN 快速入门](https://cloud.tencent.com/document/product/228/3149)。

## 操作指南
### 创建存储桶
创建存储桶的操作流程与方法，请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。

### 加速配置
1. 创建好存储桶后直接进入该存储桶的配置管理页面，或在存储桶列表单击需要配置的存储桶操作栏的【配置管理】，进入配置管理页面，选择【域名管理】。
2. 开启**默认 CDN 加速**
**默认 CDN 加速**是由系统默认生成的，经由 CDN 加速节点的域名，用户可选择开启或关闭。
(1) 在默认 CDN 加速模块下，单击【编辑】，手动开启当前状态，进入默认 CDN 加速的配置
![](https://main.qcloudimg.com/raw/1259f6760e8794f23e3ded2856db95f0.png)
(2) 默认 CDN 加速的配置：
![](https://main.qcloudimg.com/raw/74642378de3e3f16c7d5b85703242362.png)
**源站类型**：通常默认为**默认源站**，如果作为源站的存储桶开启了静态网站，并且希望为静态网站加速，则选择为**静态网站源站**。
**回源鉴权**：当存储桶为公有读时，则不需要开启回源鉴权。当存储桶为私有读时，需要添加 CDN 服务授权，并手动开启回源鉴权。更多信息可参见 [开启回源鉴权](https://cloud.tencent.com/document/product/436/36636#step1)。
**CDN 服务授权**：单击【添加 CDN 服务授权】，选择并同意CDN访问存储桶中的资源。
![](https://main.qcloudimg.com/raw/bafdbdb8756c90eb976e46536df27b57.png)
(3) 配置完成后，单击【保存】，即可开启 CDN 加速
![](https://main.qcloudimg.com/raw/b89e3895e239d79aa8b23fb18d53ba03.png)

>!对于私有读存储桶，同时开启回源鉴权和 CDN 服务授权时，将导致通过 CDN 访问源站时无需携带签名，CDN 缓存资源会进行公网分发，导致数据的安全性受到影响，建议开启 CDN 鉴权。
>
3. 开启**自定义 CDN 加速**
用户可以为存储桶绑定已备案的**自定义域名**，并开启 CDN 加速。
>?通过 COS 控制台添加自定义域名上限为10个。
>
(1) 在**自定义 CDN 加速**模块单击【添加域名】，添加已备案的自定义域名
![](https://main.qcloudimg.com/raw/307c52d34a0d024c438c6f7df8a3cff7.png)
(2) 添加域名的配置如下：
**域名**：输入待绑定的自定义域名（例如`www.example.com`）。请确保输入的域名已备案，并已在 DNS 服务商处设置好对应的 CNAME，详情请参见 [CNAME 配置](https://cloud.tencent.com/document/product/228/3121) 。
**回源鉴权**：对于私有读存储桶，请手动开启回源鉴权以保护源站。
配置完成后，单击【保存】，即可完成对域名的添加。
![](https://main.qcloudimg.com/raw/694970c66952b869725f21e7cf271f66.png)
>!对于私有读存储桶，同时开启回源鉴权和 CDN 服务授权时，将导致通过 CDN 访问源站时无需携带签名，CDN 缓存资源会进行公网分发，导致数据的安全性受到影响，建议开启 CDN 鉴权。
>
(3) 保存后，**CDN 鉴权**栏将出现 CDN 鉴权功能开关，可手动开启自定义域名 CDN 鉴权。
**CDN 鉴权：**开启时间戳鉴权配置，可防止恶意用户盗取内容，需在添加完域名后进行设置。

关于在 COS 控制台实现 CDN 加速 COS 的更多内容，请参见 [COS 域名管理概述](https://cloud.tencent.com/document/product/436/18424)。


## 建议配置
1. 配置完成后，前往 [CDN 控制台](https://console.cloud.tencent.com/cdn)为 COS 下的资源文件做好预热。提前将静态资源预热至 CDN 加速节点，降低源站压力，提高响应与下载速度。详情可见 [缓存预热](https://cloud.tencent.com/document/product/228/40273)。
2. 配置好跨域的头部参数。解决资源的跨域权限问题，详情可见 [HTTP 响应头配置](https://cloud.tencent.com/document/product/228/41737#.E5.A4.B4.E9.83.A8.E5.8F.82.E6.95.B0)。
3. 若客户源站的资源已修改，建议刷新缓存后再重新进行预热。详情可见 [缓存刷新](https://cloud.tencent.com/document/product/228/6299)。

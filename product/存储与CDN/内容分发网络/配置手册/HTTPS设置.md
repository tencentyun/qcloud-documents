> HTTPS 是指超文本传输安全协议（Hypertext Transfer Protocol Secure），是一种在 HTTP 协议基础上进行传输加密的安全协议，能够有效保障数据传输安全。配置 HTTPS 时，需要您提供域名对应的证书，将其部署在全网 CDN 节点，实现全网数据加密传输功能。
>
>  **对象存储** 或 **万象优图** 服务开启 CDN 加速后，默认的 ```.file.myqcloud.com``` 后缀域名，或```.image.myqcloud.com```后缀域名，可直接支持 HTTPS 请求，无需配置证书。
>
> 腾讯云 CDN 目前针对 HTTP2.0 协议支持已经全面公测，可直接使用。

## 配置指引
- 域名不是由，默认的 ```.file.myqcloud.com``` 或 ```.image.myqcloud.com``` 域名。
- 域名的接入方式为 **自有源** 或者 **COS源**、**FTP源**。

腾讯云 CDN 目前支持两种方式部署证书。
- 自有证书：将自有证书、私钥内容上传至 CDN 进行部署，全程加密传输，证书不落地，保障您的证书安全。
- 腾讯云托管证书：您可以通过 [SSL 证书管理](https://console.cloud.tencent.com/ssl)，将已有证书托管至腾讯云，以用于多个云产品，您也可以在该平台申请由亚洲诚信免费提供的第三方证书，将其直接部署至 CDN。

登录[CDN控制台](https://console.cloud.tencent.com/cdn)，单击左侧导航栏的 【域名管理】 进入 **域名管理** 页面。单击域名右侧【管理】按钮，进入管理页面：
![](https://main.qcloudimg.com/raw/667013013f17c055f0cb3cec4580c4ef.png)
单击 【高级配置】，找到 **HTTPS 配置** 模块。单击【前往配置】，跳转至 **证书管理** 页面配置证书。配置流程请参阅 [证书管理](https://cloud.tencent.com/document/product/228/6303)。
![](https://main.qcloudimg.com/raw/1efff7b5b6909863e0849ae6cf9f65a7.png)
证书 **配置成功** 后，会出现【强制跳转 HTTPS】开关。开启后，即使用户发起 HTTP 请求，也会强制跳转为 HTTPS 请求进行访问：
![](https://main.qcloudimg.com/raw/8ccfdda9898a09a95d702e9162ff95d6.png)

## HTTP2.0 配置
获得 HTTP2.0 内测资格的用户，在成功为域名配置了 HTTPS 证书后，可以开启 HTTP2.0。
![](https://main.qcloudimg.com/raw/19b5892f7cf04b93e37f63eef75a94d8.png)
了解更多 HTTP2.0 相关特性，请查阅 [HTTP2.0 的新特性](https://cloud.tencent.com/community/article/541321)。
## 功能介绍
HTTPS，是指超文本传输安全协议（Hypertext Transfer Protocol Secure），是一种在 HTTP 协议基础上进行传输加密的安全协议，能够有效保障数据传输安全。配置 HTTPS 时，需要您提供域名对应的证书，将其部署在全网 CDN 节点，实现全网数据加密传输功能。

<font color="red">HTTPS 配置目前已全面开放，欢迎使用。</font>

HTTP2.0火热内测中，[点击申请](https://www.qcloud.com/act/apply/cdn_http2)

## 配置说明

满足以下条件的域名才可配置 HTTPS：

- 域名管理页面，域名的状态为 **部署中** 或 **已启动**；
- 域名不是由 COS 同步而来的 .file.myqcloud.com 后缀域名；
- 域名的接入方式为 **自有源** 或者 **COS源**、**FTP源**；

登录[CDN控制台](https://console.qcloud.com/cdn)，进入 【域名管理】 页面，点击域名右侧 **管理** 按钮，进入管理页面：

![](https://mc.qcloudimg.com/static/img/70a01c53cfaa997013da2cb4b699bbf1/donmai_management.png)

在 【高级配置】中找到 **HTTPS配置** 模块

![](https://mc.qcloudimg.com/static/img/fa28d53a7eba792519986e88ea5bcef8/https.png)

## 证书类型

腾讯云 CDN 目前支持两种方式部署证书：

- 自有证书：将自有证书、私钥内容上传至 CDN 进行部署，全程加密传输，证书不落地，保障您的证书安全；
- 腾讯云托管证书：您可以通过 [SSL 证书管理](https://console.qcloud.com/ssl)，将已有证书托管至腾讯云，以用于多个云产品，您也可以在该平台申请由亚洲诚信提供的 **免费证书** ，将其直接部署至 CDN；
- 腾讯云证书：原有 .qcloudcdn.com 后缀域名为腾讯云所有，使用的为腾讯云证书，该证书已关闭添加入口。

## 证书管理

证书添加、变更、删除等操作请前往 [证书管理](https://console.qcloud.com/cdn/tools/certificate) 页面进行，文档说明请查看 [证书管理说明](https://www.qcloud.com/doc/product/228/6303)。


## 强制HTTPS

证书配置成功后，会出现 **强制跳转** 开关，开启后，即使用户发起 HTTP 请求，也会强制跳转为 HTTPS进行访问：

![](https://mc.qcloudimg.com/static/img/16abdcd52cbc8072881a2b40b05ccfee/https_set.png)

<font color="blue">仅当HTTPS证书配置成功后，才可开启强制跳转</font>

## HTTP2.0 

获得HTTP2.0内测资格的用户，在成功为域名配置了HTTPS证书后，可以开启HTTP2.0：

![](https://mc.qcloudimg.com/static/img/30c160c9102a38893f51e6e0060d158d/HTTP2.0.png)

更多技术细节，[点击查看](https://www.qcloud.com/community/article/541321)。

腾讯云对象存储 COS 使用 XML API，这是一种轻量级的、无连接状态的接口，调用此接口您可以直接通过 HTTP/HTTPS 发出请求和接受响应，实现与腾讯云对象存储后台的交互操作。

由于使用了不同的数据传输框架，对象存储 COS 提供了独立于云 API 的接口和独立的 SDK，您可直接前往 COS 的 [API 操作列表](https://cloud.tencent.com/document/product/436/10111) 了解详情，或前往 COS 的 [SDK 列表](https://cloud.tencent.com/document/product/436/6474) 下载您需要的 SDK。云 API 的指南和对应的 SDK 不包含对象存储 COS 的操作功能。

>!
>- 如您已开始使用腾讯云 COS API，即代表您已阅读并同意 [《腾讯云服务协议》](https://cloud.tencent.com/document/product/301/1967) 和 [《腾讯云对象存储服务等级协议》](https://cloud.tencent.com/document/product/436/6227)。
>- COS 的可用地域（Region）的详细信息请查阅 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) 文档。 
>- 在使用 API 或 SDK 发起请求前，建议您阅读 [创建请求概述](https://cloud.tencent.com/document/product/436/31315) 文档了解发起访问的域名、安全鉴权概念以及内外网访问检查等信息。
>- COS 存在 XML 和 JSON 两个不同版本的 API，两个版本的接口协议并不相同，但访问的数据互通。
>- 腾讯云推荐您使用 XML API，历史版本的 JSON API 将不再提供继2018年之后推出的新功能。

## 术语信息
文中会出现的一些主要概念和术语：
<style rel="stylesheet">
table th:nth-of-type(1) {
width: 150px;	
}
table th:nth-of-type(2) {
width:550px;	
}
</style>

|名称|	描述|
|---|---|
| APPID	|开发者访问 COS 服务时拥有的用户维度唯一资源标识，用以标识资源|
| SecretId | 开发者拥有的项目身份识别 ID，用以身份认证|
| SecretKey	| 开发者拥有的项目身份密钥|
| Bucket|	 COS 中用于存储数据的容器|
| Object|	 COS 中存储的具体文件，是存储的基本实体|
| Region|	域名中的地域信息。枚举值参见 [可用地域](https://cloud.tencent.com/document/product/436/6224) 文档，如：ap-beijing, ap-hongkong, eu-frankfurt 等 |
| ACL |	访问控制列表（Access Control List），是指特定 Bucket 或 Object 的访问控制信息列表|
| CORS | 跨域资源共享（Cross-Origin Resource Sharing），<br>指发起请求的资源所在域不同于该请求所指向资源所在的域的 HTTP 请求|
| Multipart Uploads |分块上传，腾讯云 COS 服务为上传文件提供的一种分块上传模式|


## 快速入门

要使用腾讯云对象存储 API，需要先执行以下步骤：

1. 在腾讯云 [对象存储控制台](https://console.cloud.tencent.com/cos5) 开通腾讯云对象存储（COS）服务。
2. 在腾讯云 [对象存储控制台](https://console.cloud.tencent.com/cos5) 创建一个 Bucket。
3. 在访问管理控制台中的 [云 API 密钥](https://console.cloud.tencent.com/capi) 页面里获取 APPID、SecretId、SecretKey 内容。
4. 编写一个请求签名算法程序（或使用任何一种服务端 SDK），详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。
5. 计算签名，调用 API 执行操作。

## 历史版本 API
请查看 [历史版本 API 简介](https://cloud.tencent.com/document/product/436/6052)。

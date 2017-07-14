腾讯云对象存储服务的 XML API 是一种轻量级的、无连接状态的接口。调用此套接口可以直接通过 http/https 发出请求和接受响应，从而实现与腾讯云对象存储（COS）后台进行交互的操作。此套 API 的请求和响应内容都为 XML 格式。
>**注意：**
>为了能更高效的使用腾讯云对象存储服务的 XML API，请在查阅其他的 API 文档之前，先详细阅读 [签名请求](https://www.qcloud.com/document/product/436/7778?!preview=true&lang=zh) 。

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
| AppID	|开发者访问 COS 服务时拥有的用户维度唯一资源标识，用以标识资源|
| SecretID | 开发者拥有的项目身份识别 ID，用以身份认证|
| SecretKey	| 开发者拥有的项目身份密钥|
| Bucket|	 COS 中用于存储数据的容器|
| Object|	 COS 中存储的具体文件，是存储的基本实体|
| Region|	域名中的地域信息。详细信息请参见 [可用地域](https://www.qcloud.com/document/product/436/6224) 文档 |
| ACL |	访问控制列表（Access Control List），是指特定 Bucket 或 Object 的访问控制信息列表|
| CORS | 跨域资源共享（Cross-Origin Resource Sharing），<br>指发起请求的资源所在域不同于该请求所指向资源所在的域的 HTTP 请求|
| Multipart Uploads |分块上传，腾讯云 COS 服务为上传文件提供的一种分块上传模式|
## 快速入门

要使用腾讯云对象存储 API，需要先执行以下步骤：

1. 购买腾讯云对象存储（COS）服务
2. 在腾讯云 [对象存储控制台](https://console.cloud.tencent.com/cos4/index) 里创建一个 Bucket
2. 在控制台 [个人 API 密钥](https://console.cloud.tencent.com/capi) 页面里获取 AppID、SecretID、SecretKey 内容
2. 编写一个请求签名算法程序（或使用任何一种服务端 SDK）
3. 计算签名，调用 API 执行操作

## 其他版本API

### JSON API

[JSON API](https://www.qcloud.com/document/product/436/6052) 是腾讯云 COS 服务在推出 XML API 前为用户提供接入使用 COS 的 API 接口，上传域名为 [Region].file.myqcloud.com。JSON API 接口与标准 XML 的 API 底层架构相同，数据互通，可以交叉使用，但是接口不兼容，域名不一致。
腾讯云 COS 的 XML API 服务推出后，推荐您使用 XML API 接口， JSON API 接口日后将保持维护状态，可以正常使用但是不发展新特性。

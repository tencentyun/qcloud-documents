在使用 COS 之前，建议先阅读 [COS 基本概念](https://cloud.tencent.com/document/product/436/6225)，了解使用 COS 需要的一些基本概念：存储桶、对象、地域以及访问域名的定义等。
COS 主要提供以下功能：
<style>
table th:first-of-type {
    width: 300px;
}
</style>

| 功能 | 描述 |  
|---------|---------|
| [创建存储桶](https://cloud.tencent.com/document/product/436/6245) | 在上传对象到 COS 之前，需要先创建存储桶。 | 
|[删除存储桶](https://cloud.tencent.com/document/product/436/6245)|如删除存储桶，需先删除存储桶中所有对象和目录。|
|[设置存储桶访问权限](https://cloud.tencent.com/document/product/436/6247)| COS 提供权限控制 ACL（Access Control List），可在创建存储桶的时候设置相应的 ACL 权限控制，也可在创建之后修改访问权限。|
|[防盗链设置](https://cloud.tencent.com/document/product/436/6250)|COS 是按使用量收费的服务，为了减少您存储在 COS 的数据被其他人盗链而产生额外费用，COS 支持通过防盗链设置来进行安全防护。|
|[回源设置](https://cloud.tencent.com/document/product/436/6248)|设置回源地址对获取数据的请求以多种方式进行回源读取，满足数据热迁移、特定请求的重定向等需求。|
|[托管静态网站](https://cloud.tencent.com/document/product/436/9512)|将存储桶配置成静态网站托管模式，并通过存储桶域名访问该静态网站。|
|[设置跨域访问](https://cloud.tencent.com/document/product/436/6251)| COS  提供 HTML5 标准中的跨域访问设置，帮助实现跨域访问。针对跨域访问，COS 支持响应 OPTIONS 请求，并根据开发者设定的规则向浏览器返回具体设置的规则。|
|[域名管理](https://cloud.tencent.com/document/product/436/6252)|通过域名管理，可将自定义域名绑定到 COS 访问域名上，实现自定义域名访问存储桶下的对象，也可同时一键配置腾讯云 CDN 实现加速功能。|
|[上传对象](https://cloud.tencent.com/document/product/436/6255)|可上传对象（如文本文件、图片、视频、应用等多格式文件）到存储桶中。|
|[下载对象](https://cloud.tencent.com/document/product/436/6260)|可通过多种方式下载对象。|
|[搜索对象](https://cloud.tencent.com/document/product/436/6256)|可在存储桶或文件夹中搜索具有相同的名称前缀的对象。|
|[设置对象权限](https://cloud.tencent.com/document/product/436/6371)|对象访问权限提供了基于对象维度的访问权限控制，且该配置优先级高于存储桶权限。|
|[设置 HTTP 头部](https://cloud.tencent.com/document/product/436/6258)|设置单个对象的 HTTP 头部。|
|[删除对象](https://cloud.tencent.com/document/product/436/6261)|单个或批量删除对象。|
|[创建文件夹](https://cloud.tencent.com/document/product/436/6263)|文件夹便于用户管理存储于 COS 的数据。|
|[删除文件夹](https://cloud.tencent.com/document/product/436/6264)|删除单个文件夹。|
|[API 文档](https://cloud.tencent.com/document/product/436/7751)|提供 COS 支持的 API 操作和相关示例。|
|[SDK 文档](https://cloud.tencent.com/document/product/436/6474)|提供主流语言 SDK 的开发操作和相关示例。|

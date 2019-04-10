在使用 COS 之前，建议先阅读 [COS 词汇表](https://cloud.tencent.com/document/product/436/18507)，了解使用 COS 需要的一些基本概念：存储桶、对象、地域以及访问域名的定义等。
COS 主要提供以下功能：
<style>
table th:first-of-type {
    width: 300px;
}
</style>

| 功能 | 描述 |  
|---------|---------|
| [创建存储桶](https://cloud.tencent.com/document/product/436/13309) | 在上传对象到 COS 之前，需要先创建存储桶。 | 
|[删除存储桶](https://cloud.tencent.com/document/product/436/32433)|对已存在的空存储桶进行删除。如删除存储桶，需先删除存储桶中所有对象以及【未完成上传】中的文件碎片。|
|[查询存储桶](https://cloud.tencent.com/document/product/436/13313)|  查询已创建的存储桶。|
|[设置存储桶访问权限](https://cloud.tencent.com/document/product/436/13315)| COS 支持存储桶设置访问权限，提供访问策略语言（Policy）和访问控制列表（ACL）功能，详情请查阅 [访问控制基本概念](https://cloud.tencent.com/document/product/436/30749)。|
|[设置防盗链](https://cloud.tencent.com/document/product/436/13319)|COS 是按使用量收费的服务，为了减少您存储在 COS 的数据被其他人盗链而产生额外费用，COS 支持通过防盗链设置来进行安全防护。|
|[设置回源](https://cloud.tencent.com/document/product/436/13310)|设置回源地址对获取数据的请求以多种方式进行回源读取，满足数据热迁移、特定请求的重定向等需求。|
|[设置跨域访问](https://cloud.tencent.com/document/product/436/13318)| COS  提供 HTML5 标准中的跨域访问设置，帮助实现跨域访问。针对跨域访问，COS 支持响应 OPTIONS 请求，并根据开发者设定的规则向浏览器返回具体设置的规则。|
|[设置静态网站](https://cloud.tencent.com/document/product/436/14984)|将存储桶配置成静态网站托管模式，并通过存储桶域名访问该静态网站。|
| [设置生命周期](https://cloud.tencent.com/document/product/436/14605)|对象存储 COS 支持用户设定规则，对指定对象在某个时间（天数）后进行自动删除或转换存储类型。|
|[子账号访问存储桶列表](https://cloud.tencent.com/document/product/436/17061)| 通过主账号授权给子账号，实现使用子账号访问存储桶及其列表。|
|[添加存储桶策略](https://cloud.tencent.com/document/product/436/33369)|用户可为存储桶添加策略，以允许或禁止某个账号、某个来源 IP（或 IP 段）访问 COS 资源。|
|[删除碎片文件](https://cloud.tencent.com/document/product/436/17313)|用户可对未完成上传的碎片文件进行删除。|
|[设置 CDN 加速](https://cloud.tencent.com/document/product/436/18424)|通过域名管理，可将自定义域名绑定到 COS 访问域名上，实现自定义域名访问存储桶下的对象，也可同时一键配置腾讯云 CDN 实现加速功能。|
|[上传对象](https://cloud.tencent.com/document/product/436/13321)|可上传对象（如文本文件、图片、视频、应用等多格式文件）到存储桶中。|
|[下载对象](https://cloud.tencent.com/document/product/436/13322)|可通过多种方式下载对象。|
|[查看对象信息](https://cloud.tencent.com/document/product/436/13326) |  查看对象的属性信息（如对象大小、对象地址）以及对象相关的配置（如设置对象的访问权限、存储类型更改等）。|
|[搜索对象](https://cloud.tencent.com/document/product/436/13325)|可在存储桶或文件夹中搜索具有相同的名称前缀的对象。|
|  [修改存储类型](https://cloud.tencent.com/document/product/436/33492)  |  对已上传到 COS 的对象进行存储类型的修改。|
|[设置对象的访问权限](https://cloud.tencent.com/document/product/436/13327)|对象访问权限提供了基于对象维度的访问权限控制，且该配置优先级高于存储桶权限。|
|[设置对象加密](https://cloud.tencent.com/document/product/436/33366)|对存放在存储桶中的对象设置加密，以防止信息被泄露。|
|[自定义 Headers](https://cloud.tencent.com/document/product/436/13361)|设置单个对象的 HTTP 头部。|
|[删除对象](https://cloud.tencent.com/document/product/436/13323)|删除单个对象或批量删除多个对象。|
| [恢复归档对象](https://cloud.tencent.com/document/product/436/32430)  | 对已归档的对象进行恢复，以便能够继续被访问或进行其他操作。|
|[创建文件夹](https://cloud.tencent.com/document/product/436/13329)|创建文件夹可以对存储于 COS 中的数据进行管理和分类。|
|[删除文件夹](https://cloud.tencent.com/document/product/436/13330)|可以删除单个文件夹，以及删除文件夹里的所有文件。|
|[API 文档](https://cloud.tencent.com/document/product/436/7751)|提供 COS 支持的 API 操作和相关示例。|
|[SDK 文档](https://cloud.tencent.com/document/product/436/6474)|提供主流语言 SDK 的开发操作和相关示例。|

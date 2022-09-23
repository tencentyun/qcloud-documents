
## 功能简介
支持通过调整资源 URL 中的查询字符串、拼接 HTTP 请求头和配置忽略大小写，自定义调整资源 Cache Key（缓存资源的唯一标识），优化节点缓存，根据不同场景响应对应的资源，提升请求资源的加载速度。

自定义 Cache Key 目前支持通过三个配置项实现：
- 查询字符串，具体操作可参见 [查询字符串](https://cloud.tencent.com/document/product/1552/70751)。
- HTTP 请求头，指定的 HTTP 请求头将被包含在 Cache Key 中，拼接在 URL 后方。只需输入 HTTP 请求头名称，例如：Accept-Language;User-Agent，Cache Key 里会自动包含头部对应的值。
- 忽略大小写，具体操作可参见 [ 忽略大小写](https://cloud.tencent.com/document/product/1552/70750)。


## 操作步骤[](id:bz)
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**规则引擎**。
2. 在规则引擎页面，选择所需站点，单击![img](https://qcloudimg.tencent-cloud.cn/raw/fe4d4900f8ad69d506adc49bdb70fa32.png)或编辑存量规则，按需配置自定义 Cache Key 规则。





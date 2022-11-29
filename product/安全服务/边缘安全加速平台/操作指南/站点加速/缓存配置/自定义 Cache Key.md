## 功能简介
支持通过调整资源 URL 中的查询字符串和配置忽略大小写，拼接 HTTP 标头等，自定义调整资源 Cache Key，优化节点缓存，根据不同场景响应对应的资源，提升请求资源的加载速度。

#### 什么是 Cache Key？
Cache Key 是节点缓存资源的唯一标识。节点响应请求资源时，默认按照完整的请求 URL 作为 Cache Key（缓存标识）去匹配缓存资源，例如：请求 `https://www.example.com/images/example.jpg?key1=value1` 与 `https://www.example.com/images/example.jpg?key2=value2` 对应两个不同的节点 Cache Key ，因为其查询字符串不同。

## 适用场景
客户端请求的资源与 URL 查询字符串，URL 字符大小写，HTTP 头部或请求协议有关，需要自定义配置资源在节点的缓存标识，实现客户端根据不同的请求行为适配到相应的节点缓存。

## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**规则引擎**。
2. 在规则引擎页面，选择所需站点，可按需配置自定义 Cache Key 规则。如何使用规则引擎，请参见 [规则引擎](https://cloud.tencent.com/document/product/1552/70901)。
   配置项说明：
<table>
<thead>
<tr>
<th width="20%">配置项</th>
<th width="80%">说明</th>
</tr>
</thead>
<tbody><tr>
<td align="left">查询字符串</td>
<td align="left">调整 URL 中的查询字符串后生成 Cache Key，默认保留原请求的全部查询参数。具体说明可参见 <a href="https://cloud.tencent.com/document/product/1552/70751">查询字符串</a>。</td>
</tr>
<tr>
<td align="left">忽略大小写</td>
<td align="left">是否忽略 URL 中英文字母的大小写，即使 URL(s) 内容一致 。具体说明可参见 <a href="https://cloud.tencent.com/document/product/1552/70750">忽略大小写</a>。</td>
</tr>
<tr>
<td align="left">HTTP 请求头</td>
<td align="left">
资源会根据某些客户端 HTTP 请求头而异，指定 HTTP 请求头拼接在 URL 后方生成 Cache Key 。只需输入 HTTP 请求头名称。
<ul><li>自定义头部：例如 `X-Client-Header`。</li>
<li>预设头部：支持根据客户端 `User-Agent` 和 IP 信息聚合的客户端信息头部，满足根据不同设备或浏览器类型缓存的需求。</li><ul>
<li>客户端设备类型：`EO-Client-Device`。<br>取值：`Mobile`，`Desktop`，`SmartTV`，`Tablet` 或 `Others`。</li>
<li>客户端操作系统：`EO-Client-OS`。<br>取值：Android，`iOS`，`Windows`，`MacOS`，`Linux` 或 `Others`。</li>
<li>客户端浏览器类型：`EO-Client-Browser`。<br>取值：`Chrome`，`Safari`，`Firefox`，`IE` 或 `Others`。</li>
<li>客户端 IP 所在地理位置：`EO-Client-IPCountry`。<br>取值：两位字母国家/地区代码（ISO 3166-1 alpha-2 codes）。</li></td>
</tr>
<tr>
<td align="left">Cookie</td>
<td align="left">调整 Cookie 参数，将调整后的 Cookie 拼接在 URL 后方生成 Cache Key 。</td>
</tr>
<tr>
<td align="left">请求协议</td>
<td align="left">是否根据不同请求协议（HTTP/HTTPS）区分缓存，默认不区分。</td>
</tr>
</tbody></table>

## 配置示例

若域名 `www.example.com`  的自定义 Cache Key 配置如下：

![](https://qcloudimg.tencent-cloud.cn/raw/dfb83780eecd2657c0a80ec953fb7f5f.png)

Cache Key 由 URL+My-Client-Header+Cookie 组成：不区分请求协议（默认），忽略全部查询字符串，忽略 URL 大小写，拼接My-Client-Header和保留指定参数后的 Cookie。

则客户端请求 A：

URL：`https://www.example.com/path/demo.jpg?key1=value1&key2=value2`。

HTTP 请求头：含 `My-Client-Header:fruit`。

Cookie：name1=yummy;name2=tasty;name3=strawberry。

与客户端请求 B：

URL：`http://www.example.com/path/demo.JPG?key1=value1&key2=value2&key3=value3`。

HTTP 请求头：含 `My-Client-Header:fruit`。

Cookie：name1=yummy;name2=tasty;name3=blueberry。

与客户端请求 C：

URL：`http://www.example.com/path/demo.JPG?key1=value1&key2=value2&key3=value3&key4=value4`。

HTTP 请求头：含 `My-Client-Header:sea`。

Cookie：name1=yummy;name2=tasty;name3=fish。


A 和 B 请求将会命中同一份缓存资源，C 命中另一份缓存资源。

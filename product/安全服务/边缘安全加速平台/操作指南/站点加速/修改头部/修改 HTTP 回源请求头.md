
## 功能简介
支持自定义变更/增加/删除 HTTP 请求头（从节点向源站请求回源时的 HTTP 请求头）。
>?EdgeOne 默认支持携带 X-Forwarded-For 和 X-Forwarded-Proto 回源，您无需再配置。
>

## 操作指南
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**规则引擎**。
2. 在规则引擎页面，选择所需站点，可按需配置修改  HTTP 请求头规则。如何使用规则引擎，请参见 [规则引擎](https://cloud.tencent.com/document/product/1552/70901)。
配置项说明：
<table>
<thead>
<tr>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>设置</td>
<td>变更指定头部参数的取值为设置后的值，且头部唯一。<br>注意：若指定头部不存在，则会增加该头部。</td>
</tr>
<tr>
<td>增加</td>
<td>增加指定的头部。<br>注意：若头部已存在，则会覆盖原有头部且唯一。</td>
</tr>
<tr>
<td>删除</td>
<td>删除指定的头部</td>
</tr>
</tbody></table>
头部类型说明：
<table>
<thead>
<tr>
<th>头部类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>自定义</td>
<td>自定义头部。<ul><li>名称：1 - 100个字符，由数字0 - 9、字符a - z、A - Z，及特殊符 <code>-</code> 组成。</li><li>值：1 - 1000个字符，不支持中文。</td>
</tr>
<tr>
<td>预设头部</td>
<td>根据客户端 `User-Agent` 信息聚合的客户端信息头部：<ul><li>客户端设备类型：`EO-Client-Device`。<br>取值：`Mobile`，`Desktop`，`SmartTV`，`Tablet` 或 `Others`。</li>
<li>客户端操作系统：`EO-Client-OS`。<br>取值：`Android`，`iOS`，`Windows`，`MacOS`，`Linux` 或 `Others`。</li>
<li>客户端浏览器类型：`EO-Client-Browser`。<br>取值：`Chrome`，`Safari`，`Firefox`，`IE` 或 `Others`。</li>
</td>
</tr>
</tbody></table>


## 注意事项
- 一个修改 HTTP 请求头操作中，可添加多条不同类型操作，最多30条，执行顺序为从上至下。
- 部分标准头部不支持修改，清单如下：
<table>
<thead>
<tr>
<td>Accept</td>
<td>Accept-Charset</td>
<td>Accept-Encoding</td>
<td>Accept-Language</td>
</tr>
</thead>
<tbody><tr>
<td>Accept-Ranges</td>
<td>Age</td>
<td>Authorization</td>
<td>Cache-Control</td>
</tr>
<tr>
<td>chunked</td>
<td>close</td>
<td>Connection</td>
<td>Content-Encoding</td>
</tr>
<tr>
<td>Content-Length</td>
<td>Content-Range</td>
<td>Content-Type</td>
<td>Cookie</td>
</tr>
<tr>
<td>Date</td>
<td>Etag</td>
<td>Expect</td>
<td>Expires</td>
</tr>
<tr>
<td>From-Tencent-Lego-Cluster</td>
<td>From-Tencent-Lego-Cluster-Client-Info</td>
<td>From-Tencent-Lego-Cluster-Edge-Server-Info</td>
<td>From-Tencent-Lego-Dsa</td>
</tr>
<tr>
<td>From-Tencent-Lego-Dsa-Client-Info</td>
<td>From-Tencent-Lego-Dsa-Edge-Server-Info</td>
<td>From-Tencent-Lego-Overload</td>
<td>Host</td>
</tr>
<tr>
<td>identity</td>
<td>If-Match</td>
<td>If-Modified-Since</td>
<td>If-None-Match</td>
</tr>
<tr>
<td>If-Range</td>
<td>keep-alive</td>
<td>Last-Modified</td>
<td>Location</td>
</tr>
<tr>
<td>multirange</td>
<td>normal</td>
<td>Pragma</td>
<td>Proxy-Authorization</td>
</tr>
<tr>
<td>Proxy-Connection</td>
<td>Range</td>
<td>Referer</td>
<td>Server</td>
</tr>
<tr>
<td>Server-Timing</td>
<td>Set-Cookie</td>
<td>Transfer-Encoding</td>
<td>upgrade</td>
</tr>
<tr>
<td>Upgrade</td>
<td>Upgrade-Insecure-Requests</td>
<td>User-Agent</td>
<td>Via</td>
</tr>
<tr>
<td>X-Cache-Lookup</td>
<td>X-Forwarded-For</td>
<td>X-Last-Update-Info</td>
<td>x-redirect-to-self</td>
</tr>
<tr>
<td>X-Via</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
</tbody></table>

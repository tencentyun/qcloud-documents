
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
<td align="left">Host</td>
<td align="left">Content-Length</td>
<td align="left">If-Modified-Since</td>
<td align="left">Etag</td>
</tr>
</thead>
<tbody><tr>
<td align="left">Accept-Encoding</td>
<td align="left">Last-Modified</td>
<td align="left">Content-Range</td>
<td align="left">Content-Type</td>
</tr>
<tr>
<td align="left">X-Cache-Lookup</td>
<td align="left">X-Last-Update-Info</td>
<td align="left">Transfer-Encoding</td>
<td align="left">Content-Encoding</td>
</tr>
<tr>
<td align="left">Connection</td>
<td align="left">Range</td>
<td align="left">Server</td>
<td align="left">Date</td>
</tr>
<tr>
<td align="left">Location</td>
<td align="left">Expect</td>
<td align="left">Cache-Control</td>
<td align="left">Expires</td>
</tr>
<tr>
<td align="left">Referer</td>
<td align="left">User-Agent</td>
<td align="left">Cookie</td>
<td align="left">X-Forwarded-For</td>
</tr>
<tr>
<td align="left">Accept-Language</td>
<td align="left">Accept-Charset</td>
<td align="left">Accept-Ranges</td>
<td align="left">Set-Cookie</td>
</tr>
<tr>
<td align="left">Via</td>
<td align="left">X-Via</td>
<td align="left">Pragma</td>
<td align="left">Upgrade</td>
</tr>
<tr>
<td align="left">If-None-Match</td>
<td align="left">If-Match</td>
<td align="left">If-Range</td>
<td align="left">From-Tencent-Lego-Cluster</td>
</tr>
<tr>
<td align="left">From-Tencent-Lego-Cluster-Client-Info</td>
<td align="left">From-Tencent-Lego-Cluster-Edge-Server-Info</td>
<td align="left">From-Tencent-Lego-Dsa</td>
<td align="left">From-Tencent-Lego-Dsa-Client-Info</td>
</tr>
<tr>
<td align="left">From-Tencent-Lego-Dsa-Edge-Server-Info</td>
<td align="left">Accept</td>
<td align="left">Upgrade-Insecure-Requests</td>
<td align="left">Server-Timing</td>
</tr>
<tr>
<td align="left">Age</td>
<td align="left">Proxy-Connection</td>
<td align="left">Authorization</td>
<td align="left">Proxy-Authorization</td>
</tr>
<tr>
<td align="left">normal</td>
<td align="left">multirange</td>
<td align="left">chunked</td>
<td align="left">identity</td>
</tr>
<tr>
<td align="left">keep-alive</td>
<td align="left">close</td>
<td align="left">upgrade</td>
<td align="left">x-redirect-to-self</td>
</tr>
<tr>
<td align="left">From-Tencent-Lego-Overload</td>
<td align="left">-</td>
<td align="left">-</td>
<td align="left">-</td>
</tr>
</tbody></table>

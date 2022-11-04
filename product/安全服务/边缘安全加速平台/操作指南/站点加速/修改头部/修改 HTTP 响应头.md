## 功能简介
支持自定义变更/增加/删除 HTTP 响应头（从节点响应客户端用户时的 HTTP 响应头），不会影响节点缓存。


## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone) ，在左侧菜单栏中，单击**规则引擎**。
2. 在规则引擎页面，选择所需站点，可按需配置修改 HTTP 响应头规则。如何使用规则引擎，请参见 [规则引擎](https://cloud.tencent.com/document/product/1552/70901)。
配置项说明
<table>
<thead>
<tr>
<th>类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>变更</td>
<td>变更指定头部参数的取值为设置后的值<br>注意：<ul><li>若指定头部不存在，则会增加该头部</li><li>若头部已存在（即使有多个重复的头部），则会覆盖原有头部且唯一（合并多个重复的头部为1个头部）</td>
</tr>
<tr>
<td>增加</td>
<td>增加指定的头部<br>注意：<br>若头部已存在（即使有多个重复的头部），则会覆盖原有头部且唯一（合并多个重复的头部为1个头部）</td>
</tr>
<tr>
<td>删除</td>
<td>删除指定的头部</td>
</tr>
</tbody></table>

## 注意事项
- 自定义头部参数格式要求如下：
  - 参数名：1 - 100个字符，由数字0 - 9、字符a - z、A - Z，及特殊符 `-` 组成。
  - 参数值：1 - 1000个字符，不支持中文。
- 一个修改 HTTP 请求头操作中，可添加多条不同类型操作，最多30条，执行顺序为从上至下。
- 部分标准头部不支持修改，清单如下：
```js.
Date
Expires
Content-Type
Content-Encoding
Content-Length
Transfer-Encoding
Cache-Control
If-Modified-Since
Last-Modified
Connection
Content-Range
ETag
Accept-Ranges
Age
Authentication-Info
Proxy-Authenticate
Retry-After
Set-Cookie
Vary
WWW-Authenticate
Content-Location
Content-MD5
Content-Range
Meter
Allow
Error
```

## 配置示例
### Access-Control-Allow-Origin
用于解决资源的跨域权限问题，实现跨域访问。

- 头部名称：Access-Control-Allow-Origin。
- 头部值：支持输入“*” ，或多个域名 / IP / 域名与 IP 混填（必须包含 `http://` 或 `https://`，例如：`http://test.com,http://1.1.1.1`， 逗号隔开，最多可输入1000字符）。
- 不同值示例说明：
<table>
<thead>
<tr>
<th width="20%">头部值</th>
<th width="80%">说明</th>
</tr>
</thead>
<tbody><tr>
<td>*</td>
<td>全匹配：<br>响应添加头部： <code>Access-Control-Allow-Origin:*</code>，允许被所有域请求。</td>
</tr>
<tr>
<td><code>http://cloud.tencent.com</code>, <code>https://cloud.tencent.com</code>,<code>http://www.b.com</code></td>
<td>固定匹配：<ul><li>来源 <code>https://cloud.tencent.com</code>，命中列表，则响应添加头部： <code>Access-Control-Allow-Origin: https://cloud.tencent.com</code>。</li><li>来源为 <code>https://www.qq.com</code>，未命中列表，响应无变化。</li></td>
</tr>
<tr>
<td><code>https://*.tencent.com</code></td>
<td>二级泛域名匹配：<ul><li>来源 <code>https://cloud.tencent.com</code>，命中列表，则响应添加头部： <code>Access-Control-Allow-Origin: https://cloud.tencent.com</code>。</li><li>来源为 <code>https://cloud.qq.com</code>，未命中列表，响应无变化。</li></td>
</tr>
<tr>
<td><code>https://cloud.tencent.com:8080</code></td>
<td>端口匹配：<ul><li>来源为 <code>https://cloud.tencent.com:8080</code>，命中列表，则响应添加头部： <code>Access-Control-Allow-Origin:https://cloud.tencent.com:8080</code>。</li><li>来源为 <code>https://cloud.tencent.com</code>，未命中列表，响应无变化。</li>注意：若存在特殊端口，则需要在列表中填写相关信息，不支持任意端口匹配，必须指定。</td>
</tr>
</tbody></table>

### Access-Control-Expose-Headers
用于指定哪些头部可以作为响应的一部分暴露给客户端。
>?默认情况下，只有6种头部可以暴露给客户端：Cache-Control、Content-Language、Content-Type、Expires、Last-Modified、Pragma。
>
- 头部名称：Access-Control-Expose-Headers。
- 头部值：输入希望暴露给客户端的头部名称（除默认的6个头部外），多个值用“;”分隔，例如：`Content-Length`,`X-My-Header`。

### Content-Disposition
用来激活浏览器的下载，同时可以设置默认的下载的文件名。

服务端向客户端浏览器发送文件时，如果是浏览器支持的文件类型，如 TXT、JPG 等类型，会默认直接使用浏览器打开，如果需要提示用户保存，则可以通过配置 Content-Disposition 字段覆盖浏览器默认行为。

- 头部名称：Content-Disposition。
- 头部值：常见配置示例如：`attachment;filename=FileName.txt`。

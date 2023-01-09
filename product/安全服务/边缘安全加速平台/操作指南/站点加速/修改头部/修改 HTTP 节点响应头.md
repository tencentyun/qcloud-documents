## 功能简介
支持自定义变更/增加/删除 HTTP 响应头（从节点响应客户端用户时的 HTTP 响应头），不会影响节点缓存。


## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone) ，在左侧菜单栏中，单击**规则引擎**。
2. 在规则引擎页面，选择所需站点，可按需配置修改 HTTP 节点响应头规则。如何使用规则引擎，请参见 [规则引擎](https://cloud.tencent.com/document/product/1552/70901)。
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
<td>删除指定的头部。</td>
</tr>
</tbody></table>

## 注意事项
- 自定义头部参数格式要求如下：
  - 参数名：1 - 100个字符，由数字0 - 9、字符a - z、A - Z，及特殊符 `-` 组成。
  - 参数值：1 - 1000个字符，不支持中文。
- 一个修改 HTTP 请求头操作中，可添加多条不同类型操作，最多30条，执行顺序为从上至下。
- 部分标准头部不支持修改，清单如下：
```js.
Accept-Ranges
Age
Allow
Authentication-Info
Cache-Control
Connection
Content-Encoding
Content-Length
Content-Location
Content-MD5
Content-Range
Content-Type
Date
Error
ETag
Expires
If-Modified-Since
Last-Modified
Meter
Proxy-Authenticate
Retry-After
Set-Cookie
Transfer-Encoding
Vary
WWW-Authenticate
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
<td>固定匹配：<ul><li>来源 <code>https://cloud.tencent.com</code>，命中列表，则响应添加头部： <code>Access-Control-Allow-Origin: https://cloud.tencent.com</code>。</li><li>来源为 <code>https://www.qq.com</code>，未命中列表，则不会响应跨域头部。</li></td>
</tr>
<tr>
<td><code>https://*.tencent.com</code></td>
<td>二级泛域名匹配：<ul><li>来源 <code>https://cloud.tencent.com</code>，命中列表，则响应添加头部： <code>Access-Control-Allow-Origin: https://cloud.tencent.com</code>。</li><li>来源为 <code>https://cloud.qq.com</code>，未命中列表，则不会响应跨域头部。</li></td>
</tr>
<tr>
<td><code>https://cloud.tencent.com:8080</code></td>
<td>端口匹配：<ul><li>来源为 <code>https://cloud.tencent.com:8080</code>，命中列表，则响应添加头部： <code>Access-Control-Allow-Origin:https://cloud.tencent.com:8080</code>。</li><li>来源为 <code>https://cloud.tencent.com</code>，未命中列表，则不会响应跨域头部。</li>注意：不支持任意端口匹配，若存在特殊端口，则必须在头部值中指定该端口。</td>
</tr>
</tbody></table>

### Access-Control-Allow-Methods
设置跨域允许的 HTTP 请求方法。

- 头部名称：Access-Control-Allow-Methods。
- 头部值：可同时设置多个，例如 POST,GET,POTIONS。


### Access-Control-Max-Age
指定预检请求的结果在多少秒内有效。
>?非简单的跨域请求，在正式通信之前，需要增加一次 HTTP 查询请求，称为“预请求”，用来查明这个跨域请求是不是安全可以接受的，如下请求会被视为非简单的跨域请求：
以 GET、HEAD 或者 POST 以外的方式发起，或者使用 POST，但是请求数据类型为 application / x-www-form-urlencoded、 multipart / form-data、text / plain 以外的数据类型，如 application / xml 或者 text / xml。

- 头部名称：Access-Control-Max-Age。
- 头部值：输入秒数，例如1728000。


### Content-Language
指定访问页面所使用的语言。
- 头部名称：Content-Language。
- 头部值：例如 zh-CN 或 en-US。

### Content-Disposition
用来激活浏览器的下载，同时可以设置默认的下载的文件名。

服务端向客户端浏览器发送文件时，如果是浏览器支持的文件类型，如 TXT、JPG 等类型，会默认直接使用浏览器打开，如果需要提示用户保存，则可以通过配置 Content-Disposition 字段覆盖浏览器默认行为。

- 头部名称：Content-Disposition。
- 头部值：常见配置示例如：`attachment;filename=FileName.txt`。


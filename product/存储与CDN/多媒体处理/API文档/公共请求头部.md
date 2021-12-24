## 描述


此篇文档将为您介绍在使用 API 时候会使用到的公共请求头部（Request Header），下文提到的头部在之后的具体 API 文档中不再赘述。

## 请求头部列表


<table>
<thead>
<tr>
<th >Header 名称</th>
<th>描述</th>
<th>类型</th>
<th>是否必选</th>
</tr>
</thead>
<tbody><tr>
<td>Authorization</td>
<td>携带鉴权信息，用以验证请求合法性的签名信息。</td>
<td>string</td>
<td>是。</td>
</tr>
<tr>
<td nowrap="nowrap">Content-Length</td>
<td>RFC 2616 中定义的 HTTP 请求内容长度（字节）。</td>
<td>integer</td>
<td>否。<br>针对 PUT 和 POST 请求，此头部是必选项。</td>
</tr>
<tr>
<td>Content-Type</td>
<td>RFC 2616 中定义的 HTTP 请求内容类型（MIME），例如 <code>application/xml</code>。</td>
<td>string</td>
<td>否。<br>针对有请求体的 PUT 和 POST 请求，此头部是必选项。</td>
</tr>
<tr>
<td>Content-MD5</td>
<td>RFC 1864 中定义的经过 Base64 编码的请求体内容 MD5 哈希值，例如 <code>ZzD3iDJdrMAAb00lgLLeig==</code>。此头部用于完整性检查，验证请求体在传输过程中是否发生变化。</td>
<td>string</td>
<td>否。</td>
</tr>
<tr>
<td>Date</td>
<td>RFC 1123 中定义的 GMT 格式当前时间，例如 <code>Wed, 29 May 2019 04:10:12 GMT</code>。</td>
<td>string</td>
<td>否。</td>
</tr>
<tr>
<td>Host</td>
<td>请求的主机，形式为 <code>&lt;BucketName-APPID&gt;.ci.&lt;Region&gt;.myqcloud.com</code></td>
<td>string</td>
<td>是。</td>
</tr>
<tr>
<td nowrap="nowrap">x-ci-security-token</td>
<td>使用临时安全凭证时需要传入的安全令牌字段。</td>
<td>string</td>
<td>否。<br>当使用临时密钥并通过 <code>Authorization</code> 携带鉴权信息时，此头部为必选项。</td>
</tr>
</tbody></table>





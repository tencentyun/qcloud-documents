## 描述

此篇文档将为您介绍在使用 API 时候会出现的公共返回头部（Response Header），下文提到的头部会在之后的具体 API 文档中不再赘述。

## 响应头部列表

<table>
   <tr>
      <th>Header 名称</th>
      <th>描述</th>
      <th>类型</th>
   </tr>
   <tr>
      <td nowrap="nowrap">Content-Length</td>
      <td>RFC 2616 中定义的 HTTP 响应内容长度（字节）。</td>
      <td>string</td>
   </tr>
   <tr>
      <td>Content-Type</td>
      <td>RFC 2616 中定义的 HTTP 响应内容类型（MIME）。</td>
      <td>string</td>
   </tr>
   <tr>
      <td>Connection</td>
      <td>RFC 2616 中定义，表明响应完成后是否会关闭网络连接。枚举值：keep-alive，close。</td>
      <td>Enum</td>
   </tr>
   <tr>
      <td>Date</td>
			<td>RFC 1123 中定义的 GMT 格式服务端响应时间，例如<code>Wed, 29 May 2019 04:10:12 GMT</code>。</td>
      <td>string</td>
   </tr>
   <tr>
      <td>Server</td>
			<td>接受请求并返回响应的服务器的名称，默认值：<code>tencent-ci</code>。</td>
      <td>string</td>
   </tr>
   <tr>
      <td nowrap="nowrap">x-ci-request-id</td>
      <td>每次请求发送时，服务端将会自动为请求生成一个 ID。</td>
      <td>string</td>
   </tr>
   <tr>
      <td>x-ci-trace-id</td>
      <td>每次请求出错时，服务端将会自动为这个错误生成一个ID。仅当请求出错时才会在响应中包含此头部。</td>
      <td>string</td>
   </tr>
</table>


## Properties（属性）

[](id:body)
### body
**body**: `string`
body 代表服务器提供的响应。


[](id:contentLength)
### contentLength
**contentLength**: `number`
contentLength 记录关联内容的长度。 -1：表示长度未知。>= 0：表示可以从 body 中读取给定的字节数。


[](id:headers)
### headers
**headers**: `Record`<`string`, `string`\>
headers 表示服务器响应的 HTTP 头。


[](id:proto)
### proto
**proto**: `string`
proto 表示协议。例如 'HTTP/1.0'。


[](id:request)
### request
**request**: [`Request`](https://cloud.tencent.com/document/product/1484/75823)
request 是为获得此响应而发送的请求。


[](id:responseTimeMS)
### responseTimeMS
**responseTimeMS**: `number`
responseTimeMS 表示请求响应时间，单位毫秒。


[](id:status)
### status
**status**: `string`
status 是来自服务器响应的 HTTP 状态消息。例如 '200 OK'。


[](id:statusCode)
### statusCode
**statusCode**: `number`
statusCode 是来自服务器响应的 HTTP 状态代码。例如 200。


## Methods

[](id:json)
### json
**json**(): `any`
JSON对象

将 Response.body 反序列化为 json。
```js
import http from 'pts/http';

export default function () {
    const data = {user_id: '12345'};
    const resp = http.get('http://httpbin.org/get', {query: data});
    console.log(resp.json().args.user_id); // 12345
};
```
**Returns**：`any`

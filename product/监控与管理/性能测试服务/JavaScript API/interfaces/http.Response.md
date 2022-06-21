# Interface: Response

[http](../modules/http.md).Response

## Table of contents

### Properties

- [body](#body)
- [contentLength](#contentlength)
- [headers](#headers)
- [proto](#proto)
- [request](#request)
- [responseTimeMS](#responsetimems)
- [status](#status)
- [statusCode](#statuscode)

### Methods

- [json](http.Response.md#json)

## Properties

<span id="body"></span>

### body

• **body**: `string`

body 代表服务器提供的响应。

#### Defined in

typings/http.d.ts:76

___

<span id="contentLength"></span>

### contentLength

• **contentLength**: `number`

contentLength 记录关联内容的长度。 -1 表示长度未知。>= 0 表示可以从 body 中读取给定的字节数。

#### Defined in

typings/http.d.ts:96

___

<span id="headers"></span>

### headers

• **headers**: `Record`<`string`, `string`\>

headers 表示服务器响应的 HTTP 头。

#### Defined in

typings/http.d.ts:80

___

<span id="proto"></span>

### proto

• **proto**: `string`

proto 表示协议。例如 'HTTP/1.0'。

#### Defined in

typings/http.d.ts:92

___

<span id="request"></span>

### request

• **request**: [`Request`](http.Request.md)

request 是为获得此响应而发送的请求。

#### Defined in

typings/http.d.ts:104

___

<span id="responseTimeMS"></span>

### responseTimeMS

• **responseTimeMS**: `number`

responseTimeMS 表示请求响应时间，单位毫秒。

#### Defined in

typings/http.d.ts:100

___

<span id="status"></span>

### status

• **status**: `string`

status 是来自服务器响应的 HTTP 状态消息。例如 '200 OK'。

#### Defined in

typings/http.d.ts:84

___

<span id="statusCode"></span>

### statusCode

• **statusCode**: `number`

statusCode 是来自服务器响应的 HTTP 状态代码。例如 200。

#### Defined in

typings/http.d.ts:88

## Methods

<span id="json"></span>

### json

▸ **json**(): `any`

将 Response.body 反序列化为 json。

```js
import http from 'pts/http';

export default function () {
    const data = {user_id: '12345'};
    const resp = http.get('http://httpbin.org/get', {query: data});
    console.log(resp.json().args.user_id); // 12345
};
```

#### Returns

`any`

JSON对象

#### Defined in

typings/http.d.ts:121

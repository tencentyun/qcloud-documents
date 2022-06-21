# Interface: Request

[http](../modules/http.md).Request

## Table of contents

### Properties

- [basicAuth](#basicauth)
- [body](#body)
- [contentLength](#contentlength)
- [discardResponseBody](#discardresponsebody)
- [headers](#headers)
- [host](#host)
- [maxRedirects](#maxredirects)
- [method](#method)
- [path](#path)
- [query](#query)
- [scheme](#scheme)
- [service](#service)
- [timeout](#timeout)
- [url](#url)

### Methods

- [chunked](http.Request.md#chunked)

## Properties

<span id="basicAuth"></span>

### basicAuth

• `Optional` **basicAuth**: [`BasicAuth`](global.BasicAuth.md)

basicAuth http 基础鉴权。

#### Defined in

typings/http.d.ts:37

___

<span id="body"></span>

### body

• `Optional` **body**: `string` \| `object` \| `ArrayBuffer`

body 是要发送的请求体。只有当使用 do 方法时才需要指定。

#### Defined in

typings/http.d.ts:25

___

<span id="contentLength"></span>

### contentLength

• `Optional` **contentLength**: `number`

contentLength 记录关联内容的长度。 -1 表示长度未知。>= 0 表示可以从 body 中读取给定的字节数。

#### Defined in

typings/http.d.ts:57

___

<span id="discardResponseBody"></span>

### discardResponseBody

• `Optional` **discardResponseBody**: `boolean`

discardResponseBody 丢弃响应体，适用于响应体太大且不需要对响应体内容进行 check 的场景。

#### Defined in

typings/http.d.ts:41

___

<span id="headers"></span>

### headers

• `Optional` **headers**: `Record`<`string`, `string`\>

headers 包含由客户端发送的请求头字段。

#### Defined in

typings/http.d.ts:17

___

<span id="host"></span>

### host

• `Optional` **host**: `string`

host 或者 host:port。

#### Defined in

typings/http.d.ts:45

___

<span id="maxRedirects"></span>

### maxRedirects

• `Optional` **maxRedirects**: `number`

maxRedirects 重定向跳转次数。

#### Defined in

typings/http.d.ts:29

___

<span id="method"></span>

### method

• `Optional` **method**: `string`

method 指定 HTTP 方法（GET、POST、PUT 等）。只有当使用 do 方法时才需要指定。

#### Defined in

typings/http.d.ts:9

___

<span id="path"></span>

### path

• `Optional` **path**: `string`

path 表示路径（相对路径省略前导斜杠）。

#### Defined in

typings/http.d.ts:49

___

<span id="query"></span>

### query

• `Optional` **query**: `Record`<`string`, `string`\>

query 是与请求一起发送的 URL 参数。

#### Defined in

typings/http.d.ts:21

___

<span id="scheme"></span>

### scheme

• `Optional` **scheme**: ``"http"`` \| ``"https"``

scheme 协议 http/https。

#### Defined in

typings/http.d.ts:53

___

<span id="contentType"></span>

### service

• `Optional` **service**: `string`

service 在 PTS 中，我们按照 url 来识别不同 service，基于 serivce 纬度生成报表。
当 url 中包含参数: http://demo.com/{id}，不同的 id 将导致请求在报表中被归类为不同的服务；
或者每个 url 含有不同的 ip port 的时候也会被归类为不同的服务；
你可通过指定 service，将此类请求在报表中归类到到同一个服务下。

#### Defined in

typings/http.d.ts:64

___

<span id="timeout"></span>

### timeout

• `Optional` **timeout**: `number`

timeout 指定此客户端发出的请求的时间限制。 超时包括连接时间、任何重定向和读取响应正文。单位毫秒。

#### Defined in

typings/http.d.ts:33

___

<span id="url"></span>

### url

• `Optional` **url**: `string`

url 指定要访问的 URL。只有当使用 do 方法时才需要指定。

#### Defined in

typings/http.d.ts:13

## Methods

<span id="chunked"></span>

### chunked

▸ `Optional` **chunked**(`body`): `void`

chunked 当数据以一系列分块的形式进行发送时，如果指定了 chunked 函数，会按行读取响应体，
每次读取到响应体之后回调 chunked 函数。

#### Parameters

| Name | Type |
| :------ | :------ |
| `body` | `string` |

#### Returns

`void`

#### Defined in

typings/http.d.ts:69

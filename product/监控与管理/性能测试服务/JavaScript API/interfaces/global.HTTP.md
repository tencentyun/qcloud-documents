# Interface: HTTP

[global](../modules/global.md).HTTP

## Table of contents

### Properties

- [basicAuth](#basicauth)
- [disableKeepAlives](#disablekeepalives)
- [discardResponseBody](#discardresponsebody)
- [headers](#headers)
- [http2](#http2)
- [maxIdleConns](#maxidleconns)
- [maxIdleConnsPerHost](#maxidleconnsperhost)
- [maxRedirects](#maxredirects)
- [timeout](#timeout)

## Properties

<span id="basicAuth"></span>

### basicAuth

• **basicAuth**: [`BasicAuth`](global.BasicAuth.md)

HTTP Basic authentication

```js
export const option = {
    http: {
        basicAuth: {
            username: 'user',
            password: 'passwd',
        }
    }
}
```

#### Defined in

typings/global.d.ts:265

___

<span id="disableKeepAlives"></span>

### disableKeepAlives

• **disableKeepAlives**: `boolean`

是否禁用长连接

```js
export const option = {
    http: {
        disableKeepAlives: true
    }
}
```

#### Defined in

typings/global.d.ts:224

___

<span id="discardResponseBody"></span>

### discardResponseBody

• **discardResponseBody**: `boolean`

是否丢弃回包

```js
export const option = {
    http: {
        discardResponseBody: true
    }
}
```

#### Defined in

typings/global.d.ts:277

___

<span id="headers"></span>

### headers

• **headers**: `Record`<`string`, `string`\>

http 请求头

```js
export const option = {
    http: {
        headers: {
            'key': 'value'
        }
    }
}
```

#### Defined in

typings/global.d.ts:238

___

<span id="http2"></span>

### http2

• **http2**: `boolean`

是否启用 HTTP2

```js
export const option = {
    http: {
        http2: true
    }
}
```

#### Defined in

typings/global.d.ts:289

___

<span id="maxIdleConns"></span>

### maxIdleConns

• **maxIdleConns**: `number`

单个 VU 最大活跃连接数

```js
export const option = {
    http: {
        maxIdleConns: 50
    }
}
```

#### Defined in

typings/global.d.ts:200

___

<span id="maxIdleConnsPerHost"></span>

### maxIdleConnsPerHost

• **maxIdleConnsPerHost**: `number`

单个 VU 单个域名最大活跃连接数

```js
export const option = {
    http: {
        maxIdleConnsPerHost: 10
    }
}
```

#### Defined in

typings/global.d.ts:212

___

<span id="maxRedirects"></span>

### maxRedirects

• **maxRedirects**: `number`

http 重定向跳转次数

```js
export const option = {
    http: {
        maxRedirects: 5
    }
}
```

#### Defined in

typings/global.d.ts:188

___

<span id="timeout"></span>

### timeout

• **timeout**: `number`

请求超时时间，单位毫秒

```js
export const option = {
    http: {
        timeout: 3000
    }
}
```

#### Defined in

typings/global.d.ts:250

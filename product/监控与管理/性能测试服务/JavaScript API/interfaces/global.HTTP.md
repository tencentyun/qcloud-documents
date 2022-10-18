## Properties（属性）
[](id:basicAuth)
### basicAuth
**basicAuth**: [`BasicAuth`](https://cloud.tencent.com/document/product/1484/75806)

HTTP Basic authentication
```plaintext
export const option = {
    http: {
        basicAuth: {
            username: 'user',
            password: 'passwd',
        }
    }
}
```


[](id:disableKeepAlives)
### disableKeepAlives
**disableKeepAlives**: `boolean`

是否禁用长连接
``` plaintext
export const option = {
    http: {
        disableKeepAlives: true
    }
}
```


[](id:discardResponseBody)
### discardResponseBody
**discardResponseBody**: `boolean`

是否丢弃回包
```json
export const option = {
    http: {
        discardResponseBody: true
    }
}
```

[](id:headers)
### headers
**headers**: `Record`<`string`, `string`\>

http 请求头
```json
export const option = {
    http: {
        headers: {
            'key': 'value'
        }
    }
}
```

[](id:http2)
### http2
**http2**: `boolean`

是否启用 HTTP2
```json
export const option = {
    http: {
        http2: true
    }
}
```

[](id:maxIdleConns)
### maxIdleConns
**maxIdleConns**: `number`

单个 VU 最大活跃连接数
```json
export const option = {
    http: {
        maxIdleConns: 50
    }
}
```

[](id:maxIdleConnsPerHost)
### maxIdleConnsPerHost
**maxIdleConnsPerHost**: `number`

单个 VU 单个域名最大活跃连接数
```plaintext
export const option = {
    http: {
        maxIdleConnsPerHost: 10
    }
}
```


[](id:maxRedirects)
### maxRedirects
**maxRedirects**: `number`

http 重定向跳转次数
```js
export const option = {
    http: {
        maxRedirects: 5
    }
}
```

[](id:timeout)
### timeout
**timeout**: `number`

请求超时时间，单位毫秒
```json
export const option = {
    http: {
        timeout: 3000
    }
}
```


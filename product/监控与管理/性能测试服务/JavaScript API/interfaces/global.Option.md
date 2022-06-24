## Properties（属性）
[](id:http)
### http
- **http**: [`HTTP`](https://cloud.tencent.com/document/product/1484/75811)

```
Defined in typings/global.d.ts:147
```
HTTP 参数选项
```js
export const option = {
    http: {
        maxRedirects: 10,
        maxIdleConns: 100,
    }
}
```

[](id:setupTimeoutSeconds)
### setupTimeoutSeconds
- **setupTimeoutSeconds**: `number`

```
Defined in typings/global.d.ts:109
```
setup 超时时间
```js
export const option = {
    setupTimeoutSeconds: 30
}
```



### teardownTimeoutSeconds
- **teardownTimeoutSeconds**: `number`

```
Defined in typings/global.d.ts:118
```
teardown 超时时间
```
export const option = {
    teardownTimeoutSeconds: 30
}
```



### tlsConfig
- **tlsConfig**: `Record`<`string`, [`TLSConfig`](https://cloud.tencent.com/document/product/1484/75813)\>
```
Defined in typings/global.d.ts:134
```
Transport Layer Security 配置
```
export const option = {
    tlsConfig: {
        'localhost': {
            insecureSkipVerify: false,
            rootCAs: [open('tool/tls/twoway/ca.crt')],
            certificates: [{cert: open('tool/tls/twoway/client.crt'), key: open('tool/tls/twoway/client.key')}]
        }
    }
}
```

[](id:trpc)
### trpc
- **trpc**: [`TRPC`](https://cloud.tencent.com/document/product/1484/75814)

```
Defined in typings/global.d.ts:160
```
TRPC 参数选项
```
export const option = {
    trpc: {
        env: "formal",
        namespace: "Production",
    }
}
```

[](id:ws)
### ws
- **ws**: [`WS`](https://cloud.tencent.com/document/product/1484/75815)

```
Defined in typings/global.d.ts:173
```
WS 参数选项
```
export const option = {
    ws: {
        writeTimeout: 3000,
        readTimeout: 3000,
    }
}
```

# Interface: Option

[global](../modules/global.md).Option

## Table of contents

### Properties

- [http](#http)
- [setupTimeoutSeconds](#setuptimeoutseconds)
- [teardownTimeoutSeconds](#teardowntimeoutseconds)
- [tlsConfig](#tlsconfig)
- [trpc](#trpc)
- [ws](#ws)

## Properties

<span id="http"></span>

### http

• **http**: [`HTTP`](global.HTTP.md)

HTTP 参数选项

```js
export const option = {
    http: {
        maxRedirects: 10,
        maxIdleConns: 100,
    }
}
```

#### Defined in

typings/global.d.ts:147

___

<span id="setupTimeoutSeconds"></span>

### setupTimeoutSeconds

• **setupTimeoutSeconds**: `number`

setup 超时时间

```js
export const option = {
    setupTimeoutSeconds: 30
}

#### Defined in

typings/global.d.ts:109

___

### teardownTimeoutSeconds

• **teardownTimeoutSeconds**: `number`

teardown 超时时间

​```js
export const option = {
    teardownTimeoutSeconds: 30
}

#### Defined in

typings/global.d.ts:118

___

### tlsConfig

• **tlsConfig**: `Record`<`string`, [`TLSConfig`](global.TLSConfig.md)\>

Transport Layer Security 配置

​```js
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

#### Defined in

typings/global.d.ts:134

___

<span id="trpc"></span>

### trpc

• **trpc**: [`TRPC`](global.TRPC.md)

TRPC 参数选项

```js
export const option = {
    trpc: {
        env: "formal",
        namespace: "Production",
    }
}
```

#### Defined in

typings/global.d.ts:160

___

<span id="ws"></span>

### ws

• **ws**: [`WS`](global.WS.md)

WS 参数选项

```js
export const option = {
    ws: {
        writeTimeout: 3000,
        readTimeout: 3000,
    }
}
```

#### Defined in

typings/global.d.ts:173

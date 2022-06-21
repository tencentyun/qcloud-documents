# Interface: WS

[global](../modules/global.md).WS

## Table of contents

### Properties

- [handshakeTimeout](#handshaketimeout)
- [readTimeout](#readtimeout)
- [writeControlTimeout](#writecontroltimeout)
- [writeTimeout](#writetimeout)

## Properties

<span id="handshakeTimeout"></span>

### handshakeTimeout

• **handshakeTimeout**: `number`

握手超时时间，单位毫秒，默认 30s

```js
export const option = {
    ws: {
        handshakeTimeout: 10000
    }
}
```

#### Defined in

typings/global.d.ts:355

___

<span id="readTimeout"></span>

### readTimeout

• **readTimeout**: `number`

读消息超时时间，单位毫秒，默认不限制

```js
export const option = {
    ws: {
        readTimeout: 3000
    }
}
```

#### Defined in

typings/global.d.ts:378

___

<span id="writeControlTimeout"></span>

### writeControlTimeout

• **writeControlTimeout**: `number`

写控制指令超时时间，单位毫秒，默认 10s

```js
export const option = {
    ws: {
        writeControlTimeout: 10000
    }
}
```

#### Defined in

typings/global.d.ts:343

___

<span id="writeTimeout"></span>

### writeTimeout

• **writeTimeout**: `number`

写消息超时时间，单位毫秒，默认不限制
```js
export const option = {
    ws: {
        writeTimeout: 3000
    }
}
```

#### Defined in

typings/global.d.ts:366

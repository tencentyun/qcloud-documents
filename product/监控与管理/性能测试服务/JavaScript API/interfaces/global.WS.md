## Properties（属性）
[](id:handshakeTimeout)
### handshakeTimeout
**handshakeTimeout**: `number`

握手超时时间，单位毫秒，默认30s
```js
export const option = {
    ws: {
        handshakeTimeout: 10000
    }
}
```

[](id:readTimeout)
### readTimeout
**readTimeout**: `number`

读消息超时时间，单位毫秒，默认不限制
```js
export const option = {
    ws: {
        readTimeout: 3000
    }
}
```

[](id:writeControlTimeout)
### writeControlTimeout
**writeControlTimeout**: `number`

写控制指令超时时间，单位毫秒，默认10s
```js
export const option = {
    ws: {
        writeControlTimeout: 10000
    }
}
```

[](id:writeTimeout)
### writeTimeout
**writeTimeout**: `number`

写消息超时时间，单位毫秒，默认不限制
```js
export const option = {
    ws: {
        writeTimeout: 3000
    }
}
```

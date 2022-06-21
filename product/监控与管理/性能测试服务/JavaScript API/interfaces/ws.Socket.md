# Interface: Socket

[ws](../modules/ws.md).Socket

## Table of contents

### Methods

- [close](#close)
- [on](#on)
- [ping](#ping)
- [pong](#pong)
- [send](#send)
- [sendBinary](#sendbinary)
- [setInterval](#setinterval)
- [setLoop](#setloop)
- [setTimeout](#settimeout)

## Methods

<span id="close"></span>

### close

▸ **close**(): `void`

连接关闭。

#### Returns

`void`

#### Defined in

typings/ws.d.ts:27

___

<span id="on"></span>

### on

▸ **on**(`event`, `callback`): `void`

消息事件监听。

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `event` | `string` | 事件名 |
| `callback` | (...`args`: `any`[]) => `void` | 回调函数 |

#### Returns

`void`

#### Defined in

typings/ws.d.ts:50

___

<span id="ping"></span>

### ping

▸ **ping**(): `void`

发送 ping 消息。

#### Returns

`void`

#### Defined in

typings/ws.d.ts:19

___

<span id="pong"></span>

### pong

▸ **pong**(): `void`

发送 pong 消息。

#### Returns

`void`

#### Defined in

typings/ws.d.ts:23

___

<span id="send"></span>

### send

▸ **send**(`msg`): `void`

文本消息发送。

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msg` | `string` | 文本内容 |

#### Returns

`void`

#### Defined in

typings/ws.d.ts:10

___

<span id="sendBinary"></span>

### sendBinary

▸ **sendBinary**(`msg`): `void`

二进制消息发送。

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `msg` | `ArrayBuffer` | 二进制内容 |

#### Returns

`void`

#### Defined in

typings/ws.d.ts:15

___

<span id="setInterval"></span>

### setInterval

▸ **setInterval**(`callback`, `intervalMs`): `void`

设置轮询函数。

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `callback` | () => `void` | 回调函数 |
| `intervalMs` | `number` | 设置时间，单位毫秒 |

#### Returns

`void`

#### Defined in

typings/ws.d.ts:33

___

<span id="setLoop"></span>

### setLoop

▸ **setLoop**(`callback`): `void`

循环执行函数。

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `callback` | () => `void` | 回调函数 |

#### Returns

`void`

#### Defined in

typings/ws.d.ts:44

___

<span id="setTimeout"></span>

### setTimeout

▸ **setTimeout**(`callback`, `intervalMs`): `void`

设置定时函数。

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `callback` | () => `void` | 回调函数 |
| `intervalMs` | `number` | 设置时间，单位毫秒 |

#### Returns

`void`

#### Defined in

typings/ws.d.ts:39

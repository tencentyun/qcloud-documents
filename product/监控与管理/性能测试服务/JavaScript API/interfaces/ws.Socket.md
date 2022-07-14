## Methods（方法）
[](id:close)
### close
**close**(): `void`
连接关闭。
```
Defined in typings/ws.d.ts:27
```
**Returns：**`void`

[](id:on)
### on
**on**(`event`, `callback`): `void`
消息事件监听。
```
Defined in typings/ws.d.ts:50
```

#### Parameters
| Name       | Type                           | Description |
| :--------- | :----------------------------- | :---------- |
| `event`    | `string`                       | 事件名      |
| `callback` | (...`args`: `any`[]) => `void` | 回调函数    |

**Returns：**`void`

[](id:ping)
### ping
**ping**(): `void`
发送 ping 消息。
```
Defined in typings/ws.d.ts:19
```
**Returns：**`void`

[](id:pong)
### pong
**pong**(): `void`
发送 pong 消息。
```
Defined in typings/ws.d.ts:23
```
**Returns：**`void`

[](id:send)
### send
**send**(`msg`): `void`
文本消息发送。
```
Defined in typings/ws.d.ts:10
```


#### Parameters
| Name  | Type     | Description |
| :---- | :------- | :---------- |
| `msg` | `string` | 文本内容    |

**Returns：**`void`

[](id:sendBinary)
### sendBinary
**sendBinary**(`msg`): `void`
二进制消息发送。
```
Defined in typings/ws.d.ts:15
```


#### Parameters
| Name  | Type          | Description |
| :---- | :------------ | :---------- |
| `msg` | `ArrayBuffer` | 二进制内容  |

**Returns：**`void`

[](id:setInterval)
### setInterval
**setInterval**(`callback`, `intervalMs`): `void`
设置轮询函数。
```
Defined in typings/ws.d.ts:33
```

#### Parameters
| Name         | Type         | Description        |
| :----------- | :----------- | :----------------- |
| `callback`   | () => `void` | 回调函数           |
| `intervalMs` | `number`     | 设置时间，单位毫秒 |

**Returns：**`void`

[](id:setLoop)
### setLoop
**setLoop**(`callback`): `void`
循环执行函数。
```
Defined in typings/ws.d.ts:44
```

#### Parameters
| Name       | Type         | Description |
| :--------- | :----------- | :---------- |
| `callback` | () => `void` | 回调函数    |

**Returns：**`void`

[](id:setTimeout)
### setTimeout
**setTimeout**(`callback`, `intervalMs`): `void`
设置定时函数。
```
Defined in typings/ws.d.ts:39
```

#### Parameters
| Name         | Type         | Description        |
| :----------- | :----------- | :----------------- |
| `callback`   | () => `void` | 回调函数           |
| `intervalMs` | `number`     | 设置时间，单位毫秒 |

**Returns：**`void`

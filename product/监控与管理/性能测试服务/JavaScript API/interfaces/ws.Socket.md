## Methods（方法）
[](id:close)
### close
**close**(): `void`
连接关闭。

**Returns：**`void`

[](id:on)
### on
**on**(`event`, `callback`): `void`
消息事件监听。


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

**Returns：**`void`

[](id:pong)
### pong
**pong**(): `void`
发送 pong 消息。

**Returns：**`void`

[](id:send)
### send
**send**(`msg`): `void`
文本消息发送。



#### Parameters
| Name  | Type     | Description |
| :---- | :------- | :---------- |
| `msg` | `string` | 文本内容    |

**Returns：**`void`

[](id:sendBinary)
### sendBinary
**sendBinary**(`msg`): `void`
二进制消息发送。


#### Parameters
| Name  | Type          | Description |
| :---- | :------------ | :---------- |
| `msg` | `ArrayBuffer` | 二进制内容  |

**Returns：**`void`

[](id:setInterval)
### setInterval
**setInterval**(`callback`, `intervalMs`): `void`
设置轮询函数。


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

#### Parameters
| Name       | Type         | Description |
| :--------- | :----------- | :---------- |
| `callback` | () => `void` | 回调函数    |

**Returns：**`void`

[](id:setTimeout)
### setTimeout
**setTimeout**(`callback`, `intervalMs`): `void`
设置定时函数。


#### Parameters
| Name         | Type         | Description        |
| :----------- | :----------- | :----------------- |
| `callback`   | () => `void` | 回调函数           |
| `intervalMs` | `number`     | 设置时间，单位毫秒 |

**Returns：**`void`

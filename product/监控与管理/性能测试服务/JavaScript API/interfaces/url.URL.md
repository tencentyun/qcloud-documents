## Constructors（构造函数）

[](id:constructor)
### constructor
- **new URL**(`url`, `base?`)

#### Parameters
| Name    | Type                                                         |
| :------ | :----------------------------------------------------------- |
| `url`   | `string`                                                     |
| `base?` | `string` \| [`URL`](https://cloud.tencent.com/document/product/1484/75838) |


```
Defined in typings/url.d.ts:5
```


## Properties（属性）

[](id:hash)
### hash
- **hash**: `string`

```
Defined in node_modules/typescript/lib/lib.dom.d.ts:14342
```

[](id:host)
### host
- **host**: `string`

```
Defined in node_modules/typescript/lib/lib.dom.d.ts:14343
```

[](id:contentType)
### hostname
- **hostname**: `string`

```
Defined in node_modules/typescript/lib/lib.dom.d.ts:14344
```

[](id:href)
### href
**href**: `string`

```
Defined in node_modules/typescript/lib/lib.dom.d.ts:14345
```

[](id:origin)
### origin
- `Readonly` **origin**: `string`

```
Defined in node_modules/typescript/lib/lib.dom.d.ts:14347
```

[](id:password)
### password
- **password**: `string`

```
Defined in node_modules/typescript/lib/lib.dom.d.ts:14348
```

[](id:pathname)
### pathname
- **pathname**: `string`

```
Defined in node_modules/typescript/lib/lib.dom.d.ts:14349
```

[](id:port)
### port
- **port**: `string`

```
Defined in node_modules/typescript/lib/lib.dom.d.ts:14350
```

[](id:protocol)
### protocol
- **protocol**: `string`

```
Defined in node_modules/typescript/lib/lib.dom.d.ts:14351
```

[](id:search)
### search
- **search**: `string`

```
Defined in node_modules/typescript/lib/lib.dom.d.ts:14352
```

[](id:searchParams)
### searchParams
- `Readonly` **searchParams**: [`URLSearchParams`](https://cloud.tencent.com/document/product/1484/75833#urlsearchparams)

```
Defined in node_modules/typescript/lib/lib.dom.d.ts:14353
```

[](id:username)
### username
- **username**: `string`

```
Defined in node_modules/typescript/lib/lib.dom.d.ts:14354
```

## Methods

[](id:setHash)
### setHash
- **setHash**(`hash`): `void`

设置网址的片段部分
```
Defined in typings/url.d.ts:14
```

#### Parameters
| Name   | Type     |
| :----- | :------- |
| `hash` | `string` |

**Returns：**`void`


[](id:setHost)
### setHost
- **setHost**(`host`): `void`

设置网址的主机部分
```
Defined in typings/url.d.ts:22
```

#### Parameters

| Name   | Type     |
| :----- | :------- |
| `host` | `string` |

**Returns：**`void`

[](id:setHostname)
### setHostname
-  **setHostname**(`hostname`): `void`

设置网址的主机名部分
```
Defined in typings/url.d.ts:30
```

#### Parameters
| Name       | Type     |
| :--------- | :------- |
| `hostname` | `string` |

**Returns：**`void`

[](id:setHref)
### setHref
- **setHref**(`href`): `void`

设置序列化的网址
```
Defined in typings/url.d.ts:38
```

#### Parameters
| Name   | Type     |
| :----- | :------- |
| `href` | `string` |

**Returns：**`void`

[](id:setPassword)
### setPassword
- **setPassword**(`password`): `void`

设置网址的密码部分
```
Defined in typings/url.d.ts:50
```

#### Parameters

| Name       | Type     |
| :--------- | :------- |
| `password` | `string` |

**Returns：**`void`

[](id:setPathname)
### setPathname
- **setPathname**(`pathname`): `void`

设置网址的路径部分
```
Defined in typings/url.d.ts:58
```

#### Parameters
| Name       | Type     |
| :--------- | :------- |
| `pathname` | `string` |

**Returns**：`void`

[](id:setPort)
### setPort
- **setPort**(`port`): `void`

设置网址的端口部分
```
Defined in typings/url.d.ts:66
```


#### Parameters
| Name   | Type     |
| :----- | :------- |
| `port` | `string` |

**Returns：**`void`

[](id:setProtocol)
### setProtocol
- **setProtocol**(`protocol`): `void`

设置网址的协议部分
```
Defined in typings/url.d.ts:74
```

#### Parameters
| Name       | Type     |
| :--------- | :------- |
| `protocol` | `string` |

**Returns**：`void`

[](id:setSearch)
### setSearch
- **setSearch**(`search`): `void`

设置网址的序列化的查询部分
```
Defined in typings/url.d.ts:82
```

#### Parameters
| Name     | Type     |
| :------- | :------- |
| `search` | `string` |

**Returns：**`void`

[](id:setUsername)
### setUsername
- **setUsername**(`username`): `void`

设置网址的用户名部分
```
Defined in typings/url.d.ts:94
```

#### Parameters
| Name       | Type     |
| :--------- | :------- |
| `username` | `string` |

**Returns：**`void`

[](id:toJSON)
### toJSON
- **toJSON**(): `string`

```
Defined in node_modules/typescript/lib/lib.dom.d.ts:14355
```

**Returns**：`string`

- **toJSON**(): `string`

返回序列化的网址，当 URL 对象用 JSON.stringify() 序列化时，会自动调用此方法
```
Defined in typings/url.d.ts:98
```

**Returns：**`string`


[](id:toString)
### toString
- **toString**(): `string`

```
 Defined in node_modules/typescript/lib/lib.dom.d.ts:14346
```
**Returns**：`string`
- **toString**(): `string`

返回序列化的网址
```
Defined in typings/url.d.ts:102
```
**Returns：**`string`

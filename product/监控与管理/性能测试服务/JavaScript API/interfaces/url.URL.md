## Constructors（构造函数）

[](id:constructor)
### constructor
**new URL**(`url`, `base?`)

#### Parameters
| Name    | Type                                                         |
| :------ | :----------------------------------------------------------- |
| `url`   | `string`                                                     |
| `base?` | `string` \| [`URL`](https://cloud.tencent.com/document/product/1484/75838) |



## Properties（属性）

[](id:hash)
### hash
**hash**: `string`


[](id:host)
### host
**host**: `string`


[](id:contentType)
### hostname
**hostname**: `string`


[](id:href)
### href
**href**: `string`


[](id:origin)
### origin
`Readonly` **origin**: `string`


[](id:password)
### password
**password**: `string`


[](id:pathname)
### pathname
**pathname**: `string`


[](id:port)
### port
**port**: `string`


[](id:protocol)
### protocol
**protocol**: `string`


[](id:search)
### search
**search**: `string`


[](id:searchParams)
### searchParams
`Readonly` **searchParams**: [`URLSearchParams`](https://cloud.tencent.com/document/product/1484/75833#urlsearchparams)


[](id:username)
### username
**username**: `string`


## Methods

[](id:setHash)
### setHash
**setHash**(`hash`): `void`
设置网址的片段部分


#### Parameters
| Name   | Type     |
| :----- | :------- |
| `hash` | `string` |

**Returns：**`void`


[](id:setHost)
### setHost
**setHost**(`host`): `void`
设置网址的主机部分


#### Parameters
| Name   | Type     |
| :----- | :------- |
| `host` | `string` |

**Returns：**`void`

[](id:setHostname)
### setHostname
**setHostname**(`hostname`): `void`
设置网址的主机名部分

#### Parameters
| Name       | Type     |
| :--------- | :------- |
| `hostname` | `string` |

**Returns：**`void`

[](id:setHref)
### setHref
**setHref**(`href`): `void`
设置序列化的网址

#### Parameters
| Name   | Type     |
| :----- | :------- |
| `href` | `string` |

**Returns：**`void`

[](id:setPassword)
### setPassword
**setPassword**(`password`): `void`
设置网址的密码部分


#### Parameters
| Name       | Type     |
| :--------- | :------- |
| `password` | `string` |

**Returns：**`void`

[](id:setPathname)
### setPathname
**setPathname**(`pathname`): `void`
设置网址的路径部分


#### Parameters
| Name       | Type     |
| :--------- | :------- |
| `pathname` | `string` |

**Returns**：`void`

[](id:setPort)
### setPort
**setPort**(`port`): `void`
设置网址的端口部分



#### Parameters
| Name   | Type     |
| :----- | :------- |
| `port` | `string` |

**Returns：**`void`

[](id:setProtocol)
### setProtocol
**setProtocol**(`protocol`): `void`
设置网址的协议部分


#### Parameters
| Name       | Type     |
| :--------- | :------- |
| `protocol` | `string` |

**Returns**：`void`

[](id:setSearch)
### setSearch
**setSearch**(`search`): `void`
设置网址的序列化的查询部分


#### Parameters
| Name     | Type     |
| :------- | :------- |
| `search` | `string` |

**Returns：**`void`

[](id:setUsername)
### setUsername
**setUsername**(`username`): `void`
设置网址的用户名部分


#### Parameters
| Name       | Type     |
| :--------- | :------- |
| `username` | `string` |

**Returns：**`void`

[](id:toJSON)
### toJSON
- **toJSON**(): `string`
**Returns**：`string`
- **toJSON**(): `string`
返回序列化的网址，当 URL 对象用 JSON.stringify() 序列化时，会自动调用此方法

**Returns：**`string`


[](id:toString)
### toString
- **toString**(): `string`

**Returns**：`string`
- **toString**(): `string`
返回序列化的网址

**Returns：**`string`

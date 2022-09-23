## Constructors（构造函数）
[](id:contentType)
### constructor
**new URLSearchParams**(`init`)


#### Parameters
| Name   | Type     |
| :----- | :------- |
| `init` | `string` |

## Methods
[](id:append)
### append
**append**(`name`, `value`): `void`
追加指定的键/值对作为新的搜索参数。



#### Parameters
| Name    | Type     |
| :------ | :------- |
| `name`  | `string` |
| `value` | `string` |

**Returns：**`void`
- **append**(`key`, `value`): `void`
插入一个指定的键或值对作为新的搜索参数。


#### Parameters
| Name    | Type                 |
| :------ | :------------------- |
| `key`   | `string`             |
| `value` | `string` \| `number` |

**Returns：**`void`

[](id:delete)
### delete
**delete**(`name`): `void`
从所有搜索参数列表中删除给定的搜索参数及其关联值。


#### Parameters
| Name   | Type     |
| :----- | :------- |
| `name` | `string` |

**Returns**：`void`

- **delete**(`key`): `void`
从搜索参数列表里删除指定的搜索参数及其对应的值。

#### Parameters
| Name  | Type     |
| :---- | :------- |
| `key` | `string` |

**Returns：**`void`


[](id:entries)
### entries
**entries**(): `string`[][]

返回一个 iterator 可以遍历所有键/值对的对象。
**Returns：**`string`[][]

[](id:forEach)
### forEach
**forEach**(`callbackfn`, `thisArg?`): `void`
```
Defined in node_modules/typescript/lib/lib.dom.d.ts:14384
```

#### Parameters
| Name         | Type                                                         |
| :----------- | :----------------------------------------------------------- |
| `callbackfn` | (`value`: `string`, `key`: `string`, `parent`: [`URLSearchParams`](../modules/url.md#urlsearchparams)) => `void` |
| `thisArg?`   | `any`                                                        |

**Returns：**`void`
- **forEach**(`callback`): `void`
通过回调函数来遍历 URLSearchParams 实例对象上的键值对。



#### Parameters
| Name       | Type                                                         |
| :--------- | :----------------------------------------------------------- |
| `callback` | (`value`: `string`, `key`: `string`, `urlSearchParams`: [`URLSearchParams`](../modules/url.md#urlsearchparams)) => `void` |

**Returns：**`void`

[](id:get)
### get
**get**(`name`): ``null`` \| `string`
返回与给定搜索参数关联的第一个值。


#### Parameters
| Name   | Type     |
| :----- | :------- |
| `name` | `string` |

**Returns**：``null`` \| `string`
- **get**(`key`): ``null`` \| `string`
获取指定搜索参数的第一个值。


#### Parameters
| Name  | Type     |
| :---- | :------- |
| `key` | `string` |

**Returns：**``null`` \| `string`

[](id:getAll)
### getAll
**getAll**(`name`): `string`[]
返回与给定搜索参数关联的所有值。


#### Parameters
| Name   | Type     |
| :----- | :------- |
| `name` | `string` |

**Returns：**`string`[]
- **getAll**(`key`): `string`
获取指定搜索参数的所有值，返回是一个数组。


#### Parameters
| Name  | Type     |
| :---- | :------- |
| `key` | `string` |

**Returns：**`string`

[](id:has)
### has
**has**(`name`): `boolean`
返回一个 boolean 值，指示是否存在此类搜索参数。

#### Parameters
| Name   | Type     |
| :----- | :------- |
| `name` | `string` |

**Returns：**`boolean`
- **has**(`key`): `boolean`
返回 Boolean 判断是否存在此搜索参数。


#### Parameters
| Name  | Type     |
| :---- | :------- |
| `key` | `string` |

**Returns：**`boolean`

[](id:keys)
### keys
**keys**(): `string`[]
返回 iterator 此对象包含了键/值对的所有键名。

**Returns：**`string`[]

[](id:set)
### set
**set**(`name`, `value`): `void`
将与给定搜索参数关联的值设置为给定值。如果有多个值，请删除其他值。
```
Defined in node_modules/typescript/lib/lib.dom.d.ts:14380
```

#### Parameters
| Name    | Type     |
| :------ | :------- |
| `name`  | `string` |
| `value` | `string` |

**Returns：**`void`
- **set**(`key`, `value`): `void`
设置一个搜索参数的新值，假如原来有多个值将删除其他所有的值。


#### Parameters
| Name    | Type                 |
| :------ | :------------------- |
| `key`   | `string`             |
| `value` | `string` \| `number` |

**Returns：**`void`

[](id:sort)
### sort
**sort**(): `void`

**Returns：**`void`

[](id:toString)
### toString
**toString**(): `string`
返回一个字符串，该字符串包含适合在URL中使用的查询字符串（不包括问号）

**Returns：**`string`
- **toString**(): `string`
返回搜索参数组成的字符串，可直接使用在 URL 上。

**Returns：**`string`

[](id:values)
### values
**values**(): `string`[]
返回 iterator 此对象包含了键或值对的所有值。

**Returns：**`string`[]

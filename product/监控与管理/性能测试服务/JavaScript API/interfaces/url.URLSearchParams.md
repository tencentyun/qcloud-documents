# Interface: URLSearchParams

[url](../modules/url.md).URLSearchParams

## Table of contents

### Constructors

- [constructor](url.URLSearchParams.md#constructor)

### Methods

- [append](#append)
- [delete](#delete)
- [entries](#entries)
- [forEach](#foreach)
- [get](#get)
- [getAll](#getall)
- [has](#has)
- [keys](#keys)
- [set](#set)
- [sort](#sort)
- [toString](#tostring)
- [values](#values)

## Constructors

<span id="contentType"></span>

### constructor

• **new URLSearchParams**(`init`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `init` | `string` |

#### Defined in

typings/url.d.ts:106



## Methods

<span id="append"></span>

### append

▸ **append**(`name`, `value`): `void`

Appends a specified key/value pair as a new search parameter.

#### Parameters

| Name | Type |
| :------ | :------ |
| `name` | `string` |
| `value` | `string` |

#### Returns

`void`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14370

▸ **append**(`key`, `value`): `void`

插入一个指定的键/值对作为新的搜索参数

#### Parameters

| Name | Type |
| :------ | :------ |
| `key` | `string` |
| `value` | `string` \| `number` |

#### Returns

`void`

#### Defined in

typings/url.d.ts:111

___

<span id="delete"></span>

### delete

▸ **delete**(`name`): `void`

Deletes the given search parameter, and its associated value, from the list of all search parameters.

#### Parameters

| Name | Type |
| :------ | :------ |
| `name` | `string` |

#### Returns

`void`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14372

▸ **delete**(`key`): `void`

从搜索参数列表里删除指定的搜索参数及其对应的值

#### Parameters

| Name | Type |
| :------ | :------ |
| `key` | `string` |

#### Returns

`void`

#### Defined in

typings/url.d.ts:115

___

<span id="entries"></span>

### entries

▸ **entries**(): `string`[][]

返回一个 iterator 可以遍历所有键/值对的对象

#### Returns

`string`[][]

#### Defined in

typings/url.d.ts:119

___

<span id="forEach"></span>

### forEach

▸ **forEach**(`callbackfn`, `thisArg?`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `callbackfn` | (`value`: `string`, `key`: `string`, `parent`: [`URLSearchParams`](../modules/url.md#urlsearchparams)) => `void` |
| `thisArg?` | `any` |

#### Returns

`void`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14384

▸ **forEach**(`callback`): `void`

通过回调函数来遍历 URLSearchParams 实例对象上的键值对

#### Parameters

| Name | Type |
| :------ | :------ |
| `callback` | (`value`: `string`, `key`: `string`, `urlSearchParams`: [`URLSearchParams`](../modules/url.md#urlsearchparams)) => `void` |

#### Returns

`void`

#### Defined in

typings/url.d.ts:123

___

<span id="get"></span>

### get

▸ **get**(`name`): ``null`` \| `string`

Returns the first value associated to the given search parameter.

#### Parameters

| Name | Type |
| :------ | :------ |
| `name` | `string` |

#### Returns

``null`` \| `string`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14374

▸ **get**(`key`): ``null`` \| `string`

获取指定搜索参数的第一个值

#### Parameters

| Name | Type |
| :------ | :------ |
| `key` | `string` |

#### Returns

``null`` \| `string`

#### Defined in

typings/url.d.ts:127

___

<span id="getAll"></span>

### getAll

▸ **getAll**(`name`): `string`[]

Returns all the values association with a given search parameter.

#### Parameters

| Name | Type |
| :------ | :------ |
| `name` | `string` |

#### Returns

`string`[]

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14376

▸ **getAll**(`key`): `string`

获取指定搜索参数的所有值，返回是一个数组

#### Parameters

| Name | Type |
| :------ | :------ |
| `key` | `string` |

#### Returns

`string`

#### Defined in

typings/url.d.ts:131

___

<span id="has"></span>

### has

▸ **has**(`name`): `boolean`

Returns a Boolean indicating if such a search parameter exists.

#### Parameters

| Name | Type |
| :------ | :------ |
| `name` | `string` |

#### Returns

`boolean`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14378

▸ **has**(`key`): `boolean`

返回 Boolean 判断是否存在此搜索参数

#### Parameters

| Name | Type |
| :------ | :------ |
| `key` | `string` |

#### Returns

`boolean`

#### Defined in

typings/url.d.ts:135

___

<span id="keys"></span>

### keys

▸ **keys**(): `string`[]

返回 iterator 此对象包含了键/值对的所有键名

#### Returns

`string`[]

#### Defined in

typings/url.d.ts:139

___

<span id="set"></span>

### set

▸ **set**(`name`, `value`): `void`

Sets the value associated to a given search parameter to the given value. If there were several values, delete the others.

#### Parameters

| Name | Type |
| :------ | :------ |
| `name` | `string` |
| `value` | `string` |

#### Returns

`void`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14380

▸ **set**(`key`, `value`): `void`

设置一个搜索参数的新值，假如原来有多个值将删除其他所有的值

#### Parameters

| Name | Type |
| :------ | :------ |
| `key` | `string` |
| `value` | `string` \| `number` |

#### Returns

`void`

#### Defined in

typings/url.d.ts:143

___

<span id="sort"></span>

### sort

▸ **sort**(): `void`

#### Returns

`void`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14381

___

<span id="toString"></span>

### toString

▸ **toString**(): `string`

Returns a string containing a query string suitable for use in a URL. Does not include the question mark.

#### Returns

`string`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14383

▸ **toString**(): `string`

返回搜索参数组成的字符串，可直接使用在 URL 上

#### Returns

`string`

#### Defined in

typings/url.d.ts:147

___

<span id="values"></span>

### values

▸ **values**(): `string`[]

返回 iterator 此对象包含了键/值对的所有值

#### Returns

`string`[]

#### Defined in

typings/url.d.ts:151

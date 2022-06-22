# Interface: URL

[url](../modules/url.md).URL

URL 接口表示提供用于创建对象URL的静态方法的对象。

## Table of contents

### Constructors

- [constructor](#constructor)

### Properties

- [hash](#hash)
- [host](#host)
- [hostname](#hostname)
- [href](#href)
- [origin](#origin)
- [password](#password)
- [pathname](#pathname)
- [port](#port)
- [protocol](#protocol)
- [search](#search)
- [searchParams](#searchparams)
- [username](#username)

### Methods

- [setHash](#sethash)
- [setHost](#sethost)
- [setHostname](#sethostname)
- [setHref](#sethref)
- [setPassword](#setpassword)
- [setPathname](#setpathname)
- [setPort](#setport)
- [setProtocol](#setprotocol)
- [setSearch](#setsearch)
- [setUsername](#setusername)
- [toJSON](#tojson)
- [toString](#tostring)

## Constructors

<span id="constructor"></span>

### constructor

• **new URL**(`url`, `base?`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `url` | `string` |
| `base?` | `string` \| [`URL`](../modules/url.md#url) |

#### Defined in

typings/url.d.ts:5



## Properties

<span id="hash"></span>

### hash

• **hash**: `string`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14342

___

<span id="host"></span>

### host

• **host**: `string`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14343

___

<span id="contentType"></span>

### hostname

• **hostname**: `string`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14344

___

<span id="href"></span>

### href

• **href**: `string`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14345

___

<span id="origin"></span>

### origin

• `Readonly` **origin**: `string`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14347

___

<span id="password"></span>

### password

• **password**: `string`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14348

___

<span id="pathname"></span>

### pathname

• **pathname**: `string`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14349

___

<span id="port"></span>

### port

• **port**: `string`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14350

___

<span id="protocol"></span>

### protocol

• **protocol**: `string`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14351

___

<span id="search"></span>

### search

• **search**: `string`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14352

___

<span id="searchParams"></span>

### searchParams

• `Readonly` **searchParams**: [`URLSearchParams`](../modules/url.md#urlsearchparams)

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14353

___

<span id="username"></span>

### username

• **username**: `string`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14354

## Methods

<span id="setHash"></span>

### setHash

▸ **setHash**(`hash`): `void`

设置网址的片段部分

#### Parameters

| Name | Type |
| :------ | :------ |
| `hash` | `string` |

#### Returns

`void`

#### Defined in

typings/url.d.ts:14

___

<span id="setHost"></span>

### setHost

▸ **setHost**(`host`): `void`

设置网址的主机部分

#### Parameters

| Name | Type |
| :------ | :------ |
| `host` | `string` |

#### Returns

`void`

#### Defined in

typings/url.d.ts:22

___

<span id="setHostname"></span>

### setHostname

▸ **setHostname**(`hostname`): `void`

设置网址的主机名部分

#### Parameters

| Name | Type |
| :------ | :------ |
| `hostname` | `string` |

#### Returns

`void`

#### Defined in

typings/url.d.ts:30

___

<span id="setHref"></span>

### setHref

▸ **setHref**(`href`): `void`

设置序列化的网址

#### Parameters

| Name | Type |
| :------ | :------ |
| `href` | `string` |

#### Returns

`void`

#### Defined in

typings/url.d.ts:38

___

<span id="setPassword"></span>

### setPassword

▸ **setPassword**(`password`): `void`

设置网址的密码部分

#### Parameters

| Name | Type |
| :------ | :------ |
| `password` | `string` |

#### Returns

`void`

#### Defined in

typings/url.d.ts:50

___

<span id="setPathname"></span>

### setPathname

▸ **setPathname**(`pathname`): `void`

设置网址的路径部分

#### Parameters

| Name | Type |
| :------ | :------ |
| `pathname` | `string` |

#### Returns

`void`

#### Defined in

typings/url.d.ts:58

___

<span id="setPort"></span>

### setPort

▸ **setPort**(`port`): `void`

设置网址的端口部分

#### Parameters

| Name | Type |
| :------ | :------ |
| `port` | `string` |

#### Returns

`void`

#### Defined in

typings/url.d.ts:66

___

<span id="setProtocol"></span>

### setProtocol

▸ **setProtocol**(`protocol`): `void`

设置网址的协议部分

#### Parameters

| Name | Type |
| :------ | :------ |
| `protocol` | `string` |

#### Returns

`void`

#### Defined in

typings/url.d.ts:74

___

<span id="setSearch"></span>

### setSearch

▸ **setSearch**(`search`): `void`

设置网址的序列化的查询部分

#### Parameters

| Name | Type |
| :------ | :------ |
| `search` | `string` |

#### Returns

`void`

#### Defined in

typings/url.d.ts:82

___

<span id="setUsername"></span>

### setUsername

▸ **setUsername**(`username`): `void`

设置网址的用户名部分

#### Parameters

| Name | Type |
| :------ | :------ |
| `username` | `string` |

#### Returns

`void`

#### Defined in

typings/url.d.ts:94

___

<span id="toJSON"></span>

### toJSON

▸ **toJSON**(): `string`

#### Returns

`string`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14355

▸ **toJSON**(): `string`

返回序列化的网址，当 URL 对象用 JSON.stringify() 序列化时，会自动调用此方法

#### Returns

`string`

#### Defined in

typings/url.d.ts:98

___

<span id="toString"></span>

### toString

▸ **toString**(): `string`

#### Returns

`string`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:14346

▸ **toString**(): `string`

返回序列化的网址

#### Returns

`string`

#### Defined in

typings/url.d.ts:102

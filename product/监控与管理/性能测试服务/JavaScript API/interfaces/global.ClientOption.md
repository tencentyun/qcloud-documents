# Interface: ClientOption

[global](../modules/global.md).ClientOption

## Hierarchy

- **`ClientOption`**

  ↳ [`Option`](protohub.Option.md)

  ↳ [`Option`](trpc_client.Option.md)

## Table of contents

### Properties

- [aliasName](#aliasname)
- [env](#env)
- [metaData](#metadata)
- [namespace](#namespace)
- [protocol](#protocol)
- [sendOnly](#sendonly)
- [serializationType](#serializationtype)
- [serviceName](#servicename)
- [target](#target)
- [timeoutMs](#timeoutms)

## Properties

<span id="aliasName"></span>

### aliasName

• `Optional` **aliasName**: `string`

trpc 特有插件别名

#### Defined in

typings/global.d.ts:73

___

<span id="env"></span>

### env

• `Optional` **env**: `string`

123 环境名，例如 formal、pre、test

#### Defined in

typings/global.d.ts:65

___

<span id="metaData"></span>

### metaData

• `Optional` **metaData**: `Record`<`string`, `string` \| `ArrayBuffer`\>

请求头信息

#### Defined in

typings/global.d.ts:89

___

<span id="namespace"></span>

### namespace

• `Optional` **namespace**: `string`

环境类型，例如 Production、Development

#### Defined in

typings/global.d.ts:69

___

<span id="protocol"></span>

### protocol

• `Optional` **protocol**: `string`

协议

#### Defined in

typings/global.d.ts:61

___

<span id="sendOnly"></span>

### sendOnly

• `Optional` **sendOnly**: `boolean`

trpc 只发不收选项

#### Defined in

typings/global.d.ts:97

___

<span id="serializationType"></span>

### serializationType

• `Optional` **serializationType**: ``0`` \| ``2``

序列化类型。0-pb，2-json

#### Defined in

typings/global.d.ts:93

___

<span id="serviceName"></span>

### serviceName

• `Optional` **serviceName**: `string`

被调服务名，用于北极星寻址

#### Defined in

typings/global.d.ts:85

___

### target

• `Optional` **target**: `string`

目标

#### Defined in

typings/global.d.ts:81

___

<span id="timeoutMs"></span>

### timeoutMs

• `Optional` **timeoutMs**: `number`

请求超时，单位毫秒

#### Defined in

typings/global.d.ts:77

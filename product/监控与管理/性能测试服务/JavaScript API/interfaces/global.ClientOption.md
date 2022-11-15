## Properties（属性）
[](id:aliasName)
### aliasName
`Optional` **aliasName**: `string`
trpc 特有插件别名


[](id:env)
### env
`Optional` **env**: `string`
123 环境名，例如 formal、pre、test


[](id:metaData)
### metaData
`Optional` **metaData**: `Record`<`string`, `string` \| `ArrayBuffer`\>
请求头信息


[](id:namespace)
### namespace
`Optional` **namespace**: `string`
环境类型，例如 Production、Development

[](id:protocol)
### protocol
`Optional` **protocol**: `string`
协议


[](id:sendOnly)
### sendOnly
`Optional` **sendOnly**: `boolean`
trpc 只发不收选项


[](id:serializationType)
### serializationType
`Optional` **serializationType**: ``0`` \| ``2``
序列化类型。0：pb，2：json


[](id:serviceName)
### serviceName
`Optional` **serviceName**: `string`
被调服务名，用于北极星寻址



### target
`Optional` **target**: `string`
目标


[](id:timeoutMs)
### timeoutMs
`Optional` **timeoutMs**: `number`
请求超时，单位毫秒


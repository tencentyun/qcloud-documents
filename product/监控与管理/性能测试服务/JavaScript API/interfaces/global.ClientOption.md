## Properties（属性）
[](id:aliasName)
### aliasName
- `Optional` **aliasName**: `string`

trpc 特有插件别名
```plaintext
Defined in typings/global.d.ts:73
```


[](id:env)
### env
- `Optional` **env**: `string`

123 环境名，例如 formal、pre、test
```plaintext
Defined in typings/global.d.ts:6
```


<span id="metaData"></span>

### metaData
- `Optional` **metaData**: `Record`<`string`, `string` \| `ArrayBuffer`\>

请求头信息
```plaintext
Defined in typings/global.d.ts:89
```

[](id:namespace)
### namespace
- `Optional` **namespace**: `string`

环境类型，例如 Production、Development
```plaintext
Defined in typings/global.d.ts:69
```

[](id:protocol)
### protocol
- `Optional` **protocol**: `string`

协议
```plaintext
Defined in typings/global.d.ts:61
```

[](id:sendOnly)
### sendOnly
- `Optional` **sendOnly**: `boolean`

trpc 只发不收选项
```plaintext
Defined in typings/global.d.ts:97
```

[](id:serializationType)
### serializationType
- `Optional` **serializationType**: ``0`` \| ``2``

序列化类型。0：pb，2：json
```plaintext
Defined in typings/global.d.ts:93
```

[](id:serviceName)
### serviceName
- `Optional` **serviceName**: `string`

被调服务名，用于北极星寻址
```plaintext
Defined in typings/global.d.ts:85
```


### target
- `Optional` **target**: `string`

目标
```plaintext
Defined in typings/global.d.ts:81
```

[](id:timeoutMs)
### timeoutMs
- `Optional` **timeoutMs**: `number`

请求超时，单位毫秒
```plaintext
Defined in typings/global.d.ts:77
```

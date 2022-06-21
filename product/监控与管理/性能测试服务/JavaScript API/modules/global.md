## Table of contents

### Interfaces

- [BasicAuth](../interfaces/global.BasicAuth.md)
- [Certificate](../interfaces/global.Certificate.md)
- [ClientOption](../interfaces/global.ClientOption.md)
- [HTTP](../interfaces/global.HTTP.md)
- [Option](../interfaces/global.Option.md)
- [TLSConfig](../interfaces/global.TLSConfig.md)
- [TRPC](../interfaces/global.TRPC.md)
- [WS](../interfaces/global.WS.md)

### Variables

- [Option](#option)

### Functions

- [int64](#int64)
- [open](#open)
- [uint64](#uint64)

## Variables

<span id="option"></span>

### Option

• **Option**: `Object`

#### Defined in

node_modules/typescript/lib/lib.dom.d.ts:17667

## Functions

<span id="int64"></span>

### int64

▸ **int64**(`v`): `object`

int64 类型。

```js
export default function () {
    let a = {
        k: int64("9223372036854775807")
    }
    console.log(JSON.stringify(a)); // {"k":"9223372036854775807"}
    console.log(a.k.toString()); // 9223372036854775807
}
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `v` | `string` | int64 类型数据的字符串格式 |

#### Returns

`object`

#### Defined in

typings/global.d.ts:34

___

<span id="open"></span>

### open

▸ **open**(`url?`, `target?`, `features?`): `WindowProxy` \| ``null``

打开文件。

```js
export default function () {
    let data = open('data/test.json');
    console.log(data); // {"a":"b"}
    data = open('data/test.json', 'b');
    console.log(data); // [object ArrayBuffer]
};
```

#### Parameters

| Name | Type |
| :------ | :------ |
| `url?` | `string` \| [`URL`](url.md#url) |
| `target?` | `string` |
| `features?` | `string` |

#### Returns

`WindowProxy` \| ``null``

文件数据

#### Defined in

```
node_modules/typescript/lib/lib.dom.d.ts:17754
```

▸ **open**(`filePath`, `mode?`): `string` \| `ArrayBuffer`

打开文件。

```js
export default function () {
    let data = open('data/test.json');
    console.log(data); // {"a":"b"}
    data = open('data/test.json', 'b');
    console.log(data); // [object ArrayBuffer]
};
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `filePath` | `string` | 文件相对路径 |
| `mode?` | ``""`` \| ``"b"`` | 可选。为空返回字符串，为 'b' 返回 ArrayBuffer |

#### Returns

`string` \| `ArrayBuffer`

文件数据

#### Defined in

typings/global.d.ts:17



___

<span id="uint64"></span>

### uint64

▸ **uint64**(`v`): `object`

uint64 类型。

```js
export default function () {
    let a = {
        k: uint64("18446744073709551615")
    }
    console.log(JSON.stringify(a)); // {"k":"18446744073709551615"}
    console.log(a.k.toString()); // 18446744073709551615
}
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `v` | `string` | uint64 类型数据的字符串格式 |

#### Returns

`object`

#### Defined in

typings/global.d.ts:51



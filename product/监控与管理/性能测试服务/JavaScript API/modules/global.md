## 目录

### Interfaces（接口）
- [BasicAuth](https://cloud.tencent.com/document/product/1484/75806)
- [Certificate](https://cloud.tencent.com/document/product/1484/75807)
- [ClientOption](https://cloud.tencent.com/document/product/1484/75810)
- [HTTP](https://cloud.tencent.com/document/product/1484/75811)
- [Option](https://cloud.tencent.com/document/product/1484/75812)
- [TLSConfig](https://cloud.tencent.com/document/product/1484/75813)
- [TRPC](https://cloud.tencent.com/document/product/1484/75814)
- [WS](https://cloud.tencent.com/document/product/1484/75815)

### Variables（变量）
- [Option](#option)

### Functions（函数）
- [int64](#int64)
- [open](#open)
- [uint64](#uint64)

## Variables
[](id:option)
### Option
- **Option**: `Object`

```
Defined innode_modules/typescript/lib/lib.dom.d.ts:17667
```

## Functions

[](id:int64)
### int64
- **int64**(`v`): `object`

int64 类型。
```
Defined in typings/global.d.ts:34
```
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

| Name | Type     | Description                |
| :--- | :------- | :------------------------- |
| `v`  | `string` | int64 类型数据的字符串格式 |

**Returns**：`object`

[](id:open)
### open
- **open**(`url?`, `target?`, `features?`): `WindowProxy` \| ``null``

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
| Name        | Type                                                         |
| :---------- | :----------------------------------------------------------- |
| `url?`      | `string` \| [`URL`](https://cloud.tencent.com/document/product/1484/75838l) |
| `target?`   | `string`                                                     |
| `features?` | `string`                                                     |

**Returns：**`WindowProxy` \| ``null``
文件数据
```
Defined in node_modules/typescript/lib/lib.dom.d.ts:17754
```
- **open**(`filePath`, `mode?`): `string` \| `ArrayBuffer`
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
| Name       | Type              | Description                                   |
| :--------- | :---------------- | :-------------------------------------------- |
| `filePath` | `string`          | 文件相对路径                                  |
| `mode?`    | ``""`` \| ``"b"`` | 可选。为空返回字符串，为 'b' 返回 ArrayBuffer |

#### Returns
`string` \| `ArrayBuffer`
文件数据。
```
Defined in typings/global.d.ts:17
```

[](id:uint64)
### uint64
- **uint64**(`v`): `object`

uint64 类型。
```
Defined in typings/global.d.ts:51
```
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
| Name | Type     | Description                 |
| :--- | :------- | :-------------------------- |
| `v`  | `string` | uint64 类型数据的字符串格式 |

**Returns：**`object`

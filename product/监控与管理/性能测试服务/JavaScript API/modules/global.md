
## Interfaces（接口）
- [BasicAuth](https://cloud.tencent.com/document/product/1484/75806)
- [Certificate](https://cloud.tencent.com/document/product/1484/75807)
- [ClientOption](https://cloud.tencent.com/document/product/1484/75810)
- [HTTP](https://cloud.tencent.com/document/product/1484/75811)
- [Option](https://cloud.tencent.com/document/product/1484/75812)
- [TLSConfig](https://cloud.tencent.com/document/product/1484/75813)
- [TRPC](https://cloud.tencent.com/document/product/1484/75814)
- [WS](https://cloud.tencent.com/document/product/1484/75815)


## Variables
[](id:option)
### Option
**Option**: `{}`
#### Type declaration

## Functions

### int64
- int64(v: *string*): *object*
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
-  v: *string*
int64 类型数据的字符串格式

#### Returns *object*

### open
- open(url?: *string* | [URL](https://cloud.tencent.com/document/product/1484/75825), target?: *string*, features?: *string*): *WindowProxy* | *null*
- open(filePath: *string*, mode?: *""* | *"b"*): *string* | *ArrayBuffer*

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
 -  Optional url: *string* | [URL](https://cloud.tencent.com/document/product/1484/75825#URL-1)
 -  Optional target: *string*
 -  Optional features: *string*

#### Returns *WindowProxy* | *null*
文件数据

### uint64
- uint64(v: *string*): *object*
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
- v: *string*
uint64 类型数据的字符串格式

#### Returns *object*

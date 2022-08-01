## 目录

### Variables（变量）
- [default](#default)

## Variables（变量）

[](id:default)

### Const default

default: { load: *any*; marshal: *any*; unmarshal: *any* }

Defined in typings/protobuf.d.ts:5

#### Type declaration

- ##### load:function 

  - load(importPaths: *string*[], ...filenames: *string*[]): *void*


```
  Defined in typings/protobuf.d.ts:22
```

加载 pb 文件。

```js
  import protobuf from 'pts/protobuf';
    
   // 加载协议文件根目录中的 demo.proto
   protobuf.load([], 'demo.proto');
    
  // 加载中协议文件 dirName 目录中的 demo.proto
   protobuf.load(['dirName'], 'demo.proto');
 ```
		
#### Parameters

- ##### importPaths: *string*[]

      用于搜索在 proto 源文件的 import 语句中引用的依赖项的路径。如果没有提供导入路径，则当前目录被假定为唯一的导入路径。

 - ##### Rest ...filenames: *string*[]

pb 文件名列表, 支持单个文件名调用

#### Returns *void*

- ##### marshal:function

  - marshal(message: *string*, value: *any*, filename?: *string*): *ArrayBuffer*

```
Defined in typings/protobuf.d.ts:50
```

    pb 序列化。

    ```js
    import protobuf from 'pts/protobuf';
    
    // 加载协议文件根目录中的 demo.proto
    protobuf.load([], 'demo.proto');
    
    // 加载中协议文件 dirName 目录中的 demo.proto
    // protobuf.load(['dirName'], 'demo.proto');
    
    export default function () {
        let data = protobuf.marshal('trpc.wtp.demo.stSayHelloReq', {"msg": "pts"});
        console.log(data); // [object ArrayBuffer]
    
        let value = protobuf.unmarshal('trpc.wtp.demo.stSayHelloReq', data);
        console.log(JSON.stringify(value)); // {"msg":"pts"}
    };
    ```

#### Parameters

 - ##### message: *string*

      结构体名

 - ##### value: *any*

      json化的请求体

 - ##### Optional filename: *string*

      文件名，可选

 #### Returns *ArrayBuffer*

    响应对象

- ##### unmarshal:function

- unmarshal(message: *string*, data: *ArrayBuffer*, filename?: *string*): *any*

- Defined in typings/protobuf.d.ts:78

 pb 反序列化。

 ```js
    import protobuf from 'pts/protobuf';
    
    // 加载协议文件根目录中的 demo.proto
    protobuf.load([], 'demo.proto');
    
    // 加载中协议文件 dirName 目录中的 demo.proto
    // protobuf.load(['dirName'], 'demo.proto');
    
    export default function () {
        let data = protobuf.marshal('trpc.wtp.demo.stSayHelloReq', {"msg": "pts"});
        console.log(data); // [object ArrayBuffer]
    
        let value = protobuf.unmarshal('trpc.wtp.demo.stSayHelloReq', data);
        console.log(JSON.stringify(value)); // {"msg":"pts"}
    };
  ```

#### Parameters

 - ##### message: *string*

      结构体名

 
  - ##### data: *ArrayBuffer*

 二进制请求体

- ##### Optional filename: *string*

  文件名，可选

 #### Returns *any*

  响应对象


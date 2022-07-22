 ## Table of contents（目录）

### Interfaces（接口）
- [BatchOption](https://cloud.tencent.com/document/product/1484/75820)
- [BatchResponse](https://cloud.tencent.com/document/product/1484/75821)
- [File](https://cloud.tencent.com/document/product/1484/75822)
- [Request](https://cloud.tencent.com/document/product/1484/75823)
- [Response](https://cloud.tencent.com/document/product/1484/75819)

### Variables（变量）
- [default](#default)

## Variables（变量）

[](id:default)



### Const default

default: { Client: (new () => { close: *any*; connect: *any*; invoke: *any*; load: *any* }) }

```
Defined in typings/grpc.d.ts:69
```


#### Type declaration

- ##### Client: (new () => { close: *any*; connect: *any*; invoke: *any*; load: *any* })

  - - new (): { close: *any*; connect: *any*; invoke: *any*; load: *any* }

 #### Returns { close: *any*; connect: *any*; invoke: *any*; load: *any* }

- ##### close:function

   - close(): *void*
 
 ```
 Defined in typings/grpc.d.ts:100
```
关闭连接。

#### Returns *void*

- ##### connect:function

  - connect(target: *string*, option?: [DialOption](https://cloud.tencent.com/document/product/1484/75816)): *void*

 ```
   Defined in typings/grpc.d.ts:95
```
建立连接。

#### Parameters

  - ##### target: *string*

     目标地址

   - ##### Optional option: [DialOption](https://cloud.tencent.com/document/product/1484/75816)

      可选。 DialOption 对象。

  #### Returns *void*

 - ##### invoke:function

 - invoke(method: *string*, request: *any*, option?: [InvokeOption](https://cloud.tencent.com/document/product/1484/75818)): [Response](https://cloud.tencent.com/document/product/1484/75819)

```
Defined in typings/grpc.d.ts:132
```

执行 method 方法。

```
   import grpc from 'pts/grpc';
          
   // 加载协议文件根目录中的 addsvc.proto
   client.load([], 'addsvc.proto');
          
    // 加载中协议文件 dirName 目录中的 addsvc.proto
    // client.load(['dirName'], 'addsvc.proto');
          
    export default () => {
    client.connect('grpcb.in:9000', {insecure: true});
          
    const rsp = client.invoke('addsvc.Add/Sum', {
          a: 1,
          b: 2,
         });
    console.log(rsp.data.v); // 3
          
    client.close();
       };
```

#### Parameters

- ##### method: *string*

       完整 path 路径 /a.b.c.d/e

 - ##### request: *any*

    业务请求内容

 - ##### Optional option: [InvokeOption](https://cloud.tencent.com/document/product/1484/75818)

    可选。InvokeOption 对象。

  #### Returns [Response](https://cloud.tencent.com/document/product/1484/75819)

   响应对象

 - ##### load:function
      - load(importPaths: *string*[], ...filenames: *string*[]): *void*
      
<dx-codeblock>
::: html 
Defined in typings/grpc.d.ts:87
:::
</dx-codeblock>

加载 pb 文件。

 ```
  import grpc from 'pts/grpc';
          
    // 加载协议文件根目录中的 addsvc.proto
     client.load([], 'addsvc.proto');
         
    // 加载中协议文件 dirName 目录中的 addsvc.proto
       client.load(['dirName'], 'addsvc.proto');
 ```
#### Parameters

 - ##### importPaths: *string*[]

  用于搜索在 proto 源文件的 import 语句中引用的依赖项的路径。如果没有提供导入路径，则当前目录被假定为唯一的导入路径。

 - ##### Rest ...filenames: *string*[]

  pb 文件名列表, 支持单个文件名调用。

  #### Returns *void*

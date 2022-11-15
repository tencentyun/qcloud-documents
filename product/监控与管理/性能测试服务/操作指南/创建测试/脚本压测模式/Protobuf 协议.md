本文将介绍 Protobuf 序列化协议的使用方法。

 

## 协议上传

![](https://qcloudimg.tencent-cloud.cn/raw/dfd5b3c74a2462cbbf14159a62d47647.png)

> ? 多协议文件请参见 [使用协议文件](https://cloud.tencent.com/document/product/1484/74048)。



## 脚本编写

借助您上传的 proto 文件，您可对脚本中的对象做序列化/反序列化。

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


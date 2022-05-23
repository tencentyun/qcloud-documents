本文将介绍 Protobuf 序列化协议的使用方法。

 

## 协议上传

![](https://qcloudimg.tencent-cloud.cn/raw/dfd5b3c74a2462cbbf14159a62d47647.png)

> ? 多协议文件参考 [使用协议文件](https://cloud.tencent.com/document/product/1484/74048)。



## 脚本编写

借助您上传的 proto 文件，您可对脚本中的对象做序列化/反序列化。

```js
import protobuf from 'pts/protobuf';

protobuf.load("demo.proto");

export default function () {
    let value = {
        "msg": "pts"
    };
    let bytes = protobuf.marshal("trpc.wtp.demo.stSayHelloReq", value);
    console.log(bytes); // [object ArrayBuffer]
};
```


本文将介绍 gRPC 协议请求的编排方法。



## 基本用法

使用 [pts/grpc API](https://cloud.tencent.com/document/product/1484/75805) 提供的接口，您可以创建 gRPC client，发送 gRPC 请求。

### 协议上传

将您定义好的 proto 文件，通过**文件管理 > 协议文件**上传。
>?关于 PTS 支持的协议类型及使用方法，请参考 [使用协议文件](https://cloud.tencent.com/document/product/1484/74048)。

### 脚本编写

先创建一个 gRPC client，然后您可以使用 client 提供的以下方法编写您的逻辑： 
- `load`：加载并解析您上传的 proto 文件。
- `connect`：与 gRPC 服务器建立连接。
- `invoke`：发起 RPC 调用并获得响应。
- `close`：关闭连接。

 

**Proto 文件及场景脚本的示例如下：**

```javascript
// based on https://github.com/go-kit/kit/blob/master/examples/addsvc/pb/addsvc.proto

syntax = "proto3";

package addsvc;

// The Add service definition.
service Add {
  // Sums two integers.
  rpc Sum (SumRequest) returns (SumReply) {}
}

// The sum request contains two parameters.
message SumRequest {
  int64 a = 1;
  int64 b = 2;
}

// The sum response contains the result of the calculation.
message SumReply {
  int64 v = 1;
  string err = 2;
}
```

**场景脚本：**

```javascript
// GRPC API
import grpc from 'pts/grpc';

const client = new grpc.Client();

// 加载协议文件根目录中的 addsvc.proto
client.load([], 'addsvc.proto');

export default () => {
  client.connect([], 'grpcb.in:9000', { insecure: true });

  const rsp = client.invoke('addsvc.Add/Sum', {
    a: 1,
    b: 2,
  });
  console.log(rsp.data.v); // 3

  client.close();
};
```

### 文件依赖

在压测场景里，您可上传以下几种类型的文件，提供压测执行时的状态数据：

- **参数文件**：以 csv 文件的形式，动态提供测试数据。场景被每个并发用户（VU）执行时，会获取参数文件里的每行数据，作为测试数据的值，供脚本里的变量引用。具体使用方法请参考 [使用参数文件](https://cloud.tencent.com/document/product/1484/74046)。
- **请求文件**：构建您的请求所需的文件，如需要上传的文件。具体使用方法请参考 [使用请求文件](https://cloud.tencent.com/document/product/1484/74047)。
- **协议文件**：请求序列化所需要用到的文件。具体使用方法请参考 [使用协议文件](https://cloud.tencent.com/document/product/1484/74048)。

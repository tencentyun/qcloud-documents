
- gRPC 是一个高性能、开源通用的 RPC 框架，也是一个语言中立、平台中立、开源的远程过程调用（RPC）系统，面向移动和 HTTP/2 设计。当前支持的语言版本有 C， C++， C#，Node.js，Python，Ruby，Objective-C，PHP，Java 和 Go。
- 在 gRPC 里客户端应用可以像调用本地对象一样直接调用另一台不同的机器上服务端应用，gRPC 基于定义服务的理念，指定其能够被远程调用的方法（包含参数和返回类型）。在服务端实现这个接口，并运行一个 gRPC 服务器来处理客户端调用。
- 目前在 gRPC 方式接入GSE的过程中，未启用 gRPC 的流式 RPC。

<dx-alert infotype="explain" title="">
关于 gRPC 的更多介绍，请您参考 [gRPC 官方文档中文版](http://doc.oschina.net/grpc) 和 [gRPC@Linux Foundation](https://www.grpc.io/)。
</dx-alert>



## 集成 gRPC 框架

1. 安装 gRPC。
2. 定义服务。
3. 生成 gRPC 代码。
4. 游戏进程集成流程。
5. 启动服务端，供 GSE 调用。
6. 客户端连接 GSE 的 gRPC 服务端。

<dx-alert infotype="explain" title="">
- C++ 语言的具体调用逻辑，请您参考 [gRPC-C++ 教程](https://cloud.tencent.com/document/product/1165/46153)。
- C# 语言的具体调用逻辑，请您参考 [gRPC-C# 教程](https://cloud.tencent.com/document/product/1165/46152)。
- Go 语言的具体调用逻辑，请您参考 [gRPC-Go 教程](https://cloud.tencent.com/document/product/1165/46154)。
- Java 语言的具体调用逻辑，请您参考 [gRPC-Java 教程](https://cloud.tencent.com/document/product/1165/46155)。
- Lua 语言的具体调用逻辑，请您参考 [gRPC-Lua 教程](https://cloud.tencent.com/document/product/1165/46156)。
- Nodejs 语言的具体调用逻辑，请您参考 [gRPC-Nodejs 教程](https://cloud.tencent.com/document/product/1165/46157)。
</dx-alert>




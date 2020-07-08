
## proto文件

1. 游戏进程和 GSE 通过 gRPC 通信，通信 proto 的协议见 GameServerGrpcSdkService.proto和GseGrpcSdkService.proto。
  ![](2.png)
1. GameServerGrpcSdkService.proto定义的三个服务接口，由游戏进程来实现，而 GSE 需要在合适的时机调用对应的接口。
2. GseGrpcSdkService.proto定义的九个服务接口，由GSE来实现，而游戏进程需要在合适的时机调用对应的接口。GSE 接口监听 gRPC 的端口为5758。

 >?
我们提供定义服务的proto文件，您可直接[下载](#proto文件下载)使用，无需自己生成。


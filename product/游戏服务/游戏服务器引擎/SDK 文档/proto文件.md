1. 游戏进程和 GSE 通过 gRPC 通信，通信 proto 的协议见 GameServerGrpcSdkService.proto 和 GseGrpcSdkService.proto。
![](https://qcloudimg.tencent-cloud.cn/raw/b6753f157c5f43b01f4d5a716c8ef7a1.png)
2. GameServerGrpcSdkService.proto 定义的三个服务接口，由游戏进程来实现，而 GSE 需要在合适的时机调用对应的接口。
3. GseGrpcSdkService.proto 定义的九个服务接口，由 GSE 来实现，而游戏进程需要在合适的时机调用对应的接口。GSE 接口监听 gRPC 的端口为5758。


<dx-alert infotype="explain" title="">
我们提供定义服务的proto文件，您可直接 [下载](https://gsegrpcdemo-1301007756.cos.ap-guangzhou.myqcloud.com/proto.zip) 使用，无需自己生成。
</dx-alert>





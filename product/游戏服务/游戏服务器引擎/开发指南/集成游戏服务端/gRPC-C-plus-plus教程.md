
## 安装gRPC
1. 先决条件--安装 CMake。
  - Linux
  ```
  $ sudo apt install -y cmake
  ```
  
  - MAC OS
  ```
  $ brew install cmake
  ```
  
1. 在本地安装 gRPC和protocol buffers。

 >?
具体安装流程请您参考[安装CMake](https://cmake.org/install)，[安装 gRPC C ++的说明](https://github.com/grpc/grpc/blob/master/BUILDING.md)，[安装protocol buffers的说明](https://github.com/protocolbuffers/protobuf/blob/master/src/README.md)。

## 定义服务
gRPC 通过 protocol buffers 实现定义一个服务：一个 RPC 服务通过参数和返回类型来指定可以远程调用的方法。

 >?
我们提供定义服务的proto文件，请您在[proto文件](#proto文件)里下载使用，无需自己生成。

## 生成 gRPC 代码
1. 定义好服务后，通过 protocol buffer 编译器 protoc 生成客户端和服务端的代码（任意 gRPC 支持的语言）。 
2. 生成的代码包括客户端的存根和服务端要实现的抽象接口。
3. 生成 gRPC 代码步骤：
    在proto目录下执行：
     - ```protoc --cpp_out=. *.proto``` 生成pb.cc和pb.h 文件。
     - ```protoc --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` *.proto```生成对应的gRPC代码。
     - 将生成的8个文件移到项目合适的位置。

## 游戏进程集成流程
![](1.png)

####服务端接口列表

| 接口名称 | 接口功能|
|-----|----|
|[OnHealthCheck](#健康检查)| 健康检查|
|[OnStartGameServerSession](#接收游戏服务器会话)|接收游戏服务器会话|
|[OnProcessTerminate](#结束游戏进程)|结束游戏进程|

####客户端接口列表

| 接口名称 | 接口功能 |
|-----|----|
|[ProcessReady](#进程已就绪)|进程准备就绪|
|[ActivateGameServerSession](#激活游戏服务器会话)|激活游戏服务器会话|
|[AcceptPlayerSession](#接收玩家会话)|接收玩家会话|
|[RemovePlayerSession](#移除玩家会话)|移除玩家会话|
|[DescribePlayerSessions](#获取玩家会话信息)|获取玩家会话列表|
|[UpdatePlayerSessionCreationPolicy](#更新玩家会话的创建策略)|更新玩家会话的创建策略|
|[TerminateGameServerSession](#结束游戏服务器会话)|结束游戏服务器会话|
|[ProcessEnding](#结束进程)|结束进程|
|[ReportCustomData](#上报自定义数据)|上报自定义数据|

####其他

 请求 meta，在游戏进程通过 gRPC 调用 [GSE 相关接口](#  调用GSE相关接口) 时，需要在 gRPC 请求的 meta 里添加两个字段。

| 字段      | 含义                                      | 类型   |
| --------- | ----------------------------------------- | ------ |
| pid       | 当前游戏进程的 pid                         | string |
| requestId | 当前请求的 requestId，已使用唯一标记一次请求 | string |

###1. 一般在服务端初始化后，进程检查自身是否可对外提供服务，Game Server 调用 ProcessReady 接口，告知 GSE 进程准备就绪，已准备好托管游戏服务器会话，GSE 接收到后，将服务器实例状态更改为“活跃”。

```
Status GseManager::ProcessReady(std::vector<std::string> &logPath, int clientPort, int grpcPort, GseResponse& reply)
{
        ProcessReadyRequest request;
        //日志路径
        for (auto iter = logPath.begin(); iter != logPath.end(); iter++)
        {
            request.add_logpathstoupload(*iter);
    }
```
```
        GConsoleLog->PrintOut(true, "ProcessReady clientPort is %d\n", clientPort);
        GConsoleLog->PrintOut(true, "ProcessReady grpcPort is %d\n", grpcPort);
```
```
        //设置端口
        request.set_clientport(clientPort);
        request.set_grpcport(grpcPort);
```
```       
        ClientContext context;
        AddMetadata(context);
```
```
        //准备就绪，可对外提供服务
        return stub_->ProcessReady(&context, request, &reply);
}
```

###2. 进程准备就绪后，GSE调用OnHealthCheck接口，对Game Server进行健康检查，每1分钟检查1次，连续3次失败就判定该进程不健康，不会分配游戏服务器会话至该进程。

```
Status GameServerGrpcSdkServiceImpl::OnHealthCheck(ServerContext* context, const HealthCheckRequest* request,  HealthCheckResponse* reply)
{
        reply->set_healthstatus(healthStatus);
        return Status::OK;
}
```
### 3.因为 Client 调用[CreateGameServerSession](https://cloud.tencent.com/document/product/1165/42067)接口创建一个游戏服务器会话，将该游戏服务器会话分配给一个进程，所以触发 GSE 调用该进程的onStartGameServerSession接口，并且将GameServerSession状态更改为“激活中”。
```
Status GameServerGrpcSdkServiceImpl::OnStartGameServerSession(ServerContext* context, const StartGameServerSessionRequest* request,  GseResponse* reply)
{
        auto gameServerSession = request->gameserversession();
        GGseManager->SetGameServerSession(gameServerSession);
```
```
        GseResponse processReadyReply;
        Status status = GGseManager->ActivateGameServerSession(gameServerSession.gameserversessionid(), gameServerSession.maxplayers(), processReadyReply);
        // 对status和replay来判断，激活是否成功
```
```
        return Status::OK;
}
```
### 4.当Game Server收到onStartGameServerSession，您自行处理一些逻辑或资源分配，准备就绪后，Game Server就调用ActivateGameServerSession接口,通知GSE游戏服务器会话已分配给一个进程，现在已准备好接收玩家请求，将服务器状态更改为“活跃”。
```
Status GseManager::ActivateGameServerSession(std::string gameServerSessionId, int maxPlayers, GseResponse& reply)
{
        GConsoleLog->PrintOut(true, "ActivateGameServerSession gameServerSessionId is %s\n", gameServerSessionId.c_str());
        GConsoleLog->PrintOut(true, "ActivateGameServerSession maxPlayers is %d\n", maxPlayers);
```
```       
        ActivateGameServerSessionRequest request; 
        request.set_gameserversessionid(gameServerSessionId);
        request.set_maxplayers(maxPlayers);
```
```
        ClientContext context;
        AddMetadata(context);
```
```
        return stub_->ActivateGameServerSession(&context, request, &reply);
}
```
### 5.当Client调用[JoinGameServerSession](https://cloud.tencent.com/document/product/1165/42061)接口玩家加入后，Game Server调用AcceptPlayerSession接口验证玩家合法性，如果连接被接受，则将PlayerSession 状态设置为“活跃”。如果Client调用JoinGameServerSession接口在60秒内未收到响应，则将PlayerSession状态更改为“超时”，然后重新调用JoinGameServerSession。
```
Status GseManager::AcceptPlayerSession(std::string playerSessionId, GseResponse& reply)
{
        AcceptPlayerSessionRequest request;
        request.set_gameserversessionid(gameServerSession.gameserversessionid());
        request.set_playersessionid(playerSessionId);
```
```
        ClientContext context;
        AddMetadata(context);
```
```
        return stub_->AcceptPlayerSession(&context, request, &reply);
}
```
### 6.游戏结束或者玩家退出后，Game Server 调用RemovePlayerSession接口移除玩家，将playersession状态更改为“已完成” ，并预留游戏服务器会话中的玩家位置。
```
Status GseManager::RemovePlayerSession(std::string playerSessionId, GseResponse& reply)
{
        GConsoleLog->PrintOut(true, "RemovePlayerSession playerSessionId is %s\n", playerSessionId.c_str());
        RemovePlayerSessionRequest request;
        request.set_gameserversessionid(gameServerSession.gameserversessionid());
        request.set_playersessionid(playerSessionId);
```
```
        ClientContext context;
        AddMetadata(context);
```
```
        return stub_->RemovePlayerSession(&context, request, &reply);
}
```
### 7.当一个游戏服务器会话（一组游戏对局/一个服务）结束后，Game Server 调用TerminateGameServerSession接口结束GameServerSession，将GameServerSession 状态更改为“已终止”。
```
Status GseManager::TerminateGameServerSession(GseResponse& reply)
{
        GConsoleLog->PrintOut(true, "start to TerminateGameServerSession\n");
        TerminateGameServerSessionRequest request;
        request.set_gameserversessionid(gameServerSession.gameserversessionid());
```
```
        ClientContext context;
        AddMetadata(context);
```
```
        return stub_->TerminateGameServerSession(&context, request, &reply);
}
```
### 8.当健康检查失败或缩容时，GSE 调用 OnProcessTerminate 接口结束游戏进程，缩容时依据是您在 GSE 控制台配置的[保护策略](https://cloud.tencent.com/document/product/1165/41028#网络)。
```
Status GameServerGrpcSdkServiceImpl::OnProcessTerminate(ServerContext* context, const ProcessTerminateRequest* request,  GseResponse* reply)
{
        auto terminationTime = request->terminationtime();
        GGseManager->SetTerminationTime(terminationTime);
```
```
        //调以下两个接口，会立即结束游戏服务器会话，建议无玩家或无游戏服务器会话后，再调用processEnding结束进程
        //不调用以下两个接口，根据保护策略调用processEnding结束进程，建议配置时限保护
```
```        
        //结束游戏服务器会话
        GseResponse terminateGameServerSessionReply;
        GGseManager->TerminateGameServerSession(terminateGameServerSessionReply);
```
```
        // 结束进程
        GseResponse processEndingReply;
        GGseManager->ProcessEnding(processEndingReply);
```
```
        return Status::OK;
}
```
### 9.Game Server调用ProcessEnding接口会立刻结束进程，将服务器进程状态更改为“已终止”，并回收资源。
```
//主动调用：一局游戏对应一个进程，当一局游戏结束后主动调用ProcessEnding接口
//被动调用：当缩容或进程异常健康检查失败时，根据保护策略被动调用ProcessEnding接口，配置完全保护和时限保护策略时需要先判断游戏服务器会话上有无玩家，再被动调用
Status GseManager::ProcessEnding(GseResponse& reply)
{
        GConsoleLog->PrintOut(true, "start to ProcessEnding\n");
        ProcessEndingRequest request;
```
```
        ClientContext context;
        AddMetadata(context);
```
```
        return stub_->ProcessEnding(&context, request, &reply);
}
```
### 10.Game Server调用DescribePlayerSessions接口获取游戏服务器会话下的玩家信息（根据业务可选）。

```
Status GseManager::DescribePlayerSessions(std::string gameServerSessionId, std::string  playerId, std::string  playerSessionId,
    std::string playerSessionStatusFilter, std::string nextToken, int limit, DescribePlayerSessionsResponse& reply)
{
        GConsoleLog->PrintOut(true, "start to DescribePlayerSessions\n");
        DescribePlayerSessionsRequest request;
        request.set_gameserversessionid(gameServerSessionId);
        request.set_playerid(playerId);
        request.set_playersessionid(playerSessionId);
        request.set_playersessionstatusfilter(playerSessionStatusFilter);
        request.set_nexttoken(nextToken);
        request.set_limit(limit);
```
```
        ClientContext context;
        AddMetadata(context);
```
```
        return stub_->DescribePlayerSessions(&context, request, &reply);
}
```
### 11.Game Server调用UpdatePlayerSessionCreationPolicy接口更新玩家会话的创建策略，设置是否接受新玩家，即游戏会话里是否允许加入人（根据业务可选）。
```
Status GseManager::UpdatePlayerSessionCreationPolicy(std::string newpolicy, GseResponse& reply)
{
        GConsoleLog->PrintOut(true, "UpdatePlayerSessionCreationPolicy, newpolicy is %s\n", newpolicy.c_str());
        UpdatePlayerSessionCreationPolicyRequest request;
        request.set_gameserversessionid(gameServerSession.gameserversessionid());
        request.set_newplayersessioncreationpolicy(newpolicy);
```
```
        ClientContext context;
        AddMetadata(context);
```
```
        return stub_->UpdatePlayerSessionCreationPolicy(&context, request, &reply);
}
```
### 12.Game Server调用ReportCustomData接口告知 GSE 的自定义数据，在查询游戏服务器会话时可以查到（根据业务可选）。
```
Status GseManager::ReportCustomData(int currentCustomCount, int maxCustomCount, GseResponse& reply)
{
        GConsoleLog->PrintOut(true, "ReportCustomData, currentCustomCount is %d\n", currentCustomCount);
        GConsoleLog->PrintOut(true, "ReportCustomData, maxCustomCount is %d\n", maxCustomCount);
```
```
        ReportCustomDataRequest request;
        request.set_currentcustomcount(currentCustomCount);
        request.set_maxcustomcount(maxCustomCount);
```
```
        ClientContext context;
        AddMetadata(context);
```
```
        return stub_->ReportCustomData(&context, request, &reply);
}
```

##启动服务端，供GSE调用

服务端运行:将GrpcServer启动起来。

```
GameServerGrpcSdkServiceImpl::GameServerGrpcSdkServiceImpl() : serverAddress("127.0.0.1:0"), healthStatus(true)
{
        sem_init(&sem, 0, 0);
}
```
```
void GameServerGrpcSdkServiceImpl::StartGrpcServer()
{
        ServerBuilder builder;
        builder.AddListeningPort(serverAddress, grpc::InsecureServerCredentials(), &grpcPort);
        builder.RegisterService(this);
        std::unique_ptr<Server> server(builder.BuildAndStart());
        sem_post(&sem);
        server->Wait();
}
```


##客户端连接GSE的gRPC服务端

连接服务端:创建一个 gRPC 频道，指定我们要连接的主机名和服务器端口，然后用这个频道创建存根实例。

```
void GseManager::InitStub()
{
        auto channel = grpc::CreateChannel("127.0.0.1:5758", grpc::InsecureChannelCredentials());
        stub_ = GseGrpcSdkService::NewStub(channel);
}
```

## C++ DEMO
### 1.[单击这里](https://gsegrpcdemo-1301007756.cos.ap-guangzhou.myqcloud.com/cpp-demo.zip)，您可下载C++ DEMO代码。
### 2.生成 gRPC 代码
C++ DEMO 代码示例里已生成 gRPC 代码，在cpp-demo/source/grpcsdk目录下，不需要额外生成。
### 3.启动服务端，供GSE调用

- 服务端实现。
在cpp-demo/source/api目录下的grpcserver.cpp，实现了服务端的三个接口。

- 服务端运行。
在cpp-demo/source/api目录下的grpcserver.cpp，将GrpcServer启动起来。


### 4.客户端连接GSE的gRPC服务端

- 客户端实现。
在cpp-demo/source/gsemanager目录下的gsemanager.cpp，实现了客户端的九个接口。

- 连接服务端。
创建一个 gRPC 频道，指定我们要连接的主机名和服务器端口，然后用这个频道创建存根实例。


### 5. 编译运行
- 安装cmake。
- 安装gcc，版本要求4.9以上。
- 将代码下载，在cpp-demo目录下，执行以下命令：
  ```
  mkdir build
  cmake ..
  make
  ```
  
 会生成对应的cpp-demo可执行文件。
- 将cpp-demo可执行文件打包为[生成包](https://cloud.tencent.com/document/product/1165/41030)，启动路径配置cpp-demo，无启动参数。
- 然后[创建服务器舰队](https://cloud.tencent.com/document/product/1165/41028)，将生成包部署在服务器舰队上，后续可进行[扩缩容](https://cloud.tencent.com/document/product/1165/45709)等一系列操作。





## 安装gRPC
1. 使用gRPC Go时，需要先安装Go的最新主要版本。
2. 其次安装Protocol buffer 编辑器，版本为protoc3。
3. 安装Protocol buffer 编辑器里Go插件。
  - 使用以下命令为Go（protoc-gen-go）安装Protocol buffer 编译器插件：
  ```
  $ export GO111MODULE=on  # Enable module mode
  $ go get github.com/golang/protobuf/protoc-gen-go
  ```

  - 更新路径以便Protocol buffer 编译器找到Go插件：
```
$ export PATH="$PATH:$(go env GOPATH)/bin"
```

 >?
具体流程请您参考[安装 Go 的说明](https://golang.org/doc/install)，[安装Protocol buffer 编辑器的说明](https://www.grpc.io/docs/protoc-installation/)。

## 定义服务
 gRPC 通过 protocol buffers 实现定义一个服务：一个 RPC 服务通过参数和返回类型来指定可以远程调用的方法。

 >?
我们提供定义服务的proto文件，请您在[proto文件](#proto文件)里下载使用，无需自己生成。

## 生成 gRPC 代码
1. 定义好服务后，通过 protocol buffer 编译器 protoc 生成客户端和服务端的代码（任意 gRPC 支持的语言）。 
2. 生成的代码包括客户端的存根和服务端要实现的抽象接口。
3. 生成 gRPC 代码步骤：
    在 proto 目录下执行：
      -```protoc --go_out=plugins=grpc:. *.proto```，会自动生成包含proto的go_package路径，而用户可以根据需要修改成适合自己的go_package路径，但不能修改package。

## 游戏进程集成流程
![](1.png)

#### 服务端接口列表

| 接口名称 | 接口功能|
|-----|----|
|[OnHealthCheck](#健康检查)| 健康检查|
|[OnStartGameServerSession](#接收游戏服务器会话)|接收游戏服务器会话|
|[OnProcessTerminate](#结束游戏进程)|结束游戏进程|
#### 客户端接口列表

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

###1.一般在服务端初始化后，进程检查自身是否可对外提供服务，Game Server 调用 ProcessReady 接口，告知 GSE 进程准备就绪，已准备好托管游戏服务器会话，GSE 接收到后，将服务器实例状态更改为“活跃”。
```
func (g *gsemanager) ProcessReady(logPath []string, clientPort int32, grpcPort int32) error {
	logger.Info("start to processready", zap.Any("logPath", logPath), zap.Int32("clientPort", clientPort),
		zap.Int32("grpcPort", grpcPort))
	req := &grpcsdk.ProcessReadyRequest{
		//日志路径
		LogPathsToUpload: logPath,
		//设置端口
		ClientPort:       clientPort,
		GrpcPort:         grpcPort,
	}
```
```
	_, err := g.rpcClient.ProcessReady(g.getContext(), req)
	if err != nil {
		logger.Info("ProcessReady fail", zap.Error(err))
		return err
	}
```
```
    //准备就绪，可对外提供服务
	logger.Info("ProcessReady success")
	return nil
}
```
###2. 进程准备就绪后，GSE调用OnHealthCheck接口，对Game Server进行健康检查，每1分钟检查1次，连续3次失败就判定该进程不健康，不会分配游戏服务器会话至该进程。
```
func _GameServerGrpcSdkService_OnHealthCheck_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(HealthCheckRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GameServerGrpcSdkServiceServer).OnHealthCheck(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/tencentcloud.gse.grpcsdk.GameServerGrpcSdkService/OnHealthCheck",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GameServerGrpcSdkServiceServer).OnHealthCheck(ctx, req.(*HealthCheckRequest))
	}
	return interceptor(ctx, in, info, handler)
}
```
### 3.因为 Client 调用[CreateGameServerSession](https://cloud.tencent.com/document/product/1165/42067)接口创建一个游戏服务器会话，将该游戏服务器会话分配给一个进程，所以触发 GSE 调用该进程的onStartGameServerSession接口，并且将GameServerSession状态更改为“激活中”。
```
func _GameServerGrpcSdkService_OnStartGameServerSession_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(StartGameServerSessionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GameServerGrpcSdkServiceServer).OnStartGameServerSession(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/tencentcloud.gse.grpcsdk.GameServerGrpcSdkService/OnStartGameServerSession",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GameServerGrpcSdkServiceServer).OnStartGameServerSession(ctx, req.(*StartGameServerSessionRequest))
	}
	return interceptor(ctx, in, info, handler)
}
```
### 4.当Game Server收到onStartGameServerSession，您自行处理一些逻辑或资源分配，准备就绪后，Game Server就调用ActivateGameServerSession接口,通知GSE游戏服务器会话已分配给一个进程，现在已准备好接收玩家请求，将服务器状态更改为“活跃”。
```
func (g *gsemanager) ActivateGameServerSession(gameServerSessionId string, maxPlayers int32) error {
	logger.Info("start to ActivateGameServerSession", zap.String("gameServerSessionId", gameServerSessionId),
		zap.Int32("maxPlayers", maxPlayers))
	req := &grpcsdk.ActivateGameServerSessionRequest{
		GameServerSessionId:  gameServerSessionId,
		MaxPlayers:           maxPlayers,
	}
```
```
	_, err := g.rpcClient.ActivateGameServerSession(g.getContext(), req)
	if err != nil {
		logger.Error("ActivateGameServerSession fail", zap.Error(err))
		return err
	}
```
```
	logger.Info("ActivateGameServerSession success")
	return nil
}
```
### 5.当Client调用[JoinGameServerSession](https://cloud.tencent.com/document/product/1165/42061)接口玩家加入后，Game Server调用AcceptPlayerSession接口验证玩家合法性，如果连接被接受，则将PlayerSession 状态设置为“活跃”。如果Client调用JoinGameServerSession接口在60秒内未收到响应，则将PlayerSession状态更改为“超时”，然后重新调用JoinGameServerSession。
```
func (g *gsemanager) AcceptPlayerSession(playerSessionId string) (*grpcsdk.GseResponse, error) {
	logger.Info("start to AcceptPlayerSession", zap.String("playerSessionId", playerSessionId))
	req := &grpcsdk.AcceptPlayerSessionRequest{
		GameServerSessionId:  g.gameServerSession.GameServerSessionId,
		PlayerSessionId:      playerSessionId,
	}
```
```
	return g.rpcClient.AcceptPlayerSession(g.getContext(), req)
}
```
### 6.游戏结束或者玩家退出后，Game Server 调用RemovePlayerSession接口移除玩家，将playersession状态更改为“已完成” ，并预留游戏服务器会话中的玩家位置。
```
func (g *gsemanager) RemovePlayerSession(playerSessionId string) (*grpcsdk.GseResponse, error) {
	logger.Info("start to RemovePlayerSession", zap.String("playerSessionId", playerSessionId))
	req := &grpcsdk.RemovePlayerSessionRequest{
		GameServerSessionId:  g.gameServerSession.GameServerSessionId,
		PlayerSessionId:      playerSessionId,
	}
```
```
	return g.rpcClient.RemovePlayerSession(g.getContext(), req)
}
```
### 7.当一个游戏服务器会话（一组游戏对局/一个服务）结束后，Game Server 调用TerminateGameServerSession接口结束GameServerSession，将GameServerSession 状态更改为“已终止”。
```
func (g *gsemanager) TerminateGameServerSession() (*grpcsdk.GseResponse, error) {
	logger.Info("start to TerminateGameServerSession")
	req := &grpcsdk.TerminateGameServerSessionRequest{
		GameServerSessionId:  g.gameServerSession.GameServerSessionId,
	}
```
```
	return g.rpcClient.TerminateGameServerSession(g.getContext(), req)
}
```
### 8.当健康检查失败或缩容时，GSE 调用 OnProcessTerminate 接口结束游戏进程，缩容时依据是您在 GSE 控制台配置的[保护策略](https://cloud.tencent.com/document/product/1165/41028#网络)。
```
func _GameServerGrpcSdkService_OnProcessTerminate_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ProcessTerminateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GameServerGrpcSdkServiceServer).OnProcessTerminate(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/tencentcloud.gse.grpcsdk.GameServerGrpcSdkService/OnProcessTerminate",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GameServerGrpcSdkServiceServer).OnProcessTerminate(ctx, req.(*ProcessTerminateRequest))
	}
	return interceptor(ctx, in, info, handler)
} 
```
### 9.Game Server调用ProcessEnding接口会立刻结束进程，将服务器进程状态更改为“已终止”，并回收资源。
```
//主动调用：一局游戏对应一个进程，当一局游戏结束后主动调用ProcessEnding接口
//被动调用：当缩容或进程异常健康检查失败时，根据保护策略被动调用ProcessEnding接口，配置完全保护和时限保护策略时需要先判断游戏服务器会话上有无玩家，再被动调用
func (g *gsemanager) ProcessEnding() (*grpcsdk.GseResponse, error) {
	logger.Info("start to ProcessEnding")
	req := &grpcsdk.ProcessEndingRequest{
	}
```
```
	return g.rpcClient.ProcessEnding(g.getContext(), req)
}
```
### 10.Game Server调用DescribePlayerSessions接口获取游戏服务器会话下的玩家信息（根据业务可选）。
```
func (g *gsemanager) DescribePlayerSessions(gameServerSessionId, playerId, playerSessionId, playerSessionStatusFilter, nextToken string,
	limit int32) (*grpcsdk.DescribePlayerSessionsResponse, error) {
	logger.Info("start to DescribePlayerSessions", zap.String("gameServerSessionId", gameServerSessionId),
		zap.String("playerId", playerId), zap.String("playerSessionId", playerSessionId),
		zap.String("playerSessionStatusFilter", playerSessionStatusFilter), zap.String("nextToken", nextToken),
		zap.Int32("limit", limit))
```
```
	req := &grpcsdk.DescribePlayerSessionsRequest{
		GameServerSessionId:       gameServerSessionId,
		PlayerId:                  playerId,
		PlayerSessionId:           playerSessionId,
		PlayerSessionStatusFilter: playerSessionStatusFilter,
		NextToken:                 nextToken,
		Limit:                     limit,
	}
```
```
	return g.rpcClient.DescribePlayerSessions(g.getContext(), req)
}
```
### 11.Game Server调用UpdatePlayerSessionCreationPolicy接口更新玩家会话的创建策略，设置是否接受新玩家，即游戏会话里是否允许加入人（根据业务可选）。
```
func (g *gsemanager) UpdatePlayerSessionCreationPolicy(newPolicy string) (*grpcsdk.GseResponse, error) {
	logger.Info("start to UpdatePlayerSessionCreationPolicy", zap.String("newPolicy", newPolicy))
	req := &grpcsdk.UpdatePlayerSessionCreationPolicyRequest{
		GameServerSessionId:            g.gameServerSession.GameServerSessionId,
		NewPlayerSessionCreationPolicy: newPolicy,
	}
```
```
	return g.rpcClient.UpdatePlayerSessionCreationPolicy(g.getContext(), req)
}
```
### 12.Game Server调用ReportCustomData接口告知 GSE 的自定义数据（根据业务可选）。
```
func (g *gsemanager) ReportCustomData(currentCustomCount, maxCustomCount int32) (*grpcsdk.GseResponse, error) {
	logger.Info("start to UpdatePlayerSessionCreationPolicy", zap.Int32("currentCustomCount", currentCustomCount),
		zap.Int32("maxCustomCount", maxCustomCount))
	req := &grpcsdk.ReportCustomDataRequest{
		CurrentCustomCount:   currentCustomCount,
		MaxCustomCount:       maxCustomCount,
	}
```
```
	return g.rpcClient.ReportCustomData(g.getContext(), req)
}
```
## 启动服务端，供GSE调用

服务端运行：将GrpcServer启动起来。

```
func (s *rpcService) StartGrpcServer() {
        listen, err := net.Listen("tcp", "127.0.0.1:")
        if err != nil {
            logger.Fatal("grpc fail to listen", zap.Error(err))
        }
```
```
        addr := listen.Addr().String()
        portStr := strings.Split(addr, ":")[1]
        s.grpcPort, err = strconv.Atoi(portStr)
        if err != nil {
            logger.Fatal("grpc fail to get port",zap.Error(err))
        }
```
```
        logger.Info("grpc listen port is", zap.Int("port", s.grpcPort))
```
```
        grpcServer := grpc.NewServer()
        grpcsdk.RegisterGameServerGrpcSdkServiceServer(grpcServer, s)
        logger.Info("start grpc server success")
        go grpcServer.Serve(listen)
}
```

## 客户端连接GSE的gRPC服务端
连接服务端：创建一个 gRPC 频道，指定我们要连接的主机名和服务器端口，然后用这个频道创建存根实例。

```
const (
        localhost = "127.0.0.1"
        agentPort = 5758
)
type gsemanager struct {
        pid    string
        gameServerSession *grpcsdk.GameServerSession
        terminationTime int64
        rpcClient grpcsdk.GseGrpcSdkServiceClient
}
```

## Go DEMO
### 1.[单击这里](https://gsegrpcdemo-1301007756.cos.ap-guangzhou.myqcloud.com/go-demo.zip)，您可下载Go DEMO代码。
### 2.生成 gRPC 代码
Go DEMO 代码示例里已生成 gRPC 代码，在go-demo/grpcsdk目录下，不需要额外生成。
### 3.启动服务端，供GSE调用

- 服务端实现。
在 go-demo/api目录下的grpcserver.go，实现了服务端的三个接口。

- 服务端运行。
在 go-demo/api目录下的grpcserver.go，将GrpcServer启动起来。


### 4.客户端连接GSE的gRPC服务端

- 客户端实现。
在go-demo/gsemanager目录下的gsemanager.go，实现了客户端的九个接口。

- 连接服务端。
创建一个 gRPC 频道，指定我们要连接的主机名和服务器端口，然后用这个频道创建存根实例。


### 5. 编译运行

- 在go-demo目录下，执行``` go mod vendor```，生成vendor目录。
- 编译命令：```go build -mod=vendor main.go```，会生成对应的go-demo可执行文件main.go。
- 将可执行文件main.go打包为[生成包](https://cloud.tencent.com/document/product/1165/41030)，启动路径配置main，无启动参数。
- 然后[创建服务器舰队](https://cloud.tencent.com/document/product/1165/41028)，将生成包部署在服务器舰队上，后续可进行[扩缩容](https://cloud.tencent.com/document/product/1165/45709)等一系列操作。
  
 



## 简介
游戏进程和 GSE 通过 grpc 通信，通信 pb 的协议见 GameServerGrpcSdkService.proto 和 GseGrpcSdkService.proto。

GameServerGrpcSdkService.proto 定义了三个服务接口，需要由游戏进程来实现。
GseGrpcSdkService.proto 定义的服务接口 GSE 来实现，游戏进程需要在合适的时机调用对应的接口，GSE 接口监听的 grpc 端口为5758。游戏开发者根据需要，生成对应语言的 pb 文件。

<dx-alert infotype="explain" title="">
- gproxy 的使用可以参考 [中文版](http://doc.oschina.net/grpc) 和 [英文版](https://www.grpc.io/)。
- 使用示例基于 go 语言，proto 生成的包名为 grpcsdk。 示例使用的公共函数 getContext，常量 LOCAL_ADDRESS 以及 message GseResponse 结构体请参见 [其他部分](#other)。
</dx-alert>





## 游戏进程集成流程
游戏进程在启动后，需要实现 grpc server，并实现 GameServerGrpcSdkService.proto 定义的三个接口。

[](id:OnHealthCheck)
### OnHealthCheck

#### 接口描述
GSE 会每隔一分钟调用一次该接口，用于获取游戏进程的健康状态，游戏进程需通过该接口，返回当前进程的健康状态。

#### 请求消息体

```
message HealthCheckRequest {
}
```

#### 返回消息体

```
message HealthCheckResponse {
    bool healthStatus = 1;
}
```

#### 字段说明

**HealthCheckResponse**

| 字段名       | 类型 | 说明                              |
| ------------ | ---- | --------------------------------- |
| healthStatus | bool | 进程健康则返回 true，否则返回 false |


#### 使用示例

```
func (s *rpcService) OnHealthCheck(ctx context.Context, req *grpcsdk.HealthCheckRequest) (*grpcsdk.HealthCheckResponse, error) {
	resp := &grpcsdk.HealthCheckResponse{
		HealthStatus: s.healthStatus,  //标记当前进程的健康状况
	}

	return resp, nil
}
```

[](id:OnStartGameServerSession)
### OnStartGameServerSession

#### 接口说明

当游戏开发者通过调用腾讯云 CreateGameServerSession 等相关云 API 接口生成 GameServerSession 后，GSE 会通过 OnStartGameServerSession 接口，将 GameServerSession 相关信息回传给游戏进程，游戏进程收到请求后，需要保存该 GameServerSession 对应的信息，并需要在其实现里调用 GSE 的 [ActivateGameServerSession 接口](#ActivateGameServerSession)。

#### 请求消息体

```
// game server session
message GameServerSession {
    string gameServerSessionId = 1;
    string fleetId = 2;
    string name = 3;
    int32 maxPlayers = 4;
    bool joinable = 5;
    repeated GameProperty gameProperties = 6;
    int32 port = 7;
    string ipAddress = 8;
    string gameServerSessionData = 9;
    string matchmakerData = 10;
    string dnsName = 11;
}

// 分配 gameserversession 到游戏进程
message StartGameServerSessionRequest {
    GameServerSession gameServerSession = 1;
}
```

#### 返回消息体

```
message GseResponse {
   enum Status {
      OK = 0;
      ERROR_400 = 1;
      ERROR_500 = 2;
   }
   Status status = 1;
   string responseData = 2;
   string errorMessage = 3;
}
```

#### 字段说明

**GameServerSession**
更多相关游戏会话详情请参见 [GameServerSession](https://cloud.tencent.com/document/api/1165/42074#GameServerSession)。


**GseResponse**

| 字段名       | 类型   | 说明                                     |
| ------------ | ------ | ---------------------------------------- |
| status       | 枚举   | 返回码，0成功；400请求错误；500内部错误 |
| responseData | string | 返回数据                                 |
| errorMessage | string | 成功或者失败提示信息                     |

#### 使用示例

```
func (s *rpcService) OnStartGameServerSession(ctx context.Context, req *grpcsdk.StartGameServerSessionRequest) (*grpcsdk.GseResponse, error) {
	s.GameServerSession = req.GameServerSession  // 保存 GameServerSession
	conn, _ := grpc.DialContext(context.Background(), LOCAL_ADDRESS, grpc.WithInsecure())
	defer conn.Close()
	cli := grpcsdk.NewGseGrpcSdkServiceClient(conn)

	request := &grpcsdk.ActivateGameServerSessionRequest{  //调用该接口激活游戏会话
		GameServerSessionId:  req.GameServerSession.GameServerSessionId,
		MaxPlayers:           req.GameServerSession.MaxPlayers,
	}

	return cli.ActivateGameServerSession(getContext(), request)
}
```

[](id:OnProcessTerminate)
### OnProcessTerminate

#### 接口说明

在缩容阶段或者健康检查持续失败，GSE 会调用该接口，通知游戏进程需结束进程，游戏进程收到请求后，需要结束其上在 [OnStartGameServerSession](#OnStartGameServerSession) 承载的游戏会话，并调用 GSE 实现的两个接口 [TerminateGameServerSession](#TerminateGameServerSession) 和 [ProcessEnding](#ProcessEnding)，通知 GSE 需结束该游戏会话和结束进程。

#### 请求消息体

```
// 结束游戏进程
message ProcessTerminateRequest {
    int64 terminationTime = 1;
}
```

#### 返回消息体

```
message GseResponse
```

#### 字段说明

##### ProcessTerminateRequest

| 字段名          | 类型  | 说明                                                         |
| --------------- | ----- | ------------------------------------------------------------ |
| terminationTime | int64 | GSE 结束进程的时间，在该时间戳后会结束进程<li>如果 fleet 是完全保护，则忽略时间<li>如果是时限保护，该时间是时限保护的时长<li>如果不保护，则默认是5分钟 |


#### 使用示例

```
func (s *rpcService) OnProcessTerminates(ctx context.Context, req *grpcsdk.ProcessTerminateRequest) (*grpcsdk.GseResponse, error) {
   s.TerminationTime = req.TerminationTime  
   conn, _ := grpc.DialContext(context.Background(), LOCAL_ADDRESS, grpc.WithInsecure())
   defer conn.Close()
   cli := grpcsdk.NewGseGrpcSdkServiceClient(conn)

   request := &grpcsdk.ProcessEndingRequest{  // 告诉GSE该进程正在结束
   }

   return cli.ProcessEnding(getContext(), request)
}
```

[](id:GSE)
## GSE 相关接口

[](id:ProcessReady)
### ProcessReady

#### 接口说明

在游戏进程启动后，如果准备就绪可以承载游戏会话，需要通知调用该接口 GSE 进程已就绪，随后 GSE 即可调用 [OnStartGameServerSession 接口](#OnStartGameServerSession) 将游戏会话分配给该进程。

#### 请求消息体

```
message ProcessReadyRequest {
    repeated string logPathsToUpload = 1;
    int32 clientPort = 2;
    int32 grpcPort = 3;
}
```

#### 返回消息体

```
message GseResponse 
```

#### 字段说明

**ProcessReadyRequest**

| 字段名           | 类型        | 说明                                                         |
| ---------------- | ----------- | ------------------------------------------------------------ |
| logPathsToUpload | string 数组 | 游戏进程需要上传的日志路径，GSE 会将其指定的日志路径文件上传到腾讯云，供游戏开发者下载 |
| clientPort       | int32       | clientPort 为游戏客户端要链接的端口                           |
| grpcPort         | int32       | grpcPort 为游戏进程实现 GameServerGrpcSdkService.proto 定义的服务指定的端口，GSE 使用该端口请求其中的三个方法 |

#### 请求示例

```
func (r *rpcClient) ProcessReady(logPath []string, clientPort int32, grpcPort int32) (*grpcsdk.GseResponse, error) {
	conn, _ := grpc.DialContext(context.Background(), LOCAL_ADDRESS, grpc.WithInsecure())
	defer conn.Close()
	req := &grpcsdk.ProcessReadyRequest{
		LogPathsToUpload: logPath,
		ClientPort:       clientPort,
		GrpcPort:         grpcPort,
	}

	client := grpcsdk.NewGseGrpcSdkServiceClient(conn)
	return client.ProcessReady(getContext(), req)
}
```

<span id="ActivateGameServerSession"></span>
### ActivateGameServerSession

#### 接口说明

游戏进程通过 [OnStartGameServerSession 接口](#OnStartGameServerSession) 收到 GSE 的回调后，需要调用该接口告诉 GSE 来激活对应的 GameServerSession。

#### 请求消息体：

```
message ActivateGameServerSessionRequest{
    string gameServerSessionId = 1;
    int32 maxPlayers = 2;
}
```

#### 返回消息体

```
message GseResponse 
```

#### 字段说明

##### ActivateGameServerSessionRequest

| 字段名              | 类型   | 说明                                                         |
| ------------------- | ------ | ------------------------------------------------------------ |
| gameServerSessionId | string | 对应 GameServerSession 结构的 GameServerSessionId，唯一标记一次游戏会话 |
| maxPlayers          | int32  | 该游戏会话最大允许加入的玩家数                               |

#### 使用示例

使用示例请参见 [OnStartGameServerSession 接口](#OnStartGameServerSession)。


[](id:AcceptPlayerSession)
### AcceptPlayerSession 

#### 接口说明

当玩家加入游戏后，游戏进程需要调用该接口并通知 GSE 玩家已经加入。GSE 通过该接口传入的 gameServerSessionId 和 playerSessionId 参数校验该玩家的合法性。

#### 请求结构体

```
message AcceptPlayerSessionRequest {
    string gameServerSessionId = 1;
    string playerSessionId = 2;
}
```

#### 返回结构体

```
message GseResponse
```

#### 字段说明

**AcceptPlayerSessionRequest**

| 字段名              | 类型   | 说明                                                         |
| ------------------- | ------ | ------------------------------------------------------------ |
| gameServerSessionId | string | 对应 GameServerSession 结构的 GameServerSessionId，唯一标记一次游戏会话 |
| playerSessionId     | string | 游戏开发者通过调用腾讯云 JoinGameServerSession 返回的玩家在对应的游戏会话中的唯一 ID |

#### 使用示例

```
func (r *rpcClient) AcceptPlayerSession(gameServerSessionId, playerSessionId string) (*grpcsdk.GseResponse, error) {
   conn, _ := grpc.DialContext(context.Background(), LOCAL_ADDRESS, grpc.WithInsecure())
   defer conn.Close()

   req := &grpcsdk.AcceptPlayerSessionRequest{
      GameServerSessionId:  gameServerSessionId,
      PlayerSessionId:      playerSessionId,
   }

   client := grpcsdk.NewGseGrpcSdkServiceClient(conn)
   return client.AcceptPlayerSession(getContext(), req)
}
```

[](id:RemovePlayerSession)
### RemovePlayerSession 

#### 接口说明
当玩家退出游戏后，游戏进程需要调用该接口通知 GSE 某个玩家已经退出。GSE 收到该请求后，将更新对应的游戏会话的当前玩家数，以允许其他玩家加入进来。

#### 请求消息体

```
message RemovePlayerSessionRequest {
    string gameServerSessionId = 1;
    string playerSessionId = 2;
}
```

#### 返回消息体

```
message GseResponse 
```

#### 字段说明

使用示例请参见 [AcceptPlayerSession](#AcceptPlayerSession)。

#### 使用示例

```
func (r *rpcClient) RemovePlayerSession(gameServerSessionId, playerSessionId string) (*grpcsdk.GseResponse, error) {
   conn, _ := grpc.DialContext(context.Background(), LOCAL_ADDRESS, grpc.WithInsecure())
   defer conn.Close()
   req := &grpcsdk.RemovePlayerSessionRequest{
      GameServerSessionId:  gameServerSessionId,
      PlayerSessionId:      playerSessionId,
   }

   client := grpcsdk.NewGseGrpcSdkServiceClient(conn)
   return client.RemovePlayerSession(getContext(), req)
}
```

[](id:DescribePlayerSessions)
### DescribePlayerSessions 

#### 接口说明

游戏进程可以通过该接口，获取当前已经加入至其上承载的游戏会话的玩家信息列表。

#### 请求消息体：

```
message DescribePlayerSessionsRequest {
   string gameServerSessionId = 1;
   string playerId = 2;
   string playerSessionId = 3;
   string playerSessionStatusFilter = 4;
   string nextToken = 5;
   int32 limit = 6;
}
```

#### 返回消息体

```
message PlayerSession {
   string playerSessionId = 1;
   string playerId = 2;
   string gameServerSessionId = 3;
   string fleetId = 4;
   string ipAddress = 5;
   string status = 6;
   int64 creationTime = 7;
   int64 terminationTime = 8;
   int32 port = 9;
   string playerData = 10;
   string dnsName = 11;
}

message DescribePlayerSessionsResponse {
   string nextToken = 1;
   repeated PlayerSession playerSessions = 2;
}
```

#### 字段说明

**DescribePlayerSessionsRequest**

相关字段含义请参见 [输入参数](https://cloud.tencent.com/document/api/1165/42063#2.-.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0)。

**DescribePlayerSessionsResponse**

相关字段含义参见 [PlayerSession](https://cloud.tencent.com/document/api/1165/42074#PlayerSession)。

#### 使用示例

```
func (r *rpcClient) DescribePlayerSessions(gameServerSessionId, playerId, playerSessionId, playerSessionStatusFilter, nextToken string,limit int32) (*grpcsdk.DescribePlayerSessionsResponse, error) {
   conn, _ := grpc.DialContext(context.Background(), LOCAL_ADDRESS, grpc.WithInsecure())
   defer conn.Close()

   req := &grpcsdk.DescribePlayerSessionsRequest{
      GameServerSessionId:       gameServerSessionId,
      PlayerId:                  playerId,
      PlayerSessionId:           playerSessionId,
      PlayerSessionStatusFilter: playerSessionStatusFilter,
      NextToken:                 nextToken,
      Limit:                     limit,
   }

   client := grpcsdk.NewGseGrpcSdkServiceClient(conn)
   return client.DescribePlayerSessions(getContext(), req)
}
```
<span id="UpdatePlayerSessionCreationPolicy"></span>
### UpdatePlayerSessionCreationPolicy 

#### 接口说明

游戏进程可以通过该接口，更新当前游戏会话玩家加入的策略。

#### 请求消息体

```
message UpdatePlayerSessionCreationPolicyRequest {
   string gameServerSessionId = 1;
   string newPlayerSessionCreationPolicy = 2;
}
```

#### 返回消息体

```
message GseResponse 
```

#### 字段说明

**UpdatePlayerSessionCreationPolicyRequest**

| 字段名                         | 类型   | 说明                                                         |
| ------------------------------ | ------ | ------------------------------------------------------------ |
| gameServerSessionId            | string | 对应 GameServerSession 结构的 GameServerSessionId，唯一标记一次游戏会话 |
| newPlayerSessionCreationPolicy | string | 更新后的策略<li>可选值有**ACCEPT_ALL**（接受所有新玩家会话）<li>**DENY_ALL** （拒绝所有新玩家会话） |

#### 使用示例

```
func (r *rpcClient) UpdatePlayerSessionCreationPolicy(gameServerSessionId, newpolicy string) (*grpcsdk.GseResponse, error) {
   conn, _ := grpc.DialContext(context.Background(), LOCAL_ADDRESS, grpc.WithInsecure())
   defer conn.Close()

   req := &grpcsdk.UpdatePlayerSessionCreationPolicyRequest{
      GameServerSessionId:            gameServerSessionId,
      NewPlayerSessionCreationPolicy: newpolicy,
   }

   client := grpcsdk.NewGseGrpcSdkServiceClient(conn)
   return client.UpdatePlayerSessionCreationPolicy(getContext(), req)
}
```

[](id:TerminateGameServerSession)
### TerminateGameServerSession 

#### 接口说明	

游戏进程需要调用该接口通知 GSE 其上承载的游戏会话已结束，GSE 后续可以将其他游戏会话重新分配到该进程。

#### 请求消息体

```
message TerminateGameServerSessionRequest {
    string gameServerSessionId = 1;
}
```

#### 返回消息体

```
message GseResponse 
```

#### 字段说明

**TerminateGameServerSessionRequest**

| 字段名              | 类型   | 说明                                                         |
| ------------------- | ------ | ------------------------------------------------------------ |
| gameServerSessionId | string | 对应 GameServerSession 结构的 GameServerSessionId，唯一标记一次游戏会话 |

#### 使用示例

```
func (r *rpcClient) TerminateGameServerSession(gameServerSessionId string) (*grpcsdk.GseResponse, error) {
   conn, _ := grpc.DialContext(context.Background(), LOCAL_ADDRESS, grpc.WithInsecure())
   defer conn.Close()
   req := &grpcsdk.TerminateGameServerSessionRequest{
      GameServerSessionId: gameServerSessionId,
   }

   client := grpcsdk.NewGseGrpcSdkServiceClient(conn)
   return client.TerminateGameServerSession(g.getContext(), req)
}
```

[](id:ProcessEnding)
### ProcessEnding 

#### 接口说明

游戏进程需要调用该接口通知 GSE 该游戏进程正在关闭。

#### 请求结构体

```
message ProcessEndingRequest {
}
```

#### 返回消息体

```
message GseResponse
```

#### 字段说明

无

#### 使用示例

```
func (r *rpcClient) ProcessEnding() (*grpcsdk.GseResponse, error) {
   conn, _ := grpc.DialContext(context.Background(), LOCAL_ADDRESS, grpc.WithInsecure())
   defer conn.Close()
   req := &grpcsdk.ProcessEndingRequest{
   }
   client := grpcsdk.NewGseGrpcSdkServiceClient(conn)
   return client.ProcessEnding(g.getContext(), req)
}
```

[](id:ReportCustomData)
### ReportCustomData 

#### 接口说明

游戏进程可以调用该接口告知 GSE 的自定义数据。

#### 请求消息体：

```
message ReportCustomDataRequest {
    int32 currentCustomCount = 1;
    int32 maxCustomCount = 2;
}
```

#### 返回消息体

```
message GseResponse
```

#### 字段说明

##### ReportCustomDataRequest

| 字段名             | 类型  | 说明         |
| ------------------ | ----- | ------------ |
| currentCustomCount | int32 | 自定义当前值 |
| maxCustomCount     | int32 | 自定义最大值 |

#### 使用示例

```
func (r *rpcClient) ReportCustomData(currentCustomCount, maxCustomCount int32) (*grpcsdk.GseResponse, error) {
   conn, _ := grpc.DialContext(context.Background(), LOCAL_ADDRESS, grpc.WithInsecure())
   defer conn.Close()
   req := &grpcsdk.ReportCustomDataRequest{
      CurrentCustomCount:   currentCustomCount,
      MaxCustomCount:       maxCustomCount,
   }

   client := grpcsdk.NewGseGrpcSdkServiceClient(conn)
   return client.ReportCustomData(getContext(), req)
}
```


[](id:other)
## 其他

### 请求 meta

在游戏进程通过 grpc 调用 [GSE 相关接口](#GSE) 时，需要在 grpc 请求的 meta 里添加两个字段。

| 字段      | 含义                                      | 类型   |
| --------- | ----------------------------------------- | ------ |
| pid       | 当前游戏进程的 pid                         | string |
| requestId | 当前请求的 requestId，已使用唯一标记一次请求 | string |

### 示例公共代码

```
const (
	LOCAL_ADDRESS = "127.0.0.1:5758"
)

var (
   pid = strconv.Itoa(os.Getpid())
)

func getContext() context.Context {
   requestId := uuid.NewV4().String()   //进程生成自己的requestId
   ctx := metadata.AppendToOutgoingContext(context.Background(), "pid", pid)
   return metadata.AppendToOutgoingContext(ctx, "requestId", requestId)
}

message GseResponse {
   enum Status {
      OK = 0;
      ERROR_400 = 1;
      ERROR_500 = 2;
   }
   Status status = 1;
   string responseData = 2;
   string errorMessage = 3;
}
```


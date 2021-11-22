
## 安装 gRPC
1. 使用 gRPC C# 时，需要先安装 .Net Core 3.1 SDK。以 CentOS 操作系统为例，版本不得低于 CentOS 7 或 CentOS 8。
  - 添加签名密钥
```
sudo rpm -Uvh https://packages.microsoft.com/config/centos/7/packages-microsoft-prod.rpm```
 - 安装 .NET Core SDK
 ```
 sudo yum install dotnet-sdk-3.1```
2. 除此之外，您还可以以下运行环境 /IDE 中使用 gRPC C#：
 - Windows：.NET Framework 4.5或更高版本，Visual Studio 2013或更高版本，Visual Studio Code。
 - Linux：Mono 4或更高版本，Visual Studio Code。
 - Mac OS X：Mono 4或更高版本，Visual Studio Code，Visual Studio for Mac。


<dx-alert infotype="explain" title="">
 具体流程请您参考 [安装 gRPC C# 操作步骤](https://github.com/grpc/grpc/blob/v1.30.0/src/csharp/README.md#prerequisites)。
</dx-alert>




## 定义服务
 gRPC 通过 protocol buffers 实现定义一个服务：一个 RPC 服务通过参数和返回类型来指定可以远程调用的方法。

<dx-alert infotype="explain" title="">
我们提供定义服务的 proto 文件，请您在 [proto 文件](https://cloud.tencent.com/document/product/1165/46111) 里下载使用，无需自己生成。
</dx-alert>



## 生成 gRPC 代码
1. 定义好服务后，通过 protocol buffer 编译器 protoc 生成客户端和服务端的代码（任意 gRPC 支持的语言）。 
2. 生成的代码包括客户端的存根和服务端要实现的抽象接口。
3. 生成 gRPC 代码步骤：
     - 下载代码，在 csharp-demo 目录下，执行如下指令：
       ```
       dotnet run
       ```    
         即可自动编译并运行服务。
     - 程序正确编译运行后，会在 csharp-demo/obj/Debug/netcoreapp3.1 文件夹生成项目依赖的库、二进制文件以及 proto 文件编译后的 .cs 文件。
     - proto 文件的引入是在 csharp-demo/csharpdemo.csproj 中：
       ```
<Protobuf Include="..\proto\csharp-demo\GameServerGrpcSdkService.proto" Link="GameServerGrpcSdkService.proto"/>
<Protobuf Include="..\proto\csharp-demo\GseGrpcSdkService.proto" Link="GseGrpcSdkService.proto" />
       ```
       项目依赖于 proto/csharp-demo 文件夹中的 GameServerGrpcSdkService.proto 和 GseGrpcSdkService.proto 两个 proto 文件。

## 游戏进程集成流程
![](https://qcloudimg.tencent-cloud.cn/raw/68245d89e36aa1cbcf47069be18ba165.png)
#### Game Server 回调接口列表

| 接口名称 | 接口功能|
|-----|----|
|[OnHealthCheck](https://cloud.tencent.com/document/product/1165/46116)| 健康检查|
|[OnStartGameServerSession](https://cloud.tencent.com/document/product/1165/46118)|接收游戏服务器会话|
|[OnProcessTerminate](https://cloud.tencent.com/document/product/1165/46121)|结束游戏进程|

#### Game Server 主调接口列表

| 接口名称 | 接口功能 |
|-----|----|
|[ProcessReady](https://cloud.tencent.com/document/product/1165/46122)|进程准备就绪|
|[ActivateGameServerSession](https://cloud.tencent.com/document/product/1165/46115)|激活游戏服务器会话|
|[AcceptPlayerSession](https://cloud.tencent.com/document/product/1165/46117)|接收玩家会话|
|[RemovePlayerSession](https://cloud.tencent.com/document/product/1165/46125)|移除玩家会话|
|[DescribePlayerSessions](https://cloud.tencent.com/document/product/1165/46114)|获取玩家会话列表|
|[UpdatePlayerSessionCreationPolicy](https://cloud.tencent.com/document/product/1165/46113)|更新玩家会话的创建策略|
|[TerminateGameServerSession](https://cloud.tencent.com/document/product/1165/46120)|结束游戏服务器会话|
|[ProcessEnding](https://cloud.tencent.com/document/product/1165/46119)|结束进程|
|[ReportCustomData](https://cloud.tencent.com/document/product/1165/46124)|上报自定义数据|

#### 其他

 请求 meta，在游戏进程通过 gRPC 调用 Game Server 主调接口时，需要在 gRPC 请求的 meta 里添加两个字段。

| 字段      | 含义                                      | 类型   |
| --------- | ----------------------------------------- | ------ |
| pid       | 当前游戏进程的 pid                         | string |
| requestId | 当前请求的 requestId，已使用唯一标记一次请求 | string |

1. 一般在服务端初始化后，进程检查自身是否可对外提供服务，Game Server 调用 ProcessReady 接口，告知 GSE 进程准备就绪，已准备好托管游戏服务器会话，GSE 接收到后，将服务器实例状态更改为“活跃”。
```
public static GseResponse ProcessReady(string[] logPath, int clientPort, int grpcPort)
{
	logger.Println($"Getting process ready, LogPath: {logPath}, ClientPort: {clientPort}, GrpcPort: {grpcPort}");
	//设置端口
	var req = new ProcessReadyRequest{
		ClientPort = clientPort,
		GrpcPort = grpcPort,
	};
	//日志路径
	req.LogPathsToUpload.Add(logPath);         //repeated类型解析pb后，是只读类型，需要Add加入           
	//准备就绪，可对外提供服务
	return GrpcClient.GseClient.ProcessReady(req, meta);
}
```
2. 进程准备就绪后，GSE 调用 OnHealthCheck 接口，对 Game Server 进行健康检查，每1分钟检查1次，连续3次失败就判定该进程不健康，不会分配游戏服务器会话至该进程。
```
public override Task<HealthCheckResponse> OnHealthCheck(HealthCheckRequest request, ServerCallContext context)
{
	logger.Println($"OnHealthCheck, HealthStatus: {GseManager.HealthStatus}");
	return Task.FromResult(new HealthCheckResponse{
			HealthStatus = GseManager.HealthStatus
	});
}
```
3. 因为 Client 调用 [CreateGameServerSession](https://cloud.tencent.com/document/product/1165/42067) 接口创建一个游戏服务器会话，将该游戏服务器会话分配给一个进程，所以触发 GSE 调用该进程的 onStartGameServerSession 接口，并且将 GameServerSession 状态更改为“激活中”。
```java
public override Task<GseResponse> OnStartGameServerSession(StartGameServerSessionRequest request, ServerCallContext context)
{
	logger.Println($"OnStartGameServerSession, request: {request}");
	GseManager.SetGameServerSession(request.GameServerSession);
	var resp = GseManager.ActivateGameServerSession(request.GameServerSession.GameServerSessionId, request.GameServerSession.MaxPlayers);
	return Task.FromResult(resp);
}
```
4. 当 Game Server 收到 onStartGameServerSession，您自行处理一些逻辑或资源分配，准备就绪后，Game Server 就调用 ActivateGameServerSession 接口，通知 GSE 游戏服务器会话已分配给一个进程，现在已准备好接收玩家请求，将服务器状态更改为“活跃”。
<dx-codeblock>
:::  Java
public static GseResponse ActivateGameServerSession(string gameServerSessionId, int maxPlayers)
{
	logger.Println($"Activating game server session, GameServerSessionId: {gameServerSessionId}, MaxPlayers: {maxPlayers}");
	var req = new ActivateGameServerSessionRequest{
			GameServerSessionId = gameServerSessionId,
			MaxPlayers = maxPlayers,
	};  
	return GrpcClient.GseClient.ActivateGameServerSession(req, meta);
}
:::
</dx-codeblock>
5. 当 Client 调用 [JoinGameServerSession](https://cloud.tencent.com/document/product/1165/42061) 接口玩家加入后，Game Server 调用 AcceptPlayerSession 接口验证玩家合法性，如果连接被接受，则将 PlayerSession 状态设置为“活跃”。如果 Client 调用 JoinGameServerSession 接口在60秒内未收到响应，则将 PlayerSession 状态更改为“超时”，然后重新调用 JoinGameServerSession。
<dx-codeblock>
:::  Java
public static GseResponse AcceptPlayerSession(string playerSessionId)
{
	logger.Println($"Accepting player session, PlayerSessionId: {playerSessionId}");
	var req = new AcceptPlayerSessionRequest{
			GameServerSessionId = gameServerSession.GameServerSessionId,
			PlayerSessionId = playerSessionId,
	};            
	return GrpcClient.GseClient.AcceptPlayerSession(req, meta);
}
:::
</dx-codeblock>
6. 游戏结束或者玩家退出后，Game Server 调用 RemovePlayerSession 接口移除玩家，将 playersession 状态更改为“已完成” ，并预留游戏服务器会话中的玩家位置。
<dx-codeblock>
:::  java 
public static GseResponse RemovePlayerSession(string playerSessionId)
{
	logger.Println($"Removing player session, PlayerSessionId: {playerSessionId}");
	var req = new RemovePlayerSessionRequest{
			GameServerSessionId = gameServerSession.GameServerSessionId,
			PlayerSessionId = playerSessionId,
	};            
	return GrpcClient.GseClient.RemovePlayerSession(req, meta);
}
:::
</dx-codeblock>
7. 当一个游戏服务器会话（一组游戏对局或一个服务）结束后，Game Server 调用 TerminateGameServerSession 接口结束 GameServerSession，将 GameServerSession 状态更改为“已终止”。
<dx-codeblock>
:::  java 
public static GseResponse TerminateGameServerSession()
{
	logger.Println($"Terminating game server session, GameServerSessionId: {gameServerSession.GameServerSessionId}");
	var req = new TerminateGameServerSessionRequest{
			GameServerSessionId = gameServerSession.GameServerSessionId
	};            
	return GrpcClient.GseClient.TerminateGameServerSession(req, meta);
}
:::
</dx-codeblock>
8. 当健康检查失败或缩容时，GSE 调用 OnProcessTerminate 接口结束游戏进程，缩容时依据是您在 GSE 控制台配置的 [保护策略](https://cloud.tencent.com/document/product/1165/41028#test12)。
<dx-codeblock>
:::  java 
 public override Task<GseResponse> OnProcessTerminate(ProcessTerminateRequest request, ServerCallContext context)
{
		logger.Println($"OnProcessTerminate, request: {request}");
		// 设置进程终止时间
		GseManager.SetTerminationTime(request.TerminationTime);
		//调以下两个接口，会立即结束游戏服务器会话，建议无玩家或无游戏服务器会话后，再调用ProcessEnding结束进程
		//不调用以下两个接口，根据保护策略调用ProcessEnding结束进程，建议配置时限保护

		// 终止游戏服务器会话
		GseManager.TerminateGameServerSession();
		// 进程退出
		GseManager.ProcessEnding();
		return Task.FromResult(new GseResponse{
				Status = GseResponse.Types.Status.Ok,
				ResponseData = "SUCCESS",
		});
}
:::
</dx-codeblock>
9. Game Server 调用 ProcessEnding 接口会立刻结束进程，将服务器进程状态更改为“已终止”，并回收资源。
<dx-codeblock>
:::  java 
//主动调用：一局游戏对应一个进程，当一局游戏结束后主动调用 ProcessEnding 接口
//被动调用：当缩容或进程异常健康检查失败时，根据保护策略被动调用 ProcessEnding 接口，配置完全保护和时限保护策略时需要先判断游戏服务器会话上有无玩家，再被动调用
public static GseResponse ProcessEnding()
{
	logger.Println($"Process ending, pid: {pid}");
	var req = new ProcessEndingRequest();            
	return GrpcClient.GseClient.ProcessEnding(req, meta);
}
:::
</dx-codeblock>
10. Game Server 调用 DescribePlayerSessions 接口获取游戏服务器会话下的玩家信息（根据业务可选）。
<dx-codeblock>
:::  java 
public static DescribePlayerSessionsResponse DescribePlayerSessions(string gameServerSessionId, string playerId, string playerSessionId, string playerSessionStatusFilter, string nextToken, int limit)
{
	logger.Println($"Describing player session, GameServerSessionId: {gameServerSessionId}, PlayerId: {playerId}, PlayerSessionId: {playerSessionId}, PlayerSessionStatusFilter: {playerSessionStatusFilter}, NextToken: {nextToken}, Limit: {limit}");
	var req = new DescribePlayerSessionsRequest{
			GameServerSessionId = gameServerSessionId,
			PlayerId = playerId,
			PlayerSessionId = playerSessionId,
			PlayerSessionStatusFilter = playerSessionStatusFilter,
			NextToken = nextToken,
			Limit = limit,
	};            
	return GrpcClient.GseClient.DescribePlayerSessions(req, meta);
}
:::
</dx-codeblock>
11. Game Server 调用 UpdatePlayerSessionCreationPolicy 接口更新玩家会话的创建策略，设置是否接受新玩家，即游戏会话里是否允许加入人（根据业务可选）。
<dx-codeblock>
:::  java
public static GseResponse UpdatePlayerSessionCreationPolicy(string newPolicy)
{
	logger.Println($"Updating player session creation policy, newPolicy: {newPolicy}");
	var req = new UpdatePlayerSessionCreationPolicyRequest{
			GameServerSessionId = gameServerSession.GameServerSessionId,
			NewPlayerSessionCreationPolicy = newPolicy,
	};            
	return GrpcClient.GseClient.UpdatePlayerSessionCreationPolicy(req, meta);
}
:::
</dx-codeblock>
12. Game Server 调用 ReportCustomData 接口告知 GSE 的自定义数据（根据业务可选）。
<dx-codeblock>
:::  java
public static GseResponse ReportCustomData(int currentCustomCount, int maxCustomCount)
{
	logger.Println($"Reporting custom data, CurrentCustomCount: {currentCustomCount}, MaxCustomCount: {maxCustomCount}");
	var req = new ReportCustomDataRequest{
			CurrentCustomCount = currentCustomCount,
			MaxCustomCount = maxCustomCount,
	};            
	return GrpcClient.GseClient.ReportCustomData(req, meta);
}
:::
</dx-codeblock>

## 启动服务端，供 GSE 调用

服务端运行：将 GrpcServer 启动起来。
<dx-codeblock>
:::  java
public class Program
{
public static int ClientPort = PortServer.GenerateRandomPort(2000, 6000);
public static int GrpcPort = PortServer.GenerateRandomPort(6001, 10000);

public static void Main(string[] args)
{
	CreateHostBuilder(args).Build().Run();
}
public static IHostBuilder CreateHostBuilder(string[] args) =>
Host.CreateDefaultBuilder(args)
	.ConfigureWebHostDefaults(webBuilder =>
	{
		webBuilder.ConfigureKestrel(options =>
		{
			 // gRPC 端口（设置不带 TLS 证书的 HTTP/2 端点）
			options.ListenAnyIP(GrpcPort, o => o.Protocols = 
					HttpProtocols.Http2);

			// HTTP 端口
			options.ListenAnyIP(ClientPort);
		});

		webBuilder.UseStartup<Startup>();
	});
}
:::
</dx-codeblock>

## 客户端连接 GSE 的 gRPC 服务端
连接服务端：创建一个 gRPC 频道，指定我们要连接的主机名和服务器端口，然后用这个频道创建存根实例。
<dx-codeblock>
:::  java
public class GrpcClient
{
	private static string agentAdress = "127.0.0.1:5758";
	public static GameServerGrpcSdkService.GameServerGrpcSdkServiceClient GameServerClient
	{
		get
		{
			Channel channel = new Channel(agentAdress, ChannelCredentials.Insecure);
			return new GameServerGrpcSdkService.GameServerGrpcSdkServiceClient(channel);
		}
	 }
	public static GseGrpcSdkService.GseGrpcSdkServiceClient GseClient
	{
		get
		{
			Channel channel = new Channel(agentAdress, ChannelCredentials.Insecure);
			return new GseGrpcSdkService.GseGrpcSdkServiceClient(channel);
		}
	}
}
:::
</dx-codeblock>


## C# DEMO
1. [单击这里](https://gsegrpcdemo-1301007756.cos.ap-guangzhou.myqcloud.com/csharp-demo.zip)，您可下载 C# DEMO 代码。
2. 生成 gRPC 代码。
C# DEMO 代码示例里已生成 gRPC 代码，在 proto/csharp-demo 目录下，不需要额外生成。
3. 启动服务端，供 GSE 调用。
 - 服务端实现。
在 csharp-demo/api 目录下的 gameserversdk.cs，实现了服务端的三个接口。
 - 服务端运行。
在 csharp-demo 目录下的 Program.cs，将 GrpcServer 启动起来。
4. 客户端连接 GSE 的 gRPC 服务端。
 - 客户端实现。
在 csharp-demo/Models 目录下的 GseManager.cs，实现了客户端的九个接口。
 - 连接服务端。
创建一个 gRPC 频道，指定我们要连接的主机名和服务器端口，然后用这个频道创建存根实例。
5. 编译运行。
 1. 生成可执行文件及依赖
  ```
  dotnet publish -c Release -r linux-x64 --self-contained true 
  ```
 以上会在 csharp-demo/bin/Release/netcoreapp3.1/linux-x64 目录下生成打包生成包所需要的所有依赖文件，其中即包含运行该服务的可执行文件csharpdemo。
 - 拷贝前置脚本 install.sh
 ```
 chmod u+x install.sh
cp install.sh bin/Release/netcoreapp3.1/linux-x64
 ```
 - 打包 GSE 生成包
 ```
 cd csharp-demo/bin/Release/netcoreapp3.1/linux-x64
zip -r csharpdemo.zip * 
```
打包好的 csharpdemo.zip 即 GSE 需要的 [生成包](https://cloud.tencent.com/document/product/1165/41030)，启动路径填写 csharpdemo，无启动参数。
 - 然后 [创建服务器舰队](https://cloud.tencent.com/document/product/1165/41028)，将生成包部署在服务器舰队上，后续可进行 [扩缩容](https://cloud.tencent.com/document/product/1165/45709) 等一系列操作。
 
 


本文介绍使用 Unity 接入 GSE SDK 的完整过程，主要包括两方面工作：
1.Unity 接入 gRPC。
2.Unity 接入 GSE SDK。

## 前提条件
已安装 Unity Hub、Unity IDE。
<dx-alert infotype="notice" title="">
本文基于 Unity 引擎版本： 2018.3.5f1、2019.4.9f1，操作系统：MacOS。
</dx-alert>



## Unity 接入 gRPC

gRPC 对 Unity 的支持仍处于实验阶段，更多信息可参见 [README](https://github.com/grpc/grpc/tree/master/src/csharp/experimental)。具体操作步骤如下：

### 步骤1：创建 Unity 项目 

需要创建一个针对 `.NET 4.x` 等效版本的 Unity 项目，由于 gRPC 使用的 API 仅在 `.NET 4.5+`可用，所以这一步是必需的，通过**Edit**>**Project Setting**>**Player**>**Configuration**>**Scripting Runtime Version**进行设置。
![](https://main.qcloudimg.com/raw/c28d0dc10bded3be2e98358a95a374fa.jpg)

[](id:test)
### 步骤2：下载 grpc_unity_package

下载 `grpc_unity_package.VERSION.zip` 的 [最新开发版本](https://packages.grpc.io/)。单击 `Buidld ID` 跳转到下载页面。
![](https://main.qcloudimg.com/raw/9ac9fa93e7de83042e1771cf0c4e6379.jpg)
单击 `c#` 目录下的 `grpc_unity_package.VERSION.zip` 即可下载成功。
![](https://main.qcloudimg.com/raw/8aa7bbbb7ab6076f28e711bc3bd92907.jpg)

### 步骤3：解压

将下载的 `.zip` 文件解压到 Unity 项目的 `Assets` 目录中，如下图所示：
![](https://main.qcloudimg.com/raw/3d319f3b4acbf2dea17f09e704e083fe.png)

### 步骤4：测试 

Unity Editor 将取出文件并自动添加到项目中，您即可在代码中使用 gRPC 和 Protobuf，如果 Unity Editor 提示错误，详情可参见 [常见问题](https://cloud.tencent.com/document/product/1165/50191)。

## Unity 接入 GSE SDK

Unity 接入 GSE SDK 包括以下几个步骤：

### 步骤1：获取 GSE SDK Protobuf 文件

获取 GSE SDK Protobuf 文件 `GameServerGrpcSdkService.proto` 和 `GseGrpcSdkService.proto`，详情可参见 [proto 文件](https://cloud.tencent.com/document/product/1165/46111)。
[](id:test2)
### 步骤2：根据 Protobuf 生成 C# 代码
1. 下载 gRPC protoc Plugin，再次访问下载 [grpc_unity_package.VERSION.zip](#test) 页面，下载对应操作系统的 protoc 压缩包。
![](https://main.qcloudimg.com/raw/0ae70c8558f0a07a04d72554004faa76.png)
2. 将压缩包解压得到 `protoc` 和 `grpc_csharp_plugin` 可执行程序。
![](https://main.qcloudimg.com/raw/026e83a43d6d3d078d7d2acc12771827.png)
[](id:test3)
3. 拷贝 `protoc` 和 `grpc_csharp_plugin` 可执行程序到和 Protobuf 文件同一目录下，并在该目录下执行以下两条命令生成 `C#` 代码：
 -  **MAC 和 Linux 环境命令如下：**
    - `protoc -I ./ --csharp_out=. GseGrpcSdkService.proto --grpc_out=. --plugin=protoc-gen-grpc=grpc_csharp_plugin`
    - ` protoc -I ./ --csharp_out=. GameServerGrpcSdkService.proto --grpc_out=. --plugin=protoc-gen-grpc=grpc_csharp_plugin`
 - **Windows 环境命令如下：**
    - ` ./protoc -I ./ --csharp_out=. GseGrpcSdkService.proto --grpc_out=. --plugin=protoc-gen-grpc=grpc_csharp_plugin.exe `
    - ` ./protoc -I ./ --csharp_out=. GameServerGrpcSdkService.proto --grpc_out=. --plugin=protoc-gen-grpc=grpc_csharp_plugin.exe`
 
 如下图所示生成四个 `.cs` 代码文件。
  ![](https://main.qcloudimg.com/raw/dad39ec6bfabea5ee2025b83596fc711.png)

### 步骤3：Unity 服务端开发使用 GSE SDK

将 [步骤2](#test2) 中生成的四个 `.cs` 文件拷贝到 Unity 项目中（可以拷贝到 Assets/Scripts/目录下单独的文件夹中），便可使用 GSE SDK 进行开发，详情可参见 [Unity DEMO](#test5)。
1. 实现 `gameserver_grpcsdk_service.proto` 定义的三个接口 `OnHealthCheck`、`OnStartGameServerSession` 和 ` OnProcessTerminate` 。
```JavaScript
public class GrpcServer : GameServerGrpcSdkService.GameServerGrpcSdkServiceBase
{
	private static Logs logger
	{
		get
		{
			return new Logs();
		}
	}
	// 健康检查
	public override Task<HealthCheckResponse> OnHealthCheck(HealthCheckRequest request, ServerCallContext context)
	{
		logger.Println($"OnHealthCheck, HealthStatus: {GseManager.HealthStatus}");
		logger.Println($"OnHealthCheck, GameServerSession: {GseManager.GetGameServerSession()}");
		return Task.FromResult(new HealthCheckResponse
		{
				HealthStatus = GseManager.HealthStatus
		});
	}
	// 接收游戏会话
	public override Task<GseResponse> OnStartGameServerSession(StartGameServerSessionRequest request, ServerCallContext context)
	{
		logger.Println($"OnStartGameServerSession, request: {request}");
		GseManager.SetGameServerSession(request.GameServerSession);
		var resp = GseManager.ActivateGameServerSession(request.GameServerSession.GameServerSessionId, request.GameServerSession.MaxPlayers);
		logger.Println($"OnStartGameServerSession, resp: {resp}");
		return Task.FromResult(resp);
	}    
	// 结束游戏进程
	public override Task<GseResponse> OnProcessTerminate(ProcessTerminateRequest request, ServerCallContext context)
	{
		logger.Println($"OnProcessTerminate, request: {request}");
		// 设置进程终止时间
		GseManager.SetTerminationTime(request.TerminationTime);
		// 终止游戏服务器会话
		GseManager.TerminateGameServerSession();
		// 进程退出
		GseManager.ProcessEnding();
		return Task.FromResult(new GseResponse());
	}
}
```
2. 开发 Unity 服务端程序（以 ChatServer 为例）。 
```JavaScript
public static void StartChatServer(int clientPort)
{
	RegisterHandlers();
	logger.Println("ChatServer Listen at " + clientPort);
	NetworkServer.Listen(clientPort);
}
```
3. 开发 gRPC 服务端。
```JavaScript
public static void StartGrpcServer(int clientPort, int grpcPort, string logPath)
{
	try
	{
		 Server server = new Server
		 {
			Services = { GameServerGrpcSdkService.BindService(new GrpcServer()) },
			Ports = { new ServerPort("127.0.0.1", grpcPort, ServerCredentials.Insecure) },
		 };
			server.Start();
			logger.Println("GrpcServer Start On localhost:" + grpcPort);
			GseManager.ProcessReady(new string[] { logPath }, clientPort, grpcPort);
	}
	catch (System.Exception e)
	{
		 logger.Println("error: " + e.Message);
	}
}
```
4. 启动开发者本身实现的服务端和 gRPC 服务端。
```JavaScript
public class StartServers : MonoBehaviour
{
	private int grpcPort = PortServer.GenerateRandomPort(2000, 6000);
	private int chatPort = PortServer.GenerateRandomPort(6001, 10000);
	private const string logPath = "./log/log.txt";
	// Start is called before the first frame update
	[Obsolete]
	void Start()
	{
		 // Start ChatServer By UNet's NetWorkServer, Listen on UDP protocol
		 MyChatServer.StartChatServer(chatPort);
		 // Start GrpcServer By Grpc, Listen on TCP protocol
		 MyGrpcServer.StartGrpcServer(chatPort, grpcPort, logPath);
	}
	[Obsolete]
	void OnGUI()
	{
	}
}
```

[](id:test5)
##	Unity DEMO
1.	[单击这里]( https://gsegrpcdemo-1301007756.cos.ap-guangzhou.myqcloud.com/unity-demo.zip)，您可以下载 Unity DEMO代码。
2.	导入 grpc unity package。
   将 [步骤2](#test2) 中  grpc_unity_package 解压到 Demo 工程 unity-demo/Assets 目录下。
3.	根据 [Protobuf](#test3) 文件生成 C# 代码。
4.	启动服务端，供 GSE 调用。
 - 服务端实现，在 `unity-demo/Assets/Scripts/Api` 目录下的 `GrpcServer.cs` 文件中实现服务端的三个接口。
 - 服务端运行，在 `unity-demo/Assets/Scripts` 目录下的 `MyGrpcServer.cs` 文件中，创建 `gRPC Server`， `StartServers.cs` 从而启动 `gRPC Server`。
5.	客户端连接 GSE 的 gRPC 服务端。
 - 客户端实现，在 `unity-demo/Assets/Scripts/Gsemanager` 目录下的 `Gsemanager.cs` 文件实现客户端的九个接口。
 - 连接服务端，创建一个 gRPC channel，指定要连接的主机和服务器端口，然后使用此 channel 创建存根实例。
6.	编译运行。
   使用 Unity Editor 打包目标系统的可执行程序，并打包为生成包，启动路径配置可执行程序名（需根据实际的可执行程序名称填写）。

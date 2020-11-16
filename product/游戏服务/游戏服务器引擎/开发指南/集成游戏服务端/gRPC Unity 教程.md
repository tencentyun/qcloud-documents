本文介绍使用 Unity 接入 GSE SDK 的完整过程，主要包括两方面工作：
1.Unity 接入 gRPC。
2.Unity 接入 GSE SDK。

## 前提条件
已安装 Unity Hub、Unity IDE。
>!文本基于 Unity 引擎 v2018.3.5f1 版本。

## Unity 接入 gRPC

目前 Unity 接入 gRPC 处于内测阶段，更多信息可参见 [README](https://github.com/grpc/grpc/tree/master/src/csharp/experimental)。具体操作步骤如下：

### 步骤1：创建 Unity 项目 

需要创建一个针对 `.NET 4.x` 同等效果版本的 Unity 项目，由于 gRPC 使用的 API 仅在 `.NET 4.5+`可用，所以这一步是必需的，通过【Edit】>【Project Setting】>【Player】>【Configuration】>【Scripting Runtime Version】进行设置。
![](https://main.qcloudimg.com/raw/c28d0dc10bded3be2e98358a95a374fa.jpg)

<span id="test"></span>
### 步骤2：下载grpc_unity_package

下载 `grpc_unity_package.VERSION.zip` 的 [最新开发版本](https://packages.grpc.io/)。单击 `Buidld ID` 跳转到下载页面。
![](https://main.qcloudimg.com/raw/9ac9fa93e7de83042e1771cf0c4e6379.jpg)
单击 `c#` 目录下的 `grpc_unity_package.VERSION.zip` 即可下载成功。
![](https://main.qcloudimg.com/raw/8aa7bbbb7ab6076f28e711bc3bd92907.jpg)

### 步骤3： 解压

将下载的``` .zip```文件解压到 Unity 项目的```Assets``` 目录中，如下图所示
![](https://main.qcloudimg.com/raw/3d319f3b4acbf2dea17f09e704e083fe.png)

### 步骤4：测试 

Unity IDE 将取出文件并自动添加到项目中，您即可在代码中使用 gRPC 和 Protobuf，如果 Unity IDE 提示错误，详情可参见 [常见问题](#test1)。

## Unity 接入 GSE SDK

Unity 接入 GSE SDK 包括以下几个步骤：

### 步骤1： 获取 GSE SDK Protobuf 文件

获取 GSE SDK Protobuf 文件 `GameServerGrpcSdkService.proto` 和 `GseGrpcSdkService.proto`，详情可参见 [proto 文件](https://cloud.tencent.com/document/product/1165/46111)。
<span id="test2"></span>
### 步骤2： 根据 Protobuf 生成 C# 代码
1. 下载 gRPC protoc Plugin，再次访问下载 [grpc_unity_package.VERSION.zip](#test) 页面，下载对应操作系统的 protoc 压缩包
![](https://main.qcloudimg.com/raw/0ae70c8558f0a07a04d72554004faa76.png)
2. 将压缩包解压得到 `protoc` 和 `grpc_csharp_plugin` 可执行程序。
![](https://main.qcloudimg.com/raw/026e83a43d6d3d078d7d2acc12771827.png)
3. 拷贝 `protoc` 和 `grpc_csharp_plugin` 可执行程序到和 Protobuf 文件同一目录下，并在该目录下执行以下两条命令生成 `C#` 代码：
 - `protoc -I ./ --csharp_out=. GseGrpcSdkService.proto --grpc_out=. --plugin=protoc-gen-grpc=grpc_csharp_plugin`
 - ` protoc -I ./ --csharp_out=. GameServerGrpcSdkService.proto --grpc_out=. --plugin=protoc-gen-grpc=grpc_csharp_plugin`
windows 下命令为
 - ` ./protoc -I ./ --csharp_out=. GseGrpcSdkService.proto --grpc_out=. --plugin=protoc-gen-grpc=grpc_csharp_plugin.exe `
 - ` ./protoc -I ./ --csharp_out=. GameServerGrpcSdkService.proto --grpc_out=. --plugin=protoc-gen-grpc=grpc_csharp_plugin.exe`
 
  ![](https://main.qcloudimg.com/raw/dad39ec6bfabea5ee2025b83596fc711.png)

### 步骤3： Unity 服务端开发使用 GSE SDK

将 [步骤2](#test2) 中生成的四个 `.cs` 文件拷贝到 Unity 项目中（可以拷贝到 Assets/Scripts/目录下单独的文件夹中），便可使用 GSE SDK 进行开发，可参考unity-demo（demo中未导入解压后的gRPC文件，仅包含示例代码）
首先用户需要实现 ```gameserver_grpcsdk_service.proto``` 定义的三个接口 ```OnHealthCheck```、```OnStartGameServerSession``` 和``` OnProcessTerminate``` .


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

其次用户需要开发自己的Unity服务端程序（以ChatServer为例）  



		 public static void StartChatServer(int clientPort)
				{
						RegisterHandlers();
						logger.Println("ChatServer Listen at " + clientPort);
						NetworkServer.Listen(clientPort);
				}

再次开发 gRPC 服务端


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

最后启动用户自己实现的服务端和gRPC服务端  


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
	
				void OnGUI()
				{
				}
		}  


## 常见问题
<span id="test1"></span>
### 将下载的` grpc_unity_package.VERSION.zip` 文件解压到Unity项目中后，Unity IDE报错 （如<u>[ 缺陷22251](https://github.com/grpc/grpc/issues/22251)</u> 中描述）：

```` 
 1. Error: Could not load signature of Google.Protobuf.ByteString:get_Span due to:Could not load file or assembly 'System.Memory, Version=4.0.1.0, Culture=neutral, PublicKeyToken=' or one of its dependencies. assembly:System.Memory, Version=4.0.1.0, Culture=neutral, PublicKeyToken= type:<unknown type> member:(null) signature:
 2. Unloading broken assembly Assets/Plugins/Google.Protobuf/lib/net45/Google.Protobuf.dll, this assembly can cause crashes in the runtime
````

解决办法：下载 2.26 版本```  grpc_unity_package.2.26.0-dev.zip``` 并解压，<u>[下载地址](https://packages.grpc.io/archive/2019/12/a02d6b9be81cbadb60eed88b3b44498ba27bcba9-edd81ac6-e3d1-461a-a263-2b06ae913c3f/index.xml)</u>

### 打包 MacOS 服务端程序，运行时可能出现以下错误：```error: grpc_csharp_ext```![](https://main.qcloudimg.com/raw/703dc0dd20342b4aff5d499f2ac1df85.png)
解决办法：重命名路径 ```Assert/Plugins/Grpc.Core/runtimes/osx/x64 ```下文件 ```grpc_csharp_ext.bundle``` 为``` grpc_csharp_ext```，拷贝到路径 ```YourUnityApp.app/Contents/Frameworks/MonoEmbedRuntime/osx``` 下，路径中不存在的目录新建即可

### 打包 Linux 服务端程序，运行时可能出现以下错误：```Unable to preload the following plugins: ScreenSelector.so```
![](https://main.qcloudimg.com/raw/f2926b2ac676f2e1e1ce85b8bae397f1.png)
解决办法：Unity Editor 中，```File -> Build Settings.. ```勾选 ```Server Build```，重新打包
![](https://main.qcloudimg.com/raw/3ffa6a320c4269669c411f32cf7597f0.png)



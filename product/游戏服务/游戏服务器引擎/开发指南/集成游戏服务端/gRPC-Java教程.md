
## 安装 gRPC
1. Java gRPC 除了 JDK 外不需要其他工具。
2. 在本地安装 gRPC Java 库 SNAPSHOT，包括代码生成插件。
<dx-alert infotype="explain" title="">
具体安装流程请您参考 [安装 gRPC Java的说明](https://github.com/grpc/grpc-java/blob/master/COMPILING.md)。
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
 - 方法一：在 java-demo/src/main/proto 下执行脚本，需要从 gprc 官网下载 protoc 和 protoc-gen-grpc-java 生成工具：
```
sh gen_pb.sh
```
```
protoc --java_out=../java --proto_path=. GameServerGrpcSdkService.proto
protoc --plugin=protoc-gen-grpc-java=`which protoc-gen-grpc-java` --grpc-java_out=../java --proto_path=. GameServerGrpcSdkService.proto
protoc --java_out=../java --proto_path=. GseGrpcSdkService.proto
protoc --plugin=protoc-gen-grpc-java=`which protoc-gen-grpc-java` --grpc-java_out=../java --proto_path=. GseGrpcSdkService.proto
```    
 - 方法二：使用 maven 工具生成 gRPC 代码，在 maven 中增加编译 grpc 代码的 maven 插件，详细信息请您参考 [gRPC-Java-RPC 库和框架](https://github.com/grpc/grpc-java)。
<dx-codeblock>
:::  Java
<build>
	 <extensions>
	 <extension>
		<groupId>kr.motd.maven</groupId>
		<artifactId>os-maven-plugin</artifactId>
		<version>1.6.2</version>
	 </extension>
	 </extensions>
	 <plugins>
	 <plugin>
		<groupId>org.xolstice.maven.plugins</groupId>
		<artifactId>protobuf-maven-plugin</artifactId>
		<version>0.6.1</version>
		<configuration>
			<protocArtifact>com.google.protobuf:protoc:3.12.0:exe:${os.detected.classifier}</protocArtifact>
			<pluginId>grpc-java</pluginId>
			<pluginArtifact>io.grpc:protoc-gen-grpc-java:1.30.2:exe:${os.detected.classifier}</pluginArtifact>
		</configuration>
		<executions>
			<execution>
			<goals>
				<goal>compile</goal>
				<goal>compile-custom</goal>
			</goals>
		 </execution>
		 </executions>
	 </plugin>
	</plugins>
</build>
:::
</dx-codeblock>


## 游戏进程集成流程
![](https://qcloudimg.tencent-cloud.cn/raw/2ece2bd5732ff6fa39b80554c7beb7d1.png)

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
```Java
public GseResponseBo processReady(ProcessReadyRequestBo request) {
	logger.info("processReady request=" + new Gson().toJson(request));
	GseResponseBo responseBo = new GseResponseBo();
	GseGrpcSdkServiceOuterClass.ProcessReadyRequest rpcRequest = GseGrpcSdkServiceOuterClass.ProcessReadyRequest
					//设置端口。
					.newBuilder().setClientPort(request.getClientPort())
					.setGrpcPort(request.getGrpcPort())
					//日志路径。
					.addAllLogPathsToUpload(request.getLogPathsToUploadList()).build();

	GseGrpcSdkServiceOuterClass.GseResponse rpcResponse;
	try {
			rpcResponse = getGseGrpcSdkServiceClient().processReady(rpcRequest);
	} catch (StatusRuntimeException e) {
			logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
			return createRpcFailedResponseBo(e.getStatus());
	}
	//准备就绪，可对外提供服务。
	logger.info("processReady response=" + rpcResponse.toString());
	return createResponseBoByRpcResponse(rpcResponse);
}
```
 2. 进程准备就绪后，GSE 调用 OnHealthCheck 接口，对 Game Server 进行健康检查，每1分钟检查1次，连续3次失败就判定该进程不健康，不会分配游戏服务器会话至该进程。
```Java
public boolean onHealthCheck() {
	//添加游戏服务器逻辑以进行健康检查。
	boolean res = getGrpcServiceConfig().getGseGrpcSdkServiceClient().isProcessHealth();
	logger.info("onHealthCheck status=" + res);
	return res;
}
```
 3. 因为 Client 调用 [CreateGameServerSession](https://cloud.tencent.com/document/product/1165/42067) 接口创建一个游戏服务器会话，将该游戏服务器会话分配给一个进程，所以触发 GSE 调用该进程的 onStartGameServerSession 接口，并且将 GameServerSession 状态更改为“激活中”。
```Java
public GseResponseBo onStartGameServerSession(GameServerSessionBo gameServerSessionBo) {
	logger.info("onStartGameServerSession gameServerSession=" + new Gson().toJson(gameServerSessionBo));
	//添加用于启动游戏服务器会话的游戏服务端逻辑。

	//保存游戏服务器会话。
	getGrpcServiceConfig().getGseGrpcSdkServiceClient().onStartGameServerSession(gameServerSessionBo);
	//激活游戏服务器会话。
	ActivateGameServerSessionRequestBo activateRequest = new ActivateGameServerSessionRequestBo();
	activateRequest.setGameServerSessionId(gameServerSessionBo.getGameServerSessionId());
	activateRequest.setMaxPlayers(gameServerSessionBo.getMaxPlayers());
	getGrpcServiceConfig().getGseGrpcSdkServiceClient().activateGameServerSession(activateRequest);

	//在此处添加最终逻辑。
	return createResponseBo(0, "SUCCESS");
}
```
 4. 当 Game Server 收到 onStartGameServerSession，您自行处理一些逻辑或资源分配，准备就绪后，Game Server 就调用 ActivateGameServerSession 接口,通知 GSE 游戏服务器会话已分配给一个进程，现在已准备好接收玩家请求，将服务器状态更改为“活跃”。
```Java
public GseResponseBo activateGameServerSession(ActivateGameServerSessionRequestBo request) {
	logger.info("activateGameServerSession request=" + new Gson().toJson(request));
	if (gameServerSessionBo == null) {
			return createResponseBo(Constants.gameServerSessionExpectCode, "no game server session found.");
	}
	GseResponseBo responseBo = new GseResponseBo();
	GseGrpcSdkServiceOuterClass.ActivateGameServerSessionRequest rpcRequest = GseGrpcSdkServiceOuterClass.ActivateGameServerSessionRequest
					.newBuilder().setMaxPlayers(request.getMaxPlayers())
					.setGameServerSessionId(gameServerSessionBo.getGameServerSessionId()).build();

	GseGrpcSdkServiceOuterClass.GseResponse rpcResponse;
	try {
			rpcResponse = getGseGrpcSdkServiceClient().activateGameServerSession(rpcRequest);
	} catch (StatusRuntimeException e) {
			logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
			return createRpcFailedResponseBo(e.getStatus());
	}
	logger.info("activateGameServerSession response=" + rpcResponse.toString());
	return createResponseBoByRpcResponse(rpcResponse);
}
```
 5. 当 Client 调用 [JoinGameServerSession](https://cloud.tencent.com/document/product/1165/42061) 接口玩家加入后，Game Server 调用 AcceptPlayerSession 接口验证玩家合法性，如果连接被接受，则将 PlayerSession 状态设置为“活跃”。如果 Client 调用 JoinGameServerSession 接口在60秒内未收到响应，则将 PlayerSession 状态更改为“超时”，然后重新调用 JoinGameServerSession。
```Java
public GseResponseBo acceptPlayerSession(PlayerSessionRequestBo request) {
	logger.info("acceptPlayerSession request=" + new Gson().toJson(request));
	if (gameServerSessionBo == null) {
			return createResponseBo(Constants.gameServerSessionExpectCode, "no game server session found.");
	}
	GseResponseBo responseBo = new GseResponseBo();
	GseGrpcSdkServiceOuterClass.AcceptPlayerSessionRequest rpcRequest = GseGrpcSdkServiceOuterClass.AcceptPlayerSessionRequest
					.newBuilder().setGameServerSessionId(gameServerSessionBo.getGameServerSessionId())
					.setPlayerSessionId(request.getPlayerSessionId()).build();

	GseGrpcSdkServiceOuterClass.GseResponse rpcResponse;
	try {
			rpcResponse = getGseGrpcSdkServiceClient().acceptPlayerSession(rpcRequest);
	} catch (StatusRuntimeException e) {
			logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
			return createRpcFailedResponseBo(e.getStatus());
	}
	logger.info("acceptPlayerSession response=" + rpcResponse.toString());
	return createResponseBoByRpcResponse(rpcResponse);
}
```
 6. 游戏结束或者玩家退出后，Game Server 调用 RemovePlayerSession 接口移除玩家，将 playersession 状态更改为“已完成” ，并预留游戏服务器会话中的玩家位置。
```Java
public GseResponseBo removePlayerSession(PlayerSessionRequestBo request) {
	logger.info("removePlayerSession request=" + new Gson().toJson(request));
	if (gameServerSessionBo == null) {
			return createResponseBo(Constants.gameServerSessionExpectCode, "no game server session found.");
	}
	GseResponseBo responseBo = new GseResponseBo();
	GseGrpcSdkServiceOuterClass.RemovePlayerSessionRequest rpcRequest = GseGrpcSdkServiceOuterClass.RemovePlayerSessionRequest
					.newBuilder().setGameServerSessionId(gameServerSessionBo.getGameServerSessionId())
					.setPlayerSessionId(request.getPlayerSessionId()).build();

	GseGrpcSdkServiceOuterClass.GseResponse rpcResponse;
	try {
			rpcResponse = getGseGrpcSdkServiceClient().removePlayerSession(rpcRequest);
	} catch (StatusRuntimeException e) {
			logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
			return createRpcFailedResponseBo(e.getStatus());
	}
	logger.info("removePlayerSession response=" + rpcResponse.toString());
	return createResponseBoByRpcResponse(rpcResponse);
}
```
 7. 当一个游戏服务器会话（一组游戏对局或一个服务）结束后，Game Server 调用 TerminateGameServerSession 接口结束 GameServerSession，将 GameServerSession 状态更改为“已终止”。
```Java
public GseResponseBo terminateGameServerSession(String gameServerSessionId) {
	logger.info("terminateGameServerSession request=" + gameServerSessionId);
	if (StringUtils.isEmpty(gameServerSessionId) && gameServerSessionBo != null
					&& !StringUtils.isEmpty(gameServerSessionBo.getGameServerSessionId())) {
			gameServerSessionId = gameServerSessionBo.getGameServerSessionId();
	}
	if (StringUtils.isEmpty(gameServerSessionId)) {
			return createResponseBo(Constants.gameServerSessionExpectCode, "no game server session found.");
	}
	GseResponseBo responseBo = new GseResponseBo();
	GseGrpcSdkServiceOuterClass.TerminateGameServerSessionRequest rpcRequest = GseGrpcSdkServiceOuterClass.TerminateGameServerSessionRequest
					.newBuilder().setGameServerSessionId(gameServerSessionId).build();

	GseGrpcSdkServiceOuterClass.GseResponse rpcResponse;
	try {
			rpcResponse = getGseGrpcSdkServiceClient().terminateGameServerSession(rpcRequest);
	} catch (StatusRuntimeException e) {
			logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
			return createRpcFailedResponseBo(e.getStatus());
	}
	logger.info("terminateGameServerSession response=" + rpcResponse.toString());
	return createResponseBoByRpcResponse(rpcResponse);
}
```
 8. 当健康检查失败或缩容时，GSE 调用 OnProcessTerminate 接口结束游戏进程，缩容时依据是您在 GSE 控制台配置的 [保护策略](https://cloud.tencent.com/document/product/1165/41028#test12)。
```Java
public GseResponseBo onProcessTerminate(long terminationTime) {
	logger.info("onProcessTerminate terminationTime=" + terminationTime);
	//现在可能结束游戏服务端。

	return createResponseBo(0, "SUCCESS");
}
```
 9. Game Server 调用 ProcessEnding 接口会立刻结束进程，将服务器进程状态更改为“已终止”，并回收资源。
```Java
//主动调用：一局游戏对应一个进程，当一局游戏结束后主动调用 ProcessEnding 接口
//被动调用：当缩容或进程异常健康检查失败时，根据保护策略被动调用 ProcessEnding 接口，配置完全保护和时限保护策略时需要先判断游戏服务器会话上有无玩家，再被动调用
public GseResponseBo processEnding() {
	logger.info("processEnding begin");
	GseResponseBo responseBo = new GseResponseBo();
	GseGrpcSdkServiceOuterClass.ProcessEndingRequest rpcRequest = GseGrpcSdkServiceOuterClass.ProcessEndingRequest
					.newBuilder().build();

	GseGrpcSdkServiceOuterClass.GseResponse rpcResponse;
	try {
			rpcResponse = getGseGrpcSdkServiceClient().processEnding(rpcRequest);
	} catch (StatusRuntimeException e) {
			logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
			return createRpcFailedResponseBo(e.getStatus());
	}
	logger.info("processEnding response=" + rpcResponse.toString());
	return createResponseBoByRpcResponse(rpcResponse);
}
```
 10. Game Server 调用 DescribePlayerSessions 接口获取游戏服务器会话下的玩家信息（根据业务可选）。
```Java
public DescribePlayerSessionsResponseBo describePlayerSessions(DescribePlayerSessionsRequestBo request) {
	logger.info("describePlayerSessions request=" + new Gson().toJson(request));
	if (StringUtils.isEmpty(request.getGameServerSessionId()) &&
					gameServerSessionBo != null && !StringUtils.isEmpty(gameServerSessionBo.getGameServerSessionId())) {
			request.setGameServerSessionId(gameServerSessionBo.getGameServerSessionId());
	}
	GseGrpcSdkServiceOuterClass.DescribePlayerSessionsRequest rpcRequest = GseGrpcSdkServiceOuterClass.DescribePlayerSessionsRequest
					.newBuilder().setGameServerSessionId(request.getGameServerSessionId())
					.setLimit(request.getLimit())
					.setNextToken(request.getNextToken())
					.setPlayerId(request.getPlayerId())
					.setPlayerSessionId(request.getPlayerSessionId())
					.setPlayerSessionStatusFilter(request.getPlayerSessionStatusFilter()).build();

	GseGrpcSdkServiceOuterClass.DescribePlayerSessionsResponse rpcResponse;
	try {
			rpcResponse = getGseGrpcSdkServiceClient().describePlayerSessions(rpcRequest);
	} catch (StatusRuntimeException e) {
			logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
			return null;
	}
	logger.info("describePlayerSessions response=" + rpcResponse.toString());
	return toPlayerSessionsResponseBo(rpcResponse);
}
```
 11. Game Server 调用 UpdatePlayerSessionCreationPolicy 接口更新玩家会话的创建策略，设置是否接受新玩家，即游戏会话里是否允许加入人（根据业务可选）。
```Java
public GseResponseBo updatePlayerSessionCreationPolicy(UpdatePlayerSessionCreationPolicyRequestBo request) {
	logger.info("updatePlayerSessionCreationPolicy request=" + new Gson().toJson(request));
	if (gameServerSessionBo == null) {
			return createResponseBo(Constants.gameServerSessionExpectCode, "no game server session found.");
	}
	GseResponseBo responseBo = new GseResponseBo();
	GseGrpcSdkServiceOuterClass.UpdatePlayerSessionCreationPolicyRequest rpcRequest = GseGrpcSdkServiceOuterClass.UpdatePlayerSessionCreationPolicyRequest
					.newBuilder().setGameServerSessionId(gameServerSessionBo.getGameServerSessionId())
					.setNewPlayerSessionCreationPolicy(request.getNewPlayerSessionCreationPolicy()).build();

	GseGrpcSdkServiceOuterClass.GseResponse rpcResponse;
	try {
			rpcResponse = getGseGrpcSdkServiceClient().updatePlayerSessionCreationPolicy(rpcRequest);
	} catch (StatusRuntimeException e) {
			logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
			return createRpcFailedResponseBo(e.getStatus());
	}
	logger.info("updatePlayerSessionCreationPolicy response=" + rpcResponse.toString());
	return createResponseBoByRpcResponse(rpcResponse);
}
```
 12. Game Server 调用 ReportCustomData 接口告知 GSE 的自定义数据（根据业务可选）。
```Java
public GseResponseBo reportCustomData(ReportCustomDataRequestBo request) {
	logger.info("reportCustomData request=" + new Gson().toJson(request));
	GseResponseBo responseBo = new GseResponseBo();
	GseGrpcSdkServiceOuterClass.ReportCustomDataRequest rpcRequest = GseGrpcSdkServiceOuterClass.ReportCustomDataRequest
					.newBuilder()
					.setCurrentCustomCount(request.getCurrentCustomCount())
					.setMaxCustomCount(request.getMaxCustomCount()).build();

	GseGrpcSdkServiceOuterClass.GseResponse rpcResponse;
	try {
			rpcResponse = getGseGrpcSdkServiceClient().reportCustomData(rpcRequest);
	} catch (StatusRuntimeException e) {
			logger.log(Level.WARNING, "RPC failed: {0}", e.getStatus());
			return createRpcFailedResponseBo(e.getStatus());
	}
	logger.info("reportCustomData response=" + rpcResponse.toString());
	return createResponseBoByRpcResponse(rpcResponse);
}
```

## 启动服务端，供 GSE 调用
服务端运行：将 GrpcServer 启动起来。
 ```Java
@Bean(name = "grpcService", initMethod = "startup", destroyMethod = "shutdown")
	public GrpcService getGrpcService() {
		GrpcServiceConfig grpcServiceConfig = new GrpcServiceConfig();
		grpcServiceConfig.setGseGrpcSdkServiceClient(gseGrpcSdkServiceClient);
		grpcServiceConfig.setGameServerGrpcPort(gameServerGrpcPort);
		grpcServiceConfig.setGameServerToClientPort(gameServerToClientPort);
		grpcServiceConfig.setTargetAddress(targetAddress);
		grpcServiceConfig.setGameServerUploadLogPath(gameServerUploadLogPath);
		GrpcService grpcService = new GrpcService(grpcServiceConfig);
		return grpcService;
}
```

## 客户端连接 GSE 的 gRPC 服务端
连接服务端：创建一个 gRPC 频道，指定我们要连接的主机名和服务器端口，然后用这个频道创建存根实例。
```java
public GseGrpcSdkServiceGrpc.GseGrpcSdkServiceBlockingStub getGseGrpcSdkServiceClient() {     
	// 这里的 “channel” 是一个频道，而不是 ManagedChannel，因此，此代码的职责不是关掉它。
	//将频道传递给代码，使代码更易于测试和重用频道。
	if (blockingStub == null) {
			managedChannel = getGrpcChannel(targetAddress);
			blockingStub = GseGrpcSdkServiceGrpc.newBlockingStub(managedChannel);
	}
	if (managedChannel.isShutdown() || managedChannel.isTerminated()) {
			managedChannel.shutdownNow();
			managedChannel = getGrpcChannel(targetAddress);
			blockingStub = GseGrpcSdkServiceGrpc.newBlockingStub(managedChannel);
	}
	return blockingStub;
}
```
## Java DEMO
 1. [单击这里](https://gsegrpcdemo-1301007756.cos.ap-guangzhou.myqcloud.com/java-demo.zip)，您可下载 Java DEMO 代码。
 2. 生成 gRPC 代码。
Java DEMO 代码示例里已生成 gRPC 代码，在 java-demo/src/main/java/tencentcloud 目录下，不需要额外生成。
 3. 启动服务端，供 GSE 调用。
  - 服务端实现。
在 java-demo/src/main/java/com/tencentcloud/gse/gameserver/service/gamelogic/impl 目录下的 GameServerGrpcCallbackImpl.java，实现了服务端的三个接口。
  - 服务端运行。
在 java-demo/src/main/java/com/tencentcloud/gse/gameserver/config 目录下的 GameServerConfig.java，将 GrpcServer 启动起来。
 4. 客户端连接 GSE 的 gRPC 服务端。
  - 客户端实现。
在 java-demo/src/main/java/com/tencentcloud/gse/gameserver/service/gsegrpc/impl 目录下的 GseGrpcSdkServiceClientImpl.java，实现了客户端的九个接口。
  - 连接服务端。
创建一个 gRPC 频道，指定我们要连接的主机名和服务器端口，然后用这个频道创建存根实例。
 5. 编译运行。
  1. 安装 Java 版本要求1.8及以上，linux 下可以使用 yum 安装 openjdk：
```
yum install -y java-1.8.0-openjdk
```
- 将代码下载，在 java-demo 目录下，使用 maven 构建生成 gse-gameserver-demo.jar，使用如下命令启动：
   ```
   java -jar gse-gameserver-demo.jar
   ``` 
- 将可执行文件 gse-gameserver-demo.jar 打包为 [生成包](https://cloud.tencent.com/document/product/1165/41030)，启动路径配置 java，启动参数配置 jar gse-gameserver-demo.jar。
- 然后 [创建服务器舰队](https://cloud.tencent.com/document/product/1165/41028)，将生成包部署在服务器舰队上，后续可进行 [扩缩容](https://cloud.tencent.com/document/product/1165/45709) 等一系列操作。


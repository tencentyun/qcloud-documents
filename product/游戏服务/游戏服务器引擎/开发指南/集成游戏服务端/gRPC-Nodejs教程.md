
## 安装 gRPC
1. 前提条件：安装 Nodejs 版本，不低于 v12.16.0。
2. 安装 gRPC。
<dx-alert infotype="explain" title="">
具体流程请您参考 [安装 gRPC Nodejs 的说明](https://github.com/grpc/grpc/tree/master/examples/node)。
</dx-alert>


## 定义服务

gRPC 通过 protocol buffers 实现定义一个服务：一个 RPC 服务通过参数和返回类型来指定可以远程调用的方法。
<dx-alert infotype="explain" title="">
我们提供定义服务的 proto 文件，请您在 [proto 文件](https://cloud.tencent.com/document/product/1165/46111) 里下载使用，无需自己生成。
</dx-alert>



## 生成 gRPC 代码
1. 定义好服务后，通过 protocol buffer 编译器 protoc 生成客户端和服务端的代码（任意 gRPC 支持的语言）。 
2. 生成的代码包括客户端的存根和服务端要实现的抽象接口。
3. 生成 gRPC 代码。
  Nodejs 版本使用 grpc/proto-loader 直接加载 pb 文件，不需要生成 gRPC-nodejs 代码。

## 游戏进程集成流程
![](https://qcloudimg.tencent-cloud.cn/raw/50d828929219826bc83f7a2be78e6c71.png)

#### Game Server 回调接口列表

| 接口名称 | 接口功能|
|-----|----|
|[OnHealthCheck](https://cloud.tencent.com/document/product/1165/46116)| 健康检查|
|[OnStartGameServerSession](https://cloud.tencent.com/document/product/1165/46118)|接收游戏服务器会话|
|[OnProcessTerminate](https://cloud.tencent.com/document/product/1165/46121)|结束游戏进程|

####  Game Server 主调接口列表

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
function ProcessReady(param) {
		console.log("ProcessReady.request", param);
		getGseGrpcSdkServiceClient().ProcessReady({
				//日志路径
				logPathsToUpload: param.logPathsToUpload,
				//设置端口
				clientPort: param.clientPort,
				grpcPort: param.grpcPort
		}, getMetadata(), function (err, response) {
				//准备就绪，可对外提供服务
				console.log('ProcessReady.response:', err, response);
		});
}
```
 2. 进程准备就绪后，GSE 调用 OnHealthCheck 接口，对 Game Server 进行健康检查，每1分钟检查1次，连续3次失败就判定该进程不健康，不会分配游戏服务器会话至该进程。
```
function OnHealthCheck(call, callback) {
		console.log("OnHealthCheck.request", call.request);

		callback(null, {healthStatus: gsesdkClient.IsProcessHealth() });
}
```
 3. 因为 Client 调用 [CreateGameServerSession](https://cloud.tencent.com/document/product/1165/42067) 接口创建一个游戏服务器会话，将该游戏服务器会话分配给一个进程，所以触发 GSE 调用该进程的 onStartGameServerSession 接口，并且将 GameServerSession 状态更改为“激活中”。
```
function OnStartGameServerSession(call, callback) {
		console.log("OnStartGameServerSession.request", call.request);
		gsesdkClient.OnStartGameServerSession(call.request);
		callback(null, {});
}
```
 4. 当 Game Server 收到 onStartGameServerSession，您自行处理一些逻辑或资源分配，准备就绪后，Game Server 就调用 ActivateGameServerSession 接口,通知 GSE 游戏服务器会话已分配给一个进程，现在已准备好接收玩家请求，将服务器状态更改为“活跃”。
```
function ActivateGameServerSession(param, w, callback) {
		console.log("ActivateGameServerSession.request", param);
		getGseGrpcSdkServiceClient().ActivateGameServerSession({
				gameServerSessionId: gameServerSession.gameServerSessionId,
				maxPlayers: param.maxPlayers
		}, getMetadata(), function (err, response) {
				console.log('ActivateGameServerSession.response:', err, response);
				if (callback != null) {
						callback(w, response);
				}
		});
}
```
 5. 当 Client 调用 [JoinGameServerSession](https://cloud.tencent.com/document/product/1165/42061) 接口玩家加入后，Game Server 调用 AcceptPlayerSession 接口验证玩家合法性，如果连接被接受，则将 PlayerSession 状态设置为“活跃”。如果 Client 调用 JoinGameServerSession 接口在60秒内未收到响应，则将 PlayerSession 状态更改为“超时”，然后重新调用 JoinGameServerSession。
```
function AcceptPlayerSession(param, w, callback) {
		console.log("AcceptPlayerSession.request", param);
		getGseGrpcSdkServiceClient().AcceptPlayerSession({
				gameServerSessionId: gameServerSession.gameServerSessionId,
				playerSessionId: param.playerSessionId
		}, getMetadata(), function (err, response) {
				console.log('AcceptPlayerSession.response:', err, response);
				if (callback != null) {
						callback(w, response);
				}
		});
}
```
 6. 游戏结束或者玩家退出后，Game Server 调用 RemovePlayerSession 接口移除玩家，将 playersession 状态更改为“已完成” ，并预留游戏服务器会话中的玩家位置。
```
function RemovePlayerSession(param, w, callback) {
		console.log("RemovePlayerSession.request", param);
		getGseGrpcSdkServiceClient().RemovePlayerSession({
				gameServerSessionId: gameServerSession.gameServerSessionId,
				playerSessionId: param.playerSessionId
		}, getMetadata(), function (err, response) {
				console.log('RemovePlayerSession.response:', err, response);
				if (callback != null) {
						callback(w, response);
				}
		});
}
```
 7. 当一个游戏服务器会话（一组游戏对局或一个服务）结束后，Game Server 调用 TerminateGameServerSession 接口结束 GameServerSession，将 GameServerSession 状态更改为“已终止”。
```
function TerminateGameServerSession(param, w, callback) {
		console.log("TerminateGameServerSession.request", param);
		getGseGrpcSdkServiceClient().TerminateGameServerSession({
				gameServerSessionId: gameServerSession.gameServerSessionId
		}, getMetadata(), function (err, response) {
				console.log('TerminateGameServerSession.response:', response);
				if (callback != null) {
						callback(w, response);
				}
		});
}
```
 8. 当健康检查失败或缩容时，GSE 调用 OnProcessTerminate 接口结束游戏进程，缩容时依据是您在 GSE 控制台配置的 [保护策略](https://cloud.tencent.com/document/product/1165/41028#test12)。
```
function OnProcessTerminate(call, callback) {
		console.log("OnProcessTerminate.request", call.request);
		callback(null, {});
}
```
 9. Game Server 调用 ProcessEnding 接口会立刻结束进程，将服务器进程状态更改为“已终止”，并回收资源。
```
//主动调用：一局游戏对应一个进程，当一局游戏结束后主动调用ProcessEnding接口
//被动调用：当缩容或进程异常健康检查失败时，根据保护策略被动调用ProcessEnding接口，配置完全保护和时限保护策略时需要先判断游戏服务器会话上有无玩家，再被动调用
function ProcessEnding(param, callback) {
		console.log("ProcessEnding.request", param);
		getGseGrpcSdkServiceClient().ProcessEnding({}, getMetadata(), function (err, response) {
				console.log('ProcessEnding.response:', response);
				if (callback != null) {
						callback(response);
				}
		});
}
```
 10. Game Server 调用 DescribePlayerSessions 接口获取游戏服务器会话下的玩家信息（根据业务可选）。
```
function DescribePlayerSessions(param, w, callback) {
		console.log("DescribePlayerSessions.request", param);
		getGseGrpcSdkServiceClient().DescribePlayerSessions({
				gameServerSessionId: gameServerSession.gameServerSessionId,
				playerSessionId: param.playerSessionId,
				playerId: param.playerId,
				playerSessionStatusFilter: param.playerSessionStatusFilter,
				nextToken: param.nextToken,
				limit: param.limit
		}, getMetadata(), function (err, response) {
				console.log('DescribePlayerSessions.response:', err, response);
				if (callback != null) {
						callback(w, response);
				}
		});
}
```
 11. Game Server 调用 UpdatePlayerSessionCreationPolicy 接口更新玩家会话的创建策略，设置是否接受新玩家，即游戏会话里是否允许加入人（根据业务可选）。
```
function UpdatePlayerSessionCreationPolicy(param, w, callback) {
		console.log("UpdatePlayerSessionCreationPolicy.request", param);
		getGseGrpcSdkServiceClient().UpdatePlayerSessionCreationPolicy({
				gameServerSessionId: gameServerSession.gameServerSessionId,
				newPlayerSessionCreationPolicy: param.newPlayerSessionCreationPolicy
		}, getMetadata(), function (err, response) {
				console.log('UpdatePlayerSessionCreationPolicy.response:', err, response);
				if (callback != null) {
						callback(w, response);
				}
		});
}
```
 12. Game Server 调用 ReportCustomData 接口告知 GSE 的自定义数据（根据业务可选）。
```
function ReportCustomData(param, w, callback) {
		console.log("ReportCustomData.request", param);
		getGseGrpcSdkServiceClient().ReportCustomData({
				currentCustomCount: Number(param.currentCustomCount),
				maxCustomCount: Number(param.maxCustomCount)
		}, getMetadata(), function (err, response) {
				console.log('ReportCustomData.response:', response);
				if (callback != null) {
						callback(w, response);
				}
		});
}
```

## 启动服务端，供 GSE 调用

服务端运行：将 GrpcServer 启动起来。
```
function startGameServer() {
  var server = new grpc.Server();
  server.addService(GameServerGrpcSdkServiceProto.GameServerGrpcSdkService.service, {
       OnHealthCheck: OnHealthCheck,
       OnProcessTerminate: OnProcessTerminate,
       OnStartGameServerSession: OnStartGameServerSession
      });
  server.bind('0.0.0.0:7000', grpc.ServerCredentials.createInsecure());
  server.start();
  gsesdkClient.ProcessReady({
    logPathsToUpload: [
      "./log/path/1",
      "./log/path/2"
    ],
    clientPort: 2000,
    grpcPort: 7000
  });
}
```

## 客户端连接 GSE 的 gRPC 服务端
连接服务端：创建一个 gRPC 频道，指定我们要连接的主机名和服务器端口，然后用这个频道创建存根实例。
```
function getGseGrpcSdkServiceClient() {
  if (gseGrpcClient == null) {
    gseGrpcClient = new GseGrpcSdkServiceProto.GseGrpcSdkService('127.0.0.1:5758', grpc.credentials.createInsecure());
  }
  return gseGrpcClient;
}
```

## Nodejs DEMO
 1. [单击这里](https://gsegrpcdemo-1301007756.cos.ap-guangzhou.myqcloud.com/nodejs-demo.zip)，您可下载 Nodejs DEMO 代码。
 2. 生成 gRPC 代码。
Nodejs 版本使用 grpc/proto-loader 直接加载 pb 文件，不需要生成 gRPC-nodejs 代码。
 3. 启动服务端，供 GSE 调用。
  - 服务端实现。
在 nodejs-demo/dynamic_code 目录下的 game_server.js，实现了服务端的三个接口。
  - 服务端运行。
在 nodejs-demo/dynamic_code 目录下的 game_server.js，将 GrpcServer 启动起来。
 4. 客户端连接 GSE 的 gRPC 服务端。
  - 客户端实现。
在 nodejs-demo/dynamic_code 目录下的 gsesdk_client.js，实现了客户端的九个接口。
  - 连接服务端。
创建一个 gRPC 频道，指定我们要连接的主机名和服务器端口，然后用这个频道创建存根实例。
 5. 编译运行
  1.  安装 nodejs，版本不低于 v12.16.0。
  - 安装 grpc 包。
 ```
cnpm install --save grpc-tools
cnpm install --save google-protobuf 
cnpm install --save grpc
cnpm install --save @grpc/proto-loader
cnpm install --save @grpc/grpc-js
```
 如果国外站点无法下载依赖包，需要配置国内的 npm 站点。
  - 将代码下载，在 nodejs-demo 目录下，执行以下命令启动测试：
	```
	cd dynamic_code
	node game_server.js  
 ```
  - 将可执行文件 game_server.js 打包为 [生成包](https://cloud.tencent.com/document/product/1165/41030)，启动路径配置 node，启动参数配置 game_server.js。
  - 然后 [创建服务器舰队](https://cloud.tencent.com/document/product/1165/41028)，将生成包部署在服务器舰队上，后续可进行 [扩缩容](https://cloud.tencent.com/document/product/1165/45709) 等一系列操作。

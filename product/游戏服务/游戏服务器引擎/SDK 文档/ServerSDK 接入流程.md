

### 集成 ServerSDK
请 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请 ServerSDK 下载链接，我们会派专人联系您，并为您提供下载链接。

```
导入头文件
 #include <tencentcloud/gse/server/GseServerAPI.h>
```  

### API 调用流程

1. 初始化，调用 InitSDK。具体操作请参见 [初始化 SDK](https://cloud.tencent.com/document/product/1165/42008)。  

```
TencentCloud::Gse::Server::InitSDKOutcome initOutcome =               
                         TencentCloud::Gse::Server::InitSDK();
if (!initOutcome.IsSuccess())
{
	return false;
} 
```  

2. 进程启动准备就绪，调用 ProcessReady，务必实现3个回调函数。具体操作请参见 [进程准备就绪](https://cloud.tencent.com/document/product/1165/42009)。 
 - onStartGameSession  
 - onProcessTerminate  
 - onHealthCheck  

```
    std::string serverOut("./logs/serverLog.txt");
    std::string serverErr("./logs/serverErr.txt");
    std::vector<std::string> logPaths;
    logPaths.push_back(serverOut);
    logPaths.push_back(serverErr);
    int listenPort = 9090;

    TencentCloud::Gse::Server::ProcessParameters processReadyParameter = TencentCloud::Gse::Server::ProcessParameters(
        std::bind(&GseManager::OnStartGameSession, this, std::placeholders::_1),
        std::bind(&GseManager::OnProcessTerminate, this),
        std::bind(&GseManager::OnHealthCheck, this),
        listenPort, TencentCloud::Gse::Server::LogParameters(logPaths)
        );

    TencentCloud::Gse::GenericOutcome readyOutcome = TencentCloud::Gse::Server::ProcessReady(processReadyParameter);

    if (!readyOutcome.IsSuccess())
    {
        return false;
    }  
```

```
void GseManager::OnStartGameServerSession(TencentCloud::Gse::Server::Model::GameServerSession myGameServerSession)
{
    TencentCloud::Gse::GenericOutcome outcome = 
    	TencentCloud::Gse::Server::ActivateGameServerSession();
}
```

```
void GseManager::OnHealthCheck()
{
    //根据进程实际健康情况，返回true or false
    return true;
}
```  

```
void GseManager::onProcessTerminate()
{   //根据实际情况，判断进程上的游戏服务器会话可以马上结束后才调用以下API,否则先设置一个标志，等待时机再调用该API
	TencentCloud::Gse::GenericOutcome outcome = 
		TencentCloud::Gse::Server::TerminateGameServerSession();
   TencentCloud::Gse::GenericOutcome outcome =
	TencentCloud::Gse::Server::ProcessEnding();
}   
```


3. 客户端连接时，通过 AcceptPlayerSession 检查该连接是否预留位置。具体操作请参见 [接受玩家会话](https://cloud.tencent.com/document/product/1165/42011)。  

```
//当客户端连上来时，调用AcceptPlayerSession检查该连接的合法性
TencentCloud::Gse::GenericOutcome outcome = 
   	TencentCloud::Gse::Server::AcceptPlayerSession(playerSessionId);
if(outcome .IsSuccess())
{
        //接受连接
}
else 
{
        //拒绝连接
} 
```
4. 玩家退出游戏服务器会话 RemovePlayerSession。具体操作请参见 [移除玩家会话](https://cloud.tencent.com/document/product/1165/42012)。

```
//玩家退出游戏服务器会话调用
TencentCloud::Gse::GenericOutcome outcome = 	
	TencentCloud::Gse::Server::RemovePlayerSession(playerSessionId);

if (outcome.IsSuccess())
{
       // 后续处理
}
```
5. 游戏服务器会话结束 TerminateGameSession。具体操作请参见 [结束游戏服务器会话](https://cloud.tencent.com/document/product/1165/42015)。  

```
//游戏服务器会话主动结束或者被动结束了，例如没有人了需要缩容时，可以结束。
TencentCloud::Gse::GenericOutcome outcome = 
	TencentCloud::Gse::Server::TerminateGameSession();

if (outcome.IsSuccess())
{
       // 后续处理
}
```
6. 进程结束 ProcessEnding。具体操作请参见 [结束进程](https://cloud.tencent.com/document/product/1165/42016)。   

```

//被通知缩容或者想重启进程
 TencentCloud::Gse::GenericOutcome outcome = TencentCloud::Gse::Server::ProcessEnding();   
```





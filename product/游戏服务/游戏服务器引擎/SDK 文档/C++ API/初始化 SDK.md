
### 接口描述 	
本接口（InitSDK）用于初始化 SDK。


### 参数描述
无参数。


### 返回值说明
如果成功，返回 [InitSdkOutcome](https://cloud.tencent.com/document/product/1165/42020#jtlx) 对象。


### 使用示例
```
TencentCloud::Gse::Server::InitSDKOutcome initOutcome =               
                         TencentCloud::Gse::Server::InitSDK();

if (!initOutcome.IsSuccess())
{
	return false;
} 
```


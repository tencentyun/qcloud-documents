>!由于产品逻辑已无法满足游戏行业技术发展，游戏服务器伸缩 GSE 将于2022年6月1日下线，请您在2022年5月31日前完成服务迁移。


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


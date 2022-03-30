>!由于产品逻辑已无法满足游戏行业技术发展，游戏服务器伸缩 GSE 将于2022年6月1日下线，请您在2022年5月31日前完成服务迁移。


### 接口描述
本接口（GetGameServerSessionId）用于获取游戏服务器会话 ID。		

### 参数描述
无参数。



### 返回值说明
游戏服务器会话 ID，具体类型为 [StringOutcome](https://cloud.tencent.com/document/product/1165/42020#jtlx)。

### 使用示例
```
TencentCloud::Gse::StringOutcome sessionIdOutcome = 
	TencentCloud::Gse::Server::GetGameServerSessionId();
```



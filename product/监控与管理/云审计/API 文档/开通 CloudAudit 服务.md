
## 接口描述
OpenAuditService 用于开通跟踪集服务。
接口访问域名：`cloudaudit.api.qcloud.com`


## 请求参数
|参数名称|必选|类型|描述|
|---------|---------|---------|--------|
|ownerUin|	是|	Number	|主账号，云 API 自动解析|
|Uin|	是|	Number|	账号，云 API 自动解析|
|clientIp|	是	|String	|用户 IP|
|clientUa|	是|	String	|客户端 UA|


>!此处每个用户只能创建1个跟踪集。

## 响应参数
响应参数为空。

## 实际案例
### 请求

```shell
{
   "ownerUin": 1150691759,
   "Uin": 1150691759,
   "clientIp": "127.0.0.1",
   "clientUa": "Chrome"
}
```
### 响应

```
{
}
```

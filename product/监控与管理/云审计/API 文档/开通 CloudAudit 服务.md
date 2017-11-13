# 开通 CloudAudit 服务
## 接口描述
  OpenAuditService 用于开通 CloudAudit 服务。
## 请求参数
|参数名称|必选|类型|描述|
|---------|---------|---------|--------|
|ownerUin|	是|	number	|主账号(云 API 自动解析)|
|uin|	是|	number|	账号（云 API 自动解析）|
|clientIp|	是	|String	|用户 IP|
|clientUa|	是|	sting	|客户端 UA|
> **注意：**
> 此处每个用户只能创建 50 个 CloudAudit。

## 实际案例
### 请求

```
{
   "ownerUin": 1150691759,
   "uin": 1150691759,
   "clientIp": "127.0.0.1",
   "clientUa": "Chrome"
}
```
### 响应

```
{
}
```



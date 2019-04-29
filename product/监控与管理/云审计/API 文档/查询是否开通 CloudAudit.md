
## 接口描述
GetAuditServiceStatus 用于查询是否开通跟踪集。
接口访问域名：`cloudaudit.api.qcloud.com`

## 请求参数
|参数名称|必选|类型|描述|
|---------|---------|---------|--------|
|ownerUin|	是|	Number	|主账号，云 API 自动解析|

## 响应参数


| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| status | Number | Audit 状态，0 代表关闭，1 代表开启 |


## 实际案例
### 请求

```
{
   "ownerUin": "Number"
}
```
### 响应

```
{
   "status":0
}
```

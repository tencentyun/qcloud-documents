
用户认证源为企业本地，MFAS 服务通过部署与企业本地的 MFAS Connector 同步单个用户信息。
>?Connector API 仅对 MFAS 服务开放，通过 MFAS 外部用户源进行配置，由 MFAS 服务调用 Connector。


### API 详情
- 请求路径：http://connector_hostname:connector_port/ldap/syncSingleUser
- 请求方法：POST
- 请求 Content-Type：application/x-www-form-urlencoded


### 请求参数
 | 请求参数 | 必填 | 说明 |
| ---- | ---- | ---- |
| loginName | 是 | 用户登录名 |
| secretKey | 是 | Connector 共享密钥 |

### 响应参数
| 响应参数 | 说明 | 备注 |
| ---- | ---- | ---- |
| success | 访问结果 | 成功：TRUE<br>失败：FALSE |
| errorCode | 错误编码 | 成功：0<br>错误：请查询错误编码表 |
| message | 错误描述 | 成功：NULL <br>错误：相应错误描述 |
| personalName | 用户姓名 | 返回用户姓名 |
| role | 用户角色 | 返回用户角色 |
| email | 用户邮箱 | 返回用户邮箱 |
| mobile | 用户电话 | 返回用户电话 |

### 响应示例
```json
{
	"success": true,
	"errorCode": 0,
	"data": {
		"personalName": "name",
		"role": "admin",
		"email": "example@tencent.com",
		"mobile": "13812345678"
	},
	"message": null
}
```
```json
{
	"success": false,
	"errorCode": -1,
	"data": null,
	"message": "不存在该用户"
}
```


用户认证源为企业本地，通过 MFAS 服务通过部署与企业本地的 MFAS Connector 同步全部用户信息。
>?Connector API 仅对 MFAS 服务开放，通过 MFAS 外部用户源进行配置，由 MFAS 服务调用 Connector。

### API 详情
- 请求路径：http://connector_hostname:connector_port/ldap/syncAllUsers
- 请求方法：POST
- 请求 Content-Type：application/x-www-form-urlencoded


### 请求参数
| 请求参数 | 必填 | 说明 |
| ---- | ---- | ---- |
| secretKey | 是 | Connector 共享密钥 |

### 响应参数
| 响应参数 | 说明 | 备注 |
| ---- | ---- | ---- |
| success | 访问结果 | 成功：TRUE<br>失败：FALSE |
| errorCode | 错误编码 | 成功：0<br>错误：请查询错误编码表 |
| message | 错误描述 | 成功：NULL <br>错误：相应错误描述 |
| totalCount | 用户总数 | 返回用户总数 |
| loginName | 用户登录名 | 返回用户登录名 |
| personalName | 用户姓名 | 返回用户姓名 |
| role | 用户角色 | 返回用户角色 |
| email | 用户邮箱 | 返回用户邮箱 |
| mobile | 用户电话 | 返回用户电话 |

 ### 响应示例
```json
{
	"success": true,
	"errorCode": 0,
	"message": null,
	"data": {
		"totalCount": 4,
		"data": [
			{
				"loginName": "xiaoming",
				"personalName": "小明",
				"role": "admin",
				"email": "xiaoming@tencent.com",
				"mobile": "13812345678"
			},
			{
				"loginName": "zhangsan",
				"personalName": "张三",
				"role": "employee",
				"email": " zhangsan@tencent.com",
				"mobile": "13687654321"
			},
			{
				"loginName": "lisi",
				"personalName": "李四",
				"role": "employee",
				"email": "lisi@tencent.com",
				"mobile": "13398765432"
			},
			{
				"loginName": "wangwu",
				"personalName": "王五",
				"role": "employee",
				"email": "wangwu@tencent.com",
				"mobile": "13611111111"
			} 
		]
	}
}
```
```json
{
	"success": false,
	"errorCode": -3,
	"data": null,
	"message": "无法同步用户"
}
```

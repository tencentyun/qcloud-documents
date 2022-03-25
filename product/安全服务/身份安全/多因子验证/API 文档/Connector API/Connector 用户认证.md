
用户认证源为企业本地， MFAS 服务通过部署与企业本地的 MFAS Connector 完成用户认证。
>?Connector API 仅对 MFAS 服务开放，通过 MFAS 外部用户源进行配置，由 MFAS 服务调用 Connector。

### API 详情
- 请求路径：http://connector_hostname:connector_port/ldap/auth
- 请求方法：POST
- 请求 Content-Type：application/x-www-form-urlencoded

### 请求参数
| 请求参数 | 必填 | 说明 |
| ---- | ---- | ---- |
| loginName | 是 | 用户登录名 |
| password  | 是 | 用户静态密码 |
| secretKey | 是 | Connector 共享密钥 |

### 响应参数
| 响应参数 | 说明 | 备注 |
| ---- | ---- | ---- |
| success | 访问结果 | 成功：TRUE<br>失败：FALSE |
| errorCode | 错误编码 | 成功：0<br>错误：请查询错误编码表 |
| message | 错误描述 | 成功：NULL <br>错误：相应错误描述 |
| data | 其他信息 | Connector 上未配置返回其他信息：NULL |

### 响应示例
```json
{
    "success": true,
    "errorCode": 0,
    "data": null,
    "message": null
}
```
```json
{
    "success": false,
    "errorCode": -3,
    "data": null,
    "message": null
}
```

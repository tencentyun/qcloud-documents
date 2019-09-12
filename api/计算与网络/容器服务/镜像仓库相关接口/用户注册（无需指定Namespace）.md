## 接口描述

本接口（RegisterRepositoryAccountNew）用户注册（无需指定 Namespace）。 

接口请求域名：
```
ccr.api.qcloud.com
```

## 输入参数

以下请求参数列表仅列出了接口请求参数，其他参数见 [公共请求参数](https://cloud.tencent.com/document/api/457/9463)。

| 参数名称 | 描述 | 类型   | 必选 |
| -------- | ---- | ------ | ---- |
| password | 密码 | String | 是   |

## 输出参数

| 参数名称 | 描述                                                         | 类型   |
| -------- | ------------------------------------------------------------ | ------ |
| code     | 公共错误码。0 表示成功，其他值表示失败                        | Int    |
| message  | 模块错误信息描述，与接口相关                                 | String |
| codeDesc | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因 | String |



## 示例

### 输入

```
  https://domain/v2/index.php?Action=RegisterRepositoryAccountNew
  &password="xxxyyyzzz"
  &其它公共参数
```

### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}
```

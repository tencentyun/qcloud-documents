### 接口描述
本接口（AssumeRoleWithSAML）用于根据 SAML 断言申请角色临时凭证。
请求域名：sts.api.qcloud.com
请求方式：HTTP POST

### 输入参数
以下请求参数列表仅列出了接口请求参数，其余公共参数列表见 [公共请求参数](https://cloud.tencent.com/document/api/213/15692)。

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| SAMLAssertion | 是 | String | base64 编码的 SAML 断言信息 |
| PrincipalArn | 是 |String|扮演者访问描述名 |
| RoleArn | 是 | String | 角色访问描述名 |
| RoleSessionName | 是 |String|会话名称 |

### 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
|  credentials | [credentials](#dataStructure)  | 对象里面包含 token，tmpSecretId，tmpSecretKey 三元组  |
| expiredTime | Integer |证书无效的时间，返回 Unix 时间戳，精确到秒 |
| expiration |String | 证书无效的时间，以 ISO8601 格式的 UTC 时间表示 |

<span id="dataStructure"></span>
### Credentials 数据结构

| 字段  | 类型  | 描述  |
|---------|---------|---------|
| token | String | token 值 |
| tmpSecretId | String | 临时安全证书 ID |
| tmpSecretKey | String | 临时安全证书 Key |


### 示例
创建一个名称为 IdP 的 SAML 身份提供商。

##### 输入示例：

``` 
POST /v2/index.php HTTP/1.1
Host: sts.api.qcloud.com
Accept: */*
Content-Length: 3927
Content-Type: application/x-www-form-urlencoded

Action=AssumeRoleWithSAML
&PrincipalArn=qcs::cam::uin/798950673:saml-provider/OneLogin
&RoleArn=qcs::cam::uin/798950673:roleName/OneLogin-Role
&RoleSessionName=test
&SAMLAssertion=c2FtbCBhc3NlcnRpb24=
&<公共请求参数>
``` 
##### 输出示例：

``` 
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "credentials": {
            "sessionToken": "d154fa74af184dfac3deb3a729c103a3003d52f840001",
            "tmpSecretId": "AKID7byWjIxUdUuRfhuctpd2T7XLpkCeqMub",
            "tmpSecretKey": "LN1yqrCt2oejxQB7AQsL8iP9VE4hzfZ9"
        },
        "expiredTime": 1541594376,
        "expiration": "2018-11-07T12:39:36Z"
    }
}
``` 

### 错误码

以下仅列出了接口业务逻辑相关的错误码，其他错误码详见 [公共错误码](https://cloud.tencent.com/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。

| 错误码 | 描述 |
|---------|---------|
| InvalidParameter.ProviderNotExist | 身份提供商已存在 |
| InvalidParameter.SAMLResponse | 无效的 SAML 断言响应 |
| InvalidParameter.InvalidRoleArn | 无效的角色访问描述名 |


此篇文档将向您介绍 Web 网页应用如何使用 IDaaS OAuth API 实现自建应用对 IDaaS 目录用户进行身份鉴权并获取用户授权的身份信息。


## 开启应用授权登录

您可以登录 [IDaaS 控制台](https://console.cloud.tencent.com/idaas)，单击左侧菜单中的【应用管理】。新建或选择需要开启授权登录的应用。新建完成后进入应用，在【详情信息】面板中“授权登录”卡片开启授权登录。
开启授权登录需要补充“可信域名”，“可信域名”为用户授权回调链接的域名。开启后，将自动分配`client_id`和`client_secret`。
![](https://main.qcloudimg.com/raw/b6401d8f9aff242a7dfd717d2a2eb007.png)


##  构造网页授权链接

用户授权的地址为`https://<IDaaS域名>/open/oauth2/authorize`。完整的授权地址格式如下：

```plaintext
https://mycorp.cloudidaas.com/open/oauth2/authorize?client_id=<client_id>&redirect_uri=<redirect_uri>&response_type=code&scope=basic&state=m7NTlQV1qc8MbCU
```

**参数说明**

| 参数          | 必选 | 说明                                                         |
| ------------- | ---- | ------------------------------------------------------------ |
| client_id     | 是   | 客户端 ID, 可以在应用【详情信息】面板中“授权登录”卡片可以查询到。  |
| redirect_uri  | 是   | 用户授权后的回调链接，请遵循 URL 规范作 URL Encode。           |
| response_type | 是   | 返回类型，此时固定为：`code`。                                 |
| scope         | 是   | 授权范围，支持 `basic` 或 `userinfo`。                         |
| state         | 否   | 推荐传入，用于校验授权发起方和接收方为同一终端，该参数将追加在 `redirect_uri` 的 query 参数中。 |

用户登录后，默认静默授权，页面将跳转至 `redirect_uri?code=<code>&state=<state>`。

## 获取 access_token

- **请求方式：**`POST`
- **请求地址：**https://api.open.cloudidaas.com/oauth2/v1/token
- **请求头部：**请指定 `Content-Type` ：为 `application/json`
- **参数说明**

| 参数          | 必选 | 说明                                                         |
| ------------- | ---- | ------------------------------------------------------------ |
| code          | 是   | 授权码，从 `redirect_uri` 的 query 参数可以获得。              |
| client_id     | 是   | 客户端 ID, 可以在应用“详情信息”面板中“授权登录”卡片可以查询到。 |
| client_secret | 是   | 客户端密钥, 可以在应用“详情信息”面板中“授权登录”卡片可以查询到。 |
| redirect_uri  | 是   | 用户授权后的回调链接。                                         |
| grant_type    | 是   | 此时固定为：`authorization_code`。                             |

**响应示例如下：**

```json
{
    "token_type": "Bearer",
    "expires_in": 600,
    "access_token": "94abc92867c1fc4ddbc22b1d3060e40d78746f95f1f8e7120306437e352825bf",
    "refresh_token": ""
}
```

## 获取用户信息

- **请求方式：**`GET`
- **请求地址：**https://api.open.cloudidaas.com/oauth2/v1/userinfo
- **参数说明**

| 参数         | 必选 | 说明                             |
| ------------ | ---- | -------------------------------- |
| access_token | 是   | 通过用户授权码获得，参考上一小节。 |

**响应示例如下：**

```json
{
  "user_id": "zhangshan",
  "name": "张三",
}
```

## 错误码

调用接口时，接口失败会返回相应的 HTTP 状态码，常见的状态码，如：

- 400 Bad Request — 无效请求。
- 401 Unauthorized — 请求未通过鉴权。
- 403 Forbidden — 请求无权限。
- 404 Not Found — 资源不存在。
- 500 Internal Server Error — 内部服务异常。
- 503 Service Unavailable — 服务不可用。

body 中还会返回 error 对象，格式形如：

```json
{
  "error": {
      "message": "",
      "type": "OAuthException",
      "code": 11000002,
      "trace_id": ""
  }
}
```

企业可以根据 error 对象中的 code 信息调试接口，排查错误。

| 错误码   | 含义                             |
| -------- | -------------------------------- |
| 9003     | 参数错误。                         |
| 11000002 | 授权码 code 或 access_token 无效。 |
| 18000000 | 授权码 code 已过期。               |
| 18000001 | access_token 已过期  。            |
| 18000002 | redirect_uri 不匹配。              |

## 接口描述
使用 [获取 Token ](https://cloud.tencent.com/document/product/1441/64396)接口返回的 refresh_token 获取新的 access_token 。


## 请求方法
POST

## 请求路径
```
/oauth2/token
```

## 请求示例
```
POST /oauth2/token HTTP/1.1
Host: localhost:8080
Content-Type: application/x-www-form-urlencoded
client_id=TENANT_CLIENT_ID&client_secret=TENANT_CLIENT_SECRET&grant_type=refresh_token&refresh_token=MOCK_REFRESH_TOKEN
```


## 请求参数
| 参数          | 可选  | 描述                                                         |
| :------------ | :---- | :----------------------------------------------------------- |
| client_id     | false | 应用的 `client_id`。需要与获取授权时使用的一致。              |
| client_secret | false | 应用的 `client_secret`。可通过租户管理平台的应用基本信息页面查看。 |
| grant_type    | false | 填固定值 `refresh_token`。                                   |
| refresh_token | true  | 获取 Token 时返回的 `refresh_token`。                         |



## 响应参数
| 参数          | 数据类型 | 描述                                    |
| :------------ | :------- | :-------------------------------------- |
| access_token  | String   | 刷新后的 OAuth 2.0 Access Token (JWT)。 |
| refresh_token | String   | 刷新后的 OAuth 2.0 Refresh Token。      |
| scope         | String   | Access Token 的 Scope。                 |
| id_token      | String   | 刷新后的 OIDC ID Token (JWT)。          |
| token_type    | String   | Token 类型，目前取固定值 `Bearer`。    |
| expires_in    | Number   | Access Token 有效期，单位秒。           |



## 正常响应示例
```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
  "access_token" : "eyJraWQiOiJkNDliYzUwNS01NTcyLTRlZDYtOWU0OC0zODhjM2Q0NGJiNDYiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJNT0NLX1VTRVJOQU1FIiwiYXVkIjoiVEVOQU5UX0NMSUVOVF9JRCIsIm5iZiI6MTYzNjQ0OTIzMSwic2NvcGUiOlsib3BlbmlkIl0sImlzcyI6Imh0dHBzOlwvXC9URU5BTlQuUE9SVEFMLkRPTUFJTiIsImV4cCI6MTYzNjQ0OTUzMSwiaWF0IjoxNjM2NDQ5MjMxLCJqdGkiOiI1YTE4ZjE0MS1lMzQxLTQzMzgtODVkNi1iYjRlNDFhODY3NjUifQ.cP9azxqZW8ELTvr70T2u8S0uxq9fnEKKVh55_6umF0RzBXMtRSeN8bW1uDHzQbYVDfQZQp-vzee35XsfZkS5dYOFQmiOr_uXwd8wdgPvy_8ZHyamY4c4ytZvysx-RDrr6oeHK63lPBrkoC1n_NI6AyZtMZxtxrodggzW593FfqG6vWE7OdPBoeQ8Qk-SEntuReNb60l9f6KYs-H8DJt9f1tYbCe_4ECrxpAbezEyhjVxj_8B72oNCybs3toc1NfZ01ouhGyRIyaDqzKLFFX8QYp-UgZV3N_muUyPNXHhvF4xsiFp_Sf0gSfQ_CYQUoXVs7R_ejSPexqqqYUyXHyzJA",
  "refresh_token" : "MOCK_REFRESH_TOKEN",
  "scope" : "openid",
  "id_token" : "eyJraWQiOiJkNDliYzUwNS01NTcyLTRlZDYtOWU0OC0zODhjM2Q0NGJiNDYiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJNT0NLX1VTRVJOQU1FIiwiYXVkIjoiVEVOQU5UX0NMSUVOVF9JRCIsImF6cCI6IlRFTkFOVF9DTElFTlRfSUQiLCJpc3MiOiJodHRwczpcL1wvVEVOQU5ULlBPUlRBTC5ET01BSU4iLCJleHAiOjE2MzY0NTEwMzEsImlhdCI6MTYzNjQ0OTIzMSwianRpIjoiMDEzYmFiMzktZjkxOC00NDhmLWEzOTYtY2U3N2VlZmZkYjM3In0.M_k7_RnA3E9ptcunBhSSZkxxqqHZhH7PIMn0QQoJGhJ0nja1ZxdMwhEMBmQDZ-cDNaWNUGFT3XZkAsJNBF06g69kAu_gMzRKeGIgCUrQUO_Z1DNoec6Q6oPg3bV5JzYtNjjySEeYrlKxG0PpY3L0uRjpQFXXL6vpm9n4LXz81gsmZiC0JAfJ-n7oDH6QJ8AmfWWJZMs2qobFXsKaFqwBehXFki5qTy8MLxkHMuW-kc4IK0gadlrvic3MRsy3qgfPnwHUfCLb7Ky77EPGXGwFbNzAYGtlimCe-ZN498RatwejTXptiqkBqUhaS7QqdEcI0etAd_4J2DmJYwcXJCFwSg",
  "token_type" : "Bearer",
  "expires_in" : 299
}
```

## 异常响应示例
refresh_token 参数有误。
```
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8

{
  "error" : "invalid_grant"
}
```

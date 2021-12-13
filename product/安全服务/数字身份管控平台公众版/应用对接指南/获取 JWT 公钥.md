## 接口描述
JWT 公钥用于对 JWT 格式的 ID Token 和 Access Token 进行验证。
>?JWT 密钥在创建用户目录时自动生成，不同用户目录的密钥不同。


## 请求方法
GET

## 请求路径
```
/oauth2/jwks
```

## 请求示例
```
GET /oauth2/jwks HTTP/1.1
Host: localhost:8080
```


## 响应参数

| 参数       | 数据类型 | 描述               |
| :--------- | :------- | :----------------- |
| keys       | Array    | 包含公钥的数组。   |
| keys[].kty | String   | 密钥类型，如 RSA。 |
| keys[].kid | String   | 密钥标识。         |
| keys[].e   | String   | RSA 公钥。         |
| keys[].n   | String   | RSA 公钥。         |


## 正常响应示例
```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "keys" : [ {
    "kty" : "RSA",
    "e" : "AQAB",
    "kid" : "d49bc505-5572-4ed6-9e48-388c3d44bb46",
    "n" : "reCXJ_FkaMcjS6Qia3g4giV1IkGckkx_l9YSoP-bo2GpK948qGnn7sS4ji501cn8TTEU2MKYywEvB6eR-Mj6THEReTzxhMEwGoytZYxpkSj9t5gGZ9-EXOZBAqFirI3AG3_oVvCxwoFncqcKR5AidZONc0lO4Lf5U4tXa5ArrKRbRGczm3kQky-Vxy13f23y5yc_VPjnRgyhScIJOPzBMWXZ-jKD4Bc1UaPHwbE3fx5ayMUqjZXID1-0VpTxAvMLpEhrbfrlGjHAbljqwmt_yKBSiPP8vJAfyv0WOLHus6BnvhpVNKMvd2WXtk6njPDTibvFm9tkAhsrQ1Q5ZTbgRQ"
  } ]
}
```


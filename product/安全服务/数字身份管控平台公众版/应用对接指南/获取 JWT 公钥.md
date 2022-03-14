## 接口描述
JWT 公钥用于对 JWT 格式的 ID Token 和 Access Token 进行验证。
>?JWT 密钥在创建用户目录时自动生成，不同用户目录的密钥不同。

## 支持的应用类型
Web 应用、单页应用、移动 App、M2M 应用、小程序应用。

## 请求方法
```
GET
```

## 请求路径
```
/oauth2/jwks
```

## 请求示例
```
GET /oauth2/jwks HTTP/1.1
Host: sample.portal.tencentciam.com
```



## 正常响应示例
```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "keys" : [ {
    "kty" : "RSA",
    "e" : "AQAB",
    "kid" : "f9694d93-d541-4985-88dc-42229873008e",
    "n" : "wYmf-IL7_pXqEjtfHme7KqS06hRQ0BzhTzORjgwnsJD_CPexMHQAd82vZfOQioW9oaMXTiSAtkXslxNIxKVjiYMVzTLHQ9nqCARHOAONiftvcOyMiDGwI_ZV2u2ltHCbQ1w8sMpREMxLiW46TYHANSQwgzg9gLojhzPEUmAS0ksTx3UURmQGLnFBEh6Ydbj8tPNnNxfZHRLtqTD0FwLpPrn3wJvQRxNk_fcrJexM5v96XdQ1SLhhcIAMyqU-_-3IkyWIcS-Z-EvZCiKNJPCfVIEpWdz0oQdGXdADSRU8cV_sl-YmUWSE355PSzK1UmbvNJWLMsO67ZsgZyetcvkaIw"
  } ]
}
```

## 响应参数

| 参数       | 数据类型 | 描述               |
| :--------- | :------- | :----------------- |
| keys       | Array    | 包含公钥的数组。   |
| keys[].kty | String   | 密钥类型，如 RSA。 |
| keys[].kid | String   | 密钥标识。         |
| keys[].e   | String   | RSA 公钥。         |
| keys[].n   | String   | RSA 公钥。         |


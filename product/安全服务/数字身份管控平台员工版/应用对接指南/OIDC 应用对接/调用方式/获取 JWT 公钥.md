EIAM 返回的是 JWT 格式的 ID Token 。请参考[ OIDC 官方文档](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation) 对 JWT 进行解密与验证。验证所需的公钥通过调用获取 JWT 公钥接口获得。

### 接口描述
JWT 公钥用于对 JWT 格式的 ID Token 和 Access Token 进行解密。

### 请求方法
GET
### 请求地址
```
/auth/oauth2/jwks
```

### 返回参数
| 参数 | 参数类型          | 描述           |
| ---- | ----------------- | -------------- |
| keys | Array of key_info | 包含公钥的数组 |
                             

### 接口示例
#### 输入示例
```
https://<auth_domain>/auth/oauth2/jwks
```
#### 返回示例
```
{
  "keys" : [ {
    "kty" : "RSA",
    "e" : "AQAB",
    "kid" : "52dd697c-b8f9-****-ad38-21db07a1575b",
    "n" : "w31qUM4pR-vWQyhstx0BFc-W6ntEPX****MR0LS4NCsFN40cFUhXV_hrfYkxmfhKpQF_4FQXdQLLBC2iliaNCFUWrGM1_i_Q6gSSrjt2D6Lzkc50-6T2ORhnI5kNxvMqQLPxLgZzS-izB5ouazHn0BFzZJJeE9LAh__hmGSUjSF36w1YEp8GI5HVO5T-RBKTMsRUdm3NyTSB3xyN_uC****svM_bOIUHGqiEAhdwpm7Pa93Wu0VtZBn5JmaeZi9OIcmcyWad6mrON_sltm5a15nDNhz2SYu8ICWH4uE1ItXtg713I8txP8TAAwid_iPS21DQZr2LJwqB0KM026w"
  } ]
}
```

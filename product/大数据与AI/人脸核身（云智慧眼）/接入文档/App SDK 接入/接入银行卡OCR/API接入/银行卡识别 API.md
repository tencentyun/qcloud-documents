合作方后台服务上送 sign、请求参数到身份证识别后台服务。
## 请求
- **请求 URL：**`https://ida.webank.com/api/paas/bankcardocrapp`
- **请求方法：**POST
- **报文格式：**Content-Type: application/json
- **请求参数：**

| 参数 | 说明   | 类型   | 长度（字节） | 是否必填 |
| ----- | ------- | -------- | ---------------- | ---------- |
| webankAppId | WebankAppId，由腾讯指定        | String        | 腾讯云线下对接决定 | 是          |
| version     | 接口版本号，默认值：1.0.0                    | String        | 20          | 是 |
| nonce       | 随机数，32位随机串（字母+数字组成的随机数） | String        | 32          | 是        |
| sign        | 签名：使用上面生成的签名            | String        | 40          | 是         |
| orderNo     | 订单号，由合作方上送，每次唯一          | String        | 32          | 是         |
| userId     | 用户的唯一标识（不要带有特殊字符）          | String        | 32          | 否         |
| bankcardStr | 银行卡正面图片的 Base64   | Base64 String |  大小不超过3MB    | 是         |

## 响应
**响应参数：**

| 参数         |     类型   | 说明        |
| ----------- | ---------- | ---------- |
| code              | String | 银行卡 OCR 识别结果的返回码</br>0：识别成功</br>其他：识别失败  |
| warningCode          | String       | Code = 0 是有值，合作方可以根据 warning 来确定         |
| msg               |String       | 请求结果描述                               |
| orderNo           |  String       |订单号，由合作方上送，每次唯一，此信息为本次身份证 OCR 识别上送的信息 |
| bankcardNo        |String       | 银行卡识别结果：银行卡号                         |
| bankcardValidDate |String       | 银行卡识别结果：银行卡有效时间                      |
| bankcardNoPhoto   | Base64 String | 银行卡识别结果：银行卡卡号照片                      |
|multiWarningCode | String | 多重告警码，含义请参考 [错误码](https://cloud.tencent.com/document/product/1007/31082) |
| clarity       | String | 图片清晰度                |

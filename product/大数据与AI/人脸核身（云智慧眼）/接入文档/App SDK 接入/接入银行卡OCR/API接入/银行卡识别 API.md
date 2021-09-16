>!如果因自身业务需要对 OCR 识别的影像文件进行存储或其他用途，请合作方务必自行保存订单号，通过订单号拉取 OCR 识别的影像文件是唯一方式。

合作方后台服务上送 sign、请求参数到身份证识别后台服务。
## 请求
- **请求 URL：**https://miniprogram-kyc.tencentcloudapi.com/api/paas/bankcardocrapp?orderNo=xxx
>!为方便查询耗时，该请求 url 后面请拼接 orderNo 订单号参数。

- **请求方法：**POST
- **报文格式：**Content-Type: application/json
- **请求参数：**

| 参数 | 说明   | 类型   | 长度（字节） | 是否必填 |
| ----- | ------- | -------- | ---------------- | ---------- |
| webankAppId | 业务流程唯一标识，即 wbappid，可参考 [获取 WBappid](https://cloud.tencent.com/document/product/1007/49634) 指引在人脸核身控制台内申请 | String        | 8 | 是    |
| version     | 接口版本号，默认值：1.0.0                    | String        | 20          | 是 |
| nonce       | 随机数，32位随机串（字母+数字组成的随机数） | String        | 32          | 是        |
| sign        | 签名：使用上面生成的签名            | String        | 40          | 是         |
| orderNo     | 订单号，字母/数字组成的字符串，由合作方上送，每次唯一          | String        | 32          | 是         |
| userId     | 用户的唯一标识（不要带有特殊字符）          | String        | 32          | 否         |
| bankcardStr | 银行卡正面图片的 Base64   | Base64 String |  大小不超过3MB    | 是         |

## 响应
**响应参数：**

| 参数         |     类型   | 说明        |
| ----------- | ---------- | ---------- |
| code              | String | 银行卡 OCR 识别结果的返回码</br>0：识别成功</br>其他：识别失败  |
| warningCode          | String       | Code = 0 是有值，合作方可以根据 warning 来确定         |
| msg               |String       | 请求结果描述                               |
| orderNo           |  String       |订单号，字母/数字组成的字符串，由合作方上送，每次唯一，此信息为本次身份证 OCR 识别上送的信息 |
| bankcardNo        |String       | 银行卡识别结果：银行卡号                         |
| bankcardValidDate |String       | 银行卡识别结果：银行卡有效时间                      |
| bankcardNoPhoto   | Base64 String | 银行卡识别结果：银行卡卡号照片                      |
|multiWarningCode | String | 多重告警码，含义请参考 [银行卡 OCR 错误码](https://cloud.tencent.com/document/product/1007/47903) |
| clarity       | String | 图片清晰度                |

**响应示例：**
```
{
   "code":"0",
   "msg":"请求成功",
   "bizSeqNo":"21062120001184436317400509484816",
   "result":{
         "bizSeqNo":"21062120001184436317400509484816",
         "transactionTime":"20210621174006",
         "orderNo":"bankcardPic5923ab9a3bc34488b51",
         "bankcardNo":"xxxxxxxxxxxxxxxxxxx",
         "bankcardValidDate":"12/2024",
         "warningCode":"0",
         "bankcardNoPhoto":"xxx",
         "multiWarningCode":"0",
         "clarity":"79",
         "success":false
},
"transactionTime":"20210621174006"
}
```

>?success：false 无意义，合作伙伴可忽略，无需处理。

### 计费
腾讯云文字识别 OCR 提供预付费和后付费两种计费模式，开通服务后默认使用后付费的计费模式。如果您拥有免费资源包或者付费资源包，将优先对资源包进行扣减，资源包耗尽后自动转入后付费（月结）的方式。详细的产品价格及计费方式请参考 [OCR 计费说明](https://cloud.tencent.com/document/product/1007/49309)。

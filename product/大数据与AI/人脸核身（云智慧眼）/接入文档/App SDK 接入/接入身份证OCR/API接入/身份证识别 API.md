合作方后台服务上送 sign、请求参数到身份证识别后台服务。
- **请求 URL：**`https://ida.webank.com/api/paas/idcardocrapp`
- **请求方法：**POST
- **报文格式：**`Content-Type: application/json`
- **请求参数：**

|参数 | 说明 | 类型 | 长度（字节） | 是否必填|
|----- | ----- | ------ | ---------------- | -----------|
|webankAppId | WebankAppId，由腾讯指定 | String | 腾讯云线下对接决定 | 是|
|version | 接口版本号<br>默认值：1.0.0 | String | 20 | 是|
|nonce | 随机数<br>32 位随机串（字母 + 数字组成的随机数） | String | 32 | 是|
|sign | 签名：使用 [生成的签名](https://cloud.tencent.com/document/product/1007/35920) | String | 40 | 是|
|orderNo | 订单号，由合作方上送，每次调用唯一 | String | 32 | 是|
|userId | 用户的唯一标识（不要带有特殊字符） | String | 32 | 否|
|cardType | 身份证正反面标识<br>0：人像面<br>1：国徽面 | String | 1 | 是|
|idcardStr | 身份证人像面或者国徽面图片的 Base64，大小不超过3MB | String | 3145728 | 是|

- **响应参数：**

|参数 | 类型 | 说明|
|----- | ------ | -----|
|code	| String	| 身份证 OCR 识别结果的返回码<br>0：识别成功<br>其他：识别失败|
|warning	| String	| Code=0 是有值，姓名和身份证外的非关键信息有误会提示，合作方可以根据 warning 来确定|
|msg	| String	| 请求结果描述|
|ocrId	| String	| 保留字段，内部标识|
|orderNo	| String	| 订单号，由合作方上送，每次调用唯一，此信息为本次身份证 OCR 识别上送的信息|
|name	| String	| 身份证识别结果：姓名|
|sex	| String	| 身份证识别结果：性别|
|nation	| String	| 身份证识别结果：民族|
|birth	| String	| 身份证识别结果：出生日期|
|idcard	| String	| 身份证识别结果：身份证号|
|address	| String	| 身份证识别结果：住址<br>如果用户没有正确上传身份证反面，则没有该字段|
|authority	| String	| 身份证识别结果：签发机关<br>如果用户没有正确上传身份证反面，则没有该字段|
|validDate	| String	| 身份证识别结果：有效日期<br>如果用户没有正确上传身份证反面，则没有该字段|
|multiWarning	| String	| 正面多重告警码，详情请参见 [错误码](https://cloud.tencent.com/document/product/1007/31082)|
|clarity	| String	| 图片清晰度|


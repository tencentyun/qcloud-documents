>!如果因自身业务需要对 OCR 识别的影像文件进行存储或其他用途，请合作方务必自行保存订单号，通过订单号拉取 OCR 识别的影像文件是唯一方式。

合作方后台服务上送 sign、请求参数到身份证识别后台服务。
- **请求 URL：**https://miniprogram-kyc.tencentcloudapi.com/api/paas/idcardocrapp?orderNo=xxx
>!为方便查询耗时，该请求 url 后面请拼接 orderNo 订单号参数。

- **请求方法：**POST
- **报文格式：**`Content-Type: application/json`
- **请求参数：**

|参数 | 说明 | 类型 | 长度（字节） | 是否必填|
|----- | ----- | ------ | ---------------- | -----------|
|webankAppId | 业务流程唯一标识，即 wbappid，可参考 [获取 WBappid](https://cloud.tencent.com/document/product/1007/49634) 指引在人脸核身控制台内申请 | String | 8 | 是|
|version | 接口版本号<br>默认值：1.0.0 | String | 20 | 是|
|nonce | 随机数<br>32 位随机串（字母 + 数字组成的随机数） | String | 32 | 是|
|sign | 签名：使用 [生成的签名](https://cloud.tencent.com/document/product/1007/35920) | String | 40 | 是|
|orderNo | 订单号，字母/数字组成的字符串，由合作方上送，每次调用唯一 | String | 32 | 是|
|userId | 用户的唯一标识（不要带有特殊字符） | String | 32 | 否|
|cardType | 身份证正反面标识<br>0：人像面<br>1：国徽面 | String | 1 | 是|  
|idcardStr | 身份证人像面或者国徽面图片的 Base64，大小不超过20MB | String | 20971520 | 是|

- **响应参数：**

|参数 | 类型 | 说明|
|----- | ------ | -----|
|code	| String	| 身份证 OCR 识别结果的返回码<br>0：识别成功<br>其他：识别失败|
|warning	| String	| Code=0 是有值，姓名和身份证外的非关键信息有误会提示，合作方可以根据 warning 来确定|
|msg	| String	| 请求结果描述|
|ocrId	| String	| 保留字段，内部标识|
|orderNo	| String	| 订单号，字母/数字组成的字符串，由合作方上送，每次调用唯一，此信息为本次身份证 OCR 识别上送的信息|
|name	| String	| 身份证识别结果：姓名|
|sex	| String	| 身份证识别结果：性别|
|nation	| String	| 身份证识别结果：民族|
|birth	| String	| 身份证识别结果：出生日期|
|idcard	| String	| 身份证识别结果：身份证号|
|address	| String	| 身份证识别结果：地址<br>如果用户没有正确上传人像面，则没有该字段|
|authority	| String	| 身份证识别结果：签发机关<br>如果用户没有正确上传国徽面，则没有该字段|
|validDate	| String	| 身份证识别结果：有效日期<br>如果用户没有正确上传国徽面，则没有该字段|
|multiWarning	| String	| 多重告警码，详情请参见 [身份证 OCR 错误码](https://cloud.tencent.com/document/product/1007/47902)|
|clarity	| String	| 图片清晰度|

#### 响应示例：
**人像面响应示例：**
```
{
    "code":"0",
    "msg":"请求成功",
    "bizSeqNo":"21062120001184493117265207455389",
    "result":{
	       "bizSeqNo":"21062120001184493117265207455389",
	       "transactionTime":"20210621172652",
	       "ocrId":"54805d89208da5bac41b72fd6ca1be82",
	       "orderNo":"1rjh4xez2vn4706nvb9x273812n21136",
	       "name":"xxx",
	       "sex":"男",
	       "nation":"汉",
	       "birth":"19881001",
	       "address":"xxxxxxxxxxxxx",
	       "idcard":"xxxxxxxxxxxxxxxxxx",
	       "warning":"00000000",
	       "sign":"2E5A4268DB6B347DF34194D903A6927B8C454AAF",
	       "clarity":"64",
	       "multiWarning":"00000000",
	       "retry":"1",
	       "success":false
	 },
	 "transactionTime":"20210621172652"
	 }
```

**国徽面响应示例：**
```
{
    "code":"0",
    "msg":"请求成功",
    "bizSeqNo":"21062120001184438417304507864378",
    "result":{
          "bizSeqNo":"21062120001184438417304507864378",
	         "transactionTime":"20210621173045",
	         "ocrId":"d1e4111f858413e92784ddbdd5f03f35",
	         "orderNo":"h1jw98k72ffe3de249qmf1723673v31v",
	         "validDate":"20190128-20390128",
	         "authority":"xxxxxx",
	         "warning":"00000000",
	         "sign":"1CCE440E241085898B41ECE87E01E6A9D15F74F6",
	         "clarity":"72",
	         "multiWarning":"00000000",
	         "retry":"1",
	         "success":false
	 },
	 "transactionTime":"20210621173045"
	 }
```


>?success：false 无意义，合作伙伴可忽略，无需处理。


### 计费
腾讯云文字识别 OCR 提供预付费和后付费两种计费模式，开通服务后默认使用后付费的计费模式。如果您拥有免费资源包或者付费资源包，将优先对资源包进行扣减，资源包耗尽后自动转入后付费（月结）的方式。详细的产品价格及计费方式请参考 [OCR 计费说明](https://cloud.tencent.com/document/product/1007/49309)。




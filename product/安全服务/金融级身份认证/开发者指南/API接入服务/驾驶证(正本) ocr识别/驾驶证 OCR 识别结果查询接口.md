驾驶证 OCR 识别的签名详情请参考 [合作方生成签名](https://cloud.tencent.com/document/product/655/30496)。

请求 URL：`https://idasc.webank.com/api/v2/ocrbase/querydriverlicenseocrresult`
请求方法：POST
报文格式：Content-Type: application/json

## 请求参数

| 参数 | 说明   | 类型   | 长度（字节） | 是否必填 |
| ---- | ----- | ----- | ---- | --- |
|webankAppId|	腾讯服务分配的 App ID|	String 	|腾讯服务分配|	是|
|orderNo	|订单号，合作方订单的唯一标识	|String |	32	|是|
|getFile	|是否需要查询驾驶证 OCR 原照，值为 1 则返回文件；其他则不返回	|String 	|1|	否|
|nonce	|随机数	|String |	32	|是|
|version|	版本号，默认值：1.0.0	|String |	20|	是|
|sign	|签名值，使用本页第一步生成的签名	|String |	40	|是|

## 响应参数

| 参数         |     类型   | 说明        |
| ----------- | ---------- | ---------- |
|code	|String	|“0” 说明驾驶证识别成功|
|licenseNo	|String|	证号|
|msg	|String	|“请求成功”|
|orderNo|	String	|订单号，由合作方上送，每次唯一，此信息为本次驾驶证 OCR 识别上送的信息|
|name|	String|	姓名|
|sex|	String|	性别|
|nationality|	String|	国籍|
|address|	String	|住址|
|birth|	String|	出生日期|
|fetchDate|	String	|领证日期|
|driveClass|	String|	准驾车型|
|validDateFrom	|String|	起始日期|
|validDateTo	|String|	有效日期|
|licenseStamp	|String	|证件红章|
|originImageStr	|Base 64 string|	驾驶证原图 Base64 字符串|
|operateTime	|String|	做 OCR 的操作时间|

## 返回示例

```
 {
    "code": 0,
    "msg":"请求成功",
    "bizSeqNo":"业务流水号"，
    "result": {
      "orderNo": "orderNoTest",
      "licenseNo": "***********",
      "name": "张三",
      "sex": "男"
    }
  }
```

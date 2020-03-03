行驶证 OCR 识别的签名详情请参考 [合作方生成签名](https://cloud.tencent.com/document/product/655/30504)。

请求 URL：`https://idasc.webank.com/api/v2/ocrbase/queryvehiclelicenseocrresult`
请求方法：POST
报文格式：Content-Type: application/json

## 请求参数

| 参数 | 说明   | 类型   | 长度（字节） | 是否必填 |
| ---- | ----- | ----- | ---- | --- |
|webankAppId|	腾讯服务分配的 App ID|	String 	|腾讯服务分配|	是|
|orderNo	|订单号，合作方订单的唯一标识	|String |	32	|是|
|getFile	|是否需要查询行驶证 OCR 原照，值为1则返回文件；其他则不返回	|String 	|1|	否|
|nonce	|随机数	|String |	32	|是|
|version|	版本号，默认值：1.0.0	|String |	20|	是|
|sign	|签名值，使用本页第一步生成的签名	|String |	40	|是|

## 响应参数

| 参数         |     类型   | 说明        |
| ----------- | ---------- | ---------- |
|code|	String	|“0” 说明行驶证识别成功|
|plateNo|	String	|车牌号码|
|msg|	String	|“请求成功”|
|orderNo|	String|	订单号，由合作方上送，每次唯一，此信息为本次行驶证 OCR 识别上送的信息|
|vehicleType	|String	|车辆类型|
|owner|	String	|所有人|
|useCharacter|	String|	使用性质|
|address	|String|	住址|
|model	|String|	品牌型号|
|vin|	String|	识别代码|
|engineNo|	String	|发动机号|
|registeDate|	String|	注册日期|
|issueDate|	String|	发证日期|
|licenseStamp|	String	|红章|
|originImageStr|	Base 64 string	|行驶证原图 Base64 字符串|
|operateTime|	String	|做 OCR 的操作时间|

## 返回示例

```
{
    "code": 0,
    "msg":"请求成功",
    "bizSeqNo":"业务流水号"，
    "result": {
      "orderNo": "orderNoTest",
      "plateNo": "*******",
      "vehicleType": "轿车",
      "owner": "张三"
    }
  }
```

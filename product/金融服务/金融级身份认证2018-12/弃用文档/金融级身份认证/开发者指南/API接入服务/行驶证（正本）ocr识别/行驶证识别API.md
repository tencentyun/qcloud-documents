合作方后台服务上送 sign、请求参数到身份证识别后台服务。
请求 URL：`https://idasc.webank.com/api/v2/ocrpaas/vehiclelicenseupload`
请求方法：POST
报文格式：Content-Type: application/json
## 请求参数

| 参数 | 说明   | 类型   | 长度（字节） | 是否必填 |
| ---- | ----- | ----- | ---- | --- |
| webankAppId | WebankAppId，由腾讯指定        | String        | 腾讯云线下对接决定 | 是          |
| version     | 接口版本号</br>默认值：1.0.0                    | String        | 20          | 是 |
| nonce       | 随机数</br>32位随机串（字母 + 数字组成的随机数） | String        | 32          | 是        |
| sign        | 签名：使用上面生成的签名            | String        | 40          | 是         |
| orderNo     | 订单号，由合作方上送，每次唯一          | String        | 32          | 是         |
|imageStr|	行驶证图片文件（Base64）	 |Base64 String|	大小不超过3M	|是|
|bizScene|	业务场景</br>场景编号，两位数字，具体如下：</br>01：贷款申请</br>02：信用卡申请</br>03：开户</br>04：修改密码</br>05：重置密码</br>06：转账</br>07：挂失 / 解挂</br>08：登录</br>09：信息维护	|String	|2	|否|

## 响应参数

| 参数         |     类型   | 说明        |
| ----------- | ---------- | ---------- |
|code	|String	|0：识别成功</br>其他：识别失败|
|plateNo	|String	|车牌号码|
|msg|	String|	请求结果描述|
|orderNo	|String|	订单号，由合作方上送，每次唯一，此信息为本次行驶证 OCR 识别上送的信息|
|vehicleType|	String|	车辆类型|
|owner	|String|	所有人|
|useCharacter	|String|	使用性质|
|address	|String	|住址|
|model	|String|	品牌型号|
|vin	|String|	识别代码|
|engineNo	|String|	发动机号|
|registeDate	|String	|注册日期|
|issueDate|	String|	发证日期|
|licenseStamp|	String	|红章|

## 返回示例

```
{
    "code": 0,
    "msg":"请求成功",
    "bizSeqNo":"业务流水号"，
    "result": {
      "orderNo": "orderNoTest",
      "plateNo": "******",
      "vehicleType": "轿车",
      "owner": "张三",
      "address": "********",
      "useCharacter": "非营运",
      "model": "*******",
      "vin": "******",
      "engineNo": "******",
      "registeDate": "2005-07-05",
      "issueDate": "2005-07-05",
      "licenseStamp": "********"
    }
  }
```

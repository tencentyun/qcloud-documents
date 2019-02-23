合作方后台服务上送 sign、请求参数到驾驶证识别后台服务。
请求 URL：`https://idasc.webank.com/api/v2/ocrpaas/driverlicenseupload`
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
|imageStr|	驾驶证图片文件（Base64）	 |Base64 String|	大小不超过3M	|是|
|bizScene|	业务场景</br>场景编号，两位数字，具体如下：</br>01：贷款申请</br>02：信用卡申请</br>03：开户</br>04：修改密码</br>05：重置密码</br>06：转账</br>07：挂失 / 解挂</br>08：登录</br>09：信息维护	|String	|2	|否|

## 响应参数

| 参数         |     类型   | 说明        |
| ----------- | ---------- | ---------- |
| code              | String | 0：识别成功</br>其他：识别失败  |
| licenseNo         | String       | 证号         |
| msg               |String       | 请求结果描述                               |
| orderNo           |  String       |订单号，由合作方上送，每次唯一，此信息为本次驾驶证 OCR 识别上送的信息 |
|name	|String|	姓名|
|sex|	String	|性别|
|nationality|	String	|国籍|
|address|	String	|住址|
|birth|	String	|出生日期|
|fetchDate	|String|	领证日期|
|driveClass|	String|	准驾车型|
|validDateFrom	|String|	起始日期|
|validDateTo|	String	|有效日期|
|licenseStamp|	String	|证件红章|

## 返回示例

```
{
    "code": 0,
    "msg":"请求成功",
    "bizSeqNo":"业务流水号"，
    "result": {
      "orderNo": "orderNoTest",
      "licenseNo": "**********",
      "name": "张三",
      "sex": "男",
      "nationality": "中国",
      "address": "***********",
      "birth": "1986-08-04",
      "fetchDate": "2012-05-28",
      "driveClass": "C1",
      "validDateFrom": "2012-05-28",
      "validDateTo": "2018-05-28",
      "licenseStamp": "**********"
    }
  }
```

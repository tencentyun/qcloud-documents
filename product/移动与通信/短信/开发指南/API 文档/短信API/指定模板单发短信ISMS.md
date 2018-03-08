## 接口描述

### 功能描述

用户发送国际短信专用接口。


### URL 示例

`https://yun.tim.qq.com/v5/tlssmssvr/send<font color=red>i</font>sms?sdkappid=xxxxx&random=xxxx`

**注**：sdkappid 请填写您在腾讯云上申请到的，random 请填成随机数。

## 请求参数

```json
{
    "ext": "",
    "extend": "",
    "params": [
        "验证码",
        "1234",
        "4"
    ],
    "sig": "30db206bfd3fea7ef0db929998642c8ea54cc7042a779c5a0d9897358f6e9505",
    "sign": "腾讯云",
    "tel": "+8613711112222",
    "time": 1457336869,
    "tpl_id": 19
}
```

| 参数   | 必选 | 类型   | 描述                                                                  |
|--------|------|--------|-----------------------------------------------------------------------|
| ext    | 否   | string | 用户的session内容，腾讯server回包中会原样返回，可选字段，不需要就填空 |
| extend | 是   | string | 通道扩展码，可选字段，默认没有开通(需要填空)                          |
| params | 是   | array  | 模板参数，若模板没有参数，请提供为空数组                              |
| sig    | 是   | string | app凭证，具体计算方式见下注                                           |
| sign   | 否   | string | 短信签名，如果使用默认签名，该字段可缺省                              |
| tel    | 是   | string | 国际电话号码，格式："+8613788888888"                                  |
| time   | 是   | number | 请求发起时间，unix时间戳，如果和系统时间相差超过10分钟则会返回失败    |
| tpl_id | 是   | number | 模板ID，在控制台审核通过的模板ID                                      |



**注**：

1. "tel"字段为国际电话号码，其格式依据[e.164](https://en.wikipedia.org/wiki/E.164)标准  
示例："tel": "+8613711112222"，加号（+）用来代替任何国家的[冠码](https://zh.wikipedia.org/wiki/%E5%9B%BD%E9%99%85%E5%86%A0%E7%A0%81%E5%88%97%E8%A1%A8)，86为国家码，13711112222为手机号 
2. "tpl_id"字段需填写审核通过的模板 ID ，上面的请求参数组合后下发的内容为：  
"【腾讯云】您的验证码是 1234，请于 4 分钟内填写。如非本人操作，请忽略本短信。"   
如果您有多个短信签名，请将需要的短信签名填入"sign"字段  
例如您有"【腾讯科技】"，"【腾讯云】"两个签名，但是想以"【腾讯云】"签名发送短信，则"sign"字段可赋值为："腾讯云" ）
3. "extend"字段的配置请联系[腾讯云短信技术支持](/doc/product/382/联系我们)  
4. "sig"字段根据公式sha256(appkey=$appkey&random=$random&time=$time&tel=$tel)生成  
伪代码如下：
```
string strTel = "+8613711112222"; //tel 的 mobile 字段的内容
string strAppKey = "dffdfd6029698a5fdf4"; //sdkappid 对应的 appkey，需要业务方高度保密
string strRand = "7226249334"; //url 中的 random 字段的值
string strTime = "1457336869"; //unix 时间戳
string sig = sha256(appkey=$strAppKey&random=$strRand&time=$strTime&tel=$strTel);
```

## 响应参数

```json
{
    "result": 0,
    "errmsg": "OK",
    "ext": "",
    "nationcode":"86",
    "fee": 1,
    "sid": "xxxxxxx"
}
```

| 参数       | 必选 | 类型   | 描述                                          |
|------------|------|--------|-----------------------------------------------|
| result     | 是   | number | 错误码，0表示成功(计费依据)，非0表示失败      |
| errmsg     | 是   | string | 错误消息，result非0时的具体错误信息           |
| ext        | 否   | string | 用户的session内容，腾讯server回包中会原样返回 |
| nationcode | 是   | string | 国家码                                        |
| fee        | 否   | number | 短信计费的条数                                |
| sid        | 否   | string | 本次发送标识id，标识一次短信下发记录          |

 



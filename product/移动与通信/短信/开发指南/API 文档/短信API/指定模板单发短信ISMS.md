## 接口描述

### 功能描述

用户发送国际/港澳台短信专用接口。

### URL 示例

```
POST https://yun.tim.qq.com/v5/tlssmssvr/sendisms?sdkappid=xxxxx&random=xxxx
```

其中，`sdkappid`请填写您在 [短信控制台](https://console.cloud.tencent.com/sms) 添加应用后生成的实际 SDK AppID，`random`请填写成随机数。

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
| ext    | 否   | string | 用户的 session 内容，腾讯 server 回包中会原样返回，可选字段，不需要就填空 |
| extend | 否   | string | 短信码号扩展号，格式为纯数字串，其他格式无效。默认没有开通，开通请联系 [腾讯云短信技术支持](https://cloud.tencent.com/document/product/382/3773) |
| params | 是   | array  | 模板参数，若模板没有参数，请提供为空数组                              |
| sig    | 是   | string | App 凭证，具体计算方式请参见下方说明                                           |
| sign   | 否   | string | 短信签名，如果使用默认签名，该字段可缺省                              |
| tel    | 是   | string | 国际电话号码，格式依据 [e.164](https://en.wikipedia.org/wiki/E.164) 标准为: `+[国家（或地区）码][手机号]` ，例如：`+8613711112222`， 其中前面有一个 `+` 号 ，`86` 为国家（或地区）码，`13711112222` 为手机号。  |
| time   | 是   | number | 请求发起时间，UNIX 时间戳（单位：秒），如果和系统时间相差超过10分钟则会返回失败    |
| tpl_id | 是   | number | 模板 ID，在控制台审核通过的模板 ID ， |


>?
>1. `tpl_id` 字段需填写审核通过的模板 ID
> 例如，模版 ID 对应的模板内容为：`您的{1}是{2}，请于{3}分钟内填写。如非本人操作，请忽略本短信。`，则上面请求参数组合后下发的内容为：`【腾讯云】您的验证码是1234，请于4分钟内填写。如非本人操作，请忽略本短信。` 
>2. 如果您有多个短信签名，请将需要的短信签名填入`sign`字段
>例如，您有`腾讯科技`和`腾讯云`两个签名，但需要以`腾讯云`签名发送短信，则`sign`字段可赋值为：`腾讯云` 
>3.  `sig` 字段根据公式 `sha256（appkey=$appkey&random=$random&time=$time&tel=$tel）`生成，其伪代码如下：
```json
string strtel = "+8613788888888"; //tel 的内容
string strAppKey = "5f03a35d00ee52a21327ab048186a2c4"; //sdkappid 对应的 appkey，需要业务方高度保密
string strRand = "7226249334"; //URL 中的 random 字段的值
string strTime = "1457336869"; //UNIX 时间戳
string sig = sha256(appkey=5f03a35d00ee52a21327ab048186a2c4&random=7226249334&time=1457336869&tel=+8613788888888)
           = ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4;
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
| result | 是   | number | 错误码，0表示成功（计费依据），非0表示失败, 参考 [错误码](https://cloud.tencent.com/document/product/382/3771)     |
| errmsg     | 是   | string | 错误消息，result 非0时的具体错误信息           |
| ext        | 否   | string | 用户的 session 内容，腾讯 server 回包中会原样返回 |
| nationcode | 是   | string | 国家（或地区）码                                        |
| fee    | 否   | number | 短信计费的条数，计费规则请参考 [国内短信内容长度计算规则](https://cloud.tencent.com/document/product/382/18058#.E7.9F.AD.E4.BF.A1.E5.86.85.E5.AE.B9.E9.95.BF.E5.BA.A6.E8.AE.A1.E7.AE.97.E8.A7.84.E5.88.99) 或 [国际/港澳台短信内容长度计算规则](https://cloud.tencent.com/document/product/382/18052#.E5.9B.BD.E9.99.85.E7.9F.AD.E4.BF.A1.E5.86.85.E5.AE.B9.E9.95.BF.E5.BA.A6.E8.AE.A1.E7.AE.97.E8.A7.84.E5.88.99)         |
| sid        | 否   | string | 本次发送标识 ID，标识一次短信下发记录          |


## DEMO
腾讯云短信服务为您提供了 [Java SDK](https://cloud.tencent.com/document/product/382/5804)、[PHP SDK](https://cloud.tencent.com/document/product/382/5804)、[Python SDK](https://cloud.tencent.com/document/product/382/5804)、[Node.js SDK](https://cloud.tencent.com/document/product/382/5804) 和 [C# SDK](https://cloud.tencent.com/document/product/382/5804) 供您参考，欢迎查阅。

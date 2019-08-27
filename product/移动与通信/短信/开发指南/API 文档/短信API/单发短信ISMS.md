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
    "msg": "您的验证码是 1234",
    "sig": "f272b136949f9e6faa5fae01cfc240caf5e6d89f2e18e8d47adf3d87ea0715fb",
    "tel": "+8613711112222",
    "time": 1457336869,
    "type": 0
}
```

| 参数   | 必选 | 类型   | 描述                                                                                     |
|--------|------|--------|------------------------------------------------------------------------------------------|
| ext    | 否   | string | 用户的 session 内容，腾讯 server 回包中会原样返回，可选字段，不需要就填空                    |
| extend | 否   | string | 短信码号扩展号，格式为纯数字串，其他格式无效。默认没有开通，开通请联系 [腾讯云短信技术支持](https://cloud.tencent.com/document/product/382/3773) |
| msg    | 是   | string | 短信消息，UTF-8编码，需要匹配审核通过的模板内容                                           |
| sig    | 是   | string | App 凭证，具体计算方式请参见下方说明                                                              |
| tel    | 是   | string | 国际电话号码，格式依据 [e.164](https://en.wikipedia.org/wiki/E.164) 标准为: `+[国家（或地区）码][手机号]` ，示例如：`+8613711112222`， 其中前面有一个 `+` 符号 ，`86` 为国家（或地区）码，`13711112222` 为手机号       |
| time   | 是   | number | 请求发起时间，UNIX 时间戳（单位：秒），如果和系统时间相差超过10分钟则会返回失败                       |
| type   | 是   | number | 短信类型，Enum{0：普通短信，1：营销短信}，要按需填值，不然会影响到业务的正常使用 |



>?
>1. `msg`字段需要匹配审核通过的模板内容
>例如，您的模板是`您的验证码是{1}。`，则`msg`字段可赋值为：`您的验证码是xxxx。`（其中 "xxxx" 为下发的验证码）
>2. 如果您有多个短信签名，请将需要的短信签名放在短信内容前面
>例如，您有`腾讯科技`和`腾讯云`两个签名，但需要以`腾讯云`签名发送短信，则`msg`字段可赋值为：`【腾讯云】您的验证码是xxxx。`（其中 "xxxx" 为下发的验证码）
>3. `sig`字段根据公式`sha256（appkey=$appkey&random=$random&time=$time&tel=$tel）`生成，其伪代码如下：
```json
string strtel = "+8613788888888"; //tel 的内容
string strAppKey = "5f03a35d00ee52a21327ab048186a2c4"; //sdkappid 对应的 appkey，需要业务方高度保密
string strRand = "7226249334"; //URL 中的 random 字段的值
string strTime = "1457336869"; //UNIX 时间戳
string sig = sha256(appkey=5f03a35d00ee52a21327ab048186a2c4&random=7226249334&time=1457336869&tel=+8613788888888)
           = f272b136949f9e6faa5fae01cfc240caf5e6d89f2e18e8d47adf3d87ea0715fb;
```


## 响应参数

```json
{
    "result": 0,
    "errmsg": "OK",
    "ext": "",
    "fee": 1,
    "nationcode": "86",
    "sid": "xxxxxxx"
}
```

| 参数       | 必选 | 类型   | 描述                                          |
|------------|------|--------|-----------------------------------------------|
| result | 是   | number | 错误码，0表示成功（计费依据），非0表示失败，参考 [错误码](https://cloud.tencent.com/document/product/382/3771)     |
| errmsg     | 是   | string | 错误消息，result 非0时的具体错误信息           |
| ext        | 否   | string | 用户的 session 内容，腾讯 server 回包中会原样返回 |
| nationcode | 是   | string | 国家（或地区）码                                        |
| fee    | 否   | number | 短信计费的条数，计费规则请参考 [国内短信内容长度计算规则](https://cloud.tencent.com/document/product/382/18058#.E7.9F.AD.E4.BF.A1.E5.86.85.E5.AE.B9.E9.95.BF.E5.BA.A6.E8.AE.A1.E7.AE.97.E8.A7.84.E5.88.99) 或 [国际/港澳台短信内容长度计算规则](https://cloud.tencent.com/document/product/382/18052#.E5.9B.BD.E9.99.85.E7.9F.AD.E4.BF.A1.E5.86.85.E5.AE.B9.E9.95.BF.E5.BA.A6.E8.AE.A1.E7.AE.97.E8.A7.84.E5.88.99)                             |
| sid        | 否   | string | 本次发送标识 ID，标识一次短信下发记录          |



## DEMO
腾讯云短信服务为您提供了 [Java SDK](https://cloud.tencent.com/document/product/382/5804)、[PHP SDK](https://cloud.tencent.com/document/product/382/5804)、[Python SDK](https://cloud.tencent.com/document/product/382/5804)、[Node.js SDK](https://cloud.tencent.com/document/product/382/5804) 和 [C# SDK](https://cloud.tencent.com/document/product/382/5804) 供您参考，欢迎查阅。

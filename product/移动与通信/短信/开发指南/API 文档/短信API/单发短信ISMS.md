## 接口描述

### 功能描述

 用户发送国际短信专用接口。


### URL 示例

`https://yun.tim.qq.com/v5/tlssmssvr/send<font color=red>i</font>sms?sdkappid=xxxxx&random=xxxx`

**注**：sdkappid 请填写您在腾讯云上申请到的，random 请填成随机数。

## 请求参数

```json
{   
    "tel": "+8613711112222", 
    "type": 0,
    "msg": "你的验证码是1234",
    "sig": "30db206bfd3fea7ef0db929998642c8ea54cc7042a779c5a0d9897358f6e9505",
    "time": 1457336869,
    "extend": "",
    "ext": ""
}
```

| 参数   | 必选 | 类型   | 描述                                                                                                                                                 |
|--------|------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| tel    |    |    | 电话号码，如需使用国际电话号码通用格式，如："+8613788888888"                                                               |
| type |    |    | 类型，0:普通短信;1:营销短信（强调：要按需填值，不然会影响到业务的正常使用） |
| msg |    |    | utf8编码，需要匹配审核通过的模板内容                                                                                                             |
| sig    |    |    | App 凭证，具体计算方式见下注                                                                                                                         |
| time   |    |    | unix时间戳，请求发起时间，如果和系统时间相差超过10分钟则会返回失败                                                                                                             |
| extend   |    |    | 通道扩展码，仅支持中国大陆，可选字段，默认没有开通(需要填空)；在短信回复场景中，腾讯server会原样返回，开发者可依此区分是哪种类型的回复|
| ext  |    |    | 用户的session内容，腾讯server回包中会原样返回，可选字段，不需要就填空。|


- 参数`tel`：

| 参数       | 必选 | 类型   | 描述     |
|------------|------|--------|----------|
| mobile     | 是   | string | 手机号码 |
| nationcode | 是   | string | 国家码   |

**注**：

1. "tel"字段为国际电话号码，其格式依据[e.164](https://en.wikipedia.org/wiki/E.164)标准  
示例："tel": "+8613711112222"，加号（+）用来代替任何国家的[冠码](https://zh.wikipedia.org/wiki/%E5%9B%BD%E9%99%85%E5%86%A0%E7%A0%81%E5%88%97%E8%A1%A8)，86为国家码，13711112222为手机号  
2. "msg"字段需要匹配审核通过的模板内容  
如果您的模板是"你的验证码是{1}"，则"msg"字段可赋值为："你的验证码是xxxx"。（其中"xxxx"为下发的验证码）  
如果您有多个短信签名，请将需要的短信签名放在短信内容前面  
例如您有"【腾讯科技】"，"【腾讯云】"两个签名，但是想以"【腾讯云】"签名发送短信，  
则"msg"字段可赋值为："【腾讯云】你的验证码是xxxx"。（其中"xxxx"为下发的验证码）
3. "extend"字段的配置请联系[腾讯云短信技术支持](/doc/product/382/联系我们) 
4. "sig"字段根据公式sha256(appkey=$appkey&random=$random&time=$time&tel=$tel)生成 
伪代码如下：
```
string strTel = "+8613711112222"; //tel字段的内容
string strAppKey = "dffdfd6029698a5fdf4"; //sdkappid对应的appkey，需要业务方高度保密
string strRand = "7226249334"; //url中的random字段的值
string strTime = "1457336869"; //unix时间戳
string sig = sha256(appkey=$strAppKey&random=$strRand&time=$strTime&tel=$strTel);
```

## 响应参数

```json
{
    "result": 0,
    "errmsg": "OK",
    "ext": "",
    "nationcode":"86",
    "sid": "xxxxxxx",
    "fee": 1
}
```

| 参数   | 必选 | 类型   | 描述                                                                                                                                                                                 |
|--------|------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| result | 是   | number | 错误码，0 表示成功(计费依据)，非 0 表示失败，参考 [错误码](https://cloud.tencent.com/document/product/382/3771)|
| errmsg | 是   | string | 错误消息，result 非 0 时的具体错误信息|
| ext    | 否   | string | 用户的 session 内容，腾讯 server 回包中会原样返回|
| nationcode    |    |  |       |
| sid    | 否   | string | 本次发送标识 id，标识一次短信下发记录 |
| fee    | 否   | number | 短信计费的条数，["fee" 字段计费说明](https://cloud.tencent.com/document/product/382/9556#.E7.9F.AD.E4.BF.A1.E5.86.85.E5.AE.B9.E9.95.BF.E5.BA.A6.E8.AE.A1.E7.AE.97.E8.A7.84.E5.88.99) |  
注：  
["fee"字段计费说明](/doc/product/382/常见问题#3-.E7.9F.AD.E4.BF.A1.E9.95.BF.E5.BA.A6)  
[result对应的错误码](/doc/product/382/错误码)                                                                                                                                         


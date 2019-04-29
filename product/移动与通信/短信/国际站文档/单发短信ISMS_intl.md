## API Description
### Description

 This API is used to send international SMS messages.

### URL Example

`POST https://yun.tim.qq.com/v5/tlssmssvr/sendisms?sdkappid=xxxxx&random=xxxx`

**Note**: Replace`xxxxx` in the field `sdkappid=xxxxx` with the sdkappid you applied for on Tencent Cloud, and replace `xxxx` in the field `random=xxxx` with a random number.

## Request Parameters

```json
{
    "ext": "",
    "extend": "",
    "msg": "Your verification code is 1234",
    "sig": "30db206bfd3fea7ef0db929998642c8ea54cc7042a779c5a0d9897358f6e9505",
    "tel": "+8613711112222",
    "time": 1457336869,
    "type": 0
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|------------------------------------------------------------------------------------------|
| ext | No | String | User's session content (optional). The Tencent server returns it as is. You can leave it empty if it is not needed. |
| extend | No | String | Extended SMS code which is valid only when it is in a format of pure numeral string. It is not enabled by default. [Contact SMS Helper](/document/product/382/3773) to enable it. |
| msg | Yes | String | UTF-8-encoded SMS message. It must match the content of the approved template. |
| sig | Yes | String | App credential. For more information on the calculation, please see the following. |
| tel | Yes | String | International phone number. Format is `+[Country code][Phone number]` defined based on [e.164](https://en.wikipedia.org/wiki/E.164) standard, for example: `+8613711112222`. It starts with a symbol `+`, followed by `86` (country code) and `13711112222` (phone number). |
| time | Yes | Number | The time to initiate the request. It is a unix timestamp (in sec). A failure message is returned if the time difference between the unix timestamp and the system time is greater than 10 minutes. |
| type | Yes | Number | SMS type. 0: Common SMS, 1: Marketing SMS. (Note: Enter the value as needed, otherwise the normal business will be affected.) |



**Note**:

1. The "msg" field needs to match the content of the approved template.
If the template is `Your verification code is {1}`, the "msg" field can be `Your verification code is xxxx`, where "xxxx" is the issued verification code.
If you have more than one SMS signatures, put the required SMS signature before SMS content. For example, if you have two signatures, "[Tencent Technology]" and "[Tencent Cloud]", and you want to send an SMS message with "[Tencent Cloud]",
the "msg" field can be `[Tencent Cloud] Your verification code is xxxx`, where "xxxx" is the issued verification code.
3. The "sig" field is generated according to the formula `sha256(appkey=$appkey&random=$random&time=$time&mobile=$mobile)`.
The pseudo code is as follows:
```json
string strtel = "+8613788888888"; //The content of tel
string strAppKey = "5f03a35d00ee52a21327ab048186a2c4"; //The appkey for the sdkappid, which must be kept confidential
string strRand = "7226249334"; //The value of the "random" field in the URL
string strTime = "1457336869"; //The Unix timestamp
string sig = sha256(appkey=5f03a35d00ee52a21327ab048186a2c4&random=7226249334&time=1457336869&tel=+8613788888888)
           = ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4;
```

## Response Parameters

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

| Parameter | Required | Type | Description |
|------------|------|--------|-----------------------------------------------|
| result | Yes | Number | Error code. 0: Successful (basis for billing). Other values: Failed. For more information, please see [Error Codes](/document/product/382/3771) |
| errmsg | Yes | String | Error message. The specific error message when the "result" is not 0 |
| ext | No | String | User's session content. The Tencent server returns it as is. |
| nationcode | Yes | String | Country code |
| fee | No | Number | Number of SMS messages billed. [About Billing](/document/product/382/9556) |
| sid | No | String | Delivery ID, indicating an SMS delivery record |

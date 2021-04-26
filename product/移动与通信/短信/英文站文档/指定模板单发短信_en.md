## API Description

### Feature

This API is used to send the SMS verification code, SMS notification, marketing SMS (not more than 450 characters) to users.

### URL Example

`POST https://yun.tim.qq.com/v5/tlssmssvr/sendsms?sdkappid=xxxxx&random=xxxx`

**Note**: Replace `xxxxx` in the field `sdkappid=xxxxx` with the sdkappid you applied for on Tencent Cloud, and replace `xxxx` in the field `random=xxxx` with a random number.

## Request Parameters

```json
{
    "ext": "",
    "extend": "",
    "params": [
        "Verification code",
        "1234",
        "4"
    ],
    "sig": "ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4",
    "sign": "Tencent Cloud",
    "tel": {
        "mobile": "13788888888",
        "nationcode": "86"
    },
    "time": 1457336869,
    "tpl_id": 19
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| ext | No | String | User's session content (optional). The Tencent server returns it as is. You can leave it empty if it is not needed. |
| extend | No | String | Extended SMS code which is valid only when it is a pure numeral string. It is not enabled by default. [Contact SMS Helper](/document/product/382/3773) to enable it. |
| params | Yes | Array | Template parameters. If the template has no parameters, leave it empty. |
| sig | Yes | String | App credential. For more information on the calculation, please see the following. |
| sign | No | String | SMS signature. To use the default signature, leave this field with the default value. |
| tel | Yes | Object | Phone number. If you need to use the universal international phone number format, such as "+8613788888888", use the API "sendisms". For more information, please see the following. |
| time | Yes | Number | The time to initiate the request. It is a unix timestamp (in sec). A failure message is returned if the time difference between the unix timestamp and the system time is greater than 10 minutes. |
| tpl_id | Yes | Number | The template ID approved on the console |

- Parameter `tel`:

| Parameter | Required | Type | Description |
|------------|------|--------|----------|
| mobile | Yes | String | Mobile number |
| nationcode | Yes | String | Country code |

**Notes**:

1. The approved template ID needs to be entered in the "tpl_id" field. Based on the above request parameters, the issued content is:
"[Tencent Cloud] Your verification code is 1234. This verification code is valid for 4 minutes. If you are not using our service, ignore this message."
If you have multiple SMS signatures, place the needed SMS signature in the "sign" field.
For example, if you have two signatures, "[Tencent Technology]" and "[Tencent Cloud]", and you want to send an SMS message with "[Tencent Cloud]", the "sign" field can be: "Tencent Cloud".
2. For the API [sendisms](/document/product/382/8717), the "tel" field is in the universal international phone number format, such as "+8613788888888".
3. The "sig" field is generated according to the formula sha256(appkey=$appkey&random=$random&time=$time&mobile=$mobile).
The pseudo codes are as follows:

```c++
string strMobile = "13788888888"; //The content of the "mobile" field of "tel"
string strAppKey = "5f03a35d00ee52a21327ab048186a2c4"; //The appkey for the sdkappid, which must be kept confidential
string strRand = "7226249334"; //The value of the "random" field in the URL
string strTime = "1457336869"; //The unix timestamp
string sig = sha256(appkey=5f03a35d00ee52a21327ab048186a2c4&random=7226249334&time=1457336869&mobile=13788888888)
           = ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4;
```

## Response Parameters

```json
{
    "result": 0,
    "errmsg": "OK",
    "ext": "",
    "fee": 1,
    "sid": "xxxxxxx"
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| result | Yes | Number | Error code. 0: Successful (basis for billing). Other values: Failed. For more information, please see [Error Codes](/document/product/382/3771). |
| errmsg | Yes | String | Error message. The specific error message when the "result" is not 0 |
| ext | No| String | User's session content. The Tencent server returns it as is. |
| fee | No | Number | Number of SMS messages billed. [About Billing](/document/product/382/18051) |
| sid | No | String | Delivery ID, indicating an SMS delivery record |

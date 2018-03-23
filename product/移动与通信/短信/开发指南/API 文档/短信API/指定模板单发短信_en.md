## API Description
### Description
This API is used to send SMS verification codes, SMS notifications, marketing SMS messages (not more than 450 characters) to users.

### URL Example
`https://yun.tim.qq.com/v5/tlssmssvr/sendsms?sdkappid=xxxxx&random=xxxx`

 **Note**: Enter the applied SDKAppID as `sdkappid`, and a random number as `random`.

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
|--------|------|--------|-----------------------------------------------------------------------------------------|
| ext | No | string | User's session content (optional). Tencent server returns it as is. You can leave it empty if it is not needed. |
| extend | Yes | string | The extended code of the channel (optional). Disabled by default. A value must be specified. |
| params | Yes | array | Template parameters. If the template has no parameters, leave it empty. |
| sig | Yes | string | App credential. For more information on the calculation, please see the following. |
| sign | No | string | SMS signature. To use the default signature, leave this field with the default value. |
| tel | Yes | object | Phone number. If you need to use the universal international phone number format, such as "+8613788888888", use the API "sendisms". For more information, please see the following. |
| time | Yes | number | The time to initiate the request. A failure message will be returned if the time difference between the unix timestamp and the system time is greater than 10 minutes. |
| tpl_id | Yes | number | The template ID approved on the console |

- Parameter `tel`:

| Parameter | Required | Type | Description |
|------------|------|--------|----------|
| mobile | Yes | string | Mobile number |
| nationcode | Yes | string | Country code |
**Notes**:
 1. The approved template ID needs to be entered in the `tpl_id` field. Based on the above request parameters, the issued content is:
 "[Tencent Cloud] Your verification code is 1234. This verification code is valid for 4 minutes. If you are not using our service, ignore the message."
 If you have multiple SMS signatures, place the needed SMS signature in the `sign` field.
 For example, if you have the two signatures "[Tencent Technology]" and "[Tencent Cloud]", and you want to send an SMS message with "[Tencent Cloud]", the `sign` field can be Tencent Cloud.
 2. To configure the `extend` field, [contact us](https://cloud.tencent.com/document/product/382/3773).
 3. For the API [sendisms](https://cloud.tencent.com/document/product/382/8717), enter the phone number in the universal international phone number format `tel` field, such as "+8613788888888".
 4. The `sig` field is generated according to the formula sha256(appkey=$appkey&random=$random&time=$time&mobile=$mobile)
 The pseudo codes are as follows:
```json
string strMobile = "13788888888"; //The content of the "mobile" field of "tel"
string strAppKey = "5f03a35d00ee52a21327ab048186a2c4"; //The appkey for the "sdkappid", which must be kept confidential
string strRand = "7226249334"; //The value of the "random" field in the URL
string strTime = "1457336869"; //The unix timestamp
string sig = sha256(appkey=5f03a35d00ee52a21327ab048186a2c4&random=7226249334&time=1457336869&mobile=13788888888)
           = ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4;
```
## Response parameters
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
|--------|------|--------|-----------------------------------------------|
| result | Yes | number | Error code. 0: Successful (basis for billing). Other values: Failed. |
| errmsg | Yes | string | Error message. The specific error message when the "result" is not 0. |
| ext | No| string | User's session content (optional). Tencent server returns it as is. |
| fee | No | number | Number of SMS messages billed. |
| sid | No | string | Delivery ID, indicating an SMS delivery record. |
**Note**:
[About Billing](https://cloud.tencent.com/document/product/382/9556#.E7.9F.AD.E4.BF.A1.E5.86.85.E5.AE.B9.E9.95.BF.E5.BA.A6.E8.AE.A1.E7.AE.97.E8.A7.84.E5.88.99)
[About Error code](https://cloud.tencent.com/document/product/382/3771)


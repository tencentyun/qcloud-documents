## API Description
### Feature
This API is used for Tencent Cloud SMS service to notify the business side of the delivery status of the SMS by calling back the service URL after an SMS message is sent to a user.

### URL Example
`POST https://yun.tim.qq.com/sms/smscallback`

## Request Parameters
```json
[
    {
        "user_receive_time": "2015-10-17 08:03:04",
        "nationcode": "86",
        "mobile": "13xxxxxxxxx",
        "report_status": "SUCCESS",
        "errmsg": "DELIVRD",
        "description": "The SMS message is successfully sent",
        "sid": "xxxxxxx"
    }
]
```

| Parameter | Required | Type | Description |
|-------------------|------|--------|---------------------------------------------------------|
| user_receive_time | Yes | String | The time when a user actually received the message |
| nationcode | Yes | String | Country code |
| mobile | Yes | String | Mobile number |
| report_status | Yes | String | Whether the message is received or not. SUCCESS: Successful. FAIL: Failed |
| errmsg | Yes | String | Error code for SMS receiving status. For more information, please see [Error Codes for Status](https://cloud.tencent.com/document/product/382/3771#2-.E7.8A.B6.E6.80.81.E5.9B.9E.E6.89.A7.E9.94.99.E8.AF.AF.E7.A0.81) |
| description | Yes | String | Description of SMS receiving status |
| sid | Yes | String | Delivery ID |
**Notes**:
A callback request may return the results of multiple SMS requests.

## Response Parameters
```json
{
    "result": 0,
    "errmsg": "OK"
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|------------------------------------------|
| result | Yes | Number | Error code. 0: Successful (basis for billing). Other values: Failed |
| errmsg | Yes | String | Error message. The specific error message when the "result" is not 0 |

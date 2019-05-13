## API Description
### Feature
This API is used for Tencent Cloud SMS service to notify the business side of the SMS reply by calling back the service URL after a user receives an SMS message and replies to it.

### URL Example
`POST https://yun.tim.qq.com/sms/smscallback`

## Request Parameters
```json
{
    "extend": "extended code",
    "mobile": "13xxxxxxxxx",
    "nationcode": "86",
    "sign": "SMS signature",
    "text": "User's reply",
    "time": 1457336869
}
```

| Parameter | Required | Type | Description |
|------------|------|--------|----------------------------------------------|
| extend | Yes | String | The extended code of the channel (optional). Disabled by default. A value must be specified. |
| mobile | Yes | String | Mobile number |
| nationcode | Yes | String | Country code |
| sign | Yes | String | SMS signature |
| text | Yes | String | User's reply |
| time | Yes | Number | Unix timestamp (in sec) |

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

## API Description
### Feature
This API is used to send voice notifications (consisting of Chinese characters, English letters, numbers or a combination with a length of not more than 100 characters) to Chinese users.

### URL Example
`POST https://yun.tim.qq.com/v5/tlsvoicesvr/sendvoiceprompt?sdkappid=xxxxx&random=xxxx`
**Note**: Replace `xxxxx` in the field `sdkappid=xxxxx` with the sdkappid you applied for on Tencent Cloud, and replace `xxxx` in the field `random=xxxx` with a random number.

## Request Parameters
```json
{
    "ext": "",
    "playtimes": 2,
    "promptfile": "Text of voice content",
    "prompttype": 2,
    "sig": "ecab4881ee80ad3d76bb1da68387428ca752eb885e52621a3129dcf4d9bc4fd4",
    "tel": {
        "mobile": "13788888888",
        "nationcode": "86"
    },
    "time": 1457336869
}
```

| Parameter | Required | Type | Description |
|------------|------|--------|------------------------------------------------------------------------|
| ext | No| String | User's session content. The Tencent server returns it as is. |
| playtimes | No | Number | The number times of playbacks (optional). Maximum is 3. Default is 2. |
| promptfile | Yes | String | UTF-8-encoded notification content. It supports Chinese characters, English letters, numbers or a combination, and must match the voice content template. |
| prompttype | Yes | Number | Voice type, which is always set to 2. |
| sig | Yes | String | App credential. For more information on the calculation, please see the following |
| tel | Yes | Object | Phone number |
| time | Yes | Number | The time to initiate the request (unix timestamp). A failure message is returned if the time difference between the unix timestamp and the system time is greater than 10 minutes. |

- Parameter `tel`:

| Parameter | Required | Type | Description |
|------------|------|--------|----------|
| mobile | Yes | String | Mobile number |
| nationcode | Yes | String | Country code |
**Note**:
1. The "sig" field is generated according to the formula sha256(appkey=$appkey&random=$random&time=$time&mobile=$mobile).
The pseudo codes are as follows:
```json
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
    "callid": "xxxx",
    "ext": ""
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|-----------------------------------------------|
| result | Yes | Number | Error code. 0: Successful (basis for billing). Other values: Failed |
| errmsg | Yes | String | Error message. The specific error message when the "result" is not 0 |
| callid | No | String | Indicate the ID of this delivery as well as a delivery record |
| ext | No | String | User's session content. The Tencent server returns it as is. |

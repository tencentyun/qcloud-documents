## API Description
### Feature
This API is used to modify an SMS signature.

### URL Example
`POST https://yun.tim.qq.com/v5/tlssmssvr/mod_sign?sdkappid=xxxxx&random=xxxx`
**Note**: Replace `xxxxx` in the field `sdkappid=xxxxx` with the sdkappid you applied for on Tencent Cloud, and replace `xxxx` in the field `random=xxxx` with a random number.

## Request Parameters
```json
{
    "pic": "xxxxx",
    "remark": "xxxxx",
    "sig": "c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df",
    "sign_id": 123,
    "text": "xxxxx",
    "time": 1457336869
}
```

| Parameter | Required | Type | Description |
|---------|------|--------|----------------------------------------------------------------------------------------------------------------------|
| pic | Yes | String | Add signature-related document screenshots in the format of string encoded with Base64 to the field (optional). The Base64 encoding tool: `http://base64.xpcha.com/indexie.php` |
| remark | Yes | String | New signature notes (optional), such as reason for application and usage scenarios |
| sig | Yes | String | App credential. For more information on the calculation, please see the following. |
| sign_id | Yes | Number | ID of the signature to be modified |
| text | Yes | String | New signature content without []. For example, if the signature is changed to [Tencent Technology], "Tencent Technology" should be entered. |
| time | Yes | Number | The time to initiate the request (unix timestamp). A failure message is returned if the time difference between the unix timestamp and the system time is greater than 10 minutes. |
**Notes**:
The "sig" field is generated according to the formula sha256(appkey=$appkey&random=$random&time=$time)
The pseudo codes are as follows:
```json
string strAppkey = "5f03a35d00ee52a21327ab048186a2c4"; //The appkey for the sdkappid, which must be kept confidential
string strRand = "7226249334"; //The value of the "random" field in the URL
string strTime = "1457336869"; //The unix timestamp
string sig = sha256(appkey=5f03a35d00ee52a21327ab048186a2c4&random=7226249334&time=1457336869)
           = c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df;
```
## Response Parameters
```json
{
    "result": 0,
    "msg": "",
    "data": {
        "id": 123,
        "status": 1,
        "text": "xxxxx"
    }
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|------------------------------------------|
| result | Yes | Number | Error code. 0: Successful (basis for billing). Other values: Failed. |
| msg | Yes | String | Error message. The specific error message when the "result" is not 0 |
| data | No | Object | Response data |

- Parameter `data`:

| Parameter | Required | Type | Description |
|--------|------|--------|-------------------------------------------------|
| id | Yes | Number | Signature ID |
| status | Yes | Number | Signature status. 0: Passed, 1: Pending approval, 2: Rejected. |
| text | Yes | String | Signature content |

## API Description
### Feature
This API is used to query the status of the SMS signature you applied for.

### URL Example
`POST https://yun.tim.qq.com/v5/tlssmssvr/get_sign?sdkappid=xxxxx&random=xxxx`
**Note**: Replace `xxxxx` in the field `sdkappid=xxxxx` with the sdkappid you applied for on Tencent Cloud, and replace `xxxx` in the field `random=xxxx` with a random number.

## Request Parameters
```json
{
    "sig": "c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df",
    "sign_id": [
        123,
        124
    ],
    "time": 1457336869
}
```

| Parameter | Required | Type | Description |
|---------|------|--------|--------------------------------------------------------------------|
| sig | Yes | String | App credential. For more information on the calculation, please see the following. |
| sign_id | Yes | Array | Signature ID, which can be specified with a value, for example, "sign_id":123 |
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
    "count": 3,
    "data": [
        {
            "id": 123,
            "reply": "xxxxx",
            "status": 0,
            "text": "xxxxx"
        }
    ]
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|-------------------------------------------------------|
| result | Yes | Number | Error code. 0: Successful (basis for billing); other values: Failed. |
| msg | Yes | String | Error message. The specific error message when the "result" is not 0. |
| count | Yes | Number | The number of returned message entries. It is valid when "result" is 0. The message content is in the "data" field. |
| data | No | Array | Response data |


- Parameters of the array element `data`:

| Parameter | Required | Type | Description |
|--------|------|--------|-------------------------------------------------|
| id | Yes | Number | Signature ID |
| reply | Yes | String | Approval information. If "status" is 2, the reason for rejection is provided. |
| status | Yes | Number | Signature status. 0: Passed, 1: Pending approval, 2: Rejected. |
| text | Yes | String | Signature content |

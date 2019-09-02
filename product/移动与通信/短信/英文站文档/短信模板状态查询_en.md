## API Description
### Description
This API is used to query the status of the SMS text message (or voice message) templates you applied for.


### URL Example
`POST https://yun.tim.qq.com/v5/tlssmssvr/get_template?sdkappid=xxxxx&random=xxxx`
**Note**: Replace `xxxxx` in the field `sdkappid=xxxxx` with the sdkappid you applied for on Tencent Cloud, and replace `xxxx` in the field `random=xxxx` with a random number.

## Request Parameters
```json
{
    "sig": "c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df",
    "time": 1457336869,
    "tpl_id": [
        123,
        124
    ],
    "tpl_page": {
        "max": 10,
        "offset": 0
    }
}
```

| Parameter | Required | Type | Description |
|----------|------|--------|---------------------------------------------------------------------------------|
| sig | Yes | String | App credential. For more information on how to calculate the signature, please see below. |
| time | Yes | Number | The time when the request is initiated. It is expressed as a Unix timestamp. A failure message is returned if the time difference between the Unix timestamp and the system time is greater than 10 minutes. |
| tpl_id | Yes | Array | An array of IDs of the template to be queried. It cannot be used together with tpl_page. |
| tpl_page | Yes | Object | Query the information of all templates by page. It cannot be used together with tpl_id. (The "total" field in the response package indicates the total number of templates) |

- Parameter `tpl_page` is composed as follows:

| Parameter | Required | Type | Description |
|--------|------|--------|----------------------------------------------------------------------------|
| max | Yes | Number | Number of entries pulled at a time. The maximum is 50 |
| offset | Yes | Number | Pull offset, with an initial value of 0. If you want to pull multiple times, the value must be the sum of the last offset and the value of the "max" field. |
**Note**:
The "sig" field is generated based on the formula sha256(appkey=$appkey&random=$random&time=$time)
The pseudo code is as follows:
```
string strAppkey = "5f03a35d00ee52a21327ab048186a2c4"; //The appkey for the sdkappid, which must be kept confidential
string strRand = "7226249334"; //The value of the "random" field in the URL
string strTime = "1457336869"; //The Unix timestamp
string sig = sha256(appkey=5f03a35d00ee52a21327ab048186a2c4&random=7226249334&time=1457336869)
           = c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df;
```
## Response Parameters
```json
{
    "result": 0,
    "msg": "",
    "total": 100,
    "count": 3,
    "data": [
        {
            "id": 123,
            "reply": "xxxxx",
            "status": 0,
            "text": "xxxxx",
            "type": 0
        }
    ]
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|-------------------------------------------------------|
| result | Yes | Number | Error code. 0: Successful (basis for billing). Other values: Failed |
| msg | Yes | String | Error message. The error message returned when "result" is not 0 |
| total | Yes | Number | The total number of templates applied. It is valid when "result" is 0 |
| count | Yes | Number | The number of information entries returned. It is valid when "result" is 0. The information is contained in the "data" field |
| data | Yes | Array | Detailed data |



- Parameter `data` is composed as follows:

| Parameter | Required | Type | Description |
|--------|------|--------|------------------------------------------------|
| id | Yes | Number | Template ID |
| status | Yes | Number | Template status. 0: Approved; 1: Pending; 2: Rejected. |
| reply | Yes | String | Approval information. If "status" is 2, the reason for rejection is returned |
| text | Yes | String | Template content |
| type | Yes | Number | SMS message type. 0: general message; 1: marketing message. |

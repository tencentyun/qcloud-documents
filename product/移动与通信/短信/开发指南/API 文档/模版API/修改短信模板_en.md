## API Description
### Description
This API is used to modify SMS text message (or voice message) templates

### URL Example
`POST https://yun.tim.qq.com/v5/tlssmssvr/mod_template?sdkappid=xxxxx&random=xxxx`
**Note**: Replace `xxxxx` in the field `sdkappid=xxxxx` with the sdkappid you applied for on Tencent Cloud, and replace `xxxx` in the field `random=xxxx` with a random number.

## Request Parameters
```json
{
    "remark": "xxxxx",
    "sig": "c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df",
    "text": "xxxxx",
    "time": 1457336869,
    "title": "xxxxx",
    "tpl_id": 123,
    "type": 0
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|--------------------------------------------------------------------|
| remark | Yes | String | Remarks for new template, such as reason for application and usage scenarios. This field is optional. |
| sig | Yes | String | App credential. For more information on how to calculate, please see below. |
| text | Yes | String | Content of new template |
| time | Yes | Number | The time at which the request is initiated. It is expressed as a Unix timestamp. A failure message is returned if the time difference between the Unix timestamp and the system time is greater than 10 minutes. |
| title | Yes | String | Name of new template (optional) |
| tpl_id | Yes | Number | ID of the template to be modified |
| type | Yes | Number | SMS message type. 0: general SMS message; 1: marketing SMS message |
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
    "data": {
        "id": 123,
        "status": 1,
        "text": "xxxxx",
        "type": 0
    },
    "msg": "",
    "result": 0
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|------------------------------------------|
| result | Yes | Number | Error code. 0: Successful (basis for billing). Other values: Failed. |
| msg | Yes | String | Error message. The error message returned when the "result" is not 0. |
| data | No | Object | Response data |


- Parameter `data` is composed as follows:

| Parameter | Required | Type | Description |
|--------|------|--------|------------------------------------------------|
| id | Yes | Number | Template ID |
| status | Yes | Number | Template status. 0: Approved; 1: Pending; 2: Rejected. |
| text | Yes | String | Template content |
| type | Yes | Number | SMS message type. 0: general message; 1: marketing message. |

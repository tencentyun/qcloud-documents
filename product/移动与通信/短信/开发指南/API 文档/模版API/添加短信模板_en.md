## API Description
### Description
Add text SMS (or voice SMS) templates

### URL Example
`https://yun.tim.qq.com/v5/tlssmssvr/add_template?sdkappid=xxxxx&random=xxxx`
**Note**: Enter the applied SDKAppID as `sdkappid`, and a random number as `random`.

## Request Parameters
```json
{
    "remark": "xxxxx",
    "sig": "c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df",
    "text": "xxxxx",
    "time": 1457336869,
    "title": "xxxxx",
    "type": 0
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|-------------------------------------------------------------------|
| remark | Yes | string | Template notes (optional), such as reason for application and usage scenarios |
| sig | Yes | string | App credential. For more information on the calculation, please see the following. |
| text | Yes | string | Template content |
| time | Yes | number | The time to initiate the request. A failure message will be returned if the time difference between the unix timestamp and the system time is greater than 10 minutes. |
| title | Yes | string | Template name (optional) |
| type | Yes | number | SMS type. 0: common SMS, 1: marketing SMS |
**Note**:
The `sig` field is generated according to the formula sha256 (appkey=$appkey&random=$random&time=$time)
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
        "text": "xxxxx",
        "type": 0
    }
}
```
| Parameter | Required | Type | Description |
|--------|------|--------|------------------------------------------|
| result | Yes | number | Error code. 0: Successful (basis for billing). Other values: Failed |
| msg | Yes | string | Error message. The specific error message when the `result` is not 0 |
| data | No | object | Response data |

- Parameter `data`:

| Parameter | Required | Type | Description |
|--------|------|--------|------------------------------------------------|
| id | Yes | number | Template ID |
| status | Yes | number | Template status. 0: Passed, 1: Pending approval, 2: Rejected |
| text | Yes | string | Template content |
| type | Yes | number | SMS type. 0: common SMS, 1: marketing SMS |




## API Description
### Feature
This API is used to pull the SMS status report in a certain period of time (the number of SMS messages submitted successfully, deliver reports, successful delivery reports, deleted delivery reports, and failure distribution).

### URL Example
`POST https://yun.tim.qq.com/v5/tlssmssvr/pullcallbackstatus?sdkappid=xxxxx&random=xxxx`
**Note**: Replace `xxxxx` in the field `sdkappid=xxxxx` with the sdkappid you applied for on Tencent Cloud, and replace `xxxx` in the field `random=xxxx` with a random number.

## Request Parameters
```json
{
    "begin_date": 2016090800,
    "end_date": 2016090823,
    "sig": "c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df",
    "time": 1457336869
}
```

| Parameter | Required | Type | Description |
|------------|------|--------|--------------------------------------------------------------------|
| begin_date | Yes | Number | Start time. Time to start pulling, which is accurate to hour. Format: yyyymmddhh |
| end_date | Yes | Number | End time. Time to end pulling, which is accurate to hour. Format: yyyymmddhh |
| sig | Yes | String | App credential. For more information on the calculation, please see the following. |
| time | Yes | Number | The time to initiate the request (unix timestamp). A failure message is returned if the time difference between the unix timestamp and the system time is greater than 10 minutes. |
**Note**:
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
    "data": {
        "status": 90,
        "status_fail": 10,
        "status_fail_0": 2,
        "status_fail_1": 2,
        "status_fail_2": 2,
        "status_fail_3": 2,
        "status_fail_4": 2,
        "status_success": 80,
        "success": 100
    },
    "errmsg": "OK",
    "result": 0
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|------------------------------------------|
| result | Yes | Number | Error code. 0: Successful (basis for billing). Other values: Failed. |
| errmsg | Yes | String | Error message. The specific error message when the "result" is not 0. |
| data | No | Object | Response data |


- Parameter `data`:

| Parameter | Required | Type | Description |
|----------------|------|--------|----------------|
| status | Yes | Number | The number of SMS reports |
| status_fail | Yes | Number | The number of deleted delivery reports |
| status_fail_0 | Yes | Number | Operator internal error |
| status_fail_1 | Yes | Number | Number is invalid or does not exist |
| status_fail_2 | Yes | Number | Out of service or powered off |
| status_fail_3 | Yes | Number | Blacklist |
| status_fail_4 | Yes | Number | Delivery frequency limit of operator |
| status_success | Yes | Number | The number of successful delivery reports|
| success | Yes | Number | The number of SMS messages submitted successfully |

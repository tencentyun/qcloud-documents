## API Description
### Feature
This API is used to pull the SMS delivery status in a certain period of time (the number of SMS messages sent, the number of SMS message sent successfully, the number of SMS messages billed).

### URL Example
`POST https://yun.tim.qq.com/v5/tlssmssvr/pullsendstatus?sdkappid=xxxxx&random=xxxx`
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
| sig | Yes | String | App credential. For more information on the calculation, please see the following |
| time | Yes | Number | The time to initiate the request (unix timestamp). A failure message is returned if the time difference between the unix timestamp and the system time is greater than 10 minutes. |
**Note**:
The "sig" field is generated according to the formula sha256(appkey=$appkey&random=$random&time=$time).
The pseudo codes are as follows:
```json
string strAppkey = "5f03a35d00ee52a21327ab048186a2c4"; // The appkey for the sdkappid, which must be kept confidential
string strRand = "7226249334"; //The value of the "random" field in the URL
string strTime = "1457336869"; //The unix timestamp
string sig = sha256(appkey=5f03a35d00ee52a21327ab048186a2c4&random=7226249334&time=1457336869)
           = c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df;
```
## Response Parameters
```json
{
    "result": 0,
    "errmsg": "OK",
    "data": {
        "bill_number": 120,
        "request": 101,
        "success": 100
    }
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|------------------------------------------|
| result | Yes | Number | Error code. 0: Successful (basis for billing). Other values: Failed. |
| msg | Yes | String | Error message. The specific error message when the "result" is not 0. |
| data | Yes | Object | Response data |


- Parameter `data`:

| Parameter | Required | Type | Description |
|-------------|------|--------|-------------------------------------------------------------------------------------------|
| bill_number | Yes | Number | The number of SMS messages billed. For example, among all SMS messages that are submitted successfully, 20 messages are long messages, each with a length of 80 bytes. A long SMS message is divided into two messages. So, the number of SMS messages billed is 80*1+20*2=120 |
| request | Yes | Number | The number of SMS messages submitted |
| success | Yes | Number | The number of SMS messages submitted successfully |

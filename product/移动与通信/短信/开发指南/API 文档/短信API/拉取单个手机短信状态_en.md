## API Description
### Feature
This API is used to pull the SMS status of a mobile phone, such as SMS delivery status and SMS reply.

### URL Example
`POST https://yun.tim.qq.com/v5/tlssmssvr/pullstatus4mobile?sdkappid=xxxxx&random=xxxx`
**Note**: Replace `xxxxx` in the field `sdkappid=xxxxx` with the sdkappid you applied for on Tencent Cloud, and replace `xxxx` in the field `random=xxxx` with a random number.


## Request Parameters
```json
{
    "begin_time": 1464624000,
    "end_time": 1464706800,
    "max": 10,
    "mobile": "13788888888",
    "nationcode": "86",
    "sig": "c13e54f047ed75e821e698730c72d030dc30e5b510b3f8a0fb6fb7605283d7df",
    "time": 1457336869,
    "type": 1
}
```

| Parameter | Required | Type | Description |
|------------|------|--------|--------------------------------------------------------------------|
| begin_time | Yes | Number | Time to start pulling. It is a unix timestamp (in sec). |
| end_time | Yes | Number | Time to end pulling. It is a unix timestamp (in sec). |
| max | Yes | Number | Number of entries pulled. Maximum value is 100 |
| mobile | Yes | string | Mobile number |
| nationcode | Yes | String | Country code |
| sig | Yes | String | App credential. For more information on the calculation, please see the following. |
| time | Yes | Number | The time to initiate the request. It is a unix timestamp (in sec). A failure message is returned if the time difference between the unix timestamp and the system time is greater than 10 minutes. |
| type | Yes | Number | The type of pulled content. 0: [SMS Delivery Status](https://cloud.tencent.com/document/product/382/5807); 1: [SMS Reply](https://cloud.tencent.com/document/product/382/5809)} |
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
    "errmsg": "ok",
    "count": 3,
    "data": []
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|------------------------------------------|
| result | Yes | Number | Error code. 0: Successful (basis for billing). Other values: Failed |
| errmsg | Yes | String | Error message. The specific error message when the "result" is not 0 |
| count | Yes | Number | The number of returned message entries. It is valid when "result" is 0. |
| data | No | Array | For more information, please see the following. |

## API Description
### Feature
This API is used for Tencent Cloud SMS service to notify the business side of the delivery status of voice notification by calling back the service URL after a voice notification is sent to a user.

### URL Example
`POST https://yun.tim.qq.com/voice/voicecallback`

## Request Parameters
```json
{
    "voiceprompt_callback": {
        "result": "0",
        "accept_time": "1470197211",
        "call_from": "",
        "callid": "xxxxxx",
        "end_calltime": "1470197221",
        "fee": "1",
        "mobile": "13xxxxxxxxx",
        "nationcode": "86",
        "start_calltime": "1470197196"
    }
}
```

| Parameter | Required | Type | Description |
|----------------------|------|--------|--------------|
| voiceprompt_callback | Yes | Object | Call back notification status |

- Parameter `voiceprompt_callback`:

| Parameter | Required | Type | Description |
|----------------|------|--------|---------------------------------------------------------|
| result | Yes | String | Error code. 0: Answered; 1: Not answered; 2: Exceptional. |
| accept_time | Yes | String | Time when a user answered the call |
| call_from | Yes | String | Calling number |
| callid | Yes | String | The ID of this delivery |
| end_calltime | Yes | String | Time to end a voice notification call |
| fee | Yes | String | Charged duration (in min) |
| mobile | Yes | String | Mobile number |
| nationcode | Yes | String | Country code |
| start_calltime | Yes | String | Time to start a voice notification call |
## Response Parameters
```json
{
    "result": 0,
    "errmsg": "OK"
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|------------------------------------------|
| result | Yes | Number | Error code. 0: Successful (basis for billing). Other values: Failed. |
| errmsg | Yes | String | Error message. The specific error message when the "result" is not 0. |

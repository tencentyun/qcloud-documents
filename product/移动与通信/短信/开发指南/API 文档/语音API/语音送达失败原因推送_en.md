## API Description
### Feature
This API is used to push the reason why voice verification code or voice notification is failed to be delivered to the target mobile number.

### URL Example
`POST https://yun.tim.qq.com/voice/voicecallback`

## Request Parameters
```json
{
    "voice_failure_callback": {
        "call_from": "075583763333",
        "callid": "xxxxxx",
        "failure_code": 8,
        "failure_reason": "Invalid number",
        "mobile": "13xxxxxxxxx",
        "nationcode": "86"
    }
}
```

| Parameter | Required | Type | Description |
|------------------------|------|--------|--------------------------|
| voice_failure_callback | Yes | Object | Call back the push of the reasons of voice delivery failure |

- Parameter `voice_failure_callback`:

| Parameter | Required | Type | Description |
|----------------|------|--------|----------------|
| call_from | Yes | String | Calling number |
| callid | Yes | String | The ID of this delivery |
| failure_code | Yes | Number | Error code |
| failure_reason | Yes | String | Reasons of failure |
| mobile | Yes | String | Mobile number |
| nationcode | Yes | String | Country code |
## Response Parameters
```json
{
    "result": 0,
    "errmsg": "OK"
}
```

| Parameter | Required | Type | Description |
|--------|------|--------|---------------------------|
| errmsg | Yes | String | The specific error message when the "result" is not 0 |
| result | Yes | Number | Error code. 0: Successful. Other values: Failed |

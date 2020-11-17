
## Description
When speech recognition is completed, the result is returned to the user via HTTP POST. And the user needs to build a service on the business server to receive the callback.

## Callback API Description

The speech recognition system returns the recognized result to the user by calling back the API. The fields in the API Body are described as follows:

| Field | Type | Description | 
| ------------- | ------------- | ---------- |
| code | Int32 | Task status. 0: Successful; other values: Failed | 
| message |String | Description of reason for success or failure | 
| requestId | Unit64 | Request ID. One request ID corresponds to one backend task ID | 
| appid | Unit64 | Tencent Cloud application ID |
| projecteid |  Unit64 | Tencent Cloud project ID |
| audioUrl |  String | URL of the audio file. If the audio source cannot be downloaded from the public network, the field is not included. |
| text |  String | Recognized text |
| audioTime | double | Audio duration |

>**Note**:
> To avoid unpacking failure due to presence of special characters (such as "&") in some fields, values of all fields must be performed with url_encode before being sent to users' business servers. After a value is obtained, perform url_decode to obtain the original value.

## User-returned Result

Upon receiving the HTTP POST callback request from the speech recognition system, the business server needs to return the result as follows:

| Name | Type | Description |
| --- | --- | --- |
| code | Int | Server error code. 0: Successful; other values: Failed |
| message | String | Description of reason for failure, such as business server overload. If the business server failed to return the result, the callback request will be resent at every interval. |


## Example
The sample API is as follows:
```
POST http://xx.yy.com/code=code&message=message&requestId=requestId&appid=appid&projectid=projectid&audioUrl=audioUrl&text=text&audioTime=audioTime
```
Upon receiving the request from the speech recognition system, the user needs to respond in json format:
```
{
"code" : 0,
"message" : "Successful"
}
```

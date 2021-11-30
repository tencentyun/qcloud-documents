## Description
When speech recognition is completed, the result is returned to the user via HTTP POST. And the user needs to build a service on the business server to receive the callback.

## Request Structure
The speech recognition system returns the recognized result to the user by calling back the API. The fields in the API Body are described as follows:

| Field | Type | Description | 
| ------------- | ------------- | ---------- |
| code | Int32 | Task status. 0: Successful; other values: Failed | 
| message |String | Description of reason for success or failure | 
| requestId | Unit64 | Request ID. One request ID corresponds to one backend task ID | 
| appid | Unit64 | Tencent Cloud application ID |
| projecteid | Unit64 | Tencent Cloud project ID |
| cosAppId | Unit64 | User COS business ID |
| audioKey | String | The unique identifier of the task on user side, such as uuId. The speech recognition system does not generate this value, but only transparently transmits it to the user when performing a callback for quick task positioning. | 
| audioBucket | String | Name of a user's COS Bucket |
| audioUrl | String | URL of the audio file |
| text | String | Recognized text |
| resultCosPath | String | The COS path of the result file. It is an absolute path beginning with Bucket root. |
| textUrl | String | The download URL of the result text file. |
| audioTime | double | Audio duration |

>**Note:**
> To avoid unpacking failure due to special characters (such as "&") in some fields, values of all fields must be performed with url_encode before being sent to users' business servers. After receiving the value, the business server performs url_decode to obtain the original value.

## User-returned Result

Upon receiving the HTTP POST callback request from the speech recognition system, the business server needs to return the result as follows:

| Name | Type | Description |
| --- | --- | --- |
| code | Int | Server error code. 0: Successful; other values: Failed |
| message | String | Description of reason for failure, such as business server overload. If the business server failed to return the result, the callback request will be resent at every interval. |

## Example
The sample API is as follows:
```
POST http://xx.yy.com/code=code&message=message&requestId=requestId&appid=appid&projectid=projectid&cosAppid=cosAppid&audioKey=audioKey&audioBucket=audioBucket&audioUrl=audioUrl&text=text&resultCosPath=resultCosPath&textUrl=textUrl&audioTime=audioTime
```
Upon receiving the request from the speech recognition system, the user needs to respond in json format:
```
{
  "code" : 0, 
  "message" : "Successful"
}
```








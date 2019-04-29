## Keyword Search Service

Keyword search service can help you search the business-focused words from your voice files. You can submit a maximum of 200 keywords at a time. The service searches the keywords from voice files and provides time offset and confidence level. Compared with the keyword matching for voice-to-text service, keyword search service is more efficient and has higher keyword recall rate. It is suitable for scenarios such as customer service voice quality check, App audio verification, LVB porn detection, etc.

## COS + Keyword Search Service

### How It Works
Four steps are involved in the technical framework:
1. You first need to a create a keyword search service template in the Artificial Audio Intelligence console, and then enter Bucket and request response method (writing into COS or callback notification).
2. Upload a voice file to Tencent Cloud COS input source Bucket.
3. COS calls back the voice data to the keyword search service to trigger auto speech recognition.
4. If the response method is writing into COS, then the keyword search service uploads the search result (a text file) to the target COS Bucket.
5. If the response method is callback notification, then the search result is sent to users through callback.
The overall technical framework of COS + Keyword Search is shown below:
![1](https://mc.qcloudimg.com/static/img/4269c37ec3464f3b9b36172310861142/guanjianci.png)
### Search Result Callback
When keyword search service is completed, if the response method is callback, the result is returned to the user via HTTP POST. And the user needs to build a service on the business server to receive the callback.

#### Request Structure
Keyword search service returns the recognized result to the user by calling back the API. The fields in the API Body are described as follows:

| Field | Type | Description | 
| ------------- | ------------- | ---------- |
| code | Int32 | Task status. 0: Successful; other values: Failed | 
| message |String | Description of reason for success or failure | 
| requestId | Unit64 | Request ID. One request ID corresponds to one backend task ID | 
| APPID | Unit64 | Tencent Cloud application ID |
| projecteid | Unit64 | Tencent Cloud project ID |
| cosAppId | Unit64 | User COS business ID |
| audioBucket | String | Name of a user's COS Bucket |
| audioUrl | String | URL of the audio file |
| text | String | Recognized text |
| audioTime | double | Audio duration |

>**Note:**
> To avoid unpacking failure due to special characters (such as "&") in some fields, values of all fields must be performed with url_encode before being sent to users' business servers. After receiving the value, the business server performs url_decode to obtain the original value.

#### Result Returned from User

Upon receiving the HTTP POST callback request from the keyword search service, the business server needs to return the result as follows:

| Name | Type | Description |
|---------|---------|---------|
| code | Int | Server error code. 0: Successful; other values: Failed |
| message | String | Description of reason for failure, such as business server overload. If the business server failed to return the result, the callback request will be resent at every interval. |

#### Example
The sample API is as follows:
```
POST http://xx.yy.com/ code=code&message=message&requestId=requestId &appid=appid& projectid = projectid & cosAppid=cosAppid&audioBucket=audioBucket&audioUrl = audioUrl &text=text& audioTime = audioTime
```
Upon receiving the request from the keyword search service, the user needs to respond in json format:
```
{
  "code" : 0, 
  "message" : "Successful"
}
```



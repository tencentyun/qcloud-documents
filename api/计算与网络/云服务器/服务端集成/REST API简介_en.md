## Overview of REST APIs 
REST APIs provided by Tencent Cloud are HTTP management APIs that serve as an entry for managing the App backend. 
The REST APIs supported by Instant Messaging can be found in the list of REST APIs. 
Although developed in early time, REST APIs have stronger managing capabilities than the App console that allows simple data management and group/one-to-one SMS messaging.
## Example 
The following displays how to use REST APIs to obtain all groups in the App. 
HTTPS request: 
```
POST /v4/group_open_http_svc/get_appid_group_list?accesstoken=xxx&identifier=group_root&sdkappid=88888888&contenttype=json HTTP/1.1Host: console.tim.qq.comContent-Length: 22 {    "Limit" : 2}
```
HTTPS response:
```
HTTP/1.1 200 OKServer: nginx/1.7.10Date: Fri, 09 Oct 2015 02:59:55 GMTContent-Length: 156Connection: keep-aliveAccess-Control-Allow-Origin: *Access-Control-Allow-Headers: X-Requested-WithAccess-Control-Allow-Methods: POST {    "ActionStatus": "OK",    "ErrorCode": 0,    "GroupIdList": [        {            "GroupId": "@TGS#1YTTZEAEG"        },        {            "GroupId": "@TGS#1KVTZEAEZ"        }    ],    "TotalCount": 58530}
```
## Calling Method 
### Request URLs 
The URLs of REST APIs are in the following format: 
https://console.tim.qq.com/$ver/$servicename/$command?sdkappid=$sdkappid&identifier=$identifier&usersig=$usersig&contenttype=json
The description and value of each parameter is as follows. The name and value of each parameter is case sensitive. 

| Parameter | Description | Value |
|---------|---------|---------|
| ver | Protocol version number. | v4 |
| servicename | Internal service name. Each servicename belongs to a service type. | Details can be found in the API descriptions. |
| command | Command word, used with servicename to identify a business feature. | Details can be found in the API descriptions. |
| sdkappid | Appid of an App in the IM cloud | You can obtain it when applying for access. |
| identifier | User name. Generally, it is the App administrator account when you call the REST API. | User name, which must be the App administrator account. |
| usersig | The signature of a user. | For an App using a standalone account system, please see [Here](http://avc.qcloud.com/wiki2.0/im/帐号登录集成/TLS后台API使用手册/TLS后台API使用手册.html#articleContent/h3%3acontains%7blinux%E4%B8%8B%E7%94%9F%E6%88%90sig%E5%92%8C%E6%A0%A1%E9%AA%8Csig%7d) to generate a sig. For an App using a hosted account system, please see [Here](http://avc.qcloud.com/wiki2.0/im/HIDE/如何/如何：生成用户凭证/如何：生成用户凭证.html) to generate a sig. |

Note: 
1. When you call the REST API on the App server, the identifier must be the App administrator account.
2. Every time you call the REST API, a usersig that can be used repeatedly is generated for the App. Pay attention to the validity period of the usersig. 
### HTTP Request Packet Format
REST APIs only support the POST method and the request packet is in JSON format. For specific packet format, please see descriptions of each API. 
Note: The POST packet cannot be empty. Even though a protocol packet does not need to have any information, an empty JSON object (i.e., {}) should be included.
### HTTP Error Codes 
Unless a network error (such as 502 error) occurs, the result after calling REST APIs is always 200. The API calling error codes and details are returned in the HTTP response packet. For more information, please see the section of HTTP response format. 
### HTTP Response Packet Format 
The response packets of REST APIs are in JSON format and have the following features:
```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    //Other response contents of REST APIs}
```
Response packets always include ActionStatus, ErrorInfo, and ErrorCode and their descriptions are as follows:

| Field | Type | Description |
|---------|---------|---------|
| ActionStatus | String | Request result. OK: succeeded. FAIL: failed. If the result is FAIL, ErrorInfo includes the failure reason. |
| ErrorInfo | String | Failure reason |
| ErrorCode | Integer | Error code. 0: succeeded. Other values: failed.|
## Common Error Codes of REST APIs 
| Error Code | Description | 
|---------|---------|
| 80001 | Message text is not secure | 
| 60002 | HTTP resolution error | 
| 60003 | JSON resolution error | 
| 60004 | Incorrect account in the request URI or JSON packet | 
| 60005 | Incorrect account in the request URI or JSON packet | 
| 60006 | sdkappid is restricted | 
| 60007 | The frequency of the REST API used for sdkappid request exceeds the limit | 
| 60008 | Service timed out | 
| 60009 | Error when requesting resources | 
## REST API Debugging Tools 
You can use the following tools to debug the REST APIs: 
### REST API Debugging Tools 
https://avc.qcloud.com/im/APITester/APITester.html
Use cases can be found [here](http://avc.qcloud.com/wiki2.0/im/新手指引/服务端集成指引/服务端集成指引.html#articleContent/h2%3acontains%7b%E5%AF%BC%E5%85%A5%E8%B4%A6%E5%8F%B7%E5%88%B0%E4%BA%91%E9%80%9A%E4%BF%A1%EF%BC%88%E4%BD%BF%E7%94%A8%E4%BA%91%E9%80%9A%E8%AE%AFREST%20API%E8%B0%83%E8%AF%95%E5%B7%A5%E5%85%B7%EF%BC%89%7d). 
### Postman 
Postman is a powerful Chrome plug-in used for debugging and sending HTTP requests for web ages. Use cases can be found [here](http://avc.qcloud.com/wiki2.0/im/新手指引/服务端集成指引/服务端集成指引.html#articleContent/h2%3acontains%7b%E4%B8%BA%E5%AF%BC%E5%85%A5%E7%9A%84%E8%AE%BE%E7%BD%AE%E8%B4%A6%E5%8F%B7%E7%9A%84%E5%9F%BA%E6%9C%AC%E8%B5%84%E6%96%99%EF%BC%88%E4%BD%BF%E7%94%A8Postman%EF%BC%89%7d).
### Debugging Tools in the PHP Server SDK 
PHP Server SDK includes a REST API debugging tool, TimRestApiGear.php, which can be used to initiate simple REST API calls. Use cases can be found [here](http://avc.qcloud.com/wiki2.0/im/新手指引/服务端集成指引/服务端集成指引.html#articleContent/h2%3acontains%7b%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E7%BE%A4%E7%BB%84%EF%BC%8C%E5%8C%85%E5%90%AB%E5%88%9D%E5%A7%8B%E7%BE%A4%E6%88%90%E5%91%98%EF%BC%88%E4%BD%BF%E7%94%A8PHP%20Server%20SDK%E4%B8%AD%E7%9A%84%E5%B7%A5%E5%85%B7%EF%BC%89%7d).
## Server SDK Integration 
### PHP Server SDK 
PHP Server SDK wraps the commonly used REST APIs into functions and exposes them to developers by API. 
The integration method can be found in PHP Server SDK. 


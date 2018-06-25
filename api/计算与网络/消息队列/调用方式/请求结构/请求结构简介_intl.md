The calls to Tencent Cloud APIs are achieved by sending requests to the server IP addresses of these APIs and adding relevant request parameters in the requests as described in API descriptions. A request for calling Tencent Cloud API is made up of the following elements:

## 1. Service Address
The service connection address of Tencent Cloud APIs depends on the modules. For more information, please see descriptions of APIs.

## 2. Communication Protocol
Most of Tencent Cloud APIs make communication over HTTPS to provide high-security channels.

## 3. Request Method
Tencent Cloud APIs support both POST and GET requests.
**Note:
1. The two methods cannot be used at the same time. If GET method is used, parameters are obtained from the Querystring. If POST method is used, parameters are obtained from the Request Body, and the parameters in the Querystring will be ignored. The rules for parameter formats are the same for both methods. Generally, POST method is used. Because GET may encounter unexpected problems if the parameter strings are too long.
2. Regardless of which request method is used by the user, all parameters need to be encoded.**

## 4. Request Parameters
Two types of parameters are needed for each request for Tencent Cloud APIs - common request parameters and API request parameters. Common request parameters are the parameters common to all APIs (For more information, refer to [Common Request Parameters](/doc/api/372/公共请求参数) section), while API request parameters are parameters specific to each API (For more information, refer to "Request Parameters" description of each API.)

## 5. Character Encoding
All requests for Tencent Cloud APIs and returned results use UTF-8 character set for encoding.

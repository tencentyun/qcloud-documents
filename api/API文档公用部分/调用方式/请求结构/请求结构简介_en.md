A Tencent Cloud API call is completed by sending a request towards Tencent Cloud API server address while adding corresponding request parameters into the request according to API description. A Tencent Cloud API request is composed of server address, communication protocol, request method, request parameters and character encoding. Details are described below:

## Service Address
The service connection address of Tencent Cloud APIs depends on the modules. For more information, please see the descriptions of each API.

## Communication Protocol
Most Tencent Cloud APIs communicate over HTTPS to provide high-security channels.

## Request Method
Tencent Cloud APIs support both POST and GET requests.

>**Note:**
1. POST and GET requests cannot be used together. If you use GET method, parameters are obtained from Querystring.If you use POST method, parameters are obtained from Request Body, in which case parameters in Querystring will be ignored. The parameter formats in these request methods are the same. We use GET requests generally. But it is recommended to use POST if the parameter strings are too long.
2. If GET method is used, all request parameters need to be encoded with URL encoding. This is not required if POST method is used.
3. The maximum length for GET requests depends on browsers and different server configurations. For example, the length limit is 2K for traditional IE browser, 8K for Firefox. For long API requests with a large number of parameters, it is recommended to use POST method to avoid request failure due to exceeded string length.
4. For POST requests, you need to pass parameters in the form of `x-www-form-urlencoded`, since the API on the cloud obtains request parameters from $_POST.

## Request Parameters
Two types of parameters are required for each Tencent Cloud API request: common request parameters and API request parameters. Common request parameters are required for all APIs (for more information, please see [Common Request Parameters](/doc/api/372/公共请求参数) section), while API request parameters are specific to each API. For more information, please see the "Request Parameters" description of each API.

## Character Encoding
All requests for Tencent Cloud APIs and their returned results are encoded using UTF-8 character set.


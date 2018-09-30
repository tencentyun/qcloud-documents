You can call a Tencent Cloud API by sending a request that contains the request parameters specified in the API description to the API service address. A Tencent Cloud API request involves service address, communication protocol, request method, request parameters and character encoding, as described below.

## Service Address
The service access address of a Tencent Cloud API depends on the module. For more information, see the description of each API.

## Communication Protocol
Most Tencent Cloud APIs communicate over HTTPS to provide high-security tunnels.

## Request Method
Tencent Cloud APIs support both POST and GET requests.

>**Notes:**
1. POST and GET requests cannot be used together. If the GET method is used, parameters are obtained from Querystring. If the POST method is used, parameters are obtained from Request Body, and the parameters in Querystring are ignored. The request parameters are organized in the same way in both types of requests. Generally, the GET method is used. If the parameter strings are too long, the POST method is used.
2. If the GET method is used, all request parameters need to be URL encoded. This is not required if the POST method is used.
3. The maximum length of GET requests varies with different browser and server settings. For example, the limit is 2 KB in traditional IE browsers, and 8 KB in Firefox browsers. For long API requests with a large number of parameters, it is recommended to use the POST method to avoid request failure due to the over-limit string length.
4. For POST requests, the input parameters take a form of `x-www-form-urlencoded`, because the cloud API acquires the request parameters from $_POST.

## Request Parameters
Two types of parameters are required for each Tencent Cloud API request: common request parameters and API request parameters. Common request parameters are required for each API (see [Common Request Parameters](/doc/api/372/公共请求参数)), while API request parameters are specific to each API (see "Request Parameters" in each API document.)

## Character Encoding
All requests for Tencent Cloud APIs and their returned results are encoded using the UTF-8 character set.


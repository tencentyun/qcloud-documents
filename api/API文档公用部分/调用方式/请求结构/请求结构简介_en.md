Calling Tencent Cloud APIs is implemented through sending a request to the server address for Tencent Cloud APIs and adding corresponding request parameters to the request in accordance with the API description. The Tencent Cloud API request structure consists of the following parts:

## 1. Service address
Tencent Cloud API service access address depends on specific modules. For details, see the description of each API.

## 2. Communication protocol
Most Tencent Cloud APIs use the HTTPS protocol to provide high-security communication channels.

## 3. Request mode
Tencent Cloud APIs support both POST and GET request modes.
**Note:
1. You cannot mix the two request modes. That is, if you use the GET method, then all parameters are obtained from Querystring; if you use the POST method, all parameters are obtained from the Request Body and those parameters in Querystring will be ignored. Both request modes use the same format of parameters. In general, GET is recommended. When the parameter string is too long, POST is recommended.
2. For the GET request mode, URL encoding is required for all request parameter values; for POST, you do not need to encode the parameters.
3. The max length of GET requests varies for different browser and server settings. For example, the max length is 2k for IE, and 8k for Firefox. For API requests with lots of parameters, use POST to avoid request failures caused by over-limit strings
## 4. Request parameters
Each Tencent Cloud API request requires two types of parameters: public request parameters and API request parameters. The public request parameter is used by every API. For details, refer to the [Public request parameters](/doc/api/372/Public request parameters) section; API request parameters are specific to each API. For details, see "Request parameters" for each API.

## 5. Character encoding
Tencent Cloud API requests and return results are encoded using the UTF-8 character set.
The process of calling Tencent Cloud APIs is achieved by sending requests to the server IP addresses of these APIs and adding relevant request parameters in the requests as described in the API descriptions. A request for calling Tencent Cloud API is made up of the following elements:

### Service Address

The service connection address of Tencent Cloud APIs depends on the modules. For more information, please see the descriptions of each API.

### Communication Protocol

Most of Tencent Cloud APIs communicate over HTTPS to provide high-security channels.

### Request Method

Tencent Cloud APIs support both POST and GET requests. 

> **Note:**
> 1. The two methods cannot be used at the same time. If GET method is used, parameters are obtained from Querystring. If POST method is used, parameters are obtained from Request Body, and the parameters in Querystring are ignored. 
> The rules for parameter formats are the same for both methods. Generally, GET method is used. If the parameter strings are too long, POST method is used.
> 2. If GET method is used, all request parameters need to be encoded with URL encoding. This is not required if POST method is used.

### Request Parameter

Two types of parameters are required for each Tencent Cloud API request: common request parameters and API request parameters. Common request parameters are the parameters common to all APIs (for more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650) section), while API request parameters are parameters specific to each API. For more information, please see "Request Parameters" description of each API.

### Character Encoding

All requests for Tencent Cloud APIs and their returned results are encoded using UTF-8 character set.


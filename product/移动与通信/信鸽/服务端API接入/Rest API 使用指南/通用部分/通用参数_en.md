The params field of each API URL structure has common parameters:

| Parameter Name | Type | Required | Description |
|-|-|-|-|
| access_id | uint | Yes | The unique identifier of the App, which is returned by the management system when the App is submitted. It can be found in [xg.qq.com Console](http://xg.qq.com) |
| cal_type | int | No | 0: offline calculation, 1: real-time statistics. Default: 0 |
| timestamp | uint | Yes | The unix timestamp of this request, which is used to confirm the validity period of the request. By default, a request whose timestamp is deviated from the server time (Beijing time) by more than 600 seconds will be rejected. |
| valid_time | uint | No | Determine the validity period (in sec) of the request in combination with timestamp. The maximum value is 600. If this parameter is not set or invalid, the validity period is calculated using the default 600 seconds. |
| sign | string | Yes | Content signature |

#### Rules for Generating Content Signatures:

1. Extract the request method (GET or POST);
2. Extract the url information of the request, including the IP or domain name of Host field or the path part of URI. Note: port of Host and querystring of Path are not included. The Host field must be included in the request, or the request is considered as invalid. For example, `openapi.xg.qq.com/v2/push/single_device` or `10.198.18.239/v2/push/single_device`;
3. Format the request parameter (excluding the sign parameter) into K=V mode. Note: all parameters should not be urlencoded when sign is calculated;
4. Arrange the formatted parameters in lexicographical ascending order of K, and note that the capital letters appear first in lexicographical order;
5. Combine request method, URL, formatted string in order, and secret_key of App;
6. Calculate the MD 5 value based on string formed in Step 5 above, and form a 32-bit hexadecimal (lowercase letter) string, i.e. the value of the this request sign (signature); Sign=MD5($http_method$url$k1=$v1$k2=$v2$secret_key). This signature value can basically guarantee that the request is sent by a valid sender and the parameter has not been modified, but it cannot avoid snooping.
  > For example, for POST request to the API `http://openapi.xg.qq.com/v2/push/single_device`, there are four parameters: access_id=123, timestamp=1386691200, Param1=Value1, Param2=Value2, and the secret_key is abcde.
The string combined in Step 5 above is: `POSTopenapi.xg.qq.com/v2/push/single_deviceaccess_id=123Param1=Value1Param2=Value2timestamp=1386691200abcde`. Note that the capital letters appear first in lexicographical order.
The MD 5 of the string is ccafecaef6be07493cfe75ebc43b7d53 which is used as the value of sign parameter.


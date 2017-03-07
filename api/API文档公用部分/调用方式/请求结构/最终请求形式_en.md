The final request URL consists of the following parts:
1) Request domain name: the domain name of the [DescribeInstances](/doc/api/229/831) request is cvm.api.qcloud.com. The actual request domain name varies with the module to which the API belongs. For details, refer to the description of each API.
2) Request path:  The request path for the cloud API is fixed at /v2/index.php.
3) Final request parameter strings:  Includes both public request parameters and API request parameters.

The combination rule for final request parameter strings is:
> https:// + Request method + Request server + Request path + ? + Request string

Therefore, we get the following final request URL, where the first six parameters are public request parameters, the other six parameters are API request parameters.

```
https://cvm.api.qcloud.com/v2/index.php?
Action=DescribeInstances
&SecretId=xxxxxxx
&Region=gz
&Timestamp=1465055529
&Nonce=59485
&Signature=mysignature
&instanceIds.0=ins-0hm4gvho
&instanceIds.1=ins-8oby8q00
&offset=0
&limit=20
&status=2
&zoneId=100003
```

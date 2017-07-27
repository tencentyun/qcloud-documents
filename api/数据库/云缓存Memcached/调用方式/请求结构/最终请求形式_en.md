The final request URL is made up of the following elements:
1) Request domain: The request domain for [Query List of Instances](/doc/api/229/831)(DescribeInstances) is cvm.api.qcloud.com. The actual request domain varies depending on the module to which the API belongs. For more information, please see descriptions of APIs.
2) Request path: The request path of Cloud API is always /v2/index.php.
3) Final request parameter string: By combining common request parameters and API request parameters,

the final format of request URL is as follows:
> https:// + request domain + request path + ? +final request parameter string

The final request URL is as follows. The first six parameters are common request parameters, and the last six ones are API request parameters.

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


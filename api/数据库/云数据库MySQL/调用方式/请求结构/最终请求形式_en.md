The final request URL consists of the following parts:
1) Request domain name: the domain name of the [DescribeInstances](/document/product/236/1266) request is cvm.api.qcloud.com. The actual request domain name varies with the module to which the API belongs. For details, refer to the description of each API.
2) Request path: The request path for the cloud API is "/v2/index.php".
3) Final request parameter strings: Includes both common request parameters and API request parameters.

The combination rule for final request parameter strings is:
> https:// + Request method + Request server + Request path + ? + Request string

Therefore, we get the following final request URL, where the first six parameters are common request parameters, the other six parameters are API request parameters.

```
https://cdb.api.qcloud.com/v2/index.php?
Action=DescribeCdbInstances
&SecretId=xxxxxxx
&Region=gz
&Timestamp=1465055529
&Nonce=59485
&Signature=mysignature
&InstanceIds.0=cdb-0hm4gvho
&InstanceIds.1=cdb-8oby8q00
```

The final request URL is made up of the following elements:
1) Request domain: The request domain for API [Bind EIP to CPM]()(EipBmBindRs) is eip.api.qcloud.com. The actual request domain varies depending on the module to which the API belongs. For more information, please see descriptions of APIs.
2) Request path: The request path of Cloud API is always /v2/index.php.
3) Final request parameter string: This includes common request parameters and API request parameters.

The final request URL is generated as follows:
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
&instanceId=cpm-09dx96dg
&eipId=eip-testcpm
```


The final request URL is made up of the following elements:
1) Request domain name: The request domain name of the API [Create Namespace](/doc/api/255/创建命名空间)(CreateNamespace) is: monitor.api.qcloud.com. The actual request domain varies depending on the module to which the API belongs. For more information, please see the description of each API.
2) Request path:  The request path of Cloud API is always /v2/index.php.
3) Final request parameter string:  API Request Parameters

The final request URL is generated as follows:
> https:// + request domain name + request path + ? +final request parameter string

The final request URL is as follows. The first six parameters are common request parameters, and the last one is API request parameter.

```
  https://monitor.api.qcloud.com/v2/index.php?
	Action=CreateNamespace
	&SecretId=xxxxxxx
	&Region=gz
	&Timestamp=1465055529
	&Nonce=59485
	&Signature=mysignature
	&namespace=name1
```


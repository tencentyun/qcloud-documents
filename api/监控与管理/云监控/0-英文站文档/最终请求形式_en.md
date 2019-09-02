The final request URL is made up of the following elements:
1) Request domain: The request domain of [Get the List of Monitoring Metrics](/doc/api/405/获取监控指标列表) (DescribeMetrics) is monitor.api.qcloud.com. The actual request domain varies depending on the module to which the API belongs. For more information, please see descriptions of APIs.
2) Request path: The request path of Cloud API is always /v2/index.php.
3) Final request parameter string: API Request Parameter.

The final request URL is generated as follows:
> https:// + request domain + request path + ? +final request parameter string

The final request URL is as follows. The first six parameters are common request parameters, and the last one is API request parameter.

```
  https://monitor.api.qcloud.com/v2/index.php?
	Action=DescribeMetrics
	&SecretId=xxxxxxx
	&Region=gz
	&Timestamp=1465055529
	&Nonce=59485
	&Signature=mysignature
	&namespace=qce/cvm
```


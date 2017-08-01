If a user wants to analyze the maximum CPU utilization of a process instead of a specific IP, he/she can aggregate the ip dimension and only use proc_name for analysis. This can be achieved by creating aggregation statistics if the original reported data remains unchanged. In this example, we use API for creation. Users can also create in CCM console:

```
#curl -k "https://monitor.api.qcloud.com/v2/index.php?Action=CreateMetricAggeration
&SecretId=AKIDlgRMo1j074b1l6nwReIvSk3sO0ssGQlC
&Nonce=56289
&Timestamp=1457433928
&Region=gz
&namespace=proc_monitor
&metricName=proc_cpu
&dimensionNames.0=proc_name
&statisticsType.0.period=300
&statisticsType.0.statistics=max
&Signature=3DeRgk4acf13QE7ecpUZfn4zkWc%3D"
```
The following values will be returned:

```
# {"code": 0, "message": ""}
```


Keep reporting the data, and view data of the specific aggregation dimension object (proc_name=xxx) after a period of time.

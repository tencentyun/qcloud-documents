Users need to log in to the CVM and configure the data reporting method. Data reporting requires you to report the metrics on Tencent CVM to Tencent Cloud Platform as specified. Example:

Report the CPU utilization of processes disk_cleaner and daemon2 on machines 1.2.3.4 and 1.2.3.5.

GET method is used. The data encoded with urlencode is as follows:

![](//mccdn.qcloud.com/static/img/3500c7bc10502733ee5403851ba57cc8/image.png)

>Note: For more information on how to generate Signature parameter, please see the data reporting steps in the [API for Data Reporting](https://www.qcloud.com/doc/api/255/4247)

```
#curl http://receiver.monitor.tencentyun.com:8080/report.cgi?Nonce=41718
&Timestamp=1457429445
&Region=gz
&Namespace=proc_monitor
&SecretId=AKIDlgRMo1j074b1l6nwReIvSk3sO0ssGQlC
&Signature=s%2FaiEege8nxOUh79rQ6WqzvEEMc%3D
&Data=[
{"dimensions":
    {"ip":"1.2.3.4","proc_name":"disk_cleaner"},
	 "value":30,
	 "metricName":"proc_cpu"
},
{"dimensions":
    {"ip":"1.2.3.5","proc_name":"daemon2"},
	 "value":20,
	 "metricName":"proc_cpu"
}
]
```
The following values will be returned:

```
# {"message": "OK", "code": 0}
```


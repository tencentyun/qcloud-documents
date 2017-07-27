## 1. Report Data

Report the CPU utilization of processes disk_cleaner and daemon2 on machines 1.2.3.4 and 1.2.3.5 by following the method below.

GET method is used. The data encoded with urlencode is as follows:

![](//mccdn.qcloud.com/static/img/3500c7bc10502733ee5403851ba57cc8/image.png)

>Note: For more information on how to generate Signature parameter, please see API [Authentication](https://www.qcloud.com/document/product/397/4247)

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

## 2. View Data
In this example, we use API for creation. Users can also create in CCM console.

Check whether the monitoring data of a specific object is calculated properly by calling the API GetMonitorData. For example, check the data of the object ip=1.2.3.5&proc_name=daemon2: monitored after 17:35:00:

>Note: For more information on how to generate Signature parameter, please see API [Authentication](https://www.qcloud.com/doc/api/255/4278)

```
#curl -k "https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&SecretId=AKIDlgRMo1j074b1l6nwReIvSk3sO0ssGQlC
&Nonce=34872
&Timestamp=1457431571
&Region=gz
&namespace=proc_monitor
&metricName=proc_cpu
&dimensions.0.name=proc_name
&dimensions.0.value=daemon2
&dimensions.1.name=ip
&dimensions.1.value=1.2.3.5
&period=300
&statistics=max
&startTime=2016-03-08+17%3A35%3A00
&Signature=FacKUqRPhqdEa%2FDvEHHAFAPKj8k%3D"
```
The following values will be returned:

```
{
    "code": 0,
    "message": "",
    "metricName": "proc_cpu",
    "startTime": "2016-03-08 17:35:00",
    "endTime": "2016-03-08 18:05:00",
    "period": "300",
    "dataPoints": {
        "ip=1.2.3.5&proc_name=daemon2": [
            "20.0",
            "90.0",
            "90.0",
            "90.0",
            "90.0",
            "90.0",
            "90.0"
        ]
    }
}
```



You can use the API GetMonitorData to view the data for a specified time range, or use the API GetMonitorRealTimeData to view the latest data of an object. For example, the real-time aggregation data in the previous step. In this example, we use API for creation. Users can also create in CCM console:

>Note: For more information on how to generate Signature parameter, please see API [Authentication](https://www.qcloud.com/doc/api/255/4278)


```
#curl -k "https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorRealtimeData
&SecretId=AKIDlgRMo1j074b1l6nwReIvSk3sO0ssGQlC
&Nonce=23034
&Timestamp=1457434224
&Region=gz
&namespace=proc_monitor
&metricName=proc_cpu
&dimensions.0.name=proc_name
&dimensions.0.value=daemon2
&period=300
&statistics=max
&Signature=mNyoxCKj8DRPdWqX%2Fw4fG%2BOCulA%3D"
```


You will get the latest real-time data as follows. The updateTime is the time stamp.

```
# {
    "code": 0,
    "message": "",
    "data": {
        "proc_name=daemon2": {
            "value": 90,
            "updateTime": "2016-03-08 18:55:00"
        }
    }
   }

```
　

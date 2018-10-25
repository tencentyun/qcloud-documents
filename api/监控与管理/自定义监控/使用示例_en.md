The following three examples show how to use custom monitoring APIs.

Usage scenario:
We have four disks, Disk 1 and Disk 2 located on machine 115.28.234.106, and Disk 3 and Disk 4 on 115.28.234.107.

| Disk Number | Machine IP | Disk Name |
|---------|---------|---------|
| 1 | 115.28.234.106 | Disk 1 |
| 2 | 115.28.234.106 | Disk 2 |
| 3 | 115.28.234.107 | Disk 3 |
| 4 | 115.28.234.107 | Disk 4 |

In example 1, Disk 1's maximum utilization in 5 minutes is analyzed based on the disk's utilization data you report.
In example 2, alarm analysis is performed on Disk 1's utilization. If the maximum utilization remains above 80% in 10 minutes (two statistical periods), an alarm is triggered and the data satisfying the alarm conditions is reported.
In example 3, the average disk utilization on machine 115.28.234.106 is analyzed. The data you report is analyzed by the aggregate dimension of machine IP to calculate the average utilization of the two disks on 115.28.234.106.


## 1. Example 1- Analyze Disk 1's maximum utilization in 5 minutes
### 1.1 Create Namespace

Machine's disk utilization data needs to be collected. The namespace is customized as "cvm", and all the information related to the machine can be placed under this namespace.
For more information about creating a namespace, please see [Create Namespace](/doc/api/255/创建命名空间).
The Action field of common request parameters is CreateNamespace. The request parameters of this API are shown below:

| Parameter Name | Description | Value |
|---------|---------|---------|
| namespace | It should not longer than 32 characters and is comprised of letters, numbers and underscores | cvm |

By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://monitor.api.qcloud.com/v2/index.php?Action=CreateNamespace
&Region=gz
&Timestamp=1465750149
&Nonce=46364
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWpTTyk18V2g%2FYi56hqls%3D
&namespace=cvm
```
The returned result of the above request is as follows, which indicates that the namespace has been successfully created.

```
{
  'code': 0,
  'message': ''
}
```

### 1.2 Create Metrics

We need to acquire the disk utilization of the machine. A metric named "diskusage" is created under the namespace cvm to represent the disk utilization.
The dimension of a disk is identified by the combination of machine IP and disk name.
To acquire the statistical data of the disk's maximum utilization, we add statistics type for the metric, that is, acquiring the maximum value among the reported data in 5 minutes. In this case, statisticsType.m.period and statisticsType.m.statistics are 300s and max respectively.
The reported disk utilization is an integer, which represents the percentage of usage, with the unit being %.
For more information about creating metrics, please see [Create Metrics](/doc/api/255/创建指标).
The Action field of common request parameters is CreateMetric. The request parameters of this API are shown below:


| Parameter Name | Description | Value |
|---------|---------|---------|
| namespace | Namespace | cvm |
| metricName | Metric name | diskusage |
| metricCname | Chinese name of metric | 'disk utilization' |
| dimensionNames.n | Statistical dimension name of the metric | 'ip','diskname' |
| statisticsType.m.period | Currently, only 300s is allowed | 300 |
| statisticsType.m.statistics | Statistics type | max |
| unit | Unit of the reported data | % |


By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://monitor.api.qcloud.com/v2/index.php?Action=CreateMetric
&Region=gz
&Timestamp=1465750149
&Nonce=46389
&SecretId=AKIDxxxxugEY
&Signature=5umi67UWpTTyk18V2g%2FYi56hqls%3D
&namespace=cvm
&metricName=diskusage
&metricCname='Disk utilization'
&dimensionNames.0=ip
&dimensionNames.1=diskname
&statisticsType.0.period=300
&statisticsType.0.statistics=max
&unit=%
```
The returned result of the above request is as follows, which indicates that the metric has been successfully created.

```
{
  'code': 0,
  'message': ''
}
```


### 1.3 Add Statistics Type

In addition to the maximum utilization of the disk under diskusage metric, we also need to get the average utilization of the disk under diskusage. For this reason, we add the statistics type avg.
The average of the reported data in 5 minutes is fetched, with the values of statisticsType.m.period and statisticsType.m.statistics being 300s and avg respectively.
For more information about adding statistics type, please see [Add Statistics Type](/doc/api/255/添加统计类型).
The Action field of common request parameters is CreateMetricStatisticsType. The request parameters of this API are shown below:

| Parameter Name |  Description | Value |
|---------|---------|---------|
| namespace | Namespace | cvm |
| metricName | Metric name | diskusage |
| dimensionNames.n | Combination of all the dimensions or the aggregate dimension of the metric | 'ip','diskname' |
| statisticsType.m.period | Currently, only 300s is allowed | 300 |
| statisticsType.m.statistics | Statistics type added for the aggregate dimension | avg |


By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://monitor.api.qcloud.com/v2/index.php?Action=CreateMetricStatisticsType
&Region=gz
&Timestamp=1468850149
&Nonce=46369
&SecretId=AKIDxxxxugEY
&Signature=5umi67UW6TTyk18V2g%2FYi56hqls%3D
&namespace=cvm
&metricName=diskusage
&dimensionNames.0=ip
&dimensionNames.1=diskname
&statisticsType.0.period=300
&statisticsType.0.statistics=avg
```
The returned result of the above request is as follows, which indicates that the statistics type has been successfully added.

```
{
  'code': 0,
  'message': ''
}
```

### 1.4 Report Data

Disk 1's utilization data needs to be reported continuously. With the statistical period set to 5 minutes, the data is reported every minute for a duration of 30 minutes.
The dimension name of Disk 1 is the combination of ip and diskname, with the dimension values being 115.28.234.106 and disk1.
In the reported data, a value of 30 indicates the Disk 1 on machine 115.28.234.106 currently has a utilization of 30%.

For more information about reporting data, please see [API for Data Reporting](/doc/api/255/数据上报接口). The Action field of common request parameters is PutMonitorData. The request parameters of this API are shown below:

| Parameter Name | Description | Value |
|---------|---------|---------|
| Namespace | Namespace | cvm |
| Data | Reported data | See below |

"Data" is composed as follows:

| Parameter Name | Description | Value |
|---------|---------|---------|
| dimensions | Combination of dimension key and value | {"ip":"115.28.234.106","diskname":"disk1"} |
| metricName | Metric name | diskusage |
| value | Reported value | 30 |

By combining common request parameters and API request parameters, you can get the final request as follows:
**Note: The domain name, port, request method and signature generation method for reporting in this API are different from those in other APIs**. For more information, please see [API for Data Reporting](/doc/api/255/数据上报接口).

```
http://receiver.monitor.tencentyun.com:8080/v2/index.php?Action=PutMonitorData
&SecretId=xxxxxxx
&Region=gz
&Timestamp=1402992826
&Nonce=345122
&Signature=mysignature
&Namespace=cvm
&Data=[{"dimensions":{"diskname":"disk1","ip":"115.28.234.106"},"metricName":"diskusage","value":30}]
```
The returned result of the above request is as follows, which indicates that the data has been successfully reported.

```
{
"code":0,
"message":"OK"
}
```


### 1.5 Query Data


You can use API [Query Monitoring Data of Metric](/doc/api/255/查询指标监控数据) or [Query Real-Time Monitoring Data of Metric](/doc/api/255/查询指标实时监控数据) to acquire results of statistical analysis of the data.
"Query Monitoring Data of Metric" is called here.
We need to obtain the utilization of Disk 1 between 2016-06-21 22:00:00 and 2016-06-21 22:15:00. The request is constructed as follows:
The namespace of Disk 1 is cvm, and the metric is diskusage.
The dimension name of Disk 1 is the combination of IP and diskname, with the dimension values being 115.28.234.106 and disk1.
The statistical granularity of monitoring data (period) is 300s by default. The statistical type (statistics) is max, which is the maximum value in 5 minutes.

For more information about querying monitoring data of metric, please see [Query Monitoring Data of Metric](/doc/api/255/查询指标监控数据). The Action field of common request parameters is GetMonitorData. The request parameters of this API are shown below:


| Parameter Name | Description | Value |
|---------|---------|---------|
| namespace | Namespace | cvm |
| metricName | Metric name | diskusage |
| dimensions.n.name | Combination of dimension names | ip,diskname |
| dimensions.n.value | Combination of dimension values | 115.28.234.106,disk1 |
| period | Statistical granularity of monitoring data. Currently, only 300s is allowed | 300 |
| statistics | Statistics type | max |
| startTime | Start time. Format is Y-m-d H:M:S. If left empty, it is 00:00:00 on current date by default | 2016-06-21 22:00:00|
| endTime | End time. If left empty, it is the current time by default | 2016-06-21 22:15:00 |
By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&Region=gz
&Timestamp=1434850149
&Nonce=46369
&SecretId=AKIDxxxxugEY
&Signature=5umi67UW6TTyk18V2g%2FYi56hqls%3D
&namespace=cvm
&metricName=diskusage
&dimensions.0.name=ip
&dimensions.1.name=diskname
&dimensions.0.value=115.28.234.106
&dimensions.1.value=disk1
&period=300
&statistics=max
&startTime=2016-06-21 22:00:00
&endTime=2016-06-21 22:15:00
```
The returned results of the above request are as follows:
```
{
    "code": 0,
    "message": "",
    "metricName": "diskusage",
    "startTime": "2016-06-21 22:00:00",
    "endTime": "2016-06-21 22:15:00",
    "period": "300",
    "dataPoints": {
        "diskname=disk1&ip=115.28.234.106": [
            80,
            70,
            50,
            60
        ]
    }
}
```
There are four data points in the output data - 80%, 70%, 50% and 60%. They represent the maximum utilization values of Disk 1 in four time periods -  21:55-22:00, 22:00-22:05, 22:05-22:10 and 22:10-22:15.

## 2. Example 2 - Alarm analysis for Disk 1's utilization

After completing Step 1.1, 1.2 and 1.3 in example 1
### 2.1 Create Alarm Rule

An alarm is triggered when the maximum utilization stays above 80% for 10 minutes (two consecutive periods).
The operatorType is greater-than sign, the threshold is 80, the number of consecutive periods is 2 (10 minutes), and the statistics type is max (we have added statistics types max and avg. max is used here).
The alarm receiver group is 8675, which is obtained by calling the API <a href="/doc/api/229/获取用户组列表" title="Obtain User Group List">Obtain User Group List</a>.
For more information about creating alarm rule, please see [Create Alarm Rule](/doc/api/255/创建告警规则). The Action field of common request parameters is CreateAlarmRule. The request parameters of this API are shown below:

| Parameter Name | Description | Value |
|---------|---------|---------|
| namespace | Namespace | cvm |
| metricName | Metric name | diskusage |
| dimensionNames.n | Combination of dimension names | ip,diskname |
| operatorType | Operator. Available values: >, <, >=, <=, !=, ==. This indicates the comparison method of the alarm rule | > |
| threshold | Number threshold above which an exception is triggered | 80 |
| constancy | Number of periods for the exception to persist before an alarm is triggered (an alarm is triggered if the exception persists for this number of periods) | 2 |
| period | Statistical period. Currently, only 300s is allowed | 300 |
| statistics | Statistics type | max |
| receiversId | Alarm receiver group ID | 8675 |


By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://monitor.api.qcloud.com/v2/index.php?Action=CreateAlarmRule
&Region=gz
&Timestamp=1434850149
&Nonce=46369
&SecretId=AKIDxxxxugEY
&Signature=5umi67UW6TTyk18V2g%2FYi56hqls%3D
&namespace=cvm
&metricName=diskusage
&dimensionNames.0=ip
&dimensionNames.1=diskname
&operatorType=>
&threshold=80
&period=300
&statistics=max
&constancy=2
&receiversId=8675
```
Output
```
{
    "code":"0",
    "message":"",
    "data":{
        "alarmRuleId":"policy-63uiec17"
    }
}
```


### 2.2 Bind Alarm Rule to Object
The generated alarm rule needs to be bound to Disk 1. Alarm rule ID is the output value of filed alarmRuleId in Step 2.1. In this example, it is policy-63uiec17.
The dimension values of "ip" and "diskname" are 115.28.234.106 and disk1 (identifying Disk 1).
For more information about binding alarm rule to object, please see [Bind Alarm Rule to Object](/doc/api/255/绑定告警规则和对象).
The Action field of common request parameters is BindAlarmRuleObjects. The request parameters of this API are shown below:

| Parameter Name | Description | Value |
|---------|---------|---------|
| alarmRuleId | Alarm rule ID | policy-63uiec17, which is the alarm rule ID generated in Step 2.1 |
| dimensions.n.name | Combination of dimensions | ip,diskname |
| dimensions.n.value | Combination of dimension values | 115.28.234.106,disk1 |

By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://monitor.api.qcloud.com/v2/index.php?Action=BindAlarmRuleObjects
&Region=gz
&Timestamp=1434850149
&Nonce=46369
&SecretId=AKIDxxxxugEY
&Signature=5umi67UW6TTyk18V2g%2FYi56hqls%3D
&alarmRuleId = policy-63uiec17 
&dimensions.0.name=ip
&dimensions.1.name=diskname
&dimensions.0.value=115.28.234.106
&dimensions.1.value=disk1
```
Output
```
{
    "code":"0",
    "message":""
}
```

### 2.3 Report Data

Report data continuously in the same way described in Step 1.4 of Example 1. The reported utilization value of disk stays above 80% for 15 minutes to trigger an alarm.

### 2.4 Query Alarm List

After reporting data for a certain period, you can query the alarm list to check if the utilization data of Disk 1 has triggered an alarm.

For more information about querying alarm list, please see [Query Alarm List](/doc/api/255/查询告警列表).
The namespace of Disk 1 is cvm, and the metric is diskusage.
The Action field of common request parameters is DescribeAlarmList. The request parameters of this API are shown below:

| Parameter Name | Description | Value |
|---------|---------|---------|
| namespace | Namespace | cvm |
| metricName | Metric name | diskusage |

By combining common request parameters and API request parameters, you can get the final request as follows:
Input
```
https://monitor.api.qcloud.com/v2/index.php?Action=DescribeAlarmList
&Region=gz
&Timestamp=1434850149
&Nonce=46369
&SecretId=AKIDxxxxugEY
&Signature=5umi67UW6TTyk18V2g%2FYi56hqls%3D
&namespace=cvm
&metricName=diskusage

```
Output
```
{
    "code": 0,
    "message": "",
    "data": {
        "alarmList": [
            {
                "metricName": "diskusage",
                "namespace": "cvm",
                "object": "ip=115.28.234.106&diskname=disk1",
                "occurTime": "2016-02-23 11:10:00",
                "recoverTime": "0000-00-00 00:00:00",
                "sendStatus": "0",
                "okStatus": "0",
                "smsSendCnt": "1",
				"alarmRuleId": "policy-63uiec17",
				"content": ""Disk Utilization" with statistical granularity of 300 seconds. "max>=80'%'" has persisted for 600 seconds"
            }
        ],
        "total": "1"
    }
}
```
It indicates that at 2016-02-23 11:10:00, the maximum utilization of Disk 1 has been above 80% for 600 seconds.
The recovery time of the alarm is 0000-00-00 00:00:00, which means the alarm has not recovered at the time of querying alarm. The utilization of Disk 1 is still greater than 80% and needs to be dealt with.


## 3. Example 3 - Analyze the average disk utilization of machine 115.28.234.106
### 3.1 Create Metric Aggregation

After completing Step 1.1 and 1.2 in example 1, we need to analyze the average utilization of all disks on machine 115.28.234.106. A new aggregation is created here.
This aggregation is under metric diskusage of namespace cvm. The aggregate dimension is the machine IP, statistical period is 300s, and statistics type is avg, the average value in 5 minutes.
For more information about creating a metric aggregation, please see [Create Metric Aggregation](/doc/api/255/创建指标聚合).
The Action field of common request parameters is CreateMetricAggregation. The request parameters of this API are shown below:

| Parameter Name |  Description | Value |
|---------|---------|---------|
| namespace | Namespace | cvm |
| metricName | Metric name | diskusage |
| dimensionNames.n | Name of dimension to be aggregated | 'ip' |
| statisticsType.m.period | Currently, only 300s is allowed | 300 |
| statisticsType.m.statistics | Statistics type added for the aggregate dimension | avg |


By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://monitor.api.qcloud.com/v2/index.php?Action=CreateMetricAggeration
&Region=gz
&Timestamp=1468850149
&Nonce=46369
&SecretId=AKIDxxxxugEY
&Signature=5umi67UW6TTyk18V2g%2FYi56hqls%3D
&namespace=cvm
&metricName=diskusage
&dimensionNames.0=ip
&statisticsType.0.period=300
&statisticsType.0.statistics=avg
```
The returned result of the above request is as follows, which indicates that the aggregation has been successfully created.

```
{
  'code': 0,
  'message': ''
}
```


### 3.2 Report Data

The utilization data of the two disks on machine 115.28.234.106 needs to be reported so that their average utilization can be analyzed.
The data of Disk 1 is reported in the same way described in Step 1.4.
The data of Disk 2 is reported as follows:
The disk name for Disk 2 is disk2.
The dimension names of Disk 2 are ip and diskname, and the dimension values are 115.28.234.106 and **disk2**.
"value" is 80, which indicates the utilization of disk2 on machine 115.28.234.106 at current time is 80%.

For more information about reporting data, please see [API for Data Reporting](/doc/api/255/数据上报接口). The Action field of common request parameters is PutMonitorData. The request parameters of this API are shown below:

| Parameter Name | Description | Value |
|---------|---------|---------|
| Namespace | Namespace | cvm |
| Data | Reported data | See below |

"Data" is composed as follows:

| Parameter Name | Description | Value |
|---------|---------|---------|
| dimensions | Combination of dimension key and value | {"ip":"115.28.234.106","diskname":"disk2"} |
| metricName | Metric name | diskusage |
| value | Reported value | 80 |

By combining common request parameters and API request parameters, you can get the final request as follows:
Note: The domain name, port, request method and signature generation method in this API are different from those in other APIs**. For more information, please see [API for Data Reporting](/doc/api/255/数据上报接口).

```
http://receiver.monitor.tencentyun.com:8080/v2/index.php?Action=PutMonitorData
&SecretId=xxxxxxx
&Region=gz
&Timestamp=1402992826
&Nonce=345122
&Signature=mysignature
&Namespace=cvm
&Data=[{"dimensions":{"diskname":"disk2","ip":"115.28.234.106"},"metricName":"diskusage","value":80}]
```
The returned result of the above request is as follows, which indicates that the data has been successfully reported.

```
{
"code":0,
"message":"OK"
}
```


### 3.3 Query Data

You can use API [Query Monitoring Data of Metric](/doc/api/255/查询指标监控数据) or [Query Real-Time Monitoring Data of Metric](/doc/api/255/查询指标实时监控数据) to acquire results of statistical analysis of the data.
"Query Monitoring Data of Metric" is called here.
We need to obtain the utilization of the two disks on machine 115.28.234.106 between 2016-06-21 22:00:0 and 2016-06-21 22:10:00. The request is constructed as follows:
The namespace is cvm, and the metric is diskusage.
The dimension name of machine IP is ip, and the dimension value is 115.28.234.106.
The statistical granularity of monitoring data (period) is 300s by default. The statistics type (statistics) is avg, which is the average in 5 minutes.

For more information about querying monitoring data of metric, please see [Query Monitoring Data of Metric](/doc/api/255/查询指标监控数据). The Action field of common request parameters is GetMonitorData. The request parameters of this API are shown below:


| Parameter Name | Description | Value |
|---------|---------|---------|
| namespace | Namespace | cvm |
| metricName | Metric name | diskusage |
| dimensions.n.name | Combination of dimension names | ip |
| dimensions.n.value | Combination of dimension values | 115.28.234.106 |
| period | Statistical granularity of monitoring data. Currently, only 300s is allowed | 300 |
| statistics | Statistics type | max |
| startTime | Start time. Format is Y-m-d H:M:S. If left empty, it is 00:00:00 on current date by default |2016-06-21 22:00:00|
| endTime | End time. If left empty, it is the current time by default | 2016-06-21 22:10:00 |
By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&Region=gz
&Timestamp=1434850149
&Nonce=46369
&SecretId=AKIDxxxxugEY
&Signature=5umi67UW6TTyk18V2g%2FYi56hqls%3D
&namespace=cvm
&metricName=diskusage
&dimensions.0.name=ip
&dimensions.0.value=115.28.234.106
&period=300
&statistics=avg
&startTime=2016-06-21 22:00:00
&endTime=2016-06-21 22:10:00
```
The returned results of the above request are as follows:
```
{
    "code": 0,
    "message": "",
    "metricName": "diskusage",
    "startTime": "2016-06-21 22:00:00",
    "endTime": "2016-06-21 22:10:00",
    "period": "300",
    "dataPoints": {
        "ip=115.28.234.106": [
            50,
            70,
            50,
        ]
    }
}
```
There are three data points in the output data - 50%, 70% and 50%. They represent the average utilization of Disk 1 and Disk 2 in three time periods - 21:55-22:00, 22:00-22:05, 22:05-22:10.



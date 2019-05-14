## 1. API Description

Domain name: monitor.api.qcloud.com


This API (GetMonitorData) is used to query the monitoring data of MongoDB product. The values for input parameters are as follows:
namespace: qce/cmongo
Fixed value for dimension name: target
dimensions.0.name=target
Dimensions.0.value=subject to the queried dimension

The following describes the value of dimensions.0.value.
MongoDB provided by Tencent Cloud is a cluster service. You can use the API to query the monitoring data of MongoDB from three dimensions: "cluster", "replica set", and "node".
among them:
"Cluster" represents a MongoDB instance you bought. You can query the number of read/write requests, capacity utilization, and timeout requests of the entire instance from this dimension.
The dimension of "replica set" can be used to query the internal capacity utilization and master-slave delay of a replica set in the cluster. A replica set instance contains only one replica set and each shard of a sharding instance is a replica.
The dimension of "node" can be used to query information such as CPU and memory of a node in a cluster.

Value Table of dimensions.0.value

| Value Type | Value Example | Description |
| ----- | ---------------------------------------- | ---------------------------------------- |
| Instance ID | cmgo-6ielucen | Instance ID is the unique identifier of a MongoDB instance. You can query this ID in [MongoDB Console](https://console.cloud.tencent.com/mongodb) or obtain it by calling MongoDB API. |
| Replica Set ID | cmgo-6ielucen_0cmgo-6ielucen_2 | The replica set ID is obtained by adding the "_index number" suffix behind the instance ID. The "index number" starts from 0, with a maximum value of "number of replica sets -1". A replica set instance contains only one replica set, so the suffix is always "_0". A sharding instance contains multiple shards and each shard is a replica set. For example, the replica set ID of the third shard is obtained by adding "_2" behind the instance ID. |
| Node ID | cmgo-6ielucen_0-node-primarycmgo-6ielucen_1-node-slave0cmgo-6ielucen_3-node-slave2 | The master node ID is obtained by adding the "-node-primary" suffix behind the replica set ID. The slave node ID is obtained by add "the index number of the salve node -node-slave". The "slave node index number" starts from 0, with a maximum value of "number of slave nodes -1". |

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see Common Request Parameters page. The Action field for this API is GetMonitorData.

### 2.1 Input Parameters

| Parameter Name               | Required   | Type       | Input Content    | Description                                       |
| ------------------ | ---- | -------- | ------- | ---------------------------------------- |
| namespace          | Yes    | String   | qce/cvm  | Namespace. Every Tencent Cloud product has a namespace. For more information, please see Input Content column.           |
| metricName         | Yes    | String   | Specific metric name | Metric name. For more information, please see 2.2                            |
| dimensions.0.name  | Yes    | String   | target  | Input parameter is target                                |
| dimensions.0.value | Yes    | String   | Subject to the queried dimension | Please see the Value Table in section 1 of API Description                     |
| period | No | Int | 60/300 | Interval for collecting monitoring data. Most metrics support a statistical granularity of 60s while some metrics only support a statistical granularity of 300s. Statistical granularity varies with metrics. Enter parameters by referring to the list of metric details in section 2.2. |
| startTime          | No    | Datetime | Start time    | Start time, such as "2016-01-01 10:25:00". Default is "00:00:00" of the current day |
| endTime            | No    | Datetime | End time    | End time. It is the current time by default. endTime cannot be earlier than startTime       |
### 2.2 Metric Name

| Metric                | Description                       | Unit   | Cluster/Instance | Value of dimensions.0.value |
| ----------------- | ------------------------ | ---- | ----- | -------------------- |
| inserts           | Number of writes per unit time                | Counts    | Cluster/Instance | Instance ID                 |
| reads             | Number of reads per unit time                | Counts    | Cluster/Instance | Instance ID                 |
| updates           | Number of updates per unit time                | Counts    | Cluster/Instance | Instance ID                 |
| deletes           | Number of deletes per unit time                | Counts    | Cluster/Instance | Instance ID                 |
| counts            | Number of counts per unit time              | Counts    | Cluster/Instance | Instance ID                 |
| aggregates        | Number of aggregates per unit time        | Counts    | Cluster/Instance | Instance ID                 |
| cluster_diskusage | Cluster capacity utilization                  | %    | Cluster/Instance | Instance ID                 |
| success           | Number of successful requests per unit time              | Counts    | Cluster/Instance | Instance ID                 |
| delay_10          | Number of successful requests with a delay of 10 ms-53 ms per unit time  | Counts    | Cluster/Instance | Instance ID                 |
| delay_50          | Number of successful requests with a delay of 50 ms-100 ms per unit time | Counts    | Cluster/Instance | Instance ID                 |
| delay_100         | Number of successful requests with a delay of over 100 ms per unit time    | Counts    | Cluster/Instance | Instance ID                 |
| replica_diskusage | Replica set capacity utilization                 | %    | Replica set   | Replica set ID                |
| slavedelay        | Average master-salve delay per unit time              | Second(s)    | Replica set   | Replica set ID                |
| cpuusage          | CPU utilization                   | %    | Node    | Node ID                 |
| memusage          | Memory utilization                    | %    | Node    | Node ID                 |
| qr                | Number of read requests in the queue           | Counts    | Node    | Node ID                 |
| qw                | Number of write requests in the queue          | Counts    | Node    | Node ID                 |
| conn              | Number of connections                      | Counts    | Node    | Node ID                 |
| netin             | Network inbound traffic                    | MB/s | Node    | Node ID                 |
| netout            | Network outbound traffic                    | MB/s | Node    | Node ID                 |


## 3. Output Parameters

| Parameter Name       | Type       | Description                  |
| ---------- | -------- | ------------------- |
| code       | Int      | Error code. 0: Successful; other values: Failed |
| message    | String   | Error message                |
| startTime  | Datetime | Start time                |
| endTime    | Datetime | End time                |
| metricName | String   | Metric name                |
| period     | Int      | Interval for collecting monitoring data              |
| dataPoints | Array    | Monitoring data list              |


## 4. Error Codes

| Error Code | Error Description    | Error Message                                 |
| ---- | ------- | ------------------------------------ |
| -502 | Resource does not exist   | OperationDenied.SourceNotExists      |
| -503 | Incorrect request parameter  | InvalidParameter                     |
| -505 | Parameter is missing    | InvalidParameter.MissingParameter    |
| -507 | Limit is exceeded    | OperationDenied.ExceedLimit          |
| -509 | Incorrect dimension group | InvalidParameter.DimensionGroupError |
| -513 | DB operation failed  | InternalError.DBoperationFail        |

## 5. Example

### 5.1 Query the Number of Requests with a Delay Greater Than 100 ms of a Cluster/Instance

Input
<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<a href="/doc/api/405/公共请求参数" title="Common Request Parameters">Common Request Parameters</a>
&namespace=qce/cmongo
&metricName=delay_100
&dimensions.0.name=target
&dimensions.0.value=cmgo-6ielucen
&startTime=2017-01-09 20:22:00
&endTime=2017-01-09 20:38:00
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "metricName": "delay_100",
    "startTime": "2017-01-09 20:20:00",
    "endTime": "2017-01-09 20:35:00",
    "period": 300,
    "dataPoints": [
        257,
        1399,
        2272
    ]
}
```
### 5.2 Query Master-Slave Delay of a Replica Set

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<a href="/doc/api/405/公共请求参数" title="Common Request Parameters">Common Request Parameters</a>
&namespace=qce/cmongo
&metricName=slavedelay
&dimensions.0.name=target
&dimensions.0.value=cmgo-6ielucen_0
&startTime=2017-01-09 20:22:00
&endTime=2017-01-09 20:38:00
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "metricName": "slavedelay",
    "startTime": "2017-01-09 20:20:00",
    "endTime": "2017-01-09 20:35:00",
    "period": 300,
    "dataPoints": [
        0,
        1,
        0
    ]
}
```
### 5.3 Query the Number of Connections of a Node

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<a href="/doc/api/405/公共请求参数" title="Common Request Parameters">Common Request Parameters</a>
&namespace=qce/cmongo
&metricName=slavedelay
&dimensions.0.name=target
&dimensions.0.value=cmgo-6ielucen_0
&startTime=2017-01-09 20:22:00
&endTime=2017-01-09 20:38:00
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "metricName": "conn",
    "startTime": "2017-01-09 20:20:00",
    "endTime": "2017-01-09 20:35:00",
    "period": 300,
    "dataPoints": [
        75,
        77,
        79,
        79
    ]
}
```








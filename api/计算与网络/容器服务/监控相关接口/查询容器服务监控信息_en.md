## 1. API Description
 
This API (GetMonitorData) is used to query CCS-related monitoring information.

Domain for API request: monitor.api.qcloud.com
**Note: This domain is different from other APIs of CCS.**

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| namespace | Yes | String | Namespace. Details are shown below |
| metricName | Yes | String | Metric name. Details of each metric are shown below |
| dimensions.n.name | Yes | String | Dimension name, which is used in combination with dimensions.n.value. Details are shown below |
| dimensions.n.value | Yes | String | Dimension value, which is used in combination with dimensions.n.name. Details are shown below | |
| period | No | Int| Statistical period for monitoring. Supported values: 60, 300, 3,600, and 86,400 (in sec). Details are shown below |
| startTime | No | Datetime | Start time, such as "2016-01-01 10:25:00".  The default is "00:00:00" of the current day |
| endTime | No | Datetime | End time. The default is the current time.  endTime cannot be earlier than startTime |

**Details of `namespace`**

| Available Value | Type | Description |
|---------|---------|---------|
| qce/cvm   | String      | Acquire the utilization of cluster's CPU and memory |
| qce/docker  | String | Acquire monitoring information about service, pod and container |

**Details of `dimensions`**
1) `dimensions.n.name` and `dimensions.n.value` are used to specify a monitoring object. Some objects can only be specified using multiple dimensions.
If you want to acquire `service_cpu_used` (service CPU utilization) when using CCS, you need to specify the following dimensions: `clusterId`, `serviceName`, `namespace`.

```
dimensions.0.name=clusterId
dimensions.0.value=cls-xxxxx
dimensions.1.name=serviceName
dimensions.1.value=test
dimensions.2.name=namespace
dimensions.2.value=default

```

2) The returned result, `dataPoints`, is an array. Each element in this array is data of a monitoring point. In the output result below, the three sets of data in `dataPoints` indicate the statistical data result in two time periods, 14:00-14:05 and 14:05-14:10. The returned data is a closed interval containing three points.
```
{
    "code": 0,
    "message": "",
    "metricName": "service_cpu_used",
    "startTime": "2016-06-28 14:10:00",
    "endTime": "2016-06-28 14:20:00",
    "period": 300,
    "dataPoints": [
        5.6,
        6.4,
        7.7
    ]
}
```

**Details of `period`**

| Available Value | Type | Description |
|---------|---------|---------|
| 60   | Int  | 1-minute granularity |
| 300  | Int |5-minute granularity |
| 3600  | Int |1-hour granularity |
| 86400  | Int |1-day granularity |

## 3. Output Parameters
| Parameter Name | Type    | Description                                 |
| ---- | ------- | ------------------------------------ |
| code | Int   |  Error code. 0: Successful; other values: Failed |
| message | String | Returned message|
| startTime | Datetime    | Start time  |
| endTime | Datetime   | End time |
| metricName | String | Metric name |
| period| Int  | Statistical period for monitoring |
| dataPoints| Array  | Monitoring data list |

## 4. Error Codes

| Error Code | Error Description    | Description                                 |
| ---- | ------- | ------------------------------------ |
| -502 | Resource does not exist   | OperationDenied.SourceNotExists      |
| -503 | Invalid request parameter  | InvalidParameter                     |
| -505 | Parameter missing    | InvalidParameter.MissingParameter    |
| -507 | Limit exceeded    | OperationDenied.ExceedLimit          |
| -509 | Invalid dimension combination | InvalidParameter.DimensionGroupError |
| -513 | DB operation failed  | InternalError.DBoperationFail        |


## 5. Monitoring Metrics at Cluster Dimension
When you query the monitoring data of cluster, the values of input parameters are as follows:

Value for dimension name: `docker_clusterid`

namespace: qce/cvm

dimensions.0.name=docker_clusterid
"dimensions.0.value" is cluster ID. Enter the clusterId (cluster ID) field returned via API [Query Cluster List](https://cloud.tencent.com/document/api/457/9448).


**Available values of `metricName`**

| Monitoring Item | Metric Name | Unit  | Description  |
|---------|---------|---------|-----|
| Cluster CPU utilization |  dc_cpu_usage | % | Average CPU utilization of nodes in the cluster |
| Cluster memory utilization |  dc_mem_usage | % | Average memory utilization of nodes in the cluster |

**Example of querying monitoring data of cluster dimension**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&namespace=qce/cvm
&metricName=dc_cpu_usage
&dimensions.0.name=docker_clusterid
&dimensions.0.value=cls-xxxxx
&startTime=2017-03-28 14:10:00
&endTime=2016-03-28 15:10:00
&period=60
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "dc_cpu_usage",
	"startTime": "2017-03-28 14:10:00",
	"endTime": "2016-03-28 15:10:00",
	"period": 60,
	"dataPoints": [
		30,
		40,
        ....
	]
}
```



## 6. Monitoring Metrics at Service Dimension
When you query the monitoring data of service dimension, the values of input parameters are as follows:

Values for dimension name: `clusterId`, `serviceName`, `namespace`

namespace: qce/docker

dimensions.0.name=clusterId
`dimensions.0.value` is cluster ID. Enter the `clusterId` (cluster ID) field returned via API [Query Cluster List](https://cloud.tencent.com/document/api/457/9448).

dimensions.1.name=serviceName
`dimensions.1.value` is service name. Enter the `serviceName` (service name) field returned via API [Query Service List](https://cloud.tencent.com/document/api/457/9440).

dimensions.2.name=namespace
`dimensions.2.value` is namespace name. Enter the `namespace` (namespace) field returned via API [Query Service List](https://cloud.tencent.com/document/api/457/9440).


**Available values of `metricName`**

| Monitoring Item | Metric Name | Unit  | Description  |
|---------|---------|---------|-----|
| Service CPU usage | service_cpu_used | Core | Total number of CPUs used by all the container pods in the service |
| Service CPU utilization (ratio to cluster) | service_cpu_usage_for_cluster | % | The ratio of service CPU utilization to cluster |
| Service memory usage | service_mem_used | MiB | Total amount of memory used by all the container pods in the service |
| Service memory utilization (ratio to cluster) | service_mem_usage_for_cluster | % | The ratio of service memory utilization to cluster |
| Service network inbound traffic | service_in_flux  | MB | Total inbound traffic of all the pods in the service within the time window |
| Service network outbound traffic | service_out_flux | MB | Total outbound traffic of all the pods in the service within the time window |
| Service network inbound bandwidth | service_in_bandwidth | Mbps | Total inbound bandwidth of all the pods in the service |
| Service network outbound bandwidth | service_out_bandwidth | Mbps | Total outbound bandwidth of all the pods in the service |
| Service network inbound packets | service_in_packets | pps | Total inbound packets of all the pods in the service |
| Service network outbound packets | service_out_packets | pps | Total outbound packets of all the pods in the service |

**Example of querying monitoring data of service dimension**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&namespace=qce/docker
&metricName=service_cpu_used
&dimensions.0.name=clusterId
&dimensions.0.value=cls-xxxxx
&dimensions.1.name=serviceName
&dimensions.1.value=test
&dimensions.2.name=namespace
&dimensions.2.value=default
&startTime=2017-03-28 14:10:00
&endTime=2016-03-28 15:10:00
&period=60
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "service_cpu_used",
	"startTime": "2017-03-28 14:10:00",
	"endTime": "2016-03-28 15:10:00",
	"period": 60,
	"dataPoints": [
		30,
		40,
        ....
	]
}
```


## 7. Monitoring Metrics at Pod Dimension
When you query the monitoring data of pod dimension, the values of input parameters are as follows:

Values for dimension name: clusterId, serviceName, namespace, podName

namespace: qce/docker

dimensions.0.name=clusterId
`dimensions.0.value` is cluster ID. Enter the clusterId (cluster ID) field returned via API [Query Cluster List](https://cloud.tencent.com/document/api/457/9448).

dimensions.1.name=serviceName
`dimensions.1.value` is service name. Enter the serviceName (service name) field returned via API [Query Service List](https://cloud.tencent.com/document/api/457/9440).

dimensions.2.name=namespace
`dimensions.2.value` is namespace name. Enter the namespace (namespace) field returned via API [Query Service List](https://cloud.tencent.com/document/api/457/9440).

dimensions.3.name=podName
`dimensions.3.value` is pod name. Enter the name (pod name) field returned via API [Query Service Pod List](https://cloud.tencent.com/document/api/457/9433).



**Available values of `metricName`**

| Monitoring Item | Metric Name | Unit  | Description  |
|---------|---------|---------|-----|
| Pod network inbound bandwidth | pod_in_bandwidth | Mbps | Containers in the same pod share a network. It is the network inbound bandwidth of the pod |
| Pod network outbound bandwidth | pod_out_bandwidth | Mbps | Containers in the same pod share a network. It is the network outbound bandwidth of the pod |
| Pod network inbound traffic | pod_in_flux | MB | Containers in the same pod share a network. It is the network inbound traffic of the pod |
| Pod network outbound traffic | pod_out_flux | MB | Containers in the same pod share a network. It is the network outbound traffic of the pod) |
| Pod network inbound packets | pod_in_packets | pps | Containers in the same pod share a network. It is the network inbound packets of the pod |
| Pod network outbound packets | pod_out_packets | pps | Containers in the same pod share a network. It is the network outbound packets of the pod |

**Example of querying monitoring data of pod dimension**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&namespace=qce/docker
&metricName=pod_in_bandwidth
&dimensions.0.name=clusterId
&dimensions.0.value=cls-xxxxx
&dimensions.1.name=serviceName
&dimensions.1.value=test
&dimensions.2.name=namespace
&dimensions.2.value=default
&dimensions.3.name=podName
&dimensions.3.value=test-3488000495-nj6s9
&startTime=2017-03-28 14:10:00
&endTime=2016-03-28 15:10:00
&period=60
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "pod_in_bandwidth",
	"startTime": "2017-03-28 14:10:00",
	"endTime": "2016-03-28 15:10:00",
	"period": 60,
	"dataPoints": [
		30,
		40,
        ....
	]
}
```


## 8. Monitoring Metrics at Container Dimension
When you query the monitoring data of container dimension, the values of input parameters are as follows:

Values for dimension name: `clusterId`, `serviceName`, `namespace`, `podName`, `containerId`

namespace: qce/docker

dimensions.0.name=clusterId
`dimensions.0.value` is cluster ID. Enter the `clusterId` (cluster ID) field returned via API [Query Cluster List](https://cloud.tencent.com/document/api/457/9448).

dimensions.1.name=serviceName
`dimensions.1.value` is service name. Enter the `serviceName` (service name) field returned via API [Query Service List](https://cloud.tencent.com/document/api/457/9440).

dimensions.2.name=namespace
`dimensions.2.value` is namespace name. Enter the `namespace` (namespace) field returned via API [Query Service List](https://cloud.tencent.com/document/api/457/9440).

dimensions.3.name=podName
`dimensions.3.value` is pod name. Enter the `name` (pod name) field returned via API [Query Service Pod List](https://cloud.tencent.com/document/api/457/9433).


dimensions.4.name=containerId
`dimensions.4.value` is container name. Enter the containerId (container ID) field returned via API [Query Service Pod List](https://cloud.tencent.com/document/api/457/9433). **Note: Container ID only needs to be entered with the first 12 characters**


**Available values of `metricName`**

| Monitoring Item | Metric Name | Unit  | Description  |
|---------|---------|---------|-----|
| Container CPU usage | container_cpu_used | Core | Number of CPUs in use |
| Container CPU utilization (ratio to CVM) | container_cpu_usage_for_node | % | Ratio of container CPU utilization to CVM |
| Container CPU utilization (ratio to Request) | container_cpu_usage_for_request | % | Ratio of container CPU utilization to Request |
| Container CPU utilization (ratio to Limit) | container_cpu_usage_for_limit | % | Ratio of container CPU utilization to Limit |
| Container memory usage | container_mem_used | MiB | Amount of memory in use |
| Container memory utilization (ratio to CVM) | container_mem_usage_for_node | % | Ratio of container memory utilization to CVM |
| Container memory utilization (ratio to Request) | container_mem_usage_for_request | % | Ratio of container memory utilization to Request|
| Container memory utilization (ratio to Limit) | container_mem_usage_for_limit | % | Ratio of container memory utilization to Limit |
| Container's disk read traffic | container_disk_read_traffic | KB/s | Traffic consumed in reading disk by container |
| Container's disk write traffic | container_disk_write_traffic | KB/s | Traffic consumed in writing disk by container |
| Container's disk read IOPS | container_disk_read | count | IOPS of read by container to disk |
| Container's disk write IOPS | container_disk_write | count | IOPS of write by container to disk |

**Example of querying monitoring data of container dimension**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&namespace=qce/docker
&metricName=container_cpu_used
&dimensions.0.name=clusterId
&dimensions.0.value=cls-xxxxx
&dimensions.1.name=serviceName
&dimensions.1.value=test
&dimensions.2.name=namespace
&dimensions.2.value=default
&dimensions.3.name=podName
&dimensions.3.value=test-3488000495-nj6s9
&dimensions.4.name=containerId
&dimensions.4.value=01c5509d2b39
&startTime=2017-03-28 14:10:00
&endTime=2016-03-28 15:10:00
&period=60
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "container_cpu_used",
	"startTime": "2017-03-28 14:10:00",
	"endTime": "2016-03-28 15:10:00",
	"period": 60,
	"dataPoints": [
		30,
		40,
        ....
	]
}
```


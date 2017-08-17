## 1. API Description

This API (GetMonitorData) is used to acquire monitoring data of cloud products. Obtain corresponding monitoring data based on the namespace of the product, object dimension description and monitoring metrics specified by the user.

Domain: monitor.api.qcloud.com

Note: The new API for acquiring monitoring data (GetMonitorData) can be used to obtain data with a granularity of 1 minute. This API can also be used to acquire monitoring data of more products with a higher granularity in the future. We will no longer update the old version (GetMetricStatistics). It is recommended to use this new API.



## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/405/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is GetMonitorData.


<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> namespace
<td> Yes
<td> String
<td> Namespace. Every cloud product has a namespace. For more information about the namespaces of products, please see Section 5.
<tr>
<td> metricName
<td> Yes
<td> String
<td> Metric name. For more information, please see Section 5
<tr>
<td> dimensions.n.name
<td> Yes
<td> String
<td> Dimension name. This is used in combination with dimensions.n.value. For more information, please see the List of Product Monitoring Metrics in Section 5.
<tr>
<td> dimensions.n.value
<td> Yes
<td> String
<td> Value of the corresponding dimension. This is used in combination with dimensions.n.name. For more information, please see the List of Product Monitoring Metrics in Section 5.
<tr>
<td> period
<td> No
<td> Int
<td> Statistical period for monitoring. Default is 300 (in seconds). Currently, CVM and cloud load balancer support granularity of 60s and 300s. The other products only support 300s. More products will be supported in the future.
<tr>
<td> startTime
<td> No
<td> Datetime
<td> Start time, such as "2016-01-01 10:25:00". The default is "00:00:00" of the current day
<tr>
<td> endTime
<td> No
<td> Datetime
<td> End time. The default is the current time. endTime cannot be earlier than startTime
</tbody></table>



## 3. Output Parameters

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error code. 0: Success. Other values indicate failure
<tr>
<td> message
<td> String
<td> Returned information
<tr>
<td> startTime
<td> Datetime
<td> Start time
<tr>
<td> endTime
<td> Datetime
<td> End Time
<tr>
<td> metricName
<td> String
<td> Metric Name
<tr>
<td> period
<td> Int
<td> Statistical period for monitoring
<tr>
<td> dataPoints
<td> Array
<td> Monitoring data list
</tbody></table>



## 4. Error Codes

| Error Code | Error Description    | Description                                 |
| ---- | ------- | ------------------------------------ |
| -502 | Resource does not exist   | OperationDenied.SourceNotExists      |
| -503 | Invalid request parameter  | InvalidParameter                     |
| -505 | Parameter missing    | InvalidParameter.MissingParameter    |
| -507 | Limit exceeded    | OperationDenied.ExceedLimit          |
| -509 | Invalid dimension combination | InvalidParameter.DimensionGroupError |
| -513 | DB operation failed  | InternalError.DBoperationFail        |



## 5. Example

Input
<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/lb
&metricName=pvv_outtraffic
&dimensions.0.name=protocol
&dimensions.0.value=tcp
&dimensions.1.name=vip
&dimensions.1.value=123.206.201.134
&dimensions.2.name=vport
&dimensions.2.value=80
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "metricName": "pvv_outtraffic",
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

Notes:
1) dimensions.n.name and dimensions.n.value are used to specify a monitoring object. Some objects can only be specified using multiple dimensions.
For example, in 5.5 Cloud Load Balance, you need to specify three dimensions (protocol, vip, vport) to acquire pvv_outtraffic (outbound traffic).
```
dimensions.0.name=protocol
dimensions.0.value=tcp
dimensions.1.name=vip
dimensions.1.value=123.206.201.134
dimensions.2.name=vport
dimensions.2.value=80

```

2) The returned result, dataPoints, is an array. Each element in this array is data of a monitoring point. In the output result below, the three sets of data in dataPoints indicate the statistical data result in two time periods, 14:00-14:05 and 14:05-14:10. The returned data is a closed interval containing three points.
```
{
    "code": 0,
    "message": "",
    "metricName": "pvv_outtraffic",
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



## 6. List of Product Monitoring Metrics

### 6.1 CVM
Tencent Cloud Virtual Machine (CVM) is a server which runs in the Tencent Cloud Data Center. For detailed introductions, please see the <a href="/document/product/213" title="CVM Introduction">CVM Introduction</a> page.
When querying monitoring data of CVMs, the values of input parameters are as follows:
namespace: qce/cvm
dimensions.0.name=unInstanceId
dimensions.0.value is the ID of CVM. This is the unInstanceId field obtained when calling the [DescribeInstances](http://www.qcloud.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8) API.


**Available values of metricName**
#### 6.1.1 Data Monitoring Metrics That Can be Acquired without Installing Monitor Agent

<table class="t">
<tbody><tr>
<th> <b>Metric Name</b>
</th><th> <b>Description</b>
</th><th> <b>Unit</b>
</th><th> <b>Dimension</b>
</th></tr>
<tr>
<td> lan_outtraffic
</td><td> Private network outbound bandwidth
</td><td> Mbps
</td><td>unInstanceId CVM ID
</td></tr>
<tr>
<td> lan_intraffic
</td><td> Private network inbound bandwidth
</td><td> Mbps
</td><td>unInstanceId CVM ID
</td></tr>
<tr>
<td> lan_outpkg
</td><td> Private network outbound packets
</td><td> packets/second
</td><td> unInstanceId CVM ID
</td></tr>
<tr>
<td> lan_inpkg
</td><td> Private network inbound packets
</td><td> packets/second
</td><td> unInstanceId CVM ID
</td></tr>
<tr>
<td> wan_outtraffic
</td><td> Public network outbound bandwidth
</td><td> Mbps
</td><td>unInstanceId CVM ID
</td></tr>
<tr>
<td> wan_intraffic
</td><td> Public network inbound bandwidth
</td><td> Mbps
</td><td> unInstanceId CVM ID
</td></tr>
<tr>
<td> acc_outtraffic
</td><td> Public network outbound traffic
</td><td> MB
</td><td>unInstanceId CVM ID
</td></tr>
<tr>
<td> wan_outpkg
</td><td> Public network outbound packets
</td><td> packets/second
</td><td> unInstanceId CVM ID
</td></tr>
<tr>
<td> wan_inpkg
</td><td> Public network inbound packets
</td><td> packets/second
</td><td> unInstanceId CVM ID
</td></tr>
</td></tr></tbody></table>

#### 6.1.2 Data Monitoring Metrics That Can Only be Acquired after Installing Monitor Agent

<table class="t">
<tbody><tr>
<th> <b>Metric name</b>
</th><th> <b>Description</b>
</th><th> <b>Unit</b>
</th><th> <b>Dimension</b>
</th></tr>
<tr>
<td> cpu_usage
</td><td> CPU utilization
</td><td>%
</td><td> unInstanceId CVM ID
</td></tr>
<tr>
<td> cpu_loadavg
</td><td> Average CPU utilization, obtained by analyzing data in /proc/loadavg and then taking the maximum value of the average CPU load within one minute
(Windows machines do not have this metric)
</td><td>
</td><td> unInstanceId CVM ID
</td></tr>
<tr>
<td> mem_used
</td><td> Used memory
</td><td> MByte
</td><td>unInstanceId CVM ID
</td></tr>
<tr>
<td> mem_usage
</td><td> Memory utilization
</td><td>% 
</td><td> unInstanceId CVM ID
</td></tr>
<tr>
<td> disk_read_traffic
</td><td> Disk read traffic
</td><td> KB/s
</td><td> unInstanceId CVM ID
</td></tr>
<tr>
<td> disk_write_traffic
</td><td> Disk write traffic
</td><td> KB/s
</td><td> unInstanceId CVM ID
</td></tr>
<tr>
<td> disk_io_await
</td><td> Disk IO wait time
</td><td> ms
</td><td> unInstanceId CVM ID
</td></tr></tbody></table>

#### 6.1.3 Example: How to read CVM monitoring metrics

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/cvm
&metricName=cpu_usage
&dimensions.0.name=unInstanceId
&dimensions.0.value=ins-e24d4dzf
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "cpu_usage",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		5.6,
		7.7
	]
}
```



### 6.2 Direct Connect
Direct Connect provides a fast approach to connect Tencent Cloud with local data centers. You can have access to Tencent Cloud computing resources in multiple regions in one go using a single physical direct connection line, to achieve a flexible and reliable hybrid cloud deployment. For detailed introductions, please see the <a href="/doc/product/216/产品概述" title="Product Overview">Direct Connect Introduction</a> page.
When querying monitoring data of direct connect products, the values of input parameters are as follows:

#### 6.2.1 Physical Direct Connect
Physical Direct Connect refers to a physical line used to connect Tencent Cloud with local data centers.
namespace: qce/dc_line
dimensions.0.name=directconnectid
dimensions.0.value is the ID of the direct connection

**Available values of metricName**

<table class="t"><tbody><tr>
<th><b>Metric Name</b></th>
<th><b>Description</b></th>
<th><b>Unit</b></th>
<th><b>Dimension</b></th>
<tr>
<td> intraffic
<td> Inbound traffic
<td> kb
<td> directconnectid Direct connection ID
<tr>
<td> outtraffic
<td> Outbound traffic
<td> kb
<td> directconnectid Direct connection ID
</tbody></table>

**Example: How to read physical direct connection monitoring metrics**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/dc_line
&metricName=inpkg
&dimensions.0.name=directconnectid
&dimensions.0.value=dc-e6p0gw5f
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "inpkg",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		15.6,
		20.3
	]
}
```

#### 6.2.2 Direct Connect Tunnel
Direct Connect Tunnel is the network link segmentation of physical direct connection.
namespace: qce/dc_channel
dimensions.0.name=directconnectconnid
dimensions.0.value is the ID of the direct connect tunnel

**Available values of metricName**

<table class="t"><tbody><tr>
<th><b>Metric name</b></th>
<th><b>Description</b></th>
<th><b>Unit</b></th>
<th><b>Dimension</b></th>
<tr>
<td> delay
<td> Delay
<td> ms
<td> directconnectconnid Direct connect tunnel ID
<tr>
<td> inpkg
<td> Inbound packets
<td> packets/second
<td> directconnectconnid Direct connect tunnel ID
<tr>
<td> intraffic
<td> Inbound traffic
<td> kb
<td> directconnectconnid Direct connect tunnel ID
<tr>
<td> outpkg
<td> Outbound packets
<td> packets/second
<td> directconnectconnid Direct connect tunnel ID
<tr>
<td> outtraffic
<td> Outbound traffic
<td> kb
<td> directconnectconnid Direct connect tunnel ID
<tr>
<td> pkgdrop
<td> Packet loss
<td> %
<td> directconnectconnid Direct connect tunnel ID
</tbody></table>

**Example: How to read direct connect tunnel monitoring metrics**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/dc_channel
&metricName=delay
&dimensions.0.name=directconnectconnid 
&dimensions.0.value=dc-081qsbc7
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "delay",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		5.6,
		7.7
	]
}
```

### 6.3 Cloud Load Balancer

Cloud Load Balancer is a service used to deliver traffic to multiple CVMs. For detailed introductions, please see the <a href="/doc/product/214/概述" title="Overview">Cloud Load Balancer Introduction</a> page.
Here's a list of cloud load balancer metrics (metricName) that can be displayed currently:

| Metric Name       | Description    | Unit   |
| ---------- | ----- | ---- |
| connum     | Current number of connections | connections    |
| new_conn   | Number of newly added connections | connections    |
| intraffic  | Inbound traffic   | Mbps |
| outtraffic | Outbound traffic   | Mbps |
| inpkg      | Inbound packet volume   | packets/s  |
| outpkg     | Outbound packet volume   | packets/s  |

Currently, cloud load balancer supports three types of namespaces: qce/lb_public, qce/lb_private and qce/lb_rs_private. qce/lb_public is the namespace for public network cloud load balancers, it includes the cloud load balancer dimension and the backend machine dimension. qce/lb_private and qce/lb_rs_private are both namespaces for private network cloud load balancers. The difference is that qce/lb_private is for the monitoring data of the cloud load balancer dimension, while qce/lb_rs_private is for the monitoring data of the backend machine dimension. Here are the descriptions of each monitoring dimension:

#### 6.3.1 Public Network Cloud Load Balancer Namespace qce/lb_public
qce/lb_public is a namespace for public network cloud load balancers. You can query all monitoring data of public network cloud load balancers here.
qce/lb_public supports the following four dimension combinations:

1) Public network cloud load balancer dimension

This dimension represents the overall monitoring metric of a public network cloud load balancer. The dimensions that you need to pass (dimensions.n.name) are listed below:

| Dimension   | Dimension Description    | Format                     |
| ---- | ------- | ---------------------- |
| vip  | VIP of cloud load balancer | ip address, such as 111.111.111.11 |

Example of how to call this dimension:
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/lb_public
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
</pre>

2) Public network cloud load balancer port dimension

This dimension represents the monitoring metric of a public network cloud load balancer port. The dimensions that you need to pass (dimensions.n.name) are listed below:

| Dimension              | Dimension Description    | Format                     |
| ---------------- | ------- | ---------------------- |
| vip              | VIP of cloud load balancer | IP address such as 111.111.111.11 |
| loadBalancerPort | Port      | int type, such as 80              |
| protocol         | Protocol      | string type, such as http         |

Example of how to call this dimension:
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/lb_public
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=loadBalancerPort
&dimensions.1.value=80
&dimensions.2.name=protocol
&dimensions.2.value=http
</pre>

3) Public Network Cloud Load Balancer Backend Server Dimension

This dimension represents the monitoring metric for a backend server that is bound to a public network cloud load balancer. The dimensions that you need to pass (dimensions.n.name) are listed below:

| Dimension              | Dimension Description          | Format                     |
| ---------------- | ------------- | ---------------------- |
| vip              | VIP of cloud load balancer       | IP address, such as 111.111.111.11 |
| loadBalancerPort | Port of cloud load balancer        | int type, such as 80              |
| protocol         | Protocol            | string type, such as http         |
| vpcId            | ID of the VPC in which the cloud load balancer resides | int type, such as 1111            |
| lanIp            | IP of the machine to which the cloud load balancer is bound   | IP address, such as 111.111.111.11 |

Example of how to call this dimension:
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/lb_public
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=loadBalancerPort
&dimensions.1.value=80
&dimensions.2.name=protocol
&dimensions.2.value=http
&dimensions.3.name=vpcId
&dimensions.3.value=1111
&dimensions.4.name=lanIp
&dimensions.4.value=111.222.111.22
</pre>

4) Public Network Cloud Load Balancer Backend Server Port Dimension
This dimension represents the monitoring metric for a certain port of a backend server that is bound to a public network cloud load balancer. The dimensions that you need to pass (dimensions.n.name) are listed below:

| Dimension              | Dimension Description          | Format                     |
| ---------------- | ------------- | ---------------------- |
| vip              | VIP of cloud load balancer       | IP address, such as 111.111.111.11 |
| loadBalancerPort | Port of cloud load balancer        | int type, such as 80              |
| protocol         | Protocol            | string type, such as http         |
| vpcId            | ID of the VPC in which the cloud load balancer resides | int type, such as 1111            |
| lanIp            | IP of the machine to which the cloud load balancer is bound   | IP address, such as 111.111.111.11 |
| port             | Port number of the machine to which the cloud load balancer is bound   | int type, such as 80              |

Example of how to call this dimension:
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/lb_public
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=loadBalancerPort
&dimensions.1.value=80
&dimensions.2.name=protocol
&dimensions.2.value=http
&dimensions.3.name=vpcId
&dimensions.3.value=1111
&dimensions.4.name=lanIp
&dimensions.4.value=111.222.111.22
&dimensions.5.name=port
&dimensions.5.value=80
</pre>

#### 6.3.2 Private Network Cloud Load Balancer Dimension Namespace qce/lb_private
qce/lb_private is a namespace for the private network cloud load balancer dimension. You can query relevant monitoring data of the private network cloud load balancer dimension here.
qce/lb_private supports the following two dimension combinations:

1) Private network cloud load balancer dimension

This dimension represents the overall monitoring metric of a private network cloud load balancer. The dimensions that you need to pass (dimensions.n.name) are listed below. There may be duplicate private network vips, thus you also need to pass the vpcId to specify an individual lb:

| Dimension    | Dimension Description          | Format                     |
| ----- | ------------- | ---------------------- |
| vip   | VIP of cloud load balancer       | IP address, such as 111.111.111.11 |
| vpcId | ID of the VPC in which the cloud load balancer resides | int type, such as 1111            |

Example of how to call this dimension:
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/lb_private
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=vpcId
&dimensions.1.value=1111
</pre>

2) Private network cloud load balancer port dimension

This dimension represents the monitoring metric of a private network cloud load balancer port. The dimensions that you need to pass (dimensions.n.name) are listed below:

| Dimension              | Dimension Description          | Format                     |
| ---------------- | ------------- | ---------------------- |
| vip              | VIP of cloud load balancer       | IP address, such as 111.111.111.11 |
| vpcId            | ID of the VPC in which the cloud load balancer resides | int type, such as 1111            |
| loadBalancerPort | Port of cloud load balancer        | int type, such as 80              |
| protocol         | Protocol            | string type, such as http         |

Example of how to call this dimension:
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/lb_private
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=vpcId
&dimensions.1.value=1111
&dimensions.2.name=loadBalancerPort
&dimensions.2.value=80
&dimensions.3.name=protocol
&dimensions.3.value=http
</pre>

#### 6.3.3 Private Network Cloud Load Balancer Backend Server Dimension Namespace qce/lb_rs_private
qce/lb_private is a namespace for the private network cloud load balancer dimension. You can query relevant monitoring data of the private network cloud load balancer dimension here.
qce/lb_private supports the following two dimension combinations:

1) Private network cloud load balancer backend machine dimension

This dimension represents the monitoring metric of the backend machine that is bound to a private network cloud load balancer. The dimensions that you need to pass (dimensions.n.name) are listed below. There may be duplicate private network vips, thus you also need to pass the vpcId to specify an individual lb:

| Dimension              | Dimension Description          | Format                     |
| ---------------- | ------------- | ---------------------- |
| vip              | VIP of cloud load balancer       | IP address, such as 111.111.111.11 |
| vpcId            | ID of the VPC in which the cloud load balancer resides | int type, such as 1111            |
| loadBalancerPort | Port of cloud load balancer        | int type, such as 80              |
| protocol         | Protocol            | string type, such as http         |
| lanIp            | IP of the machine to which the cloud load balancer is bound    | IP address, such as 111.111.111.11 |

Example of how to call this dimension:
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/lb_rs_private
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=vpcId
&dimensions.1.value=1111
&dimensions.2.name=loadBalancerPort
&dimensions.2.value=80
&dimensions.3.name=protocol
&dimensions.3.value=http
&dimensions.4.name=lanIp
&dimensions.4.value=111.222.111.22
</pre>

2) Private network cloud load balancer backend machine port dimension

This dimension represents the monitoring metric for a certain port of a backend machine that is bound to a private network cloud load balancer. The dimensions that you need to pass (dimensions.n.name) are listed below:

| Dimension              | Dimension Description          | Format                     |
| ---------------- | ------------- | ---------------------- |
| vip              | VIP of cloud load balancer       | IP address, such as 111.111.111.11 |
| vpcId            | ID of the VPC in which the cloud load balancer resides | int type, such as 1111            |
| loadBalancerPort | Port of cloud load balancer        | int type, such as 80              |
| protocol         | Protocol            | string type, such as http         |
| lanIp            | IP of the machine to which the cloud load balancer is bound    | IP address, such as 111.111.111.11 |
| port             | Port number of the machine to which the cloud load balancer is bound  | int type, such as 80              |

Example of how to call this dimension:
<pre>
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/lb_rs_private
&metricName=connum
&dimensions.0.name=vip
&dimensions.0.value=111.111.111.11
&dimensions.1.name=vpcId
&dimensions.1.value=1111
&dimensions.2.name=loadBalancerPort
&dimensions.2.value=80
&dimensions.3.name=protocol
&dimensions.3.value=http
&dimensions.4.name=lanIp
&dimensions.4.value=111.222.111.22
&dimensions.5.name=port
&dimensions.5.value=80
</pre>


### 6.4 Content Delivery Network
The CDN (Content Delivery Network) works by creating a new network layer in the existing Internet and delivering contents of websites to the network that is closest to users. For detailed introductions, please see the <a href="/doc/product/228/产品概述" title="Product Overview">CDN Introduction</a> page.
When querying monitoring data of CDN products, the values of input parameters are as follows:
namespace: qce/cdn
Available values for dimension name are: projectid, domain
dimensions.0.name=projectid&dimensions.1.name=domain
dimensions.0.value is project ID, dimensions.1.value is domain

**Available values of metricName**

| Metric Name      | Description   | Unit   | Dimension               |
| --------- | ---- | ---- | ---------------- |
| bandwidth | Bandwidth   | bps  | projectid, domain |
| requests  | Number of requests  | Request number    | projectid, domain |

**Example: How to read CDN monitoring metrics**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/cdn
&metricName=requests
&dimensions.0.name=projectid
&dimensions.0.value=1
&dimensions.0.name=domain
&dimensions.0.value=www.test.com
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "requests",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		5,
		7
	]
}
```

### 6.5 Cloud Database MySQL

Cloud Database for MySQL is a high-performance distributed data storage service created by Tencent Cloud in a professional manner based on the world's most popular open source database MySQL. For detailed introductions, please see the <a href="/doc/product/236/简介" title="Overview">Cloud Database for MySQL</a> page.
When querying monitoring data of Cloud Database for MySQL products, the values of input parameters are as follows:
namespace: qce/cdb
Value for dimension name: uInstanceId
dimensions.0.name=uInstanceId
dimensions.0.value is the ID of cdb instance

**Available values of metricName**

| Metric Name                  | Description             | Unit     | Dimension          |
| --------------------- | -------------- | ------ | ----------- |
| slow_queries          | Number of slow queries           | queries/second    | uInstanceId |
| max_connections       | Max number of connections          | connections      | uInstanceId |
| select_scan           | Number of full table scans          | scans/second    | uInstanceId |
| select_count          | Number of queries            | queries/second    | uInstanceId |
| com_update            | Number of updates            | updates/second    | uInstanceId |
| com_delete            | Number of deletes            | deletes/second    | uInstanceId |
| com_insert            | Number of inserts            | inserts/second    | uInstanceId |
| com_replace           | Number of overwrites            | overwrites/second    | uInstanceId |
| queries               | Total number of requests           | requests/second    | uInstanceId |
| threads_connected     | Number of currently opened connections        | connections      | uInstanceId |
| real_capacity         | Disk space (excluding the space occupied by binlog)         | MB     | uInstanceId |
| capacity              | Disk space (including the space occupied by binlog)         | MB     | uInstanceId |
| bytes_sent            | Private network outbound traffic          | Byte/second | uInstanceId |
| bytes_received        | Private network inbound traffic          | Byte/second | uInstanceId |
| qcache_use_rate       | Cache utilization rate          | %      | uInstanceId |
| qcache_hit_rate       | Cache hit rate          | %      | uInstanceId |
| table_locks_waited    | Number of times to wait for table lock         | locks/second    | uInstanceId |
| created_tmp_tables    | Number of temporary tables          | tables/second    | uInstanceId |
| innodb_cache_use_rate | innodb cache use rate    | %      | uInstanceId |
| innodb_cache_hit_rate | innodb cache hit rate    | %      | uInstanceId |
| innodb_os_file_reads  | Number of times innodb reads from disk    | times/second    | uInstanceId |
| innodb_os_file_writes | Number of times innodb writes to disk    | times/second    | uInstanceId |
| innodb_os_fsyncs      | Number of innodb fsync operations | times/second    | uInstanceId |
| key_cache_use_rate    | myisam cache utilization rate    | %      | uInstanceId |
| key_cache_hit_rate    | myisam cache hit rate    | %      | uInstanceId |
| volume_rate           | Capacity utilization rate          | %      | uInstanceId |
| query_rate            | Query utilization rate          | %      | uInstanceId |
| qps                   | Queries per second        | times/second    | uInstanceId |
| tps                   | Transactions per second        | times/second    | uInstanceId |
| cpu_use_rate          | CPU utilization rate   | %    | uInstanceId |
| memory_use            | Memory used      | MB    | uInstanceId |

**Example: How to read Cloud Database for MySQL monitoring metrics**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/cdb
&metricName=slow_queries
&dimensions.0.name=uInstanceId
&dimensions.0.value=cdb-e242adzf
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "slow_queries",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		55,
		46,
		33
	]
}
```

### 6.6 Cloud Database TDSQL

Tencent Cloud Database TDSQL is a highly secure enterprise-level cloud database under the OLTP scenario and has been serving for Tencent's billing services for more than 10 years. TDSQL is compatible with MySQL syntaxes, with advanced features such as thread pool, auditing, cross-region disaster recovery. This cloud database service is simple to expand, easy to use and cost-efficient. For detailed introductions, please see the <a href="/doc/product/237/产品概述" title="Product Overview">Cloud Database TDSQL Introduction</a> page.
When querying monitoring data of Cloud Database TDSQL products, the values of input parameters are as follows:

namespace: qce/tdsql
Value for dimension name: uuid 
dimensions.0.name=uuid 
dimensions.0.value is the instance uuid


**Available values of metricName**

| Metric Name                  | Description           | Unit   | Dimension    |
| --------------------- | ------------ | ---- | ---- |
| data_disk_available   | Available data disk space     | GB   | uuid |
| binlog_disk_available | Available BINLOG disk space | GB   | uuid |
| select_total          | Total number of SELECT requests   | times/second  | uuid |
| long_query            | Total number of SELECT slow queries   | times/second  | uuid |
| update_total          | Total number of UPDATE requests   | times/second  | uuid |
| insert_total          | Total number of INSERT requests   | times/second  | uuid |
| delete_total          | Total number of DELETE requests   | times/second  | uuid |
| mem_available         | Available memory       | GB   | uuid |
| disk_iops             | Disk IOPS       | times/second  | uuid |
| conn_active           | Number of active connections        | connections/second  | uuid |
| conn_running          | Number of connections          | connections/second  | uuid |
| is_mater_switched     | Monitor whether master/slave switching is commenced     | none    | uuid |
| cpu_usage_rate        | CPU utilization rate       | %    | uuid |

**Example: How to read Cloud Database TDSQL monitoring metrics**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/tdsql
&metricName=data_disk_available
&dimensions.0.name=uuid
&dimensions.0.value=tdsql-0gfryg60
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "data_disk_available",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		28.3,
		28.3
	]
}
```

### 6.7 Cloud Database SQL Server

Cloud Database SQL Server is a cloud database service developed by Tencent Cloud in a professional manner, based on the SQL Server published by Microsoft. For detailed introductions, please see the <a href="/doc/product/238/产品概述" title="Product Overview">Cloud Database SQL Server</a> page.
When querying monitoring data of Cloud Database SQL Server products, the values of input parameters are as follows:

namespace: qce/sqlserver
Value for dimension name: resourceId 
dimensions.0.name=resourceId 
dimensions.0.value is the resource ID of the instance

**Available values of metricName**

| Metric Name                   | Description                    | Unit   | Dimension         |
| ---------------------- | --------------------- | ---- | ---------- |
| cpu                    | Instance CPU utilization rate           | %    | resourceId |
| transactions           | Average number of transactions per second              | times/second  | resourceId |
| connections            | Average number of user connections to the database per second        | connections    | resourceId |
| requests               | Number of requests per second                | times/second  | resourceId |
| logins                 | Number of logins per second                | times/second  | resourceId |
| logouts                | Number of logouts per second                | times/second  | resourceId |
| storage                | Total storage occupied by instance data files and log files   | GB   | resourceId |
| in_flow                | Total size of inbound packets of all connections           | MB/s | resourceId |
| out_flow               | Total size of outbound packets of all connections           | MB/s | resourceId |
| iops                   | Number of disk I/O operations                | times/second  | resourceId |
| disk_reads             | Number of disk read operations per second              | times/second  | resourceId |
| disk_writes            | Number of disk write operations per second              | times/second  | resourceId |
| slow_queries           | Number of queries with operation time longer than 1 second         | queries    | resourceId |
| blocks_processes       | Number of currently blocked processes                | processes    | resourceId |
| lock_requests          | Average number of lock requests per second            | times/second  | resourceId |
| user_errors            | Average number of errors per second               | errors/second  | resourceId |
| sql_compilations       | Average number of SQL compilations per second           | times/second  | resourceId |
| sql_recompilations     | Average number of SQL recompilations per second          | times/second  | resourceId |
| full_scans             | Number of full scans (scans without restrictions) per second          | times/second  | resourceId |
| buffer_cache_hit_ratio | Data cache (memory) hit rate           | %    | resourceId |
| latch_waits            | Number of waiting latches per second              | times/second  | resourceId |
| lock_waits             | Average waiting time of lock requests that caused a waiting process     | ms   | resourceId |
| network_io_waits       | Average network I/O latency            | ms   | resourceId |
| plan_cache_hit_ratio   | Execution plan hit rate (each SQL has an execution plan) | %    | resourceId |

**Example: How to read Cloud Database SQL Server monitoring metrics**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/sqlserver
&metricName=cpu
&dimensions.0.name=resourceId
&dimensions.0.value=mssql-dh01nvsb
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "cpu",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		50,
		44
	]
}
```

### 6.8 Cloud Redis Store

Cloud Redis Store (CRS) is a highly available, highly reliable Redis service platform based on Tencent Cloud's years of technical experience in distributed cache and demand for Redis-related business operations. For detailed introductions, please see the <a href="/doc/product/239/产品介绍" title="Product Introduction">Cloud Redis Introduction</a> page.
When querying monitoring data of Cloud Redis products, the values of input parameters are as follows:

namespace: qce/redis
Value for dimension name: redis_uuid
dimensions.0.name=redis_uuid
dimensions.0.value is the instance uuid

**Available values of metricName**

| Metric Name             | Description          | Unit   | Dimension         |
| ---------------- | ----------- | ---- | ---------- |
| cache_hit_ratio  | cache hit rate    | %    | redis_uuid |
| cmdstat_get      | Number of get commands      | times/minute | redis_uuid |
| cmdstat_getbit   | Number of getbit commands   | times/minute | redis_uuid |
| cmdstat_getrange | Number of getrange commands | times/minute | redis_uuid |
| cmdstat_hget     | Number of hget commands     | times/minute | redis_uuid |
| cmdstat_hgetall  | Number of hgetall commands  | times/minute | redis_uuid |
| cmdstat_hmget    | Number of hmget commands    | times/minute | redis_uuid |
| cmdstat_hmset    | Number of hmset commands    | times/minute | redis_uuid |
| cmdstat_hset     | Number of hset commands     | times/minute | redis_uuid |
| cmdstat_hsetnx   | Number of hsetnx commands   | times/minute | redis_uuid |
| cmdstat_lset     | Number of lset commands     | times/minute | redis_uuid |
| cmdstat_mget     | Number of mget commands     | times/minute | redis_uuid |
| cmdstat_mset     | Number of mset commands     | times/minute | redis_uuid |
| cmdstat_msetnx   | Number of msetnx commands   | times/minute | redis_uuid |
| cmdstat_set      | Number of set commands      | times/minute | redis_uuid |
| cmdstat_setbit   | Number of setbit commands   | times/minute | redis_uuid |
| cmdstat_setex    | Number of setex commands    | times/minute | redis_uuid |
| cmdstat_setnx    | Number of setnx commands    | times/minute | redis_uuid |
| cmdstat_setrange | Number of setrange commands | times/minute | redis_uuid |
| connections      | Number of external connections       | connections    | redis_uuid |
| cpu_us           | Number of processed requests       | μs   | redis_uuid |
| in_flow          | External request packet length     | Mb   | redis_uuid |
| keys             | Number of primary keys        | keys    | redis_uuid |
| out_flow         | External return packet length     | Mb   | redis_uuid |
| stat_get         | Total number of get commands    | times/minute | redis_uuid |
| stat_set         | Total number of set commands    | times/minute | redis_uuid |
| storage          | Occupied storage        | Mb   | redis_uuid |
| storage_us       | Occupied storage percentage      | %    | redis_uuid |

**Example: How to read Cloud Redis monitoring metrics**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/redis
&metricName=cache_hit_ratio
&dimensions.0.name=redis_uuid
&dimensions.0.value=00953d35-f6b7-4c2d-b86e-613b81f4cfcc
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "cache_hit_ratio",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		50,
		30
	]
}
```


### 6.9 Cloud Database MongoDB

When querying monitoring data of Document Database MongoDB products, the values of input parameters are as follows:
namespace: qce/cmongo
Fixed value for dimension name: target
dimensions.0.name=target
dimensions.0.value depends on the dimension to be queried

The available values for dimensions.0.value will be described below.
MongoDB provided by Tencent Cloud is a clustered service. This API can be used to query monitoring data of three dimensions: the entire cluster, a certain replica set, or a certain node.
In this case:
"The entire cluster" refers to the MongoDB instance you have purchased. In this dimension, you can query information about the entire instance such as the number of read/write requests, capacity utilization, timed out requests and so on.
In the dimension of "a certain replica set", you can query the capacity utilization and master-slave latency information inside a certain replica set under the cluster. The replica set instance itself contains only one replica set, while every shard of a sharded instance is a replica set.
In the dimension of "a certain node", you can query the information of any node inside the cluster, such as the CPU and memory of the node.

For the values of dimensions.0.value, see the table below

| Value Type  | Value Example                                     | Description                                       |
| ----- | ---------------------------------------- | ---------------------------------------- |
| Instance ID  | cmgo-6ielucen                            | The instance ID is the unique identifier of a MongoDB instance;<br/>You can query this ID from the <a href="https://console.qcloud.com/mongodb">MongoDB Console</a>;<br/>You can also acquire this ID by calling MongoDB APIs |
| Replica set ID | cmgo-6ielucen_0<br/>cmgo-6ielucen_2      | Acquire replica set ID by adding the "_index number" suffix behind the instance ID;<br/>The "index number" starts from 0, up to a maximum of [number of replica sets - 1];<br/>A replica set instance contains only one replica set, thus the suffix is always "_0";<br/>Sharded instance contains multiple shards, each shard is a replica set. For example: add "_2" as suffix for the replica set ID of the third shard |
| Node ID  | cmgo-6ielucen_0-node-primary<br/>cmgo-6ielucen_1-node-slave0<br/>cmgo-6ielucen_3-node-slave2 | Add "-node-primary" suffix behind a replica set ID to acquire its primary node ID;<br/>Add "-node-slave[slave node index number]" to acquire the corresponding slave node ID, <br/>The "slave node index number" starts from 0, up to a maximum of [number of slave nodes - 1] |

Available values of metricName

| Metric                | Description                        | Unit   | Cluster/Instance | dimensions.0.value |
| ----------------- | ------------------------- | ---- | ----- | -------------------- |
| inserts           | Number of write operations per unit time                 | times    | Cluster/Instance | Instance ID                 |
| reads             | Number of read operations per unit time                 | times    | Cluster/Instance | Instance ID                 |
| updates           | Number of update operations per unit time                 | times    | Cluster/Instance | Instance ID                 |
| deletes           | Number of delete operations per unit time                 | times    | Cluster/Instance | Instance ID                 |
| counts            | Number of count operations per unit time               | times    | Cluster/Instance | Instance ID                 |
| aggregates        | Number of aggregates operations per unit time         | times    | Cluster/Instance | Instance ID                 |
| cluster_diskusage | Cluster capacity utilization                   | %    | Cluster/Instance | Instance ID                 |
| success           | Number of successful requests per unit time               | times    | Cluster/Instance | Instance ID                 |
| delay_10          | Number of successful requests with a latency of 10 ms-50 ms, per unit time   | times    | Cluster/Instance | Instance ID                 |
| delay_50          | Number of successful requests with a latency of 50 ms-100 ms, per unit time | times    | Cluster/Instance | Instance ID                 |
| delay_100         | Number of successful requests with a latency of more than 100 ms, per unit time     | times    | Cluster/Instance | Instance ID                 |
| timeouts          | Number of successful requests with a latency of 10 ms-53 ms, per unit time   | times    | Cluster/Instance | Instance ID                 |
| replica_diskusage | Replica set capacity utilization                  | %    | Replica set   | Replica set ID                |
| slavedelay        | Average master-slave latency, per unit time               | second    | Replica set   | Replica set ID                |
| cpuusage          | CPU utilization                    | %    | Node    | Node ID                 |
| memusage          | Memory utilization                     | %    | Node    | Node ID                 |
| qr                | Number of read requests waiting in the queue            | requests    | Node    | Node ID                 |
| qw                | Number of write requests waiting in the queue           | requests    | Node    | Node ID                 |
| conn              | Number of connections                       | connections    | Node    | Node ID                 |
| netin             | Network inbound traffic                     | MB/s | Node    | Node ID                 |
| netout            | Network outbound traffic                     | MB/s | Node    | Node ID                 |

Example: How to read Document Database MongoDB monitoring metrics

To query the number of requests with a latency of more than 100 ms for a certain cluster/instance, enter:

```
https://monitor.api.qcloud.com/v2/index.php?
&<common request parameters>
&namespace=qce/cmongo
&metricName=delay_100
&dimensions.0.name=target
&dimensions.0.value=cmgo-6ielucen
&startTime=2017-01-09 20:22:00
&endTime=2017-01-09 20:38:00
```

To query the number of requests with a latency of more than 100 ms for a certain cluster/instance, enter:

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

To query the master/slave latency of a certain replica set, enter:

```
https://monitor.api.qcloud.com/v2/index.php?
&<common request parameters>
&namespace=qce/cmongo
&metricName=slavedelay
&dimensions.0.name=target
&dimensions.0.value=cmgo-6ielucen_0
&startTime=2017-01-09 20:22:00
&endTime=2017-01-09 20:38:00
```

When querying the master/slave latency of a certain replica set, the output is:

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

To query the number of connections of a certain node, enter:

```
https://monitor.api.qcloud.com/v2/index.php?
&<common request parameters>
&namespace=qce/cmongo
&metricName=slavedelay
&dimensions.0.name=target
&dimensions.0.value=cmgo-6ielucen_0
&startTime=2017-01-09 20:22:00
&endTime=2017-01-09 20:38:00
```

When querying the number of connections of a certain node, the output is:

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

### 6.10 Cloud Physical Machine Load Balancers

Cloud Physical Machines provide load balancing features.
Parameters for querying Cloud Physical Machine Load Balancer product monitoring data
namespace: qce/bm_lb
Dimension description:

| Name       | Meaning    |
| -------- | ------- |
| protocol | Protocol      |
| vip      | Cloud load balancer VIP |
| vport    | Cloud load balancer port  |
| rsip     | Backend server IP |
| rsport   | Backend server port |
| vpcid    | VPC ID  |

dimensions.0.name=protocol
dimensions.0.value is the protocol value (tcp or udp)
dimensions.1.name=vip
dimensions.1.value is the cloud load balancer VIP
dimensions.2.name=vport
dimensions.2.value is the cloud load balancer port
dimensions.3.name=rsip
dimensions.3.value is the backend server IP
dimensions.4.name=rsport
dimensions.4.value is the backend server port
dimensions.5.name=vpcid
dimensions.5.value is the VPC ID

**Available values of metricName**

| Metric Name       | Description    | Unit   | Dimension                                   |
| ---------- | ----- | ---- | ------------------------------------ |
| inpkg      | Inbound packet volume   | packets/second  | protocol,vip,vport,rsip,rsport,vpcid |
| outpkg     | Outbound packet volume   | packets/second  | protocol,vip,vport,rsip,rsport,vpcid |
| intraffic  | Inbound bandwidth   | bps  | protocol,vip,vport,rsip,rsport,vpcid |
| outtraffic | Outbound bandwidth   | bps  | protocol,vip,vport,rsip,rsport,vpcid |
| connum     | Current number of connections | connections    | protocol,vip,vport,rsip,rsport,vpcid |

**Example: How to read Cloud Physical Machine Load Balancer monitoring metrics**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/bm_lb
&metricName=inpkg
&dimensions.0.name=protocol
&dimensions.0.value=tcp
&dimensions.1.name=vip
&dimensions.1.value=1.2.3.4
&dimensions.2.name=vport
&dimensions.2.value=80
&dimensions.3.name=rsip
&dimensions.3.value=11.22.33.44
&dimensions.4.name=rsport
&dimensions.4.value=8080
&dimensions.5.name=vpcid
&dimensions.5.value=1
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "inpkg",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		30,
		40
	]
}
```

### 6.11 Cloud Message Queue (CMQ)

Tencent Cloud Message Queue (CMQ) is a distributed message queue service used to provide a reliable, message-based asynchronous communication mechanism for different applications that are deployed distributively, or different components of one application. Messages are stored in a highly reliable, highly available Cloud Message Queue, while multiple processes are able to perform read/write operations at the same time, without affecting each other.
There are two CMQ models, queue and topic. The methods for monitoring them are as follows

#### 6.11.1 Querying Monitoring Data of CMQ Queue

When querying monitoring data of message service CMQ products, the values of input parameters are as follows:

namespace: qce/cmq

Value for dimension name: queueId, queueName

dimensions.0.name=queueId
dimensions.0.value is the CMQ queue instance ID

dimensions.1.name=queueName
dimensions.1.value is the CMQ queue instance name

**Available values of metricName**

| Metric Name                 | Description         | Unit   | Dimension                |
| -------------------- | ---------- | ---- | ----------------- |
| invisibleMsgNum      | Number of invisible messages in the queue  | messages    | queueId,queueName |
| visibleMsgNum        | Number of visible messages in the queue   | messages    | queueId,queueName |
| sendMsgReqCount      | Number of requests to send messages    | times    | queueId,queueName |
| sendMsgNum           | Number of sent messages    | messages    | queueId,queueName |
| recvMsgReqCount      | Number of requests to receive messages     | times    | queueId,queueName |
| recvMsgNum           | Number of received messages    | messages    | queueId,queueName |
| recvNullMsgNum       | Number of received blank messages   | messages    | queueId,queueName |
| batchRecvNullMsgNum  | Number of batch received blank messages | messages    | queueId,queueName |
| delMsgReqCount       | Number of requests to delete messages   | times    | queueId,queueName |
| delMsgNum            | Number of deleted messages    | messages    | queueId,queueName |
| sendMsgSize          | Size of sent message    | MB   | queueId,queueName |
| batchSendMsgSize     | Size of batch sent messages  | MB   | queueId,queueName |
| batchSendMsgReqCount | Number of requests to batch send messages | times    | queueId,queueName |
| batchRecvMsgReqCount | Number of requests to batch receive messages | times    | queueId,queueName |
| batchDelMsgReqCount  | Number of requests to batch delete messages | times    | queueId,queueName |

**Example: How to read CMQ monitoring metrics**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common Request Parameters</a>>
&namespace=qce/cmq
&metricName=invisibleMsgNum
&dimensions.0.name=queueId
&dimensions.0.value=queue-06c1jrku
&dimensions.1.name=queueName
&dimensions.1.value=qta-cbeba170-a6d9-11e6-8372-9000e086cbc0
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "invisibleMsgNum",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		50,
		20
	]
}
```

#### 6.11.2 Querying Monitoring Data of CMQ Topic

When querying monitoring data of message service CMQ Topic products, the values of input parameters are as follows:

namespace: qce/cmqtopic
Value for dimension name: topicId, subscriptionId

dimensions.0.name=topicId
dimensions.0.value is the CMQ topic instance ID

dimensions.1.name=subscriptionId
dimensions.1.value is the CMQ subscription instance ID

**Available values of metricName**

| Metric Name                     | Description          | Unit   | Dimension                     |
| ------------------------ | ----------- | ---- | ---------------------- |
| NumOfMsgPublished        | Number of published messages    | messages    | topicId                |
| NumOfMsgBatchPublished   | Number of batch published messages  | messages    | topicId                |
| CountOfMsgPublished      | Number of requests for published messages   | times    | topicId                |
| CountOfMsgBatchPublished | Number of requests for batch published messages | messages    | topicId                |
| PublishSize              | Size of published messages    | MB   | topicId                |
| BatchPublishSize         | Size of batch published messages  | MB   | topicId                |
| NumOfNotify              | Total number of delivered messages    | messages    | topicId,subscriptionId |
| NumOfSuccNotify          | Number of successfully delivered messages   | messages    | topicId,subscriptionId |

**Example: How to read CMQ monitoring metrics**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&namespace=qce/cmqtopic
&metricName=NumOfMsgPublished
&dimensions.0.name=topicId
&dimensions.0.value=topic-06c1jrku
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "NumOfMsgPublished",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		50,
		20
	]
}
```

### 6.12 VPC
Tencent Cloud Virtual Private Cloud (VPC) is a customized network space on Tencent Cloud that is logically isolated, which is similar to the traditional network you run in the data center. The service resources hosted in Tencent Cloud VPC include Cloud Virtual Machine, Cloud Load Balance, Cloud Database and other resources of Cloud Services in your Tencent Cloud. You can fully control your VPC environment, including customizing network segmentation, IP address and routing policy, and achieve multi-layer security protections through network ACL and security group and so on. At the same time, you can also use IPsec VPN/Direct Connect to connect the VPC with your data center, to deploy hybrid cloud in a flexible manner. For detailed introductions, please see the <a href="https://www.qcloud.com/document/product/215/535" title="Product Overview">VPC Product Overview</a> page.
When querying monitoring data of VPC products, the values of input parameters are as follows:

#### 6.12.1 Peering Connection
VPC peering connection is a service used to connect two VPCs, which allows VPC IPs to route traffic between the peer VPCs as if they belong to the same network.

When querying monitoring data of peering connection products, the values of input parameters are as follows:

Value for dimension name: vpcId, peeringConnectionId

namespace: qce/vpc_region_conn

dimensions.0.name=peeringConnectionId
dimensions.0.value is the peering connection ID

dimensions.1.name=vpcId
dimensions.1.value is the local vpcId

**Available values of metricName**

| Metric Name       | Description   | Unit   | Dimension                        |
| ---------- | ---- | ---- | ------------------------- |
| inpkg      | Inbound packet volume  | packets/second  | vpcId,peeringConnectionId |
| intraffic  | Inbound bandwidth  | Mbps | vpcId,peeringConnectionId |
| outpkg     | Outbound packet volume  | packets/second  | vpcId,peeringConnectionId |
| outtraffic | Outbound bandwidth  | Mbps | vpcId,peeringConnectionId |
| pkgdrop    | Packet loss rate  | %    | vpcId,peeringConnectionId |

**Example: How to read peering connection monitoring metrics**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&namespace=qce/vpc_region_conn
&metricName=inpkg
&dimensions.0.name=peeringConnectionId
&dimensions.0.value=pcx-086ypwc8
&dimensions.1.name=vpcId
&dimensions.1.value=vpc-086ypwc8
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "inpkg",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		30,
		40
	]
}
```

#### 6.12.2 Basic Network Cross-region Interconnection
VPC basic network cross-region interconnection means the capability for basic network CVMs in different regions to communicate with each other as if they belong to the same network.

When querying the monitoring data of basic network cross-region interconnection product, the values for input parameters are as follows:

Value for dimension name: peeringConnectionId

namespace: qce/pcx

dimensions.0.name=peeringConnectionId
dimensions.0.value is the ID for basic network cross-region interconnection

**Available values of metricName**

| Metric Name       | Description   | Unit   | Dimension                        |
| ---------- | ---- | ---- | ------------------------- |
| inpkg      | Inbound packets  | packets/second  | peeringConnectionId |
| inbandwidth  | Inbound bandwidth  | Mbps | peeringConnectionId |
| outpkg     | Outbound packets  | packets/second  | peeringConnectionId |
| outbandwidth | Outbound bandwidth  | Mbps | peeringConnectionId |
| pkgdrop    | Packet loss rate  | %    | peeringConnectionId |

**Example: How to read peering connection monitoring metrics**

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&namespace=qce/pcx
&metricName=inpkg
&dimensions.0.name=peeringConnectionId
&dimensions.0.value=pcx-086ypwc8
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "inpkg",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		30,
		40
	]
}
```

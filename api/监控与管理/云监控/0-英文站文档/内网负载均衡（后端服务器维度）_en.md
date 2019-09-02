## 1. API Description

Domain name: monitor.api.qcloud.com


Cloud Load Balancer (CLB) is a service used to distribute traffic to multiple CVMs. For more information, please see <a href="/doc/product/214/概述" title="Overview">Cloud Load Balancer</a> page.
CLB supports three namespaces: qce/lb_public, qce/lb_private and qce/lb_rs_private.

qce/lb_public: Namespace of the public network load balancer. It includes monitoring data from load balancer dimension and backend machine dimension.
qce/lb_private: Namespace of the private network load balancer. It includes monitoring data from load balancer dimension.
qce/lb_rs_private: Namespace of the private network load balancer. It includes monitoring data from backend CVM dimension.

qce/lb_rs_private is a namespace in private network load balancer backend CVM dimension, and can be used to query monitoring data in the private network load balancer backend CVM dimension.

qce/lb_rs_private is used to query monitoring data based on 2 dimension groups below. The values for input parameters are as follows:

### 1.1 Values of Input Parameters for the Private Network Load Balancer Backend CVM Dimension

Because the private network vip may be repeated, vpcId is also required to uniquely specify a lb:

namespace: qce/lb_rs_private
dimensions.0.name=vip
dimensions.0.value is the IP address.
&dimensions.1.name=vpcId
&dimensions.1.value is ID of the VPC, in which the load balancer resides
&dimensions.2.name=loadBalancerPort
&dimensions.2.value is the port number
&dimensions.3.name=protocol
&dimensions.3.value is the protocol type
&dimensions.4.name=lanIp
&dimensions.4.value is IP of the machine bound to the load balancer


### 1.2 Values of Input Parameters for the Private Network Load Balancer Backend CVM Port Dimension

Because the private network vip may be repeated, vpcId is also required to uniquely specify a lb:

namespace: qce/lb_rs_private
dimensions.0.name=vip
dimensions.0.value is the IP address.
&dimensions.1.name=vpcId
&dimensions.1.value is ID of the VPC, in which the load balancer resides
&dimensions.2.name=loadBalancerPort
&dimensions.2.value is the port number
&dimensions.3.name=protocol
&dimensions.3.value is the protocol type
&dimensions.4.name=lanIp
&dimensions.4.value is IP of the machine bound to the load balancer
&dimensions.5.name=port
&dimensions.5.value is the port number of the machine bound to the load balancer

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see <a href="/doc/api/405/公共请求参数" title="Common Request Parameters">Common Request Parameters</a> page. The Action field for this API is GetMonitorData.

### 2.1 Input Parameters

#### 2.1.1 Input Parameter Overview

| Parameter Name               | Required   | Type       | Input Content    | Description                                       |
| ------------------ | ---- | -------- | ------- | ---------------------------------------- |
| namespace          | Yes    | String   | qce/cvm  | Namespace. Every Tencent Cloud product has a namespace. For more information, please see Input Content column.           |
| metricName         | Yes    | String   | Specific metric name | Metric name. For more information, please see 2.2                            |
| dimensions.n.name  | Yes    | String   | Dimension name   | Dimension name, which is used in combination with dimensions.n.value. For more information, please see section 2.1.2. |
| dimensions.n.value | Yes    | String   | Dimension value   | Dimension value, which is used in combination with dimensions.n.name. For more information, please see section 2.1.2. |
| period             | No    | Int      | 60/300  | Interval for collecting monitoring data. Most metrics support a statistical granularity of 60s while some metrics only support a statistical granularity of 300s. Statistical granularity varies with metrics. Enter parameters by referring to the list of metric details in section 2.2. |
| startTime          | No    | Datetime | Start time    | Start time, such as "2016-01-01 10:25:00". Default is "00:00:00" of the current day |
| endTime            | No    | Datetime | End time    | End time. It is the current time by default. endTime cannot be earlier than startTime       |
#### 2.1.2 Overview of Parameters at Each Dimension

| Parameter Name               | Dimension Name             | Dimension Description          | Format                            |
| ------------------ | ---------------- | ------------- | ----------------------------- |
| dimensions.0.name  | vip              | Load balancer VIP       | Dimension name of String type: vip              |
| dimensions.0.value | vip              | Load balancer VIP       | Specific IP address, such as 111.111.111.11        |
| dimensions.1.name  | vpcId            | ID of the VPC, in which the load balancer resides | Dimension name of String type: vpcId            |
| dimensions.1.value | vpcId            | ID of the VPC, in which the load balancer resides | Specific VPC ID, such as 1111                |
| dimensions.2.name  | loadBalancerPort | Load balancer port        | Dimension name of String type: loadBalancerPort |
| dimensions.2.value | loadBalancerPort | Load balancer port        | Specific port number, such as 80                     |
| dimensions.3.name  | protocol         | Protocol            | Dimension name of String type: protocol         |
| dimensions.3.value | protocol         | Protocol            | String type, such as http                |
| dimensions.4.name  | lanIp            | IP of the machine bound to the load balancer   | Dimension name of String type: lanIp            |
| dimensions.4.value | lanIp            | IP of the machine bound to the load balancer   | Specific IP address, such as 111.111.111.11        |
| dimensions.5.name  | Port             | Port number of the machine bound to the load balancer  | Dimension name of String type: port             |
| dimensions.5.value | Port             | Port number of the machine bound to the load balancer  | Specific port number, such as 80                     |

### 2.2 Metric Name

| Metric name (metricName) | Description    | Unit   |
| ---------------- | ----- | ---- |
| connum           | Number of current connections | -    |
| new_conn         | Number of new connections | -    |
| intraffic        | Inbound traffic   | Mbps |
| outtraffic       | Outbound traffic   | Mbps |
| inpkg            | Inbound packets   | Packets/sec  |
| outpkg           | Outbound packets   | Packets/sec  |


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
| -507 | Limit is exceeded       | OperationDenied.ExceedLimit          |
| -509 | Incorrect dimension group | InvalidParameter.DimensionGroupError |
| -513 | DB operation failed  | InternalError.DBoperationFail        |

## 5. Example

Input

<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<a href="/doc/api/405/公共请求参数" title="Common Request Parameters">Common Request Parameters</a>
&namespace=qce/lb_public
&metricName=intraffic
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
&startTime=2016-06-28 14:10:00
&endTime=2016-06-28 14:20:00
</pre>

Output

```
{
	"code": 0,
	"message": "",
	"metricName": "intraffic",
	"startTime": "2016-06-28 14:10:00",
	"endTime": "2016-06-28 14:20:00",
	"period": 300,
	"dataPoints": [
		5.6,
		6.5
		7.7
	]
}
```

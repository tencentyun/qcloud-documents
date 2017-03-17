## 1. API Description

GetMonitorData is used to obtain monitoring data of the cloud load balancer. You can obtain appropriate monitoring data based on the namespace of the cloud load balancer, object dimension description and monitor metrics specified by the user.

Domain for API access: monitor.api.qcloud.com

## 2. Request Parameters
   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is GetMonitorData.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> namespace
<td> Yes
<td> String
<td> Namespace. Every cloud product has a namespace. The namespace corresponding to the cloud load balancer is qce/lb.
<tr>
<td> metricName
<td> Yes
<td> String
<td> Metric name.
<tr>
<td> dimensions.n.name
<td> Yes
<td> String
<td> Dimension name. The dimension structure of each namespace is different. For more information on dimension APIs, please see the table below. Using it with dimensions.n.value.
<tr>
<td> dimensions.n.value
<td> Yes
<td> String
<td> Dimension value.
<tr>
<td> startTime
<td> No
<td> Datetime
<td> Start time, such as "2016-01-01 10:25:00".  The default is "00:00:00" of the current day.
<tr>
<td> endTime
<td> No
<td> Datetime
<td> End time. The default is the current time.  endTime shall be no later than startTime; It is recommended to set endTime and startTime on the same day.
<tr>
<td> period
<td> No
<td> Int
<td> Statistical period for monitoring. Currently, the time granularity for monitoring is 300s (5 minutes) only.
</tbody></table>

**Table of dimension names:**

| Dimension | Description |
|---------|---------|
| protocol | Protocol |
|  vip | VIP of cloud load balancer |
|  vport | Port of cloud load balancer |
| rsip| IP of backend server |
| rsport| Port of backend server |
| vpcid | VPC ID |

**Available values of metricName**
<table class="t"><tbody><tr>
<th><b>Metric Name</b></th>
<th><b>Description</b></th>
<th><b>Unit</b></th>
<th><b>Dimension</b></th>
<tr>
<td> pvv_connum
<td> Number of active connections (aggregated by protocol, vip and vport)
<td> count
<td> protocol, vip, vport
<tr>
<td> pvv_inactive_conn
<td> Number of inactive connections (aggregated by protocol, vip and vport)
<td> count
<td>  protocol, vip, vport
<tr>
<td> pvv_inpkg
<td> Number of inbound packages (aggregated by protocol, vip and vport)
<td> count/s
<td> protocol, vip, vport
<tr>
<td> pvv_intraffic
<td> Number of inbound traffic (aggregated by protocol, vip and vport)
<td> bps
<td> protocol, vip, vport
<tr>
<td> pvv_new_conn
<td> Number of new connections (aggregated by protocol, vip and vport)
<td> count
<td> protocol, vip, vport
<tr>
<td> pvv_outpkg
<td> Number of outbound packages (aggregated by protocol, vip and vport)
<td> count/s
<td> protocol, vip, vport
<tr>
<td> pvv_outtraffic
<td> Number of outbound traffic (aggregated by protocol, vip and vport)
<td> bps
<td> protocol, vip, vport
</tbody></table>

<table class="t"><tbody><tr>
<th><b>Metric Name</b></th>
<th><b>Description</b></th>
<th><b>Unit</b></th>
<th><b>Dimension</b></th>
<tr>
<td> rrv_connum
<td> Number of active connections (aggregated by rsip, vpcid and rsport)
<td> count
<td> rsip, vpcid, rsport
<tr>
<td> rrv_inactive_conn
<td> Number of inactive connections (aggregated by rsip, vpcid and rsport)
<td> count
<td>  rsip, vpcid, rsport
<tr>
<td> rrv_inpkg
<td> Number of inbound packages (aggregated by rsip, vpcid and rsport)
<td> count/s
<td> rsip, vpcid, rsport
<tr>
<td> rrv_intraffic
<td> Number of inbound traffic (aggregated by rsip, vpcid and rsport)
<td> bps
<td> rsip, vpcid, rsport
<tr>
<td> rrv_new_conn
<td> Number of new connections (aggregated by rsip, vpcid and rsport)
<td> count
<td> rsip, vpcid, rsport
<tr>
<td> rrv_outpkg
<td> Number of outbound packages (aggregated by rsip, vpcid and rsport)
<td> count/s
<td> rsip, vpcid, rsport
<tr>
<td> rrv_outtraffic
<td> Number of outbound traffic (aggregated by rsip, vpcid and rsport)
<td> bps
<td> rsip, vpcid, rsport
</tbody></table>

<table class="t"><tbody><tr>
<th><b>Metric Name</b></th>
<th><b>Description</b></th>
<th><b>Unit</b></th>
<th><b>Dimension</b></th>
<tr>
<td> rv_connum
<td> Number of active connections (aggregated by rsip and vpcid)
<td> count
<td> rsip, vpcid
<tr>
<td> rv_inactive_conn
<td> Number of inactive connections (aggregated by rsip and vpcid)
<td> count
<td>  rsip, vpcid
<tr>
<td> rv_inpkg
<td> Number of inbound packages (aggregated by rsip and vpcid)
<td> count/s
<td> rsip, vpcid
<tr>
<td> rv_intraffic
<td> Number of inbound traffic (aggregated by rsip and vpcid)
<td> bps
<td> rsip, vpcid
<tr>
<td> rv_new_conn
<td> Number of new connections (aggregated by rsip and vpcid)
<td> count
<td> rsip, vpcid
<tr>
<td> rv_outpkg
<td> Number of outbound packages (aggregated by rsip and vpcid)
<td> count/s
<td> rsip, vpcid
<tr>
<td> rv_outtraffic
<td> Number of outbound traffic (aggregated by rsip and vpcid)
<td> bps
<td> rsip, vpcid
</tbody></table>



## 3. Response Parameters

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://www.qcloud.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common request parameters">Common Error Codes</a> on the Error Code page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> startTime
<td> Datetime
<td> Start time.
<tr>
<td> endTime
<td> Datetime
<td> End Time.
<tr>
<td> metricName
<td> String
<td> Metric name.
<tr>
<td> period
<td> Int
<td> Statistical period for monitoring.
<tr>
<td> dataPoints
<td> Object
<td> Monitoring data list. Each element of the array is the monitoring point data.
</tbody></table>




## 4. Example
Input
<pre>
 
https://monitor.api.qcloud.com/v2/index.php?Action=GetMonitorData
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&namespace=qce/lb
&metricName=pvv_inactive_conn
&dimensions.0.name=protocol
&dimensions.0.value=HTTP
&dimensions.1.name=vip
&dimensions.1.value=111.111.111.111
&dimensions.2.name=vport
&dimensions.2.value=80
&startTime=2015-12-28 14:00:00
&endTime=2015-12-28 14:05:00
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "metricName": "pvv_inactive_conn",
    "startTime": "2015-12-28 14:00:00",
    "endTime": "2015-12-28 14:05:00",
    "period": 300,
    "dataPoints":  [
           0
        ]
}
```

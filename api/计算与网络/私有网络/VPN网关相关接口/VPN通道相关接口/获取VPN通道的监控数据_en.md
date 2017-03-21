## 1. API Description

This API (DescribeVpnConnMonitor) is used to obtain the monitoring data of VPN channel.
Domain for API request:<font style="color:red">vpc.api.qcloud.com</font> 

 

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. See the<a href="/doc/api/372/4153" title="Common request parameters"> Common Request Parameters</a> page for details. The Action field for this API is DescribeVpnConnMonitor.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | yes | string | Virtual private cloud ID, which can be vpcId or unVpcId. unVpcId is recommended. For example: vpc-03vihbk9. Can be queried via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>.  | 
| vpnGwId | Yes | String | VPN gateway ID assigned by the system, which can be vpnGwId or unVpnGwId. unVpnGwId is recommended. For example: vpngw-dystbrkv. Can be queried via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E7%BD%91%E5%85%B3%E5%88%97%E8%A1%A8" title="DescribeVpnGw">DescribeVpnGw</a>.  |
| vpnConnId | Yes | String | VPN channel ID assigned by the system, which can be vpnConnId or unVpnConnId. unVpnConnId is recommended. For example: vpnx-ol6bcqp0. Can be queried via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E9%80%9A%E9%81%93%E5%88%97%E8%A1%A8" title="DescribeVpnConn">DescribeVpnConn</a>.  |  
| metricName | Yes | String | Monitor metric name (currently only two metrics are supported: "outtraffic" for outbound traffic of public network, "intraffic" for inbound traffic of public network) |
| starttime | No | datetime | Start time. If left blank, it will be this time yesterday by default. The time span cannot be more than 2 days. If it's more than 2 days, the start time will be set to the end time minus 2 days, for example 2016-07-06 12:00:00 |
| endtime | No | datetime | End time. If left blank, it will be the present time by default. 2016-07-07 12:00:00 |
 

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded; other values: Failed |
| message |  String | Error message |
| data.data | Array  | Channel metric traffic/bandwidth, unit: bps. Recorded every 5 minutes.  Example: data[1] means a channel metric traffic/bandwidth of (starttime+5) ~ (starttime+10) minutes. The returned result will be outbound traffic when metricName is set to outtraffic and inbound traffic when it is set to intraffic |

## 4. Error Code Table
 The API does not have a business error code. For common error codes, refer to <a href="https://www.qcloud.com/doc/api/245/%e7%a7%81%e6%9c%89%e7%bd%91%e7%bb%9c%e9%94%99%e8%af%af%e7%a0%81?viewType=preview" title="VPC Error Codes for details">VPC Error Codes.</a>

## 5. Example
 
Input
<pre>
https://domain/v2/index.php?Action=DescribeVpnConnMonitor
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&vpcId=7
&vpnGwId=8
&vpnConnId=5
&metricName=outtraffic
&starttime=2015-07-14 00:00:00
&endtime=2015-07-14 23:00:00
</pre>

Output
```

{
    "code" : 0,
    "message" : "ok",
    "data" : [
		1221,
		1212,
		787
	],
}




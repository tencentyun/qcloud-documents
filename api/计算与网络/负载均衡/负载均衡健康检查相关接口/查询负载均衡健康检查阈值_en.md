## 1. API Description

  DescribeLBHealth is used to query the related parameters of default health check for cloud load balancer instances.
 
Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
  
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalanceId
<td> Yes
<td> string
<td> The ID of the cloud load balancer instance, which can be loadBalancerId or unLoadBalancerId (recommended). You can query it via the API <a href="https://www.qcloud.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>.
</tbody></table>
 

## 3. Response Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://www.qcloud.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common request parameters">Common Error Code</a> in the Error Code page.
<tr>
<td> msg
<td> string
<td> Module error message description depending on API.
<tr>
<td> data
<td> array
<td> Returned data
</tbody></table>
Data structure
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> appId
<td> int
<td> Application ID.
<tr>
<td> projectId
<td> int
<td> Project ID.
<tr>
<td> LBName
<td> string
<td> Name of the cloud load balancer instance.
<tr>
<td> health
<td> array
<td> Health threshold data.
</tbody></table>
health structure
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> switch
<td> int
<td>Switch of health check. 1: On; 0: Off; Default: On.
<tr>
<td> timeOut
<td> int
<td>Timeout. Response time of CVM port. An integer between 2-60 seconds.
<tr>
<td> intervalTime
<td> int
<td>Check interval. The interval (in seconds) between CVM port checks. An integer between 5-300 seconds.
<tr>
<td> healthNum
<td> int
<td>Healthy threshold. Indicate the number of consecutive successful health checks for the health check result changing from fail to success (an integer between 2-10).
<tr>
<td> unhealthNum
<td> int
<td>Unhealthy threshold. Indicate the number of consecutive failed health checks for the health check result changing from success to fail (an integer between 2-10).
</tbody></table>
 

## 4. Example
 
Input:
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeLBHealth
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&loadBalanceId=lb-abcdefgh
</pre>
Output:
```
{
"code":0,
"msg":"ok",
"data":
	[
		{
			"appId":1351000042,
			"projectId":0,
			"LBName":"20_1",
			"health":
			{
				"switch":1,
				"timeOut":2,
				"intervalTime":5,
				"healthNum":2,
				"unhealthNum":2,
				"status":1
			}
		}
	]
}
```



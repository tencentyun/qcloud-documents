## 1. API Description
 
 ModifyLBHealth is used to modify the parameters of default health check for cloud load balancer instances. When the API is called, the health check parameters for all listeners of the cloud load balancer instances will be modified to the input parameters entered by the user. Health check attributes (On/Off; modify the 4 fields of health check: timeOut, intervalTime, healthNum and unhealthNum).
 
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
<td> ID of the cloud load balancer instance, which can be loadBalancerId or unLoadBalancerId (recommended). You can query it via the API <a href="https://cloud.tencent.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>.
<tr>
<td> switch
<td> Yes
<td> int
<td> Switch of health check. 1: On; 0: Off.
<tr>
<td> timeOut
<td> Yes
<td> int
<td> Timeout. Response time of CVM port. An integer between 2-60 seconds. Note: The value shall be less than that specified in intervalTime.
<tr>
<td> intervalTime
<td> Yes
<td> int
<td> Check interval. The interval (in seconds) between CVM port checks. An integer between 5-300 seconds. The value in timeOut shall be less than that specified in intervalTime.
<tr>
<td> healthNum
<td>Yes
<td> int
<td> Healthy threshold. Indicate the number of consecutive successful health checks for the health check result changing from fail to success (an integer between 2-10).
<tr>
<td> unhealthNum
<td>Yes
<td> int
<td> Unhealthy threshold. Indicate the number of consecutive failed health checks for the health check result changing from success to fail (an integer between 2-10).
</tbody></table>

 

## 3. Response Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> int
<td> Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://cloud.tencent.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common request parameters">Common Error Codes</a> on the Error Code page.
<tr>
<td> msg
<td> string
<td> Module error message description depending on API.
<tr>
<td> data
<td> array
<td> Returned array.
</tbody></table>
Data structure
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> taskId
<td> int
<td> Request task ID. The API is a asynchronous task, and can be called based on this parameter
<a href="/doc/api/244/4007">DescribeLoadBalancersTaskResult</a> is used to query the result of task operation.
</tbody></table>
 

## 4. Example
 
Input:
<pre>`https://domain/v2/index.php?Action=ModifyLBHealth`
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&loadBalanceId=lb-abcdefgh
&switch=1
&timeOut=20
&intervalTime=5
&healthNum=3
</pre>
Output:
```
{
    "code" : 0,
    "message" : "",
    "data":{
          "taskId":12
      }
}

```



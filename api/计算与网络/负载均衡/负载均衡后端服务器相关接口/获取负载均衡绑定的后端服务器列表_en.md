## 1. API Description
 DescribeLoadBalancerBackends API is used to query the list of CVMs bound to the CLB instance by the instance ID.
 
 Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is DescribeLoadBalancerBackends.

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerId
<td> Yes
<td> String
<td>  ID of the cloud load balancer instance, which can be loadBalancerId or unLoadBalancerId (recommended). You can query it via the API <a href="https://www.qcloud.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>.
<tr>
<td> offset
<td> No
<td> Int
<td> Data offset, default is 0.
<tr>
<td> limit
<td> No
<td> Int
<td> Length of returned data. Default is 20, maximum is 100.
</tbody></table>

 

## 3. Response Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common request parameters">Common Error Codes</a> on the Error Code page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> totalCount
<td> Int
<td> Return the total number of CVMs bound to this cloud load balancer instance.
<tr>
<td> backendSet
<td> Array
<td> Returned backend server array.
</tbody></table>

</b></th>backendSet array structure:</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> instanceId
<td> String
<td> CVM instance ID.
<tr>
<td> unInstanceId
<td> String
<td> CVM instance ID, can be used in any operations in place of instanceId. It is recommended to use this ID.
<tr>
<td> weight
<td> Int
<td> Weight of the CVM.
<tr>
<td> instanceName
<td> String
<td> Name of the CVM.
<tr>
<td> lanIp
<td> String
<td> Private IP of the CVM.
<tr>
<td> wanIpSet
<td> Array
<td> Public IP of the CVM.
<tr>
<td> instanceStatus
<td> Int
<td> Status of the CVM<br>1: Malfunction, 2: Running, 3: Creating, 4: Off, 5: Returned, 6: Returning, 7: Rebooting, 8: Booting, 9: Shutting Down, 10: Resetting Password, 11: Formatting, 12: Creating Image, 13: Configuring Bandwidth, 14: Re-installing System, 19: Upgrading, 21: Hot-Migrating.
</tbody></table>

 

## 4. Example
 
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&loadbancerId=lb-abcdefgh
</pre>
Output
```
{
  "code" : 0,
  "message" : "",
  "totalCount" : 2,
  "backendSet":[
  {
    "instanceId" : "qcvm2ed56d3399a1b92f31cf0891fdba700b",
    "unInstanceId" : "ins-123test1",
    "instanceName" : "my-backend-name1",
    "weight" : 10,
    "lanIp" : "10.10.10.1",
    "wanIpSet":["203.195.179.123"],
    "instanceStatus" : 2
  },
  {
    "instanceId" : "qcvm1ed56d3399a1b92f31cf0891fdba700b",
    "unInstanceId" : "ins-123test2",
    "instanceName" : "my-backend-name2",
    "weight" : 10,
    "lanIp" : "10.10.10.2",
    "wanIpSet":["203.195.179.124"],
    "instanceStatus" : 2
  }]
}

```




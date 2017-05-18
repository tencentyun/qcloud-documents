## 1. API Description
 DescribeLoadBalancersByInstances provides the ability to query cloud load balancer listeners associated with the CVM. The private IP or name of the CVM can be used for querying. You can specify the number of returned cloud load balancer instances. Default: 20.
 
Domain for API access: lb.api.qcloud.com
 

## 2. Request Parameters
  The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is DescribeLoadBalancersByInstances.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> backendIps.n
<td> No
<td> String
<td> Private IP of the CVM.
<tr>
<td> backendInstanceName
<td> No
<td> String
<td> Name of the CVM.
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
<td> Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://www.qcloud.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common request parameters">Common Error Codes</a> on the Error Code page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> totalCount
<td> Int
<td> The total number of cloud load balancer instances matching the filter criteria.
<tr>
<td> loadBalancerSet
<td> Array
<td> The returned array of the cloud load balancer instance. The data structure is as follows.
</tbody></table>

</b></th>loadBalancerSet structure</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerId
<td> String
<td> The unique ID of the cloud load balancer instance.
<tr>
<td> unLoadBalancerId
<td> String
<td> The unified unique ID of the cloud load balancer instance.
<tr>
<td> loadBalancerName
<td> String
<td> Name of the cloud load balancer instance.
<tr>
<td> loadBalancerType
<td> Int
<td> Type of the cloud load balancer instance <br>1: public network (without daily rate) 2: public network (with daily rate) 3: private network.
<tr>
<td> domain
<td> String
<td> Domain of the cloud load balancer instance. (This field is not applicable to the cloud load balancer instances of private network.)
<tr>
<td> loadBalancerVips
<td> Array
<td> VIP list of the cloud load balancer instance.
<tr>
<td> status
<td> Int
<td> Status of the cloud load balancer instance, <br>0: creating, 1: running. 
<tr>
<td> createTime
<td> String
<td> Creation time of the cloud load balancer instance.
<tr>
<td> sessionExpire
<td> Int
<td> Indicate whether to enable session persistence feature for the cloud load balancer instance. 0 means disabled; others means enabled and the value here is the session duration. Session persistence feature is not applicable to the cloud load balancer instances of private network.
<tr>
<td> instanceId
<td> String
<td> CVM ID.
<tr>
<td> unInstanceId
<td> String
<td> Unified ID of CVM. You can query it by calling <a href="http://www.qcloud.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeInstances">DescribeInstances</a>.
<tr>
<td> instanceName
<td> String
<td> Name of the CVM.
<tr>
<td> backendLanIp
<td> String
<td> Private IP of the CVM.
<tr>
<td> backendWanIpSet
<td> Array
<td> Public IP of the CVM.
<tr>
<td> vpcId
<td> Int
<td> The numerical digits of VPC ID. 0: basic network; others: VPC.
<tr>
<td> subnetId
<td> Int
<td> The numerical digits of the subnet ID.
<tr>
<td> projectId
<td> Int
<td> Project ID.
</tbody></table>

 

## 4. Example
 
Use the default parameters to query the cloud load balancer instances:
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeLoadBalancersByInstances
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
</pre>
Output
```
{
  "code" : 0,
  "message" : "",
  "totalCount" : 1,
  "loadBalancerSet":[
  {
    "loadBalancerId" : "my-lb-id1",
    "unLoadBalancerId" : "lb-abcdefgh",
    "loadBalancerName" : "my-lb-name1",
    "loadBalancerType" : 2,
    "domain" : "LB607.clb.myqcloud.com",
    "loadBalancerVips":["203.195.179.123"],
    "createTime" : "2014-07-29 15:08:39",
    "status" : 1,
    "sessionExpire" : 0,
    "instanceId" : "qcvm1234",
    "unInstanceId" : "ins-12345678",
    "instanceName" : "my-backend-name1",
    "backendLanIp" : "10.4.3.45",
    "backendWanIpSet" : ["203.195.192.91"],
	"vpcId" : 0,
	"subnetId" :0,
	"projectId" : 0
  }
  ]
}

```




## 1. API Description
 DescribeLoadBalancers is used to get the user's list of cloud load balancer instances. The cloud load balancer instance matching the criteria will be returned based on the parameters you entered. The name, type, and public VIP of the cloud load balancer instance can be entered for filtering. If no parameter is entered, all cloud load balancer instances in the account will be returned.
 
Domain for API access: lb.api.qcloud.com


## 2. Request Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is DescribeLoadBalancers.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerIds.n
<td> No
<td> String
<td> The unique ID of the cloud load balancer instance. This can be loadBalancerId or unLoadBalancerId (recommended).
<tr>
<td> loadBalancerType
<td> No
<td> Int
<td> Type of the cloud load balancer instance <br>1: public network (without daily rate) 2: public network (with daily rate) 3: private network.
<tr>
<td> loadBalancerName
<td> No
<td> String
<td> Name of the cloud load balancer instance.
<tr>
<td> domain
<td> No
<td> String
<td> Domain of the cloud load balancer instance. Naming rule: 1-60 characters, including English letters (in lowercase), numbers, "." or "-". This field is not applicable to the cloud load balancer of private network.
<tr>
<td> loadBalancerVips.n
<td> No
<td> String
<td> VIP address of the cloud load balancer instance. You may enter multiple addresses.
<tr>
<td> backendWanIps.n
<td> No
<td> String
<td> Public IP of the backend CVM.
<tr>
<td> offset
<td> No
<td> Int
<td> Data offset, default is 0.
<tr>
<td> limit
<td> No
<td> Int
<td> Length of returned data. Default: 20.
<tr>
<td> orderBy
<td> No
<td> String
<td> Sorting field, which can be:
loadBalancerName, createTime, domain and loadBalancerType.
<tr>
<td> orderType
<td> No
<td> Int
<td>  1: Backward sequence; 0: Forward sequence. The default is backward sequence.
<tr>
<td> searchKey
<td> No
<td> String
<td> Search field: name, domain, and VIP (fuzzy match).
<tr>
<td> projectId
<td> No
<td> Int
<td>The project ID of the cloud load balancer instance.　You can query it via <a href="/doc/api/403/4400">DescribeProject</a>.
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
<td> The returned array of the cloud load balancer instance.
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
<td> Domain of the cloud load balancer instance. There is no domain for cloud load balancer instances of private network.
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
<td> statusTime
<td> String
<td> Time of the last status change of the cloud load balancer instance.
<tr>
<td> projectId
<td> Int
<td> The project ID of the cloud load balancer instance. 0: default project.
<tr>
<td> vpcId
<td> Int
<td> The numerical digits of VPC ID. 0: basic network.
<tr>
<td> subnetId
<td> Int
<td> The numerical digits of VPC subnet ID. 0: default subnet.
</tbody></table>

 

## 4. Example
 
Use the default parameters to query the list of cloud load balancer instances:
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeLoadBalancers
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output
```

{
  "code" : 0,
  "message" : "",
  "totalCount" : 2,
  "loadBalancerSet":[
  {
    "loadBalancerId" : "my-lb-id1",
    "unLoadBalancerId" : "lb-abcdefgh",
    "loadBalancerName" : "my-lb-name1",
    "loadBalancerType" : 2,
    "domain" : "LB607.clb.myqcloud.com",
    "loadBalancerVips":["203.195.179.123"],
    "createTime" : "2014-07-29 15:08:39",
    "statusTime" : "2014-08-29 15:08:39",
    "status" : 1,
    "sessionExpire" : 0
  },
  {
    "loadBalancerId" : "my-lb-id2",
    "unLoadBalancerId" : "lb-xxxxx2",
    "loadBalancerName" : "my-lb-name2",
    "loadBalancerType" : 2,
    "domain" : "LB608.clb.myqcloud.com",
    "loadBalancerVips":["203.195.179.124"],
    "createTime" : "2014-07-29 15:08:39",
    "statusTime" : "2014-08-29 15:08:39",
    "status" : 1,
    "sessionExpire" : 1000,
    "projectId":0,
    "vpcId":0,
    "subnetId":0
  }]
}

```




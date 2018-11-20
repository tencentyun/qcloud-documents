## API Description
This API (DescribeLoadBalancerBackends) is used to view the list of CVMs bound to the load balancer instance backend according to the instance ID.
 
 Domain for API access: `lb.api.qcloud.com`

## Request Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is DescribeLoadBalancerBackends.

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerId
<td> Yes
<td> String
<td> ID of the load balancer instance, which can be queried via the API <a href="https://cloud.tencent.com/document/api/214/1261" title="DescribeLoadBalancers">DescribeLoadBalancers</a>.
</tbody></table>

 

## Response Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Successful; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> codeDesc
<td> String
<td> Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned.
<tr>
<td> totalCount
<td> Int
<td> Return the total number of CVMs bound to this load balancer instance.
<tr>
<td> backendSet
<td> Array
<td> Returned backend server array.
</tbody></table>

</b></th> backendSet is composed as follows: </b></th>
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
<td> CVM instance ID, which can be used in any operations in place of instanceId. It is recommended to use this ID.
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
<td> Status of the CVM <br>1: Malfunction, 2: Running, 3: Creating, 4: Off, 5: Returned, 6: Returning, 7: Rebooting, 8: Booting, 9: Shutting Down, 10: Resetting Password, 11: Formatting, 12: Creating Image, 13: Configuring Bandwidth, 14: Re-installing System, 19: Upgrading, 21: Hot-Migrating.
</tbody></table>

 

## Example
 
Request
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeLoadBalancerBackends
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerId=lb-byhpduqt
</pre>
Response
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "totalCount": 1,
    "backendSet": [
        {
            "instanceId": "qcvmed9e93b0bb2784b043c983761e624639",
            "unInstanceId": "ins-9o9ex9s0",
            "instanceName": "test_k8s_1",
            "lanIp": "10.104.222.152",
            "wanIpSet": [
                "193.112.93.144"
            ],
            "instanceStatus": 4,
            "weight": 44
        }
    ]
}

```


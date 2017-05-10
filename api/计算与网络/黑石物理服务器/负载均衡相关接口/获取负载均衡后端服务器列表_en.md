## 1. API Description
 
This API (DescribeBmLoadBalancerBackends) is used to query the backend CPM list of a BM load balancer instance.

Domain for API request: <font style="color:red">lb.api.qcloud.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. For additional parameters, see [Common Request Parameters](/doc/api/456/6718) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String | ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/doc/api/456/6658). |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please see [Common Error Codes](/doc/api/456/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |
| data | Array | Returned array. |
| totalCount | Int | Total number of CPMs bound to the BM load balancer instance. |
| backendSet | Array | An arrary of returned CPMs. |

Parameter backendSet contains the following fields

| Parameter Name | Type | Description |
|---------|---------|---------|
| instanceId | String | ID of CPM. |
| instanceName | String | User-defined name of the CPM. |
| lanIp | String | Private IP of the CPM. |
| wanIpSet | Array | Public IP list of the CPM. |
| instanceStatus | Int | CPM status. 1: Running, 2: Shutting down, 3: Off, 4: Shutdown failed, 5: Booting, 6: Booting failed, 7: Rebooting, 8: Reboot failed, 9: Re-installing system, 10: Reinstallation failed, 11: Resetting password, 12: Binding EIP, 13: Unbinding EIP |
| weight | Int | Weight of the CPM. |


Module Error Code

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| 11041 | InvalidParameter.CCDBLBNotExist | Record of this BM load balancer does not exist in CCDB |

## 4. Example
 
Input

<pre>
	https://domain/v2/index.php?
	Action=DescribeBmLoadBalancerBackends
	&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
	&loadBalancerId=lb-abcdefgh
</pre>
Output

```
{
  "code": 0,
  "message": "",
  "codeDesc": "Success",
  "data": [],
  "totalCount": 1,
  "backendSet": [
    {
      "instanceId": "cpm-abcdefgh",
      "instanceName": "CPM",
      "lanIp": "10.0.0.1",
      "wanIpSet": [
        "115.115.115.115"
      ],
      "instanceStatus": "1",
      "weight": 10
    }
  ]
}

```

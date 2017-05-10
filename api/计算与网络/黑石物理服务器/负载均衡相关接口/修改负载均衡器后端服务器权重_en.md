## 1. API Description
 
This API (ModifyBmLoadBalancerBackends) is used to modify the weight of backend CPMs for BM load balancer instances.

Domain for API request: <font style="color:red">lb.api.qcloud.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. For additional parameters, see [Common Request Parameters](/doc/api/456/6718) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String | ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/doc/api/456/6658).  |
| backends.n.instanceId | Yes | String | An array of CPM IDs ( n represents the array subscript).  |
| backends.n.weight | is | Int | An array of weights of bound CPMs (n represents the array subscript). Value range is 0-100 (default is 10).  |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please see [Common Error Codes](/doc/api/456/6725) in the Error Codes page.  |
| message | String | Module error message description depending on API.  |
| codeDesc | String | Error code message description.  |
| requestId | Int | Task ID. This API is an asynchronous task. You can query task operation result by calling API [DescribeBmLoadBalancersTaskResult](/doc/api/456/6666) based on this parameter |


Module Error Code

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| 9824 | InvalidParameter.VpcIdNotConsistent | vpcId of CPM is not consistent with that of the BM load balancer |
| 10005 | InvalidParameter.InstanceWrongInfo | Incorrect information or status of CPM |
| 11041 | InvalidParameter.CCDBLBNotExist | Record of this BM load balancer does not exist in CCDB |
| 12003 | IncorrectStatus.LBWrongStatus | The operation is impossible due to incorrect status of BM load balancer |

## 4. Example
 
Input

<pre>
	https://domain/v2/index.php?
	Action=ModifyBmLoadBalancerBackends
	&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
	&loadBalancerId=lb-abcdefgh
	&backends.1.instanceId=cpm-6789test
	&backends.1.weight=10
	&backends.2.instanceId=cpm-1234test
	&backends.2.weight=6
</pre>
Output

```
{
  "code" : 0,
  "message" : "",
  "codeDesc": "Success",
  "requestId" : 1234
}

```

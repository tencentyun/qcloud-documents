## 1. API Description
 
This API (DescribeBmLoadBalancerListeners) is used to acquire the listener list of BM load balancer instances.

Domain for API request: <font style="color:red">lb.api.qcloud.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. For additional parameters, see [Common Request Parameters](/doc/api/456/6718) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String | ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/doc/api/456/6658). |
| listenerIds | No | Array | Listener ID array, described using listenerIds.n and can be queried by using the [DescribeBmLoadBalancerListeners](/doc/api/456/6657) API. |
| protocol | No | Int | Protocol type of listener. 2: TCP. |
| loadBalancerPort | No | Int | Listener port. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please see [Common Error Codes](/doc/api/456/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |
| listenerSet | Array | Listener information array. |
| totalCount | Int | Number of listeners in the listenerSet array. |

listenerSet is an array that is used to describe the information of listeners under the current load balancer instance. It includes the following fields

| Parameter Name | Type | Description |
|---------|---------|---------|
| loadBalancerPort | Int | Listening port of the BM load balancer listener. Value range: 1-65535. |
| instancePort | Int | Backend CPM listening port of BM load balancer instance listener. Value range: 1-65535. |
| protocol | Int | Protocol type of BM load balancer instance listener. 2: TCP |
| status | Int | BM load balancer listener status. 1: normal, other values: abnormal. |
| bandwidth | Int | Used to specify the maximum bandwidth of the listener with the billing mode is pay-by-fixed bandwidth. Value range: 0-1000 (in Mbps). |
| listenerName | String | User-defined listener name. |
| listenerId | String | Listener ID. |
| sessionExpire | Int | Session duration. Unit: second |
| healthSwitch | Int | Indicate whether Health Check is enabled: 1 (On) and 0 (Off). |
| timeOut | Int | Response timeout. Unit: second. |
| intervalTime | Int | Health check time interval. Unit: second |
| healthNum | Int | Health threshold of BM load balancer listener. Default value is 3, which means the forwarding is considered normal if it is detected to be healthy for three times consecutively. Value range: 2-10; unit: count. |
| unhealthNum | Int | Unhealth threshold of BM load balancer listener. Default value is 3, which means the forwarding is considered abnormal if it is detected to be unhealthy for three times consecutively. Value range: 2-10; unit: count. ||


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
	Action=DescribeBmLoadBalancerListeners
	&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
	&loadBalancerId=lb-abcdefgh
	&listenerIds.1=lbl-abcdefgh
</pre>
Output

```
{
  "code": 0,
  "message": "",
  "codeDesc": "Success",
  "listenerSet": [
    {
      "loadBalancerPort": 1234,
      "instancePort": 1234,
      "protocol": 2,
      "status": 1,
      "bandwidth": 0,
      "listenerName": "listenerName",
      "listenerId": "lbl-abcdefgh",
      "sessionExpire": 900,
      "healthSwitch": 0,
      "timeOut": 2,
      "intervalTime": 5,
      "healthNum": 3,
      "unhealthNum": 3
    },
  "totalCount": 1
}

```

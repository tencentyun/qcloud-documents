## 1. API Description
 
This API (DescribeBmListeners) is used to acquire BM load balancer layer-4 listeners.

Domain for API request: bmlb.api.qcloud.com


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalancerId | Yes | String |  ID of the BM load balancer instance, which can be queried via API [DescribeBmLoadBalancers](/document/product/386/9306). |
| listenerIds.n | No | Array | Layer-4 listener ID array, which can be queried via API [DescribeBmListeners](/document/product/386/9296). |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed For more information, please see [Common Error Codes](/document/product/386/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |
| listenerSet | Array | Listener information array. |
| totalCount | Int | Number of listeners in the listenerSet array. |

listenerSet is an array that is used to describe the information of listeners under the current BM load balancer instance. It includes the following fields

| Parameter Name | Type | Description |
|---------|---------|---------|
| listenerId | String | Listener ID. |
| listenerName | String | User-defined listener name. |
| protocol | String | Protocol type of BM load balancer instance listener. Value can be TCP or UDP. |
| loadBalancerPort | Int | Listening port of the BM load balancer listener. Value range: 1-65535. |
| bandwidth | Int | Used to specify the maximum bandwidth of the listener with the billing mode is pay-by-fixed bandwidth. Value range: 0-1000 (in Mbps). |
| listenerType | String | Listener type: L4Listener (layer-4 listener) or L7Listener (layer-7 listener). |
| sessionExpire | Int | Session duration (in sec) |
| healthSwitch | Int | Indicate whether Health Check is enabled: 1 (On) and 0 (Off). |
| timeOut | Int | Response timeout (in sec). |
| intervalTime | Int | Health check time interval (in sec). |
| healthNum | Int | Health threshold of BM load balancer listener. Default value is 3, which means the forwarding is considered normal if it is detected to be healthy for three times consecutively. Value range: 2-10; unit: count. |
| unhealthNum | Int | Unhealth threshold of BM load balancer listener. Default value is 3, which means the forwarding is considered abnormal if it is detected to be unhealthy for three times consecutively. Value range: 2-10; unit: count. |
| status | Int | Current status of the listener. 0: Creating; 1: Running; 2: Creation failed; 3: Deleting; 4: Deletion failed. |
| addTimestamp | String | Creation time stamp. |


Module Error Codes

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| 11041 | InvalidParameter.CCDBLBNotExist | Record of this BM load balancer does not exist in CCDB |

## 4. Examples
 
Input

<pre>
https://domain/v2/index.php?Action=DescribeBmListeners
&<<a href="https://cloud.tencent.com/document/product/386/6718">Public Request Parameters</a>>
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
            "listenerId": "lbl-abcdefgh",
            "listenerName": "test-tcp",
            "protocol": "tcp",
            "loadBalancerPort": 1234,
            "bandwidth": 0,
            "listenerType": "L4Listener",
            "sessionExpire": 900,
            "healthSwitch": 1,
            "timeOut": 2,
            "intervalTime": 5,
            "healthNum": 3,
            "unhealthNum": 3,
            "status": 1,
            "addTimestamp": "2017-04-19 22:07:11"
        }
    ],
    "totalCount": 1
}

```

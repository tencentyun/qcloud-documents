## 1. API Description
 
This API (DescribeBmLBHealthStatus) is used to query the health status of BM load balancer instances.

Domain for API request: <font style="color:red">lb.api.qcloud.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. For additional parameters, see [Common Request Parameters](/doc/api/456/6718) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| loadBalanceId | Yes | String | ID of BM load balancer instance, which can be queried via API [DescribeBmLoadBalancer](/doc/api/456/6658). |
| listenerId | No | String | Listener ID, which can be queried via API [DescribeBmLoadBalancerListeners](/doc/api/456/6657). |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, please see [Common Error Codes](/doc/api/456/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |
| Data | Obj | Returned object. |

data is a json object that is used to describe the health status information of listeners under the current BM load balancer instance. It includes the following fields

| Parameter Name | Type | Description |
|---------|---------|---------|
| LoadBalanceId in the input parameters| Array | Health status information of listeners under the BM load balancer instance. |

The array contains the following fields


| Parameter Name | Type | Description |
|---------|---------|---------|
| ip | String | Private IP of the CPM. |
| protocol | String | Protocol. |
| port | Int | Port of the CPM. |
| vport | Int | Listening port of the BM load balancer | |
| healthStatus | Int | Health check result. 1: healthy; 0: unhealthy; -1: incomplete target. |


Module Error Code

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| 11060 | InternalError.TGWAbnormal | TGW service error |
| 12012 | InvalidResource.NotExist | The BM load balancer instance does not exist |

## 4. Example
 
Input

<pre>
	https://domain/v2/index.php?
	Action=DescribeBmLBHealthStatus
	&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
	&loadBalanceId=lb-abcdefgh
</pre>
Output

```
{
  "code": 0,
  "message": "",
  "codeDesc": "Success",
  "data": {
    "lb-abcdefgh": [
      {
        "ip": "",
        "protocol": "tcp",
        "port": 1234,
        "vport": 1234,
        "healthStatus": -1
      },
      {
        "ip": "",
        "protocol": "tcp",
        "port": 2345,
        "vport": 2345,
        "healthStatus": -1
      }
    ]
  }
}

```

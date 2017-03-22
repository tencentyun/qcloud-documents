## 1. API Description
 ModifyLoadBalancerListener is used to modify the attributes of cloud load balancer listeners.
 
Domain for API access: lb.api.qcloud.com


## 2. Request Parameters

   The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is ModifyLoadBalancerListener.
 
| Parameter Name | Required | Type | Description |
|-----|------|--------|-----------|
| loadBalancerId | Yes | String | The ID of the cloud load balancer instance, which can be loadBalancerId or unLoadBalancerId (recommended). You can query it via the API <a href="https://www.qcloud.com/doc/api/244/%E6%9F%A5%E8%AF%A2%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeLoadBalancers">DescribeLoadBalancers</a>. |
| listenerId | Yes | String | ID of the cloud load balancer listener. You can query it via the API<a href="https://www.qcloud.com/doc/api/244/%E8%8E%B7%E5%8F%96%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%E7%9B%91%E5%90%AC%E5%99%A8%E5%88%97%E8%A1%A8" title=" DescribeLoadBalancerListeners"> DescribeLoadBalancerListeners</a>. |
| listenerName | No | String | Listener name. |
| sessionExpire | No | Int | Session duration. 0 means disabled. <br>Value range for listeners with TCP or UDP protocols on public network (with daily rate): 900-3600; value range for listeners with HTTP protocols on public network (without daily rate): 900-3600; <br>value range for listeners with HTTP or HTTPS protocols on public network (with daily rate): 30-3600; <br>Not supported for private network cloud load balancers. |
| healthSwitch | No | Int | Indicate whether to enable Health Check: 1 (On) and 0 (Off). |
| timeOut | No | Int | Response timeout. Value range: 2-60 seconds; <br>Response timeout of listeners with HTTP or HTTPS protocols on public network (with daily rate) cannot be set currently. The default is 5 seconds. |
| intervalTime | No | Int | Check interval. Value range: 5-300. The default is 5. |
| healthNum | No | Int | Healthy threshold. Value range: 2-10. |
| unhealthNum | Int | Unhealthy threshold | Value range: 2-10. |
| httpHash | No | Int | Forwarding methods of cloud load balancer listeners. This field is only supported for HTTP or HTTPS listeners on the public network with daily rate. Available values: wrr (weighted round robin), <br>ip_hash (IP_HASH). Default is wrr. |
| httpCode | No | Int | For HTTP and HTTPS listeners, this returned status code is used to determine the health status. Value range: 1-31. The default is 31. <br>1: it is considered healthy if the health check returns 1xx code; 2: it is considered healthy if the health check returns 2xx code; 4: it is considered healthy if the health check returns 3xx code; 8: it is considered healthy if the health check returns 4xx code; 16: it is considered healthy if the health check returns 5xx code. If there are multiple codes that can show the health status, enter the accumulated value corresponding to such codes. |
| httpCheckPath | No | String | The health check path for HTTP and HTTPS listeners. By default, it must start with /. |
| SSLMode | No | String | Authentication type of HTTPS listeners. Unidirectional: unidirectional authentication; mutual: mutual authentication. |
| certId | No | String | New server certificate ID of HTTPS listeners. |
| certCaId | No | String | New client certificate ID of HTTPS listeners. |
| certCaContent | No | String | New client certificate content of HTTPS listeners. |
| certCaName | No | String | New client certificate name of HTTPS listeners. |
| certContent | No | String | New server certificate content of HTTPS listeners. |
| certKey | No | String | New server certificate key of HTTPS listeners. |
| certName | No | String | New server certificate name of HTTPS listeners. |

## 3. Response Parameters
 
 
| Parameter Name | Type | Description |
|-------|---|---------------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to [Common Error Code](/doc/api/244/1530) in the Error Code page. |
| message | String | Module error message description depending on API. |
| requestId | Int | Request task ID. You can query the operation status through API [DescribeLoadBalancersTaskResult](/doc/api/244/4007). |

## 4. Example
 
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=ModifyLoadBalancerListener
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
loadBalancerId=lb-ltkip4do
&listenerId=lbl-6hkiqc6c
&SSLMode=unidirectional
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 18642
}

```




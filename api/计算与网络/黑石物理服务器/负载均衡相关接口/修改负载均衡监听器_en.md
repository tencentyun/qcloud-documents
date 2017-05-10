## 1. API Description
 This API (ModifyBmLoadBalancerListener) is used to modify the attributes of BM load balancer listeners.

Domain: lb.api.qcloud.com

## 2. Request Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, see [Common Request Parameters](/doc/api/456/6718) page. The Action field for this API is ModifyBmLoadBalancerListener.
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerId
<td> Yes
<td> String
<td> ID of BM load balancer instance, which can be queried via API <a href="/doc/api/456/6658" title="DescribeLoadBalancers">DescribeBmLoadBalancers</a>.

<tr>
<td> listenerId
<td> Yes
<td> String
<td> Listener ID. You can query these IDs by using the <a href="/doc/api/456/6657" title="DescribeLoadBalancers">DescribeBmLoadBalancerListeners</a> API.
<tr>
<td> listenerName
<td> No
<td> String
<td> Listener name.

<tr>
<td> sessionExpire
<td> No
<td> Int
<td> Session duration. 0 means disabled. Available value range for TCP protocol listeners: 900-3600.

<tr>
<td> healthSwitch
<td> No
<td> Int
<td> Indicate whether to enable Health Check for BM load balancer instance listeners: 1 (On) and 0 (Off). Default is 1 (On).

<tr>
<td> timeOut
<td> No
<td> Int
<td> Health check response timeout for BM load balancer listeners (in second). Value range: 2-60. Default is 2. The response timeout must be smaller than health check time interval.

<tr>
<td> intervalTime
<td> No
<td> Int
<td> Health check time interval forBM load balancer listeners. Default value: 5; value range: 5-300; unit: second.

<tr>
<td> healthNum
<td> No
<td> Int
<td> Health threshold for BM load balancer listeners. Default value is 3. The forwarding is considered normal if it is detected to be healthy for [healthNum] times consecutively. Value range: 2-10; unit: count.

<tr>
<td> unhealthNum
<td> No
<td> Int
<td> Unhealth threshold for BM load balancer listeners. Default value is 3. The forwarding is considered abnormal if it is detected to be unhealthy for [unhealthNum] times consecutively. Value range: 2-10; unit: count.

<tr>
<td> bandwidth
<td> No
<td> Int
<td> Used to specify the maximum bandwidth of the listener when the billing mode is pay-by-fixed bandwidth. Value range: 0-1000 (in Mbps).

</tbody></table>

## 3. Output Parameters
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href="/doc/api/456/6725" title="Common Error Codes">Common Error Codes</a> on the Error Codes page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> requestId
<td> int
<td> Request task ID. The API is an asynchronous task.
<a href="/doc/api/456/6666">You can query task operation result by calling the DescribeBmLoadBalancerListeners</a> API, based on this parameter.
</tbody></table>

Module Error Code

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |

## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=ModifyBmLoadBalancerListener
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerId=lb-aaaa
&listenerId=lbl-bbbbb
&listenerName=hh
&healthSwitch=1
&timeOut=6
&intervalTime=10
&healthNum=8
&unhealthNum=8
&sessionExpire=1000
&bandwidth=5
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 2376368
}
```



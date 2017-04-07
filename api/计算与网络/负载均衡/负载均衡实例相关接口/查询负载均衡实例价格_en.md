## 1. API Description
 
InquiryLBPrice is used to query the price of the cloud load balancer instance. For more information on prices of cloud load balancer instances, please refer to [Price Overview](/doc/product/214/价格总览) from product instructions.

Domain for API access:  lb.api.qcloud.com


## 2. Request Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](/doc/api/244/4183). The Action field for this API is InquiryLBPrice.

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerType <td> Yes <td> int <td> Type of the cloud load balancer instance. <br>1: public network (without daily rate) 2: public network (with daily rate) 3: private network.
</tbody></table>

 

## 3. Response Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>

<tr>
<td> code <td> Int <td> Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href="https://www.qcloud.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common request parameters">Common Error Codes</a> on the Error Code page.
<tr>
<td> message <td> String <td> Module error message description depending on API.
<tr>
<td> price <td> Int <td> Price for the cloud load balancer instance, "RMB 0.01/day".
</tbody></table>

 

## 4. Example
 
Query the price of the cloud load balancer instance on public network (with daily rate):
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=InquiryLBPrice
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerType=2
</pre>
The returned correct output of the request:
```
{
    "code": 0,
    "message": "",
    "price": 100
}
```



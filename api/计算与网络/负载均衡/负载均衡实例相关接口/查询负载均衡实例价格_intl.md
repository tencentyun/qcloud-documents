### API Description
 
This API (InquiryLBPrice) is used to query the price of load balancer instance. For more information, please see [Price Overview](https://cloud.tencent.com/document/product/214/1149).

Domain name for API access: `lb.api.qcloud.com`


## Request Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/api/214/4183) page. The Action field for this API is InquiryLBPrice.

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerType <td> Yes <td> Int <td> Type of the load balancer instance.<br> 2: Public network-based; 3: Private network-based.
</tbody></table>

 

## Response Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>

<tr>
<td> code <td> Int <td> Common error code. 0: Successful; other values: Failed. For more information, please see <a href="https://cloud.tencent.com/doc/api/244/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="Common Error Codes">Common Error Codes</a> on the Error Codes page.
<tr>
<td> message <td> String <td> Module error message description depending on API.
<tr>
<td> codeDesc
<td> String
<td> Error code. For a successful operation, "Success" is returned. For a failed operation, a message describing the failure is returned.
<tr>
<td> price <td> Int <td> Price of the load balancer instance (in 0.01 CNY/hr).
</tbody></table>

 

## Example
 
Query the price of a public-based load balancer instance.
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=InquiryLBPrice
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerType=2
</pre>
The returned correct output of the request:
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "price": 2
}
```



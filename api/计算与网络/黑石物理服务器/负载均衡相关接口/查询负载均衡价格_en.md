## 1. API Description
 This API (InquiryBmLBPrice) is used to query the price of BM load balancers. The price for public network-based load balancer is 1 CNY per day, and private network-based load balancer is free of charge. > Note: When purchasing public network-based load balancer instance, a balance of 30 CNY will be frozen (monthly cost). Please make sure you have sufficient balance under your account. When you stop the use of BM load balance service in advance, the corresponding charges will be deducted from the frozen balance based on actual usage period, and the remaining balance will be returned to the account.

Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, see [Common Request Parameters](/doc/api/456/6718) page. The Action field for this API is InquiryBmLBPrice.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerType
<td> Yes
<td> Int
<td> Type of BM load balancer. Value can be 2 or 3. 2 indicates public network; 3 indicates private network.
</tbody></table>

## 3. Response Parameters
 
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
<td> price
<td> Int
<td>Price of the BM load balancer instance (in 0.01 CNY/day).
</tbody></table>

Module Error Code

| Error Code | Error Message | Error Description |
|------|------| --------|
| 9009 | InternalError.TradeError | Incorrect request billing API |
| 100001 | InvalidParameter | Incorrect parameter |
| 100004 | OperationDenied.NoPermission | The operation is not supported |
| 500008 | TradeError.QueryPriceError | Price query failed |
| 700104 | TradeError.GoodsConfigInvalid | Failed to obtain commodity configuration |
| 700108 | TradeError.GoodsCodeInvalid | Invalid commodity ID |
| 700102 | TradeError.CheckGoodsError | Service parameter verification failed |

## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=InquiryBmLBPrice
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&loadBalancerType=2
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "price": 100
}
```



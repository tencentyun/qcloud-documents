## 1. API Description
 This API (InquiryBmLBPrice) is used to query the prices of BM load balancers. The price for public network-based load balancer is 1 CNY per day, and private network-based load balancer is free of charge. 
> Note: For the purchase of public network-based load balancer instance, a balance of 30 CNY will be frozen (monthly fee). Please make sure you have sufficient balance under your account. When you stop the use of load balance service before the expiration date, the fee will be deducted from the frozen balance based on actual usage period, and the remaining balance will be returned to the account.

Domain for API access: lb.api.qcloud.com

## 2. Request Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](/document/product/386/6718). The Action field for this API is InquiryBmLBPrice.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> loadBalancerType
<td> Yes
<td> String
<td> Type of load balancer. Value can be open or internal. "open" represents public network (with daily rate), and "internal" represents private network.
</tbody></table>

## 3. Response Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Successful; other values: Failed. For more information, please see <a href="/document/product/386/6725" title="Common Error Codes">Common Error Codes</a> on the Error Codes page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> price
<td> Int
<td>Price of the BM load balancer instance (in 0.01 CNY/day).
</tbody></table>

Module Error Codes

| Error Code | Error Message | Error Description |
|------|------| --------|
| 9009 | InternalError.TradeError | Error occurred while requesting billing API |
| 100001 | InvalidParameter | Invalid parameter |
| 100004 | OperationDenied.NoPermission | The operation is not supported |
| 500008 | TradeError.QueryPriceError | Price query failed |
| 700104 | TradeError.GoodsConfigInvalid | Failed to obtain goods configuration |
| 700108 | TradeError.GoodsCodeInvalid | Invalid goods ID |
| 700102 | TradeError.CheckGoodsError | Service parameter verification failed |

## 4. Example
Input
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=InquiryBmLBPrice
&<<a href="https://www.qcloud.com/document/product/386/6718">Public Request Parameters</a>>
&loadBalancerType=open
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



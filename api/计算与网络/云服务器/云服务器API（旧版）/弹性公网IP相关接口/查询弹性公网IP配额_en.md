## 1. API Description
 
Domain name: eip.api.qcloud.com
API name: DescribeEipQuota

This API is used to query the quota on EIPs for a specified region.

 

## 2. Input Parameters
 

<table class="t"><tbody><tr>
<th>Parameter Name</th>
<th>Required</th>
<th>Type</th>
<th>Description</th>
<tr>
<th>null</th>
<th>-</th>
<th>-</th>
<th>-</th>
</tbody></table>

 

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| data | Array | Returned data structure|

Data structure

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> data.eipNumQuota <td> Int <td> Total quota on the number of EIPs that can be requested.
<tr>
<td> data.currentEipNum <td> Int <td> Current number of EIPs
<tr>
<td> data.dailyApplyQuota <td> Int <td> Daily quota on the number of requests for EIPs
<tr>
<td> data.dailyApplyCount <td> Int <td> Number of requests for EIPs on current day
<tr>
<td> data.dailyAllocWanIpQuota <td> Int <td> Daily quota on the operations to reallocate an ordinary public IP when an EIP is unbound
<tr>
<td> data.dailyAllocWanIpCount <td> Int <td> Number of operations to reallocate an ordinary public IP when an EIP is unbound on current day
</tbody></table>

 

## 4. Example
 
Input
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>>

</pre>

Output
```

{
    "code": 0,
    "message": "",
    "data": {
        "eipNumQuota": 20,
        "currentEipNum": 2,
        "dailyApplyQuota": 10,
        "dailyApplyCount": 7,
        "dailyAllocWanIpQuota": 10,
        "dailyAllocWanIpCount": 2    
    }
}

```


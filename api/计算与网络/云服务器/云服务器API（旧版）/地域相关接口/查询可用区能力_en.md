## 1. API Description
This API (DescribeZoneAbility) is used to query the capacities of availability zones, including [Cloud Block Storage](https://cloud.tencent.com/document/product/439/6329) and [Virtual Private Cloud](https://cloud.tencent.com/doc/product/215/535).

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>


## 2. Input Parameters

The following list only provides request parameters for this API. For other parameters, refer to [Common Request Parameters](/document/api/213/6976).
 
| Name | Required | Type | Description |
|---------|---------|---------|---------|
| zoneId| Yes | Int| Availability zone ID.
| capacity.n| Yes | String | The capacity to query. Query for CBS and VPC capacities is supported currently (This API allows passing multiple IDs at a time. For the format of this parameter, refer to `id.n` section in [API Introduction](https://cloud.tencent.com/doc/api/229/568)).


## 3. Output Parameters
 
| Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81). |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81). |
| capacitySet | Array | Return the list of information on capacities. |


capacitySet is a collection of information on capacities. The data structure of information on a capacity is as follows:

| Name | Type | Description |
|---------|---------|---------|
| capacity | Array | Capacity item.
| isSupported | Int | Supported or not; 0: Not supported; 1: Supported.

## 4. Example
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=DescribeZoneAbility
  &zoneId=800001
  &capacity.1=cbs
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output

```
{
    "code" : 0,
    "message" : "",
    "capacitySet" : [
        {
            "isSupported" : 1,
            "capacity" : [
                "cbs"
            ]
        }
    ]
}
```






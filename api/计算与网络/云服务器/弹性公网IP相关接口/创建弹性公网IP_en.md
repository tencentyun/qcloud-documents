## 1. API Description
 
Domain name: eip.api.qcloud.com
API name: CreateEip

Create an elastic public IP (EIP), a static IP address designed for dynamic cloud computing. With EIP, you can quickly remap the EIP to another instance, shielding off the instance failures.
Your EIP is associated with a Tencent Cloud account, instead of an instance, until you choose to explicitly release it or your payment is more than 7 days overdue.
* The platform imposes quotas on number of EIPs that a user can request for each region. Please refer to [Overview of EIP Products](/doc/product/213/1941). The above quotas can be obtained through [DescribeEipQuota](/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E9%85%8D%E9%A2%9D) API.


## 2. Input Parameters
 


| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| goodsNum | No | Int | Number of EIPs that can be requested at a time (The default is 1, and the maximum is 5)


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| data | Array | Return a list |

Data structure


| Parameter Name | Type | Description |
|---------|---------|---------|
| data.eipIds | Array |List of EIP instance IDs created

## 4. Example
 
Input

```
 https://eip.api.qcloud.com/v2/index.php?
 &<<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>>
```

Output

```

{
    "code": 0,
    "message": "",
    "data": {
        "eipIds": [
            "eip-m44ku5d2"
        ]
    }
}

```


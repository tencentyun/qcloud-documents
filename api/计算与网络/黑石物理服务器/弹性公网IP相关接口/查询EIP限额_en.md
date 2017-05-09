## 1. API Description
This API (DescribeEipBmQuota) is used to query the quota of EIPs in use. By default, a single customer can request a maximum of 100 EIPs.
 
Domain: <font style="color:red">eip.api.qcloud.com</font>


## 2. Input Parameters
 
| Parameter Name | Required | Type | Description |
|-------|----|---|----|----|
| None | - | - | - |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725).  |
| message | String | Error message |
| data | Array | Return the quota information. For more information on its composition, please see below |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---|---|---|
| data.eipNumQuota | Int | Total quota on the number of EIPs that can be requested. | 
| Data.currentEipNum | Int | Number of EIPs in use, which is the total number of EIPs in the statues of "creating", "binding", "bound", "unbinding", and "unbound" | 
| data.dailyApplyQuota | Int | Daily quota on the number of requests for EIPs 
| data.dailyApplyCount | Int | Number of requests for EIPs on current day | 

## 4. Error Codes
| Error Code | Error Message | Error Description |
|---|---|---|
| 9006 | InternalErr | An error occurred with internal data operation |

## 5. Example
 
Input
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &Action=DescribeEipBmQuota
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
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



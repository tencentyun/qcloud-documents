## 1. API Description
This API (EipBmApply) is used to create a BM EIP.
 
Domain: bmeip.api.qcloud.com


## 2. Input Parameters
 
| Parameter Name | Required | Type | Description |
|-------|----|---|----|----|
| goodsNum | No | Int | Number of the EIPs to be created. Default is 1, and maximum is 20 |
| payMode | No | String | Billing mode of the EIP to be created. "flow": Bill by Traffic; "bandwidth": Bill by Bandwidth (in MB) |
| bandwidth | No | Int | The capped bandwidth selected if EIP is billed by bandwidth (in MB; maximum is 1000 MB) |
| vpcId | Yes | Int | ID of the VPC to which the requested EIP belongs |

 > The platform imposes quotas on number of EIPs that a user can request for each region. The above quota can be obtained via the API [DescribeEipBmQuota](/doc/api/456/6668).

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725).  |
| message | String | Error message |
| data | Array | Return the asynchronous task information of the requested EIP instance. For more information on its composition, please see below |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---|---|---|
| data.eipIds | Array | Return the list of EIP instance IDs being requested |
| data.requestId | Int | ID of asynchronous task for binding to CPM. The task status can be queried via API [EipBmQueryTask](/document/product/386/6670) |

## 4. Error Codes
| Error Code | Error Message | Error Description |
|---|---|---|
| 9003 | ParamInvalid | Incorrect request parameter |
| 9006 | InternalErr | An error occurred with internal data operation |
| 30001 | ExceedTheLimit | The total number of requested EIP exceeds the quota |
| 30003 | ExceedDailyLimit | The number of requested EIPs on current day exceeds the daily quota |
| 30016 | ISPInvalid | Invalid ISP |


## 5. Example
 
Input
```

  https://bmeip.api.qcloud.com/v2/index.php?
  &Action=EipBmApply
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>&goodsNum=2&payMode=flow&vpcId=1
```

Output
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "eipIds": [
            "eip-qcloudv5"
        ],
        "requestId": 2382031
    }
}

```



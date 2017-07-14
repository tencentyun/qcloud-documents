## 1. API Description
This API (EipBmModifyCharge) is used to modify the billing mode of EIPs. There are two available billing modes. You can use this API to modify your billing mode based on your business scenario. After the modification, the request for changing billing mode will take effect in the next billing period (each hour is counted as a billing period).
 
Domain: <font style="color:red">eip.api.qcloud.com</font>


## 2. Input Parameters
 
| Parameter Name | Required | Type | Description |
|-------|----|---|----|----|
| eipIds.n | No | Array | List of EIP instance IDs, with the subscripts starting with 0. It can be queried via API [DescribeEipBm](/doc/api/456/6671) |
| payMode | Yes | String | Billing mode of EIP. "flow": Bill by Traffic; "bandwidth": Bill by Bandwidth |
| bandwidth | No | Int | Upper limit of bandwidth (in MB) .The field is only available when the billing mode is "Bill by Bandwidth". Default is 1, and minimum is 0.


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725).  |
| message | String | Error message |
| data | Array | Return asynchronous task ID. For more information on its composition, please see below |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---|---|---|
| data.requestId | Int | ID of asynchronous task for binding to CPM. The task status can be queried via API [EipBmQueryTask](/doc/api/456/6670) |

## 4. Error Codes
| Error Code | Error Message | Error Description |
|---|---|---|
| 9003 | ParamInvalid | Incorrect request parameter |
| 9006 | InternalErr | An error occurred with internal data operation |
| 30016 | ISPInvalid | Invalid ISP |

## 5. Example
 
Input
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &Action=EipBmModifyCharge
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>&eipIds.0=eip-test&payMode=bandwidth&bandwidth=40
</pre>

Output
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": 2383050
    }
}
```



## 1. API Description
This API (EipBmUnbindRs) is used to unbind an EIP from a CPM. After the EIP is unbound, inactivity fee will still be charged for it, so please [release and clean up](/document/product/386/6676) it in a timely manner .
 
Domain: <font style="color:red">bmeip.api.qcloud.com</font>
 

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|-------|----|---|----|----|
| eipId | No | String | EIP instance ID |
| instanceId | No | String | CPM Instance ID, which can be obtained from the "instanceID" in the returned fields of API [DescribeDevice](/doc/api/456/6728) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725).  |
| message | String | Error message |
| data | Array | Return asynchronous task information. For more information on its composition, please see below |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---|---|---|
| data.requestId | Int | ID of asynchronous task for binding to CPM. The task status can be queried via API [EipBmQueryTask](/document/product/386/6670) |

## 4. Error Codes
| Error Code | Error Message | Error Description |
|---|---|---|
| 9003 | ParamInvalid | Incorrect request parameter |
| 9006 | InternalErr | An error occurred with internal data operation |
| 9032 | InternalCgwErr | Internal API error |
| 30009 | EipNotExist | The EIP does not exist |
| 30010 | EipStateCannotOp | The EIP is not allowed to be unbound under current status |

## 5. Example
 
Input
<pre>

  https://bmeip.api.qcloud.com/v2/index.php?
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &Action=EipBmUnbindRs
  &instanceId=cpm-xxxxxx&eipId=eip-vvvvvvv

</pre>

Output
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": 100000
    }
}

```



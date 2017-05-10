## 1. API Description
This API is used to bind BM EIP to a CPM.

Domain: <font style="color:red">eip.api.qcloud.com</font>
API name: EipBmBindRs


## 2. Input Parameters
 
| Parameter Name | Required | Type | Description |
|-------|----|---|----|----|
| eipId | Yes | String | EIP instance ID |
| instanceId | Yes | String | CPM instance ID, which can be obtained via the instanceId in the returned fields of API [DescribeDevice](/doc/api/456/6728) |

 > Currently, EIP is not allowed to be bound to a CPM that has been bound to an NAT gateway.

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725).  |
| message | String | Error message |
| data | Array | Return asynchronous task information |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---|---|---|
| data.requestId | Int | ID of asynchronous task for binding to CPM. The task status can be queried via API [EipBmQueryTask](/doc/api/456/6670) |

## 4. Error Codes
| Error Code | Error Message | Error Description |
|---|---|---|
| 9003 | ParamInvalid | Incorrect request parameter |
| 9006 | InternalErr | An error occurred with internal data operation |
| 30009 | EipNotExist | The EIP does not exist |
| 30010 | EipStateCannotOp | The EIP is not allowed to be bound under current status |
| 30012 | EipInArrears | The EIP is in arrears |
| 30017 | EipHasBindRs | The EIP has been bound to RS |
| 30021 | VpcIdNotMatch | VPCs of EIP and RS do not match |

## 5. Example
 
Input
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &Action=EipBmBindRs
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
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



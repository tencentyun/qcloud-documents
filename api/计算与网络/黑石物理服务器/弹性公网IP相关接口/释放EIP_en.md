## 1. API Description
This API (EipBmDelete) is used to release EPIs make it easier for users to clean up unused EIP resources.

Domain: <font style="color:red">eip.api.qcloud.com</font>


## 2. Input Parameters
 
| Parameter Name | Required | Type | Description |
|-------|----|---|----|----|
| eipIds.n | Yes | Array | List of EIP instance IDs, with the subscripts starting with 0. It can be queried via API [DescribeEipBm](/doc/api/456/6671) |

 > Only unbound EIPs can be released. Any bound EIP cannot be released.

## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725).  |
| message | String | Error message |
| data | Array | Return asynchronous task information. For more information on its composition, please see below |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---|---|---|
| data.requestId | Int | ID of asynchronous task for binding to CPM. The task status can be queried via API [EipBmQueryTask](/doc/api/456/6670) |

## 4. Error Codes
| Error Code | Error Message | Error Description |
|---|---|---|
| 9000 | InternalCgwErr | An error occurred with internal API |
| 9003 | ParamInvalid | Incorrect request parameter |
| 9006 | InternalErr | An error occurred with internal data operation |
| 30009 | EipNotExist | The EIP does not exist |
| 30010 | EipStateCannotOp | The EIP is not allowed to be released under current status |
| 30013 | EipRecordNotExist | EIP record does not exist |

## 5. Example
 
Input
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &Action=EipBmDelete
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>&eipIds.0=eip-iiiii
</pre>

Output
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": 2383049
    }
}

```



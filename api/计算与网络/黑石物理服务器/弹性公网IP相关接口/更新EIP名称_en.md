## 1. API Description
This API (ModifyEipAlias) is used to rename EIP. You can customize the requested EIP alias through this API for an easier management.
 
Domain: eip.api.qcloud.com




## 2. Input Parameters
 
| Parameter Name | Required | Type | Description |
|-------|----|---|----|----|
| eipId | Yes | String | EIP instance ID. It can be queried via API [DescribeEipBm](/doc/api/456/6671) |
| eipName | Yes | String | EIP name to be set. It should be a combination of letters, numbers, hyphen "-" or underscore "_".|


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725).  |
| message | String | Error message |


## 4. Error Codes
| Error Code | Error Message | Error Description |
|---|---|---|
| 9003 | ParamInvalid | Incorrect request parameter |
| 9006 | InternalErr | An error occurred with internal data operation |
| 30009 | EipNotExist | The EIP does not exist |

## 5. Example
 
Input
```

  https://eip.api.qcloud.com/v2/index.php?
  &Action=ModifyEipAlias
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>&eipId=eip-test&eipName=test
```

Output
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": []
}

```


